# file: project/youtube_dl/extractor/tvplay.py:236-335
# asked: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 285], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}
# gained: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}

import io

import pytest

from youtube_dl.compat import compat_HTTPError
from youtube_dl.extractor.tvplay import TVPlayIE
from youtube_dl.utils import ExtractorError, GeoRestrictedError


class _FakeDownloader(object):
    def __init__(self):
        self.params = {}

    def report_warning(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        pass

    def to_screen(self, *args, **kwargs):
        pass

    def to_stderr(self, *args, **kwargs):
        pass

    def trouble(self, *args, **kwargs):
        pass


def _make_extractor(monkeypatch, video, streams=None, streams_error=None):
    extractor = TVPlayIE()
    monkeypatch.setattr(extractor, '_downloader', _FakeDownloader())
    records = {
        'geo': [],
        'download_urls': [],
        'f4m': [],
        'm3u8': [],
    }

    def fake_match_id(url):
        return '12345'

    def fake_geo_bypass(context):
        records['geo'].append(context)

    def fake_download_json(url, video_id, note=None, *args, **kwargs):
        records['download_urls'].append(url)
        if '/stream/' in url:
            if streams_error is not None:
                raise streams_error
            return streams if streams is not None else {}
        return video

    def fake_f4m(url, video_id, f4m_id=None, fatal=False, **kwargs):
        records['f4m'].append((url, video_id, f4m_id, fatal))
        return [{'format_id': 'f4m-format', 'url': url, 'ext': 'f4m'}]

    def fake_m3u8(url, video_id, ext=None, entry_protocol=None, m3u8_id=None, fatal=False, **kwargs):
        records['m3u8'].append((url, video_id, ext, entry_protocol, m3u8_id, fatal))
        return [{'format_id': 'hls-format', 'url': url, 'ext': 'mp4'}]

    monkeypatch.setattr(extractor, '_match_id', fake_match_id)
    monkeypatch.setattr(extractor, '_initialize_geo_bypass', fake_geo_bypass)
    monkeypatch.setattr(extractor, '_download_json', fake_download_json)
    monkeypatch.setattr(extractor, '_extract_f4m_formats', fake_f4m)
    monkeypatch.setattr(extractor, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(extractor, '_sort_formats', lambda formats: None)
    return extractor, records


def test_full_extraction_all_format_types_and_sami_lang(monkeypatch):
    video = {
        'title': 'Full Title',
        'description': 'A description',
        'format_title': 'Series Name',
        'format_position': {'episode': '3', 'season': '2'},
        '_embedded': {'season': {'title': 'Season 2'}},
        'duration': '95',
        'created_at': '2020-01-02T03:04:05Z',
        'views': {'total': 999},
        'age_limit': '18',
        'sami_path': 'http://example.com/subs_lv.xml',
        'is_geo_blocked': False,
    }
    streams = {
        'streams': {
            'hds': 'http://example.com/video.f4m',
            'hls': 'http://example.com/video.m3u8',
            'medium': 'http://example.com/video.mp4',
            'high': 'rtmp://example.com/app/playpath123',
            'bad_rtmp': 'rtmpbad',
            'empty': None,
            'blank': '',
        }
    }
    extractor, records = _make_extractor(monkeypatch, video, streams)

    result = extractor._real_extract('http://tvplay.skaties.lv/shows/full-title/12345')

    assert records['geo'] == [{'countries': ['LV']}]
    assert records['download_urls'] == [
        'http://playapi.mtgx.tv/v3/videos/12345',
        'http://playapi.mtgx.tv/v3/videos/stream/12345',
    ]
    assert len(records['f4m']) == 1
    assert 'hdcore=3.5.0' in records['f4m'][0][0]
    assert 'plugin=aasp-3.5.0.151.81' in records['f4m'][0][0]
    assert records['f4m'][0][1:] == ('12345', 'hds', False)
    assert records['m3u8'] == [
        ('http://example.com/video.m3u8', '12345', 'mp4', 'm3u8_native', 'hls', False)
    ]
    assert result['id'] == '12345'
    assert result['title'] == 'Full Title'
    assert result['description'] == 'A description'
    assert result['series'] == 'Series Name'
    assert result['episode_number'] == 3
    assert result['season'] == 'Season 2'
    assert result['season_number'] == 2
    assert result['duration'] == 95
    assert result['timestamp'] == 1577934245
    assert result['view_count'] == 999
    assert result['age_limit'] == 18
    assert result['subtitles'] == {'lv': [{'url': 'http://example.com/subs_lv.xml'}]}
    assert [f['format_id'] for f in result['formats']] == [
        'f4m-format', 'hls-format', 'medium', 'high',
    ]
    assert result['formats'][2] == {
        'format_id': 'medium',
        'quality': 1,
        'ext': 'mp4',
        'url': 'http://example.com/video.mp4',
    }
    assert result['formats'][3] == {
        'format_id': 'high',
        'quality': 2,
        'ext': 'flv',
        'url': 'rtmp://example.com/app',
        'app': 'app',
        'play_path': 'playpath123',
        'preference': -1,
    }


def test_no_geo_country_minimal_video_and_no_subtitles(monkeypatch):
    video = {'title': 'Minimal'}
    streams = {'streams': {'medium': 'http://example.com/min.mp4'}}
    extractor, records = _make_extractor(monkeypatch, video, streams)

    result = extractor._real_extract('http://localhost/videos/12345')

    assert records['geo'] == []
    assert result == {
        'id': '12345',
        'title': 'Minimal',
        'description': None,
        'series': None,
        'episode_number': None,
        'season': None,
        'season_number': None,
        'duration': None,
        'timestamp': None,
        'view_count': None,
        'age_limit': 0,
        'formats': [{
            'format_id': 'medium',
            'quality': 1,
            'ext': 'mp4',
            'url': 'http://example.com/min.mp4',
        }],
        'subtitles': {},
    }


def test_subtitles_default_lang_from_url_and_missing_streams_key(monkeypatch):
    video = {
        'title': 'Default Lang',
        'sami_path': 'http://example.com/subs.xml',
    }
    extractor, records = _make_extractor(monkeypatch, video, streams={})

    result = extractor._real_extract('https://play.tv3.lt/programos/show/12345')

    assert records['geo'] == [{'countries': ['LT']}]
    assert result['formats'] == []
    assert result['subtitles'] == {'lt': [{'url': 'http://example.com/subs.xml'}]}


def test_geo_restricted_when_no_formats_and_geo_blocked(monkeypatch):
    video = {'title': 'Blocked', 'is_geo_blocked': True}
    streams = {'streams': {'medium': None, 'high': ''}}
    extractor, records = _make_extractor(monkeypatch, video, streams)

    with pytest.raises(GeoRestrictedError) as exc_info:
        extractor._real_extract('http://tvplay.skaties.lv/shows/blocked/12345')

    assert 'might not be available in your country' in str(exc_info.value)
    assert records['geo'] == [{'countries': ['LV']}]


def test_streams_403_http_error_converted_to_expected_error(monkeypatch):
    http_error = compat_HTTPError(
        'http://playapi.mtgx.tv/v3/videos/stream/12345',
        403,
        'Forbidden',
        {},
        io.BytesIO(b'{"msg": "Access denied in your region"}'),
    )
    streams_error = ExtractorError('Download failed', cause=http_error)
    extractor, records = _make_extractor(
        monkeypatch, {'title': 'Forbidden'}, streams_error=streams_error)

    with pytest.raises(ExtractorError) as exc_info:
        extractor._real_extract('http://tvplay.skaties.lv/shows/forbidden/12345')

    assert 'Access denied in your region' in str(exc_info.value)
    assert exc_info.value is not streams_error
    assert records['download_urls'] == [
        'http://playapi.mtgx.tv/v3/videos/12345',
        'http://playapi.mtgx.tv/v3/videos/stream/12345',
    ]


def test_streams_non_403_http_error_is_reraised(monkeypatch):
    http_error = compat_HTTPError(
        'http://playapi.mtgx.tv/v3/videos/stream/12345',
        500,
        'Internal Server Error',
        {},
        io.BytesIO(b'{"msg": "Server error"}'),
    )
    streams_error = ExtractorError('Original stream failure', cause=http_error)
    extractor, _records = _make_extractor(
        monkeypatch, {'title': 'Server Error'}, streams_error=streams_error)

    with pytest.raises(ExtractorError) as exc_info:
        extractor._real_extract('http://tvplay.skaties.lv/shows/error/12345')

    assert exc_info.value is streams_error
    assert 'Original stream failure' in str(exc_info.value)


def test_streams_extractor_error_without_http_cause_is_reraised(monkeypatch):
    streams_error = ExtractorError('Plain stream failure')
    extractor, _records = _make_extractor(
        monkeypatch, {'title': 'Plain Error'}, streams_error=streams_error)

    with pytest.raises(ExtractorError) as exc_info:
        extractor._real_extract('http://tvplay.skaties.lv/shows/error/12345')

    assert exc_info.value is streams_error
    assert 'Plain stream failure' in str(exc_info.value)

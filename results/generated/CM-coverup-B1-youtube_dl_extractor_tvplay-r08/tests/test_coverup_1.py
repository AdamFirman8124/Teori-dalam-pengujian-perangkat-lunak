# file: project/youtube_dl/extractor/tvplay.py:236-335
# asked: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 285], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}
# gained: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 285], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}

import io

import pytest

from youtube_dl import YoutubeDL
from youtube_dl.compat import compat_HTTPError, compat_urlparse
from youtube_dl.extractor.tvplay import TVPlayIE
from youtube_dl.utils import ExtractorError, GeoRestrictedError, parse_iso8601


GEO_URL = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
NO_GEO_URL = 'mtg:418113'


@pytest.fixture
def ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True})
    extractor = TVPlayIE(ydl)
    try:
        yield extractor
    finally:
        getattr(ydl, 'close', lambda: None)()


def _make_download_json(video, streams=None, error=None):
    calls = []

    def fake_download_json(url, video_id, note=None, *args, **kwargs):
        calls.append((url, video_id, note))
        if '/stream/' in url:
            if error is not None:
                raise error
            return streams
        return video

    return fake_download_json, calls


def test_real_extract_all_format_types_and_metadata(ie, monkeypatch):
    video = {
        'title': 'Test Title',
        'description': 'Test description',
        'format_title': 'Test Series',
        'format_position': {'episode': '3', 'season': '2'},
        '_embedded': {'season': {'title': 'Season 2'}},
        'duration': '125',
        'created_at': '2014-07-23T00:30:56+00:00',
        'views': {'total': 42},
        'age_limit': '18',
        'sami_path': 'http://example.com/subtitles/sub_en.xml',
    }
    streams = {
        'streams': {
            'hls': 'http://example.com/master.m3u8',
            'hds': 'http://example.com/manifest.f4m',
            'rtmp': 'rtmp://example.com/app/playpath',
            'badrtmp': 'rtmp://example.com/app',
            'medium': 'http://example.com/video.mp4',
            'high': None,
            'empty': '',
        }
    }

    fake_download_json, calls = _make_download_json(video, streams)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)

    geo_calls = []
    monkeypatch.setattr(
        ie, '_initialize_geo_bypass',
        lambda geo_bypass_context=None: geo_calls.append(geo_bypass_context))

    f4m_calls = []
    m3u8_calls = []

    def fake_f4m(manifest_url, video_id, **kwargs):
        f4m_calls.append((manifest_url, video_id, kwargs))
        return [{'url': 'http://example.com/f4m', 'ext': 'mp4', 'format_id': 'hds-1'}]

    def fake_m3u8(*args, **kwargs):
        m3u8_calls.append((args, kwargs))
        return [{'url': 'http://example.com/hls', 'ext': 'mp4', 'format_id': 'hls-1'}]

    monkeypatch.setattr(ie, '_extract_f4m_formats', fake_f4m)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)

    info = ie._real_extract(GEO_URL)

    # geo bypass was initialized from the URL's country code
    assert geo_calls == [{'countries': ['LV']}]

    # both JSON endpoints were requested with the right ids
    assert calls[0] == (
        'http://playapi.mtgx.tv/v3/videos/418113', '418113', 'Downloading video JSON')
    assert calls[1] == (
        'http://playapi.mtgx.tv/v3/videos/stream/418113', '418113', 'Downloading streams JSON')

    # f4m manifest got the hdcore/plugin query and the right kwargs
    assert len(f4m_calls) == 1
    f4m_url, f4m_video_id, f4m_kwargs = f4m_calls[0]
    parsed = compat_urlparse.urlparse(f4m_url)
    assert parsed.path == '/manifest.f4m'
    assert compat_urlparse.parse_qs(parsed.query) == {
        'hdcore': ['3.5.0'],
        'plugin': ['aasp-3.5.0.151.81'],
    }
    assert f4m_video_id == '418113'
    assert f4m_kwargs == {'f4m_id': 'hds', 'fatal': False}

    # m3u8 manifest got the expected positional/keyword arguments
    assert len(m3u8_calls) == 1
    assert m3u8_calls[0][0] == (
        'http://example.com/master.m3u8', '418113', 'mp4', 'm3u8_native')
    assert m3u8_calls[0][1] == {'m3u8_id': 'hls', 'fatal': False}

    formats = {f['format_id']: f for f in info['formats']}
    assert set(formats) == {'hls-1', 'hds-1', 'rtmp', 'medium'}
    assert formats['rtmp'] == {
        'format_id': 'rtmp',
        'quality': -1,
        'ext': 'flv',
        'url': 'rtmp://example.com/app',
        'app': 'app',
        'play_path': 'playpath',
        'preference': -1,
    }
    assert formats['medium'] == {
        'format_id': 'medium',
        'quality': 1,
        'ext': 'mp4',
        'url': 'http://example.com/video.mp4',
    }

    assert info['id'] == '418113'
    assert info['title'] == 'Test Title'
    assert info['description'] == 'Test description'
    assert info['series'] == 'Test Series'
    assert info['episode_number'] == 3
    assert info['season'] == 'Season 2'
    assert info['season_number'] == 2
    assert info['duration'] == 125
    assert info['timestamp'] == parse_iso8601('2014-07-23T00:30:56+00:00')
    assert info['view_count'] == 42
    assert info['age_limit'] == 18
    assert info['subtitles'] == {
        'en': [{'url': 'http://example.com/subtitles/sub_en.xml'}],
    }


def test_real_extract_geo_blocked(ie, monkeypatch):
    video = {'title': 'Geo blocked', 'is_geo_blocked': True}
    fake_download_json, _ = _make_download_json(video, {'streams': {}})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda *a, **k: None)

    with pytest.raises(GeoRestrictedError) as excinfo:
        ie._real_extract(GEO_URL)

    assert 'copyright reasons' in str(excinfo.value)


def test_real_extract_403_raises_error_with_server_message(ie, monkeypatch):
    http_error = compat_HTTPError(
        'http://playapi.mtgx.tv/v3/videos/stream/418113', 403, 'Forbidden', {},
        io.BytesIO(b'{"msg": "This video is not available"}'))
    error = ExtractorError('Unable to download JSON metadata', cause=http_error)
    fake_download_json, _ = _make_download_json({'title': 'x'}, error=error)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda *a, **k: None)

    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(GEO_URL)

    # a NEW error is raised, carrying the message from the 403 response body
    assert excinfo.value is not error
    assert 'This video is not available' in str(excinfo.value)


def test_real_extract_http_error_not_403_is_reraised(ie, monkeypatch):
    http_error = compat_HTTPError(
        'http://playapi.mtgx.tv/v3/videos/stream/418113', 500, 'Server Error', {},
        io.BytesIO(b''))
    error = ExtractorError('Unable to download JSON metadata', cause=http_error)
    fake_download_json, _ = _make_download_json({'title': 'x'}, error=error)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda *a, **k: None)

    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(GEO_URL)

    assert excinfo.value is error


def test_real_extract_non_http_error_is_reraised(ie, monkeypatch):
    error = ExtractorError('Something else went wrong')
    fake_download_json, _ = _make_download_json({'title': 'x'}, error=error)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda *a, **k: None)

    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(GEO_URL)

    assert excinfo.value is error


def test_real_extract_no_geo_country_and_default_subtitle_lang(ie, monkeypatch):
    video = {
        'title': 'Minimal',
        'sami_path': 'http://example.com/subtitles/subtitle.xml',
    }
    streams = {'streams': {'high': 'http://example.com/video.mp4'}}
    fake_download_json, calls = _make_download_json(video, streams)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)

    geo_calls = []
    monkeypatch.setattr(
        ie, '_initialize_geo_bypass',
        lambda geo_bypass_context=None: geo_calls.append(geo_bypass_context))

    info = ie._real_extract(NO_GEO_URL)

    # no country in the URL -> geo bypass untouched
    assert geo_calls == []
    assert calls[0][0] == 'http://playapi.mtgx.tv/v3/videos/418113'

    # sami path has no _xx.xml suffix -> fall back to the URL's TLD (empty here)
    assert info['subtitles'] == {
        '': [{'url': 'http://example.com/subtitles/subtitle.xml'}],
    }
    assert info['id'] == '418113'
    assert info['title'] == 'Minimal'
    assert info['description'] is None
    assert info['series'] is None
    assert info['episode_number'] is None
    assert info['season'] is None
    assert info['season_number'] is None
    assert info['duration'] is None
    assert info['timestamp'] is None
    assert info['view_count'] is None
    assert info['age_limit'] == 0
    assert [f['format_id'] for f in info['formats']] == ['high']
    assert info['formats'][0]['url'] == 'http://example.com/video.mp4'
    assert info['formats'][0]['ext'] == 'mp4'


def test_real_extract_no_subtitles(ie, monkeypatch):
    video = {'title': 'No subs'}
    fake_download_json, _ = _make_download_json(
        video, {'streams': {'medium': 'http://example.com/video.mp4'}})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda *a, **k: None)

    info = ie._real_extract(GEO_URL)

    assert info['subtitles'] == {}
    assert info['title'] == 'No subs'
    assert len(info['formats']) == 1
    assert info['formats'][0]['format_id'] == 'medium'

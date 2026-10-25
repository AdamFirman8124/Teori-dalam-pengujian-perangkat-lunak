# file: project/youtube_dl/extractor/tvplay.py:382-415
# asked: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}
# gained: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}

import pytest
from youtube_dl.extractor.tvplay import ViafreeIE
from youtube_dl.utils import ExtractorError, GeoRestrictedError, parse_iso8601
from youtube_dl.compat import compat_HTTPError


def test_viafree_success_full(monkeypatch):
    ie = ViafreeIE()
    url = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    country = 'se'
    path = 'program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    program = {
        'guid': '757786',
        '_links': {'streamLink': {'href': 'https://example.com/stream-link'}},
        'episode': {'seriesTitle': 'My Series', 'episodeNumber': '3', 'seasonNumber': '2'},
        'video': {'duration': {'milliseconds': 1116000}},
        'availability': {'start': '2016-08-14T00:00:00Z'},
    }
    content = {
        '_embedded': {'viafreeBlocks': [{'_embedded': {'program': program}}]},
        'meta': {'title': 'My Title', 'image': 'http://example.com/thumb.jpg', 'description': 'My desc'},
    }
    stream_data = {'embedded': {'prioritizedStreams': [{'_links': {}, 'links': {'stream': {'href': 'http://example.com/playlist.m3u8'}}}] if False else [{'links': {'stream': {'href': 'http://example.com/playlist.m3u8'}}}] }}
    captured = {}

    def fake_geo_headers():
        captured['geo_called'] = True
        return {'Ytdl-request-proxy': 'http://proxy/'}

    def fake_download_json(url_or_request, video_id, headers=None, **kwargs):
        captured.setdefault('download_calls', []).append((url_or_request, video_id, headers))
        if 'viafree-content' in str(url_or_request):
            assert video_id == path
            assert str(url_or_request) == 'https://viafree-content.mtg-api.com/viafree-content/v1/%s/path/%s' % (country, path)
            return content
        assert url_or_request == 'https://example.com/stream-link'
        assert video_id == '757786'
        assert headers == {'Ytdl-request-proxy': 'http://proxy/'}
        return stream_data

    fake_formats = [{'url': 'http://example.com/720p.m3u8', 'format_id': '720p'}]

    def fake_extract_m3u8(m3u8_url, video_id, ext=None, **kwargs):
        captured['m3u8_url'] = m3u8_url
        captured['m3u8_video_id'] = video_id
        captured['m3u8_ext'] = ext
        return list(fake_formats)

    def fake_sort(formats):
        captured['sorted'] = True
        formats.sort(key=lambda f: f.get('format_id', ''))

    monkeypatch.setattr(ie, 'geo_verification_headers', fake_geo_headers)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8)
    monkeypatch.setattr(ie, '_sort_formats', fake_sort)

    result = ie._real_extract(url)

    assert captured['geo_called'] is True
    assert captured['m3u8_url'] == 'http://example.com/playlist.m3u8'
    assert captured['m3u8_video_id'] == '757786'
    assert captured['m3u8_ext'] == 'mp4'
    assert captured['sorted'] is True
    assert result['id'] == '757786'
    assert result['title'] == 'My Title'
    assert result['thumbnail'] == 'http://example.com/thumb.jpg'
    assert result['description'] == 'My desc'
    assert result['series'] == 'My Series'
    assert result['episode_number'] == 3
    assert result['season_number'] == 2
    assert result['duration'] == 1116
    assert result['timestamp'] == parse_iso8601('2016-08-14T00:00:00Z')
    assert result['formats'] == fake_formats


def test_viafree_success_missing_optional(monkeypatch):
    ie = ViafreeIE()
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    program = {
        'guid': '999',
        '_links': {'streamLink': {'href': 'https://example.com/s2'}},
    }
    content = {
        '_embedded': {'viafreeBlocks': [{'_embedded': {'program': program}}]},
        'meta': {'title': 'Only Title'},
    }
    stream_data = {'embedded': {'prioritizedStreams': [{'links': {'stream': {'href': 'http://example.com/other.m3u8'}}}] }}
    monkeypatch.setattr(ie, 'geo_verification_headers', lambda: {})
    monkeypatch.setattr(ie, '_download_json', lambda u, vid, headers=None, **kw: content if 'viafree-content' in str(u) else stream_data)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', lambda u, vid, ext=None, **kw: [{'url': u}])
    monkeypatch.setattr(ie, '_sort_formats', lambda f: None)

    result = ie._real_extract(url)

    assert result['id'] == '999'
    assert result['title'] == 'Only Title'
    assert result['thumbnail'] is None
    assert result['description'] is None
    assert result['series'] is None
    assert result['episode_number'] is None
    assert result['season_number'] is None
    assert result['duration'] is None
    assert result['timestamp'] is None
    assert result['formats'] == [{'url': 'http://example.com/other.m3u8'}]


def test_viafree_geo_restricted_403(monkeypatch):
    ie = ViafreeIE()
    url = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    program = {
        'guid': '757786',
        '_links': {'streamLink': {'href': 'https://example.com/blocked'}},
        'episode': {},
    }
    content = {
        '_embedded': {'viafreeBlocks': [{'_embedded': {'program': program}}]},
        'meta': {'title': 'T'},
    }
    err = ExtractorError('Unable to download JSON metadata')
    err.cause = compat_HTTPError('https://example.com/blocked', 403, 'Forbidden', {}, None)

    def fake_download_json(url_or_request, video_id, headers=None, **kwargs):
        if 'viafree-content' in str(url_or_request):
            return content
        raise err

    monkeypatch.setattr(ie, 'geo_verification_headers', lambda: {})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    called = {}
    monkeypatch.setattr(ie, '_extract_m3u8_formats', lambda *a, **kw: called.setdefault('called', True) or [])
    with pytest.raises(GeoRestrictedError) as excinfo:
        ie._real_extract(url)
    assert getattr(excinfo.value, 'countries', None) == ['se']
    assert 'called' not in called


def test_viafree_reraise_non_http_cause(monkeypatch):
    ie = ViafreeIE()
    url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    program = {
        'guid': '123',
        '_links': {'streamLink': {'href': 'https://example.com/s'}},
    }
    content = {
        '_embedded': {'viafreeBlocks': [{'_embedded': {'program': program}}]},
        'meta': {'title': 'T'},
    }
    orig = ExtractorError('boom')
    orig.cause = ValueError('not http')

    def fake_download_json(url_or_request, video_id, headers=None, **kwargs):
        if 'viafree-content' in str(url_or_request):
            return content
        raise orig

    monkeypatch.setattr(ie, 'geo_verification_headers', lambda: {})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(url)
    assert excinfo.value is orig


def test_viafree_reraise_http_non403(monkeypatch):
    ie = ViafreeIE()
    url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    program = {
        'guid': '123',
        '_links': {'streamLink': {'href': 'https://example.com/s'}},
    }
    content = {
        '_embedded': {'viafreeBlocks': [{'_embedded': {'program': program}}]},
        'meta': {'title': 'T'},
    }
    orig = ExtractorError('not found')
    orig.cause = compat_HTTPError('https://example.com/s', 404, 'Not Found', {}, None)

    def fake_download_json(url_or_request, video_id, headers=None, **kwargs):
        if 'viafree-content' in str(url_or_request):
            return content
        raise orig

    monkeypatch.setattr(ie, 'geo_verification_headers', lambda: {})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(url)
    assert excinfo.value is orig

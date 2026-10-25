# file: project/youtube_dl/extractor/tvplay.py:382-415
# asked: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}
# gained: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}

import pytest

from youtube_dl.compat import compat_HTTPError
from youtube_dl.extractor.tvplay import ViafreeIE
from youtube_dl.utils import ExtractorError, GeoRestrictedError, parse_iso8601


TEST_URL_SE = 'https://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
TEST_URL_NO = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
STREAM_LINK_HREF = 'https://stream.example.com/stream-link'
M3U8_HREF = 'https://example.com/playlist.m3u8'


def _make_full_program():
    return {
        'guid': '757786',
        '_links': {'streamLink': {'href': STREAM_LINK_HREF}},
        'episode': {
            'seriesTitle': 'Det beste vorspielet',
            'episodeNumber': '1',
            'seasonNumber': '2',
        },
        'video': {'duration': {'milliseconds': 1116000}},
        'availability': {'start': '2016-08-14T12:30:00Z'},
    }


def _make_content(program, title='Det beste vorspielet - Sesong 2 - Episode 1',
                  image='https://example.com/thumb.jpg', description='Some description'):
    return {
        '_embedded': {
            'viafreeBlocks': [
                {'_embedded': {'program': program}},
            ],
        },
        'meta': {
            'title': title,
            'image': image,
            'description': description,
        },
    }


def _make_stream_json(href=M3U8_HREF):
    return {
        'embedded': {
            'prioritizedStreams': [
                {'links': {'stream': {'href': href}}},
            ],
        },
    }


def test_viafree_success_full_metadata(monkeypatch):
    program = _make_full_program()
    content_json = _make_content(program)
    stream_json = _make_stream_json()
    fake_formats = [{'url': M3U8_HREF, 'format_id': 'low', 'ext': 'mp4'}]
    seen = {}

    def fake_download_json(self, url_or_request, video_id=None, **kwargs):
        if isinstance(url_or_request, str) and 'viafree-content' in url_or_request:
            assert video_id is not None
            seen['content_url'] = url_or_request
            return content_json
        seen['stream_url'] = url_or_request
        return stream_json

    def fake_extract_m3u8(self, m3u8_url, video_id, ext=None, **kwargs):
        seen['m3u8_url'] = m3u8_url
        seen['m3u8_video_id'] = video_id
        seen['m3u8_ext'] = ext
        return list(fake_formats)

    def fake_sort_formats(self, formats):
        seen['sorted'] = True

    monkeypatch.setattr(ViafreeIE, 'geo_verification_headers', lambda self: {})
    monkeypatch.setattr(ViafreeIE, '_download_json', fake_download_json)
    monkeypatch.setattr(ViafreeIE, '_extract_m3u8_formats', fake_extract_m3u8)
    monkeypatch.setattr(ViafreeIE, '_sort_formats', fake_sort_formats)

    ie = ViafreeIE()
    result = ie._real_extract(TEST_URL_SE)

    assert seen['stream_url'] == STREAM_LINK_HREF
    assert seen['m3u8_url'] == M3U8_HREF
    assert seen['m3u8_video_id'] == '757786'
    assert seen['m3u8_ext'] == 'mp4'
    assert seen.get('sorted') is True
    assert result['id'] == '757786'
    assert result['title'] == 'Det beste vorspielet - Sesong 2 - Episode 1'
    assert result['thumbnail'] == 'https://example.com/thumb.jpg'
    assert result['description'] == 'Some description'
    assert result['series'] == 'Det beste vorspielet'
    assert result['episode_number'] == 1
    assert result['season_number'] == 2
    assert result['duration'] == 1116
    assert result['timestamp'] == parse_iso8601('2016-08-14T12:30:00Z')
    assert result['formats'] == fake_formats


def test_viafree_success_missing_optionals(monkeypatch):
    program = {
        'guid': '99999',
        '_links': {'streamLink': {'href': STREAM_LINK_HREF}},
    }
    content_json = {
        '_embedded': {
            'viafreeBlocks': [{'_embedded': {'program': program}}],
        },
        'meta': {'title': 'Minimal Title'},
    }
    stream_json = _make_stream_json()
    fake_formats = [{'url': M3U8_HREF, 'ext': 'mp4'}]

    def fake_download_json(self, url_or_request, video_id=None, **kwargs):
        if isinstance(url_or_request, str) and 'viafree-content' in url_or_request:
            return content_json
        return stream_json

    monkeypatch.setattr(ViafreeIE, 'geo_verification_headers', lambda self: {})
    monkeypatch.setattr(ViafreeIE, '_download_json', fake_download_json)
    monkeypatch.setattr(
        ViafreeIE, '_extract_m3u8_formats',
        lambda self, url, video_id, ext=None, **kwargs: list(fake_formats))
    monkeypatch.setattr(ViafreeIE, '_sort_formats', lambda self, formats: None)

    ie = ViafreeIE()
    result = ie._real_extract(TEST_URL_NO)

    assert result['id'] == '99999'
    assert result['title'] == 'Minimal Title'
    assert result['thumbnail'] is None
    assert result['description'] is None
    assert result['series'] is None
    assert result['episode_number'] is None
    assert result['season_number'] is None
    assert result['duration'] is None
    assert result['timestamp'] is None
    assert result['formats'] == fake_formats


def test_viafree_geo_restricted_403(monkeypatch):
    program = _make_full_program()
    content_json = _make_content(program)
    cause = compat_HTTPError('https://stream.example.com/stream-link', 403, 'Forbidden', {}, None)

    def fake_download_json(self, url_or_request, video_id=None, **kwargs):
        if isinstance(url_or_request, str) and 'viafree-content' in url_or_request:
            return content_json
        raise ExtractorError('Unable to download JSON metadata', cause=cause)

    monkeypatch.setattr(ViafreeIE, 'geo_verification_headers', lambda self: {})
    monkeypatch.setattr(ViafreeIE, '_download_json', fake_download_json)
    monkeypatch.setattr(
        ViafreeIE, '_extract_m3u8_formats',
        lambda self, *a, **k: (_ for _ in ()).throw(AssertionError('should not be called')))

    ie = ViafreeIE()
    with pytest.raises(GeoRestrictedError):
        ie._real_extract(TEST_URL_SE)


def test_viafree_reraise_non403_http(monkeypatch):
    program = _make_full_program()
    content_json = _make_content(program)
    cause = compat_HTTPError('https://stream.example.com/stream-link', 404, 'Not Found', {}, None)

    def fake_download_json(self, url_or_request, video_id=None, **kwargs):
        if isinstance(url_or_request, str) and 'viafree-content' in url_or_request:
            return content_json
        raise ExtractorError('Unable to download JSON metadata', cause=cause)

    monkeypatch.setattr(ViafreeIE, 'geo_verification_headers', lambda self: {})
    monkeypatch.setattr(ViafreeIE, '_download_json', fake_download_json)

    ie = ViafreeIE()
    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(TEST_URL_SE)
    assert not isinstance(excinfo.value, GeoRestrictedError)
    assert isinstance(excinfo.value.cause, compat_HTTPError)
    assert excinfo.value.cause.code == 404


def test_viafree_reraise_non_http_cause(monkeypatch):
    program = _make_full_program()
    content_json = _make_content(program)

    def fake_download_json(self, url_or_request, video_id=None, **kwargs):
        if isinstance(url_or_request, str) and 'viafree-content' in url_or_request:
            return content_json
        raise ExtractorError('boom', cause=ValueError('nope'))

    monkeypatch.setattr(ViafreeIE, 'geo_verification_headers', lambda self: {})
    monkeypatch.setattr(ViafreeIE, '_download_json', fake_download_json)

    ie = ViafreeIE()
    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(TEST_URL_SE)
    assert not isinstance(excinfo.value, GeoRestrictedError)
    assert isinstance(excinfo.value.cause, ValueError)

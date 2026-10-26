# file: project/youtube_dl/extractor/tvplay.py:382-415
# asked: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}
# gained: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}

import pytest
from youtube_dl.extractor.tvplay import ViafreeIE
from youtube_dl.compat import compat_HTTPError
from youtube_dl.utils import ExtractorError, GeoRestrictedError, parse_iso8601


TEST_URL = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
STREAM_LINK_HREF = 'https://example.com/stream-link'
M3U8_HREF = 'https://example.com/playlist.m3u8'


def _make_content(program, title='Test Title', image='https://example.com/thumb.jpg', description='Test description'):
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


def _make_full_program():
    return {
        'guid': '757786',
        '_links': {'streamLink': {'href': STREAM_LINK_HREF}},
        'episode': {
            'seriesTitle': 'Test Series',
            'episodeNumber': 3,
            'seasonNumber': 2,
        },
        'video': {'duration': {'milliseconds': 1116000}},
        'availability': {'start': '2016-08-14T12:00:00+00:00'},
    }


def _make_stream_json(href=M3U8_HREF):
    return {
        'embedded': {
            'prioritizedStreams': [
                {'links': {'stream': {'href': href}}},
            ],
        },
    }


def _install_mocks(monkeypatch, ie, content, second_result):
    monkeypatch.setattr(ie, 'geo_verification_headers', lambda *a, **k: {'X-Test': '1'})

    sort_calls = []

    def fake_sort(formats):
        sort_calls.append(list(formats))
        formats.sort(key=lambda f: f.get('url', ''))

    monkeypatch.setattr(ie, '_sort_formats', fake_sort)

    captured = {}

    def fake_extract_m3u8(url, video_id, ext=None, **kwargs):
        captured['url'] = url
        captured['video_id'] = video_id
        captured['ext'] = ext
        return [{'url': 'https://example.com/720p.m3u8', 'format_id': '720p', 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8)

    def fake_download_json(url_or_request, video_id, *args, **kwargs):
        s = str(url_or_request)
        if 'viafree-content.mtg-api.com' in s:
            return content
        captured['stream_url'] = s
        captured['stream_video_id'] = video_id
        captured['stream_headers'] = kwargs.get('headers')
        if isinstance(second_result, Exception):
            raise second_result
        return second_result

    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    return captured, sort_calls


def test_viafree_success_full_metadata(monkeypatch):
    ie = ViafreeIE()
    program = _make_full_program()
    content = _make_content(program)
    stream_json = _make_stream_json()
    captured, sort_calls = _install_mocks(monkeypatch, ie, content, stream_json)

    result = ie._real_extract(TEST_URL)

    assert result['id'] == '757786'
    assert result['title'] == 'Test Title'
    assert result['thumbnail'] == 'https://example.com/thumb.jpg'
    assert result['description'] == 'Test description'
    assert result['series'] == 'Test Series'
    assert result['episode_number'] == 3
    assert result['season_number'] == 2
    assert result['duration'] == 1116
    assert result['timestamp'] == parse_iso8601('2016-08-14T12:00:00+00:00')
    assert isinstance(result['formats'], list)
    assert len(result['formats']) == 1
    assert result['formats'][0]['url'] == 'https://example.com/720p.m3u8'
    # postconditions on intermediate values
    assert captured['url'] == M3U8_HREF
    assert captured['video_id'] == '757786'
    assert captured['ext'] == 'mp4'
    assert captured['stream_url'] == STREAM_LINK_HREF
    assert captured['stream_video_id'] == '757786'
    assert captured['stream_headers'] == {'X-Test': '1'}
    assert len(sort_calls) == 1


def test_viafree_success_missing_optional_fields(monkeypatch):
    ie = ViafreeIE()
    program = {
        'guid': '999',
        '_links': {'streamLink': {'href': STREAM_LINK_HREF}},
        # no 'episode', no 'video', no 'availability'
    }
    content = _make_content(program, image=None, description=None)
    # meta without image/description keys to exercise .get defaults
    content['meta'] = {'title': 'Only Title'}
    stream_json = _make_stream_json()
    captured, sort_calls = _install_mocks(monkeypatch, ie, content, stream_json)

    result = ie._real_extract(TEST_URL)

    assert result['id'] == '999'
    assert result['title'] == 'Only Title'
    assert result['thumbnail'] is None
    assert result['description'] is None
    assert result['series'] is None
    assert result['episode_number'] is None
    assert result['season_number'] is None
    assert result['duration'] is None
    assert result['timestamp'] is None
    assert result['formats'][0]['url'] == 'https://example.com/720p.m3u8'
    assert captured['url'] == M3U8_HREF
    assert len(sort_calls) == 1


def test_viafree_geo_restricted_403(monkeypatch):
    ie = ViafreeIE()
    program = _make_full_program()
    content = _make_content(program)
    http_err = compat_HTTPError(STREAM_LINK_HREF, 403, 'Forbidden', {}, None)
    exc = ExtractorError('Unable to download JSON metadata', cause=http_err)
    _install_mocks(monkeypatch, ie, content, exc)

    with pytest.raises(GeoRestrictedError) as excinfo:
        ie._real_extract(TEST_URL)
    # country extracted from TEST_URL is 'se'
    assert getattr(excinfo.value, 'countries', ['se']) == ['se']


def test_viafree_reraise_non_403_http_error(monkeypatch):
    ie = ViafreeIE()
    program = _make_full_program()
    content = _make_content(program)
    http_err = compat_HTTPError(STREAM_LINK_HREF, 404, 'Not Found', {}, None)
    exc = ExtractorError('Unable to download JSON metadata', cause=http_err)
    _install_mocks(monkeypatch, ie, content, exc)

    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(TEST_URL)
    assert excinfo.value is exc
    assert isinstance(excinfo.value.cause, compat_HTTPError)
    assert excinfo.value.cause.code == 404


def test_viafree_reraise_non_http_error(monkeypatch):
    ie = ViafreeIE()
    program = _make_full_program()
    content = _make_content(program)
    exc = ExtractorError('Unable to download JSON metadata', cause=ValueError('oops'))
    _install_mocks(monkeypatch, ie, content, exc)

    with pytest.raises(ExtractorError) as excinfo:
        ie._real_extract(TEST_URL)
    assert excinfo.value is exc
    assert isinstance(excinfo.value.cause, ValueError)

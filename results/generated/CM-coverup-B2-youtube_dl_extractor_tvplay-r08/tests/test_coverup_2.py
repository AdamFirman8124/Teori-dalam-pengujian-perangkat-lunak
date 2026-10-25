# file: project/youtube_dl/extractor/tvplay.py:382-415
# asked: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}
# gained: {"lines": [383, 384, 385, 386, 387, 388, 389, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414], "branches": [[396, 397], [396, 398]]}

import pytest

from youtube_dl.compat import compat_HTTPError
from youtube_dl.extractor.tvplay import ViafreeIE
from youtube_dl.utils import (
    ExtractorError,
    GeoRestrictedError,
    int_or_none,
    parse_iso8601,
)

COUNTRY = 'se'
PATH = 'programmer/underholdning/some-show/avsnitt-1'
URL = 'https://viafree.%s/%s' % (COUNTRY, PATH)
CONTENT_URL = (
    'https://viafree-content.mtg-api.com/viafree-content/v1/%s/path/%s'
    % (COUNTRY, PATH)
)
STREAM_LINK_HREF = 'https://api.example.com/viafree/streamLink'
STREAM_HREF = 'https://stream.example.com/master.m3u8'
GUID = 'guid-1234'
TITLE = 'Test Title'
THUMBNAIL = 'https://img.example.com/thumb.jpg'
DESCRIPTION = 'A description'
SERIES = 'Test Series'
EPISODE_NUMBER = 3
SEASON_NUMBER = 2
DURATION_MS = 1116000
AVAILABILITY_START = '2016-08-14T19:30:00+0000'


class FakeDownloader(object):
    def __init__(self):
        self.params = {}


def make_content():
    program = {
        'guid': GUID,
        '_links': {'streamLink': {'href': STREAM_LINK_HREF}},
        'episode': {
            'seriesTitle': SERIES,
            'episodeNumber': EPISODE_NUMBER,
            'seasonNumber': SEASON_NUMBER,
        },
        'video': {'duration': {'milliseconds': DURATION_MS}},
        'availability': {'start': AVAILABILITY_START},
    }
    return {
        '_embedded': {
            'viafreeBlocks': [{'_embedded': {'program': program}}],
        },
        'meta': {
            'title': TITLE,
            'image': THUMBNAIL,
            'description': DESCRIPTION,
        },
    }


def make_stream_json():
    return {
        'embedded': {
            'prioritizedStreams': [
                {'links': {'stream': {'href': STREAM_HREF}}},
            ],
        },
    }


def make_ie(monkeypatch, content, stream_json=None, stream_error=None):
    ie = ViafreeIE(FakeDownloader())
    calls = []

    def fake_download_json(url_or_request, video_id, *args, **kwargs):
        calls.append((url_or_request, video_id))
        if url_or_request == CONTENT_URL:
            return content
        if stream_error is not None:
            raise stream_error
        return stream_json

    def fake_extract_m3u8_formats(m3u8_url, video_id, *args, **kwargs):
        return [{'url': m3u8_url, 'ext': 'mp4', 'format_id': 'test'}]

    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8_formats)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: None)
    return ie, calls


def test_viafree_full_success(monkeypatch):
    ie, calls = make_ie(
        monkeypatch, make_content(), stream_json=make_stream_json())

    info = ie._real_extract(URL)

    # Lines 383-385: URL parsed, content JSON downloaded from the right URL
    assert calls[0] == (CONTENT_URL, PATH)
    # Lines 392-394: streamLink JSON fetched with guid as video id
    assert calls[1] == (STREAM_LINK_HREF, GUID)
    # Lines 400-401: m3u8 formats extracted from the stream href
    assert info['formats'][0]['url'] == STREAM_HREF
    assert info['formats'][0]['ext'] == 'mp4'
    # Lines 404-414: returned metadata
    assert info['id'] == GUID
    assert info['title'] == TITLE
    assert info['thumbnail'] == THUMBNAIL
    assert info['description'] == DESCRIPTION
    assert info['series'] == SERIES
    assert info['episode_number'] == EPISODE_NUMBER
    assert info['season_number'] == SEASON_NUMBER
    assert info['duration'] == int_or_none(DURATION_MS, 1000)
    assert info['timestamp'] == parse_iso8601(AVAILABILITY_START)


def test_viafree_geo_restricted_403(monkeypatch):
    ie, calls = make_ie(
        monkeypatch,
        make_content(),
        stream_error=ExtractorError(
            'Unable to download JSON metadata',
            cause=compat_HTTPError(
                STREAM_LINK_HREF, 403, 'Forbidden', {}, None),
        ),
    )

    with pytest.raises(GeoRestrictedError):
        ie._real_extract(URL)

    # Lines 383-388 executed before the failure; streamLink fetch attempted
    assert calls[0] == (CONTENT_URL, PATH)
    assert calls[1] == (STREAM_LINK_HREF, GUID)


def test_viafree_non_403_http_error_reraised(monkeypatch):
    original = ExtractorError(
        'Unable to download JSON metadata',
        cause=compat_HTTPError(
            STREAM_LINK_HREF, 404, 'Not Found', {}, None),
    )
    ie, calls = make_ie(
        monkeypatch, make_content(), stream_error=original)

    with pytest.raises(ExtractorError) as exc_info:
        ie._real_extract(URL)

    # Line 398: the original error is re-raised, not converted to geo error
    assert exc_info.value is original
    assert not isinstance(exc_info.value, GeoRestrictedError)
    assert calls[0] == (CONTENT_URL, PATH)
    assert calls[1] == (STREAM_LINK_HREF, GUID)

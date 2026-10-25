# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import pytest

from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.utils import unsmuggle_url


URL = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
PLAYLIST_ID = 'btcc-2018-all-the-action-from-brands-hatch'
TITLE = 'BTCC 2018: All the action from Brands Hatch'
VIDEO_IDS = ['1234567890123', '9876543210987', '5555555555555']
BRIGHTCOVE_TEMPLATE = (
    'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')


class _StubDownloader(object):
    """Minimal downloader stub: InfoExtractor only needs .params here."""

    params = {}

    def report_warning(self, *args, **kwargs):
        pass

    def to_screen(self, *args, **kwargs):
        pass


def _make_ie():
    return ITVBTCCIE(_StubDownloader())


def _webpage(video_ids, title=TITLE):
    head = '<meta property="og:title" content="%s">' % title if title else ''
    body = ''.join('<div data-video-id="%s"></div>' % vid for vid in video_ids)
    return '<html><head>%s</head><body>%s</body></html>' % (head, body)


@pytest.fixture
def download_calls(monkeypatch):
    """Patch _download_webpage; returns a list recording (url, video_id) calls."""
    calls = []
    page = {'html': _webpage(VIDEO_IDS)}

    def fake_download_webpage(self, url_or_request, video_id, *args, **kwargs):
        calls.append((url_or_request, video_id))
        return page['html']

    monkeypatch.setattr(
        ITVBTCCIE, '_download_webpage', fake_download_webpage, raising=True)
    return calls, page


def test_itvbtcc_real_extract_full_coverage(download_calls):
    calls, _ = download_calls
    result = _make_ie()._real_extract(URL)

    assert calls == [(URL, PLAYLIST_ID)]

    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == TITLE

    entries = result['entries']
    assert len(entries) == len(VIDEO_IDS)

    for entry, video_id in zip(entries, VIDEO_IDS):
        assert entry['_type'] == 'url'
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        assert entry['id'] == video_id

        base_url = BRIGHTCOVE_TEMPLATE % video_id
        assert entry['url'].startswith(base_url)

        unsmuggled, data = unsmuggle_url(entry['url'])
        assert unsmuggled == base_url
        assert data['geo_ip_blocks'] == [
            '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']
        assert data['referrer'] == URL


def test_itvbtcc_real_extract_no_videos(download_calls):
    calls, page = download_calls
    page['html'] = _webpage([])

    result = _make_ie()._real_extract(URL)

    assert calls == [(URL, PLAYLIST_ID)]
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == TITLE
    assert result['entries'] == []

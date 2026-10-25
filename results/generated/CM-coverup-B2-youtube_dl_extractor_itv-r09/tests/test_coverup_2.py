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
TEMPLATE = (
    'http://players.brightcove.net/1582188683001/'
    'HkiHLnNRx_default/index.html?videoId=%s'
)
GEO_IP_BLOCKS = ['193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']


class FakeDownloader(object):
    """Minimal downloader so InfoExtractor warning paths do not crash."""

    params = {}


def _make_ie(monkeypatch, webpage, title=TITLE):
    """Build an ITVBTCCIE with network and og:title lookup stubbed out."""
    ie = ITVBTCCIE()
    ie.set_downloader(FakeDownloader())
    calls = []

    def fake_download_webpage(url_or_request, video_id, *args, **kwargs):
        calls.append(('download', url_or_request, video_id))
        return webpage

    def fake_og_search_title(html, **kwargs):
        calls.append(('og_title', html, kwargs))
        return title

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_og_search_title', fake_og_search_title)
    return ie, calls


def test_itvbtcc_real_extract_with_videos(monkeypatch):
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="%s">'
        '</head><body>'
        '<div data-video-id="1234567890123"></div>'
        "<div data-video-id='9876543210987'></div>"
        '<div data-video-id="5555555555555"></div>'
        '</body></html>' % TITLE
    )
    ie, calls = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(URL)

    # _download_webpage called once with the original url and playlist id
    assert calls[0] == ('download', URL, PLAYLIST_ID)
    # _og_search_title called with fatal=False on the downloaded page
    assert calls[1][0] == 'og_title'
    assert calls[1][1] == webpage
    assert calls[1][2] == {'fatal': False}

    # playlist_result postconditions
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == TITLE

    entries = result['entries']
    assert len(entries) == len(VIDEO_IDS)

    for entry, video_id in zip(entries, VIDEO_IDS):
        assert entry['_type'] == 'url'
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        assert entry['id'] == video_id

        base_url = TEMPLATE % video_id
        assert entry['url'].startswith(base_url)

        # smuggled payload postconditions
        unsmuggled, data = unsmuggle_url(entry['url'])
        assert unsmuggled == base_url
        assert data['geo_ip_blocks'] == GEO_IP_BLOCKS
        assert data['referrer'] == URL


def test_itvbtcc_real_extract_without_videos(monkeypatch):
    webpage = '<html><head></head><body><p>no videos here</p></body></html>'
    ie, calls = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(URL)

    assert calls[0] == ('download', URL, PLAYLIST_ID)
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == TITLE
    assert result['entries'] == []


def test_itvbtcc_real_extract_without_title(monkeypatch):
    webpage = '<html><body><div data-video-id="1234567890123"></div></body></html>'
    ie, calls = _make_ie(monkeypatch, webpage, title=None)

    result = ie._real_extract(URL)

    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert 'title' not in result
    assert len(result['entries']) == 1
    assert result['entries'][0]['id'] == '1234567890123'

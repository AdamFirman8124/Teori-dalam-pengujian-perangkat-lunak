# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import pytest

from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.utils import smuggle_url, unsmuggle_url


URL = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
PLAYLIST_ID = 'btcc-2018-all-the-action-from-brands-hatch'

WEBPAGE = '''
<html><head><title>BTCC 2018: All the action from Brands Hatch</title></head>
<body>
  <div class="video" data-video-id="5779302764001"></div>
  <div class="video" data-video-id='5779302764002'></div>
  <div class="video" data-video-id="5779302764003"></div>
  <div class="video" data-video-id="not-a-number"></div>
</body></html>
'''

VIDEO_IDS = ['5779302764001', '5779302764002', '5779302764003']

EXPECTED_SMUGGLE = {
    'geo_ip_blocks': [
        '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21',
    ],
    'referrer': URL,
}


def _build_ie(monkeypatch, webpage, title):
    """Create an ITVBTCCIE with network/HTML helpers stubbed out."""
    ie = ITVBTCCIE()
    calls = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        calls['download'] = (url, video_id)
        return webpage

    def fake_og_search_title(html, **kwargs):
        calls['og'] = (html, kwargs)
        return title

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_og_search_title', fake_og_search_title)
    return ie, calls


def _expected_entry(video_id):
    return smuggle_url(
        ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id,
        EXPECTED_SMUGGLE)


def test_real_extract_full_playlist(monkeypatch):
    ie, calls = _build_ie(monkeypatch, WEBPAGE, 'BTCC 2018: All the action from Brands Hatch')

    result = ie._real_extract(URL)

    # The webpage was fetched with the matched playlist id.
    assert calls['download'] == (URL, PLAYLIST_ID)
    # Title lookup was non-fatal.
    assert calls['og'] == (WEBPAGE, {'fatal': False})

    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'

    entries = result['entries']
    assert len(entries) == len(VIDEO_IDS)
    assert [e['id'] for e in entries] == VIDEO_IDS

    for entry, video_id in zip(entries, VIDEO_IDS):
        assert entry['_type'] == 'url'
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        assert entry['url'] == _expected_entry(video_id)
        assert 'videoId=%s' % video_id in entry['url']
        # The smuggled data is URL-encoded inside the fragment, so decode
        # it with unsmuggle_url before asserting on its contents.
        smuggled_url, smuggled_data = unsmuggle_url(entry['url'])
        assert smuggled_url == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert smuggled_data == EXPECTED_SMUGGLE
        assert '193.113.0.0/16' in smuggled_data['geo_ip_blocks']
        assert smuggled_data['referrer'] == URL


def test_real_extract_without_title(monkeypatch):
    ie, calls = _build_ie(monkeypatch, WEBPAGE, None)

    result = ie._real_extract(URL)

    assert calls['og'] == (WEBPAGE, {'fatal': False})
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert 'title' not in result
    assert [e['id'] for e in result['entries']] == VIDEO_IDS


def test_real_extract_no_videos(monkeypatch):
    ie, calls = _build_ie(monkeypatch, '<html><body>no videos here</body></html>', 'Empty')

    result = ie._real_extract(URL)

    assert calls['download'] == (URL, PLAYLIST_ID)
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == 'Empty'
    assert result['entries'] == []


def test_valid_url_matches_btcc_pages():
    assert ITVBTCCIE.suitable(URL)
    assert ITVBTCCIE.suitable('https://itv.com/btcc/some-video')
    assert not ITVBTCCIE.suitable('http://www.itv.com/other/btcc-2018')

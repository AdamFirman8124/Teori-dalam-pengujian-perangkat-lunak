# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import json

import pytest

from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.utils import unsmuggle_url


WEBPAGE = '''
<html><head>
<meta property="og:title" content="BTCC 2018: All the action from Brands Hatch" />
</head><body>
<div data-video-id="1111111111"></div>
<div data-video-id='2222222222'></div>
<a data-video-id="3333333333">link</a>
<div data-video-id="not-a-number"></div>
</body></html>
'''

URL = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
PLAYLIST_ID = 'btcc-2018-all-the-action-from-brands-hatch'


def _make_ie(monkeypatch, webpage, title):
    ie = ITVBTCCIE()
    calls = {}

    def fake_download_webpage(url_or_request, video_id, *args, **kwargs):
        calls['download'] = (url_or_request, video_id)
        return webpage

    def fake_og_search_title(html, **kwargs):
        calls['og'] = (html, kwargs)
        return title

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_og_search_title', fake_og_search_title)
    return ie, calls


def test_real_extract_full_playlist(monkeypatch):
    ie, calls = _make_ie(
        monkeypatch, WEBPAGE, 'BTCC 2018: All the action from Brands Hatch')

    result = ie._real_extract(URL)

    # _download_webpage called with the page url and the matched playlist id
    assert calls['download'] == (URL, PLAYLIST_ID)
    # _og_search_title called non-fatally on the downloaded webpage
    assert calls['og'] == (WEBPAGE, {'fatal': False})

    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'

    entries = result['entries']
    assert len(entries) == 3
    assert [e['id'] for e in entries] == ['1111111111', '2222222222', '3333333333']

    for entry, video_id in zip(entries, ['1111111111', '2222222222', '3333333333']):
        assert entry['_type'] == 'url'
        assert entry['ie_key'] == 'BrightcoveNew'
        assert entry['id'] == video_id

        smuggled_url, data = unsmuggle_url(entry['url'], {})
        assert smuggled_url == (
            'http://players.brightcove.net/1582188683001/'
            'HkiHLnNRx_default/index.html?videoId=%s' % video_id)
        assert data['geo_ip_blocks'] == [
            '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']
        assert data['referrer'] == URL
        # smuggle payload is JSON-encoded in the fragment
        assert json.loads(json.dumps(data)) == data


def test_real_extract_no_title_no_videos(monkeypatch):
    ie, calls = _make_ie(monkeypatch, '<html><body>nothing here</body></html>', None)

    result = ie._real_extract(URL)

    assert calls['download'] == (URL, PLAYLIST_ID)
    assert calls['og'] == ('<html><body>nothing here</body></html>', {'fatal': False})

    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['entries'] == []
    # falsy title must not be added to the playlist result
    assert 'title' not in result

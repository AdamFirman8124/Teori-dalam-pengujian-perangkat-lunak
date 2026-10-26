# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.utils import unsmuggle_url


def test_itvbtcc_extracts_all_brightcove_entries(monkeypatch):
    ie = ITVBTCCIE()
    url = (
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    title = 'BTCC 2018: All the action from Brands Hatch'
    webpage = (
        '<html><body>'
        '<div data-video-id="1234567890001"></div>'
        "<div data-video-id='9876543210002'></div>"
        '<div data-video-id="not-numeric"></div>'
        '</body></html>'
    )
    calls = {}

    def download_webpage(request_url, video_id, *args, **kwargs):
        calls['download'] = (request_url, video_id)
        return webpage

    def search_title(html, fatal=True):
        calls['title_search'] = (html, fatal)
        return title

    monkeypatch.setattr(ie, '_download_webpage', download_webpage)
    monkeypatch.setattr(ie, '_og_search_title', search_title)

    result = ie._real_extract(url)

    assert calls == {
        'download': (url, playlist_id),
        'title_search': (webpage, False),
    }
    assert result['_type'] == 'playlist'
    assert result['id'] == playlist_id
    assert result['title'] == title

    entries = result['entries']
    assert [entry['id'] for entry in entries] == [
        '1234567890001',
        '9876543210002',
    ]

    for entry in entries:
        video_id = entry['id']
        brightcove_url, smuggled_data = unsmuggle_url(entry['url'])

        assert entry['_type'] == 'url'
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        assert brightcove_url == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert smuggled_data == {
            'geo_ip_blocks': [
                '193.113.0.0/16',
                '54.36.162.0/23',
                '159.65.16.0/21',
            ],
            'referrer': url,
        }


def test_itvbtcc_returns_empty_playlist_without_title(monkeypatch):
    ie = ITVBTCCIE()
    url = 'https://www.itv.com/btcc/races/race-without-videos'
    playlist_id = 'race-without-videos'
    webpage = '<html><body>No video IDs or OpenGraph title</body></html>'
    calls = {}

    def download_webpage(request_url, video_id, *args, **kwargs):
        calls['download'] = (request_url, video_id)
        return webpage

    def search_title(html, fatal=True):
        calls['title_search'] = (html, fatal)
        return None

    monkeypatch.setattr(ie, '_download_webpage', download_webpage)
    monkeypatch.setattr(ie, '_og_search_title', search_title)

    result = ie._real_extract(url)

    assert calls == {
        'download': (url, playlist_id),
        'title_search': (webpage, False),
    }
    assert result == {
        '_type': 'playlist',
        'entries': [],
        'id': playlist_id,
    }

# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import json
from urllib.parse import parse_qs, urlsplit

from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.extractor.itv import ITVBTCCIE


def test_itv_btcc_extracts_and_smuggles_all_video_ids(monkeypatch):
    extractor = ITVBTCCIE()
    url = 'https://www.itv.com/btcc/races/brands-hatch-highlights'
    webpage = '''
        <html>
          <body>
            <div data-video-id="123456"></div>
            <div data-video-id='789012'></div>
          </body>
        </html>
    '''
    title_calls = []

    def download_webpage(requested_url, video_id):
        assert requested_url == url
        assert video_id == 'brands-hatch-highlights'
        return webpage

    def search_title(received_webpage, fatal=True):
        title_calls.append((received_webpage, fatal))
        return 'Brands Hatch Highlights'

    monkeypatch.setattr(extractor, '_download_webpage', download_webpage)
    monkeypatch.setattr(extractor, '_og_search_title', search_title)

    result = extractor._real_extract(url)

    assert title_calls == [(webpage, False)]
    assert result['_type'] == 'playlist'
    assert result['id'] == 'brands-hatch-highlights'
    assert result['title'] == 'Brands Hatch Highlights'
    assert len(result['entries']) == 2

    for entry, video_id in zip(result['entries'], ('123456', '789012')):
        assert entry['_type'] == 'url'
        assert entry['id'] == video_id
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()

        split_url = urlsplit(entry['url'])
        assert split_url._replace(fragment='').geturl() == (
            ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
        )

        smuggled_data = json.loads(
            parse_qs(split_url.fragment)['__youtubedl_smuggle'][0]
        )
        assert smuggled_data == {
            'geo_ip_blocks': [
                '193.113.0.0/16',
                '54.36.162.0/23',
                '159.65.16.0/21',
            ],
            'referrer': url,
        }


def test_itv_btcc_returns_empty_untitled_playlist_when_no_videos(
        monkeypatch):
    extractor = ITVBTCCIE()
    url = 'http://itv.com/btcc/archive/no-video-page'
    webpage = '<html><body>No Brightcove videos</body></html>'
    title_calls = []

    def download_webpage(requested_url, video_id):
        assert requested_url == url
        assert video_id == 'no-video-page'
        return webpage

    def search_title(received_webpage, fatal=True):
        title_calls.append((received_webpage, fatal))
        return None

    monkeypatch.setattr(extractor, '_download_webpage', download_webpage)
    monkeypatch.setattr(extractor, '_og_search_title', search_title)

    result = extractor._real_extract(url)

    assert title_calls == [(webpage, False)]
    assert result == {
        '_type': 'playlist',
        'entries': [],
        'id': 'no-video-page',
    }

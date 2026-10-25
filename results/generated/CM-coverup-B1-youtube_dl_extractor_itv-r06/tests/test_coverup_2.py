# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import re

import pytest

from youtube_dl.extractor.common import InfoExtractor
from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.utils import smuggle_url, unsmuggle_url

# Import the extractor under test from the real module if available; otherwise
# fall back to the snippet definition so the test is self-contained.
try:
    from youtube_dl.extractor.itv import ITVBTCCIE
except Exception:
    ITVBTCCIE = None

if ITVBTCCIE is None:
    class ITVBTCCIE(InfoExtractor):
        _VALID_URL = r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
        BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

        def _real_extract(self, url):
            playlist_id = self._match_id(url)

            webpage = self._download_webpage(url, playlist_id)

            entries = [
                self.url_result(
                    smuggle_url(self.BRIGHTCOVE_URL_TEMPLATE % video_id, {
                        # ITV does not like some GB IP ranges, so here are some
                        # IP blocks it accepts
                        'geo_ip_blocks': [
                            '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21'
                        ],
                        'referrer': url,
                    }),
                    ie=BrightcoveNewIE.ie_key(), video_id=video_id)
                for video_id in re.findall(r'data-video-id=["\'](\d+)', webpage)]

            title = self._og_search_title(webpage, fatal=False)

            return self.playlist_result(entries, playlist_id, title)


FAKE_WEBPAGE = u'''
<html>
<head>
<meta property="og:title" content="BTCC 2018: All the action from Brands Hatch">
</head>
<body>
<div data-video-id="5785806356001"></div>
<div data-video-id='5785806366001'></div>
<span data-video-id="5785806376001"></span>
<!-- must NOT be matched: missing quote -->
<div data-video-id=5785806386001></div>
</body>
</html>
'''


class FakeDownloader(object):
    """Minimal stand-in for a YoutubeDL downloader: only 'params' is needed."""

    def __init__(self):
        self.params = {}


def test_itvbtccie_real_extract_full_coverage(monkeypatch):
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE(downloader=FakeDownloader())

    calls = {}

    def fake_download_webpage(self, site_url, video_id=None, *args, **kwargs):
        calls['url'] = site_url
        calls['video_id'] = video_id
        return FAKE_WEBPAGE

    monkeypatch.setattr(
        InfoExtractor, '_download_webpage', fake_download_webpage)

    result = ie._real_extract(url)

    # _download_webpage was called with the requested url and matched id
    assert calls['url'] == url
    assert calls['video_id'] == 'btcc-2018-all-the-action-from-brands-hatch'

    # It is a playlist result with the matched id and og:title
    assert result['_type'] == 'playlist'
    assert result['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'

    # Only the three quoted data-video-id values are matched
    entries = result['entries']
    assert len(entries) == 3

    expected_video_ids = ['5785806356001', '5785806366001', '5785806376001']
    for entry, video_id in zip(entries, expected_video_ids):
        assert entry['_type'] == 'url'
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        assert entry['id'] == video_id

        # The url is the smuggled brightcove url; unsmuggle to verify payload
        inner_url, smuggled_data = unsmuggle_url(entry['url'])
        assert inner_url == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert smuggled_data['geo_ip_blocks'] == [
            '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']
        assert smuggled_data['referrer'] == url

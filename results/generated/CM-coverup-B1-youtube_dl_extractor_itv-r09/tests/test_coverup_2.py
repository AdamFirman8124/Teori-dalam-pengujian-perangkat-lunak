# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import pytest
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.utils import unsmuggle_url


class _FakeDownloader(object):
    def __init__(self):
        self.params = {'no_color': True}
        self.warnings = []

    def report_warning(self, message, *args, **kwargs):
        self.warnings.append(message)
        return None


def _make_extractor_with_webpage(monkeypatch, webpage, captured=None):
    if captured is None:
        captured = {}
    fake_dl = _FakeDownloader()

    def fake_download_webpage(self, url_or_request, video_id, *args, **kwargs):
        captured['url_or_request'] = url_or_request
        captured['video_id'] = video_id
        captured['args'] = args
        captured['kwargs'] = kwargs
        return webpage

    monkeypatch.setattr(ITVBTCCIE, '_download_webpage', fake_download_webpage)
    ie = ITVBTCCIE()
    ie.set_downloader(fake_dl)
    captured['downloader'] = fake_dl
    return ie, captured


def test_itvbtcc_multiple_ids_double_and_single_quotes(monkeypatch):
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="BTCC 2018: All the action from Brands Hatch" />'
        '</head><body>'
        '<div data-video-id="12345"></div>'
        "<div data-video-id='67890'></div>"
        '</body></html>'
    )
    ie, captured = _make_extractor_with_webpage(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['url_or_request'] == url
    assert captured['video_id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert result['_type'] == 'playlist'
    assert result['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert len(result['entries']) == 2
    expected_ids = ['12345', '67890']
    for entry, video_id in zip(result['entries'], expected_ids):
        assert entry['_type'] == 'url'
        assert entry['id'] == video_id
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        base_url, smuggled = unsmuggle_url(entry['url'])
        assert base_url == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert smuggled['referrer'] == url
        assert smuggled['geo_ip_blocks'] == [
            '193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21',
        ]


def test_itvbtcc_no_entries_no_title(monkeypatch):
    url = 'https://itv.com/btcc/some-episode-id'
    webpage = '<html><head></head><body><p>No videos here</p></body></html>'
    ie, captured = _make_extractor_with_webpage(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['video_id'] == 'some-episode-id'
    assert result['_type'] == 'playlist'
    assert result['id'] == 'some-episode-id'
    assert result['entries'] == []
    assert result.get('title') is None
    assert 'title' not in result
    assert len(captured['downloader'].warnings) == 1


def test_itvbtcc_single_entry_smuggled_url_details(monkeypatch):
    url = 'https://www.itv.com/btcc/races/my-race-video'
    webpage = (
        '<html><head><meta property="og:title" content="My Race Title"/></head>'
        '<body><span data-video-id="99999"></span></body></html>'
    )
    ie, captured = _make_extractor_with_webpage(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert result['id'] == 'my-race-video'
    assert result['title'] == 'My Race Title'
    assert len(result['entries']) == 1
    entry = result['entries'][0]
    assert entry['id'] == '99999'
    assert entry['ie_key'] == BrightcoveNewIE.ie_key()
    base_url, smuggled = unsmuggle_url(entry['url'])
    assert 'videoId=99999' in base_url
    assert base_url.startswith('http://players.brightcove.net/1582188683001/')
    assert smuggled['referrer'] == url
    assert len(smuggled['geo_ip_blocks']) == 3

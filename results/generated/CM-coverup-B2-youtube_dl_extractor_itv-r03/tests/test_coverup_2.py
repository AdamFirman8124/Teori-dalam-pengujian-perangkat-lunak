# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import pytest
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.utils import unsmuggle_url


TEST_URL = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
PLAYLIST_ID = 'btcc-2018-all-the-action-from-brands-hatch'
EXPECTED_GEO_BLOCKS = ['193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']


class _FakeDownloader(object):
    """Minimal stand-in for YoutubeDL, enough for InfoExtractor helpers."""

    def __init__(self):
        self.params = {'no_color': True}
        self.warnings = []
        self.messages = []

    def report_warning(self, message, *args, **kwargs):
        self.warnings.append(message)

    def report_error(self, message, *args, **kwargs):
        self.messages.append(message)

    def to_screen(self, message, *args, **kwargs):
        self.messages.append(message)

    def to_stdout(self, message, *args, **kwargs):
        self.messages.append(message)

    def trouble(self, *args, **kwargs):
        raise AssertionError('unexpected trouble() call: %r' % (args,))


def _make_extractor_with_webpage(monkeypatch, webpage, captured=None):
    ie = ITVBTCCIE()
    ie.set_downloader(_FakeDownloader())

    def fake_download_webpage(url, video_id, *args, **kwargs):
        if captured is not None:
            captured['url'] = url
            captured['video_id'] = video_id
        return webpage

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    return ie


def test_real_extract_multiple_entries_with_title(monkeypatch):
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="BTCC 2018: All the action from Brands Hatch" />'
        '</head><body>'
        '<div data-video-id="12345"></div>'
        "<div data-video-id='67890'></div>"
        '</body></html>'
    )
    captured = {}
    ie = _make_extractor_with_webpage(monkeypatch, webpage, captured)

    result = ie._real_extract(TEST_URL)

    assert captured['url'] == TEST_URL
    assert captured['video_id'] == PLAYLIST_ID
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert isinstance(result['entries'], list)
    assert len(result['entries']) == 2

    expected_ids = ['12345', '67890']
    for entry, video_id in zip(result['entries'], expected_ids):
        assert entry['_type'] == 'url'
        assert entry['id'] == video_id
        assert entry['ie_key'] == BrightcoveNewIE.ie_key()
        base_url, smuggled = unsmuggle_url(entry['url'])
        assert base_url == ie.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert 'videoId=%s' % video_id in base_url
        assert smuggled['geo_ip_blocks'] == EXPECTED_GEO_BLOCKS
        assert smuggled['referrer'] == TEST_URL


def test_real_extract_no_entries_no_title(monkeypatch):
    webpage = '<html><head></head><body><p>No videos here</p></body></html>'
    captured = {}
    ie = _make_extractor_with_webpage(monkeypatch, webpage, captured)

    result = ie._real_extract(TEST_URL)

    assert captured['url'] == TEST_URL
    assert captured['video_id'] == PLAYLIST_ID
    assert result['_type'] == 'playlist'
    assert result['id'] == PLAYLIST_ID
    assert result['entries'] == []
    # _og_search_title(fatal=False) yields None; playlist_result omits falsy title
    assert result.get('title') is None


def test_real_extract_single_entry_no_og_title(monkeypatch):
    webpage = (
        '<html><head><title>Fallback</title></head><body>'
        '<span data-video-id="99999"></span>'
        '</body></html>'
    )
    ie = _make_extractor_with_webpage(monkeypatch, webpage)

    result = ie._real_extract(TEST_URL)

    assert result['id'] == PLAYLIST_ID
    assert result.get('title') is None
    assert len(result['entries']) == 1
    entry = result['entries'][0]
    assert entry['id'] == '99999'
    assert entry['ie_key'] == BrightcoveNewIE.ie_key()
    base_url, smuggled = unsmuggle_url(entry['url'])
    assert base_url == ie.BRIGHTCOVE_URL_TEMPLATE % '99999'
    assert smuggled['geo_ip_blocks'] == EXPECTED_GEO_BLOCKS
    assert smuggled['referrer'] == TEST_URL

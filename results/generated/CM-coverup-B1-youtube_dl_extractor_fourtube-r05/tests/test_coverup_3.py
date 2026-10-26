# file: project/youtube_dl/extractor/fourtube.py:25-41
# asked: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}

import pytest

from youtube_dl.extractor.fourtube import FourTubeBaseIE


class _FakeDownloader(object):
    """Minimal stand-in for the downloader: _sort_formats only touches
    self._downloader.params, so an object with a params dict is enough."""
    def __init__(self):
        self.params = {}


def _strip_ext(formats):
    """_sort_formats mutates each format by adding an 'ext' key derived
    from the url; remove it so assertions can compare the fields that
    _extract_formats itself produces."""
    for f in formats:
        f.pop('ext', None)
    return formats


class TestFourTubeBaseExtractFormats(object):
    """Coverage tests for FourTubeBaseIE._extract_formats (lines 26-41)."""

    def _make_ie(self, monkeypatch):
        ie = FourTubeBaseIE()
        # _sort_formats accesses self._downloader.params; the default
        # instance attribute is None, so install a fake downloader.
        monkeypatch.setattr(ie, '_downloader', _FakeDownloader())
        # Shadow the class attribute on the instance only, so no class-level
        # state is polluted; the instance is discarded after the test.
        ie._TKN_HOST = 'token.example.com'
        return ie

    def test_extract_formats_builds_token_url_and_sorted_formats(self, monkeypatch):
        ie = self._make_ie(monkeypatch)
        sources = ['720', '240', '1080']  # deliberately unsorted input
        tokens_json = {
            '240': {'token': 'https://cdn.example.com/240.m3u8'},
            '720': {'token': 'https://cdn.example.com/720.m3u8'},
            '1080': {'token': 'https://cdn.example.com/1080.m3u8'},
        }
        captured = {}

        def fake_download_json(token_url, video_id, data=b'', headers=None):
            captured['token_url'] = token_url
            captured['video_id'] = video_id
            captured['data'] = data
            captured['headers'] = headers
            return tokens_json

        monkeypatch.setattr(ie, '_download_json', fake_download_json)

        url = 'https://www.fourtube.com/videos/some-video'
        formats = ie._extract_formats(url, 'vid123', 'media456', sources)

        # Line 26-27: token URL built from _TKN_HOST, media_id and joined sources
        assert captured['token_url'] == (
            'https://token.example.com/media456/desktop/720+240+1080')
        # Line 30: _download_json called with the right video_id and empty body
        assert captured['video_id'] == 'vid123'
        assert captured['data'] == b''
        # Lines 31-32: Origin derived from url scheme/hostname, Referer is url
        assert captured['headers']['Origin'] == 'https://www.fourtube.com'
        assert captured['headers']['Referer'] == url
        # Lines 34-39: one format entry per source, with correct fields
        assert len(formats) == 3
        by_id = {f['format_id']: f for f in formats}
        for src in sources:
            entry = by_id[src + 'p']
            assert entry['url'] == tokens_json[src]['token']
            assert entry['resolution'] == src + 'p'
            assert entry['quality'] == int(src)
        # Line 40: _sort_formats ran -> formats sorted ascending by quality
        qualities = [f['quality'] for f in formats]
        assert qualities == sorted(qualities)
        # Line 41: the (sorted) formats list is returned; drop the 'ext'
        # key that _sort_formats adds as a side effect before comparing.
        assert _strip_ext(formats) == [
            {'url': 'https://cdn.example.com/240.m3u8',
             'format_id': '240p', 'resolution': '240p', 'quality': 240},
            {'url': 'https://cdn.example.com/720.m3u8',
             'format_id': '720p', 'resolution': '720p', 'quality': 720},
            {'url': 'https://cdn.example.com/1080.m3u8',
             'format_id': '1080p', 'resolution': '1080p', 'quality': 1080},
        ]

    def test_extract_formats_single_source(self, monkeypatch):
        ie = self._make_ie(monkeypatch)
        tokens_json = {'360': {'token': 'https://cdn.example.com/360.token'}}
        captured = {}

        def fake_download_json(token_url, video_id, data=b'', headers=None):
            captured['token_url'] = token_url
            captured['headers'] = headers
            return tokens_json

        monkeypatch.setattr(ie, '_download_json', fake_download_json)

        url = 'http://www.porntube.com/videos/other-video'
        formats = ie._extract_formats(url, 'vid999', 'media999', ['360'])

        assert captured['token_url'] == (
            'https://token.example.com/media999/desktop/360')
        # http scheme is preserved in the Origin header
        assert captured['headers']['Origin'] == 'http://www.porntube.com'
        assert captured['headers']['Referer'] == url
        assert _strip_ext(formats) == [{
            'url': 'https://cdn.example.com/360.token',
            'format_id': '360p',
            'resolution': '360p',
            'quality': 360,
        }]

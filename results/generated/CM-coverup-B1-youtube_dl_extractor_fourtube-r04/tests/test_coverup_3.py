# file: project/youtube_dl/extractor/fourtube.py:25-41
# asked: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}

import pytest

from youtube_dl.extractor.fourtube import FourTubeBaseIE


class FakeDownloader(object):
    """Minimal stand-in for YoutubeDL: only .params is needed by _sort_formats."""

    def __init__(self, params=None):
        self.params = params if params is not None else {}


class TestFourTubeBaseExtractFormats(object):
    """Coverage tests for FourTubeBaseIE._extract_formats (lines 26-41)."""

    def _make_ie(self):
        ie = FourTubeBaseIE()
        # Shadow the class attribute on the instance only, so no class-level
        # state is polluted; the instance is discarded after the test.
        ie._TKN_HOST = 'token.example.com'
        # _sort_formats accesses self._downloader.params; without a downloader
        # set, self._downloader is None and sorting raises AttributeError.
        ie.set_downloader(FakeDownloader())
        return ie

    @staticmethod
    def _summary(formats):
        # _sort_formats mutates each format dict (adds 'ext'), so compare only
        # the fields _extract_formats itself is responsible for.
        return [
            (f['url'], f['format_id'], f['resolution'], f['quality'])
            for f in formats
        ]

    def test_extract_formats_builds_token_url_and_sorted_formats(self, monkeypatch):
        ie = self._make_ie()
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

        # Lines 26-27: token URL built from _TKN_HOST, media_id and joined sources
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
        # Line 41: the (sorted) formats list is returned
        assert self._summary(formats) == [
            ('https://cdn.example.com/240.m3u8', '240p', '240p', 240),
            ('https://cdn.example.com/720.m3u8', '720p', '720p', 720),
            ('https://cdn.example.com/1080.m3u8', '1080p', '1080p', 1080),
        ]

    def test_extract_formats_single_source(self, monkeypatch):
        ie = self._make_ie()
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
        assert self._summary(formats) == [
            ('https://cdn.example.com/360.token', '360p', '360p', 360),
        ]

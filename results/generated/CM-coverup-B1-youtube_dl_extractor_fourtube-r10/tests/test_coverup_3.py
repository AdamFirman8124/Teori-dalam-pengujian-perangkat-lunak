# file: project/youtube_dl/extractor/fourtube.py:25-41
# asked: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}

import pytest

from youtube_dl.extractor.fourtube import FourTubeBaseIE


class _FakeFourTubeIE(FourTubeBaseIE):
    IE_NAME = 'fake:fourtube'
    _VALID_URL = r'https?://(?:www\.)?example\.com/(?:v|embed)/(?P<id>[^/?#&]+)'
    _TKN_HOST = 'tkn.example.com'


class _FakeDownloader(object):
    """Stand-in for a YoutubeDL instance; _sort_formats only reads .params."""
    def __init__(self):
        self.params = {}


class _Recorder(object):
    """Minimal call recorder used to stub out extractor methods."""

    def __init__(self, return_value=None, side_effect=None):
        self.return_value = return_value
        self.side_effect = side_effect
        self.calls = []

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        if self.side_effect is not None:
            raise self.side_effect
        return self.return_value

    @property
    def call_count(self):
        return len(self.calls)

    def assert_called_once_with(self, *args, **kwargs):
        assert self.call_count == 1, 'expected 1 call, got %d' % self.call_count
        assert self.calls[0] == (args, kwargs)

    def assert_not_called(self):
        assert self.call_count == 0, 'expected no calls, got %d' % self.call_count


@pytest.fixture
def ie():
    # Fresh extractor instance per test so no state leaks between tests.
    # _downloader is required by the real _sort_formats implementation.
    ie = _FakeFourTubeIE()
    ie._downloader = _FakeDownloader()
    return ie


def test_extract_formats_single_source(ie, monkeypatch):
    download_json = _Recorder(return_value={'480': {'token': 'token-480'}})
    sort_formats = _Recorder()
    monkeypatch.setattr(ie, '_download_json', download_json)
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    url = 'https://www.example.com/v/abc123'
    formats = ie._extract_formats(url, 'abc123', 'media42', ['480'])

    assert formats == [{
        'url': 'token-480',
        'format_id': '480p',
        'resolution': '480p',
        'quality': 480,
    }]

    download_json.assert_called_once_with(
        'https://tkn.example.com/media42/desktop/480',
        'abc123',
        data=b'',
        headers={
            'Origin': 'https://www.example.com',
            'Referer': url,
        },
    )
    sort_formats.assert_called_once_with(formats)
    assert sort_formats.calls[0][0][0] is formats


def test_extract_formats_multiple_sources(ie, monkeypatch):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    download_json = _Recorder(return_value=tokens)
    sort_formats = _Recorder()
    monkeypatch.setattr(ie, '_download_json', download_json)
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    url = 'http://example.com/v/xyz'
    formats = ie._extract_formats(url, 'xyz', 'media7', ['240', '720'])

    assert formats == [
        {'url': 'token-240', 'format_id': '240p', 'resolution': '240p', 'quality': 240},
        {'url': 'token-720', 'format_id': '720p', 'resolution': '720p', 'quality': 720},
    ]

    # Sources are '+' joined into a single token request path.
    download_json.assert_called_once_with(
        'https://tkn.example.com/media7/desktop/240+720',
        'xyz',
        data=b'',
        headers={
            'Origin': 'http://example.com',
            'Referer': url,
        },
    )
    sort_formats.assert_called_once_with(formats)


def test_extract_formats_empty_sources(ie, monkeypatch):
    download_json = _Recorder(return_value={})
    sort_formats = _Recorder()
    monkeypatch.setattr(ie, '_download_json', download_json)
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    url = 'https://www.example.com/v/none'
    formats = ie._extract_formats(url, 'none', 'media0', [])

    assert formats == []
    download_json.assert_called_once_with(
        'https://tkn.example.com/media0/desktop/',
        'none',
        data=b'',
        headers={
            'Origin': 'https://www.example.com',
            'Referer': url,
        },
    )
    sort_formats.assert_called_once_with(formats)


def test_extract_formats_uses_real_sort_formats(ie, monkeypatch):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    download_json = _Recorder(return_value=tokens)
    monkeypatch.setattr(ie, '_download_json', download_json)

    formats = ie._extract_formats(
        'https://www.example.com/v/order', 'order', 'media9', ['720', '240'])

    # Real _sort_formats sorts by ascending quality, so input order is reversed.
    assert [f['format_id'] for f in formats] == ['240p', '720p']
    assert [f['quality'] for f in formats] == [240, 720]
    for fmt in formats:
        assert fmt['url'] == tokens[str(fmt['quality'])]['token']
        assert fmt['resolution'] == fmt['format_id']


def test_extract_formats_propagates_download_error(ie, monkeypatch):
    download_json = _Recorder(side_effect=RuntimeError('boom'))
    sort_formats = _Recorder()
    monkeypatch.setattr(ie, '_download_json', download_json)
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    with pytest.raises(RuntimeError, match='boom'):
        ie._extract_formats(
            'https://www.example.com/v/err', 'err', 'media1', ['480'])

    sort_formats.assert_not_called()


def test_extract_formats_missing_token_key(ie, monkeypatch):
    # Only one of the requested sources has a token: building formats must fail.
    download_json = _Recorder(return_value={'480': {'token': 'token-480'}})
    sort_formats = _Recorder()
    monkeypatch.setattr(ie, '_download_json', download_json)
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    with pytest.raises(KeyError):
        ie._extract_formats(
            'https://www.example.com/v/partial', 'partial', 'media2',
            ['480', '720'])

    sort_formats.assert_not_called()

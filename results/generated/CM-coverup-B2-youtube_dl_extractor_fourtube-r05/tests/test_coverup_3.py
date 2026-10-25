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
    """Stand-in for the real downloader; only .params is accessed."""

    def __init__(self, params=None):
        self.params = params if params is not None else {}


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

    def assert_called_once_with(self, *args, **kwargs):
        assert len(self.calls) == 1, 'expected exactly 1 call, got %d' % len(self.calls)
        call_args, call_kwargs = self.calls[0]
        assert call_args == args, 'positional args mismatch: %r != %r' % (call_args, args)
        assert call_kwargs == kwargs, 'keyword args mismatch: %r != %r' % (call_kwargs, kwargs)

    def assert_not_called(self):
        assert not self.calls, 'expected no calls, got %r' % (self.calls,)


@pytest.fixture
def ie():
    # Fresh extractor instance per test so no state leaks between tests.
    return _FakeFourTubeIE()


@pytest.fixture
def patch_method(monkeypatch):
    def _patch(ie, name, return_value=None, side_effect=None):
        recorder = _Recorder(return_value=return_value, side_effect=side_effect)
        monkeypatch.setattr(ie, name, recorder)
        return recorder
    return _patch


def test_extract_formats_single_source(ie, patch_method):
    download_json = patch_method(
        ie, '_download_json', return_value={'480': {'token': 'token-480'}})
    sort_formats = patch_method(ie, '_sort_formats')

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


def test_extract_formats_multiple_sources(ie, patch_method):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    download_json = patch_method(ie, '_download_json', return_value=tokens)
    sort_formats = patch_method(ie, '_sort_formats')

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


def test_extract_formats_empty_sources(ie, patch_method):
    download_json = patch_method(ie, '_download_json', return_value={})
    sort_formats = patch_method(ie, '_sort_formats')

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
    monkeypatch.setattr(
        ie, '_download_json', _Recorder(return_value=tokens))
    # The real _sort_formats accesses self._downloader.params; provide a
    # minimal fake downloader so no real network/downloader state is touched.
    monkeypatch.setattr(ie, '_downloader', _FakeDownloader())

    formats = ie._extract_formats(
        'https://www.example.com/v/order', 'order', 'media9', ['720', '240'])

    # Real _sort_formats orders formats; with equal preference/protocol the
    # format_id tiebreak puts the lower resolution first.
    assert [f['format_id'] for f in formats] == ['240p', '720p']
    assert [f['quality'] for f in formats] == [240, 720]
    for fmt in formats:
        assert fmt['url'] == tokens[str(fmt['quality'])]['token']
        assert fmt['resolution'] == fmt['format_id']


def test_extract_formats_propagates_download_error(ie, patch_method):
    download_json = patch_method(
        ie, '_download_json', side_effect=RuntimeError('boom'))
    sort_formats = patch_method(ie, '_sort_formats')

    with pytest.raises(RuntimeError, match='boom'):
        ie._extract_formats(
            'https://www.example.com/v/err', 'err', 'media1', ['480'])

    download_json.assert_called_once_with(
        'https://tkn.example.com/media1/desktop/480',
        'err',
        data=b'',
        headers={
            'Origin': 'https://www.example.com',
            'Referer': 'https://www.example.com/v/err',
        },
    )
    sort_formats.assert_not_called()


def test_extract_formats_missing_token_key(ie, patch_method):
    # Only one of the requested sources has a token: building formats must fail.
    download_json = patch_method(
        ie, '_download_json', return_value={'480': {'token': 'token-480'}})
    sort_formats = patch_method(ie, '_sort_formats')

    with pytest.raises(KeyError):
        ie._extract_formats(
            'https://www.example.com/v/partial', 'partial', 'media2',
            ['480', '720'])

    download_json.assert_called_once_with(
        'https://tkn.example.com/media2/desktop/480+720',
        'partial',
        data=b'',
        headers={
            'Origin': 'https://www.example.com',
            'Referer': 'https://www.example.com/v/partial',
        },
    )
    sort_formats.assert_not_called()

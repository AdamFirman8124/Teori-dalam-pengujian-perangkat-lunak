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
    def __init__(self):
        self.params = {}


@pytest.fixture
def ie():
    # Fresh extractor instance per test so no state leaks between tests.
    return _FakeFourTubeIE()


@pytest.fixture
def calls():
    return {'download_json': [], 'sort_formats': []}


def _patch_download_json(monkeypatch, ie, calls, tokens=None, exc=None):
    def fake_download_json(url_or_request, video_id, *args, **kwargs):
        calls['download_json'].append({
            'url_or_request': url_or_request,
            'video_id': video_id,
            'args': args,
            'kwargs': kwargs,
        })
        if exc is not None:
            raise exc
        return tokens

    monkeypatch.setattr(ie, '_download_json', fake_download_json)


def _patch_sort_formats(monkeypatch, ie, calls):
    def fake_sort_formats(formats, field_preference=None):
        calls['sort_formats'].append(formats)

    monkeypatch.setattr(ie, '_sort_formats', fake_sort_formats)


def test_extract_formats_single_source(ie, calls, monkeypatch):
    _patch_download_json(monkeypatch, ie, calls, tokens={'480': {'token': 'token-480'}})
    _patch_sort_formats(monkeypatch, ie, calls)

    url = 'https://www.example.com/v/abc123'
    formats = ie._extract_formats(url, 'abc123', 'media42', ['480'])

    assert formats == [{
        'url': 'token-480',
        'format_id': '480p',
        'resolution': '480p',
        'quality': 480,
    }]

    assert len(calls['download_json']) == 1
    dl = calls['download_json'][0]
    assert dl['url_or_request'] == 'https://tkn.example.com/media42/desktop/480'
    assert dl['video_id'] == 'abc123'
    assert dl['kwargs'].get('data') == b''
    assert dl['kwargs'].get('headers') == {
        'Origin': 'https://www.example.com',
        'Referer': url,
    }

    assert len(calls['sort_formats']) == 1
    assert calls['sort_formats'][0] is formats


def test_extract_formats_multiple_sources(ie, calls, monkeypatch):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    _patch_download_json(monkeypatch, ie, calls, tokens=tokens)
    _patch_sort_formats(monkeypatch, ie, calls)

    url = 'http://example.com/v/xyz'
    formats = ie._extract_formats(url, 'xyz', 'media7', ['240', '720'])

    assert formats == [
        {'url': 'token-240', 'format_id': '240p', 'resolution': '240p', 'quality': 240},
        {'url': 'token-720', 'format_id': '720p', 'resolution': '720p', 'quality': 720},
    ]

    # Sources are '+' joined into a single token request path.
    assert len(calls['download_json']) == 1
    dl = calls['download_json'][0]
    assert dl['url_or_request'] == 'https://tkn.example.com/media7/desktop/240+720'
    assert dl['video_id'] == 'xyz'
    assert dl['kwargs'].get('data') == b''
    assert dl['kwargs'].get('headers') == {
        'Origin': 'http://example.com',
        'Referer': url,
    }

    assert len(calls['sort_formats']) == 1
    assert calls['sort_formats'][0] is formats


def test_extract_formats_empty_sources(ie, calls, monkeypatch):
    _patch_download_json(monkeypatch, ie, calls, tokens={})
    _patch_sort_formats(monkeypatch, ie, calls)

    url = 'https://www.example.com/v/none'
    formats = ie._extract_formats(url, 'none', 'media0', [])

    assert formats == []
    assert len(calls['download_json']) == 1
    dl = calls['download_json'][0]
    assert dl['url_or_request'] == 'https://tkn.example.com/media0/desktop/'
    assert dl['video_id'] == 'none'
    assert dl['kwargs'].get('data') == b''
    assert dl['kwargs'].get('headers') == {
        'Origin': 'https://www.example.com',
        'Referer': url,
    }
    assert len(calls['sort_formats']) == 1
    assert calls['sort_formats'][0] == []


def test_extract_formats_uses_real_sort_formats(ie, monkeypatch):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    # Use a properly initialized calls dict (previous bug: passed a bare {}).
    calls = {'download_json': [], 'sort_formats': []}
    _patch_download_json(monkeypatch, ie, calls, tokens=tokens)
    # Real _sort_formats reads self._downloader.params; provide a fake one.
    monkeypatch.setattr(ie, '_downloader', _FakeDownloader(), raising=False)

    formats = ie._extract_formats(
        'https://www.example.com/v/order', 'order', 'media9', ['720', '240'])

    # Real _sort_formats sorts by ascending quality, so input order is reversed.
    assert [f['format_id'] for f in formats] == ['240p', '720p']
    assert [f['quality'] for f in formats] == [240, 720]
    for fmt in formats:
        assert fmt['url'] == tokens[str(fmt['quality'])]['token']
        assert fmt['resolution'] == fmt['format_id']
    # The download call was recorded correctly.
    assert len(calls['download_json']) == 1
    assert calls['download_json'][0]['url_or_request'] == \
        'https://tkn.example.com/media9/desktop/720+240'


def test_extract_formats_propagates_download_error(ie, calls, monkeypatch):
    _patch_download_json(monkeypatch, ie, calls, exc=RuntimeError('boom'))
    _patch_sort_formats(monkeypatch, ie, calls)

    with pytest.raises(RuntimeError, match='boom'):
        ie._extract_formats(
            'https://www.example.com/v/err', 'err', 'media1', ['480'])

    assert len(calls['download_json']) == 1
    assert calls['sort_formats'] == []


def test_extract_formats_missing_token_key(ie, calls, monkeypatch):
    # Only one of the requested sources has a token: building formats must fail.
    _patch_download_json(monkeypatch, ie, calls, tokens={'480': {'token': 'token-480'}})
    _patch_sort_formats(monkeypatch, ie, calls)

    with pytest.raises(KeyError):
        ie._extract_formats(
            'https://www.example.com/v/partial', 'partial', 'media2',
            ['480', '720'])

    assert len(calls['download_json']) == 1
    assert calls['sort_formats'] == []

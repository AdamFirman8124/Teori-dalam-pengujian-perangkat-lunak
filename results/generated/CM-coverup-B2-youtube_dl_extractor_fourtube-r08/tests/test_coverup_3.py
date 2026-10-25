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
    def __init__(self, params=None):
        self.params = params or {}


@pytest.fixture
def ie():
    # Fresh extractor instance per test so no state leaks between tests.
    return _FakeFourTubeIE()


def test_extract_formats_single_source(ie, monkeypatch):
    calls = []

    def fake_download_json(url, video_id, **kwargs):
        calls.append((url, video_id, kwargs))
        return {'480': {'token': 'token-480'}}

    sorted_calls = []
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: sorted_calls.append(formats))

    url = 'https://www.example.com/v/abc123'
    formats = ie._extract_formats(url, 'abc123', 'media42', ['480'])

    assert formats == [{
        'url': 'token-480',
        'format_id': '480p',
        'resolution': '480p',
        'quality': 480,
    }]

    assert calls == [(
        'https://tkn.example.com/media42/desktop/480',
        'abc123',
        {'data': b'', 'headers': {
            'Origin': 'https://www.example.com',
            'Referer': url,
        }},
    )]
    assert len(sorted_calls) == 1
    assert sorted_calls[0] is formats


def test_extract_formats_multiple_sources(ie, monkeypatch):
    calls = []
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }

    def fake_download_json(url, video_id, **kwargs):
        calls.append((url, video_id, kwargs))
        return tokens

    sorted_calls = []
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: sorted_calls.append(formats))

    url = 'http://example.com/v/xyz'
    formats = ie._extract_formats(url, 'xyz', 'media7', ['240', '720'])

    assert formats == [
        {'url': 'token-240', 'format_id': '240p', 'resolution': '240p', 'quality': 240},
        {'url': 'token-720', 'format_id': '720p', 'resolution': '720p', 'quality': 720},
    ]

    # Sources are '+' joined into a single token request path.
    assert calls == [(
        'https://tkn.example.com/media7/desktop/240+720',
        'xyz',
        {'data': b'', 'headers': {
            'Origin': 'http://example.com',
            'Referer': url,
        }},
    )]
    assert len(sorted_calls) == 1
    assert sorted_calls[0] is formats


def test_extract_formats_empty_sources(ie, monkeypatch):
    calls = []

    def fake_download_json(url, video_id, **kwargs):
        calls.append((url, video_id, kwargs))
        return {}

    sorted_calls = []
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: sorted_calls.append(formats))

    url = 'https://www.example.com/v/none'
    formats = ie._extract_formats(url, 'none', 'media0', [])

    assert formats == []
    assert calls == [(
        'https://tkn.example.com/media0/desktop/',
        'none',
        {'data': b'', 'headers': {
            'Origin': 'https://www.example.com',
            'Referer': url,
        }},
    )]
    assert len(sorted_calls) == 1
    assert sorted_calls[0] is formats


def test_extract_formats_uses_real_sort_formats(ie, monkeypatch):
    tokens = {
        '240': {'token': 'http://cdn.example.com/video-240.mp4'},
        '720': {'token': 'http://cdn.example.com/video-720.mp4'},
    }
    monkeypatch.setattr(ie, '_download_json', lambda *a, **kw: tokens)
    monkeypatch.setattr(ie, '_downloader', _FakeDownloader({'prefer_free_formats': False}))

    formats = ie._extract_formats(
        'https://www.example.com/v/order', 'order', 'media9', ['720', '240'])

    # Real _sort_formats sorts by ascending quality, so input order is reversed.
    assert [f['format_id'] for f in formats] == ['240p', '720p']
    assert [f['quality'] for f in formats] == [240, 720]
    for fmt in formats:
        assert fmt['url'] == tokens[str(fmt['quality'])]['token']
        assert fmt['resolution'] == fmt['format_id']


def test_extract_formats_propagates_download_error(ie, monkeypatch):
    def failing_download_json(*args, **kwargs):
        raise RuntimeError('boom')

    sorted_calls = []
    monkeypatch.setattr(ie, '_download_json', failing_download_json)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: sorted_calls.append(formats))

    with pytest.raises(RuntimeError, match='boom'):
        ie._extract_formats(
            'https://www.example.com/v/err', 'err', 'media1', ['480'])

    assert sorted_calls == []


def test_extract_formats_missing_token_key(ie, monkeypatch):
    # Only one of the requested sources has a token: building formats must fail.
    monkeypatch.setattr(
        ie, '_download_json', lambda *a, **kw: {'480': {'token': 'token-480'}})

    sorted_calls = []
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: sorted_calls.append(formats))

    with pytest.raises(KeyError):
        ie._extract_formats(
            'https://www.example.com/v/partial', 'partial', 'media2',
            ['480', '720'])

    assert sorted_calls == []

# file: project/youtube_dl/extractor/fourtube.py:25-41
# asked: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}

from unittest.mock import Mock

import pytest

from youtube_dl.extractor.fourtube import FourTubeBaseIE


class _FakeFourTubeIE(FourTubeBaseIE):
    IE_NAME = 'fake:fourtube'
    _VALID_URL = r'https?://(?:www\.)?example\.com/(?:v|embed)/(?P<id>[^/?#&]+)'
    _TKN_HOST = 'tkn.example.com'


@pytest.fixture
def ie():
    # Fresh extractor instance per test so no state leaks between tests.
    return _FakeFourTubeIE()


def test_extract_formats_single_source(ie, monkeypatch):
    download_json = Mock(return_value={'480': {'token': 'token-480'}})
    sort_formats = Mock()
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
    assert sort_formats.call_args[0][0] is formats


def test_extract_formats_multiple_sources(ie, monkeypatch):
    tokens = {
        '240': {'token': 'token-240'},
        '720': {'token': 'token-720'},
    }
    download_json = Mock(return_value=tokens)
    sort_formats = Mock()
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
    download_json = Mock(return_value={})
    sort_formats = Mock()
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
    monkeypatch.setattr(ie, '_download_json', Mock(return_value=tokens))
    # Real _sort_formats needs a downloader with a params dict.
    monkeypatch.setattr(ie, '_downloader', Mock(params={}), raising=False)

    formats = ie._extract_formats(
        'https://www.example.com/v/order', 'order', 'media9', ['720', '240'])

    # Real _sort_formats runs without error and keeps every format intact.
    assert len(formats) == 2
    assert {f['format_id'] for f in formats} == {'240p', '720p'}
    for fmt in formats:
        assert fmt['url'] == tokens[str(fmt['quality'])]['token']
        assert fmt['resolution'] == fmt['format_id']
        assert isinstance(fmt['quality'], int)


def test_extract_formats_propagates_download_error(ie, monkeypatch):
    monkeypatch.setattr(
        ie, '_download_json', Mock(side_effect=RuntimeError('boom')))
    sort_formats = Mock()
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    with pytest.raises(RuntimeError, match='boom'):
        ie._extract_formats(
            'https://www.example.com/v/err', 'err', 'media1', ['480'])

    sort_formats.assert_not_called()


def test_extract_formats_missing_token_key(ie, monkeypatch):
    # Only one of the requested sources has a token: building formats must fail.
    monkeypatch.setattr(
        ie, '_download_json',
        Mock(return_value={'480': {'token': 'token-480'}}))
    sort_formats = Mock()
    monkeypatch.setattr(ie, '_sort_formats', sort_formats)

    with pytest.raises(KeyError):
        ie._extract_formats(
            'https://www.example.com/v/partial', 'partial', 'media2',
            ['480', '720'])

    sort_formats.assert_not_called()

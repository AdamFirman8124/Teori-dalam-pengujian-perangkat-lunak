# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest

from youtube_dl.socks import ProxyError


@pytest.fixture
def codes(monkeypatch):
    mapping = {ProxyError.ERR_SUCCESS: 'succeeded', 0x05: 'connection refused'}
    monkeypatch.setattr(ProxyError, 'CODES', mapping, raising=False)
    return mapping


def test_proxy_error_known_code_derives_message(codes, monkeypatch):
    code = ProxyError.ERR_SUCCESS
    expected_msg = codes[code]

    err = ProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, expected_msg)

    monkeypatch.undo()
    assert not hasattr(ProxyError, 'CODES')


def test_proxy_error_unknown_code_uses_unknown_error(codes):
    code = 0xFF
    assert code not in codes

    err = ProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, 'unknown error')


def test_proxy_error_falsy_mapped_message_uses_unknown_error(codes):
    code = 0x05
    codes[code] = ''

    err = ProxyError(code)

    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved(codes):
    code = ProxyError.ERR_SUCCESS

    err = ProxyError(code, 'custom failure')

    assert err.args == (code, 'custom failure')


def test_proxy_error_no_arguments():
    err = ProxyError()

    assert isinstance(err, OSError)
    assert err.args == (None, None)


def test_proxy_error_message_without_code():
    err = ProxyError(msg='only message')

    assert err.args == (None, 'only message')

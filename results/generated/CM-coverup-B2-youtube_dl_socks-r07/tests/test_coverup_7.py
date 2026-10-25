# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest

from youtube_dl.socks import ProxyError


@pytest.fixture
def codes(monkeypatch):
    table = {0x00: 'succeeded', 0x01: 'general failure', 0x02: None}
    monkeypatch.setattr(ProxyError, 'CODES', table, raising=False)
    return table


def test_proxy_error_known_code_derives_message(codes):
    code = ProxyError.ERR_SUCCESS
    assert code in codes
    expected_msg = codes[code]
    assert expected_msg

    err = ProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, expected_msg)


def test_proxy_error_falsy_code_message_falls_back(codes):
    code = 0x02
    assert code in codes
    assert not codes[code]

    err = ProxyError(code)

    assert err.args == (code, 'unknown error')


def test_proxy_error_unknown_code_uses_unknown_error(codes):
    code = 0xFF
    assert code not in codes

    err = ProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved(codes):
    code = 0x01

    err = ProxyError(code, 'custom failure')

    assert err.args == (code, 'custom failure')


def test_proxy_error_no_arguments(codes):
    err = ProxyError()

    assert isinstance(err, OSError)
    assert err.args == (None, None)


def test_proxy_error_message_without_code(codes):
    err = ProxyError(msg='only message')

    assert err.args == (None, 'only message')


def test_codes_attribute_removed_after_fixture(monkeypatch):
    monkeypatch.setattr(ProxyError, 'CODES', {0x00: 'ok'}, raising=False)
    assert ProxyError.CODES == {0x00: 'ok'}
    monkeypatch.undo()
    assert not hasattr(ProxyError, 'CODES')

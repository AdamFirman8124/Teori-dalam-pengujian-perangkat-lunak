# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import socket

import pytest

from youtube_dl.socks import ProxyError


@pytest.fixture
def codes(monkeypatch):
    table = {0x00: 'succeeded', 0x01: 'general SOCKS server failure'}
    monkeypatch.setattr(ProxyError, 'CODES', table, raising=False)
    return table


def test_proxy_error_known_code_derives_message(codes):
    code = ProxyError.ERR_SUCCESS
    assert code in codes

    err = ProxyError(code)

    assert isinstance(err, socket.error)
    assert isinstance(err, OSError)
    assert err.args == (code, codes[code])


def test_proxy_error_unknown_code_uses_unknown_error(codes):
    code = 0xFF
    assert code not in codes

    err = ProxyError(code)

    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved(codes):
    code = 0x01

    err = ProxyError(code, 'custom failure')

    assert err.args == (code, 'custom failure')


def test_proxy_error_explicit_message_does_not_consult_codes(monkeypatch):
    class ExplodingCodes(dict):
        def get(self, key, default=None):
            raise AssertionError('CODES must not be consulted when msg is given')

    monkeypatch.setattr(ProxyError, 'CODES', ExplodingCodes(), raising=False)

    err = ProxyError(0x01, 'explicit')

    assert err.args == (0x01, 'explicit')


def test_proxy_error_no_arguments(codes):
    err = ProxyError()

    assert isinstance(err, socket.error)
    assert err.args == (None, None)


def test_proxy_error_message_without_code(codes):
    err = ProxyError(msg='only message')

    assert err.args == (None, 'only message')


def test_proxy_error_codes_attribute_removed_after_fixture(codes):
    assert ProxyError.CODES is codes

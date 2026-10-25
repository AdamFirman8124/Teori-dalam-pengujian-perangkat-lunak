# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest

from youtube_dl.socks import ProxyError, Socks5Error


def test_proxy_error_known_code_derives_message():
    # ProxyError itself has no CODES; the lookup path is exercised via a
    # subclass that defines one (e.g. Socks5Error).
    codes = getattr(Socks5Error, 'CODES', None)
    assert codes, 'Socks5Error must define a CODES mapping for this test'

    code = next(iter(codes))
    expected_msg = codes[code]

    err = Socks5Error(code)

    assert isinstance(err, ProxyError)
    assert isinstance(err, OSError)
    assert err.args == (code, expected_msg)


def test_proxy_error_unknown_code_uses_unknown_error():
    # Pick a code that is not present in the subclass CODES mapping.
    codes = getattr(Socks5Error, 'CODES', {})
    code = 0xFF
    while code in codes:
        code += 1

    err = Socks5Error(code)

    assert isinstance(err, ProxyError)
    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved():
    err = ProxyError(0x01, 'custom failure')

    assert isinstance(err, OSError)
    assert err.args == (0x01, 'custom failure')


def test_proxy_error_no_arguments():
    err = ProxyError()

    assert isinstance(err, OSError)
    assert err.args == (None, None)


def test_proxy_error_message_without_code():
    err = ProxyError(msg='only message')

    assert err.args == (None, 'only message')

# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import youtube_dl.socks as socks


class _TestProxyError(socks.ProxyError):
    """Subclass providing the CODES mapping that ProxyError.__init__ expects."""
    CODES = {
        0x00: 'request granted',
        0x5B: 'request rejected or failed',
    }


def test_proxy_error_known_code_derives_message():
    code = _TestProxyError.ERR_SUCCESS
    expected_msg = _TestProxyError.CODES[code]
    assert expected_msg

    err = _TestProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, expected_msg)
    assert err.args[0] == code
    assert err.args[1] == expected_msg


def test_proxy_error_unknown_code_uses_unknown_error():
    code = 0xFF
    assert code not in _TestProxyError.CODES

    err = _TestProxyError(code)

    assert isinstance(err, OSError)
    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved():
    code = 0x5B

    err = _TestProxyError(code, 'custom failure')

    assert err.args == (code, 'custom failure')


def test_proxy_error_no_arguments():
    err = _TestProxyError()

    assert isinstance(err, OSError)
    assert err.args == (None, None)


def test_proxy_error_message_without_code():
    err = _TestProxyError(msg='only message')

    assert err.args == (None, 'only message')

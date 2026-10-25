# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

from youtube_dl.socks import ProxyError, Socks5Error


def test_proxy_error_known_code_derives_message():
    code = Socks5Error.ERR_GENERAL_FAILURE
    expected_msg = Socks5Error.CODES[code]
    assert expected_msg

    err = Socks5Error(code)

    assert isinstance(err, OSError)
    assert err.args == (code, expected_msg)
    assert err.args[0] == code
    assert err.args[1] == expected_msg


def test_proxy_error_unknown_code_uses_unknown_error():
    code = 99
    assert code not in Socks5Error.CODES

    err = Socks5Error(code)

    assert isinstance(err, OSError)
    assert err.args == (code, 'unknown error')


def test_proxy_error_explicit_message_is_preserved():
    code = Socks5Error.ERR_GENERAL_FAILURE

    err = Socks5Error(code, 'custom failure')

    assert err.args == (code, 'custom failure')


def test_proxy_error_no_arguments():
    err = ProxyError()

    assert isinstance(err, OSError)
    assert err.args == (None, None)


def test_proxy_error_message_without_code():
    err = ProxyError(msg='only message')

    assert err.args == (None, 'only message')

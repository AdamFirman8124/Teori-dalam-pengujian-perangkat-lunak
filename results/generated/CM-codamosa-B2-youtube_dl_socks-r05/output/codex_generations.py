

# Generated at 2026-11-03 02:50:07.139448
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is set
    assert s._proxy is None

    # Default parameters: rdns=True, username=None, password=None
    s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 1080)
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, 'proxy.example.com', 1080, None, None, True)
    assert s._proxy.type == ProxyType.SOCKS5
    assert s._proxy.host == 'proxy.example.com'
    assert s._proxy.port == 1080
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # All parameters specified
    s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 9050, rdns=False,
               username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS4, '127.0.0.1', 9050, 'user', 'pass', False)

    # SOCKS4A proxy type
    s.setproxy(ProxyType.SOCKS4A, 'proxy.example.org', 8080)
    assert s._proxy.type == ProxyType.SOCKS4A
    assert s._proxy.host == 'proxy.example.org'
    assert s._proxy.port == 8080

    # Setting a proxy twice should overwrite the previous one
    s.setproxy(ProxyType.SOCKS5, 'other.example.com', 3128)
    assert s._proxy.host == 'other.example.com'
    assert s._proxy.port == 3128

    # Invalid proxy type should raise AssertionError
    try:
        s.setproxy(3, 'proxy.example.net', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError(
            'Expected AssertionError for invalid proxytype')

    # Proxy should remain unchanged after failed setproxy call
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, 'other.example.com', 3128, None, None, True)

    s.close()

# Generated at 2026-11-03 02:51:30.291963
# Unit test for constructor of class Socks4Command
def test_Socks4Command():
    command = Socks4Command()
    assert command is not None
    assert command.CMD_CONNECT == 0x01
    assert command.CMD_BIND == 0x02

# Generated at 2026-11-03 02:52:22.613832
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    err = InvalidVersionError(5, 4)
    assert err.args[0] == 0
    assert err.args[1] == 'Invalid response version from server. Expected 05 got 04'

    err = InvalidVersionError(0x5, 0x5A)
    assert err.args == (0, 'Invalid response version from server. Expected 05 got 5a')

    err = InvalidVersionError(SOCKS5_VERSION, SOCKS4_REPLY_VERSION)
    assert err.args == (0, 'Invalid response version from server. Expected 05 got 00')

    err = InvalidVersionError(0xFF, 0x1)
    assert err.args == (0, 'Invalid response version from server. Expected ff got 01')

# Generated at 2026-11-03 02:56:22.849745
# Unit test for method connect_ex of class sockssocket
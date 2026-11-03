

# Generated at 2026-11-02 19:05:35.692024
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    address_type = Socks5AddressType()
    assert address_type is not None
    assert Socks5AddressType.ATYP_IPV4 == 0x01
    assert Socks5AddressType.ATYP_DOMAINNAME == 0x03
    assert Socks5AddressType.ATYP_IPV6 == 0x04

# Generated at 2026-11-02 19:06:36.600168
# Unit test for constructor of class Proxy
def test_Proxy():
    # Construct with positional arguments
    proxy = Proxy(ProxyType.SOCKS5, '127.0.0.1', 1080, 'user', 'pass', True)
    assert proxy.type == ProxyType.SOCKS5
    assert proxy.host == '127.0.0.1'
    assert proxy.port == 1080
    assert proxy.username == 'user'
    assert proxy.password == 'pass'
    assert proxy.remote_dns is True

    # Construct with keyword arguments
    proxy = Proxy(type=ProxyType.SOCKS4, host='proxy.example.com', port=9050,
                  username=None, password=None, remote_dns=False)
    assert proxy.type == ProxyType.SOCKS4
    assert proxy.host == 'proxy.example.com'
    assert proxy.port == 9050
    assert proxy.username is None
    assert proxy.password is None
    assert proxy.remote_dns is False

    # Verify namedtuple tuple-like behavior
    assert tuple(proxy) == (ProxyType.SOCKS4, 'proxy.example.com', 9050,
                            None, None, False)
    assert len(proxy) == 6
    assert Proxy._fields == ('type', 'host', 'port', 'username',
                             'password', 'remote_dns')

    # Two proxies with the same values should compare equal
    proxy_a = Proxy(ProxyType.SOCKS4A, 'localhost', 8080, 'u', 'p', True)
    proxy_b = Proxy(ProxyType.SOCKS4A, 'localhost', 8080, 'u', 'p', True)
    assert proxy_a == proxy_b
# nonce:6a523ec7

# Generated at 2026-11-02 19:10:35.697363
# Unit test for constructor of class ProxyError
def test_ProxyError():
    import socket

    # Constructor with no arguments
    err = ProxyError()
    assert isinstance(err, socket.error)
    assert err.args == (None, None)

    # Constructor with both code and msg
    err = ProxyError(0x01, 'custom error message')
    assert isinstance(err, socket.error)
    assert err.args == (0x01, 'custom error message')

    # Constructor with only a code: ProxyError has no CODES attribute,
    # so looking up the message raises AttributeError
    try:
        ProxyError(0x01)
    except AttributeError:
        pass
    else:
        raise AssertionError('AttributeError not raised for missing CODES lookup')

    # Constructor with code=None and an explicit msg
    err = ProxyError(None, 'explicit message')
    assert err.args == (None, 'explicit message')

# Generated at 2026-11-02 19:13:06.133493
# Unit test for constructor of class ProxyError
def test_ProxyError():
    # Constructor with no arguments: code and msg default to None
    err = ProxyError()
    assert err.args == (None, None)

    # Constructor with only a message
    err = ProxyError(msg='connection to proxy failed')
    assert err.args == (None, 'connection to proxy failed')

    # Constructor with both code and message: message is kept as given
    err = ProxyError(0x01, 'general SOCKS server failure')
    assert err.args == (0x01, 'general SOCKS server failure')

    # ProxyError must be an instance of socket.error
    assert isinstance(err, socket.error)

    # Constructor with only a code: ProxyError itself has no CODES mapping,
    # so building the default message raises AttributeError
    try:
        ProxyError(0x01)
    except AttributeError:
        pass
    else:
        raise AssertionError('expected AttributeError when no CODES lookup is possible')
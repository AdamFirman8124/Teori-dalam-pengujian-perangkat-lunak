

# Generated at 2026-11-02 18:39:57.986421
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from unittest import mock

    sock = sockssocket()
    try:
        # All data arrives in a single recv call
        with mock.patch.object(sock, 'recv', side_effect=[b'hello']):
            assert sock.recvall(5) == b'hello'

        # Data arrives in multiple recv calls
        with mock.patch.object(sock, 'recv', side_effect=[b'he', b'll', b'o']):
            assert sock.recvall(5) == b'hello'

        # A later recv returns more data than requested; all of it is accumulated
        with mock.patch.object(sock, 'recv', side_effect=[b'ab', b'cdefgh']):
            assert sock.recvall(5) == b'abcdefgh'

        # Empty recv signals EOF and must raise EOFError with the missing byte count
        with mock.patch.object(sock, 'recv', return_value=b''):
            try:
                sock.recvall(5)
            except EOFError as e:
                assert '5 bytes missing' in str(e)
            else:
                raise AssertionError('EOFError not raised')
    finally:
        sock.close()

# Generated at 2026-11-02 18:41:56.030677
# Unit test for constructor of class Socks5Error
def test_Socks5Error():
    # Test with a known error code
    error = Socks5Error(0x01)
    assert error.errno == 0x01
    assert error.args == (0x01, 'general SOCKS server failure')

    # Test with a known error code (connection refused)
    error = Socks5Error(0x05)
    assert error.args == (0x05, 'Connection refused')

    # Test with an unknown error code
    error = Socks5Error(0x77)
    assert error.args == (0x77, 'unknown error')

    # Test with explicit code and message
    error = Socks5Error(0x02, 'custom message')
    assert error.args == (0x02, 'custom message')

    # Test with no arguments
    error = Socks5Error()
    assert error.args == (None, None)

    # Test that it is an instance of ProxyError and socket.error
    error = Socks5Error(0x01)
    assert isinstance(error, ProxyError)
    assert isinstance(error, socket.error)

# Generated at 2026-11-02 18:43:27.671689
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    # Test with a known error code from CODES
    error = Socks4Error(91)
    assert error.args == (91, 'request rejected or failed')

    # Test with another known error code
    error = Socks4Error(92)
    assert error.args == (92, 'request rejected because SOCKS server cannot connect to identd on the client')

    # Test with a third known error code
    error = Socks4Error(93)
    assert error.args == (93, 'request rejected because the client program and identd report different user-ids')

    # Test with an unknown error code
    error = Socks4Error(94)
    assert error.args == (94, 'unknown error')

    # Test with explicit code and custom message
    error = Socks4Error(91, 'custom message')
    assert error.args == (91, 'custom message')

    # Test with no arguments
    error = Socks4Error()
    assert error.args == (None, None)

    # Test class attribute ERR_SUCCESS
    assert Socks4Error.ERR_SUCCESS == 90

    # Test that it is a subclass of ProxyError (and thus socket.error)
    error = Socks4Error(91)
    assert isinstance(error, ProxyError)
    assert isinstance(error, socket.error)

# Generated at 2026-11-02 18:44:49.144106
# Unit test for constructor of class Socks5Auth
def test_Socks5Auth():
    auth = Socks5Auth()
    assert auth.AUTH_NONE == 0x00
    assert auth.AUTH_GSSAPI == 0x01
    assert auth.AUTH_USER_PASS == 0x02
    assert auth.AUTH_NO_ACCEPTABLE == 0xFF

# Generated at 2026-11-02 18:46:22.250187
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    # SOCKS4 proxy with default parameters
    s = sockssocket()
    assert s._proxy is None
    s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
    assert s._proxy == Proxy(ProxyType.SOCKS4, '127.0.0.1', 1080, None, None, True)
    s.close()

    # SOCKS4A proxy with remote DNS disabled
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS4A, 'proxy.example.com', 9050, rdns=False)
    assert s._proxy == Proxy(ProxyType.SOCKS4A, 'proxy.example.com', 9050, None, None, False)
    s.close()

    # SOCKS5 proxy with authentication credentials
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS5, '10.0.0.1', 3128, rdns=True, username='user', password='pass')
    assert s._proxy == Proxy(ProxyType.SOCKS5, '10.0.0.1', 3128, 'user', 'pass', True)
    s.close()

    # Overwriting an existing proxy configuration
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
    s.setproxy(ProxyType.SOCKS5, 'localhost', 8080, username='foo', password='bar')
    assert s._proxy == Proxy(ProxyType.SOCKS5, 'localhost', 8080, 'foo', 'bar', True)
    s.close()

    # Invalid proxy type must raise AssertionError and leave proxy unset
    s = sockssocket()
    raised = False
    try:
        s.setproxy(123, '127.0.0.1', 1080)
    except AssertionError:
        raised = True
    assert raised
    assert s._proxy is None
    s.close()
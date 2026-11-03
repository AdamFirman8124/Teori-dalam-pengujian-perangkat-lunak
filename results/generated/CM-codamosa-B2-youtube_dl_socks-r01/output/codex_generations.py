

# Generated at 2026-11-01 23:06:42.005112
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():import unittest
from unittest import mock


class TestSockssocketConnectEx(unittest.TestCase):

    def _make_socket(self):
        # Avoid creating a real OS socket
        with mock.patch('socket.socket.__init__', return_value=None):
            s = sockssocket()
        return s

    def test_connect_ex_without_proxy_calls_connect_ex_directly(self):
        s = self._make_socket()
        with mock.patch('socket.socket.connect_ex', return_value=0) as mock_connect_ex:
            result = s.connect_ex(('example.com', 80))

        mock_connect_ex.assert_called_once_with(s, ('example.com', 80))
        self.assertEqual(result, 0)

    def test_connect_ex_with_socks5_proxy_connects_to_proxy(self):
        s = self._make_socket()
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 1080)

        with mock.patch('socket.socket.connect_ex', return_value=0) as mock_connect_ex, \
                mock.patch.object(s, '_setup_socks5', return_value=None) as mock_setup:
            result = s.connect_ex(('example.com', 80))

        mock_connect_ex.assert_called_once_with(s, ('proxy.example.com', 1080))
        mock_setup.assert_called_once_with(('example.com', 80))
        self.assertEqual(result, 0)

    def test_connect_ex_with_socks4_proxy_connects_to_proxy(self):
        s = self._make_socket()
        s.setproxy(ProxyType.SOCKS4, '10.0.0.1', 1080)

        with mock.patch('socket.socket.connect_ex', return_value=0) as mock_connect_ex, \
                mock.patch.object(s, '_setup_socks4', return_value=None) as mock_setup:
            result = s.connect_ex(('example.com', 80))

        mock_connect_ex.assert_called_once_with(s, ('10.0.0.1', 1080))
        mock_setup.assert_called_once_with(('example.com', 80))
        self.assertEqual(result, 0)

    def test_connect_ex_with_socks4a_proxy_connects_to_proxy(self):
        s = self._make_socket()
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.2', 9050, rdns=True)

        with mock.patch('socket.socket.connect_ex', return_value=0) as mock_connect_ex, \
                mock.patch.object(s, '_setup_socks4a', return_value=None) as mock_setup:
            result = s.connect_ex(('example.com', 443))

        mock_connect_ex.assert_called_once_with(s, ('10.0.0.2', 9050))
        mock_setup.assert_called_once_with(('example.com', 443))
        self.assertEqual(result, 0)

    def test_connect_ex_returns_nonzero_result_without_setup(self):
        s = self._make_socket()
        s.setproxy(ProxyType.SOCKS5, '10.0.0.3', 1080)

        with mock.patch('socket.socket.connect_ex', return_value=111) as mock_connect_ex, \
                mock.patch.object(s, '_setup_socks5') as mock_setup:
            result = s.connect_ex(('example.com', 80))

        mock_connect_ex.assert_called_once_with(s, ('10.0.0.3', 1080))
        mock_setup.assert_not_called()
        self.assertEqual(result, 111)

    def test_connect_ex_result_zero_still_runs_setup(self):
        s = self._make_socket()
        s.setproxy(ProxyType.SOCKS5, '10.0.0.4', 1080, rdns=False,
                   username='user', password='pass')

        with mock.patch('socket.socket.connect_ex', return_value=0) as mock_connect_ex, \
                mock.patch.object(s, '_setup_socks5', return_value=None) as mock_setup:
            result = s.connect_ex(('192.168.1.1', 8080))

        mock_connect_ex.assert_called_once_with(s, ('10.0.0.4', 1080))
        mock_setup.assert_called_once_with(('192.168.1.1', 8080))
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-01 23:07:38.328827
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    import struct
    from unittest import mock

    # Case 1: no proxy configured -> delegate directly to socket.socket.connect_ex
    s = sockssocket()
    with mock.patch.object(socket.socket, 'connect_ex', return_value=1234) as mock_ce:
        result = s.connect_ex(('127.0.0.1', 80))
    mock_ce.assert_called_once_with(s, ('127.0.0.1', 80))
    assert result == 1234

    # Case 2: proxy configured -> connects to proxy, performs SOCKS5 handshake
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS5, '10.0.0.1', 1080)
    s.sendall = mock.Mock()
    s.recvall = mock.Mock(side_effect=[
        struct.pack('!BB', SOCKS5_VERSION, Socks5Auth.AUTH_NONE),          # method selection reply
        struct.pack('!BBBB', SOCKS5_VERSION, 0x00, 0, Socks5AddressType.ATYP_IPV4),  # reply header
        socket.inet_aton('10.0.0.2'),                                      # bound address
        struct.pack('!H', 443),                                            # bound port
    ])
    with mock.patch.object(socket.socket, 'connect_ex', return_value=0) as mock_ce:
        result = s.connect_ex(('127.0.0.1', 80))
    mock_ce.assert_called_once_with(s, ('10.0.0.1', 1080))
    # auth negotiation packet: version, one method (no-auth)
    assert s.sendall.call_args_list[0][0][0] == struct.pack(
        '!BBB', SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)
    # connect request packet: version, CMD_CONNECT, reserved, ATYP_IPV4, ip, port
    assert s.sendall.call_args_list[1][0][0] == (
        struct.pack('!BBBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0,
                    Socks5AddressType.ATYP_IPV4)
        + socket.inet_aton('127.0.0.1') + struct.pack('!H', 80))
    assert result == 0

    # Case 3: underlying connect fails -> return code immediately, no SOCKS setup
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS4, '10.0.0.1', 1080)
    with mock.patch.object(socket.socket, 'connect_ex', return_value=111) as mock_ce, \
            mock.patch.object(sockssocket, '_setup_socks4') as mock_setup:
        result = s.connect_ex(('127.0.0.1', 80))
    mock_ce.assert_called_once_with(s, ('10.0.0.1', 1080))
    mock_setup.assert_not_called()
    assert result == 111

# Generated at 2026-11-01 23:08:20.276355
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    from unittest import mock

    # --- Scenario 1: real loopback connection without a proxy ---
    # With no proxy configured, connect_ex must behave like the regular
    # socket method and return 0 on a successful connection.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 0))
    server.listen(1)
    srv_addr = server.getsockname()

    sock = sockssocket()
    try:
        ret = sock.connect_ex(srv_addr)
        assert ret == 0, 'expected successful connection, got error %r' % ret
    finally:
        sock.close()
        server.close()

    # --- Scenario 2: no proxy -> delegation to socket.socket.connect_ex ---
    sock = sockssocket()
    try:
        with mock.patch.object(
                socket.socket, 'connect_ex', return_value=0) as mocked:
            ret = sock.connect_ex(('127.0.0.1', 12345))
        mocked.assert_called_once_with(sock, ('127.0.0.1', 12345))
        assert ret == 0
    finally:
        sock.close()

    # --- Scenario 3: proxy configured -> proxy endpoint is dialed first ---
    # Reserve a local port and release it so nothing listens there.
    holder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    holder.bind(('127.0.0.1', 0))
    dead_port = holder.getsockname()[1]
    holder.close()

    sock = sockssocket()
    try:
        sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', dead_port)
        with mock.patch.object(
                socket.socket, 'connect_ex',
                return_value=111) as mocked:  # 111 == ECONNREFUSED
            ret = sock.connect_ex(('example.com', 80))
        # The connection attempt must have gone to the proxy, not the
        # destination, and the error code must be propagated instead of
        # raising an exception.
        mocked.assert_called_once_with(sock, ('127.0.0.1', dead_port))
        assert ret == 111
    finally:
        sock.close()

# Generated at 2026-11-01 23:09:02.804692
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # Full arguments
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080, rdns=True,
                   username='user', password='pass')
        assert s._proxy == Proxy(ProxyType.SOCKS5, '127.0.0.1', 1080,
                                 'user', 'pass', True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username == 'user'
        assert s._proxy.password == 'pass'
        assert s._proxy.remote_dns is True

        # Default arguments
        s.setproxy(ProxyType.SOCKS4, 'localhost', 9050)
        assert s._proxy == Proxy(ProxyType.SOCKS4, 'localhost', 9050,
                                 None, None, True)

        # rdns=False
        s.setproxy(ProxyType.SOCKS4A, 'proxy.example.com', 1080, rdns=False)
        assert s._proxy == Proxy(ProxyType.SOCKS4A, 'proxy.example.com', 1080,
                                 None, None, False)

        # Invalid proxy type must trigger the assertion
        try:
            s.setproxy(99, '127.0.0.1', 1080)
            assert False, 'expected AssertionError for invalid proxytype'
        except AssertionError:
            pass

        # Proxy must remain unchanged after failed call
        assert s._proxy == Proxy(ProxyType.SOCKS4A, 'proxy.example.com', 1080,
                                 None, None, False)
    finally:
        s.close()

# Generated at 2026-11-01 23:09:24.820376
# Unit test for constructor of class Socks5Auth
def test_Socks5Auth():
    # Instantiate the class
    socks5_auth = Socks5Auth()
    # Verify the instance is of the correct type
    assert isinstance(socks5_auth, Socks5Auth)
    # Verify the authentication method constants
    assert socks5_auth.AUTH_NONE == 0x00
    assert socks5_auth.AUTH_GSSAPI == 0x01
    assert socks5_auth.AUTH_USER_PASS == 0x02
    assert socks5_auth.AUTH_NO_ACCEPTABLE == 0xFF

# Generated at 2026-11-01 23:10:23.804048
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    # Constructor with only a code: message is resolved from the CODES table
    err = Socks4Error(91)
    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (91, 'request rejected or failed')

    # Unknown code falls back to the generic message
    err = Socks4Error(99)
    assert err.args == (99, 'unknown error')

    # Explicit message is passed through unchanged
    err = Socks4Error(91, 'custom failure')
    assert err.args == (91, 'custom failure')

    # No arguments at all
    err = Socks4Error()
    assert err.args == (None, None)

    # Class-level constants
    assert Socks4Error.ERR_SUCCESS == 90
    assert Socks4Error.CODES[91] == 'request rejected or failed'
    assert Socks4Error.CODES[92] == 'request rejected because SOCKS server cannot connect to identd on the client'
    assert Socks4Error.CODES[93] == 'request rejected because the client program and identd report different user-ids'

# Generated at 2026-11-01 23:11:18.491270
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest.mock as mock

    sock = sockssocket()

    # Data arrives complete in a single recv call
    with mock.patch.object(sock, 'recv', side_effect=[b'hello']) as mock_recv:
        assert sock.recvall(5) == b'hello'
        mock_recv.assert_called_once_with(5)

    # Data arrives in multiple chunks; recv must be called with the
    # remaining byte count each time
    with mock.patch.object(sock, 'recv', side_effect=[b'he', b'll', b'o']) as mock_recv:
        assert sock.recvall(5) == b'hello'
        assert mock_recv.call_args_list == [mock.call(5), mock.call(3), mock.call(1)]

    # recv returns more bytes than requested; only the needed part is kept
    with mock.patch.object(sock, 'recv', side_effect=[b'abcdefg']):
        assert sock.recvall(3) == b'abc'

    # recv returns fewer bytes than requested; loop continues correctly
    with mock.patch.object(sock, 'recv', side_effect=[b'ab', b'cdef']):
        assert sock.recvall(6) == b'abcdef'

    # Zero-byte request returns immediately without calling recv
    with mock.patch.object(
            sock, 'recv',
            side_effect=AssertionError('recv should not be called')) as mock_recv:
        assert sock.recvall(0) == b''
        assert mock_recv.call_count == 0

    # Premature EOF (recv returns empty) raises EOFError reporting
    # how many bytes are still missing
    with mock.patch.object(sock, 'recv', side_effect=[b'abc', b'']):
        try:
            sock.recvall(6)
        except EOFError as e:
            assert '3 bytes missing' in str(e)
        else:
            raise AssertionError('EOFError not raised')

    sock.close()

# Generated at 2026-11-01 23:12:40.921204
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()

    # Case 1: data arrives one byte at a time
    pending = [bytes([c]) for c in b'HelloWorld']

    def fake_recv_byte(bufsize):
        if pending:
            return pending.pop(0)
        return b''

    sock.recv = fake_recv_byte
    try:
        assert sock.recvall(10) == b'HelloWorld'
    finally:
        del sock.recv

    # Case 2: everything is returned by a single recv call
    pending = [b'all-at-once']

    def fake_recv_all(bufsize):
        if pending:
            return pending.pop(0)
        return b''

    sock.recv = fake_recv_all
    try:
        assert sock.recvall(11) == b'all-at-once'
    finally:
        del sock.recv

    # Case 3: recv returns fewer bytes than requested, requiring multiple calls
    pending = [b'ab', b'cd']

    def fake_recv_partial(bufsize):
        if pending:
            return pending.pop(0)
        return b''

    sock.recv = fake_recv_partial
    try:
        assert sock.recvall(4) == b'abcd'
    finally:
        del sock.recv

    # Case 4: connection closed before all bytes were received -> EOFError
    pending = [b'short']

    def fake_recv_short(bufsize):
        if pending:
            return pending.pop(0)
        return b''

    sock.recv = fake_recv_short
    try:
        try:
            sock.recvall(100)
        except EOFError as e:
            assert 'bytes missing' in str(e)
        else:
            raise AssertionError('Expected EOFError for incomplete data')
    finally:
        del sock.recv

    sock.close()

# Generated at 2026-11-01 23:13:02.735017
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    from socks import (
        sockssocket, Proxy, ProxyType,
        SOCKS4_VERSION, SOCKS5_VERSION,
    )

    # Default: no proxy set
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    assert s._proxy is None

    # SOCKS5 proxy with all parameters
    s.setproxy(
        ProxyType.SOCKS5, '192.168.0.1', 9050, rdns=True,
        username='user', password='pass')
    expected = Proxy(
        type=ProxyType.SOCKS5, host='192.168.0.1', port=9050,
        username='user', password='pass', remote_dns=True)
    assert s._proxy == expected

    # SOCKS4 proxy with defaults (no rdns, no auth)
    s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
    expected = Proxy(
        type=ProxyType.SOCKS4, host='127.0.0.1', port=1080,
        username=None, password=None, remote_dns=True)
    assert s._proxy == expected

    # SOCKS4A with remote_dns disabled
    s.setproxy(ProxyType.SOCKS4A, 'proxy.example.com', 8080, rdns=False)
    expected = Proxy(
        type=ProxyType.SOCKS4A, host='proxy.example.com', port=8080,
        username=None, password=None, remote_dns=False)
    assert s._proxy == expected

    # Setting a proxy twice should overwrite the previous one
    s.setproxy(ProxyType.SOCKS5, '10.0.0.1', 3128)
    assert s._proxy.host == '10.0.0.1'
    assert s._proxy.port == 3128

    # Invalid proxy type must raise AssertionError
    try:
        s.setproxy(99, '127.0.0.1', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('AssertionError not raised for invalid proxytype')

    # Proxy type constants sanity check
    assert ProxyType.SOCKS4 == 0
    assert ProxyType.SOCKS4A == 1
    assert ProxyType.SOCKS5 == 2

    s.close()

# Generated at 2026-11-01 23:13:23.518556
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from unittest import mock

    sock = sockssocket()

    # All data received in a single recv call
    with mock.patch.object(sock, 'recv', return_value=b'hello'):
        assert sock.recvall(5) == b'hello'

    # Data received across multiple recv calls is accumulated
    with mock.patch.object(sock, 'recv', side_effect=[b'hello', b' ', b'world']):
        assert sock.recvall(11) == b'hello world'

    # recv is called with exactly the number of remaining bytes
    calls = []

    def recv_side_effect(cnt):
        calls.append(cnt)
        return b'x' * cnt

    with mock.patch.object(sock, 'recv', side_effect=recv_side_effect):
        assert sock.recvall(4) == b'xxxx'
    assert calls == [4]

    # Zero bytes requested returns empty data without calling recv
    with mock.patch.object(sock, 'recv', side_effect=AssertionError('recv should not be called')):
        assert sock.recvall(0) == b''

    # Connection closed before all data received raises EOFError
    with mock.patch.object(sock, 'recv', side_effect=[b'abc', b'de', b'']):
        try:
            sock.recvall(10)
        except EOFError as e:
            assert '5 bytes missing' in str(e)
        else:
            raise AssertionError('EOFError not raised')

    sock.close()

# Generated at 2026-11-01 23:14:32.026528
# Unit test for method recvall of class sockssocket

# Generated at 2026-11-01 23:15:54.051836
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    server = socket.socket()
    server.bind(('127.0.0.1', 0))
    server.listen(1)
    port = server.getsockname()[1]

    client = sockssocket()
    client.connect(('127.0.0.1', port))
    conn, _ = server.accept()

    conn.sendall(b'hello')
    conn.sendall(b' world')

    assert client.recvall(11) == b'hello world'

    conn.close()
    client.close()
    server.close()
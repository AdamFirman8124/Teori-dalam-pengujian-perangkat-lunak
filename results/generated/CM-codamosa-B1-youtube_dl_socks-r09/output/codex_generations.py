

# Generated at 2026-10-24 06:20:53.133530
# Unit test for constructor of class Socks5Error
def test_Socks5Error():
    # known code -> message looked up from CODES
    err = Socks5Error(0x01)
    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (0x01, 'general SOCKS server failure')
    assert err.args[0] == Socks5Error.ERR_GENERAL_FAILURE

    # all documented codes
    expected = {
        0x01: 'general SOCKS server failure',
        0x02: 'connection not allowed by ruleset',
        0x03: 'Network unreachable',
        0x04: 'Host unreachable',
        0x05: 'Connection refused',
        0x06: 'TTL expired',
        0x07: 'Command not supported',
        0x08: 'Address type not supported',
        0xFE: 'unknown username or invalid password',
        0xFF: 'all offered authentication methods were rejected',
    }
    assert Socks5Error.CODES == expected
    for code, msg in expected.items():
        e = Socks5Error(code)
        assert e.args == (code, msg)

    # unknown code -> fallback message
    e = Socks5Error(0x09)
    assert e.args == (0x09, 'unknown error')

    # explicit msg is not overwritten by CODES lookup
    e = Socks5Error(0x01, 'custom')
    assert e.args == (0x01, 'custom')

    e = Socks5Error(0x09, 'custom')
    assert e.args == (0x09, 'custom')

    # default: no code, no message
    e = Socks5Error()
    assert e.args == (None, None)

# Generated at 2026-10-24 06:21:07.146050
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    try:
        from unittest import mock
    except ImportError:  # Python 2 compatibility
        import mock

    address = ('example.com', 443)
    expected_result = 0

    with mock.patch.object(
            sockssocket, '_make_proxy',
            autospec=True,
            return_value=expected_result) as make_proxy:
        sock = sockssocket()
        try:
            result = sock.connect_ex(address)

            assert result == expected_result
            make_proxy.assert_called_once_with(
                sock, socket.socket.connect_ex, address)
        finally:
            sock.close()

# Generated at 2026-10-24 06:21:13.394401
# Unit test for constructor of class sockssocket
def test_sockssocket():
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert isinstance(sock, socket.socket)
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_STREAM
        assert sock._proxy is None
    finally:
        sock.close()

# Generated at 2026-10-24 06:21:17.794106
# Unit test for constructor of class sockssocket
def test_sockssocket():sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:21:22.557772
# Unit test for constructor of class sockssocket

# Generated at 2026-10-24 06:21:29.570583
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    address_type = Socks5AddressType()

    assert address_type.ATYP_IPV4 == 0x01
    assert address_type.ATYP_DOMAINNAME == 0x03
    assert address_type.ATYP_IPV6 == 0x04

# Generated at 2026-10-24 06:21:39.321377
# Unit test for constructor of class Socks4Command
def test_Socks4Command():
    # Instantiation trivially succeeds (no __init__)
    cmd = Socks4Command()
    assert cmd is not None
    assert Socks4Command.CMD_CONNECT == 0x01
    assert Socks4Command.CMD_BIND == 0x02


def test_Socks5Command_inherits_Socks4Command():
    assert Socks5Command.CMD_CONNECT == 0x01
    assert Socks5Command.CMD_BIND == 0x02
    assert Socks5Command.CMD_UDP_ASSOCIATE == 0x03
    assert issubclass(Socks5Command, Socks4Command)


def test_Socks5Auth_constants():
    assert Socks5Auth.AUTH_NONE == 0x00
    assert Socks5Auth.AUTH_GSSAPI == 0x01
    assert Socks5Auth.AUTH_USER_PASS == 0x02
    assert Socks5Auth.AUTH_NO_ACCEPTABLE == 0xFF


def test_Socks5AddressType_constants():
    assert Socks5AddressType.ATYP_IPV4 == 0x01
    assert Socks5AddressType.ATYP_DOMAINNAME == 0x03
    assert Socks5AddressType.ATYP_IPV6 == 0x04


def test_ProxyType_constants():
    assert ProxyType.SOCKS4 == 0
    assert ProxyType.SOCKS4A == 1
    assert ProxyType.SOCKS5 == 2


def test_ProxyError_resolves_known_code():
    err = Socks5Error(0x05)
    assert err.args[1] == 'Connection refused'


def test_ProxyError_unknown_code():
    err = Socks4Error(99)
    assert err.args[1] == 'unknown error'


def test_setproxy_stores_proxy():
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 9050,
               rdns=True, username='u', password='p')
    assert s._proxy == Proxy(ProxyType.SOCKS5, '127.0.0.1', 9050, 'u', 'p', True)
    s.close()


def test_setproxy_rejects_bad_type():
    s = sockssocket()
    try:
        s.setproxy(99, '127.0.0.1', 9050)
        assert False, 'expected AssertionError'
    except AssertionError:
        pass
    finally:
        s.close()

# Generated at 2026-10-24 06:21:49.845639
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:21:59.367832
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:01.784999
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:22:04.201021
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:22:17.082764
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 06:22:36.030171
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class ChunkedSocket(sockssocket):
        def __init__(self, chunks):
            super(ChunkedSocket, self).__init__()
            self.chunks = collections.deque(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            if not self.chunks:
                return b''

            chunk = self.chunks.popleft()
            if len(chunk) > size:
                self.chunks.appendleft(chunk[size:])
                chunk = chunk[:size]
            return chunk

    sock = ChunkedSocket([b'ab', b'c', b'def'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 3]
    finally:
        sock.close()

    # Verify that an early EOF is reported.
    sock = ChunkedSocket([b'ab', b''])
    try:
        try:
            sock.recvall(3)
        except EOFError as error:
            assert str(error) == '1 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 06:22:37.402517
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:22:38.895704
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:40.271076
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:41.584328
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:22:42.989577
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:44.525981
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:45.838096
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:22:47.291477
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:22:49.928951
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:22:52.356082
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:22:54.758126
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:22:57.176639
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:22:59.588832
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:02.003642
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:04.420546
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:06.832528
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:09.249178
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:11.662199
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:23:14.090692
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:23:21.393063
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 06:23:40.233150
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_calls = []

        def recv(self, size):
            self.recv_calls.append(size)
            return next(self.chunks)

    # Verify that recvall combines partial reads.
    fake_socket = FakeSocket([b'ab', b'cde', b'f'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_calls == [6, 4, 1]

    # Verify that an early EOF raises EOFError.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('EOFError was not raised')

# Generated at 2026-10-24 06:23:57.936066
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import pytest

    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.recv_calls = []

        def recv(self, count):
            self.recv_calls.append(count)
            return self.chunks.pop(0) if self.chunks else b''

    # It should combine partial reads and request only the remaining bytes.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_calls == [6, 4, 3]

    # It should raise EOFError if the connection closes prematurely.
    fake_socket = FakeSocket([b'ab', b'c', b''])

    with pytest.raises(EOFError, match=r'^3 bytes missing$'):
        sockssocket.recvall(fake_socket, 6)

# Generated at 2026-10-24 06:24:13.308815
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks, b'')

    # recvall must combine partial reads.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 3]

    # An EOF before all requested bytes arrive must raise EOFError.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 06:24:15.818028
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:24:18.235000
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:24:24.573337
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 06:24:43.927787
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:24:45.359555
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 06:24:59.595191
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            if not self.chunks:
                return b''
            chunk = self.chunks.pop(0)
            assert len(chunk) <= size
            return chunk

    # Data arriving in multiple chunks is combined.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    # An EOF before all requested bytes arrive raises EOFError.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 06:25:02.010460
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:04.425681
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:06.842974
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:09.255302
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:11.670407
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:14.084985
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:16.499997
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:18.914338
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:21.330370
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:23.745297
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:26.158031
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:28.574210
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:25:42.192487
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        assert s._proxy is None

        s.setproxy(ProxyType.SOCKS5, "127.0.0.1", 1080)
        assert s._proxy == Proxy(ProxyType.SOCKS5, "127.0.0.1", 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == "127.0.0.1"
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        s.setproxy(ProxyType.SOCKS4, "10.0.0.1", 9050, rdns=False, username="user", password="pass")
        assert s._proxy == Proxy(ProxyType.SOCKS4, "10.0.0.1", 9050, "user", "pass", False)

        s.setproxy(ProxyType.SOCKS4A, "proxy.example.com", 8080, True, "alice", "secret")
        assert s._proxy.type == ProxyType.SOCKS4A
        assert s._proxy.host == "proxy.example.com"
        assert s._proxy.port == 8080
        assert s._proxy.username == "alice"
        assert s._proxy.password == "secret"
        assert s._proxy.remote_dns is True

        try:
            s.setproxy(999, "127.0.0.1", 1080)
        except AssertionError:
            pass
        else:
            raise AssertionError("module_0.setproxy() did not reject invalid proxy type")
        assert s._proxy.type == ProxyType.SOCKS4A
    finally:
        s.close()

# Generated at 2026-10-24 06:25:43.511666
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:44.957060
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:25:46.348235
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:25:47.718307
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:25:49.159625
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:25:50.578795
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:26:09.636470
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, chunks):
            super(StubSocket, self).__init__()
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return self.chunks.pop(0)

    sock = StubSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 2]
    finally:
        sock.close()

    # Verify that an early EOF raises the documented error.
    sock = StubSocket([b'ab', b''])
    try:
        try:
            sock.recvall(4)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 06:26:12.139504
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:14.559262
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:16.972348
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:19.385754
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:21.802200
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:24.216631
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:26.630187
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:29.047583
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:31.466196
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:33.879099
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:36.294813
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:38.710122
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:41.127517
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:43.541780
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:45.955178
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:26:48.372582
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:50.786288
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:53.204801
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:55.621304
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:26:58.041554
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:27:00.456898
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:27:03.025212
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        assert s._proxy is None

        s.setproxy(ProxyType.SOCKS5, "127.0.0.1", 1080)
        assert s._proxy == Proxy(ProxyType.SOCKS5, "127.0.0.1", 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == "127.0.0.1"
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        s.setproxy(ProxyType.SOCKS4, "10.0.0.1", 9050, rdns=False, username="user", password="pass")
        assert s._proxy == Proxy(ProxyType.SOCKS4, "10.0.0.1", 9050, "user", "pass", False)

        s.setproxy(ProxyType.SOCKS4A, "proxy.example.com", 8080, True, "alice", "secret")
        assert s._proxy.type == ProxyType.SOCKS4A
        assert s._proxy.host == "proxy.example.com"
        assert s._proxy.port == 8080
        assert s._proxy.username == "alice"
        assert s._proxy.password == "secret"
        assert s._proxy.remote_dns is True

        try:
            s.setproxy(999, "127.0.0.1", 1080)
        except AssertionError:
            pass
        else:
            raise AssertionError("module_0.setproxy() did not reject invalid proxy type")
        assert s._proxy.type == ProxyType.SOCKS4A
    finally:
        s.close()

# Generated at 2026-10-24 06:27:16.313508
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)

        def recv(self, count):
            chunk = next(self.chunks, b'')
            assert len(chunk) <= count
            return chunk

    fake_socket = FakeSocket([b'hello', b' ', b'world'])

    result = sockssocket.recvall(fake_socket, 11)

    assert result == b'hello world'

# Generated at 2026-10-24 06:27:35.345573
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, responses):
            super(FakeSocksSocket, self).__init__()
            self.responses = iter(responses)
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return next(self.responses)

    # Verify that fragmented data is collected completely.
    sock = FakeSocksSocket([b'ab', b'cde', b'f'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 1]
    finally:
        sock.close()

    # Verify that an early EOF raises an informative error.
    sock = FakeSocksSocket([b'abc', b''])
    try:
        try:
            sock.recvall(5)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 06:28:26.682742
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class PartialRecvSocket(sockssocket):
        def __init__(self, chunks):
            super(PartialRecvSocket, self).__init__(
                socket.AF_INET, socket.SOCK_STREAM)
            self.chunks = list(chunks)
            self.requested_counts = []

        def recv(self, cnt):
            self.requested_counts.append(cnt)
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            if len(chunk) > cnt:
                self.chunks.insert(0, chunk[cnt:])
                chunk = chunk[:cnt]
            return chunk

    sock = PartialRecvSocket([b'ab', b'cde', b'f'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.requested_counts == [6, 4, 1]

        sock.chunks = [b'ab', b'']
        try:
            sock.recvall(4)
        except EOFError as exc:
            assert str(exc) == '2 bytes missing'
        else:
            raise AssertionError('module_0.recvall() did not raise EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 06:28:28.017179
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:28:29.417134
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:28:30.848835
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:28:32.302185
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:28:33.824423
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:28:35.353390
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:28:48.460405
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)

        def recv(self, count):
            return next(self.chunks)[:count]

    fake_socket = FakeSocket([b'hello', b' ', b'world'])

    result = sockssocket.recvall(fake_socket, 11)

    assert result == b'hello world'

# Generated at 2026-10-24 06:28:50.885139
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:28:53.306143
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:28:55.721036
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:28:58.134761
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:00.547270
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:02.963340
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:05.377341
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:29:07.790210
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:29:10.206018
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:29:12.621902
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:15.033991
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:17.446467
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:19.861541
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:29:21.310972
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 06:29:36.199486
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self):
            self.chunks = iter([b'ab', b'c', b'def'])
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks)

    fake_socket = FakeSocket()

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 3]

# Generated at 2026-10-24 06:29:58.093164
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest


# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall(monkeypatch):
    chunks = collections.deque([b'ab', b'c', b'def'])
    requested_sizes = []

    def fake_recv(self, size):
        requested_sizes.append(size)
        return chunks.popleft()

    monkeypatch.setattr(sockssocket, 'recv', fake_recv)

    sock = sockssocket()
    try:
        assert sock.recvall(6) == b'abcdef'
        assert requested_sizes == [6, 4, 3]

        # An empty read before receiving all requested bytes indicates EOF.
        chunks.extend([b'ab', b''])
        requested_sizes[:] = []

        with pytest.raises(EOFError, match='2 bytes missing'):
            sock.recvall(4)

        assert requested_sizes == [4, 2]
    finally:
        sock.close()

# Generated at 2026-10-24 06:30:00.508761
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:02.923771
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:05.432811
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:07.845186
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:30:10.258288
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:30:12.673961
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 06:30:15.090121
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:17.500524
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:19.914997
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:22.330313
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:24.751975
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 06:30:26.467626
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 06:30:47.214560
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return next(self.chunks, b'')

    # It should combine partial reads until the requested count is reached.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    # It should raise EOFError if the connection closes too early.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as exc:
        assert str(exc) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')
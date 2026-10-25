

# Generated at 2026-10-25 00:38:54.334603
# Unit test for constructor of class Socks5Error
def test_Socks5Error():
    error = Socks5Error(Socks5Error.ERR_GENERAL_FAILURE)
    assert error.args == (
        Socks5Error.ERR_GENERAL_FAILURE,
        'general SOCKS server failure',
    )

    unknown_error = Socks5Error(0x99)
    assert unknown_error.args == (0x99, 'unknown error')

    custom_error = Socks5Error(0x01, 'custom message')
    assert custom_error.args == (0x01, 'custom message')

# Generated at 2026-10-25 00:39:20.560471
# Unit test for constructor of class Proxy
def test_Proxy():
    # Construct with positional args in field order
    proxy = Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 1080, 'user', 'pass', True)

    assert proxy.type == ProxyType.SOCKS5
    assert proxy.host == '127.0.0.1'
    assert proxy.port == 1080
    assert proxy.username == 'user'
    assert proxy.password == 'pass'
    assert proxy.remote_dns is True

    # Construct with keyword args
    proxy = Proxy(
        type=ProxyType.SOCKS4A, host='proxy.example.com', port=9050,
        username=None, password=None, remote_dns=False)

    assert proxy.type == ProxyType.SOCKS4A
    assert proxy.host == 'proxy.example.com'
    assert proxy.port == 9050
    assert proxy.username is None
    assert proxy.password is None
    assert proxy.remote_dns is False

    # Tuple equality (namedtuple behavior)
    assert proxy == (ProxyType.SOCKS4A, 'proxy.example.com', 9050, None, None, False)

    # Immutable: assignment must raise AttributeError
    try:
        proxy.host = 'other.example.com'
    except AttributeError:
        pass
    else:
        raise AssertionError('Proxy should be immutable')

    # Length and field names
    assert len(proxy) == 6
    assert proxy._fields == (
        'type', 'host', 'port', 'username', 'password', 'remote_dns')

    print('test_Proxy passed.')

# Generated at 2026-10-25 00:39:41.541807
# Unit test for constructor of class Proxy
def test_Proxy():
    proxy = Proxy(
        ProxyType.SOCKS5,
        '127.0.0.1',
        1080,
        'username',
        'password',
        True,
    )

    assert proxy.type == ProxyType.SOCKS5
    assert proxy.host == '127.0.0.1'
    assert proxy.port == 1080
    assert proxy.username == 'username'
    assert proxy.password == 'password'
    assert proxy.remote_dns is True

# Generated at 2026-10-25 00:39:48.100731
# Unit test for constructor of class ProxyType
def test_ProxyType():
    proxy_type = ProxyType()

    assert proxy_type.SOCKS4 == 0
    assert proxy_type.SOCKS4A == 1
    assert proxy_type.SOCKS5 == 2

# Generated at 2026-10-25 00:39:54.549935
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    error = Socks4Error(91)
    assert error.args == (91, 'request rejected or failed')

    unknown_error = Socks4Error(255)
    assert unknown_error.args == (255, 'unknown error')

    custom_error = Socks4Error(92, 'custom message')
    assert custom_error.args == (92, 'custom message')

# Generated at 2026-10-25 00:40:11.423762
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, responses):
            super(FakeSocksSocket, self).__init__()
            self.responses = list(responses)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return self.responses.pop(0) if self.responses else b''

    sock = FakeSocksSocket([b'ab', b'c', b'def'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.requested_sizes == [6, 4, 3]
    finally:
        sock.close()

    sock = FakeSocksSocket([b'ab', b''])
    try:
        try:
            sock.recvall(4)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('module_0.recvall() did not raise EOFError')
    finally:
        sock.close()

# Generated at 2026-10-25 00:40:14.084721
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 00:40:15.417531
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:16.745811
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:18.087893
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:40:23.013860
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:40:25.677014
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 00:40:27.022461
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:28.346287
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:46.862737
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    try:
        with patch.object(
            sockssocket,
            'recv',
            side_effect=[b'ab', b'cde', b'f'],
        ) as recv:
            assert sock.recvall(6) == b'abcdef'
            assert recv.call_args_list == [call(6), call(4), call(1)]

        with patch.object(
            sockssocket,
            'recv',
            side_effect=[b'ab', b''],
        ):
            with pytest.raises(EOFError, match=r'4 bytes missing'):
                sock.recvall(6)
    finally:
        sock.close()

# Generated at 2026-10-25 00:40:49.521318
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 00:40:50.956945
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:52.282948
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:54.949647
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 00:40:56.394871
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:40:57.833252
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:41:19.155962
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, chunks):
            super(FakeSocksSocket, self).__init__()
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return self.chunks.pop(0) if self.chunks else b''

    # Data split across multiple recv() calls is combined correctly.
    sock = FakeSocksSocket([b'ab', b'cd', b'e'])
    try:
        assert sock.recvall(5) == b'abcde'
        assert sock.recv_sizes == [5, 3, 1]
        assert sock.recvall(0) == b''
    finally:
        sock.close()

    # EOF before receiving the requested number of bytes raises EOFError.
    sock = FakeSocksSocket([b'ab', b''])
    try:
        try:
            sock.recvall(3)
        except EOFError as error:
            assert str(error) == '1 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-25 00:41:20.489131
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:41:24.964779
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:41:28.962627
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:41:32.031001
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 00:41:33.399686
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:41:34.720715
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:41:36.053071
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:41:42.680507
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:41:59.270152
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks, b'')

    fake_socket = FakeSocket([b'ab', b'cde', b'f'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 1]

    # An empty recv before all requested bytes arrive indicates EOF.
    eof_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(eof_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:42:00.703622
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:42:05.310520
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:42:22.412205
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, responses):
            # Avoid creating a real network socket.
            self.responses = iter(responses)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.responses)

    sock = StubSocket([b'ab', b'c', b'def'])

    assert sock.recvall(6) == b'abcdef'
    assert sock.recv_sizes == [6, 4, 3]

    sock = StubSocket([b'ab', b''])

    try:
        sock.recvall(4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('module_0.recvall() did not raise EOFError')

# Generated at 2026-10-25 00:42:38.284767
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            try:
                return next(self.chunks)
            except StopIteration:
                return b''

    # Data received over multiple recv() calls is combined.
    fake_socket = FakeSocket([b'ab', b'cde', b'f'])
    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 1]

    # Requesting zero bytes does not call recv().
    fake_socket = FakeSocket([])
    assert sockssocket.recvall(fake_socket, 0) == b''
    assert fake_socket.recv_sizes == []

    # EOF before the requested byte count raises EOFError.
    fake_socket = FakeSocket([b'ab'])
    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:42:39.717719
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:42:44.837985
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-25 00:42:49.138150
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:43:05.832181
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class LimitedRecvSocket(sockssocket):
        """Force module_0.recvall() to perform multiple recv() calls."""
        def recv(self, bufsize, flags=0):
            return super(LimitedRecvSocket, self).recv(min(bufsize, 2), flags)

    raw_reader, writer = socket.socketpair()
    reader = LimitedRecvSocket(fileno=raw_reader.detach())

    try:
        writer.sendall(b'abcdef')
        assert reader.recvall(6) == b'abcdef'
    finally:
        reader.close()
        writer.close()

    # Verify that premature EOF raises EOFError.
    raw_reader, writer = socket.socketpair()
    reader = LimitedRecvSocket(fileno=raw_reader.detach())

    try:
        writer.sendall(b'abc')
        writer.close()

        try:
            reader.recvall(5)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('module_0.recvall() did not raise EOFError')
    finally:
        reader.close()
        writer.close()

# Generated at 2026-10-25 00:43:07.264824
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:43:11.972995
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:43:13.306639
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:43:17.260793
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:43:33.582795
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.requested_sizes = []

        def recv(self, count):
            self.requested_sizes.append(count)
            return self.chunks.pop(0) if self.chunks else b''

    fake_socket = FakeSocket([b'ab', b'cd', b'ef'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 2]

    incomplete_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(incomplete_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError for an incomplete response')

# Generated at 2026-10-25 00:43:34.912954
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:43:40.364134
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:43:53.141837
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return next(self.chunks)

    # Verify that partial reads are combined.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])

    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    # Verify that an early EOF raises EOFError.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:44:09.113586
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, chunks):
            # Do not create a real network socket.
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self._chunks)

    client = FakeSocksSocket([b'ab', b'c', b'de'])

    assert client.recvall(5) == b'abcde'
    assert client.recv_sizes == [5, 3, 2]

    client = FakeSocksSocket([b'ab', b''])

    try:
        client.recvall(5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('module_0.recvall() did not raise EOFError on premature EOF')

# Generated at 2026-10-25 00:44:19.871545
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)

        def recv(self, count):
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            if len(chunk) > count:
                self.chunks.insert(0, chunk[count:])
                chunk = chunk[:count]
            return chunk

    # Data split across multiple recv() calls is combined correctly.
    fake_socket = FakeSocket([b'ab', b'cd', b'ef'])
    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'

    # Requesting zero bytes returns immediately.
    fake_socket = FakeSocket([])
    assert sockssocket.recvall(fake_socket, 0) == b''

    # Premature EOF raises EOFError with the number of missing bytes.
    fake_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as exc:
        assert str(exc) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:44:29.901507
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class MockSocksSocket(sockssocket):
        def __init__(self, responses):
            super(MockSocksSocket, self).__init__()
            self.responses = iter(responses)

        def recv(self, count, *args):
            return next(self.responses)

    sock = MockSocksSocket([b'he', b'll', b'o'])
    try:
        assert sock.recvall(5) == b'hello'
    finally:
        sock.close()

# Generated at 2026-10-25 00:44:31.239215
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:44:35.531946
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:44:51.814698
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

    # Verify that partial reads are combined.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    # Verify that an early EOF raises the documented error.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:45:08.104562
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = iter(responses)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.responses)

    # Verify that partial reads are accumulated.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 3]

    # Verify that an early EOF raises the expected error.
    fake_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:45:10.510358
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:45:12.927125
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:45:14.313392
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-25 00:45:15.662348
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:45:20.163323
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:45:21.817194
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:45:26.938427
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:45:36.666088
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return next(self.chunks)

    fake_socket = FakeSocket([b'hello', b' ', b'world'])

    result = sockssocket.recvall(fake_socket, 11)

    assert result == b'hello world'
    assert fake_socket.requested_sizes == [11, 6, 5]

# Generated at 2026-10-25 00:45:47.315041
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, chunks):
            self.chunks = list(chunks)

        def recv(self, count):
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            result = chunk[:count]
            remainder = chunk[count:]
            if remainder:
                self.chunks.insert(0, remainder)
            return result

    sock = FakeSocksSocket([b'ab', b'c', b'def'])
    assert sock.recvall(6) == b'abcdef'

    sock = FakeSocksSocket([b'ab', b''])
    try:
        sock.recvall(3)
    except EOFError as error:
        assert str(error) == '1 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:46:02.061393
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self._chunks, b'')

    # Verify that fragmented data is collected until the requested size.
    sock = FakeSocket([b'ab', b'c', b'def'])
    assert sockssocket.recvall(sock, 6) == b'abcdef'
    assert sock.recv_sizes == [6, 4, 3]

    # Verify that an early EOF raises an error with the missing byte count.
    sock = FakeSocket([b'abc', b''])
    try:
        sockssocket.recvall(sock, 6)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:46:17.730275
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            try:
                chunk = next(self.chunks)
            except StopIteration:
                return b''
            assert len(chunk) <= size
            return chunk

    # Handles partial reads until the requested byte count is reached.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 3]

    # Requesting zero bytes returns immediately.
    fake_socket = FakeSocket([])
    assert sockssocket.recvall(fake_socket, 0) == b''
    assert fake_socket.recv_sizes == []

    # An EOF before all requested bytes arrive raises EOFError.
    fake_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:46:30.938173
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from unittest import mock

    sock = sockssocket()
    try:
        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'c', b'def']) as recv:
            assert sock.recvall(6) == b'abcdef'
            assert recv.call_args_list == [
                mock.call(6),
                mock.call(4),
                mock.call(3),
            ]

        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'']) as recv:
            try:
                sock.recvall(4)
            except EOFError as error:
                assert str(error) == '2 bytes missing'
            else:
                raise AssertionError('EOFError was not raised')
    finally:
        sock.close()

# Generated at 2026-10-25 00:46:52.748757
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks, b'')

    receiver = FakeSocket([b'ab', b'c', b'def'])

    assert sockssocket.recvall(receiver, 6) == b'abcdef'
    assert receiver.recv_sizes == [6, 4, 3]

    receiver = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(receiver, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-25 00:46:55.407526
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:46:57.832120
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:00.513116
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:02.926994
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:05.340789
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:07.754714
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:10.166609
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:12.591127
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:15.007652
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:17.431177
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:47:19.849582
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:47:22.281279
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:47:24.699808
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:27.141207
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:29.554191
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:47:31.975640
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:47:38.009990
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:47:39.443487
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:47:44.164631
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-25 00:48:03.626048
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, responses):
            super(StubSocket, self).__init__()
            self.responses = list(responses)
            self.requested_counts = []

        def recv(self, count):
            self.requested_counts.append(count)
            return self.responses.pop(0)

    sock = StubSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.requested_counts == [6, 4, 2]
    finally:
        sock.close()

    # Verify that an early EOF raises the expected exception.
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

# Generated at 2026-10-25 00:48:06.043536
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:08.585574
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:11.002347
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:13.584019
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:48:16.001916
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:48:18.415485
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:48:20.833740
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:23.250772
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:25.665454
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 00:48:28.080041
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:48:30.498681
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 00:48:32.918190
# Unit test for method setproxy of class sockssocket


# Generated at 2026-10-24 22:56:46.489662
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    address_type = Socks5AddressType()

    assert isinstance(address_type, Socks5AddressType)
    assert address_type.ATYP_IPV4 == 0x01
    assert address_type.ATYP_DOMAINNAME == 0x03
    assert address_type.ATYP_IPV6 == 0x04

# Generated at 2026-10-24 22:57:01.835880
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

# Generated at 2026-10-24 22:57:23.265731
# Unit test for constructor of class ProxyError
def test_ProxyError():# Explicit message is passed through unchanged.
    err = ProxyError(0x01, 'custom message')
    assert isinstance(err, socket.error)
    assert err.args == (0x01, 'custom message')

    # No code and no message.
    err = ProxyError()
    assert err.args == (None, None)

    # Code with no message resolves through the subclass CODES table.
    err = Socks5Error(0x05)
    assert err.args == (0x05, 'Connection refused')

    # Unknown code falls back to 'unknown error'.
    err = Socks5Error(0x42)
    assert err.args == (0x42, 'unknown error')

    # SOCKS4 codes resolve from Socks4Error.CODES.
    err = Socks4Error(91)
    assert err.args == (91, 'request rejected or failed')

    # Explicit message overrides the CODES lookup.
    err = Socks5Error(0x05, 'overridden')
    assert err.args == (0x05, 'overridden')

# Generated at 2026-10-24 22:57:26.029451
# Unit test for constructor of class ProxyError
def test_ProxyError():# Explicit message is passed through unchanged.
    err = ProxyError(0x01, 'custom message')
    assert isinstance(err, socket.error)
    assert err.args == (0x01, 'custom message')

    # No code and no message.
    err = ProxyError()
    assert err.args == (None, None)

    # Code with no message resolves through the subclass CODES table.
    err = Socks5Error(0x05)
    assert err.args == (0x05, 'Connection refused')

    # Unknown code falls back to 'unknown error'.
    err = Socks5Error(0x42)
    assert err.args == (0x42, 'unknown error')

    # SOCKS4 codes resolve from Socks4Error.CODES.
    err = Socks4Error(91)
    assert err.args == (91, 'request rejected or failed')

    # Explicit message overrides the CODES lookup.
    err = Socks5Error(0x05, 'overridden')
    assert err.args == (0x05, 'overridden')

# Generated at 2026-10-24 22:57:54.072595
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 22:57:55.462652
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 22:57:56.939106
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 22:58:24.603991
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self._chunks = list(chunks)

        def recv(self, cnt):
            if not self._chunks:
                return b''
            chunk = self._chunks.pop(0)
            assert len(chunk) <= cnt
            return chunk

    fake = FakeSocket([b'ab', b'cdef'])
    assert sockssocket.recvall(fake, 6) == b'abcdef'

    fake = FakeSocket([])
    assert sockssocket.recvall(fake, 0) == b''

    fake = FakeSocket([b'ab'])
    try:
        sockssocket.recvall(fake, 4)
    except EOFError as exc:
        assert str(exc) == '2 bytes missing'
    else:
        raise AssertionError('EOFError not raised')

# Generated at 2026-10-24 22:58:34.930211
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 22:58:43.122896
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 22:58:59.302356
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = iter(responses)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.responses)

    # Verify that fragmented data is combined correctly.
    fake_socket = FakeSocket([b'ab', b'cde', b'f'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 1]

    # Verify that an early EOF raises EOFError.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 22:59:00.734800
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 22:59:04.420473
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 22:59:19.986740
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = iter(responses)
            self.requested = []

        def recv(self, count):
            self.requested.append(count)
            return next(self.responses)

    # Verify that partial reads are combined correctly.
    fake_socket = FakeSocket([b'ab', b'cde', b'f'])
    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.requested == [6, 4, 1]

    # Verify that an early EOF raises the expected error.
    fake_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(fake_socket, 6)
    except EOFError as error:
        assert str(error) == '4 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 22:59:21.420320
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 22:59:25.937468
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 22:59:41.798029
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    try:
        # Ensure recvall combines data returned by multiple recv calls.
        with patch.object(
            sockssocket,
            'recv',
            side_effect=[b'ab', b'cd', b'ef'],
        ) as mock_recv:
            assert sock.recvall(6) == b'abcdef'
            assert mock_recv.call_args_list == [call(6), call(4), call(2)]

        # Ensure an EOF before the requested byte count raises EOFError.
        with patch.object(
            sockssocket,
            'recv',
            side_effect=[b'ab', b''],
        ):
            with pytest.raises(EOFError, match=r'2 bytes missing'):
                sock.recvall(4)
    finally:
        sock.close()

# Generated at 2026-10-24 22:59:44.974421
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 22:59:52.651178
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 22:59:54.496427
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 22:59:59.531275
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:00:16.614600
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        recvall = sockssocket.recvall

        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return self.chunks.pop(0) if self.chunks else b''

    # Verify that partial reads are combined and only the remaining bytes
    # are requested on each call.
    sock = FakeSocket([b'ab', b'c', b'def'])
    assert sock.recvall(6) == b'abcdef'
    assert sock.recv_sizes == [6, 4, 3]

    # Verify that an EOF before all requested bytes arrive raises EOFError.
    sock = FakeSocket([b'ab', b''])
    try:
        sock.recvall(4)
    except EOFError as exc:
        assert str(exc) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:00:26.814593
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = list(responses)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return self.responses.pop(0)

    fake_socket = FakeSocket([b'ab', b'c', b'def'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    incomplete_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(incomplete_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('module_0.recvall() did not raise EOFError')

# Generated at 2026-10-24 23:00:43.545844
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class ChunkedSocket(sockssocket):
        def __init__(self, chunks):
            super(ChunkedSocket, self).__init__()
            self.chunks = list(chunks)

        def recv(self, count):
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            result, remainder = chunk[:count], chunk[count:]
            if remainder:
                self.chunks.insert(0, remainder)
            return result

    sock = ChunkedSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
    finally:
        sock.close()

    sock = ChunkedSocket([b'ab', b'c', b''])
    try:
        try:
            sock.recvall(5)
        except EOFError as exc:
            assert str(exc) == '2 bytes missing'
        else:
            raise AssertionError('module_0.recvall() did not raise EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:00:44.880349
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:00:49.791282
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:01:04.230361
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.requests = []

        def recv(self, count):
            self.requests.append(count)
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            assert len(chunk) <= count
            return chunk

    # Verify that recvall continues receiving until the requested size is met.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requests == [6, 4, 3]

    # Verify that an early EOF raises the expected exception.
    incomplete_socket = FakeSocket([b'ab'])

    try:
        sockssocket.recvall(incomplete_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:01:05.604312
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:01:10.270877
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:01:21.843143
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:01:44.270550
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 23:01:45.701660
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:01:50.822156
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:02:07.616221
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, chunks):
            super(StubSocket, self).__init__()
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, count, *args, **kwargs):
            self.recv_sizes.append(count)

            if not self.chunks:
                return b''

            data = self.chunks.pop(0)
            result, remaining = data[:count], data[count:]

            if remaining:
                self.chunks.insert(0, remaining)

            return result

    sock = StubSocket([b'ab', b'c', b'def'])

    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 3]

        try:
            sock.recvall(1)
        except EOFError as error:
            assert str(error) == '1 bytes missing'
        else:
            raise AssertionError('module_0.recvall() did not raise EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:02:24.716426
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return self.chunks.pop(0) if self.chunks else b''

    fake_socket = FakeSocket([b'ab', b'c', b'def'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

# Generated at 2026-10-24 23:02:26.161262
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:02:30.962387
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:02:42.124504
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

    sock = FakeSocksSocket([b'ab', b'c', b'def'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 3]
    finally:
        sock.close()

    sock = FakeSocksSocket([b'ab', b''])
    try:
        try:
            sock.recvall(3)
        except EOFError as error:
            assert str(error) == '1 bytes missing'
        else:
            raise AssertionError('EOFError was not raised')
    finally:
        sock.close()

# Generated at 2026-10-24 23:02:43.455446
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:02:48.263282
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:03:01.376269
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            if not self.chunks:
                return b''
            return self.chunks.pop(0)

    # recvall should combine partial reads until the requested size is reached.
    fake_socket = FakeSocket([b'a', b'bc', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 5, 3]

    # recvall should raise EOFError if the connection closes too early.
    fake_socket = FakeSocket([b'ab'])

    try:
        sockssocket.recvall(fake_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:03:02.712625
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:03:06.782690
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:03:28.718776
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocksSocket(sockssocket):
        def __init__(self, chunks):
            super(StubSocksSocket, self).__init__()
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return next(self._chunks)

    # Verify that fragmented data is collected completely.
    sock = StubSocksSocket([b'ab', b'c', b'def'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 3]
    finally:
        sock.close()

    # Verify that an early EOF raises EOFError.
    sock = StubSocksSocket([b'ab', b''])
    try:
        try:
            sock.recvall(4)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:03:30.065531
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:03:34.143656
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:03:45.614545
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, chunks):
            super(FakeSocksSocket, self).__init__()
            self.chunks = list(chunks)

        def recv(self, count, *args):
            if not self.chunks:
                return b''

            chunk = self.chunks.pop(0)
            result = chunk[:count]
            remainder = chunk[count:]

            if remainder:
                self.chunks.insert(0, remainder)

            return result

    sock = FakeSocksSocket([b'he', b'll', b'o'])
    try:
        assert sock.recvall(5) == b'hello'
    finally:
        sock.close()


def test_sockssocket_recvall_raises_on_eof():
    class FakeSocksSocket(sockssocket):
        def __init__(self):
            super(FakeSocksSocket, self).__init__()
            self.responses = iter((b'ab', b''))

        def recv(self, count, *args):
            return next(self.responses, b'')

    sock = FakeSocksSocket()
    try:
        try:
            sock.recvall(4)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:03:48.032696
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:03:50.449406
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:03:52.867490
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:03:55.284722
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:03:57.834865
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:00.252170
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:02.779048
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:04:05.198557
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:04:13.345218
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():sock = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 23:04:14.671025
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:20.177013
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:26.269403
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:04:36.916695
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

    incomplete_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(incomplete_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError for an incomplete response')

# Generated at 2026-10-24 23:04:38.348498
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:42.788976
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:04:45.485046
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:47.902447
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:50.320661
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:04:52.910725
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:04:55.340202
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:04:57.758422
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:00.329555
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:02.747837
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:05.168117
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:07.582293
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:10.000031
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:12.421920
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:14.839694
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:05:17.437560
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():sock = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 23:05:18.760366
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 23:05:20.102243
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:05:25.767303
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:05:27.127584
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:05:33.573231
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():proxy_socket = sockssocket()

# Generated at 2026-10-24 23:05:50.544526
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from unittest import mock

    sock = sockssocket()
    try:
        # Verify that recvall combines partial reads and requests only
        # the number of bytes still missing.
        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'c', b'de']) as recv:
            assert sock.recvall(5) == b'abcde'
            assert recv.call_args_list == [
                mock.call(5),
                mock.call(3),
                mock.call(2),
            ]

        # Verify that an EOF before all requested bytes are received raises.
        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'']):
            try:
                sock.recvall(5)
            except EOFError as error:
                assert str(error) == '3 bytes missing'
            else:
                raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:06:00.096886
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = list(responses)
            self.recv_calls = []

        def recv(self, count):
            self.recv_calls.append(count)
            return self.responses.pop(0)

    # Verify that partial reads are accumulated.
    fake_socket = FakeSocket([b'ab', b'cde', b'f'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_calls == [6, 4, 1]

    # Verify that an early EOF raises an error with the missing byte count.
    fake_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:06:02.516001
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:04.932121
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:07.481360
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:09.897128
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:12.313963
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:14.731167
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:06:34.368926
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class ChunkedSocket(sockssocket):
        def __init__(self, chunks):
            super(ChunkedSocket, self).__init__()
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, count):
            self.recv_sizes.append(count)
            return next(self._chunks, b'')

    sock = ChunkedSocket([b'ab', b'c', b'def'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 3]
    finally:
        sock.close()

    sock = ChunkedSocket([b'ab', b''])
    try:
        try:
            sock.recvall(5)
        except EOFError as error:
            assert str(error) == '3 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:06:56.488451
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()

    try:
        # recvall must combine partial reads and request only the remainder.
        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'cd', b'e']) as recv:
            assert sock.recvall(5) == b'abcde'
            assert recv.call_args_list == [
                mock.call(5),
                mock.call(3),
                mock.call(1),
            ]

        # An empty read before receiving all bytes indicates EOF.
        with mock.patch.object(
                sockssocket, 'recv',
                side_effect=[b'ab', b'']):
            try:
                sock.recvall(5)
            except EOFError as error:
                assert str(error) == '3 bytes missing'
            else:
                raise AssertionError('recvall did not raise EOFError')
    finally:
        sock.close()
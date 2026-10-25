

# Generated at 2026-10-24 23:29:51.025365
# Unit test for constructor of class Socks4Command

# Generated at 2026-10-24 23:29:53.554065
# Unit test for constructor of class Socks4Command

# Generated at 2026-10-24 23:29:55.973114
# Unit test for constructor of class Socks4Command

# Generated at 2026-10-24 23:29:58.391446
# Unit test for constructor of class ProxyType

# Generated at 2026-10-24 23:30:00.969562
# Unit test for constructor of class ProxyType

# Generated at 2026-10-24 23:30:03.389344
# Unit test for constructor of class ProxyType

# Generated at 2026-10-24 23:30:05.809978
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 23:30:08.227724
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 23:30:10.645728
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 23:30:13.062423
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-24 23:30:15.477100
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-24 23:30:17.898823
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-24 23:30:20.315674
# Unit test for constructor of class Proxy

# Generated at 2026-10-24 23:30:22.733982
# Unit test for constructor of class Proxy

# Generated at 2026-10-24 23:30:25.163241
# Unit test for constructor of class Proxy

# Generated at 2026-10-24 23:30:27.567630
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 23:30:29.989135
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 23:30:32.405277
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 23:30:34.821980
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:30:37.241212
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:30:39.658672
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:30:42.078059
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:44.498943
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:46.913292
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:49.331034
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:51.748116
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:54.166075
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:30:56.583416
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:30:59.000401
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:31:01.417604
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:31:03.834858
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 23:31:10.284826
# Unit test for constructor of class ProxyError
def test_ProxyError():error = ProxyError(7, 'test error')

# Generated at 2026-10-24 23:31:11.615559
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:31:17.638457
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:31:42.317650
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 23:31:48.870229
# Unit test for constructor of class Socks5Error
def test_Socks5Error():err = Socks5Error(0x05)

# Generated at 2026-10-24 23:31:59.721985
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    expected_messages = {
        91: 'request rejected or failed',
        92: 'request rejected because SOCKS server cannot connect to identd on the client',
        93: 'request rejected because the client program and identd report different user-ids',
    }

    for code, message in expected_messages.items():
        error = Socks4Error(code)
        assert error.args == (code, message)
        assert error.errno == code
        assert error.strerror == message

    unknown_error = Socks4Error(99)
    assert unknown_error.args == (99, 'unknown error')

    custom_error = Socks4Error(91, 'custom message')
    assert custom_error.args == (91, 'custom message')

# Generated at 2026-10-24 23:32:02.142140
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:32:04.561539
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:32:06.976686
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:32:09.394420
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:11.811075
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:14.228132
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:16.644672
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:19.059795
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:25.101382
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:32:50.885924
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, chunks):
            super(StubSocket, self).__init__()
            self.chunks = list(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return self.chunks.pop(0)

    # It should combine partial reads until the requested size is reached.
    sock = StubSocket([b'ab', b'c', b'def'])

# Generated at 2026-10-24 23:32:52.213066
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:32:56.966846
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:33:09.872494
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks)

    fake_socket = FakeSocket([b'ab', b'cd', b'ef'])

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 2]

# Generated at 2026-10-24 23:33:12.598742
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:33:15.017230
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:33:17.589064
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():sock = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 23:33:35.368554
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(sockssocket):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, cnt):
            self.recv_sizes.append(cnt)
            chunk = next(self.chunks, b'')
            assert len(chunk) <= cnt
            return chunk

    # Verify that partial reads are combined.
    sock = FakeSocket([b'ab', b'c', b'def'])
    assert sock.recvall(6) == b'abcdef'
    assert sock.recv_sizes == [6, 4, 3]

    # Verify that an EOF before all requested bytes raises EOFError.
    sock = FakeSocket([b'ab', b''])
    try:
        sock.recvall(4)
    except EOFError as exc:
        assert str(exc) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:33:51.956935
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class ChunkedSocket(sockssocket):
        def __init__(self, chunks):
            super(ChunkedSocket, self).__init__()
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return next(self._chunks, b'')

    sock = ChunkedSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.recv_sizes == [6, 4, 2]
    finally:
        sock.close()

# Generated at 2026-10-24 23:33:53.277198
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:33:58.509904
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 23:34:00.933254
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:03.471520
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:34:05.888284
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:34:08.308792
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:34:10.724858
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:13.146112
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:15.556369
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:17.974522
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:20.392548
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:34:27.299657
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 23:34:44.387310
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def __init__(self, chunks):
            super(StubSocket, self).__init__()
            self._chunks = iter(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return next(self._chunks)

    sock = StubSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
        assert sock.requested_sizes == [6, 4, 2]
    finally:
        sock.close()


def test_sockssocket_recvall_raises_on_eof():
    class StubSocket(sockssocket):
        def __init__(self):
            super(StubSocket, self).__init__()
            self._chunks = iter([b'ab', b''])

        def recv(self, size):
            return next(self._chunks)

    sock = StubSocket()
    try:
        try:
            sock.recvall(5)
            assert False, 'Expected EOFError'
        except EOFError as error:
            assert str(error) == '3 bytes missing'
    finally:
        sock.close()

# Generated at 2026-10-24 23:34:59.770052
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.chunks)

    # Verify that fragmented data is collected completely.
    fake_socket = FakeSocket([b'ab', b'cd', b'ef'])

    assert sockssocket.recvall(fake_socket, 6) == b'abcdef'
    assert fake_socket.recv_sizes == [6, 4, 2]

    # Verify that an early EOF raises an informative error.
    incomplete_socket = FakeSocket([b'ab', b''])

    try:
        sockssocket.recvall(incomplete_socket, 4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError for an incomplete response')

# Generated at 2026-10-24 23:35:02.412436
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:04.830477
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:07.358126
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:09.775827
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:12.193391
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:14.768255
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:17.184600
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:19.602101
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:22.020530
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:24.437095
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:26.856741
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:29.271954
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:31.692095
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:34.122857
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:36.554479
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:38.972897
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:41.390088
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:43.809418
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:35:46.228280
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:48.644463
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:51.060998
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:53.476699
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:55.891764
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:35:58.310825
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:00.727182
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:03.142954
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:05.561415
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:07.979257
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:10.399383
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:12.817408
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:15.235481
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:17.654032
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:20.070947
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:22.489540
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:24.909194
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:27.324291
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:29.741483
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:32.156361
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:34.576337
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:36.994423
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:39.409692
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:41.827418
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:44.242733
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:46.660254
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:49.080641
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:36:51.496284
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:53.911118
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:56.327731
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:36:58.743077
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:01.161319
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:03.579427
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:05.994280
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:08.411232
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:10.828590
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:13.244766
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:15.661809
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:18.076481
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:20.493774
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:22.909587
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:25.329199
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:27.743503
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:30.161169
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:32.577629
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:34.994651
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:37.412340
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:39.830472
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:42.244223
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:44.661943
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:47.079344
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:49.498780
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:51.918436
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:54.335305
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 23:37:56.751466
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:37:59.167866
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:01.584244
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:04.000178
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:06.415568
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:08.832476
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:13.025162
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:15.440461
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:17.859223
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:20.277765
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:22.694264
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:25.108928
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:27.525332
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:29.943904
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:32.360396
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:34.778905
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:37.191575
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:39.607684
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:42.025861
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:44.439959
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:46.857182
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:49.278538
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:51.694241
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:54.109269
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:56.530191
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:38:58.944665
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:39:01.362975
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:39:03.780455
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:39:06.195743
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 23:39:07.597839
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import socket

# Generated at 2026-10-24 23:39:19.228969
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, responses):
            super(FakeSocksSocket, self).__init__()
            self.responses = iter(responses)

        def recv(self, _size):
            return next(self.responses, b'')

    sock = FakeSocksSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
    finally:
        sock.close()


def test_sockssocket_recvall_raises_on_eof():
    class FakeSocksSocket(sockssocket):
        def __init__(self, responses):
            super(FakeSocksSocket, self).__init__()
            self.responses = iter(responses)

        def recv(self, _size):
            return next(self.responses, b'')

    sock = FakeSocksSocket([b'ab', b''])
    try:
        try:
            sock.recvall(4)
        except EOFError as error:
            assert str(error) == '2 bytes missing'
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()

# Generated at 2026-10-24 23:39:35.000146
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, responses):
            self.responses = iter(responses)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            try:
                return next(self.responses)
            except StopIteration:
                return b''

    # It should combine partial reads until the requested count is reached.
    fake_socket = FakeSocket([b'ab', b'c', b'def'])
    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.requested_sizes == [6, 4, 3]

    # It should raise EOFError if the connection closes prematurely.
    fake_socket = FakeSocket([b'ab', b''])
    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '3 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 23:39:58.452372
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocket(sockssocket):
        def recv(self, count):
            chunk = self._recv_chunks.pop(0)
            assert len(chunk) <= count
            return chunk

    sock = StubSocket()
    try:
        # Verify that multiple partial reads are combined.
        sock._recv_chunks = [b'ab', b'c', b'def']
        assert sock.recvall(6) == b'abcdef'
        assert not sock._recv_chunks

        # Requesting zero bytes should not call recv().
        sock._recv_chunks = []
        assert sock.recvall(0) == b''

        # EOF before receiving the requested amount should raise EOFError.
        sock._recv_chunks = [b'ab', b'']
        try:
            sock.recvall(3)
        except EOFError as exc:
            assert exc.args == ('1 bytes missing',)
        else:
            raise AssertionError('Expected EOFError')
    finally:
        sock.close()
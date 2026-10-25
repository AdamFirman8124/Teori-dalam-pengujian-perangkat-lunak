

# Generated at 2026-10-24 19:36:36.948397
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:36:45.365059
# Unit test for constructor of class Socks4Command
def test_Socks4Command():
    cmd = Socks4Command()
    assert cmd.CMD_CONNECT == 0x01
    assert cmd.CMD_BIND == 0x02
    # constants also reachable on the class itself
    assert Socks4Command.CMD_CONNECT == 0x01
    assert Socks4Command.CMD_BIND == 0x02
    # Socks5Command subclasses Socks4Command and adds UDP_ASSOCIATE
    assert Socks5Command.CMD_CONNECT == 0x01
    assert Socks5Command.CMD_BIND == 0x02
    assert Socks5Command.CMD_UDP_ASSOCIATE == 0x03

# Generated at 2026-10-24 19:36:56.153344
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    def _check(expected_version, got_version):
        error = InvalidVersionError(expected_version, got_version)

        # ProxyError.__init__ passes (code=0, msg) to socket.error
        assert isinstance(error, InvalidVersionError)
        assert isinstance(error, ProxyError)
        assert isinstance(error, socket.error)

        assert error.args[0] == 0
        assert error.args[1] == (
            'Invalid response version from server. Expected {0:02x} got '
            '{1:02x}'.format(expected_version, got_version))

    # Decimal versions are rendered as two lowercase hex digits
    _check(SOCKS5_VERSION, SOCKS4_VERSION)  # Expected 05 got 04
    _check(0xFF, 0x00)                      # Expected ff got 00

# Generated at 2026-10-24 19:36:58.572324
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 19:37:00.987736
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 19:37:03.407582
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 19:37:15.136938
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

# Generated at 2026-10-24 19:37:48.336394
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:37:50.862158
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:37:53.280221
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:37:55.699365
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:37:58.115919
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:38:00.534138
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:38:02.951080
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:38:05.368359
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:38:07.783696
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:38:24.282027
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:38:25.709719
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:38:27.149240
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:38:43.584426
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:38:44.943383
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:38:46.399137
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:39:02.907162
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:39:05.328879
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:39:07.743806
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:39:10.313152
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:39:20.591394
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():calls = []


# Generated at 2026-10-24 19:39:47.531256
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocksSocket(sockssocket):
        def __init__(self, responses):
            super(FakeSocksSocket, self).__init__()
            self.responses = iter(responses)

        def recv(self, count, *args):
            return next(self.responses)

    sock = FakeSocksSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
    finally:
        sock.close()

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

# Generated at 2026-10-24 19:39:49.952140
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:39:52.521512
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:39:54.940615
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:39:57.358076
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:39:59.928123
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:40:02.462612
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:40:04.878898
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:40:07.299667
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:40:09.715907
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:40:11.189903
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:40:12.609579
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:40:46.821994
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:40:56.958377
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket


# Generated at 2026-10-24 19:40:59.382123
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:01.977927
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:04.396361
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:06.814248
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:09.232701
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:11.649215
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 19:41:14.066791
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:41:16.486583
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:41:18.903806
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:41:21.322633
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:41:22.775136
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-24 19:41:39.251933
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:41:40.683347
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:41:42.116043
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:41:43.550152
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:41:59.012889
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from .socks import sockssocket


class FakeSocket(object):
    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, count):
        self.calls.append(count)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def test_sockssocket_recvall_reads_until_requested_length():
    fake = FakeSocket([b'ab', b'cde'])

    result = sockssocket.recvall(fake, 5)

    assert result == b'abcde'
    assert fake.calls == [5, 3]


def test_sockssocket_recvall_raises_eoferror_when_connection_closes():
    fake = FakeSocket([b'ab', b''])

    with pytest.raises(EOFError, match=r'3 bytes missing'):
        sockssocket.recvall(fake, 5)


def test_sockssocket_recvall_returns_empty_bytes_for_zero_length():
    fake = FakeSocket([])

    result = sockssocket.recvall(fake, 0)

    assert result == b''
    assert fake.calls == []

# Generated at 2026-10-24 19:42:01.431128
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:03.847494
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:06.263900
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:08.679042
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:11.095446
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:13.514107
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:15.932612
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:18.347193
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:20.765129
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:23.181859
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:25.598491
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:28.018367
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:30.434632
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:32.852249
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:42:34.275730
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-24 19:42:35.664998
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:42:37.136226
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:42:38.539434
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:42:39.972872
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:42:41.405430
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:42:42.840852
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:42:44.253903
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:42:45.707192
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:42:47.140771
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:42:48.573700
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:42:50.008338
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:42:52.369638
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:43:18.885585
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)
            self.requested_sizes = []

        def recv(self, size):
            self.requested_sizes.append(size)
            return next(self.chunks)

    fake_socket = FakeSocket([b'he', b'll', b'o'])

    result = sockssocket.recvall(fake_socket, 5)

    assert result == b'hello'
    assert fake_socket.requested_sizes == [5, 3, 1]

# Generated at 2026-10-24 19:43:21.476075
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:43:23.893809
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:43:26.308534
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:43:28.722938
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:43:31.136371
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:43:33.555304
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:43:35.975512
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:43:42.329427
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 19:44:15.616300
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:44:18.035305
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:44:20.555215
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:44:22.972806
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:25.391505
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:27.809717
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:30.228997
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:32.645461
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:35.165827
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:37.587117
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:44:39.015594
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-24 19:44:56.068439
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket.__new__(sockssocket)

    def make_recv(chunks):
        it = iter(chunks)
        calls = []

        def recv(n):
            calls.append(n)
            try:
                return next(it)
            except StopIteration:
                return b''
        recv.calls = calls
        return recv

    # 1. cnt == 0 returns empty without reading
    s.recv = make_recv([b'never'])
    assert s.recvall(0) == b''
    assert s.recv.calls == []

    # 2. single recv returns exactly cnt bytes
    s.recv = make_recv([b'foobar'])
    assert s.recvall(6) == b'foobar'
    assert s.recv.calls == [6]

    # 3. fragmented recvs are concatenated, requests shrink by received len
    s.recv = make_recv([b'fo', b'ob', b'ar'])
    assert s.recvall(6) == b'foobar'
    assert s.recv.calls == [6, 4, 2]

    # 4. recv returning more than one byte at a time still works
    s.recv = make_recv([b'a', b'bcde'])
    assert s.recvall(5) == b'abcde'
    assert s.recv.calls == [5, 4]

    # 5. empty recv in the middle -> EOFError with remaining count
    s.recv = make_recv([b'he', b''])
    try:
        s.recvall(5)
        assert False, 'expected EOFError'
    except EOFError as e:
        assert '3 bytes missing' in str(e)

    # 6. immediate EOF
    s.recv = make_recv([b''])
    try:
        s.recvall(4)
        assert False, 'expected EOFError'
    except EOFError as e:
        assert '4 bytes missing' in str(e)

# Generated at 2026-10-24 19:45:12.550598
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:13.988608
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:45:15.419319
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:45:18.110439
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:20.632963
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:23.163345
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:25.576589
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:45:27.993120
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:45:30.414977
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:45:32.987568
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:35.404471
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:37.824120
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:40.241820
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:45:41.689425
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:45:43.167378
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 19:45:59.628940
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket.__new__(sockssocket)

    def make_recv(chunks):
        it = iter(chunks)
        calls = []

        def recv(n):
            calls.append(n)
            try:
                return next(it)
            except StopIteration:
                return b''
        recv.calls = calls
        return recv

    # 1. cnt == 0 returns empty without reading
    s.recv = make_recv([b'never'])
    assert s.recvall(0) == b''
    assert s.recv.calls == []

    # 2. single recv returns exactly cnt bytes
    s.recv = make_recv([b'foobar'])
    assert s.recvall(6) == b'foobar'
    assert s.recv.calls == [6]

    # 3. fragmented recvs are concatenated, requests shrink by received len
    s.recv = make_recv([b'fo', b'ob', b'ar'])
    assert s.recvall(6) == b'foobar'
    assert s.recv.calls == [6, 4, 2]

    # 4. recv returning more than one byte at a time still works
    s.recv = make_recv([b'a', b'bcde'])
    assert s.recvall(5) == b'abcde'
    assert s.recv.calls == [5, 4]

    # 5. empty recv in the middle -> EOFError with remaining count
    s.recv = make_recv([b'he', b''])
    try:
        s.recvall(5)
        assert False, 'expected EOFError'
    except EOFError as e:
        assert '3 bytes missing' in str(e)

    # 6. immediate EOF
    s.recv = make_recv([b''])
    try:
        s.recvall(4)
        assert False, 'expected EOFError'
    except EOFError as e:
        assert '4 bytes missing' in str(e)

# Generated at 2026-10-24 19:46:01.090176
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    try:
        # initially no proxy
        assert s._proxy is None

        # defaults: rdns=True, username=None, password=None
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, '127.0.0.1', 1080, None, None, True)
        assert s._proxy.type == ProxyType.SOCKS5
        assert s._proxy.host == '127.0.0.1'
        assert s._proxy.port == 1080
        assert s._proxy.username is None
        assert s._proxy.password is None
        assert s._proxy.remote_dns is True

        # all supported types
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4

        s.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 1080)
        assert s._proxy.type == ProxyType.SOCKS4A

        # custom auth + rdns=False maps to remote_dns
        s.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 9050,
                   rdns=False, username='user', password='pass')
        assert s._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 9050,
            'user', 'pass', False)

        # overwrites previous value
        s.setproxy(ProxyType.SOCKS4A, '10.0.0.1', 1081)
        assert s._proxy == Proxy(
            ProxyType.SOCKS4A, '10.0.0.1', 1081, None, None, True)
    finally:
        s.close()

    # invalid proxytype must fail assertion
    s2 = sockssocket()
    try:
        for bad_type in (99, -1, None, 'SOCKS5'):
            try:
                s2.setproxy(bad_type, '127.0.0.1', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'module_0.setproxy(%r) should raise AssertionError' % (bad_type,))
    finally:
        s2.close()

# Generated at 2026-10-24 19:46:29.249379
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self, chunks):
            self.chunks = iter(chunks)

        def recv(self, count):
            return next(self.chunks, b'')

    # Verify that fragmented reads are combined.
    fake_socket = FakeSocket([b'hel', b'lo ', b'world'])
    assert sockssocket.recvall(fake_socket, 11) == b'hello world'

    # Verify that an early EOF raises EOFError.
    fake_socket = FakeSocket([b'abc', b''])
    try:
        sockssocket.recvall(fake_socket, 5)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('Expected EOFError')

# Generated at 2026-10-24 19:46:31.673330
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:46:34.091989
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:46:36.508527
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 19:46:38.926824
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:46:41.346176
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 19:46:42.729655
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()


# Generated at 2026-10-25 11:19:08.760644
# Unit test for constructor of class Socks4Command
def test_Socks4Command():
    command = Socks4Command()

    assert command.CMD_CONNECT == 0x01
    assert command.CMD_BIND == 0x02

# Generated at 2026-10-25 11:19:18.693178
# Unit test for constructor of class ProxyError
def test_ProxyError():
    class TestProxyError(ProxyError):
        CODES = {
            1: 'known error',
        }

    error = TestProxyError(1)
    assert error.args == (1, 'known error')

    error = TestProxyError(2)
    assert error.args == (2, 'unknown error')

    error = TestProxyError(1, 'custom message')
    assert error.args == (1, 'custom message')

    error = TestProxyError()
    assert error.args == (None, None)

# Generated at 2026-10-25 11:19:29.343817
# Unit test for constructor of class Socks5Auth
def test_Socks5Auth():
    # constructor with no args should succeed (default object.__init__)
    auth = Socks5Auth()
    assert isinstance(auth, Socks5Auth)

    # class constants must be defined with RFC1928 values
    assert Socks5Auth.AUTH_NONE == 0x00
    assert Socks5Auth.AUTH_GSSAPI == 0x01
    assert Socks5Auth.AUTH_USER_PASS == 0x02
    assert Socks5Auth.AUTH_NO_ACCEPTABLE == 0xFF

    # accessible via instance
    assert auth.AUTH_NONE == 0x00
    assert auth.AUTH_GSSAPI == 0x01
    assert auth.AUTH_USER_PASS == 0x02
    assert auth.AUTH_NO_ACCEPTABLE == 0xFF

    # no custom __init__ - extra args must fail
    try:
        Socks5Auth(0x00)
        assert False, "Socks5Auth() should not accept arguments"
    except TypeError:
        pass

# Generated at 2026-10-25 11:19:39.993974
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    expected_version = SOCKS5_VERSION
    got_version = SOCKS4_VERSION

    error = InvalidVersionError(expected_version, got_version)

    expected_message = (
        'Invalid response version from server. Expected 05 got 04'
    )

    assert isinstance(error, ProxyError)
    assert isinstance(error, socket.error)
    assert error.args == (0, expected_message)

# Generated at 2026-10-25 11:19:50.846595
# Unit test for constructor of class sockssocket
def test_sockssocket():
    # Test 1: constructor initializes with no proxy configured
    s = sockssocket()
    assert isinstance(s, socket.socket), 'sockssocket should subclass socket.socket'
    assert s._proxy is None, 'constructor must initialize _proxy to None'

    # Test 2: setproxy stores all fields correctly
    s.setproxy(
        proxytype=ProxyType.SOCKS5,
        addr='127.0.0.1',
        port=1080,
        rdns=False,
        username='user',
        password='pass')
    expected = Proxy(ProxyType.SOCKS5, '127.0.0.1', 1080, 'user', 'pass', False)
    assert s._proxy == expected, 'setproxy must populate the Proxy namedtuple: got {0}'.format(s._proxy)

    # Test 3: setproxy defaults (rdns=True, no credentials)
    s2 = sockssocket()
    s2.setproxy(ProxyType.SOCKS4A, 'proxy.example.com', 9050)
    assert s2._proxy == Proxy(ProxyType.SOCKS4A, 'proxy.example.com', 9050, None, None, True)

    # Test 4: invalid proxy type is rejected
    try:
        s3 = sockssocket()
        s3.setproxy(proxytype=99, addr='127.0.0.1', port=1080)
        assert False, 'setproxy must raise AssertionError on invalid proxytype'
    except AssertionError:
        pass

    # Cleanup
    for sock in (s, s2, s3):
        try:
            sock.close()
        except socket.error:
            pass


if __name__ == '__main__':
    test_sockssocket()
    print('test_sockssocket passed')

# Generated at 2026-10-25 11:19:54.431765
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 11:20:24.128426
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket

# Generated at 2026-10-25 11:20:32.525810
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:20:41.971058
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 11:20:43.328507
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket

# Generated at 2026-10-25 11:20:44.811312
# Unit test for constructor of class Socks5Error
def test_Socks5Error():
    # 1. Known codes -> looked up from Socks5Error.CODES
    for code, expected_msg in Socks5Error.CODES.items():
        err = Socks5Error(code)
        assert isinstance(err, ProxyError)
        assert isinstance(err, socket.error)
        assert err.args[0] == code
        assert err.args[1] == expected_msg

    # spot-checks
    assert Socks5Error(0x01).args == (0x01, 'general SOCKS server failure')
    assert Socks5Error(0x05).args == (0x05, 'Connection refused')
    assert Socks5Error(0xFE).args == (0xFE, 'unknown username or invalid password')
    assert Socks5Error(0xFF).args == (0xFF, 'all offered authentication methods were rejected')

    # 2. Unknown code -> 'unknown error'
    err = Socks5Error(0x09)
    assert err.args[0] == 0x09
    assert err.args[1] == 'unknown error'

    # 3. Explicit msg overrides CODES lookup
    err = Socks5Error(0x01, 'custom message')
    assert err.args == (0x01, 'custom message')

    err = Socks5Error(0x09, 'custom message')
    assert err.args == (0x09, 'custom message')

    # 4. No args -> (None, None)
    err = Socks5Error()
    assert err.args == (None, None)

    err = Socks5Error(None, None)
    assert err.args == (None, None)

# Generated at 2026-10-25 11:20:49.420227
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:20:50.957289
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:20:54.336973
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 11:21:05.952202
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError(5, 'boom')

# Generated at 2026-10-25 11:21:07.851983
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:10.929883
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 11:21:12.869602
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError(5, 'boom')

# Generated at 2026-10-25 11:21:16.302349
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 11:21:24.337660
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError(5, 'boom')

# Generated at 2026-10-25 11:21:28.946725
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:30.278692
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:21:31.714435
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:21:33.351100
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:34.784337
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:21:36.115941
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:37.448441
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:41.133236
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:42.478765
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():
    # 1. No proxy: success returns 0
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    target = listener.getsockname()
    s = sockssocket()
    try:
        assert s.connect_ex(target) == 0
    finally:
        s.close()
        listener.close()

    # 2. No proxy: failure returns errno, does not raise

# Generated at 2026-10-25 11:21:43.856591
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:21:51.995638
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:21:54.655260
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:22:02.874971
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:22:05.292216
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:07.839266
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:10.252622
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:12.667797
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:15.081658
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:17.496643
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:22:19.915212
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:22.333086
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:25.163566
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:27.581292
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:29.997272
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:32.412905
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:34.828970
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:37.246115
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:39.659313
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:42.075650
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:44.493829
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:46.907640
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:49.323525
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:51.742886
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:54.157738
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:56.572287
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:22:58.990925
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:23:01.813007
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 11:23:03.206021
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:06.232589
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:07.757531
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:09.301441
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:10.737370
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:12.143290
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:16.777881
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:18.969763
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:20.999020
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:22.531469
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:23.881391
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:27.018811
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:29.766149
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:23:32.184547
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:23:40.224008
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():a, b = socket.socketpair()

# Generated at 2026-10-25 11:23:41.762103
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:43.235134
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:44.656187
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:46.166865
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:47.715419
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:49.159030
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:23:54.365009
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:23:58.966076
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:00.401385
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:01.850728
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:09.719107
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:11.659971
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:13.114001
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:14.528568
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:17.400165
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:19.821114
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:22.232876
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:24.647891
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:24:27.271101
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:24:29.794137
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:24:32.206540
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:34.620635
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:37.034688
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:24:38.490912
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:39.934015
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:42.134876
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:45.047638
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:46.691011
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:48.045071
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:52.608974
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:53.942633
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()

    # Initially no proxy is configured
    assert s._proxy is None

    # Valid proxy type stores all fields in the expected order
    s.setproxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        rdns=False, username='user', password='pass')
    assert s._proxy == Proxy(
        ProxyType.SOCKS5, '127.0.0.1', 9050,
        'user', 'pass', False)

    # All supported proxy types are accepted
    for proxytype in (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5):
        s.setproxy(proxytype, 'proxy.example.com', 1080)
        assert s._proxy.type == proxytype
        assert s._proxy.host == 'proxy.example.com'
        assert s._proxy.port == 1080

    # Defaults: remote DNS on, no credentials
    s.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    assert s._proxy.remote_dns is True
    assert s._proxy.username is None
    assert s._proxy.password is None

    # Invalid proxy type is rejected
    try:
        s.setproxy(99, 'proxy.example.com', 1080)
    except AssertionError:
        pass
    else:
        raise AssertionError('setproxy accepted invalid proxy type')

# Generated at 2026-10-25 11:24:55.288845
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:24:58.047142
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:25:00.461889
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:02.878375
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:05.293568
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:07.707019
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:10.442695
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:12.858272
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:15.278337
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:17.694150
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:20.108207
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 11:25:22.523142
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:24.937529
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:27.353481
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:29.768297
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:32.540325
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:35.084728
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:37.499472
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:39.913135
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:42.326808
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:44.743847
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:47.160974
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:49.575340
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:51.989323
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:54.403464
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:56.818502
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:25:59.234883
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:01.652278
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:04.066116
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:08.826458
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:11.241818
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:13.659618
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:16.076066
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:18.490665
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:20.904488
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:23.319805
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:25.733437
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:28.150609
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:30.565941
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:32.979630
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:35.393211
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:37.810065
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:40.224547
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:42.639722
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:45.056342
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:47.467542
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:49.883137
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:52.329270
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:54.710654
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:57.126134
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:26:59.538421
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:01.956744
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:04.370850
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:06.784330
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:09.198348
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:11.612445
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:14.029361
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:16.445066
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:18.858851
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:25.351404
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:27.798366
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:30.183400
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:32.601723
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:35.014150
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:37.428493
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:27:43.294327
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    # Build an instance without invoking socket's real __init__
    sock = sockssocket.__new__(sockssocket)

    # Case 1: all bytes arrive in a single recv call
    sock.recv = lambda bufsize: b'hello world'[:bufsize]
    assert sock.recvall(11) == b'hello world'

    # Case 2: bytes arrive in multiple chunks
    chunks = [b'foo', b'bar', b'baz']
    state = {'i': 0}

    def chunked_recv(bufsize):
        if state['i'] < len(chunks):
            c = chunks[state['i']]
            state['i'] += 1
            return c
        return b''

    sock.recv = chunked_recv
    assert sock.recvall(9) == b'foobarbaz'

    # Case 3: recv returns fewer bytes than requested each time
    def capped_recv(bufsize):
        return b'x' * min(bufsize, 4)

    sock.recv = capped_recv
    assert sock.recvall(10) == b'x' * 10

    # Case 4: connection closed early -> EOFError reporting missing byte count
    state2 = {'called': False}

    def short_recv(bufsize):
        if not state2['called']:
            state2['called'] = True
            return b'ab'
        return b''

    sock.recv = short_recv
    try:
        sock.recvall(5)
        raise AssertionError('expected EOFError')
    except EOFError as e:
        assert '3 bytes missing' in str(e)

    # Case 5: requesting zero bytes returns empty immediately without recv
    def fail_recv(bufsize):
        raise AssertionError('recv should not be called for cnt=0')

    sock.recv = fail_recv
    assert sock.recvall(0) == b''

# Generated at 2026-10-25 11:27:44.687832
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:46.198697
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:47.627026
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:49.066467
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:50.600750
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:52.092485
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:27:53.564760
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:00.687531
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:02.070888
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:03.500049
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:05.037373
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:06.674398
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:08.300816
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():import pytest

from socks import sockssocket  # adjust to your package path


class FakeSocket(object):
    """Stand-in exposing only recv(), so no real socket is needed."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.calls = []

    def recv(self, cnt):
        self.calls.append(cnt)
        if not self.chunks:
            return b''
        return self.chunks.pop(0)


def _recvall(chunks, cnt):
    fake = FakeSocket(chunks)
    return sockssocket.recvall(fake, cnt), fake


def test_recvall_single_read():
    data, fake = _recvall([b'abcd'], 4)
    assert data == b'abcd'
    assert fake.calls == [4]


def test_recvall_multiple_reads():
    data, fake = _recvall([b'ab', b'cd', b'ef'], 6)
    assert data == b'abcdef'
    assert fake.calls == [6, 4, 2]


def test_recvall_zero_bytes_does_not_read():
    data, fake = _recvall([], 0)
    assert data == b''
    assert fake.calls == []


def test_recvall_eof_mid_stream():
    fake = FakeSocket([b'ab'])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 5)
    assert '3 bytes missing' in str(exc.value)
    assert fake.calls == [5, 3]


def test_recvall_eof_immediately():
    fake = FakeSocket([])
    with pytest.raises(EOFError) as exc:
        sockssocket.recvall(fake, 2)
    assert '2 bytes missing' in str(exc.value)

# Generated at 2026-10-25 11:28:10.880591
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:13.576859
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:15.993735
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:18.683871
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:21.094630
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:23.513183
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:25.925900
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:28.602590
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:31.013856
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:33.430753
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:35.845404
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:38.257793
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:48.815090
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:51.229421
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:53.646818
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:56.058194
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:28:58.471989
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:29:00.885779
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:29:03.298736
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:29:05.757448
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 11:29:08.161678
# Unit test for method recvall of class sockssocket
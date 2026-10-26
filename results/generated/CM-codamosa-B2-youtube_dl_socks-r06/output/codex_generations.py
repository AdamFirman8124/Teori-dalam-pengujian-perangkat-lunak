

# Generated at 2026-10-25 08:57:22.861080
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 08:57:31.567219
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket as _socket

# Generated at 2026-10-25 08:57:33.986548
# Unit test for constructor of class Socks5Auth

# Generated at 2026-10-25 08:58:23.585480
# Unit test for constructor of class Socks5Auth
def test_Socks5Auth():auth = Socks5Auth()

# Generated at 2026-10-25 08:58:36.078378
# Unit test for constructor of class Socks5Auth
def test_Socks5Auth():
    auth = Socks5Auth()

    assert isinstance(auth, Socks5Auth)
    assert auth.AUTH_NONE == 0x00
    assert auth.AUTH_GSSAPI == 0x01
    assert auth.AUTH_USER_PASS == 0x02
    assert auth.AUTH_NO_ACCEPTABLE == 0xFF

    assert Socks5Auth.AUTH_NONE == 0x00
    assert Socks5Auth.AUTH_GSSAPI == 0x01
    assert Socks5Auth.AUTH_USER_PASS == 0x02
    assert Socks5Auth.AUTH_NO_ACCEPTABLE == 0xFF

    values = [
        auth.AUTH_NONE,
        auth.AUTH_GSSAPI,
        auth.AUTH_USER_PASS,
        auth.AUTH_NO_ACCEPTABLE,
    ]
    assert len(values) == len(set(values))
    assert all(isinstance(value, int) for value in values)

    try:
        Socks5Auth(0x00)
        raise AssertionError("Socks5Auth() should take no arguments")
    except TypeError:
        pass

# Generated at 2026-10-25 08:58:40.395436
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    obj = Socks5AddressType()

    assert isinstance(obj, Socks5AddressType)
    assert Socks5AddressType.ATYP_IPV4 == 0x01
    assert Socks5AddressType.ATYP_DOMAINNAME == 0x03
    assert Socks5AddressType.ATYP_IPV6 == 0x04

# Generated at 2026-10-25 08:58:48.418119
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

# Generated at 2026-10-25 08:59:07.859256
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

# Generated at 2026-10-25 08:59:09.460173
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    from socks import Socks4Error, ProxyError

    # ERR_SUCCESS code
    assert Socks4Error.ERR_SUCCESS == 90

    # known codes -> looked up message from CODES
    e = Socks4Error(91)
    assert e.args == (91, 'request rejected or failed')
    assert isinstance(e, ProxyError)

    e = Socks4Error(92)
    assert e.args == (
        92,
        'request rejected because SOCKS server cannot connect to identd on the client',
    )

    e = Socks4Error(93)
    assert e.args == (
        93,
        'request rejected because the client program and identd report different user-ids',
    )

    # unknown code -> fallback message
    e = Socks4Error(999)
    assert e.args == (999, 'unknown error')

    # ERR_SUCCESS is not in CODES -> fallback message
    e = Socks4Error(90)
    assert e.args == (90, 'unknown error')

    # explicit msg is not overwritten by lookup
    e = Socks4Error(91, 'custom')
    assert e.args == (91, 'custom')

    e = Socks4Error(999, 'custom')
    assert e.args == (999, 'custom')

    # no code / no msg
    e = Socks4Error()
    assert e.args == (None, None)

    e = Socks4Error(None, 'only-msg')
    assert e.args == (None, 'only-msg')

# Generated at 2026-10-25 08:59:47.249229
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 09:00:56.058273
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket as _socket

# Generated at 2026-10-25 09:00:59.231821
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 09:01:00.983286
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket as _socket

# Generated at 2026-10-25 09:01:02.515064
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

# Generated at 2026-10-25 09:01:20.981138
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 09:01:46.132830
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError()

# Generated at 2026-10-25 09:01:47.556466
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

# Generated at 2026-10-25 09:02:05.896369
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 09:02:08.456936
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError()

# Generated at 2026-10-25 09:02:13.269924
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

# Generated at 2026-10-25 09:02:16.158427
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 09:02:17.671423
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():import socket as _socket

# Generated at 2026-10-25 09:02:19.875372
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

# Generated at 2026-10-25 09:02:21.203739
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

# Generated at 2026-10-25 09:02:25.865126
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

# Generated at 2026-10-25 09:02:28.396776
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:02:30.818709
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:02:33.236027
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:02:35.764237
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:02:38.180402
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:02:40.600523
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:02:53.207402
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

# Generated at 2026-10-25 09:02:54.945905
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

# Generated at 2026-10-25 09:02:56.583342
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

# Generated at 2026-10-25 09:02:58.364239
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

# Generated at 2026-10-25 09:02:59.884023
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

# Generated at 2026-10-25 09:03:01.492250
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

# Generated at 2026-10-25 09:03:03.040219
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

# Generated at 2026-10-25 09:03:04.512474
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

# Generated at 2026-10-25 09:03:05.943448
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

# Generated at 2026-10-25 09:03:07.646999
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

# Generated at 2026-10-25 09:03:10.105122
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

# Generated at 2026-10-25 09:03:11.743559
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

# Generated at 2026-10-25 09:03:13.182275
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

# Generated at 2026-10-25 09:03:14.613492
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

# Generated at 2026-10-25 09:03:16.046082
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

# Generated at 2026-10-25 09:03:17.478514
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

# Generated at 2026-10-25 09:03:18.911889
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

# Generated at 2026-10-25 09:03:20.343688
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

# Generated at 2026-10-25 09:03:22.891116
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:25.308963
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:27.726507
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:30.143625
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:03:32.560459
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:03:35.166346
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 09:03:37.743455
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:40.162695
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:42.577005
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:03:57.525069
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    from urllib3.contrib.socks import Proxy, ProxyType, sockssocket

    sock = sockssocket()
    try:
        # Defaults: rdns=True, no credentials
        assert sock._proxy is None
        sock.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 1080)
        assert sock._proxy == Proxy(
            ProxyType.SOCKS5, 'proxy.example.com', 1080, None, None, True)

        # Explicit rdns=False with credentials (SOCKS4A)
        sock.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 9050,
                      rdns=False, username='user', password='pass')
        assert sock._proxy == Proxy(
            ProxyType.SOCKS4A, '127.0.0.1', 9050, 'user', 'pass', False)

        # SOCKS4 is enum value 0 (falsy) and must still be accepted
        sock.setproxy(ProxyType.SOCKS4, '10.0.0.1', 1080, username='u')
        assert sock._proxy == Proxy(
            ProxyType.SOCKS4, '10.0.0.1', 1080, 'u', None, True)

        # Overwriting replaces the previous proxy
        sock.setproxy(ProxyType.SOCKS5, 'other.example.com', 8080)
        assert sock._proxy.host == 'other.example.com'
        assert sock._proxy.port == 8080

        # Invalid proxy types must raise AssertionError and leave state intact
        previous = sock._proxy
        for bad_type in (-1, 3, 99, None, 'SOCKS5', 2.0):
            try:
                sock.setproxy(bad_type, 'proxy.example.com', 1080)
            except AssertionError:
                pass
            else:
                raise AssertionError(
                    'setproxy accepted invalid proxy type %r' % (bad_type,))
            assert sock._proxy == previous
    finally:
        sock.close()

# Generated at 2026-10-25 09:04:02.090569
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

# Generated at 2026-10-25 09:04:03.626989
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

# Generated at 2026-10-25 09:04:05.159925
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

# Generated at 2026-10-25 09:04:06.707768
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

# Generated at 2026-10-25 09:04:08.177641
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

# Generated at 2026-10-25 09:04:10.596075
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

# Generated at 2026-10-25 09:04:12.128974
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

# Generated at 2026-10-25 09:04:14.665884
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:17.327667
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:20.024288
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:22.441449
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:25.246672
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:27.661912
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:30.114841
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:32.620247
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:35.192135
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:37.608812
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:40.025821
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:42.442785
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:44.861021
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:47.280622
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:49.695050
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:52.112530
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:54.529659
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:56.943816
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:04:59.363494
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:01.781349
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:04.197823
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:06.613554
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:09.030152
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:11.448220
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:13.866610
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:16.281321
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:18.730957
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:21.145889
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:23.560683
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:25.977510
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:28.394379
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:30.814116
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:33.230528
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:35.647612
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:38.064039
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:40.481704
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:42.901831
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:45.314922
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:47.733003
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:50.148070
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:52.564414
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:54.982842
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:57.407026
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:05:59.818579
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:02.236471
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:04.652639
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:07.068168
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:09.486128
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:13.109484
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:15.524834
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:17.943342
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:20.360583
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:22.780704
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:25.194987
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:27.612848
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:30.068954
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:32.521196
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:34.941290
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:37.355635
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:39.774185
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:42.191107
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:44.609083
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 09:06:47.026015
# Unit test for method recvall of class sockssocket
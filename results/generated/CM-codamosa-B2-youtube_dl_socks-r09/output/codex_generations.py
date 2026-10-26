

# Generated at 2026-10-25 07:15:21.260351
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:15:23.676967
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:15:26.090192
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:15:28.505017
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:30.921750
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:33.341980
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:35.755063
# Unit test for constructor of class ProxyType

# Generated at 2026-10-25 07:15:38.378884
# Unit test for constructor of class ProxyType

# Generated at 2026-10-25 07:15:40.795527
# Unit test for constructor of class ProxyType

# Generated at 2026-10-25 07:15:43.211788
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:45.633700
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:48.047797
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 07:15:50.464921
# Unit test for constructor of class Proxy

# Generated at 2026-10-25 07:15:52.880846
# Unit test for constructor of class Proxy

# Generated at 2026-10-25 07:15:58.836867
# Unit test for constructor of class Proxy
def test_Proxy():proxy = Proxy(ProxyType.SOCKS5, '127.0.0.1', 1080, 'user', 'pass', True)

# Generated at 2026-10-25 07:16:00.371869
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

# Generated at 2026-10-25 07:16:17.474114
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

# Generated at 2026-10-25 07:16:18.909486
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

# Generated at 2026-10-25 07:16:20.273721
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

# Generated at 2026-10-25 07:16:37.955498
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 07:16:40.372570
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 07:16:42.787368
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 07:16:45.202518
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:16:47.619124
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:16:50.032873
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:16:52.447834
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-25 07:17:03.348096
# Unit test for constructor of class Socks4Error
def test_Socks4Error():err = Socks4Error(91)

# Generated at 2026-10-25 07:17:09.721610
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

# Generated at 2026-10-25 07:17:33.831941
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

# Generated at 2026-10-25 07:17:36.253479
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:38.667919
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:41.082259
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:43.496439
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:45.912888
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:48.329338
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:50.742711
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:53.160164
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:55.691225
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:17:58.011580
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:00.429713
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:02.847798
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:05.259597
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:07.678243
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:10.095752
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:12.510457
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:14.927392
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:17.343444
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:19.758090
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:22.177204
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:24.594536
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:27.008837
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:29.426665
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:31.843611
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:34.261379
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:36.674219
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:39.092504
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 07:18:41.509827
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:18:43.921958
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:18:46.341411
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:18:48.756422
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:51.171538
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:53.588874
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:56.005897
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:18:58.417688
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:00.832028
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:03.250679
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:05.666599
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:08.080162
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:10.498738
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:12.916142
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:15.329127
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:17.748255
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:20.164714
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:22.577924
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:24.997827
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:27.413321
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:29.828878
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:32.245782
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:34.663543
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:37.119859
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:39.587475
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:41.990775
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:44.409995
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:19:46.823494
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:49.242096
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:51.659177
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:54.070290
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:56.486810
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:19:58.904804
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:01.352530
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:03.737857
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:06.153023
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:08.591842
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:11.004978
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:13.423209
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:15.836921
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:18.252394
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:20.665316
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:23.082076
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:25.507744
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:27.923235
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:30.341597
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:32.755094
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:35.173832
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:37.589695
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:40.006560
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:42.419611
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:44.838924
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:47.255678
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:49.727069
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:20:52.126193
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:54.545839
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:56.957864
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:20:59.375191
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:01.791911
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:04.207161
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:06.651769
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:09.065666
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:11.480056
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 07:21:13.898032
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:16.314462
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:18.732520
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:21.444634
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:23.862554
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:26.279480
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:28.692260
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:31.103593
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:33.520231
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:35.973441
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:38.388050
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:40.802878
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:43.216436
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:45.629568
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:48.045709
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:50.460576
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:52.873747
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:55.287253
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:57.701685
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:21:59.301714
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 07:22:00.720110
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 07:22:02.258093
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

# Generated at 2026-10-25 07:22:03.691664
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

# Generated at 2026-10-25 07:22:05.037929
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

# Generated at 2026-10-25 07:22:06.565420
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

# Generated at 2026-10-25 07:22:08.184192
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

# Generated at 2026-10-25 07:22:09.557066
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

# Generated at 2026-10-25 07:22:10.946540
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

# Generated at 2026-10-25 07:22:12.395165
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

# Generated at 2026-10-25 07:22:13.826932
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

# Generated at 2026-10-25 07:22:15.263256
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

# Generated at 2026-10-25 07:22:16.695711
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

# Generated at 2026-10-25 07:22:19.113427
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:21.703023
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:24.113719
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:26.529553
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:29.108458
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:31.652960
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:34.065954
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:36.479548
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:38.894037
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:41.398697
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:43.811460
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:46.224826
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:48.665364
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:51.080188
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:53.495334
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:55.910627
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:22:58.329614
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:00.746561
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:03.161619
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:05.576807
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:07.990033
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:10.408439
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:12.823322
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:15.239687
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:17.652287
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:20.064519
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:22.477350
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:24.891204
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:27.309086
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:29.832654
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:32.167137
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:34.582777
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:37.092644
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:39.538603
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:41.955698
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:44.368343
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:46.784126
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:49.197496
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:23:51.815753
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 07:23:54.567826
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

# Generated at 2026-10-25 07:23:55.902829
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

# Generated at 2026-10-25 07:23:57.244589
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

# Generated at 2026-10-25 07:23:58.571212
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

# Generated at 2026-10-25 07:23:59.915538
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

# Generated at 2026-10-25 07:24:01.349415
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

# Generated at 2026-10-25 07:24:02.785937
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

# Generated at 2026-10-25 07:24:04.129193
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

# Generated at 2026-10-25 07:24:05.479919
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

# Generated at 2026-10-25 07:24:06.880074
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

# Generated at 2026-10-25 07:24:08.721489
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

# Generated at 2026-10-25 07:24:10.154973
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

# Generated at 2026-10-25 07:24:11.590486
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

# Generated at 2026-10-25 07:24:14.125831
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:16.798684
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:19.211234
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:21.743677
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:24.159876
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:26.575211
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:28.990337
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:31.404281
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:33.817646
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:36.233218
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:38.645708
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:41.061342
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:43.473806
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:45.889680
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:48.303658
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:50.719914
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:53.132753
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:55.547108
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:24:57.966558
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:25:00.400410
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 07:25:01.864767
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 07:25:05.450775
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

# Generated at 2026-10-25 07:25:06.991771
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

# Generated at 2026-10-25 07:25:08.389962
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

# Generated at 2026-10-25 07:25:09.862906
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

# Generated at 2026-10-25 07:25:11.287962
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

# Generated at 2026-10-25 07:25:12.742491
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

# Generated at 2026-10-25 07:25:14.089566
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

# Generated at 2026-10-25 07:25:15.488398
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

# Generated at 2026-10-25 07:25:16.944993
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

# Generated at 2026-10-25 07:25:18.357255
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
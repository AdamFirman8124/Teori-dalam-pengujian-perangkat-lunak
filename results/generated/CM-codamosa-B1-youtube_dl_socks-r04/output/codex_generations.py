

# Generated at 2026-10-24 15:51:10.480277
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

# Generated at 2026-10-24 15:51:20.608135
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    obj = Socks5AddressType()

    assert isinstance(obj, Socks5AddressType)
    assert Socks5AddressType.ATYP_IPV4 == 0x01
    assert Socks5AddressType.ATYP_DOMAINNAME == 0x03
    assert Socks5AddressType.ATYP_IPV6 == 0x04

# Generated at 2026-10-24 15:51:23.501205
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 15:52:29.005439
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 15:52:31.542416
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 15:53:32.806883
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:53:48.483215
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():import socket

# Generated at 2026-10-24 15:53:51.340885
# Unit test for method connect of class sockssocket

# Generated at 2026-10-24 15:54:07.931620
# Unit test for method connect of class sockssocket
def test_sockssocket_connect():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:54:10.447256
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:54:12.862735
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:54:15.441012
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:54:17.849051
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 15:54:20.394824
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 15:54:22.807032
# Unit test for constructor of class Socks5Error

# Generated at 2026-10-24 15:54:25.219922
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 15:54:27.632274
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 15:54:30.044917
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 15:54:32.458167
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:54:34.871224
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:54:52.167418
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-24 15:54:55.239079
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:55:15.207785
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():import socket

# Generated at 2026-10-24 15:55:16.846670
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

# Generated at 2026-10-24 15:55:50.433971
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    expected_version = 0x05
    got_version = 0x04

    err = InvalidVersionError(expected_version, got_version)

    expected_msg = (
        'Invalid response version from server. '
        'Expected 05 got 04'
    )

    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (0, expected_msg)
    assert err.args[0] == 0
    assert err.args[1] == expected_msg

    # hex formatting is zero-padded, lowercase `02x`
    err2 = InvalidVersionError(0x00, 0xFF)
    assert err2.args == (
        0,
        'Invalid response version from server. Expected 00 got ff'
    )

# Generated at 2026-10-24 15:55:51.957274
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    expected_version = 0x05
    got_version = 0x04

    err = InvalidVersionError(expected_version, got_version)

    expected_msg = (
        'Invalid response version from server. '
        'Expected 05 got 04'
    )

    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (0, expected_msg)
    assert err.args[0] == 0
    assert err.args[1] == expected_msg

    # hex formatting is zero-padded, lowercase `02x`
    err2 = InvalidVersionError(0x00, 0xFF)
    assert err2.args == (
        0,
        'Invalid response version from server. Expected 00 got ff'
    )

# Generated at 2026-10-24 15:55:53.405178
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    expected_version = 0x05
    got_version = 0x04

    err = InvalidVersionError(expected_version, got_version)

    expected_msg = (
        'Invalid response version from server. '
        'Expected 05 got 04'
    )

    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (0, expected_msg)
    assert err.args[0] == 0
    assert err.args[1] == expected_msg

    # hex formatting is zero-padded, lowercase `02x`
    err2 = InvalidVersionError(0x00, 0xFF)
    assert err2.args == (
        0,
        'Invalid response version from server. Expected 00 got ff'
    )

# Generated at 2026-10-24 15:55:54.821145
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

# Generated at 2026-10-24 15:55:56.278348
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

# Generated at 2026-10-24 15:55:57.792672
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

# Generated at 2026-10-24 15:56:01.128969
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:56:02.721431
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():import socket

# Generated at 2026-10-24 15:56:20.471001
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

# Generated at 2026-10-24 15:56:22.885392
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:56:25.299286
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:56:27.712380
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:56:30.127086
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:56:32.540796
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:56:34.952581
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 15:56:37.365294
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:56:39.778741
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 15:57:07.133644
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-24 15:57:08.565932
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

# Generated at 2026-10-24 15:57:10.101660
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

# Generated at 2026-10-24 15:57:26.167879
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

# Generated at 2026-10-24 15:57:27.601064
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

# Generated at 2026-10-24 15:57:29.136883
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

# Generated at 2026-10-24 15:57:31.750392
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:57:34.163668
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:57:36.580881
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:57:38.990640
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:57:41.404433
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:57:54.851188
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 15:57:56.283987
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

# Generated at 2026-10-24 15:57:57.699957
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

# Generated at 2026-10-24 15:57:59.062414
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

# Generated at 2026-10-24 15:58:00.584785
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

# Generated at 2026-10-24 15:58:17.071144
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

# Generated at 2026-10-24 15:59:04.666730
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 15:59:23.005513
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 15:59:24.542936
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 15:59:57.322192
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = Mock()
    sock.recv.side_effect = [b'ab', b'cde']

    result = sockssocket.recvall(sock, 5)

    assert result == b'abcde'
    assert sock.recv.call_args_list == [
        call(5),
        call(3),
    ]

# Generated at 2026-10-24 16:00:08.587525
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        recvall = sockssocket.recvall

        def __init__(self, responses):
            self.responses = iter(responses)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self.responses)

    sock = FakeSocket([b'ab', b'c', b'def'])

    assert sock.recvall(6) == b'abcdef'
    assert sock.recv_sizes == [6, 4, 3]


def test_sockssocket_recvall_raises_on_eof():
    class FakeSocket(object):
        recvall = sockssocket.recvall

        def __init__(self):
            self.responses = iter([b'ab', b''])

        def recv(self, size):
            return next(self.responses)

    sock = FakeSocket()

    try:
        sock.recvall(4)
    except EOFError as error:
        assert str(error) == '2 bytes missing'
    else:
        raise AssertionError('EOFError was not raised')

# Generated at 2026-10-24 16:00:25.030850
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

# Generated at 2026-10-24 16:00:58.457763
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class ChunkedSocket(sockssocket):
        def __init__(self, chunks):
            super(ChunkedSocket, self).__init__()
            self._chunks = iter(chunks)
            self.recv_sizes = []

        def recv(self, size):
            self.recv_sizes.append(size)
            return next(self._chunks)

    sock = ChunkedSocket([b'ab', b'cd', b'e'])
    try:
        assert sock.recvall(5) == b'abcde'
        assert sock.recv_sizes == [5, 3, 1]
    finally:
        sock.close()

# Generated at 2026-10-24 16:01:16.477680
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


# Generated at 2026-10-24 20:47:37.079909
# Unit test for constructor of class ProxyError
def test_ProxyError():
    def test(self):
        # Base ProxyError with no arguments
        e = ProxyError()
        self.assertEqual(e.args, (None, None))

        # Base ProxyError with explicit message (base class has no CODES map)
        e = ProxyError(None, 'custom message')
        self.assertEqual(e.args, (None, 'custom message'))

        # Socks4Error resolves code 91 from its CODES table
        e = Socks4Error(91)
        self.assertEqual(e.args, (91, 'request rejected or failed'))

        # Socks4Error with unknown code falls back to 'unknown error'
        e = Socks4Error(99)
        self.assertEqual(e.args, (99, 'unknown error'))

        # Socks5Error resolves hex codes from its CODES table
        e = Socks5Error(0x03)
        self.assertEqual(e.args, (0x03, 'Network unreachable'))

        # Socks5Error authentication failure code
        e = Socks5Error(0xFE)
        self.assertEqual(e.args, (0xFE, 'unknown username or invalid password'))

        # Socks5Error with unknown code falls back to 'unknown error'
        e = Socks5Error(0xDE)
        self.assertEqual(e.args, (0xDE, 'unknown error'))

        # Socks5Error with explicit message overrides the CODES lookup
        e = Socks5Error(0x05, 'custom message')
        self.assertEqual(e.args, (0x05, 'custom message'))

        # InvalidVersionError formats both versions as two-digit hex
        e = InvalidVersionError(5, 4)
        self.assertEqual(
            e.args,
            (0, 'Invalid response version from server. Expected 05 got 04'))

        # Proxy hierarchy: all errors are socket.error subclasses
        self.assertTrue(issubclass(ProxyError, socket.error))
        self.assertTrue(issubclass(Socks4Error, ProxyError))
        self.assertTrue(issubclass(Socks5Error, ProxyError))
        self.assertTrue(issubclass(InvalidVersionError, ProxyError))

    # Run standalone, matching youtube-dl's test file style
    unittest.main()

# Generated at 2026-10-24 20:47:38.407552
# Unit test for constructor of class ProxyError
def test_ProxyError():err = ProxyError(42, "custom failure")

# Generated at 2026-10-24 20:47:56.663021
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-24 20:48:05.596813
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 20:48:06.941354
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Generated at 2026-10-24 20:48:23.525065
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:48:24.948973
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:48:26.382510
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:48:33.757190
# Unit test for constructor of class Socks5AddressType
def test_Socks5AddressType():
    address_type = Socks5AddressType()

    assert address_type.ATYP_IPV4 == 0x01
    assert address_type.ATYP_DOMAINNAME == 0x03
    assert address_type.ATYP_IPV6 == 0x04

# Generated at 2026-10-24 20:48:50.242546
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:48:51.678981
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:48:53.109204
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:49:24.034426
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

# Generated at 2026-10-24 20:49:31.110598
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:49:32.533445
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:49:33.966530
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:49:35.400485
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

# Generated at 2026-10-24 20:49:36.793807
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

# Generated at 2026-10-24 20:49:38.153701
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

# Generated at 2026-10-24 20:49:40.674393
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:49:43.092771
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:49:45.508758
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:49:47.927702
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 20:49:50.345158
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 20:49:52.761600
# Unit test for constructor of class ProxyError

# Generated at 2026-10-24 20:49:55.178710
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:49:57.597247
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:00.173755
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:02.601911
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 20:50:05.010378
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 20:50:07.424217
# Unit test for constructor of class InvalidVersionError

# Generated at 2026-10-24 20:50:09.841780
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:12.258125
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:14.673747
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:17.090987
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:19.508230
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:21.925720
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:24.341650
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:26.759261
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:29.174016
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:31.589906
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:34.006310
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:36.423890
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:38.840088
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:41.257885
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:43.675404
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:50:46.091566
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:48.509578
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:50.925353
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:53.343027
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:50:59.266507
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():sock = sockssocket()

# Generated at 2026-10-24 20:51:15.958808
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:51:17.390661
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:51:18.825418
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:51:45.040923
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class StubSocksSocket(sockssocket):
        def __init__(self, responses):
            super(StubSocksSocket, self).__init__()
            self.responses = iter(responses)

        def recv(self, count):
            data = next(self.responses)
            assert len(data) <= count
            return data

    sock = StubSocksSocket([b'ab', b'cd', b'ef'])
    try:
        assert sock.recvall(6) == b'abcdef'
    finally:
        sock.close()

# Generated at 2026-10-24 20:52:00.811243
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class FakeSocket(object):
        def __init__(self):
            self.chunks = [b'he', b'll', b'o']

        def recv(self, count):
            return self.chunks.pop(0)

    sock = FakeSocket()

    result = sockssocket.recvall(sock, 5)

    assert result == b'hello'


def test_sockssocket_recvall_raises_on_eof():
    class FakeSocket(object):
        def recv(self, count):
            return b''

    sock = FakeSocket()

    with pytest.raises(EOFError, match=r'5 bytes missing'):
        sockssocket.recvall(sock, 5)

# Generated at 2026-10-24 20:52:03.235928
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:05.656629
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:08.070128
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:10.491238
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:12.907039
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:15.324207
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:17.741645
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:20.158026
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:22.576012
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:45.149050
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:52:46.545605
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:52:47.905742
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:53:02.898931
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = Mock()
    sock.recv.side_effect = [b'he', b'll', b'o']

    result = sockssocket.recvall(sock, 5)

    assert result == b'hello'
    assert sock.recv.call_count == 3
    sock.recv.assert_any_call(5)
    sock.recv.assert_any_call(3)
    sock.recv.assert_any_call(1)


def test_sockssocket_recvall_raises_on_connection_close():
    sock = Mock()
    sock.recv.side_effect = [b'he', b'']

    try:
        sockssocket.recvall(sock, 5)
        assert False, 'Expected EOFError'
    except EOFError as exc:
        assert str(exc) == '3 bytes missing'

# Generated at 2026-10-24 20:53:05.438418
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:07.848653
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:10.389684
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:12.811973
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:15.229664
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:17.647236
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:20.065157
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:22.479792
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:24.898007
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:27.316060
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:29.731550
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:32.151228
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:34.569287
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:36.984703
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:43.099956
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:53:59.698066
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:54:01.133178
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:54:02.549691
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:54:03.955057
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

# Generated at 2026-10-24 20:54:18.435950
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    fake_socket = Mock()
    fake_socket.recv.side_effect = [b'ab', b'cde', b'f']

    result = sockssocket.recvall(fake_socket, 6)

    assert result == b'abcdef'
    assert fake_socket.recv.call_args_list == [
        ((6,),),
        ((4,),),
        ((1,),),
    ]


def test_sockssocket_recvall_raises_on_eof():
    fake_socket = Mock()
    fake_socket.recv.side_effect = [b'ab', b'']

    try:
        sockssocket.recvall(fake_socket, 5)
        assert False, 'Expected EOFError'
    except EOFError as exc:
        assert str(exc) == '3 bytes missing'

# Generated at 2026-10-24 20:54:20.855124
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:54:23.272903
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:54:25.690856
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:54:35.126898
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:54:36.559882
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:54:37.995729
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:54:54.483652
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:54:55.910910
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:54:57.321956
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:55:13.852655
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:16.271735
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:18.789508
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:21.206736
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:23.627502
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:26.042572
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:28.459566
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:30.877631
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:55:32.295138
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:56:04.630641
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:07.155222
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:09.572071
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:11.989984
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:14.406721
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:16.823792
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:19.237045
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:21.653429
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:24.069604
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:26.489783
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:28.904896
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:31.326132
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:33.742859
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:36.160604
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:38.578620
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:40.994473
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:43.411810
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:45.826553
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:48.244806
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:50.660835
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:53.076218
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:56:55.491134
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:56:57.908976
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:57:00.326836
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:57:02.740106
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:57:04.217164
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:57:05.623225
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-24 20:57:21.801618
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = mock.Mock()
    sock.recv.side_effect = [b'ab', b'cde']

    result = sockssocket.recvall(sock, 5)

    assert result == b'abcde'
    sock.recv.assert_has_calls([
        mock.call(5),
        mock.call(3),
    ])

# Generated at 2026-10-24 20:57:24.228474
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:57:26.643466
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:57:29.062609
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-24 20:57:31.586237
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:57:34.001892
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-24 20:57:36.417037
# Unit test for method recvall of class sockssocket
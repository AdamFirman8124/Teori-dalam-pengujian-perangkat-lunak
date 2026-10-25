

# Generated at 2026-10-25 04:14:58.391121
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 04:15:00.807151
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 04:15:03.221909
# Unit test for method connect of class sockssocket

# Generated at 2026-10-25 04:15:05.636620
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:08.051211
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:10.465288
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:12.879603
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:15.296032
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:17.710780
# Unit test for constructor of class sockssocket

# Generated at 2026-10-25 04:15:20.126521
# Unit test for method connect_ex of class sockssocket

# Generated at 2026-10-25 04:15:31.131708
# Unit test for method connect_ex of class sockssocket
def test_sockssocket_connect_ex():from unittest.mock import patch


# Generated at 2026-10-25 04:15:37.272902
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='testuser',
            password='testpass',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'testuser',
            'testpass',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:15:49.711279
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    # Known codes map to their messages, passed as (code, msg) to socket.error
    assert Socks4Error(91).args == (91, "request rejected or failed")
    assert Socks4Error(92).args == (
        92,
        "request rejected because SOCKS server cannot connect to identd on the client",
    )
    assert Socks4Error(93).args == (
        93,
        "request rejected because the client program and identd report different user-ids",
    )

    # Unknown code, including ERR_SUCCESS (90 is not in CODES)
    assert Socks4Error(90).args == (90, "unknown error")
    assert Socks4Error(999).args == (999, "unknown error")

    # Explicit message overrides the code lookup
    assert Socks4Error(91, "custom failure").args == (91, "custom failure")
    assert Socks4Error(None, "custom failure").args == (None, "custom failure")

    # No arguments
    assert Socks4Error().args == (None, None)

    # Inheritance and errno/strerror from OSError
    err = Socks4Error(91)
    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.errno == 91
    assert err.strerror == "request rejected or failed"
    assert Socks4Error.ERR_SUCCESS == 90

# Generated at 2026-10-25 04:15:56.910701
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='test-user',
            password='test-password',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'test-user',
            'test-password',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:15:59.443384
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:16:02.002665
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:16:04.418855
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:16:06.835938
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-25 04:16:09.380795
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-25 04:16:11.796386
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-25 04:16:14.392515
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 04:16:16.809329
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 04:16:19.221429
# Unit test for constructor of class ProxyError

# Generated at 2026-10-25 04:16:21.636202
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:16:24.052728
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:16:26.468657
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:16:28.886122
# Unit test for constructor of class Socks4Error

# Generated at 2026-10-25 04:16:35.002947
# Unit test for constructor of class Socks4Error
def test_Socks4Error():error = Socks4Error(91)

# Generated at 2026-10-25 04:16:36.388274
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

# Generated at 2026-10-25 04:16:43.400805
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='user',
            password='secret',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'user',
            'secret',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:16:44.813237
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

# Generated at 2026-10-25 04:16:46.268776
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

# Generated at 2026-10-25 04:16:53.845229
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    proxy_socket = sockssocket()
    try:
        proxy_socket.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='user',
            password='password',
        )

        assert proxy_socket._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'user',
            'password',
            False,
        )
    finally:
        proxy_socket.close()

# Generated at 2026-10-25 04:16:55.278397
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

# Generated at 2026-10-25 04:16:56.713663
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

# Generated at 2026-10-25 04:17:04.291428
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        result = sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='test-user',
            password='test-password',
        )

        assert result is None
        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            'test-user',
            'test-password',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:17:06.710462
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:09.124885
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:11.541352
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:13.955020
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:16.534925
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:18.949847
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:17:21.374677
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:23.790026
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:26.215703
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:28.630931
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:31.045844
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:33.461168
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:35.878154
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:17:42.179719
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():left, right = socket.socketpair()

# Generated at 2026-10-25 04:17:57.547921
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():from unittest.mock import patch


# Generated at 2026-10-25 04:17:58.954932
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

# Generated at 2026-10-25 04:18:00.338928
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

# Generated at 2026-10-25 04:18:01.839300
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

# Generated at 2026-10-25 04:18:09.315076
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='testuser',
            password='testpass',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            'testuser',
            'testpass',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:18:12.150178
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:14.564772
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:16.979548
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:19.403691
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:21.820306
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:24.539385
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:26.960941
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:29.386063
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:31.809353
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:34.223248
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:36.643312
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:39.061415
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:41.475982
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:43.899415
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:46.324531
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:18:48.741971
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:51.156531
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:53.572552
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:18:55.985681
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:19:06.935525
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():left, right = socket.socketpair()

# Generated at 2026-10-25 04:19:12.111529
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:19:13.519294
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

# Generated at 2026-10-25 04:19:14.916054
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

# Generated at 2026-10-25 04:19:16.287492
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

# Generated at 2026-10-25 04:19:17.657660
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

# Generated at 2026-10-25 04:19:19.048187
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

# Generated at 2026-10-25 04:19:20.448705
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

# Generated at 2026-10-25 04:19:21.819549
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

# Generated at 2026-10-25 04:19:23.217898
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

# Generated at 2026-10-25 04:19:24.588238
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

# Generated at 2026-10-25 04:19:25.955377
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

# Generated at 2026-10-25 04:19:27.445637
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

# Generated at 2026-10-25 04:19:34.659237
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='test-user',
            password='test-password',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'test-user',
            'test-password',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:19:37.198432
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:39.614157
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:42.156864
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:44.571152
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:46.984961
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:49.400512
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:51.815464
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:54.229425
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:56.645693
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:19:59.060434
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:20:01.475064
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:20:04.206579
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():s = sockssocket()

# Generated at 2026-10-25 04:20:05.610499
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

# Generated at 2026-10-25 04:20:12.604932
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='user',
            password='password',
        )

        assert sock._proxy == Proxy(
            type=ProxyType.SOCKS5,
            host='127.0.0.1',
            port=1080,
            username='user',
            password='password',
            remote_dns=False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:20:14.038034
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

# Generated at 2026-10-25 04:20:21.208674
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='user',
            password='secret',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            'user',
            'secret',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:20:27.454166
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            rdns=False,
            username='test-user',
            password='test-password',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            'proxy.example.com',
            1080,
            'test-user',
            'test-password',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:20:28.887127
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

# Generated at 2026-10-25 04:20:35.748048
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        assert sock._proxy is None

        sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='testuser',
            password='testpass',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            'testuser',
            'testpass',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:20:38.304016
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:20:40.842453
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:20:43.257092
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:20:45.674280
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:20:48.102043
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:20:50.516552
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:20:52.931052
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:20:55.346818
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:20:57.761092
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:00.176133
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:21:02.712798
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:21:05.128592
# Unit test for method setproxy of class sockssocket

# Generated at 2026-10-25 04:21:13.330511
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            rdns=False,
            username='testuser',
            password='testpass',
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            '127.0.0.1',
            1080,
            'testuser',
            'testpass',
            False,
        )
    finally:
        sock.close()

# Generated at 2026-10-25 04:21:14.772750
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

# Generated at 2026-10-25 04:21:19.421251
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

# Generated at 2026-10-25 04:21:20.795607
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

# Generated at 2026-10-25 04:21:22.237366
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

# Generated at 2026-10-25 04:21:23.671002
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

# Generated at 2026-10-25 04:21:25.115403
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

# Generated at 2026-10-25 04:21:26.641097
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

# Generated at 2026-10-25 04:21:28.085027
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

# Generated at 2026-10-25 04:21:29.465006
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

# Generated at 2026-10-25 04:21:30.870054
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

# Generated at 2026-10-25 04:21:32.272891
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

# Generated at 2026-10-25 04:21:39.343931
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

# Generated at 2026-10-25 04:21:40.712761
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

# Generated at 2026-10-25 04:21:42.204873
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

# Generated at 2026-10-25 04:21:44.794804
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:47.317176
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:49.735688
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:52.271244
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:54.692848
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:57.116333
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:21:59.538043
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:01.954143
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:04.367949
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:06.782346
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:09.197692
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:11.612418
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:14.030769
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:16.712669
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():s = sockssocket.__new__(sockssocket)

# Generated at 2026-10-25 04:22:23.231307
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():sender, receiver = socket.socketpair()

# Generated at 2026-10-25 04:22:24.622412
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

# Generated at 2026-10-25 04:22:26.146058
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

# Generated at 2026-10-25 04:22:39.344207
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

# Generated at 2026-10-25 04:22:40.880547
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

# Generated at 2026-10-25 04:22:42.262448
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

# Generated at 2026-10-25 04:22:43.619436
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

# Generated at 2026-10-25 04:22:44.989620
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

# Generated at 2026-10-25 04:22:51.130651
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

# Generated at 2026-10-25 04:22:52.535723
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

# Generated at 2026-10-25 04:22:53.987183
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

# Generated at 2026-10-25 04:22:56.626016
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:22:59.149084
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:23:01.564105
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:23:03.977904
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:23:06.545950
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:23:08.960422
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:23:32.834142
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

# Generated at 2026-10-25 04:23:34.333444
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

# Generated at 2026-10-25 04:23:35.766276
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

# Generated at 2026-10-25 04:23:37.200237
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

# Generated at 2026-10-25 04:23:38.633964
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

# Generated at 2026-10-25 04:23:40.067798
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

# Generated at 2026-10-25 04:23:41.502140
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

# Generated at 2026-10-25 04:23:42.901579
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

# Generated at 2026-10-25 04:23:44.367820
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

# Generated at 2026-10-25 04:23:45.801203
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

# Generated at 2026-10-25 04:24:37.172732
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:39.586993
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:42.002684
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:44.417836
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:46.831727
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:49.246318
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:51.663276
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:54.079925
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:56.497672
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:24:58.912925
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:25:01.327300
# Unit test for method recvall of class sockssocket

# Generated at 2026-10-25 04:25:03.744733
# Unit test for method recvall of class sockssocket
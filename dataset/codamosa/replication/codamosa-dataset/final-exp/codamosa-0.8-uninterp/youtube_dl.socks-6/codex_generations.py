

# Generated at 2022-06-14 18:09:35.832386
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    test_data = b'0123456789'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        with sockssocket(socket.AF_INET, socket.SOCK_STREAM) as s_sock:
            s_sock.connect(s.getsockname())
            conn, _ = s.accept()
            conn.sendall(test_data)
            conn.close()
            data = s_sock.recvall(len(test_data))
            assert(data == test_data)

# Generated at 2022-06-14 18:09:46.786011
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import sys
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    def test_recv(buffer_size=1, data=b'hello'):
        s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

        data = bytearray(data, 'latin-1')
        split_idx = 1
        received_bytes = 0
        while received_bytes < len(data):
            s.recv.return_value = data[received_bytes:min(received_bytes + buffer_size, len(data))]
            if received_bytes < split_idx:
                s.recv.return_value = b''
            received_bytes = s.recv.call_count
            if received_bytes >= len(data):
                s

# Generated at 2022-06-14 18:09:53.473982
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    ss = sockssocket()
    ss.connect(('example.com', 80))
    import time, random
    data = str(time.time())
    request_str = 'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11\r\nX-Message: %s\r\n\r\n' % (data)
    ss.sendall(request_str)
    response_str = ss.recvall(4096) #4096 is enough
    assert response_str.find(data) != -1

# Generated at 2022-06-14 18:09:54.005020
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    pass

# Generated at 2022-06-14 18:10:00.039571
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    class MockSocket(sockssocket):
        def __init__(self, *args, **kwargs):
            pass

        def connect(self, address):
            pass

        def recv(self, cnt):
            return b'\x00' * cnt

    s = MockSocket()
    assert s.recvall(10) == b'\x00' * 10



# Generated at 2022-06-14 18:10:10.841054
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import sys
    import time
    if sys.version_info.major == 2:
        import StringIO
        file_obj = StringIO.StringIO()
    else:
        import io
        file_obj = io.BytesIO()

    ss = sockssocket()
    ss.setproxy(ProxyType.SOCKS4A, 'target_host', 1080)
    def _slow_send(data):
        for chunk in [data[i:i+1] for i in range(len(data))]:
            file_obj.write(chunk)
            time.sleep(0.01)
    ss.recv = file_obj.read
    ss.sendall = _slow_send
    ss.connect(('localhost', 80))
    assert('HTTP' == ss.recv(4))

# Generated at 2022-06-14 18:10:22.599673
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import struct
    # Create a simple TCP server
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(('127.0.0.1', 0))
    srv.listen(1)
    srv_port = srv.getsockname()[1]

    # Send a string of length 10 to it
    mystr = '1234567890'
    cli = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

    srv_conn, addr = srv.accept()
    srv_conn.send(str.encode(mystr))

    # Connect to it
    cli.connect(('127.0.0.1', srv_port))
    # Receive the string
    res = cli.recv

# Generated at 2022-06-14 18:10:29.102667
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    try:
        sockssocket.recvall(None, None)
    except TypeError:
        print("Unit test for method recvall of class sockssocket: PASSED")
    except:
        print("Unit test for method recvall of class sockssocket: FAILED")
    else:
        print("Unit test for method recvall of class sockssocket: FAILED")


# Generated at 2022-06-14 18:10:32.616577
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sockssocket.recvall('', 0)

vers = tuple(map(int, socket.__version__.split('.')))
if vers >= (2, 7):
    sockssocket.recv_into = sockssocket.makefile = None

# Generated at 2022-06-14 18:10:39.848337
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    lport = s.getsockname()[1]
    p = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    p.connect(('127.0.0.1', lport))
    l, addr = s.accept()
    l.sendall(b'abcdefg')
    assert p.recvall(5) == b'abcde'
    assert p.recvall(100) == b'fg'
    l.sendall(b'abc')
    assert p.recvall(10) == b'abc'
    l.close()
    p.close()



# Generated at 2022-06-14 18:11:05.051419
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import os
    os.system("python pycurl_sockssocket_recvall_test.py")


# Generated at 2022-06-14 18:11:09.559144
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    test_socket = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.settimeout(2)
    test_socket.connect(('ya.ru', 80))
    assert len(test_socket.recvall(4)) == 4
    test_socket.close()

# Generated at 2022-06-14 18:11:16.511067
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall(): 
    s = sockssocket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setproxy(ProxyType.SOCKS5, "127.0.0.1", 1080)
    s.connect(("youtube.com", 80))
    data = s.recvall(20)
    s.close()
    print(data)

test_sockssocket_recvall()

# Generated at 2022-06-14 18:11:22.354759
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('example.org', 80))
    data = compatible_bytes('GET / HTTP/1.1\r\nHost: example.org\r\n\r\n', 'utf-8')
    sock.sendall(data)
    size = len(sock.recv(4096))
    assert sock.recvall(size)

# Generated at 2022-06-14 18:11:27.609128
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket()
    dat = b'aaaaaaaaaaaaaaaaaaaa'
    s.sendall(dat)
    assert(s.recvall(len(dat)) == dat)
    s.close()

if __name__ == '__main__':
    test_sockssocket_recvall()

# Generated at 2022-06-14 18:11:30.035325
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    ss = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect(('localhost', 22))
    ss.sendall(b'hello world')
    print(ss.recvall(11))
    ss.close()

# Generated at 2022-06-14 18:11:40.613622
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    ss = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

    ss.setproxy(ProxyType.SOCKS4, '192.168.1.1', 9050)
    try:
        ss.recvall(1)
    except EOFError:
        pass
    else:
        assert False

    ss.close()
    ss = sockssocket(socket.AF_INET, socket.SOCK_STREAM)

    ss.setproxy(ProxyType.SOCKS4, '192.168.1.1', 9050)
    try:
        ss.recvall(2)
    except EOFError:
        pass
    else:
        assert False

    ss.close()

# Generated at 2022-06-14 18:11:47.419367
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    test_packet = b'Hello, World!'
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.bind(('localhost', 0))
    test_socket.listen(1)
    test_addr = test_socket.getsockname()

    client = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((test_addr[0], test_addr[1]))

    server, _ = test_socket.accept()
    server.send(test_packet)
    server.close()

    assert(client.recvall(len(test_packet)) == test_packet)

    test_socket.close()
    client.close()


# Generated at 2022-06-14 18:11:53.512722
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest

    class TestSockssocketRecvall(unittest.TestCase):
        def setUp(self):
            self.s = sockssocket()

        def test_recvall(self):
            self.assertEqual(self.s.recvall(1), b'')
            self.assertEqual(self.s.recvall(1), b'')

    unittest.main()

# Entry function of sockssocket unit test.
# Can be run directly.

# Generated at 2022-06-14 18:12:04.138952
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    ss = sockssocket()
    # We need to define at least 2 functions to avoid the "unexpected
    # indent" error (see https://github.com/ytdl-org/youtube-dl/issues/8980)
    def helper1(sock, buf):
        return [b'first', b'second']

    def helper2(sock, buf):
        return [b'third']

    ss.recv = helper1
    # Test if it works for one call
    assert ss.recvall(6) == b'firsts'
    # Test if it works for multiple calls
    ss.recv = helper2
    assert ss.recvall(6) == b'third'

# Generated at 2022-06-14 18:12:20.995515
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket()
    assert s.recvall(3) == b'\x00\x00\x00'


# Generated at 2022-06-14 18:12:32.849539
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import binascii
    from .compat import compat_urllib_request
    import unittest

    def hex_to_bin(s):
        return binascii.unhexlify(s.encode('ascii'))
    def bin_to_hex(s):
        return binascii.hexlify(s).decode('ascii')

    class TestSockssocketRecvall(unittest.TestCase):
        def test_recvall(self):
            sock = sockssocket()

            # 10 bytes
            expected = hex_to_bin('2b 3c 6e 77 7d')
            sock.recv = lambda cnt: expected[:cnt]
            self.assertEqual(expected, sock.recvall(len(expected)))

            # 11 bytes

# Generated at 2022-06-14 18:12:44.745048
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.google.com', 80))

    req = b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n'
    sock.sendall(req)

    status_line = compat_ord(sock.recv(1)) == ord('H')
    header_data = sock.recvall(9)
    header_stop = header_data.startswith(b'TTP/1.1') or header_data == b'HTTP/1.0'

    if not status_line or not header_stop:
        raise Exception("HTTP response status line or header doesn't match")

# Generated at 2022-06-14 18:12:52.966077
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 6667))
    s2 = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    s2.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
    s2.connect(('127.0.0.1', 6667))


# Generated at 2022-06-14 18:12:57.193800
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    def recvall_mock(cnt):
        return '0'*cnt
    sock.recv = recvall_mock
    assert sock.recvall(4) == '0000'
    assert sock.recvall(8) == '00000000'

# Generated at 2022-06-14 18:13:05.696826
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    # Test on both Python 2 and Python 3
    try:
        # Python 2
        import SocketServer
        from threading import Thread
    except ImportError:
        # Python 3
        import socketserver as SocketServer
        from threading import Thread

    class ThreadedMyTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
        pass

    class MyTCPHandler(SocketServer.BaseRequestHandler):
        def handle(self):
            self.request.sendall(b'hello')

    class RecvallTest(object):
        def test_recvall(self):
            # Set up
            server = ThreadedMyTCPServer(('localhost', 0), MyTCPHandler)

            _, port = server.server_address
            # Start thread to listen

# Generated at 2022-06-14 18:13:16.000775
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    with sockssocket() as sock:
        import struct
        import time
        import random
        import threading

        def send(sock):
            time.sleep(0.1)
            sock.sendall(struct.pack('h', 1))
        t = threading.Thread(target=send, args=(sock,))
        t.start()
        sock.bind(('',random.randint(10000,60000)))
        sock.listen(1)
        c,a = sock.accept()
        assert (1,) == struct.unpack('h', c.recvall(2))
        c.close()
        t.join()

if __name__ == '__main__':
    test_sockssocket_recvall()

# Generated at 2022-06-14 18:13:19.341538
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    with sockssocket() as ss:
        #should send all data in one go, so no empty recv expected
        ss.sendall(b'Test')
        ss.settimeout(1)
        #recv 4 bytes
        ss.recvall(4)


# Generated at 2022-06-14 18:13:28.893429
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    print('Testing method recvall of class sockssocket')
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    req = (b'GET / HTTP/1.0\r\n'
           b'Host: www.google.com\r\n'
           b'\r\n')
    s.sendall(req)
    resp_len = int(s.recv(4))
    resp = s.recvall(resp_len)
    print('recvall method test passed')


if __name__ == '__main__':
    test_sockssocket_recvall()

# Generated at 2022-06-14 18:13:39.408152
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import pytest
    wrong_data = b'asdfasd'
    correct_data = b'hi'
    ss = sockssocket()
    ss.recv = lambda: wrong_data
    with pytest.raises(EOFError) as excinfo:
        ss.recvall(5)
    assert '5 bytes missing' in str(excinfo.value)
    ss.recv = lambda: correct_data
    assert ss.recvall(2) == correct_data
    assert ss.recvall(3) == correct_data + correct_data

# Reference server implementation:
# https://github.com/romanz/socks5server/blob/master/socks5.py


# Generated at 2022-06-14 18:14:03.380658
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    assert sock.recvall(0) == b''
    assert sock.recvall(2) == b'XX'

    sock.close()
    try:
        sock.recvall(2)
        assert False, 'Expected EOFError'
    except EOFError:
        pass

    try:
        sock.recvall(4)
        assert False, 'Expected EOFError'
    except EOFError:
        pass

    sock = sockssocket()
    try:
        sock.recvall(-1)
        assert False, 'Expected ValueError'
    except ValueError:
        pass



# Generated at 2022-06-14 18:14:13.516721
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import mock

    class TestRecvAll(unittest.TestCase):
        def setUp(self):
            self.mock_sock = mock.MagicMock(socket.socket)
            self.mock_sock.recv.return_value = b'foo'

            self.socksocket = sockssocket()
            self.socksocket.recv = self.mock_sock.recv
            self.socksocket.recvall(0)
            self.socksocket.recvall(3)


# Generated at 2022-06-14 18:14:20.663678
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    t_address = ('127.0.0.1', 8080)
    s = sockssocket()
    s.connect(t_address)
    try:
        # test with normal case
        s.sendall(b'test http server!')
        assert s.recvall(16) == b'test http server!'
        # test with abnormal case
        s.sendall(b'1')
        try:
            s.recvall(16)
        except EOFError as e:
            assert str(e) == '15 bytes missing'
    finally:
        s.close()



# Generated at 2022-06-14 18:14:30.459593
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import random

    sock = sockssocket()

    # Test reading 0 bytes.
    assert sock.recvall(0) == b''
    # Test reading 1 byte
    sock.sendall(compat_struct_pack('!B', 0xFF))
    assert sock.recvall(1) == compat_struct_pack('!B', 0xFF)
    # Try again, but now with 2 bytes at once
    sock.sendall(compat_struct_pack('!BB', 0xFF, 0xFF))
    assert sock.recvall(1) == compat_struct_pack('!B', 0xFF)
    # Test reading == cnt bytes
    assert sock.recvall(1) == compat_struct_pack('!B', 0xFF)
    # Test reading more than cnt bytes
    assert sock.recv

# Generated at 2022-06-14 18:14:40.952746
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest, mock

    class TestRecvAll(unittest.TestCase):
        def setUp(self):
            self.socket = sockssocket()

        def test_all_data(self):
            with mock.patch.object(self.socket, 'recv') as mock_recv:
                mock_recv.side_effect = [b'foo', b'bar']
                self.assertEqual(self.socket.recvall(6), b'foobar')

        def test_not_all_data(self):
            with mock.patch.object(self.socket, 'recv') as mock_recv:
                mock_recv.side_effect = [b'foo', b'bar']
                with self.assertRaises(EOFError):
                    self.socket.recvall(7)

   

# Generated at 2022-06-14 18:14:46.502567
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 12345))
    sock.sendall(b'abc')
    assert sock.recvall(3) == b'abc'
    sock.close()

# Generated at 2022-06-14 18:14:53.591607
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    # Test for correct receiving
    buffer = b'hello world!'
    for i in range(10):
        sock.recvall(len(buffer)) == buffer
    # Test for correct exception raising on empty buffer
    try:
        sock.recvall(0)
        assert False
    except Exception:
        pass
    # Test for correct exception raising on partial buffer
    try:
        sock.recvall(len(buffer) + 1)
        assert False
    except Exception:
        pass

# Generated at 2022-06-14 18:15:02.014435
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import os
    import unittest

    class Test(unittest.TestCase):
        def setUp(self):
            self.file_to_read = os.path.join(os.path.dirname(__file__), 'resources', 'test_data.txt')

        def test_sockssocket_recvall(self):
            # Arrange
            test_content = '111111111'
            test_content_len = len(test_content)
            test_s = sockssocket()

            # Act
            with open(self.file_to_read, 'r') as rf:
                res = test_s.recvall(test_content_len)

            # Assert
            self.assertEqual(res, test_content)


if __name__ == '__main__':
    import unittest

# Generated at 2022-06-14 18:15:05.368713
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket()
    # Test with valid data
    s.recv_data = b'abcde'
    assert s.recvall(2) == b'ab'
    assert s.recvall(3) == b'cde'
    # Test with invalid data
    s.recv_data = b'abcd'
    try:
        assert s.recvall(5) == b'abcde'
    except EOFError:
        pass
    else:
        assert False, 'Exception not raised'

# Generated at 2022-06-14 18:15:09.664194
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    H = '127.0.0.1'
    P = 9000
    from .test_sock import MockSocket
    mock_socket = MockSocket(MockSocket.HELLO_WORLD_RESPONSE)
    sockssocket.recvall(mock_socket, len(MockSocket.HELLO_WORLD_RESPONSE))


# Generated at 2022-06-14 18:15:29.315910
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket()
    # Test recvall with no data
    s.recvall(0)
    s.close()

    # Test recvall with incomplete data
    s = sockssocket()
    s.connect(('example.com', 80))
    s.sendall(b'GET / HTTP/1.1\r\n\r\n')
    s.recvall(4)
    s.close()

# Generated at 2022-06-14 18:15:39.837422
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    test = sockssocket()
    test.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    test.bind(('127.0.0.1', 8001))
    test.listen(1)
    client = sockssocket()
    client.connect(('127.0.0.1', 8001))
    server, addr = test.accept()
    server.sendall(b'\x00\x00\x00\x00')  # 4 bytes
    server.close()
    c = client.recvall(4)  # 4 bytes
    client.close()
    test.close()
    if c == b'\x00\x00\x00\x00':
        print('sockssocket.recvall works fine')

# Generated at 2022-06-14 18:15:46.998715
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import socks
    import select
    import threading
    import time
    import re


    # Test data
    test_data_strings = [
        'http://httpbin.org/headers',
        'http://httpbin.org/connection',
        'http://httpbin.org/html',
        'http://httpbin.org/base64/SFRUUEJJTiBpcyBhd2Vzb21l',
        'http://httpbin.org/uuid',
        'http://httpbin.org/get',
    ]
    # test_data_strings = ['http://httpbin.org/base64/SFRUUEJJTiBpcyBhd2Vzb21l']

    # Test case
    class TestCase(object):
        def __init__(self, test_data):
            self.test_data

# Generated at 2022-06-14 18:15:48.012402
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    pass


# Generated at 2022-06-14 18:15:52.592919
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    def _test(cnt):
        s = sockssocket()
        s.recvall(cnt)
        assert False  # Shouldn't reach this point

    try:
        _test(0)
        _test(1)
    except EOFError:
        return

    assert False  # Shouldn't reach this point

# Generated at 2022-06-14 18:16:03.076236
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest
    class TestSockssocket(unittest.TestCase):
        def test_recvall(self):
            test_socket = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
            test_socket.setblocking(1)
            test_socket.connect(("www.google.com", 80))
            http_request = b'GET / HTTP/1.1\nHost: www.google.com\n\n'
            test_socket.sendall(http_request)
            response = test_socket.recvall(512)
            test_socket.close()
            self.assertGreater(len(response), 0)
    unittest.main()


# Generated at 2022-06-14 18:16:12.949276
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest
    import socket
    import select
    
    class TestSocket(sockssocket):
        def recv(self, cnt):
            return super(TestSocket, self).recv(1)

    class TestStringSocket(unittest.TestCase):

        def setUp(self):
            self.socket = TestSocket()

        def testRecvAll(self):
            self.socket.recvAllData = "abcdef"
            result = self.socket.recvall(3)
            self.assertEqual("abc", result)

        def testRecvAllEmpty(self):
            self.socket.recvAllData = ""
            self.assertRaises(EOFError, self.socket.recvall, 3)

        def testRecvAllExceeded(self):
            self.socket.recv

# Generated at 2022-06-14 18:16:23.458263
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import test.support
    import unittest
    import io
    import sys

    class SocksSocketRecvAllTestCase(unittest.TestCase):
        def _do_test(self, base_bytes, n, expected_bytes):
            server = sockssocket()
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            address = server.getsockname()
            client = sockssocket()
            client.connect(address)
            client = sockssocket(client.accept()[0])
            client.setblocking(True)
            server = sockssocket(client.accept()[0])
            server.setblocking(True)
            server.sendall(base_bytes)
            received_bytes = client.recvall(n)

# Generated at 2022-06-14 18:16:28.319716
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS4, '1.1.1.1', 1)
    print(s._proxy)


if __name__ == '__main__':
    test_sockssocket_recvall()

# Generated at 2022-06-14 18:16:35.736923
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.python.org', 80))

    s.sendall(b'GET / HTTP/1.0\r\n\r\n')
    result = b''

    while len(result) < 14:
        cur = s.recv(14 - len(result))
        if not cur:
            raise EOFError('14 bytes missing')
        result += cur

    result = result.decode('latin-1')
    assert result == 'HTTP/1.0 200 OK\r\n'

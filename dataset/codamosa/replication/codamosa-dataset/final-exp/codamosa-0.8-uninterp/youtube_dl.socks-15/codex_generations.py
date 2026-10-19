

# Generated at 2022-06-14 18:09:20.447078
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    err_msg = 'method recvall() failed to reiceve data through TCP socket'

# Generated at 2022-06-14 18:09:28.472247
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    a = sockssocket()
    assert a._proxy == None

    a.setproxy(ProxyType.SOCKS4, "127.0.0.1", 1080)
    assert a._proxy.type == ProxyType.SOCKS4
    assert a._proxy.host == '127.0.0.1'
    assert a._proxy.port == 1080
    assert a._proxy.username is None
    assert a._proxy.password is None
    assert a._proxy.remote_dns is True

    a.setproxy(ProxyType.SOCKS4, "127.0.0.1", 1080, username="username12345")
    assert a._proxy.username == "username12345"
    a.setproxy(ProxyType.SOCKS4, "127.0.0.1", 1080, password="password12345")
    assert a

# Generated at 2022-06-14 18:09:31.941901
# Unit test for constructor of class ProxyError
def test_ProxyError():
    with pytest.raises(ProxyError):
        ProxyError(1, 'a')


# Generated at 2022-06-14 18:09:33.962315
# Unit test for constructor of class Socks5Error
def test_Socks5Error():
    err = Socks5Error(0x01)
    assert err.args == (0x01, 'general SOCKS server failure')



# Generated at 2022-06-14 18:09:38.577451
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    exception_raised = False
    try:
        raise InvalidVersionError(SOCKS4_VERSION, SOCKS4_REPLY_VERSION)
    except InvalidVersionError as e:
        if e.strerror == 'Invalid response version from server. Expected 04 got 00':
            exception_raised = True
    assert exception_raised



# Generated at 2022-06-14 18:09:49.156068
# Unit test for constructor of class InvalidVersionError
def test_InvalidVersionError():
    expected_version = 0x00
    got_version = 0x01
    iv_error = InvalidVersionError(expected_version, got_version)
    assert(iv_error.errno == 0)
    input_string = '{0:02x}'.format(expected_version)
    output_string = '0'
    assert(input_string == output_string)
    input_string = '{0:02x}'.format(got_version)
    output_string = '1'
    assert(input_string == output_string)
    input_string = 'Invalid response version from server. Expected {0:02x} got {1:02x}'.format(expected_version, got_version)
    output_string = 'Invalid response version from server. Expected 0x00 got 0x01'

# Generated at 2022-06-14 18:09:59.644941
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest
    import uuid
    import base64
    import select

    class Test(unittest.TestCase):
        def test_basic(self):
            def client(server_address):
                with sockssocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(server_address)
                    test_message = base64.b64encode(uuid.uuid4().bytes)
                    sent_cnt = sock.send(test_message)
                    self.assertEqual(sent_cnt, len(test_message))

            def server(server_address):
                with sockssocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.bind(server_address)
                    sock.listen(1)

                    rlist, _,

# Generated at 2022-06-14 18:10:03.661531
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    '''
    This is a unit test for method recvall of class sockssocket
    This unit test should be run with following command in a Python 2.7 interpreter:
    import sockssocket
    sockssocket.test_sockssocket_recvall()
    '''
    import sys
    import socket
    import thread
    import random

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.st

# Generated at 2022-06-14 18:10:11.017481
# Unit test for constructor of class Socks4Error
def test_Socks4Error():
    error_code = 91
    error_msg = 'request rejected or failed'
    try:
        raise Socks4Error(error_code)
    except Socks4Error as e:
        assert e.errno == error_code
        assert e.strerror == error_msg
        print('Socks4Error constructor tests passed')


# Generated at 2022-06-14 18:10:17.388533
# Unit test for constructor of class ProxyError
def test_ProxyError():
    with pytest.raises(TypeError):
        ProxyError()
    with pytest.raises(TypeError):
        ProxyError('error message')
    assert isinstance(ProxyError(0, ''), ProxyError)
    assert (ProxyError(0, '').args == (0, '') and
            ProxyError(0, 'error message').args == (0, 'error message'))


# Generated at 2022-06-14 18:10:30.877643
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('wikipedia.org', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: wikipedia.org\r\n\r\n')
    header = s.recvall(4096)
    assert header.startswith(b'HTTP/1.')

# Generated at 2022-06-14 18:10:40.392890
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import random
    import string

    def _generate_data():
        data = bytearray()
        for i in range(0, random.randint(0, 500)):
            data.extend(random.sample(string.ascii_letters, 1))
        return data

    def _append_data(data, new_data):
        start = random.randint(0, len(data) - 1)
        data[start:len(data)] = new_data
        return data

    def _cut_data(data, length):
        start = random.randint(0, len(data) - 1)
        pos = start + length
        data[pos:len(data)] = ''
        return data


# Generated at 2022-06-14 18:10:52.144857
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    # Use localhost to avoid connection errors from firewall, router or ISP
    PROXY_TYPE = ProxyType.SOCKS4
    PROXY_ADDRESS = '127.0.0.1'
    PROXY_PORT = 1080
    PROXY_USERNAME = 'test'
    PROXY_PASSWORD = 'test'
    PROXY_REMOTE_DNS = True
    SOCKET_REMOTE_ADDR = 'www.google.com'
    SOCKET_REMOTE_PORT = 80

    test_sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    test_sock.setproxy(PROXY_TYPE, PROXY_ADDRESS, PROXY_PORT, PROXY_REMOTE_DNS, PROXY_USERNAME, PROXY_PASSWORD)
    test_

# Generated at 2022-06-14 18:11:05.468813
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    # Create a plain instance of class socket
    raw_socket = socket.socket()
    # .bind() and .listen() are needed because SOCK_STREAM sockets have to
    # first be bound, and then a backlog of connections is created with .listen()
    raw_socket.bind((socket.gethostname(), 0))
    raw_socket.listen()

    # Create a listening server socket
    server = raw_socket
    # Unpack the value returned by .getsockname() as (ip, port)
    host, port = server.getsockname()

    # Create a plain instance of class socket
    client = raw_socket
    # Connect the client to server.
    client.connect((host, port))

    # Test the method recvall with a user input of the length
    length = 6
    message = 'abcdef'


# Generated at 2022-06-14 18:11:15.156569
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    # Test cases for non-blocking sockets
    from .compat import compat_socket
    from .compat import compat_fileobject
    from .compat import compat_makefile
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    sock.connect(('localhost', 25))
    # We are not interested in the first message sent back by the server
    # so we should discard it.
    try:
        sock.recvall(1024)
    except EOFError:
        pass
    # Reset buffer
    sock = compat_makefile(sock, mode='rb', buffering=0)
    lines = []
    while True:
        line = sock.readline()
        if not line:
            break
        lines.append(line)
    sock.close

# Generated at 2022-06-14 18:11:23.475324
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    test_string = b'Test result'

    def _fake_recv(cnt):
        # Return all of the missing chars
        return test_string[len(sock._buffer):cnt]

    sock.recv = _fake_recv
    assert test_string == sock.recvall(len(test_string))
    try:
        sock.recvall(len(test_string)+10)
        assert False, 'Missing bytes did not raise an error'
    except EOFError:
        pass

if __name__ == '__main__':
    test_sockssocket_recvall()

# Generated at 2022-06-14 18:11:35.511860
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    from .compat import StringIO
    from .testtools import _FakeProxy
    from .testtools import _FakeSocket
    from .testtools import assertRaises

    with assertRaises(socket.error):
        sockssocket.setproxy('invalid', '1.2.3.4', 5678)

    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS5, '1.2.3.4', 5678, username='foo', password='bar')
    assert sock._proxy.type == ProxyType.SOCKS5
    assert sock._proxy.host == '1.2.3.4'
    assert sock._proxy.port == 5678
    assert sock._proxy.username == 'foo'
    assert sock._proxy.password == 'bar'
    assert sock._proxy.remote_dns

    sock._proxy

# Generated at 2022-06-14 18:11:43.813315
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    assert isinstance(sock, sockssocket)
    sock.setproxy(proxytype=ProxyType.SOCKS5, addr='127.0.0.1', port=1080, username='user', password='pass')
    assert isinstance(sock, sockssocket)
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080, username='user', password='pass')
    assert isinstance(sock, sockssocket)


# Generated at 2022-06-14 18:11:47.434873
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket()
    s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 10808, True, 'foo', 'bar')
    assert isinstance(s._proxy, Proxy)

# Generated at 2022-06-14 18:11:52.166064
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import os

    with open(os.devnull, 'rb') as devnull:
        sock = sockssocket()
        sock.setproxy(ProxyType.SOCKS4A, 'localhost', 1080)

        try:
            sock.connect((devnull.fileno(), 12345))
        except socket.error:
            pass

        try:
            sock.recvall(4)
        except EOFError as e:
            assert str(e) == '4 bytes missing'

        sock.close()

# Generated at 2022-06-14 18:12:07.815442
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    ss = sockssocket()
    ss.setproxy(ProxyType.SOCKS4, '127.0.0.1', 8080)
    ss.setproxy(ProxyType.SOCKS5, '127.0.0.1', 8080)
    ss.setproxy(ProxyType.SOCKS5, '127.0.0.1', 8080, username='user', password='passwd')
    ss.setproxy(ProxyType.SOCKS4, '127.0.0.1', 8080, username='user', password='passwd')
    ss.setproxy(ProxyType.SOCKS4A, '127.0.0.1', 8080, username='user', password='passwd')
    return

# Generated at 2022-06-14 18:12:14.430030
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    proxytype = ProxyType.SOCKS4A
    addr = "127.0.0.1"
    port = 1080
    username = "username"
    password = "password"
    s.setproxy(proxytype, addr, port, username=username, password=password)
    assert s._proxy == Proxy(proxytype, addr, port, username, password, remote_dns=True)
    s.close()


# Generated at 2022-06-14 18:12:17.982418
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    try:
        sockssocket.setproxy(sockssocket,1,123,123)
    except AttributeError:
        return False
    return True


# Generated at 2022-06-14 18:12:29.841813
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import time
    import unittest

    class TestSockssocketRecvall(unittest.TestCase):
        def test_recvall(self):
            s = sockssocket()
            s.bind(('localhost', 0))
            s.listen(1)
            cs = sockssocket()
            cs.connect(s.getsockname())
            cs.sendall(b'X' * 4)
            s, _ = s.accept()
            a = s.recvall(4)
            self.assertEqual(a, b'X' * 4)

        def test_recvall_timeout(self):
            s = sockssocket()
            s.bind(('localhost', 0))
            s.listen(1)
            cs = sockssocket()
            cs.settimeout(0.1)

# Generated at 2022-06-14 18:12:39.851543
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import sys
    import time
    import select
    import random
    import traceback
    s = sockssocket()
    s.settimeout(1)

# Generated at 2022-06-14 18:12:46.782500
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    socks_address = "127.0.0.1"
    socks_port = 1080
    proxy_type = ProxyType.SOCKS5
    sockss = sockssocket()
    sockss.setproxy(proxy_type, socks_address, socks_port)

    assert sockss._proxy.type == proxy_type
    assert sockss._proxy.host == socks_address
    assert sockss._proxy.port == socks_port

# Generated at 2022-06-14 18:12:58.022433
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from .compat import (
        compat_struct_pack,
        compat_str,
    )
    import socks  # noqa
    import socket as socket_module  # noqa

    def test_recvall(got_bytes, expected_bytes):
        if isinstance(expected_bytes, bytes):
            expected_bytes = expected_bytes.decode('utf-8')
        if isinstance(got_bytes, bytes):
            got_bytes = got_bytes.decode('utf-8')
        print('got: "{0}", expected: "{1}"'.format(got_bytes, expected_bytes))
        assert expected_bytes == got_bytes

    def test_socksproxy(proxytype):
        socks.set_default_proxy(proxytype, '127.0.0.1', 1080)
        sock = socks.socks

# Generated at 2022-06-14 18:13:05.862808
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import pytest

    test_data = [
        (lambda sock: sock.recv(1), b'Hello', EOFError),
        (lambda sock: sock.recvall(10), b'Hello', ValueError),
    ]

    for fn, data, result in test_data:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        sock.listen(5)
        sock.settimeout(1)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(sock.getsockname())
        conn.send(data)

        tconn, addr = sock.accept()

# Generated at 2022-06-14 18:13:16.468182
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from .compat import compat_socket

    hostname = b'timoschmid.de'
    query = b'GET / HTTP/1.0\r\nHost: ' + hostname + b'\r\n\r\n'
    server_address = (hostname, 80)
    family = compat_socket.AF_INET
    sock = sockssocket(family, compat_socket.SOCK_STREAM)
    try:
        sock.connect(server_address)
        sock.sendall(query)
        data = sock.recvall(64)
        assert data == b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n'
    finally:
        sock.close()

# Generated at 2022-06-14 18:13:28.351322
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import struct
    import sys
    from .compat import (
        compat_urllib_request,
    )
    IPV4_TEST_URL = 'http://google.com/generate_204'
    sock = sockssocket()
    s = compat_urllib_request.urlopen(IPV4_TEST_URL)
    f = s.fp
    buf = bytearray(b'a')
    while True:
        data = f.raw.read(1024)
        if not data:
            break
        buf += data
        if 1025 <= len(buf):
            break
    l = len(buf)
    l_hex = hex(l)
    sock.close()
    assert l == 1025, 'Unexpected l of {0}'.format(l)

# Generated at 2022-06-14 18:13:46.442116
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    proxy_list = [
        Proxy(ProxyType.SOCKS4, "127.0.0.1", 1080),
        Proxy(ProxyType.SOCKS4A, "127.0.0.1", 1080),
        Proxy(ProxyType.SOCKS5, "127.0.0.1", 1080),
    ]
    assert set(map(lambda x: x._proxy, proxy_list)) == set(proxy_list)


# Generated at 2022-06-14 18:13:57.766427
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import binascii
    from .compat import compat_unhexlify
    from .utils import run_test_server
    from .network import get_http_proxy_server_port
    from .network import get_proxy_server_port
    from .network import get_socks4_proxy_server_port
    from .network import get_socks5_proxy_server_port
    import socks

    server_ports = {
        'http': get_http_proxy_server_port(),
        'socks': get_proxy_server_port(),
        'socks4': get_socks4_proxy_server_port(),
        'socks5': get_socks5_proxy_server_port()
    }

    def tf_sockssocket_recvall(s):
        test_data = compat_unhexl

# Generated at 2022-06-14 18:14:05.129191
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    ss = sockssocket()
    ss.setblocking(True)
    ss.connect(('google.com', 80))
    ss.sendall(
        b'GET / HTTP/1.1\r\n'
        b'Host: google.com\r\n'
        b'Connection: close\r\n'
        b'\r\n')
    first_line = ss.recvall(16)
    assert first_line == b'HTTP/1.1 200 OK'

    ss.close()
    ss = sockssocket()
    ss.setblocking(False)
    ss.connect(('google.com', 80))

# Generated at 2022-06-14 18:14:13.347625
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    from .compat import compat_str
    sock = sockssocket()
    sock.connect(('127.0.0.1', 10000))

    # fake content length 3
    sock._buffering = (False, False, False, b'3')

    # fake recv response, 1 byte
    sock._rbuf = compat_str(b'\x01')

    # fake recv response, 2 byte
    sock._rbuf += compat_str(b'\x02')

    sock.recvall(3)



# Generated at 2022-06-14 18:14:18.665102
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import select
    
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 80))
    s.send('GET / HTTP/1.1\r\n\r\n'.encode('ascii'))
    
    # Wait until there is any data or the timeout expires
    inready, outready, errready = select.select([s], [], [], 1.0)
    if inready:
        sdata = s.recv(1024)
        print(sdata)
    else:
        print('... no response from the server')
        
    s.close()

# Generated at 2022-06-14 18:14:28.679542
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    socket.socket = sockssocket
    class Test():
        m_count = 0
        def recv(self, bytes):
            m_count = 0
            data = b''
            for x in range(bytes):
                data += bytes([x])
            m_count = bytes
            return data

    import pytest
    s_socks = Test()
    s_socks.recv = s_socks.recv
    result = s_socks.recvall(10)
    assert len(result) == 10
    with pytest.raises(EOFError):
        s_socks.recvall(100)


# Generated at 2022-06-14 18:14:31.552637
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS5, "socks.example.com", 1080, True, None, None)
    sock.connect(("example.com", 80))
    sock.sendall("GET / HTTP/1.0\r\n\r\n")
    data = sock.recv(1024)

# Generated at 2022-06-14 18:14:38.549947
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import socket
    sock = sockssocket()
    assert not hasattr(sock, 'recvall')
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
    sock.connect(('127.0.0.1', 80))
    assert hasattr(sock, 'recvall')


# Generated at 2022-06-14 18:14:44.985674
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    """
    >>> import socket
    >>> test_sockssocket_recvall.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> test_sockssocket_recvall.sock.connect(('192.168.1.1', 80))
    >>> test_sockssocket_recvall.sock.send(b'GET / HTTP/1.1\\r\\n\\r\\n')
    14
    >>> len(test_sockssocket_recvall.sock.recvall(1024)) == 1024
    True
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 18:14:52.673393
# Unit test for method setproxy of class sockssocket
def test_sockssocket_setproxy():
    import socks
    proxy_type = ProxyType.SOCKS5
    addr = '1.1.1.1'
    port = 1080
    rdns = True
    username = 'username'
    password = 'password'
    remote_dns = True
    sockssocket().setproxy(proxy_type, addr, port, rdns, username, password, remote_dns)
    assert sockssocket()._proxy == Proxy(proxy_type, addr, port, username, password, remote_dns)



# Generated at 2022-06-14 18:17:14.427888
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest
    import string
    from .test_compat import mock

    class TestSocksSocket(unittest.TestCase):
        def test_recvall_with_valid_size(self):
            sock = sockssocket()
            sock.recv = mock.Mock(side_effect=[string.ascii_lowercase, string.ascii_uppercase])
            result = sock.recvall(52)
            self.assertEqual(len(result), 52)
            self.assertEqual(result, string.ascii_lowercase + string.ascii_uppercase)

        def test_recvall_with_invalid_size(self):
            sock = sockssocket()
            sock.recv = mock.Mock(return_value=string.ascii_lowercase)


# Generated at 2022-06-14 18:17:24.392056
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    def test_method(test):
        test.test_name = 'recvall'
        bytes_to_receive = 2 ** 20
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 0))
        port = server.getsockname()[1]
        server.listen(1)

        client = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)
        client.connect(('127.0.0.1', port))
        server_socket, addr = server.accept()

# Generated at 2022-06-14 18:17:29.829334
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    total_len = 0
    for i in range(1, 30):
        assert len(sock.recvall(i)) == i
        total_len += i
    assert len(sock.recvall(total_len)) == total_len

# Generated at 2022-06-14 18:17:40.812742
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import unittest
    import mock

    class TestCase(unittest.TestCase):
        @mock.patch('socket.socket.sendall')
        @mock.patch('socket.socket.recv')
        def runTest(self, mock_recv, mock_sendall):
            mock_sendall.side_effect = [None, None, None, None, None]
            mock_recv.side_effect = ['abcde', 'fghij', 'klmno', '', 'xyz']
            socket.recv = mock_recv
            socket.sendall = mock_sendall
            self.assertEqual(sockssocket.recvall(5), 'abcde')
            self.assertEqual(sockssocket.recvall(5), 'fghij')

# Generated at 2022-06-14 18:17:44.093672
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import time
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 6667))
    sock.sendall(b'NICK testbot\r\n')
    time.sleep(1)
    try:
        data = sock.recvall(20)
        assert data == b'NICK testbot\r\n', data
    finally:
        sock.close()



# Generated at 2022-06-14 18:17:49.147045
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket()
    assert sock.recvall(0) == b''
    assert sock.recvall(1) == b'\x00'
    assert sock.recvall(2) == b'\x00\x00'
    assert sock.recvall(3) == b'\x00\x00\x00'
    assert sock.recvall(4) == b'\x00\x00\x00\x00'

# Generated at 2022-06-14 18:18:01.465261
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.listen(1)
    sock.settimeout(2)
    try:
        sock2 = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.settimeout(2)
        sock2.connect(('localhost', port))
        (conn, addr) = sock.accept()
        conn.sendall(b'*' * 1024)
        conn.close()
        d = sock2.recvall(1024)
        assert len(d) == 1024
    except Exception:
        sock.close()
        raise
    finally:
        sock2.close()

    sock.close()

#

# Generated at 2022-06-14 18:18:11.454469
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    import struct
    import unittest

    class Test(unittest.TestCase):
        def test_recvall_success(self):
            s = sockssocket()
            s.recv = lambda num: struct.pack('!I', num)
            self.assertEqual(s.recvall(4), struct.pack('!I', 4))

        def test_recvall_failure(self):
            from functools import partial
            s = sockssocket()
            s.recv = partial(lambda num: b'', 3)
            self.assertRaises(EOFError, s.recvall, 4)
    unittest.main()



# Generated at 2022-06-14 18:18:19.463666
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    def test_fun(target_socket, input_data, target_data_len, res_data):
        orig_recv = target_socket.recv
        incoming_data = iter(input_data)
        def new_recv(rlen):
            return next(incoming_data)

        setattr(target_socket, "recv", new_recv)
        result = target_socket.recvall(target_data_len)
        setattr(target_socket, "recv", orig_recv)
        return result == res_data

    # Let's fake a socket, and provide the data to test
    sock = socket.socket()
    test_result = test_fun(sock, [b'123', b'4567', b'89'], len(b'123456789'), b'123456789')

# Generated at 2022-06-14 18:18:24.375723
# Unit test for method recvall of class sockssocket
def test_sockssocket_recvall():
    test_sockssocket = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    test_sockssocket.connect(('127.0.0.1', 1))
    test_sockssocket.recvall(1)
    return True
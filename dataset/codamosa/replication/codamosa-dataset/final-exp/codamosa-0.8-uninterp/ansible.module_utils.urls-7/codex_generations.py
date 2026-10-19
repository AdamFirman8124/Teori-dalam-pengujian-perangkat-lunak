

# Generated at 2022-06-13 04:47:15.685014
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    '''
    Ensure we can call httplib.HTTPSConnection.__init__ with a UnixHTTPSConnection instance
    '''
    connection = UnixHTTPSConnection('/path/to/unix/socket')('host', port=8080)
    assert isinstance(connection, UnixHTTPSConnection)
    assert connection.host == 'host'
    assert connection.port == 8080

#
# Custom exceptions
#



# Generated at 2022-06-13 04:47:20.734752
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    url = urlparse('http://test.test')
    assert maybe_add_ssl_handler(url, False) is None
    assert maybe_add_ssl_handler(url, True) is None

    url = urlparse('https://test.test')
    assert maybe_add_ssl_handler(url, False) is None
    assert maybe_add_ssl_handler(url, True) is not None


# Generated at 2022-06-13 04:47:22.914045
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    time_string = rfc2822_date_string(datetime.datetime.utcnow().timetuple())
    assert re.match(r'^\w{3}, \d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} \-\d{4}$', time_string) is not None



# Generated at 2022-06-13 04:47:34.001233
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    """ Unit tests for function get_channel_binding_cert_hash. """
    if not HAS_CRYPTOGRAPHY:
        return

    with open(os.path.join(data_path, 'cert.pem'), 'r') as f:
        # Test that a full certificate works
        cert_1_sha256 = get_channel_binding_cert_hash(f.read().encode('utf-8'))

# Generated at 2022-06-13 04:47:37.742965
# Unit test for method open of class Request
def test_Request_open():
    url = "https://api.github.com/repos/ansible/ansible/releases/latest"
    request = Request(url, connect_timeout=10, force_basic_auth=True, url_username="ihaolin", url_password="ShenZhen2016")
    print(request.open().read())


# Generated at 2022-06-13 04:47:51.043022
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():         # pylint: disable=too-many-statements
    import sys
    if sys.version_info < (2, 7):
        raise SkipTest('Python 2.6 does not support these unit tests')
    import httpretty
    class MockHTTPConnection(httplib.HTTPConnection):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            httplib.HTTPConnection.__init__(self, 'example.com')

        def connect(self):
            self.sock = DummySocket()

    class DummySocket(object):
        def sendall(self, data):
            self.data = data

        def makefile(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return

# Generated at 2022-06-13 04:47:56.646859
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    import datetime
    given = datetime.datetime(2014, 6, 17, 1, 2, 3, tzinfo=datetime.timezone(datetime.timedelta(hours=3, minutes=30)))
    expected = 'Tue, 17 Jun 2014 01:02:03 +0330'
    assert rfc2822_date_string(given.timetuple(), '+0330') == expected



# Generated at 2022-06-13 04:48:09.861593
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    FakeSock = collections.namedtuple('FakeSock', ('server_hostname', ))

    # Happy path
    FakeSocket = collections.namedtuple('FakeSocket', ('wrap_socket', ))
    my_socket = FakeSocket(wrap_socket=lambda x, y: x)
    conn = CustomHTTPSConnection('example.com', port=443)
    conn.sock = FakeSock(server_hostname='example.com')
    conn.connect()
    assert conn.sock is my_socket

    # GCE only has the python ssl module (no openssl) and thus does not have server_hostname
    FakeSocket = collections.namedtuple('FakeSocket', ('wrap_socket', ))
    my_socket = FakeSocket(wrap_socket=lambda x, y: x)

# Generated at 2022-06-13 04:48:14.073172
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    handler = maybe_add_ssl_handler('http://www.google.com',False)
    assert handler is None
    handler = maybe_add_ssl_handler('https://www.google.com',False)
    assert handler is not None


# Generated at 2022-06-13 04:48:26.251180
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockHTTPSConnection(CustomHTTPSConnection):
        def __init__(_MockHTTPSConnection, *args, **kwargs):
            CustomHTTPSConnection.__init__(_MockHTTPSConnection, *args, **kwargs)
            _MockHTTPSConnection.call_count = {}
            _MockHTTPSConnection.call_count['__init__'] = _MockHTTPSConnection.call_count.get('__init__', 0) + 1
            _MockHTTPSConnection.context = _MockHTTPSConnection.cert_file = _MockHTTPSConnection.key_file = _MockHTTPSConnection.sock = _MockHTTPSConnection._tunnel_host = None

# Generated at 2022-06-13 04:50:55.012488
# Unit test for constructor of class Request
def test_Request():
    r = Request('http://fakeurl.com/')
    assert r.get_full_url() == 'http://fakeurl.com/'
    r = Request('https://fakeurl.com/')
    assert r.get_full_url() == 'https://fakeurl.com/'
    r = Request('ftp://fakeurl.com/')
    assert r.get_full_url() == 'ftp://fakeurl.com/'
    r = Request('http://fakeurl.com/path/')
    assert r.get_full_url() == 'http://fakeurl.com/path/'
    r = Request('http://fakeurl.com/path/', '/query/string/')
    assert r.get_full_url() == 'http://fakeurl.com/query/string/'

# Generated at 2022-06-13 04:51:00.645924
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    response = "HTTP/1.0 403 Forbidden\r\n"
    handler = SSLValidationHandler("hostname", "port")
    try:
        handler.validate_proxy_response(response)
    except Exception as e:
        assert e.__str__() == "Connection to proxy failed"



# Generated at 2022-06-13 04:51:12.178093
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''Unit test for function build_ssl_validation_error'''
    test_hostname = 'somehost'
    test_port = 80
    test_paths = ['path1', 'path2']
    test_exc = 'some exception'
    result = build_ssl_validation_error(test_hostname, test_port, test_paths, test_exc)
    assert isinstance(result, SSLValidationError)
    # parse out the message and validate it looks like what we'd expect

# Generated at 2022-06-13 04:51:16.407914
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    try:
        from urllib.parse import urlsplit
    except ImportError:
        from urlparse import urlsplit

    class Test_req:

        def get_full_url(self, url):
            return url

        def set_proxy(self, url):
            self.url = url

    url = "https://google.com"
    req = Test_req()
    handler = SSLValidationHandler(urlsplit(url)[1], 443)
    try:
        handler.http_request(req)
    except Exception:
        return False
    return True


# Generated at 2022-06-13 04:51:23.307554
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    import unittest, http.client
    def _context_wrap_socket(self):
        pass
    def _context_wrap_socket_called(self, *args):
        self.context_wrap_socket_called = True
    class TestCustomHTTPSConnection(unittest.TestCase):
        @staticmethod
        def _make_connection_class():
            class MockConnection(CustomHTTPSConnection):
                def __init__(self, *args, **kwargs):
                    sock = mock.Mock()
                    sock.create_connection = mock.Mock(return_value=sock)
                    sock.family = 8
                    sock.type = 1
                    sock.proto = 0
                    sock.fileno = lambda: 42
                    sock.getpeername = lambda: ('foo', 'bar')
                    self.sock = sock
                   
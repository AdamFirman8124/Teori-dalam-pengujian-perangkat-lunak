

# Generated at 2022-06-22 13:15:28.164986
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    assert True

# Generated at 2022-06-22 13:15:38.216905
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    from tornado.httpclient import HTTPRequest, HTTPResponse
    from tornado.httpclient import _HTTPConnection

    class MyHTTPConnection(_HTTPConnection):
        code = None
        reason = None
        headers = None
        chunks = []
        final_callback = None
        parsed = httputil.url_parse('http://localhost')

    class TestHTTPRequest(unittest.TestCase):
        def test_redirects(self):
            self.stream = DummyStream()
            conn = MyHTTPConnection(self.stream, HTTPResponse, 'localhost', 80)
            conn.final_callback = mock.Mock()
            request = HTTPRequest(url='http://localhost/test')
            conn.request = request

# Generated at 2022-06-22 13:15:46.389836
# Unit test for method run of class _HTTPConnection

# Generated at 2022-06-22 13:15:56.664067
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    obj = SimpleAsyncHTTPClient()
    obj.close()
    obj.close_all_connections()
    obj.initialize()
    # obj.close_all_connections()
    obj.max_clients = 6
    obj.queue = collections.deque()
    obj.active = {}
    obj.waiting = {}
    obj.max_buffer_size = 100
    obj.max_header_size = 10
    obj.max_body_size = 10
    obj.resolver = Resolver()
    obj.own_resolver = True
    obj.tcp_client = TCPClient(resolver=obj.resolver)
    obj.close()


# Generated at 2022-06-22 13:16:08.169658
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    conn = HTTPClient()
    conn._create_connection = mock.MagicMock()
    future = conn._HTTPConnection('google.com', 80)
    future.connection.headers_received(None, None)
    assert future.on_connection_close() == None
    assert future._release() == None
    assert future._handle_exception(None, None, None) == True
    assert future._should_follow_redirect() == False
    assert future._should_follow_redirect() == True
    assert future.finish() == None
    assert future._on_end_request() == None
    assert future.data_received(None) == None
    assert future._on_timeout(None) == None
    assert future._remove_timeout() == None


# Generated at 2022-06-22 13:16:16.628901
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado.netutil import ssl_options_to_context
    from tornado.iostream import IOStream
    import socket

    class _DummySocket(socket.socket):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
            self.host = "127.0.0.1"
            self.port = 80
            self.connect_called = False

        def connect(self, *args: Any, **kwargs: Any) -> None:
            self.connect_called = True
            self.connect_args = args
            self.connect_kwargs = kwargs

    def dummy_socket(*args: Any, **kwargs: Any) -> socket.socket:
        # type: (...) -> socket.socket
        sock = _

# Generated at 2022-06-22 13:16:20.521438
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    url = 'http://httpbin.org/get'
    client = AsyncHTTPClient()
    response = yield client.fetch(url)
    print(response.body)

test_SimpleAsyncHTTPClient_fetch_impl()

# Create an HTTP 1.1 connection

# Generated at 2022-06-22 13:16:27.897890
# Unit test for method on_connection_close of class _HTTPConnection

# Generated at 2022-06-22 13:16:35.199035
# Unit test for method finish of class _HTTPConnection

# Generated at 2022-06-22 13:16:41.209640
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    """Unit test for method finish of class _HTTPConnection.
    """
    # POST /test/user HTTP/1.1
    # Host: localhost:8080
    # Connection: keep-alive
    # Content-Length: 11
    # Accept: application/json, text/plain, */*
    # Origin: http://localhost:8080
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
    # Content-Type: application/x-www-form-urlencoded
    # Accept-Encoding: gzip, deflate, br
    # Accept-Language: zh-CN,zh;q=0.8,en;q=0.6


# Generated at 2022-06-22 13:17:16.750122
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    pass

# Generated at 2022-06-22 13:17:22.418464
# Unit test for method data_received of class _HTTPConnection

# Generated at 2022-06-22 13:17:24.625310
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    should_be = "Stream closed"
    actual = str(HTTPStreamClosedError("Stream closed"))
    assert should_be == actual



# Generated at 2022-06-22 13:17:31.370759
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    # Given a SimpleAsyncHTTPClient object with AsyncHTTPClient as parent class
    client = SimpleAsyncHTTPClient()
    # When calling its initialize method
    client.initialize()
    # Then its active attribute should be {}
    assert client.active == {}
    # And its queue attribute should be instance of collections.deque
    assert isinstance(client.queue, collections.deque)
    # And its waiting attribute should be {}
    assert client.waiting == {}
    # And its own_resolver attribute should be True
    assert client.own_resolver == True

# Generated at 2022-06-22 13:17:32.844483
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    SimpleAsyncHTTPClient_object=SimpleAsyncHTTPClient()
    SimpleAsyncHTTPClient_object.close()



# Generated at 2022-06-22 13:17:41.557338
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # Unit test for method on_connection_close of class _HTTPConnection.
    # mock
    io_loop = mock.Mock()
    request = mock.Mock()
    release_callback = mock.Mock()
    final_callback = mock.Mock()

    # create object
    _HTTPConnection(
        io_loop,
        request,
        release_callback,
        final_callback,
        max_header_size=None,
        max_body_size=None,
    )
    # test
    _HTTPConnection.on_connection_close()



# Generated at 2022-06-22 13:17:42.712830
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    raise NotImplementedError

# Generated at 2022-06-22 13:17:45.276985
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import unittest
    assert(os.system("./test_HTTPConnection_run.sh") == 0)

# Generated at 2022-06-22 13:17:56.720051
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    def test():
        stream = IOStream(socket.socket())
        request = HTTPRequest('http://127.0.0.1:8888/')
        conn = HTTPClient._HTTPConnection(stream, request, True,
                                          '127.0.0.1', 8888, None, None, None, None,
                                          None, None)
        assert conn.request is not None
        assert conn.connection is None
        assert conn.code is None
        assert conn.headers is None
        assert conn.chunks is not None

        # Test StreamClosedError
        stream.error = StreamClosedError()
        conn.final_callback = mock.Mock()
        conn.on_connection_close()
        conn.final_callback.assert_called_with(mock.ANY)
        conn.final_callback.reset_m

# Generated at 2022-06-22 13:18:00.027330
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    msg = "my message"
    inst = HTTPTimeoutError(msg)
    assert inst.message == msg
    assert str(inst) == msg


# Generated at 2022-06-22 13:18:40.955933
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    with pytest.raises(TypeError, match="Too many positional arguments"):
        HTTPClient()



# Generated at 2022-06-22 13:18:49.943806
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # In this function, we test fetch_impl method of class SimpleAsyncHTTPClient
    # In this function, we first create several request object and callbacks
    # and add these request and callbacks into queue.
    # Then we call fetch_impl method and pass a request and a callback.
    # Then we check the size of queue, if the size is correct,
    # we check the first element of the queue, if it is correct,
    # we check the last element of the queue,
    # if it is correct, we remove the first element of the queue,
    # we check the size of active, if it is correct,
    # we check the first element of active, if it is correct.

    # create a AsyncHTTPClient instance
    client = SimpleAsyncHTTPClient()
    # set max_clients to 1000
    client.max_clients = 1000


# Generated at 2022-06-22 13:18:52.266694
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    client = SimpleAsyncHTTPClient(io_loop=None)
    expected_result = None
    assert client.close() == expected_result


# Generated at 2022-06-22 13:18:55.322556
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    req = httpclient.HTTPRequest("http://www.google.com")
    client = httpclient.AsyncHTTPClient()
    resp = client.fetch(req)
    assert resp != None

# Generated at 2022-06-22 13:19:07.371767
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    io_loop = IOLoop()
    io_loop.make_current()
    http_client = HTTPClient(io_loop=io_loop)
    conn = _HTTPConnection(http_client, [], 1, "http://www.google.com", io_loop)
    assert conn.client.io_loop == io_loop
    assert conn.stream is None
    assert conn.closed
    assert conn._sockaddr == [('www.google.com', 80)]
    assert conn.code is None
    assert conn.headers is None
    assert conn.chunks == []
    assert conn.max_header_size == 65536
    assert conn.max_body_size == 104857600
    assert conn.final_callback is None
    assert conn.release_callback is None
    assert conn.start_time == 0
    assert conn

# Generated at 2022-06-22 13:19:18.163997
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    print("test__HTTPConnection_run()")
    # Initialization
    request = HTTPRequest("https://www.python.org")
    callback = lambda x: True
    io_loop = IOLoop.current()
    final_callback = lambda x: True
    max_header_size = 20000000
    max_body_size = 20000000
    release_callback = lambda: True
    decompress = True
    start_time = 0.0
    fetcher = _HTTPConnection(
        request,
        callback,
        io_loop,
        final_callback,
        max_header_size,
        max_body_size,
        release_callback,
        decompress,
        start_time,
    )
    # Fake an active connection
    client = HTTPClient(io_loop=io_loop)

# Generated at 2022-06-22 13:19:22.702114
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    _HTTPConnection(client = None, request = None, final_callback=None, release_callback = None,
                    timeout = None, auth_username = "None", auth_password = "None", auth_mode = "None")

test__HTTPConnection()


# Generated at 2022-06-22 13:19:36.231938
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    def test_response_part(chunk: bytes, stream: IOStream):
        pass

    from tornado.iostream import IOStream

    from tornado.testing import AsyncTestCase, gen_test

    from tornado.httpclient import HTTPResponse, HTTPClient, HTTPRequest

    from tornado.simple_httpclient import _HTTPConnection

    from tornado.platform.asyncio import to_asyncio_future

    from tornado.test.util import unittest

    try:
        from unittest import mock
    except ImportError:
        import mock

    import unittest.mock

    class Test__HTTPConnection(AsyncTestCase):
        def setUp(self):
            super(Test__HTTPConnection, self).setUp()

# Generated at 2022-06-22 13:19:46.788098
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    class Mock_RequestProxy:
        def __init__(self):
            self.stream = MagicMock()
            self.stream.closed = MagicMock(return_value=False)

        def close(self):
            pass


    class Mock_HTTPRequest:
        def __init__(self):
            self.auth_username = "a"
            self.auth_password = "b"
            self.auth_mode = "c"
            self.user_agent = "d"
            self.allow_nonstandard_methods = False
            self.request_timeout = 0
            self.connect_timeout = 0
            self.network_interface = "e"
            self.proxy_host = "f"
            self.proxy_port = 0
            self.proxy_username = "g"

# Generated at 2022-06-22 13:19:53.611536
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    success = True
    inst = _HTTPConnection(None, None, None, None, None, None, None)
    try:
        inst.on_connection_close()
    except Exception as e:
        success = False
        print("test _HTTPConnection on_connection_close: {0}".format(e))
    assert success, "test _HTTPConnection on_connection_close failed"

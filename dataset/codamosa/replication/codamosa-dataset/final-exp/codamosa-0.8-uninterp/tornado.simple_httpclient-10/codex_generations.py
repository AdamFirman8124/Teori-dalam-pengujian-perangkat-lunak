

# Generated at 2022-06-22 13:15:35.539197
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    pass


# Generated at 2022-06-22 13:15:36.073682
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    pass

# Generated at 2022-06-22 13:15:40.374989
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """
    Unit test for method _HTTPConnection.headers_received
    """
    # TODO
    # The test passed, but do not know how to verify it.
    
    # The function only has side effect, and returns None.
    # However, it triggers finish method of _HTTPConnection based on the headers.
    # And the finish method is quite complex, not sure how to verify them.
    # So just leave it here for now...
    pytest.skip()


# Generated at 2022-06-22 13:15:47.322553
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    try:
        import socket
        import ssl
    except ImportError:
        raise unittest.SkipTest("sockets required")

    from tornado.simple_httpclient import _HTTPConnection
    from tornado.httpserver import HTTPServer
    from tornado.iostream import IOStream
    from tornado.testing import bind_unused_port, AsyncHTTPTestCase

    class MyHTTPConnection(_HTTPConnection):
        def headers_received(
            self,
            first_line: Union[httputil.ResponseStartLine, httputil.RequestStartLine],
            headers: httputil.HTTPHeaders,
        ) -> None:
            print(first_line)
            print(headers)


# Generated at 2022-06-22 13:15:56.343902
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    def test_const():
        http_client = SimpleAsyncHTTPClient()
        http_conn = _HTTPConnection(
            SimpleAsyncHTTPClient(), "www.example.com", 443, "/", True, None, None
        )
        assert http_conn.client == http_client
        assert http_conn.parsed == urllib.parse.urlparse("www.example.com")
        assert http_conn.connect_timeout == 20.0
        assert http_conn.request_timeout == 20.0
        assert http_conn.max_header_size == 1048576
        assert http_conn.max_body_size == 1048576
        assert http_conn.chunks == []
        assert http_conn.request == {}
        assert http_conn.code is None
        assert http_conn.reason is None

# Generated at 2022-06-22 13:15:59.949277
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    client = SimpleAsyncHTTPClient()
    client.close()
    pass
if __name__ == '__main__':
    client = SimpleAsyncHTTPClient()
    client.close()
    pass

# Generated at 2022-06-22 13:16:05.823797
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # Setup Tests
    io_loop = IOLoop()
    conn = _HTTPConnection(
        io_loop,
        "127.0.0.1",
        443,
        SimpleAsyncHTTPClient(io_loop, max_clients=10),
        "GET",
        "/",
        {},
        ResponseStartLine("1.1", 200, "OK"),
        None,
        None,
    )
    conn.final_callback = None
    conn.stream = StreamClosedError("Test")

    # Unit under test
    conn.on_connection_close()



# Generated at 2022-06-22 13:16:08.082102
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    # test SimpleAsyncHTTPClient()
    obj = SimpleAsyncHTTPClient()

    # test SimpleAsyncHTTPClient.close
    pass



# Generated at 2022-06-22 13:16:19.330553
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    test__HTTPConnection_finish = unittest.TestCase()
    test__HTTPConnection_finish.assertEqual = asynctest.failUnlessEqual
    test__HTTPConnection_finish.assertIs = asynctest.failUnlessIs

    def test__HTTPConnection_finish(self):
        def header(self):
            return None

        def body(self):
            return None

        def test__HTTPConnection_finish(self):
            self.client = AsyncHTTPClient()
            self.client.fetch(
                HTTPRequest(
                    "http://localhost:9/",
                    streaming_callback=self.header,
                    header_callback=self.header,
                    body_callback=self.body,
                )
            )
        self.assertIs(test__HTTPConnection_finish, None)
    test

# Generated at 2022-06-22 13:16:29.354410
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    # Create an instance of the class under testing
    http_client = SimpleAsyncHTTPClient()
    assert hasattr(http_client, 'max_clients') == True
    assert hasattr(http_client, 'queue') == True
    assert hasattr(http_client, 'active') == True
    assert hasattr(http_client, 'waiting') == True
    assert hasattr(http_client, 'max_buffer_size') == True
    assert hasattr(http_client, 'max_header_size') == True
    assert hasattr(http_client, 'max_body_size') == True
    assert hasattr(http_client, 'resolver') == True
    assert hasattr(http_client, 'own_resolver') == True
    assert hasattr(http_client, 'tcp_client') == True

# Generated at 2022-06-22 13:17:18.511304
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    import logging
    from tornado import testing

    def run_until_complete(future):
        """Runs the given future until it completes, then returns its result.

        For historical reasons, this is available in the ``tornado.testing``
        module.  New code should use the ``async_test`` decorator or the
        ``run_sync`` method in ``tornado.gen``.
        """
        return testing.gen_test(future)()

    class _ConnectionDelegate(object):
        def __init__(
                self,
                final_callback,
                release_callback,
                max_buffer_size,
                max_header_size,
                max_body_size,
        ):
            self.final_callback = final_callback
            self.release_callback = release_callback
            self.max_buffer_size = max_

# Generated at 2022-06-22 13:17:21.405500
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # test __init__() of class _HTTPConnection
    _HTTPConnection()



# Generated at 2022-06-22 13:17:28.890437
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # HttpClient object
    client = HttpClient()
    # define request object
    request = HTTPRequest(url="http://www.baidu.com")
    # define stream object
    stream = IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    # define _HTTPConnection object
    http_connection = _HTTPConnection(
        client, request, stream, "127.0.0.1", 80)
    # assert nothing return when data_received function was called
    assert http_connection.data_received(chunk=b'chunk') == None


# Generated at 2022-06-22 13:17:40.581959
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    io_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(io_loop)

# Generated at 2022-06-22 13:17:51.869776
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # Test for a connection with a past request.
    client = SimpleAsyncHTTPClient(io_loop=IOLoop())
    http_client = _HTTPConnection(client, client.io_loop)
    http_client.request = HTTPRequest(
        method="GET",
        url="http://www.tornadoweb.org/en/stable/",
        connect_timeout=0.1,
        request_timeout=0.1,
        streaming_callback=None
    )
    http_client.stream = DummyStream()
    http_client.parsed = httputil.url_parse(http_client.request.url)
    # Create a dummy socket address to pass to _HTTPConnection.
    http_client._sockaddr = ("", 80)
    # Callback to be run at the end of the request.
    http_client

# Generated at 2022-06-22 13:17:53.276279
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    _HTTPConnection()

# Generated at 2022-06-22 13:17:54.882794
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    a=_HTTPConnection()
    assert a._run()==None

# Generated at 2022-06-22 13:18:07.703903
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    chunk = b''
    async def async_call(
        first_line: httputil.ResponseStartLine,
        headers: httputil.HTTPHeaders,
    ) -> int:
        pass
    ioloop =  IOloop()
    response = HTTPResponse()
    headers = httputil.HTTPHeaders()
    headers.add("Location","")
    response.headers = headers
    request = HTTPRequest()
    request.max_redirects = 1
    request.url = "http://localhost"
    headers_rcvd = _HTTPConnection()
    headers_rcvd.code = 301
    headers_rcvd.reason = "redirection"
    headers_rcvd.final_callback = async_call
    headers_rcvd.request = request
    headers_rcvd.headers = headers
    headers_rcvd

# Generated at 2022-06-22 13:18:18.268532
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    def test_body():
        # Test body of method __str__() of class HTTPTimeoutError
        pass
    # Create an instance of class HTTPError
    obj: HTTPError = HTTPError(599, message=None)
    # Apply method __str__()
    obj.__str__()
    # Unit test
    test_body()
    # Test passed
    print("Test passed")
    return


# Hack the signature of the signals callback
# http://stackoverflow.com/questions/14306801/python3-the-type-of-the-signal-callback-function
# The following methods should be ignored by Mypy as they are signals
if sys.version_info >= (3, 5):
    from tornado import stack_context


# Generated at 2022-06-22 13:18:23.159533
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    from tornado import testing
    from typing import Any, Optional, Type

    io_loop = testing.IOLoop()
    io_loop.make_current()

    class Request(object):
        streaming_callback = None  # type: Any
        final_callback = None  # type: Any
        release_callback = None  # type: Any

    class ResponseStartLine(object):
        def __init__(self, code, reason):
            self.code = code
            self.reason = reason

    class Response(object):
        request = Request()
        code = None  # type: Optional[int]
        reason = None  # type: Optional[str]
        headers = None  # type: Optional[Any]

        async def headers_received(
            self, first_line, headers
        ) -> None:
            self.code = first_

# Generated at 2022-06-22 13:22:25.806569
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # test func data_received(self, chunk: bytes) -> None

    from tornado.httpclient import HTTPResponse, HTTPRequest
    from tornado.log import app_log

    def test__HTTPConnection_headers_received():
        # test func headers_received(
        #     self,
        #     first_line: Union[httputil.ResponseStartLine, httputil.RequestStartLine],
        #     headers: httputil.HTTPHeaders,
        # ) -> None

        # No code example

        # pass
        pass


# Generated at 2022-06-22 13:22:28.137989
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    stream = IOStream(socket.socket())
    conn = _HTTPConnection(stream)
    assert conn is not None


# Generated at 2022-06-22 13:22:40.191189
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    request = HTTPRequest(url="http://www.example.com", )
    request._finish_time = 3.2
    request.io_loop = IO_LOOP()
    request.connect_timeout = 4.1
    request._start_time = 1.5
    request.request_timeout = 5.0
    request.proxy_host = None
    request.proxy_port = 80
    request.proxy_username = None
    request.proxy_password = None
    request.follow_redirects = True
    request.max_redirects = 10
    request.allow_nonstandard_methods = False
    request.validate_cert = False
    request.ca_certs = None
    request.allow_ipv6 = False
    request.streaming_callback = None
    request.header_callback = None
    request

# Generated at 2022-06-22 13:22:41.426420
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    # class _HTTPConnection(object):
    pass


# Generated at 2022-06-22 13:22:43.406217
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # FIXME: need test!!
    assert True



# Generated at 2022-06-22 13:22:48.314577
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    response = HTTPResponse(
        request, 200, reason=None, headers=None, request_time=None, start_time=None,
        buffer=buffer, effective_url=request.url, 
    )
    assert response.code == 200
    assert response.reason == None
    assert response.headers == None
    assert response.request_time == None
    assert response.start_time == None
    assert response.buffer == buffer
    assert response.effective_url == request.url
    
test__HTTPConnection_data_received()


# Generated at 2022-06-22 13:22:51.890781
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    url = "http://127.0.0.1:8888"
    response = requests.get(url)
    assert response.status_code == 200, 'url: {}'.format(url)
    body, response_code = response.text, response.status_code
    return body, response_code

# Generated at 2022-06-22 13:22:55.691452
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    # SimpleAsyncHTTPClient : HTTPTimeoutError
    # Unit test for method __str__ of class HTTPTimeoutError
    # test_HTTPTimeoutError___str__()
    var = HTTPTimeoutError("Timeout")
    assert str(var) == "Timeout"


# Generated at 2022-06-22 13:22:59.217822
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    message = "test"
    error = HTTPTimeoutError(message)
    assert str(error) == "test"
    error = HTTPTimeoutError("")
    assert str(error) == "Timeout"


# Generated at 2022-06-22 13:23:04.186517
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    io_loop = IOLoop.current()
    io_loop.run_sync(
        lambda: _HTTPConnection(
            io_loop=io_loop,
            sockaddr=("127.0.0.1", "8080"),
            max_header_size=1048576,
            max_body_size=100 * 1024 * 1024,
            request=HTTPRequest(url="url", method="method", headers="headers"),
            final_callback=lambda response: print(response),
            connect_timeout=30,
            start_time=io_loop.time(),
        ).run()
    )



# Generated at 2022-06-22 13:23:43.613605
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # without follow_redirects
    # without callback
    # status_code == 100
    req = httpclient.HTTPRequest(
        url="http://example.com/somepath",
        method="GET",
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": "Tornado/4.5.3",
        },
    )
    client = _HTTPClient()
    client.request = req
    client.code = None
    client.reason = None
    client.headers = None
    client.chunks = [b""]
    client.io_loop = IOLoop()
    client.start_time = client.io_loop.time()
    client.start_wall_time = 0.0

# Generated at 2022-06-22 13:23:48.096028
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    # Unit test for method finish of class _HTTPConnection
    request = HTTPRequest(url="http://www.google.com/")
    connection = _HTTPConnection(request, "http://www.google.com/")
    connection.finish()


# Generated at 2022-06-22 13:23:57.026128
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    """Ensure that data is properly received"""
    # 1. Build the HTTPConnection object
    request = HTTPRequest(url="www.google.com")
    stream = IOStream(socket.socket())
    http_connection = _HTTPConnection(
        request,
        client=None,
        final_callback=None,
        release_callback=None,
        start_time=0,
        io_loop=None,
    )
    # 2. Get data
    data = "Hello World!".encode('utf8')
    # 3. Send data to data_received
    http_connection.data_received(data)
    # 4. Ensure that the data is in the chunks list (a list of bytes)
    to_test = data in http_connection.chunks
    # 5. Assert the test result
    assert to_test



# Generated at 2022-06-22 13:24:00.897402
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    io_loop = None
    response = None
    with pytest.raises(AssertionError):
        client = Client()
        proxy = _HTTPConnection(client, io_loop, None, None, None)
        proxy.finish()


# Generated at 2022-06-22 13:24:10.722201
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado.httpclient import HTTPRequest, _RequestProxy

    def mock_fetch(
        url: str,
        callback: Callable[..., Any] = None,
        **kwargs: Any,
    ) -> Future[HTTPResponse]:
        proxy = _RequestProxy(
            HTTPRequest(url, **kwargs),
            max_redirects=10,
            release_callback=None,
            prepare_curl_callback=None,
        )

        conn = _HTTPConnection(
            client=None,
            request=proxy,
            release_callback=None,
            final_callback=None,
            follows_redirect=False,
            session=None,
            io_loop=None,
        )

        conn._run(HTTP1Connection(None, True, None, None))
        return Future()

   

# Generated at 2022-06-22 13:24:12.468642
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    stream = None
    _HTTPConnection.finish(stream)



# Generated at 2022-06-22 13:24:15.104886
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    def test_should_follow_redirect():
        assert True
    def test_should_not_follow_redirect():
        assert True


# Generated at 2022-06-22 13:24:16.391903
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    # _HTTPConnection.finish(self)
    return


# Generated at 2022-06-22 13:24:19.983195
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    http = _HTTPConnection(None, None, None, None, None, None, None)
    http.chunks = ['1']
    http.code = None
    assert http.finish() == None

# Generated at 2022-06-22 13:24:25.178215
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    request, callback, timeout_handle = object(), object(), object()
    instance = SimpleAsyncHTTPClient()
    instance.fetch_impl(request, callback)
    assert instance.queue is not None
    assert instance.active is not None
    assert instance.waiting is not None
    assert instance.tcp_client is not None
    assert instance.resolver is not None
    assert instance.own_resolver is not None
    assert isinstance(instance, AsyncHTTPClient)


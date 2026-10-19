

# Generated at 2022-06-22 13:15:49.568206
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    message = "message"
    http_stream_closed_error = HTTPStreamClosedError(message)
    assert message == http_stream_closed_error.message
    assert message == http_stream_closed_error.__str__()


# Generated at 2022-06-22 13:15:52.393904
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    _HTTPConnection._should_follow_redirect()
    _HTTPConnection._on_end_request()
    _HTTPConnection.finish()

# Generated at 2022-06-22 13:16:05.510419
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # verify that the chunked encoding works correctly
    # for non-ascii characters
    # Python 2.6's http server can serve 'latin-1' encoded texts
    # with chunked encoding, but Python 2.5 cannot.
    # See also http://bugs.python.org/issue6580
    text = u"\xe4\xf6\xfc".encode("latin-1")
    handler = ChunkHandler(text)
    server = HTTPServer(handler)
    server.listen(io_loop=IOLoop())
    client = AsyncHTTPClient(io_loop=IOLoop())

# Generated at 2022-06-22 13:16:14.863959
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    first_line_str = "GET /fake HTTP/1.1\r\n"
    first_line = httputil.parse_response_start_line(native_str(first_line_str))
    headers_str = "Content-Length: 40\r\n"
    headers = httputil.HTTPHeaders.parse(headers_str)
    data = b'{"info": {"name": "Tornado", "language": "Python"},\n'
    hc = _HTTPConnection(None, None, None, None, None, None, None)
    hc.headers_received(first_line, headers)
    hc.data_received(data)
    hc.finish()

# Generated at 2022-06-22 13:16:25.001119
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    from tornado import testing


    class TestHTTPConnection(testing.AsyncHTTPTestCase):
        async def get_app(self):
            return Application()

        async def test_headers_received(self):
            await self.http_client.fetch(
                self.get_url("/"),
                method="POST",
                body="foo=bar&baz=quux",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )


    response = TestHTTPConnection().get_response()
    assert response.code == 200
    assert response.headers["Content-Length"] == "7"
    assert b"Cookie" not in response.body

# Generated at 2022-06-22 13:16:25.651499
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    _HTTPConnection

# Generated at 2022-06-22 13:16:37.749441
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    client = SimpleAsyncHTTPClient()
    client.max_clients = 10
    client.queue = collections.deque()
    client.active = {}
    client.waiting = {}
    client.max_buffer_size = max_buffer_size = 104857600
    client.max_header_size = max_header_size = None
    client.max_body_size = max_body_size = None
    assert client.max_clients == 10
    assert client.queue == collections.deque()
    assert client.active == {}
    assert client.waiting == {}
    assert client.max_buffer_size == max_buffer_size
    assert client.max_header_size == max_header_size
    assert client.max_body_size == max_body_size

# Generated at 2022-06-22 13:16:38.292193
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    pass

# Generated at 2022-06-22 13:16:38.949385
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    pass

# Generated at 2022-06-22 13:16:44.869861
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # (self: _HTTPConnection, first_line, headers) -> None
    args = _HTTPConnection.headers_received.__getargspec__.args
    base = ["first_line", "headers"]
    if args[-1] == "**kwargs":
        args = args[:-1]
    # if type(args[-1]) is str and args[-1].startswith("**"):
    #   args[-1] = "**" + args[-1]
    # print(args, base)
    # assert args == base


if __name__ == "__main__":
    test__HTTPConnection_headers_received()

# Generated at 2022-06-22 13:18:28.554362
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
   AsyncHTTPClient = SimpleAsyncHTTPClient
   client = AsyncHTTPClient()
   client.close()



# Generated at 2022-06-22 13:18:32.682285
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # Test that is called inside `_HTTPConnection.headers_received` when
    # `self.request.expect_100_continue` is true and the code is 100.
    # The method `self._write_body` should be called.
    pass


# Generated at 2022-06-22 13:18:44.586411
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    global _Resolver_instance_count
    _Resolver_instance_count = 0
    global _Resolver_instance__resolve_count
    _Resolver_instance__resolve_count = 0
    global _Resolver_instance__resolve_hostname_count
    _Resolver_instance__resolve_hostname_count = 0
    global _Resolver_instance__resolve_future_count
    _Resolver_instance__resolve_future_count = 0
    global _Resolver_instance__cancel_count
    _Resolver_instance__cancel_count = 0
    global _IOLoop_instance_count
    _IOLoop_instance_count = 0
    global _IOLoop_instance_current_count
    _IOLoop_instance_current_count = 0
    global _IOLoop_instance_make

# Generated at 2022-06-22 13:18:55.377546
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    import io
    import pytest
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.iostream import IOStream
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.testing import bind_unused_port
    from tornado.testing import ExpectLog
    from tornado.testing import LogTrapTestCase
    from tornado.testing import main
    from tornado.testing import bind_unused_port, AsyncHTTPTestCase
    from tornado.testing import gen_test, ExpectLog, LogTrapTestCase
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.iostream import IOStream
    from tornado.netutil import _client_ssl_defaults # type: ignore
    from tornado.simple_httpclient import _HTTPConnection

# Generated at 2022-06-22 13:19:00.619515
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # Make an empty callback for the test
    def empty_callback():
        pass
    # Make an empty _HTTPConnection object and call its method run
    http_connection = _HTTPConnection( None, None, "", empty_callback, empty_callback, None, None, None )
    result = http_connection.run( None )

    print( result )

# Generated at 2022-06-22 13:19:05.955876
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    try:
        raise HTTPStreamClosedError('Test')
    except HTTPStreamClosedError as e:
        assert str(e)=='Test'
    try:
        raise HTTPStreamClosedError('')
    except HTTPStreamClosedError as e:
        assert str(e)=='Stream closed'



# Generated at 2022-06-22 13:19:09.218820
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    with pytest.raises(NotImplementedError):
        _HTTPConnection("a", "b", "c", "d").finish('a')


# Generated at 2022-06-22 13:19:19.452327
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    http1conn = HTTP1Connection(
        IOStream(),
        True,
        HTTP1ConnectionParameters(
            no_keep_alive=True,
            max_header_size=65536,
            max_body_size=65536,
            decompress=True
        ),
        ""
    )
    client = HTTPClient()
    request = HTTPRequest(
        url="http://www.tornadoweb.org/en/stable/"
    )
    callback = None
    io_loop = IOLoop.current()
    release_callback = None
    final_callback = print
    httpconn = _HTTPConnection(
        client,
        request,
        callback,
        io_loop=io_loop,
        release_callback=release_callback,
        final_callback=final_callback
    )

# Generated at 2022-06-22 13:19:32.504245
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    async def _HTTPConnection_run():
        utils.reset_timeout_counter()
        reset_timeout_counter()
        with patch("httputil.HTTPResponse._on_chunk_received"), patch(
            "httpclient._HTTPConnection.on_connection_close"
        ), patch("httpclient._HTTPConnection.headers_received"), patch(
            "httpclient._HTTPConnection.data_received"
        ), patch("httpclient._HTTPConnection.finish"):
            connection = _HTTPConnection(
                Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock()
            )
            connection.finish = Mock()
            await connection.run()
            connection.finish.assert_called_once()
            utils.reset_timeout_counter()
            reset_timeout_counter()

# Generated at 2022-06-22 13:19:44.353987
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import datetime
    # What about the other 2?
    # _HTTPConnection('str', 'str', 'str', 'str', 'str', 'str', 'str')
    # _HTTPConnection('str', 'str', 'str', 'str', 'str', 'str', 'str')
    async def async_f():
        return 1
    a = _HTTPConnection('str', 'str', 'str', 'str', 'str', 'str', 'str')
    a.async_f = async_f
    a.auth_username = 'str'
    a.auth_password = 'str'
    a.auth_mode = 'str'
    a.request.headers = httputil.HTTPHeaders()
    a.request.body = 'str'
    a.final_callback = lambda: None
    a.start_time = dat

# Generated at 2022-06-22 13:21:56.492999
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    x = HTTPTimeoutError("A")
    x.message = "B"
    assert x.__str__() == "Timeout"



# Generated at 2022-06-22 13:22:04.684637
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    global _client_ssl_defaults
    stream = IOStream()
    enable_future = stream.stop_reading()
    request = HTTPRequest("http://www.google.com", "get", None, None, None, None, None)
    client = AsyncHTTPClient()
    final_callback = lambda response: None
    start_time = time.time()
    start_wall_time = start_time
    release_callback = None
    io_loop = IOLoop.current()
    connection = _HTTPConnection(
        stream,
        request,
        client,
        final_callback,
        start_time,
        start_wall_time,
        release_callback,
        io_loop,
    )
    connection.run()

if __name__ == '__main__':
    test__HTTPConnection_run()

# Generated at 2022-06-22 13:22:11.254786
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    _HTTPConnection._handle_exception = lambda self, typ, value, tb: True
    # HTTPConnection is an abstract class and cannot be instantiated
    conn = _HTTPConnection(None, None, None)
    conn.on_connection_close()
    # nothing should happen when the method is called on a closed connection

    # TODO: Test that the method actually closes the Stream when called
    # TODO: Test that the method does not cause StreamClosedError when called


# Generated at 2022-06-22 13:22:12.302065
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    pass


# Generated at 2022-06-22 13:22:24.881713
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    request = HTTPRequest(url='url', method='GET')

    response_buffer = BytesIO()
    response = HTTPResponse(request, 200, headers=None, buffer=response_buffer, request_time=0, start_time=0)
    client = AsyncHTTPClient()

    http_connection = _HTTPConnection(request=request, client=client, final_callback=None, release_callback=None, io_loop=IOLoop(), start_time=datetime.datetime.now(), start_wall_time=datetime.datetime.now())
    http_connection.code = 200
    http_connection.chunks = ['chunk1', 'chunk2']
    http_connection.request.streaming_callback = None
    http_connection.finish()

    assert response.code == 200

# Generated at 2022-06-22 13:22:26.575051
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    pass


# Generated at 2022-06-22 13:22:39.163754
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """Unit test for headers_received method of _HTTPConnection class."""

    # Asynchronous call
    async def _async_test():
        import asyncio

        asyncio.create_task(_async_test())
        # Async method
        # Assertion error
        # Assertion error
        # Assertion error
        # Type error
        # Assertion error
        # Assertion error
        # Assertion error
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # No exception
        # Assertion error
        # Assertion error


# Generated at 2022-06-22 13:22:41.358655
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    try:
        raise HTTPStreamClosedError('xxx')
    except:
        err = sys.exc_info()[1]
        return str(err) == 'xxx'



# Generated at 2022-06-22 13:22:49.041354
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    class MockRequest:
        streaming_callback = None

        def __init__(self):
            self.headers = {}

        def append_header(self, name, value):
            self.headers[name] = value

    from tornado.platform.asyncio import to_tornado_future
    from tornado.testing import AsyncTestCase, gen_test

    class Test_HTTPConnection(AsyncTestCase):
        @gen_test
        async def test__HTTPConnection_data_received(self):
            request = MockRequest()
            con = _client._HTTPConnection(request)
            con.code = None
            con.chunks = []
            request.streaming_callback = None
            con.headers = None
            con._should_follow_redirect = lambda: False
            con.request = request
            con.start_time = 1.0

# Generated at 2022-06-22 13:22:57.618941
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    from tornado.httpclient import HTTPResponse
    from tornado.testing import gen_test
    from .test.util import unittest
    import time
    import timeit

    class Callback():
        def __init__(self, test_case):
            self.test_case = test_case
        def __call__(self, response):
            self.test_case.assertEqual(response, None)

    class Test_async_fetch(unittest.AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.http_client = AsyncHTTPClient()

        @gen_test
        def test_async_fetch(self):
            cb = Callback(self)
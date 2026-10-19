

# Generated at 2022-06-22 13:16:36.693019
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    # init
    _HTTPConnection(None, None, None, None, None, None, None)


# Generated at 2022-06-22 13:16:43.467440
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # This is the method _HTTPConnection.data_received
    # tornado/httpclient.py:
    data_received = _HTTPConnection.data_received.__wrapped__
    # Unit test for _HTTPConnection.data_received
    # Test case 1
    http_connection = _HTTPConnection(
        parsed_url = None,
        max_body_size = None,
        max_header_size = None,
        max_buffer_size = None,
    )
    http_connection, chunk = data_received(
        http_connection,
        chunk = None,
    )

    # Unit test for _HTTPConnection.data_received
    # Test case 2

# Generated at 2022-06-22 13:16:47.628856
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # Tests that exception logging is working correctly
    # Note: The underlying function has no return value, so this test
    # will always pass.
    try:
        _HTTPConnection(
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ).on_connection_close()
    except Exception as e:
        assert False



# Generated at 2022-06-22 13:16:49.938997
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    assert str(HTTPTimeoutError(None)) == "Timeout"
    assert str(HTTPTimeoutError("message")) == "message"
    assert str(HTTPTimeoutError('')) == ''



# Generated at 2022-06-22 13:17:01.343795
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    http_client = AsyncHTTPClient()

# Generated at 2022-06-22 13:17:03.255610
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():

    assert _HTTPConnection().headers_received()



# Generated at 2022-06-22 13:17:06.335162
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    http_stream_closed_error = HTTPStreamClosedError("Error")
    assert http_stream_closed_error.__str__() == "Error"


# Generated at 2022-06-22 13:17:17.240221
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    async def test(stream):
        req = HTTPRequest("http://localhost/", method="POST", body="hello")
        conn = _HTTPConnection(req, stream, 1024, 1024, 5, True, None, None)
        conn.code = 200
        conn.reason = "OK"
        conn.headers = httputil.HTTPHeaders({"Content-Type": "text/html"})
        conn.chunks = ["hello", "world"]
        conn.final_callback = mock.Mock(spec=[])
        conn.client = mock.Mock(spec=["fetch"])
        conn.request = mock.Mock(spec=[])

        # test expected behavior
        conn.finish()

        # test follow redirect
        conn.request.max_redirects = 1
        conn.code = 302

# Generated at 2022-06-22 13:17:23.646067
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    _HTTPConnection(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )

# Generated at 2022-06-22 13:17:24.566087
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    pass


# Generated at 2022-06-22 13:18:44.857791
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # Creating headers for test
    headers = httputil.HTTPHeaders()
    headers.add("Location", "http://example.com")

    # Creating request for test
    request = HTTPRequest(request_timeout=10)

    # Creating instance of True
    instance = _HTTPConnection(request, None, None)
    # Calling headers_received
    instance.headers_received(None, headers)
    # Perform _should_follow_redirect()
    result = instance.code is not None and instance.code in (
        301,
        302,
        303,
        307,
        308,
    ) and instance.request.max_redirects > 0 and headers.get("Location") is not None
    # Asserting the result
    assert result is False

# Generated at 2022-06-22 13:18:46.738492
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    """
    Create a SimpleAsyncHTTPClient instance
    Send a request to the server using the fetch_impl method of SimpleAsyncHTTPClient instance
    """
    client = SimpleAsyncHTTPClient()
    url = "http://localhost:9898"
    response = client.fetch_impl(url)


# Generated at 2022-06-22 13:18:58.986119
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    request = None
    # Testing if method with an empty body returns None
    http_client = HTTPClient()
    http_client.fetch(request, raise_error=False)
    # Testing if method with a non empty body returns a HTTPResponse
    http_client2 = HTTPClient()
    http_client2.fetch(request, raise_error=False)
    # Testing if method without a body returns HTTPResponse, this is to catch
    # the case when all the headers have been received
    http_client3 = HTTPClient()
    http_client3.fetch(request, raise_error=False)
    # Testing if method with an empty headers returns None
    http_client4 = HTTPClient()
    http_client4.fetch(request, raise_error=False)
    # Testing if method with a non empty headers

# Generated at 2022-06-22 13:19:02.621126
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    x = HTTPClient()
    x.on_connection_close()


if __name__ == "__main__":
    test__HTTPConnection_on_connection_close()

# Generated at 2022-06-22 13:19:05.092597
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    client = SimpleAsyncHTTPClient()
    request = HTTPRequest("http://www.google.com")
    response = _HTTPConnection()
    response.data_received(chunk)


# Generated at 2022-06-22 13:19:16.251496
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    client = HTTPClient()
    data_received = _HTTPConnection.data_received
    request = HTTPRequest(url="http://127.0.0.1/data_received")
    request.streaming_callback = print
    request.follow_redirects = True
    request.max_redirects = 1
    response = HTTPResponse(request, 302, headers={"Location": "http://127.0.0.1/test"})
    # Test 1: Redirection
    assert data_received(client, request) is None
    assert request.url == "http://127.0.0.1/test"
    assert request.max_redirects == 0
    assert client._release() is None
    assert client._run_callback(response) is None
    assert client._on_end_request() is None
    # Test

# Generated at 2022-06-22 13:19:19.563873
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    """
    SimpleAsyncHTTPClient.fetch_impl
    """
    # Impossible to test without a server as we would need to test
    # two coroutines running simultaneously.
    assert False



# Generated at 2022-06-22 13:19:32.746223
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    """Unit test for method _HTTPConnection.run."""
    import os
    import unittest
    import unittest.mock
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    import asynctest
    import tornado.httpclient
    import tornado.http1connection
    import tornado.httpserver
    import tornado.locks
    import tornado.platform.asyncio
    import tornado.testing
    import tornado.web
    import tornado.websocket

    class TestCase(tornado.testing.AsyncHTTPTestCase):
        """Unit tests for HTTP client requests."""

        def setUp(self):
            super().setUp()
            self.http_client = tornado.httpclient.AsyncHTTPClient(self.io_loop)

# Generated at 2022-06-22 13:19:38.188636
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # _HTTPConnection: method on_connection_close
    origin = AsyncHTTPClient()
    response = origin.fetch("http://www.google.com")
    result = response.result()
# Asynchronous, see https://tornado.readthedocs.io/en/latest/testing.html

# Generated at 2022-06-22 13:19:48.291171
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    stream = IOStream(socket.socket(), io_loop=IOLoop.current())
    connection = _HTTPConnection(
        stream,
        ('127.0.0.1', 80),
        HTTPRequest(
            "GET",
            "http://localhost/",
            headers={"Content-Length": "3"},
            body="foo",
        ),
        5,
        IOLoop.current(),
        chunk_size=8192 * 4,
    )

    assert connection.stream is stream
    assert connection.parsed == urllib.parse.SplitResult(
        scheme='http',
        netloc='localhost',
        path='/',
        query='',
        fragment=''
    )

# Generated at 2022-06-22 13:22:08.277535
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    client = SimpleAsyncHTTPClient()
    client.close()



# Generated at 2022-06-22 13:22:09.704870
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    client = SimpleAsyncHTTPClient()
    client.close()



# Generated at 2022-06-22 13:22:17.024081
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    http_client = HTTPClient()
    class Stream(object):
        '''
        Class that creates mock `IOStream` object
        '''
        error = None
        
        def close(self):
            # TODO: this may cause a StreamClosedError to be raised
            # by the connection's Future.  Should we cancel the
            # connection more gracefully?
            pass
    
        def set_close_callback(self, callback):
            pass


# Generated at 2022-06-22 13:22:18.551944
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    pass


# Generated at 2022-06-22 13:22:28.130068
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    from tornado.httputil import HTTPHeaders, RequestStartLine
    from tornado.test.util import unittest
    from tornado.test.httpclient_test import _test_write

    class _DummyConnection(object):

        def __init__(self, f):
            self._f = f

        def write_headers(self, start_line, headers, chunk=None):
            self._f(start_line, headers, chunk)

        def close(self):
            pass

    class _HTTPConnectionTest(unittest.TestCase):

        def _f(self, start_line, headers, chunk=None):
            self.assertIs(type(start_line), RequestStartLine)
            self.assertEqual("GET", start_line.method)
            self.assertEqual("/hello", start_line.path)


# Generated at 2022-06-22 13:22:40.055565
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    from tornado.escape import native_str
    from tornado.httpclient import HTTPRequest
    from tornado.httputil import HTTPHeaders
    from tornado.httputil import _RequestProxy
    from tornado.stack_context import StackContext
    from test.util import run_until
    import contextlib
    import io
    import unittest
    import unittest.mock
    import urllib.parse
    import warnings

    class _Fakesock(io.BytesIO):
        def getsockopt(self, level, optname, buflen=None):  # type: ignore
            if optname == socket.SOL_SOCKET and level == socket.SOL_SOCKET:
                return struct.pack("i", 1)
            raise NotImplementedError()


# Generated at 2022-06-22 13:22:46.200168
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    from tornado.iostream import StreamClosedError
    from tornado.httputil import HTTPServerRequest
    a = _HTTPConnection(HTTPServerRequest(headers={},protocol="http",host="",method="",uri="",version=""),)
    a.final_callback = ""
    a.stream.error = ""
    try:
        a.on_connection_close()
    except HTTPStreamClosedError:
        pass
    else:
        raise Exception("must raise error")


# Generated at 2022-06-22 13:22:56.266755
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    http_client = HTTPClient()
    protocol = _HTTPConnection(http_client, None, None)
    protocol._sockaddr = ("localhost", 80)
    protocol.request = httpclient.HTTPRequest("http://localhost:8989/")
    protocol.code = 200
    protocol.headers = {"Location": "http://localhost"}
    protocol.chunks = [b"abc", b"def"]
    protocol.original_request = None
    protocol.final_callback = None
    protocol.start_time = time()
    protocol.start_wall_time = time()
    protocol.io_loop = IO_Scheduler()
    protocol.stream = IOStream(None)
    protocol._timeout = None
    protocol._release = MagicMock()
    protocol._run_callback = MagicMock()
    protocol._remove_timeout = MagicMock

# Generated at 2022-06-22 13:23:05.208042
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    from tornado import testing

    class _HTTPConnectionTestCase(testing.AsyncHTTPTestCase):
        def get_app(self):
            return self.application

        def test_finish(self):
            # _HTTPConnection.finish only accepts None as parameter
            self.assertRaises(TypeError, self.http_client._HTTPConnection.finish, 'test')
            self.assertRaises(TypeError, self.http_client._HTTPConnection.finish, 1)
            self.assertRaises(TypeError, self.http_client._HTTPConnection.finish, 123.456)
            self.assertRaises(TypeError, self.http_client._HTTPConnection.finish, True)
            self.assertRaises(TypeError, self.http_client._HTTPConnection.finish, {})

# Generated at 2022-06-22 13:23:08.203222
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # Create a SimpleAsyncHTTPClient instance
    simpleAsyncHTTPClient = SimpleAsyncHTTPClient()

    # get parameter request
    simpleAsyncHTTPClient.fetch_impl()

    # get parameter callback
    simpleAsyncHTTPClient.fetch_impl()

    # invoke method fetch_impl with non-positional argument
    try:
        simpleAsyncHTTPClient.fetch_impl()
    except Exception as error:
        print(error)

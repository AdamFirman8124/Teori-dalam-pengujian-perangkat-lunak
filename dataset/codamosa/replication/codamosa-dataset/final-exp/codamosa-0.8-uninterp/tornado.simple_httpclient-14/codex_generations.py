

# Generated at 2022-06-22 13:15:48.682315
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    from tornado import ioloop

    # TODO: write unit test for method on_connection_close of class _HTTPConnection
    ioloop.IOLoop.current().run_sync(test__HTTPConnection_on_connection_close)

# Generated at 2022-06-22 13:15:53.364322
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    req = httpclient.HTTPRequest("http://example.com/foo")
    conn = _HTTPConnection(req, None, object(), object(), object())
    conn.stream = httpclient.HTTPStreamClosedError("Test message")
    conn.on_connection_close()

# Generated at 2022-06-22 13:15:56.263401
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    """Unit test for _HTTPConnection.run"""
    _HTTPConnection.run()


# Generated at 2022-06-22 13:16:03.184165
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    # _HTTPConnection.finish() -> None
    connection = _HTTPConnection(
        client=None,
        request=None,
        stream=None,
        release_callback=None,
        final_callback=None,
        io_loop=None,
        max_header_size=None,
        max_body_size=None,
    )
    assert connection.finish() is None

# Generated at 2022-06-22 13:16:12.964931
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    from tornado.httputil import HTTPHeaders
    from tornado.testing import AsyncHTTPTestCase, gen_test, ExpectLog

    class SimpleAsyncHTTPClientTest(AsyncHTTPTestCase):

        def get_app(self):
            return Application()

        def fetch_impl(
            self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]
        ) -> None:
            key = object()
            self.queue.append((key, request, callback))
            assert request.connect_timeout is not None
            assert request.request_timeout is not None
            timeout_handle = None
            if len(self.active) >= self.max_clients:
                timeout = (
                    min(request.connect_timeout, request.request_timeout)
                    or request.connect_timeout
                    or request.request_timeout
                )

# Generated at 2022-06-22 13:16:25.138122
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import io
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado import gen
    from tornado import httpclient
    from tornado import iostream
    from tornado import httputil
    from tornado import netutil
    from tornado import testing
    from tornado import web
    from tornado import websocket
    from tornado.test.util import unittest
    from tornado.test.util import skipIfNonUnix  # type: ignore

    class EchoHandler(web.RequestHandler):
        async def get(self) -> None:
            self.write("code " + str(self.get_argument("code", 200)))

        async def post(self) -> None:
            self.set_header("Content-Length", "3")
            self.write("asdf")

    # We need an asyncio event loop.

# Generated at 2022-06-22 13:16:33.452877
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    loop = IOLoop()
    # param: stream:
    # param: all_connections:
    # param: max_buffer_size:
    # param: max_header_size:
    # param: max_body_size:
    # param: decompress:
    # param: read_chunk_size:
    # param: skip_payload_length_check:
    # param: body_timeout:
    conn = _HTTPConnection(stream=None, all_connections=None, max_buffer_size=None, max_header_size=None, max_body_size=None, decompress=None, read_chunk_size=None, skip_payload_length_check=None, body_timeout=None)
    assert isinstance(conn, _HTTPConnection)
    # param: first_line: HTTP version ('HTTP

# Generated at 2022-06-22 13:16:38.677347
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
  self = _HTTPConnection(
    request = httputil.HTTPMessageDelegate(
      headers = {
        "Accept-Encoding": "gzip",
        "Host": "www.example.com",
        "User-Agent": "Tornado/1.2",
      },
      start_line = "GET /?foo=bar HTTP/1.1",
      trailer = {},
    ),
    buffer = BytesIO(b'this is a test'),
    code = 200,
    headers = {
      "Content-Length": "11",
    },
    reason = "OK",
    request_time = 0.0,
    start_time = 0.0,
  )
  self.final_callback = None
  self.io_loop = IOLoop()

# Generated at 2022-06-22 13:16:39.717653
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    _HTTPConnection()
    _HTTPConnection()

# Generated at 2022-06-22 13:16:47.324479
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import mock

    mock_self = mock.Mock(spec=HTTPClient)
    mock_request = mock.Mock(spec=HTTPRequest)
    mock_response = mock.Mock(spec=HTTPResponse)
    mock_request.final_callback.return_value = mock_response
    mock_response.result.return_value = 'foo'
    mock_request.callback.return_value = mock_response
    mock_self.async_fetch.return_value = mock_request
    mock_request.final_callback.return_value = 'foo'
    mock_response.result.return_value = 'foo'
    mock_request.request_timeout = None
    mock_self.validate_cert = True
    mock_request.request_timeout = None
    mock_request.allow_nonstandard_methods

# Generated at 2022-06-22 13:19:06.076027
# Unit test for method run of class _HTTPConnection

# Generated at 2022-06-22 13:19:17.003822
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    import random
    import re
    import ssl
    import time
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado.log import gen_log
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.testing import gen_test, bind_unused_port, AsyncHTTPSTestCase
    from tornado.test.util import unittest, skipIfNonUnix
    from tornado.web import Application, RequestHandler
    from tornado.websocket import WebSocketHandler
    # Try to import OpenSSL, but don't fail if we don't have it.
    try:
        import OpenSSL  # type: ignore
    except ImportError:
        OpenSSL = None
    try:
        import pycurl  # type: ignore
    except ImportError:
        pyc

# Generated at 2022-06-22 13:19:17.717075
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    pass

# Generated at 2022-06-22 13:19:30.391588
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    http_client = AsyncHTTPClient()
    req = httpclient.HTTPRequest(url="https://www.google.cn")

# Generated at 2022-06-22 13:19:42.554286
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import os
    import time
    import socket
    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test
    from tornado.tcpclient import TCPClient
    from tornado.httputil import HTTPConnectionParameters
    from tornado.gen import coroutine
    from tornado.escape import to_unicode
    from tornado.simple_httpclient import _HTTPConnection


    class _DummyHTTPConnection(HTTPConnection):
        def initialize(
            self, request: HTTPRequest, release_callback: Callable[[], None]
        ) -> None:
            self.request = request
            self.release_callback = release_callback
            self.closed = False


# Generated at 2022-06-22 13:19:47.235013
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # set up
    self = _HTTPConnection(self=None, stream=object(), final_callback=None)
    first_line = str()
    headers = dict()

    # testing
    self.headers_received(first_line=first_line, headers=headers)


# Generated at 2022-06-22 13:19:59.501907
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado.escape import utf8
    from tornado.ioloop import IOLoop
    from tornado.http1connection import HTTP1Connection, HTTP1ConnectionParameters
    import tornado
    import _io
    import io
    import socket
    import ssl


    # Mock objects
    class Mock_HTTP1Connection(HTTP1Connection):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.stream = None # type: Optional[Union[IOStream, tornado.tcpclient.TCPClient]]
            self.closed = False
            self.server_hostname = None # type: Optional[str]
            self.server_alpn_protocols = None # type: Optional[List[str]]
            self.client_alpn_protocols = None # type:

# Generated at 2022-06-22 13:20:11.640810
# Unit test for method run of class _HTTPConnection

# Generated at 2022-06-22 13:20:18.098526
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():

    class UnitTestClass:

        def setUp(self):
            self.request = MagicMock()
            self.client = MagicMock()
            self.final_callback = MagicMock()
            self.request.follow_redirects = True
            self.request.max_redirects = 2
            self.request.method = "POST"
            self.code = 301
            self.headers = MagicMock()
            self.headers.get.return_value = "http://example.com"
            self.chunks = [b"first_chunk", b"second_chunk"]
            self.io_loop = MagicMock()
            self.io_loop.time = MagicMock(return_value=1)
            self.start_time = 0
            self.start_wall_time = 1


# Generated at 2022-06-22 13:20:20.315197
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    def test():
        _HTTPConnection.finish(None)
        return None

    return test()



# Generated at 2022-06-22 13:21:25.731678
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    import os
    import sys
    import unittest
    import unittest.mock

    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.httpclient import _HTTPConnection

    class AsyncTestCase(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if sys.version_info >= (3, 7):
                self.addClassCleanup(
                    AsyncIOLoop.current().close,
                    # This can useful to help identify leftover tasks
                    # in the `finally` block of an `await` statement.
                    # Set to `False` to disable this behavior.
                    warn_if_dirty=True,
                )

# Generated at 2022-06-22 13:21:30.186174
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    # Check that the method __str__ of class HTTPTimeoutError returns the correct value.
    # Test on a class instance with the default value for its argument.
    error = HTTPTimeoutError(message = None)
    assert str(error) == "Timeout"

    # Test on a class instance with a different value for its argument.
    error = HTTPTimeoutError(message = "There has been a timeout.")
    assert str(error) == "There has been a timeout."


# Generated at 2022-06-22 13:21:43.130078
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # Test init
    class TestConfigure(AsyncHTTPClient):
        def initialize(  # type: ignore
            self,
            max_clients: int = 10,
            hostname_mapping: Optional[Dict[str, str]] = None,
            max_buffer_size: int = 104857600,
            resolver: Optional[Resolver] = None,
            defaults: Optional[Dict[str, Any]] = None,
            max_header_size: Optional[int] = None,
            max_body_size: Optional[int] = None,
        ) -> None:
            pass

    client = TestConfigure()
    client.initialize()

# Generated at 2022-06-22 13:21:53.755709
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    self = _HTTPConnection()
    self.code = 200
    self.request = SimpleAsyncHTTPClient()._fetch_impl(HTTPRequest(url="http://httpbin.org/get")).request
    self.request.follow_redirects = True
    self.request.max_redirects = 5
    self.headers = SimpleAsyncHTTPClient()._fetch_impl(HTTPRequest(url="http://httpbin.org/get")).headers
    self.headers['Location'] = "http://httpbin.org/get"
    self.request.method = "GET"
    self.request.body = None
    self.request.headers.pop('Content-Length')
    self.request.headers.pop('Content-Type')
    self.request.headers.pop('Content-Encoding')

# Generated at 2022-06-22 13:22:03.128942
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    def main(self):
        return self.chunk_size
    # mock the method run of class _HTTPConnection

# Generated at 2022-06-22 13:22:07.688317
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    e = HTTPStreamClosedError("")
    assert str(e) == "Stream closed"
    assert e.message == "Stream closed"
    assert e.code == 599
    e = HTTPStreamClosedError(None)
    assert str(e) == "Stream closed"
    assert e.message == "Stream closed"
    assert e.code == 599
    message = "foobar"
    e = HTTPStreamClosedError(message)
    assert str(e) == message
    assert e.message == message
    assert e.code == 599



# Generated at 2022-06-22 13:22:11.534699
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    _HTTPConnection = HTTPClient()._HTTPConnection
    conn = _HTTPConnection(None, None, None, None)
    assert hasattr(conn, "stream")
    assert hasattr(conn, "on_connection_close")
    assert conn.on_connection_close() is None


# Generated at 2022-06-22 13:22:18.355631
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    """
    Tests for method on_connection_close of class _HTTPConnection.
    """
    pass

    # Test for method on_connection_close of class _HTTPConnection
    def test_on_connection_close(self, http_client_conn, io_loop):
        """Test that on_connection_close() raises an error with a 404"""
        io_loop.run_sync(
            lambda: http_client_conn.fetch(HTTPRequest("/not-found"))
        )
        assert True

    # Unit test for method finish of class _HTTPConnection
    def test_finish(self, http_client_conn, http_server_conn, io_loop):
        """Test that finish() does not fail with a 404"""

# Generated at 2022-06-22 13:22:24.560152
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
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
        None,
        None,
        None,
    ).on_connection_close()



# Generated at 2022-06-22 13:22:26.150564
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    pass



# Generated at 2022-06-22 13:23:28.334338
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    http_client = SimpleAsyncHTTPClient()
    request = HTTPRequest('http://www.163.com',method='GET')
    callback = lambda x:x
    http_client.fetch_impl(request,callback)
    http_client.close()


# Generated at 2022-06-22 13:23:36.276169
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado import ioloop, httpclient, locks
    import logging, sys

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    async def handle_request(request):
        headers = {"Content-Type": "text/plain"}
        return httpclient.HTTPResponse(
            request,
            200,
            headers=headers,
            buffer=io.BytesIO(b"Hello world!"),
            effective_url="http://127.0.0.1:8881",
        )

    async def go():
        server = test_utils.AsyncHTTPSTestServer(handle_request)
        await server.start_server()


# Generated at 2022-06-22 13:23:40.537442
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    def test(self):
        self.parsed.scheme = 'http'
        self.parsed.port = None
        self.request.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.request.headers['Content-Length'] = str(len(self.request.body))

    _HTTPConnection.run = test

# Generated at 2022-06-22 13:23:45.109879
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    request = HTTPRequest('http://www.example.com')
    self = _HTTPConnection(request, [], 10, logging.getLogger())
    text = '''
        <html>
            <head>
                <title>Example Web Page</title>
            </head>
            <body>
                <p>You have reached this web page by typing
                "www.example.com", "example.com", or "localhost" into your web browser.</p>
            </body>
        </html>
    '''
    chunk = bytes(text, 'utf-8')
    self.data_received(chunk)
    assert self.chunks[0] == chunk


# Generated at 2022-06-22 13:23:55.039243
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    info("Test method headers_received of class _HTTPConnection")
    from tornado.httpclient import _HTTPConnection
    from typing import List, IO
    import sys
    import io
    import sys
    from contextlib import redirect_stdout
    from io import StringIO

    def get_stdout(function, *args) -> List[str]:
        f = io.StringIO()
        with redirect_stdout(f):
            function(*args)
        return f.getvalue().splitlines()


# Generated at 2022-06-22 13:23:56.591466
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    http_client = HTTPClient()
    http_client.fetch("httpbin.org/ip")



# Generated at 2022-06-22 13:24:04.552124
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    timeout1 = "Timeout1"
    timeout2 = "Timeout2"
    error_message1 = "Timeout {0}".format(timeout1) if timeout1 else "Timeout"
    error_message2 = "Timeout {0}".format(timeout2) if timeout2 else "Timeout"
    requests = [HTTPRequest(url="https://www.baidu.com"), HTTPRequest(url="https://www.google.com")]
    callbacks = [Callable[..., Any](), Callable[..., Any]()]
    keys = [object(), object()]

# Generated at 2022-06-22 13:24:15.192369
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    class MockRequest:
        method = None
        url = None
        max_redirects = None
        headers = None
        original_request = None

    class MockClient:
        def fetch(self, *args, **kwargs): pass

    class MockIOStream:
        def close(self): pass

    code = None
    chunks = []
    final_callback = None
    start_time = None
    start_wall_time = None
    stream = MockIOStream()
    httpcon = _HTTPConnection(MockRequest(), MockClient())

    httpcon.code = code
    httpcon.chunks = chunks
    httpcon.final_callback = final_callback
    httpcon.start_time = start_time
    httpcon.start_wall_time = start_wall_time
    httpcon.stream = stream


# Generated at 2022-06-22 13:24:24.773373
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    if is_asyncio_test():
        coro = _HTTPConnection_finish()
        future = asyncio.ensure_future(coro)
        asyncio.get_event_loop().run_until_complete(future)
    else:
        _HTTPConnection_finish()


async def _HTTPConnection_finish():
    client = SimpleAsyncHTTPClient(io_loop=IOLoop.current())
    # Test that redirects are followed.
    for code in (301, 302, 303, 307, 308):
        req = HTTPRequest("http://localhost:%d/" % code, follow_redirects=True)
        response = await client.fetch(req)
        assert response.code == 200
        assert response.effective_url == "http://localhost:8888/"

# Generated at 2022-06-22 13:24:26.086401
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    pass  # TODO


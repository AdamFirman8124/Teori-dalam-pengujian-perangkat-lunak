

# Generated at 2022-06-22 13:15:36.017693
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    http_client = AsyncHTTPClient()
    request = HTTPRequest(url = "http://www.baidu.com")
    http_connection = _HTTPConnection(http_client, request)
    http_connection.finish()

# Generated at 2022-06-22 13:15:40.241129
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    _client = SimpleAsyncHTTPClient()
    request = HTTPRequest("http://www.github.com")
    callback = print
    _client.fetch_impl(request, callback)
    #_client.fetch_impl(request, callback)
    #_client.fetch_impl(request, callback)


# Generated at 2022-06-22 13:15:47.298151
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    import inspect
    import sys
    import time
    import unittest
    import urllib.parse
    import zlib

    import mock
    import tornado.concurrent
    import tornado.escape
    import tornado.gen
    import tornado.httpclient
    import tornado.httputil
    import tornado.ioloop
    import tornado.iostream
    import tornado.netutil
    import tornado.platform.auto
    import tornado.testing
    import tornado.test.util
    import tornado.web
    import tornado.websocket
    from tornado.httpclient import (
        HTTPRequest,
        HTTPResponse,
        _RequestProxy,
    )  # type: ignore

    from tornado.httputil import HTTPHeaders, _ArgumentParser


# Generated at 2022-06-22 13:15:49.731469
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # test for _HTTPConnection
    # test for on_connection_close method
    assert False



# Generated at 2022-06-22 13:16:01.450819
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # Create a mock io_loop
    mock_io_loop = unittest.mock.MagicMock()
    mock_io_loop.time.return_value = 1

    # Create a mock resolver
    mock_resolver = unittest.mock.MagicMock()
    mock_resolver.resolve.return_value = (socket.AF_INET, ("192.0.2.0", 80), 80)

    # Create a mock TCP Client
    mock_tcp_client = unittest.mock.MagicMock()

    # Create a mock AsyncHTTPClient
    mock_asynchttpclient = unittest.mock.MagicMock()

    # Create a mock HTTPRequest
    mock_http_request = unittest.mock.MagicMock()
    mock_http_request.connect_

# Generated at 2022-06-22 13:16:02.474263
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """Test for method headers_received of class _HTTPConnection."""
    pass



# Generated at 2022-06-22 13:16:12.853469
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    pass

    # Create a mock object that will be used as the HTTPConnection instance
    http_connection_mock = MagicMock(spec=_HTTPConnection, wraps=_HTTPConnection())

    # Mock the redirect, if we are going to follow a redirect so just discard the body.
    http_connection_mock._should_follow_redirect.return_value = False

    # Mock of self.request.streaming_callback
    streaming_callback_mock = MagicMock(side_effect=[])
    http_connection_mock.request.streaming_callback = streaming_callback_mock

    chunks_mock = MagicMock(return_value=b"Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    http_connection_mock.chunks = chunks_mock

    # Call the method under

# Generated at 2022-06-22 13:16:19.082317
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    loop = IOLoop.current()
    host, port = "127.0.0.1", 7000
    stream = StreamConnection(loop, host, port)
    sockaddr = (host, port)
    connection = _HTTPConnection(stream, sockaddr)
    assert connection.final_callback == None
    loop.close()


# Generated at 2022-06-22 13:16:28.161340
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    from tornado.httputil import HTTPHeaders, ResponseStartLine
    from tornado.httpclient import HTTPResponse
    from tornado.testing import gen_test
    import unittest

    h = HTTPHeaders()
    h.add("test1", "test2")
    h.add("test", "test3")
    h.add("test1", "test4")
    httplib_response = HTTPResponse(None, 200, headers=h)
    response = _HTTPConnection(None, httplib_response)
    yield response.headers_received(
        ResponseStartLine("GET", "/", "HTTP/1.1"), h
    )
    assert response.headers == h



# Generated at 2022-06-22 13:16:29.275946
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize(): # noqa: F811
    pass



# Generated at 2022-06-22 13:17:07.245927
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    pass


# Generated at 2022-06-22 13:17:07.872299
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    pass

# Generated at 2022-06-22 13:17:16.933685
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    """Test the method initialize of class SimpleAsyncHTTPClient."""
    s = SimpleAsyncHTTPClient()
    assert s.max_clients == 10
    assert s.max_clients == s.max_buffer_size
    assert s.max_header_size == None
    assert s.max_body_size == None

    s = SimpleAsyncHTTPClient(
        max_clients=3,
        hostname_mapping={"a": "b"},
        max_buffer_size=1,
        resolver=Resolver(),
        defaults={"a": "b"},
        max_header_size=1,
        max_body_size=2,
    )
    assert s.max_clients == 3
    assert s.max_clients == s.max_buffer_size
    assert s.max_header_size == 1


# Generated at 2022-06-22 13:17:19.290116
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    return

_VALID_SOURCE_ADDRESS = re.compile(r"^\d+\.\d+\.\d+\.\d+$")



# Generated at 2022-06-22 13:17:29.427227
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # TODO: add test cases
    return
# Class for managing asynchronous HTTP client feature.
#
# An HTTP client for use with `.IOLoop`-based asyncio applications.
# `HTTPClient` implements the following interface:
#
#   .. testcode::
#
#       from tornado.httpclient import (
#           AsyncHTTPClient,
#           HTTPRequest,
#           HTTPResponse,
#       )
#       from tornado.ioloop import IOLoop
#
#       loop = IOLoop.current()
#
#       def handle_response(response: HTTPResponse) -> None:
#           if response.error:
#               raise response.error
#           print(response.body)
#
#       request = HTTPRequest('http://www.google.com/')
#       client = AsyncHTTP

# Generated at 2022-06-22 13:17:41.830063
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    from tornado.httpclient import HTTPError
    from tornado.httpclient import HTTPResponse
    from tornado.httpclient import HTTPRequest
    from tornado.httpclient import _RequestProxy
    from tornado.httpclient import _HTTPConnection

    import io
    import sys
    import traceback
    import unittest


    class Test__HTTPConnection_finish(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_finish(self):
            if sys.version_info[0] == 2:
                h = httplib.HTTPMessage(io.BytesIO())
            else:
                h = httplib.HTTPMessage()



# Generated at 2022-06-22 13:17:53.227499
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    request = HTTPRequest(url='http://www.example.com')
    request = _RequestProxy(request, 'http://www.example.com')
    client = SimpleAsyncHTTPClient()
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    stream = IOStream(loop=loop, socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    hc = _HTTPConnection(request, client, stream)
    hc.code = 200
    hc.chunks = [b'a']
    hc.request.method = 'POST'
    hc.request.body = b'POST'
    hc.request.headers['Content-Length'] = '4'

# Generated at 2022-06-22 13:18:05.398927
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado.httpclient import HTTPRequest
    from tornado.httpserver import HTTPServer
    
    import tornado.escape
    import tornado.ioloop
    import tornado.web
    import tornado.websocket
    import tornado.testing
    
    
    
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")
    
    def ws_client_test_message(ws, message):
        """
        Handles incoming messages on the WebSocket.

        :param ws: The websocket object.
        :param message: The message data.
        """
        print(message)
        ws.close()
    

# Generated at 2022-06-22 13:18:10.923978
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    import httptools
    from tornado.httpserver import _HTTPConnection
    from tornado.httputil import HTTPHeaders
    from tornado import testing
    from tornado.testing import AsyncTestCase
    from tornado.test.util import unittest
    @testing.gen_test
    async def test_headers_received():
        expected_headers = [("Header", "Value")]
        expected_reason = "OK"
        start_line = httptools.ResponseStartLine("HTTP/1.0", 200, expected_reason)
        stream = mock.MagicMock()
        connection = _HTTPConnection(stream)
        connection.headers_received(start_line, HTTPHeaders(expected_headers))
        self.assertEqual(200, connection.code)
        self.assertEqual(expected_reason, connection.reason)

# Generated at 2022-06-22 13:18:21.247866
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    def callback(response):
        return response
    request = HTTPRequest('a')
    asyncHTTPClient = SimpleAsyncHTTPClient()
    asyncHTTPClient.fetch_impl(request, callback)
    assert asyncHTTPClient.queue[0][0] == request
    assert len(asyncHTTPClient.queue) == 1
    assert len(asyncHTTPClient.active) == 0
    assert len(asyncHTTPClient.waiting) == 1
    assert asyncHTTPClient.waiting[request] == (request, callback, None)
    asyncHTTPClient.max_clients = 1
    asyncHTTPClient.fetch_impl(request, callback)
    assert len(asyncHTTPClient.queue) == 0
    assert len(asyncHTTPClient.active) == 1
    assert len(asyncHTTPClient.waiting) == 2

# Generated at 2022-06-22 13:19:10.348237
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    import pytest
    from tornado.ioloop import IOLoop
    from tornado.netutil import Resolver
    from tornado.tcpclient import TCPClient
    from tornado.tcpserver import TCPServer
    from tornado.web import RequestHandler, Application
    import threading
    import socket
    import errno
    import time
    handler_done = threading.Event()
    server_done = threading.Event()
    client_done = threading.Event()
    class TCPServerHelper(TCPServer):
        def __init__(self, io_loop=None, ssl_options=None, **kwargs):
            super().__init__(io_loop=io_loop, ssl_options=ssl_options, **kwargs)

        def handle_stream(self, stream, address):
            pass

# Generated at 2022-06-22 13:19:11.485260
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    assert False, "Unimplemented"

# Generated at 2022-06-22 13:19:22.202109
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    con = _HTTPConnection(None, None, None, None)
    con.headers_received(None, None)
    assert con.headers == None

    con.request.follow_redirects = False
    con.headers_received(None, None)
    assert con.headers == None

    con.request.follow_redirects = True
    con.request.max_redirects = 0
    con.headers_received(None, None)
    assert con.headers == None

    con.request.max_redirects = 0
    con.code = 301
    con.headers = None
    con.headers_received(None, None)
    assert con.headers == None

    con.code = 301
    con.headers = {"Location": "http://127.0.0.1:8080"}

# Generated at 2022-06-22 13:19:23.532512
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # create case data
    pass



# Generated at 2022-06-22 13:19:24.320336
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    pass


# Generated at 2022-06-22 13:19:28.852167
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    from tornado.testing import AsyncHTTPTestCase, gen_test


# Generated at 2022-06-22 13:19:38.294870
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    async_client = AsyncHTTPClient(max_clients=10, resolver=Resolver())
    async_client_simple = SimpleAsyncHTTPClient(max_clients=10, resolver=Resolver())

    # check if tests are enabled
    if not async_client.configured:
        return

    # simple tests that a connection is made
    response = await async_client.fetch("http://www.facebook.com/")
    response = await async_client_simple.fetch("http://www.facebook.com/")
    assert response.code == 200


# Generated at 2022-06-22 13:19:47.310734
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    pass

    # _HTTPConnection._handle_exception
    # _HTTPConnection._remove_timeout
    # _HTTPConnection._release
    # _HTTPConnection._run_callback
    # _HTTPConnection._should_follow_redirect
    # _HTTPConnection.finish
    # _HTTPConnection.method

    # _HTTPConnection.headers_received
    # _HTTPConnection.on_connection_close
    # _HTTPConnection.on_headers
    # _HTTPConnection.on_headers_complete
    # _HTTPConnection.on_message_begin
    # _HTTPConnection.on_message_complete
    # _HTTPConnection.on_status
    # _HTTPConnection.on_url
    # _HTTPConnection.on_body



# Generated at 2022-06-22 13:19:51.700619
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    request = HTTPRequest('http://example.com/foo/bar')
    callback = lambda x: None
    client = SimpleAsyncHTTPClient()
    client.fetch_impl(request, callback)



# Generated at 2022-06-22 13:20:02.770656
# Unit test for method headers_received of class _HTTPConnection

# Generated at 2022-06-22 13:20:44.465201
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    ____test_connection = _HTTPConnection(
        ____test_request_proxy, ____test_stream, ____test_host, ____test_port
    )
    ____test_connection.final_callback = None
    ____test_connection.stream = None
    assert ____test_connection.final_callback is None

# Generated at 2022-06-22 13:20:57.073239
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # Create an instance of _HTTPConnection class
    connection = _HTTPConnection("test")
    # Set attribute chunks of connection with a list
    connection.chunks = []
    # Set attribute code of connection with a number
    connection.code = 200
    # Set attribute request with an instance of HTTPRequest class
    connection.request = httpclient.HTTPRequest("test")
    # Call method data_received of connection with a number
    connection.data_received(b"test")
    # Assert that chunks of connection has a value
    assert connection.chunks != []
    assert connection.chunks == [b"test"]

    # Set attribute request.streaming_callback of connection with a function
    connection.request.streaming_callback = lambda x: print(x)
    # Call data_received of conneciton with a number

# Generated at 2022-06-22 13:20:59.145588
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    global _HTTPConnection
    instance = _HTTPConnection(object,object,object)
    instance.on_connection_close()


# Generated at 2022-06-22 13:21:04.456144
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    headers = httputil.HTTPHeaders()
    first_line = httputil.ResponseStartLine("HTTP/1.1", 200, "")
    headers_received(
        first_line,
        headers,
    )

# Generated at 2022-06-22 13:21:16.321092
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    url = "http://www.baidu.com"
    args = parse_url_impl(url)
    request = HTTPRequest(url)
    connection = _HTTPConnection(args, request, 
        client=None, final_callback=None,
        release_callback=None,
        io_loop=None, max_header_size=None,
        chunk_size=10 * 1024 * 1024, max_body_size=2**20,
        decompress_response=True, proxy_host=None,
        proxy_port=None, proxy_username=None,
        proxy_password=None, allow_ipv6=False
        )
    assert connection.io_loop is None
    assert connection.chunk_size == 10485760
    assert connection.max_body_size == 1048576
    assert connection.request.allow

# Generated at 2022-06-22 13:21:23.528536
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    instance = SimpleAsyncHTTPClient()
    instance.close()


if typing.TYPE_CHECKING:
    import typing

    HTTPParseError = typing.TypeVar(
        "HTTPParseError",
        httputil.HTTPInputError,
        httputil.HTTPParserEOFError,
        httputil.HTTPParserInvalidInput,
    )
else:
    HTTPParseError = httputil.HTTPInputError



# Generated at 2022-06-22 13:21:32.572558
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # Create a simple HTTP 1.1 client on top of Tornado's IOStreams
    simpleAsyncHTTPClient = SimpleAsyncHTTPClient(max_clients=10, hostname_mapping=None, max_buffer_size=104857600, resolver=None, defaults=None, max_header_size=None, max_body_size=None)
    # Initialize a simple HTTP 1.1 client on top of Tornado's IOStreams
    simpleAsyncHTTPClient.initialize(max_clients=10, hostname_mapping=None, max_buffer_size=104857600, resolver=None, defaults=None, max_header_size=None, max_body_size=None)
    # True if the implementation supports cookies, and they should be returned
    # in a ``Cookie`` header.

# Generated at 2022-06-22 13:21:43.046264
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """Unit test for method headers_received of class _HTTPConnection"""
    # Test body or generated setup code
    io_loop = IOLoop()
    request = HTTPRequest(url="http://www.google.com")
    client = HTTPClient()
    h = _HTTPConnection(io_loop, request, client)
    import inspect
    args = inspect.getargvalues(inspect.currentframe())
    for i in args:
        print(i, args[i])
    h.headers_received(request, request.headers)
    assert True == True  # TODO: implement your test here


# Generated at 2022-06-22 13:21:46.623095
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    # prepare the test env
    # execute the target code
    # assert the expected result
    assert False



# Generated at 2022-06-22 13:21:47.801536
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # TODO: Fix it
    pass


# Generated at 2022-06-22 13:22:38.571495
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    strs = [b"This is the first sample string"]
    for s in strs:
        strs.append(s + b" and this is the second sample string")
    test = _HTTPConnection(stream=None)
    for i, s in enumerate(strs):
        with pytest.raises(AssertionError):
            test._HTTPConnection.headers_received(None, None)
        with pytest.raises(AssertionError):
            test._HTTPConnection._run_callback(None)
        with pytest.raises(AssertionError):
            test._HTTPConnection._remove_timeout()
        with pytest.raises(AssertionError):
            test._HTTPConnection._handle_exception(None, None, None)
        with pytest.raises(AssertionError):
            test._HTTPConnection

# Generated at 2022-06-22 13:22:39.669843
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    SimpleAsyncHTTPClient.initialize()



# Generated at 2022-06-22 13:22:47.790847
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    pass  # TODO: Implement test

    # def _start_timeout(self):
    #     if self.request.request_timeout:
    #         self._timeout = self.io_loop.add_timeout(
    #             self.start_time + self.request.request_timeout,
    #             functools.partial(self._on_timeout, "after %s seconds".format(self.request.request_timeout)))
    #     elif self.request.connect_timeout:
    #         self._timeout = self.io_loop.add_timeout(
    #             self.start_time + self.request.connect_timeout,
    #             functools.partial(self._on_timeout, "after %s seconds".format(self.request.connect_timeout)))

# Generated at 2022-06-22 13:22:49.509866
# Unit test for method __str__ of class HTTPTimeoutError
def test_HTTPTimeoutError___str__():
    err = HTTPTimeoutError('timeout error')
    assert str(err) == 'timeout error'
    err = HTTPTimeoutError('')
    assert str(err) == 'Timeout'


# Generated at 2022-06-22 13:22:57.944479
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    from tornado import testing
    from tornado.httpclient import _HTTPRequestProxy
    from tornado.testing import AsyncHTTPTestCase, ExpectLog

    class SimpleAsyncHTTPClientTest(testing.AsyncHTTPTestCase):
        def get_http_client(self):
            # type: () -> SimpleAsyncHTTPClient
            return SimpleAsyncHTTPClient(self.io_loop, force_instance=True)

        def test_max_clients(self):
            # type: () -> None
            client = self.get_http_client()
            self.assertEqual(10, client.max_clients)

        @testing.gen_test
        def test_close(self):
            client = self.get_http_client()
            req = HTTPRequest("http://example.com", connect_timeout=3600)

# Generated at 2022-06-22 13:23:06.150752
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # verify that _HTTPConnection.run(self, io_loop, release_callback) raises
        # an exception when self has an attribute called final_callback that
        # is None
        pass

    # verify that _HTTPConnection.run(self, io_loop, release_callback) raises
        # an exception when self has an attribute called max_body_size that is
        # None
        pass

    # verify that _HTTPConnection.run(self, io_loop, release_callback) raises
        # an exception when self has an attribute called max_header_size that
        # is None
        pass

    # verify that _HTTPConnection.run(self, io_loop, release_callback) raises
        # an exception when self has an attribute called parsed that is None
        pass

    # verify that _HTTPConnection.run(self, io_loop, release_callback)

# Generated at 2022-06-22 13:23:06.955548
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    obj = SimpleAsyncHTTPClient()
    obj.close()

# Generated at 2022-06-22 13:23:12.012489
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    first_line, headers = generate_data()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Generated at 2022-06-22 13:23:14.303094
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    # _HTTPConnection specific attributes should be set at instance creation
    io_loop = IOLoop()
    _HTTPConnection(io_loop)



# Generated at 2022-06-22 13:23:25.673786
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    from tornado.concurrent import Future
    from tornado.concurrent import TracebackFuture
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition
    from tornado.testing import AsyncTestCase, bind_unused_port
    from tornado.testing import gen_test
    from tornado.testing import ExpectLog
    from typing import Any
    from typing import Callable
    import socket
    import unittest
    # TODO: find out what is going on
    #@unittest.skip("Sometimes hangs")
    class _HTTPConnectionUnitTest(AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            sock, port = bind_unused_port()
            self.port = port
            self.sock = sock


# Generated at 2022-06-22 13:15:30.958935
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():

    client = SimpleAsyncHTTPClient()
    client.close()

# Generated at 2022-06-22 13:15:37.536844
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    cls_reference = SimpleAsyncHTTPClient
    fetch_impl_reference = cls_reference.fetch_impl
    @patch('tornado.httpclient.HTTPClient')
    def test_fetch_impl(self):
        request = magicMock(spec=HTTPRequest)
        callback = magicMock(spec=Callable[[HTTPResponse], None])
        fetch_impl_reference(self, request, callback)
        # TODO
        pass
        print('test_fetch_impl')
    test_fetch_impl(cls_reference(), 'cls_argument')


# Generated at 2022-06-22 13:15:38.702238
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    """
    _HTTPConnection()
    """
    pass



# Generated at 2022-06-22 13:15:39.905518
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """Test for method headers_received of class _HTTPConnection"""
    # TODO
    assert True



# Generated at 2022-06-22 13:15:40.538627
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    pass
    

# Generated at 2022-06-22 13:15:47.321603
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    import mock
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httputil import HTTPHeaders
    from tornado.httputil import HTTPServerRequest

    request_mock = mock.Mock()

    request_mock.headers = HTTPHeaders()
    response_mock = mock.Mock()
    response_mock.code = 204
    response_mock.reason = "No Content"
    response_mock.headers = HTTPHeaders()
    def finish():
        pass
    response_mock.finish = finish
    method_mock = mock.Mock()
    method_mock.return_value = response_mock
    client_mock = mock.Mock()
    client_mock.fetch = method_mock
    client_mock.return_value = client_mock

# Generated at 2022-06-22 13:15:56.381940
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    request = HTTPRequest("https://example.com", method="GET")
    client = HTTPClient()
    low_level_client = _HTTPConnection(
        request,
        client,
        client.io_loop,
        client._connector,
    )

    # test POST redirects
    low_level_client.request.method = "POST"
    low_level_client.headers = httputil.HTTPHeaders({"Location": "http://foo.com"})
    low_level_client.code = 301
    low_level_client.final_callback = MagicMock()
    low_level_client.client.fetch = MagicMock()
    low_level_client.finish()

    assert low_level_client.final_callback.called
    assert low_level_client.client.fetch.called

    #

# Generated at 2022-06-22 13:16:08.562515
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    max_clients = 10
    hostname_mapping = {
        'host 1': 'host 1',
        'host 2': 'host 2',
        'host 3': 'host 3',
        'host 4': 'host 4',
        'host 5': 'host 5'
    }
    resolver = Resolver()
    max_buffer_size = 104857600
    defaults = None
    max_header_size = None
    max_body_size = None
    http_client = SimpleAsyncHTTPClient()
    http_client.initialize(max_clients, hostname_mapping, max_buffer_size, resolver, defaults, max_header_size, max_body_size)
    assert http_client.max_clients == 10
    assert len(http_client.queue) == 0

# Generated at 2022-06-22 13:16:19.574105
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    self = _HTTPConnection()
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    self.request.ssl_options = get_ssl_context(cur_dir)
    self.request.stream.set_close_callback(self.on_connection_close)
    self.request.stream.fileno = lambda: None
    self.request.stream.get_fd = lambda: None
    self.request.stream.connect = lambda *args: None
    self.request.stream.starttls = lambda *args: None
    self.max_header_size = 65536
    self.max_body_size = 65536
    self.request.expect_100_continue = True
    self.request.decompress_response = True

# Generated at 2022-06-22 13:16:27.437357
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    fetch_impl = object()
    max_clients = object()
    hostname_mapping = object()
    max_buffer_size = object()
    resolver = object()
    defaults = object()
    max_header_size = object()
    max_body_size = object()
    # mock

# Generated at 2022-06-22 13:17:00.891943
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    pass


# Generated at 2022-06-22 13:17:04.966523
# Unit test for constructor of class _HTTPConnection
def test__HTTPConnection():
    conn = _HTTPConnection("1.2.3.4", 80, True)
    assert conn is not None
    assert conn.buffer == b""
    conn.buffer += b"1234567890"
    assert conn.buffer == b"1234567890"

# Generated at 2022-06-22 13:17:16.066689
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    request, client = mock.Mock(), mock.Mock()
    HTTPRequest.__init__ = mock.Mock(return_value=None)
    HTTPRequest.headers = {}
    HTTPRequest.release_callback = None
    HTTPRequest.expect_100_continue = False
    HTTPRequest.ssl_options = None
    HTTPRequest.decompress_response = False
    HTTPRequest.user_agent = "Tornado/{}".format(version)
    assert not hasattr(HTTPRequest, "allow_nonstandard_methods")
    assert not hasattr(HTTPRequest, "validate_cert")
    assert not hasattr(HTTPRequest, "ca_certs")
    assert not hasattr(HTTPRequest, "client_cert")
    assert not hasattr(HTTPRequest, "client_key")

# Generated at 2022-06-22 13:17:19.780568
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    stream = IOStream(socket.socket())
    client = HTTPClient()
    request = HTTPRequest("http://www.example.com/")
    http = _HTTPConnection(client, request, stream)
    first_line = httputil.ResponseStartLine("200", "OK")
    headers = httputil.HTTPHeaders()
    headers["Set-Cookie"] = "foo=bar"
    http.headers_received(first_line, headers)
    assert http.headers == headers
    assert http.code == 200
    assert http.reason == "OK"


# Generated at 2022-06-22 13:17:20.691911
# Unit test for method close of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_close():
    
    pass


# Generated at 2022-06-22 13:17:21.915201
# Unit test for method initialize of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_initialize():
    pass



# Generated at 2022-06-22 13:17:22.976804
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    pass # TODO


# Generated at 2022-06-22 13:17:28.646229
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # https://www.tornadoweb.org/en/stable/_modules/tornado/httpclient.html#SimpleAsyncHTTPClient.fetch_impl
    client = SimpleAsyncHTTPClient(max_clients=10)
    url = 'http://www.example.com/'
    callback = lambda response : None
    client.fetch_impl(url, callback)


# Generated at 2022-06-22 13:17:41.101532
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """Test _HTTPConnection.headers_received method."""
    # Init
    io_loop = IOLoop(make_current=True)
    r = HTTPRequest(url="http://google.com", method='GET')
    connection = HTTPClient()._HTTPConnection(r, io_loop)
    first_line = httputil.ResponseStartLine('HTTP/1.1', 200, 'OK')
    headers = httputil.HTTPHeaders()
    headers['Content-Type'] = 'text/html'
    headers['Content-Length'] = '14'
    headers['Date'] = 'Sun, 23 Sep 2018 20:21:41 GMT'
    headers['Cache-Control'] = 'private'
    headers['Server'] = 'GSE'
    headers['X-XSS-Protection'] = '1; mode=block'

# Generated at 2022-06-22 13:17:52.457330
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    # _HTTPConnection is a wrapper class around _HTTPConnection
    # that is returned by AsyncHTTPClient.fetch.  This test
    # exercise the _HTTPConnection class itself, not the
    # end-to-end behavior of AsyncHTTPClient.
    conn = _HTTPConnection(
        HTTPRequest(url="http://localhost"),
        max_header_size=100,
        max_body_size=100,
        decompress_response=True,
    )
    conn.headers_received(
        httputil.ResponseStartLine("HTTP/1.0", 501, "Not Implemented"),
        httputil.HTTPHeaders({"Content-Length": "0"}),
    )
    assert conn.code == 501
    assert conn.reason == "Not Implemented"
    assert conn.headers == httputil.HTTPHeaders

# Generated at 2022-06-22 13:20:57.949964
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    """Unit tests for _HTTPConnection.data_received.

    Raises:
        AssertionError: If any of the tests fails.
    """
    import tornado.httpclient
    from tornado.httpclient import HTTPRequest

    req = HTTPRequest("http://localhost:9000/")
    cli_inst = tornado.httpclient.AsyncHTTPClient()
    cli_inst.fetch(req)
    print(_HTTPConnection.data_received.__doc__)


if __name__ == "__main__":
    test__HTTPConnection_data_received()

# Generated at 2022-06-22 13:21:04.276034
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    class MockClient(object):
        def fetch(
            self, request: HTTPRequest, callback: Callable, **kwargs: Any
        ) -> "Future[HTTPResponse]":
            pass

    class MockIOLoop(object):
        def add_callback(self, func: Callable, *args: Any, **kwargs: Any) -> None:
            pass

    class MockStream(object):
        def is_closed(self) -> bool:
            pass

    class MockHTTPHeaders(object):
        def get_list(self, name: str) -> List[str]:
            pass

        def __len__(self) -> int:
            pass


# Generated at 2022-06-22 13:21:16.179778
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    # Test that the correct parameters are passed to the the run method
    # of _HTTPConnection class
    http_client = HTTPClient()
    request = http_client.fetch("http://localhost/")
    assert request.method == "GET"
    assert request.request_timeout == 20
    assert request.connect_timeout == 20
    assert request.follow_redirects == True
    assert request.max_redirects == 5
    assert request.decompress_response == True
    assert request.user_agent == "User-Agent"
    assert request.allow_nonstandard_methods == False
    assert request.validate_cert == True
    assert request.ca_certs == None
    assert request.client_cert is None
    assert request.client_key is None
    assert request.auth_username is None
    assert request.auth

# Generated at 2022-06-22 13:21:22.957889
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    request = HTTPRequest('http://127.0.0.1')
    test = AsyncHTTPClient()
    http_conn = await test._request(request, connection_type=HTTP1Connection)
    http_conn.on_connection_close()
    assert isinstance(http_conn.stream.error, HTTPStreamClosedError)


# Generated at 2022-06-22 13:21:24.150184
# Unit test for method fetch_impl of class SimpleAsyncHTTPClient
def test_SimpleAsyncHTTPClient_fetch_impl():
    # gen_log.info("success")
    print("success")



# Generated at 2022-06-22 13:21:32.233264
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    # Produce a subclass of _HTTPConnection that has an additional argument in its
    # constructor and override the finish method that calls the original finish
    # method with the additional argument.
    # This unit test tests that the override and the original finish method work
    # together.
    success = False
    try:
        class MockHTTPConnection(_HTTPConnection):
            def __init__(self, additionalArg, **kwargs):
                self.additionalArg = additionalArg
                super(MockHTTPConnection, self).__init__(**kwargs)

            def finish(self):
                super(MockHTTPConnection, self).finish()
                self.additionalArg = True
    except AttributeError:
        success = True
    assert success



# Generated at 2022-06-22 13:21:44.450522
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    args = [1]
    args[0] = httputil.RequestStartLine('GET', '/', 'HTTP/1.1')
    args.append(httputil.HTTPHeaders())
    kwargs = {}
    self = SimpleHTTPServer._HTTPConnection()
    self.code = 1
    self.chunks = []
    self.chunks.append(b'chunk')
    self.request = kwargs['request']
    self.io_loop = kwargs['io_loop']
    self.max_header_size = kwargs['max_header_size']
    self.max_body_size = kwargs['max_body_size']
    self.start_time = kwargs['start_time']
    self.start_wall_time = kwargs['start_wall_time']


# Generated at 2022-06-22 13:21:47.440938
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    # _HTTPConnection.on_connection_close(self)
    raise NotImplementedError()

# Generated at 2022-06-22 13:21:51.280875
# Unit test for method __str__ of class HTTPStreamClosedError
def test_HTTPStreamClosedError___str__():
    exception = HTTPStreamClosedError("")
    assert isinstance(exception, HTTPError)
    assert isinstance(exception, Exception)
    assert isinstance(exception, BaseException)
    assert exception.__str__() is None



# Generated at 2022-06-22 13:22:00.543820
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    from tornado.httputil import HTTPHeaders

    # method finish
    # initializing
    request = HTTPRequest(
        method='GET',
        url='http://localhost:8080/',
        validate_cert=False,
        allow_nonstandard_methods=False,
    )
    connection = _HTTPConnection(request, 
                                 client=None,
                                 release_callback=None,
                                 max_body_size=104857600,
                                 max_header_size=65536,
                                 final_callback=None,
                                 io_loop=None,
                                 chunk_size=None)
    # executing
    connection.code = 200
    connection.reason = 'Success'
    connection.headers = HTTPHeaders(Location='location')
    if connection._should_follow_redirect():
        assert connection

# Generated at 2022-06-22 13:22:45.711330
# Unit test for method data_received of class _HTTPConnection
def test__HTTPConnection_data_received():
    # [0]
    # https://github.com/tornadoweb/tornado/blob/08e822c/tornado/httpclient.py#L1169
    pass

data_received.__test__ = False  # type: ignore



# Generated at 2022-06-22 13:22:47.394692
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    pass



# Generated at 2022-06-22 13:22:51.041363
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    dummy = True
    if dummy:
        return
    def fun():
        self = _HTTPConnection(('localhost', 8000), HTTP1Connection, None, None, None, None, None, True)
        return self.run()
    fun()


# Generated at 2022-06-22 13:22:51.762038
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    pass



# Generated at 2022-06-22 13:23:02.348849
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    from tornado.httputil import HTTPHeaders
    from tornado.http1connection import _HTTPConnection
    from tornado import httputil
    httpconnection = _HTTPConnection('localhost', 80)
    httpconnection.request = _RequestProxy('GET')
    httpconnection.final_callback = lambda a: None
    httpconnection.headers_received(httputil.ResponseStartLine('HTTP', '200', 'OK'), HTTPHeaders())
    httpconnection.request.follow_redirects = True
    httpconnection.code = 302
    httpconnection.headers["Location"] = 'http://www.google.com'
    httpconnection.headers_received(httputil.ResponseStartLine('HTTP', '200', 'OK'), HTTPHeaders())
    httpconnection.code = 302

# Generated at 2022-06-22 13:23:04.156685
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    response = _HTTPConnection(HTTPRequest(url="http://www.example.com"),
                               lambda r: None, None)
    response.on_connection_close()

# Generated at 2022-06-22 13:23:09.563057
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    class FakeHTTPRequest(object):
        def __init__(self, code: int, headers: httputil.HTTPHeaders, method: str = "GET", body: bytes = b'', connection: Any = None):
            self.code = code
            self.headers = headers
            self.method = method
            self.body = body
            self.connection = connection

        def get_execute_future(self):
            return None

    class FakeStream(object):
        def __init__(self, *args, **kwargs):
            self.__exception__ = None

        def close(self, *args, **kwargs):
            pass

        def set_exception(self, exception):
            self.__exception__ = exception

    class FakeClient(object):
        def __init__(self):
            self.fetch_called

# Generated at 2022-06-22 13:23:14.665818
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    """
    Unit test for method headers_received of class _HTTPConnection
    """
    try:
        from tornado.escape import native_str
    except:
        from tornado.escape import to_unicode as native_str
    try:
        from urllib.parse import urlsplit
    except:
        from urlparse import urlsplit
    try:
        from urllib.parse import urlunsplit
    except:
        from urlparse import urlunsplit
    try:
        from urllib.parse import urljoin
    except:
        from urlparse import urljoin
    stream = IOStream(socket.socket())
    client = HTTPClient(io_loop=IOLoop.current())
    request = HTTPRequest(url="https://www.google.com/")

# Generated at 2022-06-22 13:23:15.500602
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    pass

# Generated at 2022-06-22 13:23:26.498889
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import to_tornado_future
    import asyncio
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = IOLoop()
    loop.make_current()

    def finish():
        loop.stop()

    stream = IOStream(socket.socket(), io_loop=loop)
    req_headers = httputil.HTTPHeaders()
    req_headers["User-Agent"] = "Mozilla/5.0"
    req_headers["Accept-Encoding"] = "gzip"
    req_headers["Content-Type"] = "application/x-www-form-urlencoded"

# Generated at 2022-06-22 13:24:15.656983
# Unit test for method headers_received of class _HTTPConnection
def test__HTTPConnection_headers_received():
    src = BytesIO(b"")
    dst = BytesIO()
    chunk = b""
    first_line = httputil.ResponseStartLine("", 200, "")
    headers = httputil.HTTPHeaders()
    connection = _HTTPConnection(src, dst)
    headers_received(connection, first_line, headers)

    # Verify that the instance's chunk field is a list of 10 bytes.
    assert isinstance(connection.chunks, list)
    assert connection.chunks[0] is chunk

    # Verify that the instance's first_line field is an httputil.ResponseStartLine object.
    assert isinstance(connection.first_line, httputil.ResponseStartLine)
    assert connection.first_line.code is first_line.code

    # Verify that the instance's headers field is an object of the type htt

# Generated at 2022-06-22 13:24:25.284028
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.testing import AsyncTestCase
    from tornado.testing import ExpectLog
    from tornado.testing import LogTrapTestCase, main
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.httpclient import HTTPResponse
    from tornado.httpclient import HTTPError
    from tornado.httputil import HTTPHeaders
    from tornado.httputil import HTTPConnectionParameters
    from tornado.httputil import HTTP1Connection
    import socket
    import unittest
    import tornado
    import time
    import httputil
    import io
    import io
    import io
    import ssl
    import sys
    import os
    import base64
    import socket
    import unittest
    import tornado


# Generated at 2022-06-22 13:24:25.955511
# Unit test for method on_connection_close of class _HTTPConnection
def test__HTTPConnection_on_connection_close():
    pass

# Generated at 2022-06-22 13:24:31.222039
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    chain = gen.chain_future(Future(), Future())
    chain.future.set_result(None)
    future = Future()
    chain.add_chain_future(future)
    
    
    
    
    
    
    
    
    
    
    
    io_loop = IOLoop()
    io_loop.make_current()

# Generated at 2022-06-22 13:24:40.769533
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    # This tests the headers_received method of _HTTPConnection.
    # Since headers_received is already tested, we are only testing
    # that the code to follow redirects works here.
    request = HTTPRequest("http://www.google.com/", follow_redirects=True)
    client = HTTPClient()
    # We use a _RequestProxy here to simulate a redirect.
    conn = _HTTPConnection(client, _RequestProxy(request), client.io_loop, client.max_header_size)
    conn.code = 302
    conn.headers = httputil.HTTPHeaders(Location="http://www.tornadoweb.org/")
    conn.final_callback = Mock()
    # Make sure the _RequestProxy is set to the expected type.
    assert conn.request.__class__ == _RequestProxy
    # This mimics the

# Generated at 2022-06-22 13:24:41.658533
# Unit test for method finish of class _HTTPConnection
def test__HTTPConnection_finish():
    _HTTPConnection();



# Generated at 2022-06-22 13:24:50.667829
# Unit test for method run of class _HTTPConnection
def test__HTTPConnection_run():
    if not hasattr(sys.stdout, "isatty") or sys.stdout.isatty():
        return

    def main():
        url = url_concat("http://localhost:%d" % get_unused_port(), dict(foo="bar"))
        http_client = HTTPClient()
        http_client.fetch(url)
        http_client.close()



# Generated at 2022-06-22 13:15:28.339129
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:38.312569
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.testing
    import tornado.platform.asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    import asyncio
    import tornado.escape
    import tornado.httpclient
    from tornado.httpclient import HTTPRequest
    import tornado.httputil
    import tornado.ioloop
    import tornado.stack_context
    import tornado.testing
    import tornado.util
    import tornado.web
    import tornado.websocket


    class AsyncHTTPClientTest(tornado.testing.AsyncHTTPTestCase):
        def get_app(self):
            return tornado.web.Application(
                [
                    (
                        "/",
                        tornado.web.RequestHandler,
                        dict(get=self._request_callback),
                    )
                ]
            )


# Generated at 2022-06-22 13:15:41.335045
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    """Test the method fetch of class HTTPClient."""
    httpClient = HTTPClient()
    response = httpClient.fetch("http://www.google.co.kr/")
    assert response.body != None


# Generated at 2022-06-22 13:15:54.507298
# Unit test for function main
def test_main():
    import os
    import sys
    import unittest.mock as mock
    from tornado import testing
    from tornado import ioloop

    from tornado.httpclient import main
    from tornado.options import options

    def main_test(response_code, response_headers, response_body,
                  proxy_host=None, proxy_port=None,
                  print_headers=False, print_body=True,
                  follow_redirects=True, validate_cert=True):
        context = testing.AsyncHTTPTestCase()
        main.AsyncHTTPClient = mock.Mock()
        # Some constraints on the mock behavior to make it act like
        # a real AsyncHTTPClient

# Generated at 2022-06-22 13:16:00.118666
# Unit test for function main
def test_main():
    def mock_parse_command_line():
        return ["args"]
    def mock_client_fetch():
        return HTTPClient.fetch()
    with patch("tornado.httpclient.parse_command_line", side_effect=mock_parse_command_line):
        with patch("tornado.httpclient.HTTPClient.fetch", side_effect=mock_client_fetch):
            assert main() is None

# Generated at 2022-06-22 13:16:10.573096
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.concurrent # type: ignore
    import tornado.httpclient # type: ignore
    import tornado.httputil # type: ignore
    import tornado.iostream # type: ignore
    import tornado.platform.auto # type: ignore
    import tornado.util # type: ignore

    from tornado.httpclient import HTTPRequest, HTTPResponse
    from tornado.httputil import HTTPHeaders
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.stack_context import ExceptionStackContext
    from tornado import testing
    import functools
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado import gen

    from asyncio import get_event_loop
    from asyncio.events import AbstractEventLoop
    from asyncio.streams import StreamWriter
    import urllib
    import re

# Generated at 2022-06-22 13:16:12.913462
# Unit test for function main
def test_main():
    if __name__ == "__main__":
        main()
    assert 1==1



# Generated at 2022-06-22 13:16:19.926156
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    rp = _RequestProxy(HTTPRequest("http://www.google.com"), {"abc": 123})
    assert hasattr(rp, "request")
    assert not hasattr(rp, "request_time")
    assert isinstance(rp.request, HTTPRequest)
    assert rp.connect_timeout == 20
    assert rp.abc == 123
    assert rp.defghi1234 is None



# Generated at 2022-06-22 13:16:29.803502
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.curl_httpclient import CurlAsyncHTTPClient
    import tornado.web

    class TestHandler(tornado.web.RequestHandler):
        def get(self):
            self.set_header("Content-Type", "text/plain")
            self.write("Hello, world")

    io_loop = IOLoop()
    io_loop.make_current()

    app = tornado.web.Application([("/", TestHandler)])
    ports = [
        app.add_sockets(io_loop, "127.0.0.1", 0)[0].getsockname()[1]
        for _ in range(3)
    ]

    def test_close(port: int) -> None:
        future = AsyncHTTPClient().fetch("http://127.0.0.1:%d" % port)



# Generated at 2022-06-22 13:16:41.055050
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    # Tested function
    def _fetch(client, url, params, method, headers, body, name):
        if url == '/test_bind':
            # Test bind() method
            assert name == 'test_bind', 'Wrong bind name'
        else:
            assert method == 'POST', 'Wrong method'
            if url == '/test_func_callback':
                # Test callback function
                assert headers['test1'] == 'test1'
                assert params['test2'] == 'test2'
                assert body == 'test3=test3', 'Wrong body'
            elif url == '/test_coroutine':
                # Test coroutine
                assert headers['test1'] == 'test1'
                assert params['test2'] == 'test2'
                assert body == 'test3=test3', 'Wrong body'


# Generated at 2022-06-22 13:16:50.137587
# Unit test for function main
def test_main():
  from tornado.testing import AsyncHTTPTestCase, main

  class MainTesting(AsyncHTTPTestCase):
    def test_main(self):
      main()

  main()

# Generated at 2022-06-22 13:16:51.242123
# Unit test for function main
def test_main():
    pass


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:16:52.324272
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    assert callable(AsyncHTTPClient().fetch_impl(None, None))



# Generated at 2022-06-22 13:16:52.780229
# Unit test for function main
def test_main():
    main()



# Generated at 2022-06-22 13:17:04.605194
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import tornado
    import tornado.ioloop
    import tornado.iostream

    class FakeRawIOBase(tornado.iostream.BaseIOStream):
        def set_close_callback(self, callback: Callable[["Future[None]", None], None]) -> None:
            pass

    class TestAsyncHTTPClient(tornado.httpclient.AsyncHTTPClient):
        _instance_cache = None  # type: Dict[tornado.ioloop.IOLoop, AsyncHTTPClient]

        def initialize(self, defaults: Optional[Dict[str, Any]] = None) -> None:
            pass

        def fetch_impl(
            self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]
        ) -> None:
            # Dummy
            pass


# Generated at 2022-06-22 13:17:12.927286
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    curr_AsyncHTTPClient_fetch_impl = AsyncHTTPClient.fetch_impl
    test_AsyncHTTPClient_fetch_impl.__name__ = "fetch_impl"
    
    @functools.wraps(test_AsyncHTTPClient_fetch_impl)
    def test_AsyncHTTPClient_fetch_impl(
        request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]) -> None:
        pass
    
    AsyncHTTPClient.fetch_impl = test_AsyncHTTPClient_fetch_impl


# Generated at 2022-06-22 13:17:22.680067
# Unit test for function main
def test_main():
    with mock.patch('sys.argv', ['httpclient_test', 'http://httpbin.org/get']):
        with mock.patch('tornado.httpclient.HTTPClient.fetch') as mockfetch:
            with mock.patch('sys.stdout') as mockstdout:
                mockfetch.return_value = mock.Mock()
                mockfetch.return_value.headers = {}
                mockfetch.return_value.body = b'Test content'
                main()
                mockstdout.write.assert_called_with(b'Test content')
            with mock.patch('sys.exit') as mockexit:
                with mock.patch('sys.stderr') as mockstderr:
                    mockfetch.side_effect = HTTPError(429)
                    main()

# Generated at 2022-06-22 13:17:34.754063
# Unit test for method __getattr__ of class _RequestProxy

# Generated at 2022-06-22 13:17:38.287108
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    def test_demo(request, callback):
        pass
    request = HTTPRequest('http://www.baidu.com')
    callback = None
    AsyncHTTPClient.fetch_impl(request, callback)
    return True


# Generated at 2022-06-22 13:17:49.104886
# Unit test for function main
def test_main():
    from tornado.testing import LogTrapTestCase, AsyncTestCase, gen_test, bind_unused_port
    import os.path
    from tornado.netutil import add_accept_handler
    from tornado.ioloop import IOLoop
    from tornado.httputil import HTTPHeaders
    from tornado.httpclient import HTTPRequest
    from tornado.tcpserver import TCPServer
    import logging

    class TestServer(TCPServer):
        """Http server that can be started and stopped in tests and which
        serves files from a static directory.
        """

        def initialize(self, path):
            self.path = path

        def handle_stream(self, stream, address):
            self._read_request(stream)
            method = self.request.method.decode("latin1")


# Generated at 2022-06-22 13:18:08.164022
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    try:
        AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    except ValueError as e:
        print("ValueError:%s" % e)



# Generated at 2022-06-22 13:18:11.504461
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    """
    def fetch_impl(self, request: "HTTPRequest", callback: Callable[[
    "HTTPResponse"], None]) -> None:
    raise NotImplementedError()
    """



# Generated at 2022-06-22 13:18:21.060610
# Unit test for function main
def test_main():
    from tornado.testing import AsyncTestCase, gen_test, main
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httputil import HTTPHeaders
    from tornado.escape import native_str

    class SyncHTTPClientTest(AsyncTestCase):
        def test_main(self):
            client = AsyncHTTPClient(self.io_loop)
            response = yield client.fetch('https://httpbin.org/get')
            print(response.headers)
            print(response.body)
            print(native_str(response.body))
            self.assertTrue(isinstance(response.headers, HTTPHeaders))
            self.assertTrue(response.body is not None)

    if __name__ == '__main__':
        main()

# Generated at 2022-06-22 13:18:33.285647
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    import asyncio
    if AsyncIOMainLoop.initialized():
        raise Exception("D'oh.")
    loop = asyncio.get_event_loop()
    AsyncIOMainLoop().install()

# Generated at 2022-06-22 13:18:37.662067
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        pass


# This is a stripped down version of certifi's where() function, which
# essentially just finds the default ca_certs file.

# Generated at 2022-06-22 13:18:43.793969
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.testing import AsyncHTTPTestCase

    class TestAsyncHTTPClient(AsyncHTTPTestCase):
        def get_app(self):
            return None

        async def test_AsyncHTTPClient_close(self):
            http_client = AsyncHTTPClient()
            try:
                http_client.close()
            except RuntimeError as e:
                self.fail("unexpected RuntimeError: {}".format(str(e)))

# Generated at 2022-06-22 13:18:53.103798
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase
    from tornado.web import RequestHandler, Application
    import unittest
    import tornado.options
    import logging

    class HelloHandler(RequestHandler):
        def get(self):
            self.write('Hello, world')

    class DownstreamHandler(RequestHandler):
        def get(self):
            self.request.connection.close()

    class FetchHandler(RequestHandler):
        def get(self):
            client = AsyncHTTPClient(self.application.io_loop)
            client.fetch(self.reverse_url('hello'), self.handle_fetch)

        def handle_fetch(self, response):
            self.write(response.body)
            self.finish()


# Generated at 2022-06-22 13:18:54.899914
# Unit test for constructor of class HTTPRequest
def test_HTTPRequest():
    request = HTTPRequest("http://www.baidu.com", "GET", {}, "")
    assert request.url == "http://www.baidu.com"
    assert request.method == "GET"
    assert request.headers == {}
    assert request.body == b''

test_HTTPRequest()



# Generated at 2022-06-22 13:19:02.249162
# Unit test for function main
def test_main():
    import signal
    import subprocess
    import sys
    import time
    import tornado.ioloop

    def test_main_http_callback(response):
        if response.error:
            raise Exception("unexpected error from http client: %s" % response.error)

    def test_main_timeout_callback_inner():
        tornado.ioloop.IOLoop.current().stop()
        print("timeout")
        raise Exception("timeout")

    def test_main_timeout_callback():
        # the test will usually finish well before the timeout, so
        # schedule the timeout to happen on the IOLoop instead of
        # using the one in fetch()
        tornado.ioloop.IOLoop.current().add_timeout(
            time.time() + 5, test_main_timeout_callback_inner
        )


# Generated at 2022-06-22 13:19:06.554657
# Unit test for function main
def test_main():
    if "TEST" not in os.environ:
        return
    if os.environ["TEST"] == "true":
        main()
    else:
        pass

if __name__ == "__main__":
    test_main()
 


# Generated at 2022-06-22 13:19:21.605015
# Unit test for function main
def test_main():
    testing_args = ['/', '/ip']
    try: 
        main(testing_args)
    except HTTPError as e:
        pass
    assert e.response.code > 200




# Generated at 2022-06-22 13:19:29.976865
# Unit test for function main
def test_main():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.httpclient import AsyncHTTPClient
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web

    class MainTest(AsyncTestCase):
        def setUp(self):
            super(MainTest, self).setUp()
            self.http_client = AsyncHTTPClient(self.io_loop)
            self._orig_main = tornado.httpclient.main
            tornado.httpclient.main = main

        def tearDown(self):
            tornado.httpclient.main = self._orig_main
            super(MainTest, self).tearDown()


# Generated at 2022-06-22 13:19:30.660551
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    pass



# Generated at 2022-06-22 13:19:40.295440
# Unit test for function main
def test_main():
    import unittest.mock
    from tornado.options import options

    with unittest.mock.patch("tornado.ioloop.IOLoop") as IOLoop:
        main()

    assert IOLoop.current().stop.called

    opts = options.as_dict()
    assert opts["print_headers"] is False
    assert opts["print_body"] is True
    assert opts["follow_redirects"] is True
    assert opts["validate_cert"] is True
    assert opts["proxy_host"] is None
    assert opts["proxy_port"] is None



# Generated at 2022-06-22 13:19:42.823938
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    c=AsyncHTTPClient()
    c.initialize()

# Generated at 2022-06-22 13:19:45.817788
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # AsyncHTTPClient.fetch_impl(self, request, callback) -> None
    client = AsyncHTTPClient()
    client.fetch_impl(request=HTTPRequest(), callback=None)



# Generated at 2022-06-22 13:19:55.376891
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
  from tornado.curl_httpclient import CurlAsyncHTTPClient
  from tornado.httpclient import AsyncHTTPClient
  import tornado.simple_httpclient
  from tornado.testing import AsyncHTTPTestCase, gen_test
  # Testing AsyncHTTPClient.close method.
  import asyncio
  import functools
  import ssl
  import socket
  import unittest
  import unittest.mock
  class CloseTest(AsyncHTTPTestCase):

    def get_app(self) -> object:
      #from tornado.platform.asyncio import to_asyncio_future
      async def async_sleep(delay: float, result: object) -> object:
        await asyncio.sleep(delay)
        return result

      class SleepHandler(RequestHandler):
        async def get(self) -> object:
          delay = float

# Generated at 2022-06-22 13:19:58.167872
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    instance = AsyncHTTPClient()
    # These tests depend on the implementation of simple_httpclient.
    assert instance.defaults == {"allow_nonstandard_methods": False}



# Generated at 2022-06-22 13:20:10.505576
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    client = AsyncHTTPClient()
    request = HTTPRequest("http://localhost/")
    future = client.fetch(request)
    future_result1 = future.result()
    future_result2 = future.result()
    assert future_result1 == future_result2
    
    # test for fetch_impl method
    future = Future()
    def handle_response(response):
        future_set_result_unless_cancelled(future, response)
    client.fetch_impl(request, handle_response)
    future_result3 = future.result()
    assert future_result3 == future_result1
    
    client.close()
    #@typing.no_type_check # line 1698

# Generated at 2022-06-22 13:20:13.280927
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.ioloop import IOLoop
    io_loop = IOLoop.current()
    io_loop._run_callback(f)
    io_loop.start()
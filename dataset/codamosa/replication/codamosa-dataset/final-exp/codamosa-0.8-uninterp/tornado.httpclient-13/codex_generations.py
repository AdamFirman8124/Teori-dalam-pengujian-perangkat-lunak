

# Generated at 2022-06-22 13:14:58.449396
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    pass


# Generated at 2022-06-22 13:15:08.384841
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase
    from tornado.web import RequestHandler
    from tornado.web import Application
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpserver import HTTPServer
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    import asyncio
    import time
    import sys
    from unittest.mock import patch
    from unittest.mock import MagicMock
    import io
    import logging
    import os
    import re
    import socket
    import threading
    import functools
    import hmac
    import platform
    import shutil
    import zlib
    # Requires root or administrator access.
    test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_s

# Generated at 2022-06-22 13:15:19.057282
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import RequestHandler
    from tornado.options import define, parse_command_line
    from tornado.httpserver import HTTPServer
    class MainTest(AsyncHTTPTestCase):
        def get_app(self):
            class MainHandler(RequestHandler):
                def get(self):
                    self.write("hello")
            return tornado.web.Application([(r"/", MainHandler)])
        @gen_test
        def test_main(self):
            define("print_headers", type=bool, default=False)
            define("print_body", type=bool, default=True)
            define("follow_redirects", type=bool, default=True)
            define("validate_cert", type=bool, default=True)

# Generated at 2022-06-22 13:15:20.025441
# Unit test for function main
def test_main():
    x = main()

# Generated at 2022-06-22 13:15:29.249631
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import unittest
    async def asyncTearDown():
        await gen.sleep(0)
    class AsyncHTTPClientTestCase(unittest.TestCase):
        def tearDown(self):
            self.io_loop.run_sync(asyncTearDown)
        def testAsyncHTTPClientConstructor(self):
            self.http_client = httpclient.AsyncHTTPClient()
            self.assertIsInstance(self.http_client, httpclient.AsyncHTTPClient)
        def test_fetch_impl(self):
            self.http_client = httpclient.AsyncHTTPClient()
            request_proxy = _RequestProxy(None, None)
            def callback(response):
                pass
            self.http_client.fetch_impl(request_proxy, callback)

# Generated at 2022-06-22 13:15:32.607202
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest('http://www.google.com', method='POST')
    defaults = {'method': 'GET'}
    req_proxy = _RequestProxy(request, defaults)
    assert req_proxy.method == 'POST' and req_proxy.defaults == defaults

# Generated at 2022-06-22 13:15:34.917402
# Unit test for function main
def test_main():
    # https://stackoverflow.com/questions/8298358/simulate-command-line-arguments-in-python
    main()


# Generated at 2022-06-22 13:15:43.558862
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    class Request(object):
        def __init__(self, method, **kwargs):
            self.method = method
            self.kwargs = kwargs
    request = Request("GET", name="test1")
    defaults = {"name":"test2"}
    request_proxy = _RequestProxy(request, defaults)
    print("request_proxy.method:", request_proxy.method)
    print("request_proxy.name:", request_proxy.name)
    print("request_proxy.kwargs:", request_proxy.kwargs)

# test__RequestProxy___getattr__()



# Generated at 2022-06-22 13:15:47.230822
# Unit test for function main
def test_main():
   pass 


if __name__ == "__main__":
    print("Use `python -m tornado.httputil` to run this program")
    sys.exit(1)

# Generated at 2022-06-22 13:15:47.667875
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:15:54.864061
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:15:56.497165
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()

# Generated at 2022-06-22 13:16:00.506189
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.simple_httpclient
    x = tornado.simple_httpclient.SimpleAsyncHTTPClient(force_instance=True)
    x.fetch("localhost")

# Generated at 2022-06-22 13:16:01.523338
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass

# Generated at 2022-06-22 13:16:02.321427
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    o = AsyncHTTPClient()
    o.__new__()


# Generated at 2022-06-22 13:16:12.649161
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    # Check the parameters

    # Initialize the IOLoop current
    io_loop = IOLoop.current()

    # See if the instance cache is None
    if force_instance:
        instance_cache = None
    else:
        instance_cache = cls._async_clients()

    # Make sure the instance knows which cache to remove itself from.
    # It can't simply call _async_clients() because we may be in
    # __new__(AsyncHTTPClient) but instance.__class__ may be
    # SimpleAsyncHTTPClient.
    instance._instance_cache = instance_cache

    # Add the value to the instance cache
    if instance_cache is not None:
        instance_cache[instance.io_loop] = instance

    # Return the instance
    return instance



# Generated at 2022-06-22 13:16:16.107088
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    # Check that close() doesn't have any errors.
    # Since it is a no-op for all subclasses,
    # call it on a SimpleAsyncHTTPClient
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    http_client = SimpleAsyncHTTPClient()
    http_client.close()



# Generated at 2022-06-22 13:16:16.678618
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:16:18.238061
# Unit test for function main
def test_main():
  pass

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:16:18.873528
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    pass



# Generated at 2022-06-22 13:16:35.959691
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    request = HTTPRequest("http://www.example.com")
    response = HTTPResponse(
        request,
        code=200,
        headers=None,
        buffer=None,
        effective_url=None,
        error=None,
        request_time=None,
        time_info=None,
        reason="OK",
        start_time=None,
    )
    response.rethrow()
    response._error_is_response_code = True
    response.error = HTTPError(200, "OK", response)
    with pytest.raises(HTTPError):
        response.rethrow()

# Generated at 2022-06-22 13:16:36.893784
# Unit test for function main
def test_main():
    with pytest.raises(ObjectNotFoundError):
        main()



# Generated at 2022-06-22 13:16:37.573132
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 13:16:38.280888
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 13:16:49.096036
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import unittest
    import tornado
    from tornado.httputil import HTTPHeaders
    from tornado.httpclient import HTTPRequest, HTTPResponse
    from tornado.httputil import HTTPHeaders
    from tornado.concurrent import Future, TracebackFuture
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.util import raise_exc_info
    from tornado.web import RequestHandler
    from tornado.httpserver import HTTPServer, HTTPRequest
    import asyncio
    import time
    from tornado.testing import AsyncHTTPTestCase
    class _RequestProxy(object):
        """Wraps an HTTPRequest with defaults and gives it an async interface."""


# Generated at 2022-06-22 13:17:00.158377
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    import tornado.ioloop
    import tornado.httpserver
    import threading
    import time
    import unittest

    class SyncHandler(tornado.web.RequestHandler):
        def get(self):
            self.write('Hello, world')

    app = tornado.web.Application([
        (r'/', SyncHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)

    class RequestProxyTest(unittest.TestCase):
        def handle_request(self, response):
            if response.error:
                raise Exception('Error response %s', response.error)
            else:
                self.assertEqual('Hello, world', response.body)
            self.stop()

       

# Generated at 2022-06-22 13:17:10.602465
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import pytest
    import uuid
    import shutil
    import os
    import sys
    import logging
    import subprocess
    import logging
    import sys
    import http.client
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import urllib.response
    import pair
    import tornado.httpclient
    import tornado.httpserver
    import tornado.httputil
    import tornado.web
    import tornado.ioloop
    import tornado.netutil
    import tornado.process
    import tornado.simple_httpclient
    import tornado.options

    from tornado.httpclient import AsyncHTTPClient


# Generated at 2022-06-22 13:17:20.401944
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    http_client = AsyncHTTPClient()
    http_client.fetch_impl(HTTPRequest('/foo'), f)
    # Test the exception if the subclass just implement the function
    def fetch_impl(self, request, callback):
        pass
    http_client.fetch_impl = fetch_impl
    try:
        http_client.fetch_impl(HTTPRequest('/foo'), f)
        assert False
    except NotImplementedError:
        assert True
    # Test the exception if an inherited class does not implement the function
    class A(AsyncHTTPClient): pass
    a = A()
    try:
        a.fetch_impl(HTTPRequest('/foo'), f)
        assert False
    except NotImplementedError:
        assert True



# Generated at 2022-06-22 13:17:21.002418
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass

# Generated at 2022-06-22 13:17:25.868321
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    # AsyncHTTPClient.__new__ -> AsyncHTTPClient.__new__
    # self = AsyncHTTPClient(force_instance = False, ** kwargs)
    # self = AsyncHTTPClient()
    # force_instance = False
    # kwargs = {}
    # return instance
    pass


# Generated at 2022-06-22 13:17:36.664449
# Unit test for function main
def test_main():
    import subprocess
    import os
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.escape import to_unicode
    from tornado.test.util import unittest
    url = "http://www.baidu.com"
    program = "python3"
    script = "./tornado/httpclient.py"
    result = subprocess.check_output([program, script, url], cwd=os.path.expanduser("~"))
    result_str = to_unicode(result)
    print(result_str)
    assert len(result_str) > 0
if __name__ == "__main__":
    test_main()

# Generated at 2022-06-22 13:17:38.902372
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    force_instance = True
    testAsyncHTTPClient = AsyncHTTPClient(force_instance)


# Generated at 2022-06-22 13:17:39.936123
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass



# Generated at 2022-06-22 13:17:46.408931
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    async def async_func():
        http_client = AsyncHTTPClient()
        http_client.close()

    # schedule async call
    io_loop = IOLoop.current()
    io_loop.add_callback(functools.partial(io_loop.run_sync, async_func))
    time.sleep(0.001)
    # run until all callbacks are scheduled
    io_loop.start()


# Generated at 2022-06-22 13:17:50.478291
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    http_client = HTTPClient()
    response = http_client.fetch("http://www.google.com/")
    print(response.body)
    http_client.close()


# Generated at 2022-06-22 13:17:53.276340
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    TestFetcher.test__RequestProxy___getattr__()


# TODO: move _ConnectionParameters here

# Generated at 2022-06-22 13:18:05.291892
# Unit test for function main
def test_main(): # make sure this function name is unique
    import sys
    import os
    import json
    import unittest
    from unittest.mock import patch, Mock
    from tornado.concurrent import Future
    from tornado.testing import AsyncTestCase, gen_test, main
    from tornado.httpclient import AsyncHTTPClient

    # The tornado.httpclient.main function is a command-line utility,
    # so we don't actually test it here (it has its own test in its
    # own file).  But it's handy to use it to test the HTTPClient
    # class, so we construct a command line and parse it here.
    def main_test(self):
        sys.argv = ['tornado.httpclient', '-h']

# Generated at 2022-06-22 13:18:08.572760
# Unit test for function main
def test_main():
    file_path = os.path.dirname(__file__) + "/main_test.txt"
    with open(file_path, 'rb') as f: 
        data = f.read().replace("\n", "")
    with patch('sys.stdout',new=StringIO()) as fake_out:
        main()
        assert fake_out.getvalue().replace("\n", "") == data


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:18:18.860124
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import Application
    from tornado.options import parse_command_line, options
    from tornado.httputil import HTTPHeaders
    
    
    def handle_request(request):
        assert(request.method == 'GET')
        assert(request.uri == '/')
        assert(request.version == 'HTTP/1.1')
        assert(request.headers[b'Content-Type'] == b'text/html')
        assert(request.body == b'')
        headers = HTTPHeaders({"Content-Type": "text/html; charset=UTF-8"})
        return HTTPResponse(request, 200, headers, b"Hello")
    

# Generated at 2022-06-22 13:18:19.981095
# Unit test for function main
def test_main():
    assert main()



# Generated at 2022-06-22 13:18:43.244064
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()

# Generated at 2022-06-22 13:18:44.256999
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:18:46.016055
# Unit test for function main
def test_main():
    import sys
    sys.argv = ['', '--validate_cert', 'True', 'http://www.baidu.com']
    main()


if __name__ == "__main__":
    test_main()
    print('TEST SUCEEDED!')

# Generated at 2022-06-22 13:18:57.546649
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import pytest
    import tornado.web

    async def async_fetch_url(url):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(url)
        return response.body.decode('utf-8')

    async def main():
        body = await async_fetch_url("https://httpbin.org/get")
        print(body)

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().run

# Generated at 2022-06-22 13:19:04.390983
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import RequestHandler, Application
    class SimpleHandler(RequestHandler):
        def get(self):
            self.write("hello")
    class TestMain(AsyncHTTPTestCase):
        def get_app(self):
            return Application([(r'/', SimpleHandler)])
        @gen_test
        def test_main(self):
            gen = main()
            self.assertIsNotNone(gen)
            result = yield gen
            self.assertIsNone(result)


# Generated at 2022-06-22 13:19:06.815302
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
  '''
  Unit test for method initialize of class AsyncHTTPClient
  '''
  from tornado_httpclient import AsyncHTTPClient
  httpc = AsyncHTTPClient()
  httpc.initialize()

# Generated at 2022-06-22 13:19:13.956060
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import tornado.ioloop

    class FooAsyncHTTPClient(AsyncHTTPClient):
        def initialize(self, *args, **kwargs):
            pass

        def fetch_impl(self, request: HTTPRequest, callback):
            callback(
                HTTPResponse(request, 200, buffer=BytesIO(utf8("response")), request_time=1)
            )

    AsyncHTTPClient.configure("tests.unit.ioloop_test.FooAsyncHTTPClient")
    client = AsyncHTTPClient()
    response = client.fetch("/")
    assert response.body == b"response"
    assert response.request_time() == 1

# Generated at 2022-06-22 13:19:16.165058
# Unit test for function main
def test_main():
	#main()
	return

if __name__ == "__main__":
	# Unit test for function main
	main()

# Generated at 2022-06-22 13:19:24.379538
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    import time
    import unittest
    from tornado.testing import AsyncHTTPTestCase, gen_test
    class AsyncHTTPClientMethodsTestCase(unittest.TestCase):
        def test_initialize(self):
            client=SimpleAsyncHTTPClient()
            client.initialize()
            self.assertIsInstance(client.io_loop,IOLoop)
    # The return type annotation is required as a workaround for
    # http://bugs.python.org/issue24931.
    def wrap(fn):
        return fn  # type: ignore

# Generated at 2022-06-22 13:19:29.288895
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    """Unit test for class HTTPClient."""

    c = HTTPClient()
    assert c._closed == False
    assert c._async_client != None
    assert isinstance(c, HTTPClient)

    c.close()
    assert c._closed == True



# Generated at 2022-06-22 13:19:56.504737
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    instance = AsyncHTTPClient.configured_class()()
    assert isinstance(instance, AsyncHTTPClient)

# Generated at 2022-06-22 13:20:02.521968
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    async def f():
        http_client = AsyncHTTPClient()
        http_client.close()
        try:
            response = await http_client.fetch("http://www.google.com")
        except Exception as e:
            print("Error: %s" % e)
        else:
            print(response.body)
    IOLoop.current().run_sync(f)

# Generated at 2022-06-22 13:20:04.030274
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    ...


# Generated at 2022-06-22 13:20:04.924318
# Unit test for function main
def test_main():
    main()



# Generated at 2022-06-22 13:20:15.848849
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    cls = AsyncHTTPClient
    import tornado.testing
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    from tornado.platform.asyncio import AsyncIOMainLoop

    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())

    def get_new_ioloop() -> IOLoop:
        return IOLoop.current()

    AsyncIOMainLoop().install()
    ioloop = get_new_ioloop()

    class MainHandler(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world")

    async def get_url(url: str) -> str:
        request = HTTPRequest(url)
        response = await cls().fetch(request)
        return response.body.decode("utf-8")

   

# Generated at 2022-06-22 13:20:27.903428
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    #
    # Same as above, but with a callback
    #
    @gen.coroutine
    def f():
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch("http://www.google.com")
        except Exception as e:
            print("Error: %s" % e)
        else:
            print(response.body)

    IOLoop.instance().run_sync(f)

    @gen.coroutine
    def main():
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch(
                "http://www.google.com", raise_error=False
            )
        except Exception as e:
            print("Error: %s" % e)
        else:
            if response.error:
                print

# Generated at 2022-06-22 13:20:29.337483
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    client = HTTPClient()
    client.close()



# Generated at 2022-06-22 13:20:41.028675
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient

    AsyncHTTPClient.configure("tornado.simple_httpclient.SimpleAsyncHTTPClient", max_clients=10)
    http_client = AsyncHTTPClient()
    print("xxx", http_client)
    http_client = SimpleAsyncHTTPClient()
    print("xxx", http_client)
    http_client = AsyncHTTPClient()
    print("xxx", http_client)

    def handle_request(response):
        if response.error:
            print("Error:", response.error)
        else:
            print(response.body)
        http_client.close()

    http_client.fetch("http://www.baidu.com", callback=handle_request)


# Generated at 2022-06-22 13:20:53.154246
# Unit test for function main
def test_main():
    import tornado.options
    import functools
    import io
    import logging
    import sys

    _ArgumentParser = getattr(tornado.options, '_ArgumentParser', None)
    if _ArgumentParser is None:
        return
    if sys.version_info[:2] == (2, 6):
        # Python 2.6 doesn't support the argparse module.
        return

    arguments = [
        '--print_headers',
        '--print_body',
        '--no_follow_redirects',
        'https://www.example.com/',
        'http://www.ahtnamas.net/',
    ]
    io_module = io
    if sys.version_info[0] == 2:
        io_module = sys


# Generated at 2022-06-22 13:21:01.950057
# Unit test for function main
def test_main():
    import sys
    import logging
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.httpclient import main
    from tornado.log import access_log

    # To silence warnings during the test
    logging.getLogger('tornado.access').setLevel(logging.CRITICAL)

    # Unit test has to be Async because of
    # "IOLoop must be started in order to make asynchronous calls"
    class FakeStdin(io.BytesIO):
        def readline(self):
            return self.read(1)

    class TestMain(AsyncTestCase):
        @gen_test
        def test_main(self):
            main()
            main([__file__])
            main(['-h'])

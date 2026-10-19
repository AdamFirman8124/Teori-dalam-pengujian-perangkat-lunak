

# Generated at 2022-06-22 13:15:13.151225
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:15:21.987057
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    http_client = HTTPClient()
    try:
        response = http_client.fetch("http://www.google.com/")
        print(response.body)
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))

    http_client.close()


# Generated at 2022-06-22 13:15:30.768200
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    handle = HTTPClient()
    try:
        response = handle.fetch("http://www.google.com/")
        print(response.body)
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    handle.close()


# Generated at 2022-06-22 13:15:32.727685
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:36.017211
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()


# Generated at 2022-06-22 13:15:39.081893
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    #Create an instance of class _RequestProxy
    request_proxy = _RequestProxy(None, None)
    #Test getattr method
    assert request_proxy.__getattr__("a_attr") is None


# Generated at 2022-06-22 13:15:40.539755
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:47.667688
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    io_loop = IOLoop(make_current=False)
    io_loop.make_current()
    httpclient = AsyncHTTPClient(io_loop=io_loop)
    httpclient.close()
    httpclient.close()
    httpclient.close()
    httpclient.close()
    httpclient.close()
    httpclient._closed = True
    httpclient.close()


# Generated at 2022-06-22 13:15:59.477253
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import unittest
    from . import AsyncHTTPClient
    from . import HTTPRequest
    from . import IOLoop
    from . import HTTPError

    class MyAsyncHTTPClient(AsyncHTTPClient):
        def fetch_impl(self, request, callback):
            if request.url.lower() == 'http://examplE.com/1':
                callback('example.com')
            else:
                callback(HTTPError(521))

    class TestAsyncHTTPClient(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop.current()
            self.client = MyAsyncHTTPClient()

        def tearDown(self):
            self.client.close()
            self.io_loop.close()


# Generated at 2022-06-22 13:16:06.765396
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.httputil import ResponseStartLine
    from tornado.http1connection import HTTP1ServerConnection, StringTranslator
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.httputil import HTTPHeaders
    from tornado.http1connection import HTTP1ConnectionParameters
    from tornado.platform.asyncio import AsyncIOMainLoop
    import asyncio
    from tornado.locks import Event
    from tornado import gen
    from tornado.httputil import HTTPConnectionParameters
    from tornado.http1connection import HTTPHeaders
    AsyncIOMainLoop().install()

# Generated at 2022-06-22 13:16:44.061313
# Unit test for function main
def test_main():
    main()

# python -m tornado.httputil.function_test
if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:16:52.292109
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    # Don't let the tests accidentally use real networks
    AsyncHTTPClient.configure(None, defaults=dict(allow_ipv6=False))
    for client_class in (
        SimpleAsyncHTTPClient,
        SimpleAsyncHTTPClient,  # try it twice to test the cache
    ):
        client = client_class()
        client.io_loop = IOLoop()
        # put a new IOLoop in current(), since we seem to have a global
        # cache of IOLoops
        io_loop = IOLoop()
        io_loop.make_current()
        try:
            url = "http://www.facebook.com/"
            response = client.fetch(url, raise_error=False)
            assert response.result().code == 599
        finally:
            io_loop.clear_current()
            io_

# Generated at 2022-06-22 13:17:04.189812
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from typing import Dict, Optional, Sequence, Any
    import datetime
    import time
    import unittest
    from tornado.httpclient import _RequestProxy
    from tornado.log import app_log
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.options import define, options, parse_command_line, parse_config_file
    import tornado.web
    import tornado.ioloop
    import tornado.escape
    import tornado.gen
    import tornado.platform.asyncio
    import tornado.testing
    define('port', default=None, help='port to listen on')
    parse_command_line()
    import unittest
    import asyncio
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncHTTPTestCase, bind_unused_

# Generated at 2022-06-22 13:17:15.217418
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    import os
    import sys
    import time
    import unittest
    from uuid import uuid4
    from tornado import gen
    from tornado import ioloop
    from tornado import testing
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.locks import Event
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.stack_context import StackContext
    from tornado.testing import LogTrapTestCase
    from tornado.web import Application
    from tornado.web import RequestHandler
    @gen.coroutine
    def f():
        raise gen.Return(None)
    @gen.coroutine
    def foo():
        raise gen.Return(None)
    @gen.coroutine
    def check_max_clients():
        raise gen.Return(None)


# Generated at 2022-06-22 13:17:23.462933
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    print("-"*10 + "test_AsyncHTTPClient_close" + "-"*10)
    AsyncHTTPClient._async_clients.clear()
    args = {"force_instance": True, "defaults": {"user_agent":"MyUserAgent"}}
    client_1 = AsyncHTTPClient(**args)
    client_2 = AsyncHTTPClient(**args)
    assert client_1 is client_2
    client_1.close()
    client_2.close() # do something is ok, it's idempotent
    client_3 = AsyncHTTPClient(**args)
    assert client_1 is not client_3
    client_3.close()



# Generated at 2022-06-22 13:17:26.113589
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    s = AsyncHTTPClient()
    def handle_response(response):
        pass

    s.fetch_impl(HTTPRequest(), handle_response) # does not raise error


# Generated at 2022-06-22 13:17:39.225173
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.platform.asyncio import BaseAsyncIOLoop
    client = AsyncHTTPClient()
    assert isinstance(client, AsyncHTTPClient)
    loop = IOLoop.current()
    client2 = AsyncHTTPClient()
    assert isinstance(client2, AsyncHTTPClient)
    assert client is client2
    assert client.io_loop is loop
    assert client._instance_cache is AsyncHTTPClient._async_clients()
    client3 = AsyncHTTPClient(force_instance=True)
    assert isinstance(client3, AsyncHTTPClient)
    assert client3 is not client2
    assert client3._instance_cache is None
    assert client3.io_loop is loop

# Generated at 2022-06-22 13:17:39.947267
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    pass

# Generated at 2022-06-22 13:17:50.603632
# Unit test for function main
def test_main():
    import sys

    if sys.version_info >= (3, 6):
        # Already tested in Python 3.5.2
        return
    import tornado.testing

    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.web import RequestHandler
    from tornado.httpserver import HTTPServer
    from tornado.testing import AsyncHTTPTestCase

    from tornado import gen

    class HelloHandler(RequestHandler):
        def get(self):
            self.write("Hello")

    class HelloRedirectHandler(RequestHandler):
        def get(self):
            self.redirect("/hello")

    class HelloUnicodeHandler(RequestHandler):
        def get(self):
            self.write(u"Привет")


# Generated at 2022-06-22 13:17:55.466772
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.httpclient
    client = tornado.httpclient.AsyncHTTPClient(max_clients=1000)
    request = tornado.httpclient.HTTPRequest("http://google.com")
    assert client.fetch_impl(request, None) is None


# Generated at 2022-06-22 13:19:06.904129
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)


# Generated at 2022-06-22 13:19:07.621543
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-22 13:19:11.587439
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    client = HTTPClient()
    client.close()
    asyncio.get_event_loop().close()


# Generated at 2022-06-22 13:19:12.449936
# Unit test for function main
def test_main():
    pass



# Generated at 2022-06-22 13:19:21.955363
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.testing as testing
    import tornado.web as web

    class SleepHandler(web.RequestHandler):
        def get(self):
            time.sleep(3600)

    application = web.Application([(r"/sleep", SleepHandler)])

    @testing.gen_test
    def test(io_loop):
        response = yield AsyncHTTPClient(io_loop=io_loop).fetch(
            "http://127.0.0.1:%d/sleep" % application.get_http_port()
        )
        assert response.body is not None
        io_loop.stop()

    io_loop = testing.IOLoop.current()
    io_loop.run_sync(functools.partial(test, io_loop))



# Generated at 2022-06-22 13:19:33.572912
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    test_AsyncHTTPClient_fetch()
    # Exercise the singleton logic in the constructor
    AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
    # Add a close method to stop the warning about a missing close
    AsyncHTTPClient().close = lambda: None
    client1 = AsyncHTTPClient(force_instance=True)
    assert type(client1) is AsyncHTTPClient.configurable_default
    client2 = AsyncHTTPClient(force_instance=True)
    assert client1 is client2
    client1.close()
    client2.close()
    assert not AsyncHTTPClient()._closed
    AsyncHTTPClient().close()



# Generated at 2022-06-22 13:19:42.627573
# Unit test for function main
def test_main():
    from tornado.options import define, options, parse_command_line
    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)
    args = parse_command_line()
    client = HTTPClient()

# Generated at 2022-06-22 13:19:43.996906
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:19:54.344798
# Unit test for method __new__ of class AsyncHTTPClient

# Generated at 2022-06-22 13:19:57.651101
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    client = AsyncHTTPClient()
    request = HTTPRequest("http://www.google.com")
    def callback(response):
        response.body
    client.fetch_impl(request, callback)


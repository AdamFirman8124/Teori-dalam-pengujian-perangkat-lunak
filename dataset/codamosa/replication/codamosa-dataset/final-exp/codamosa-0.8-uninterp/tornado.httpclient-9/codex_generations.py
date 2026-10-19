

# Generated at 2022-06-22 13:15:08.425751
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl(): 
    import asyncio
    import pytest
    import tornado.httpclient
    import tornado.simple_httpclient
    import tornado.testing

    class MyException(Exception):
        pass
    
    
    class MyHTTPClient(tornado.simple_httpclient.SimpleAsyncHTTPClient):
        def fetch_impl(self, request, callback):
            # Once we add support for streaming bodies, this should
            # probably return a stream.
            callback(
                tornado.httpclient.HTTPResponse(
                    request, 200, buffer=b"My fake body"
                )
            )
    
    
    @tornado.testing.gen_test
    def main():
        client = MyHTTPClient()
        response = yield client.fetch("http://example.com/foo")
        assert response.body == b"My fake body"
    

# Generated at 2022-06-22 13:15:09.315847
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass
    

# Generated at 2022-06-22 13:15:10.461969
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    pass



# Generated at 2022-06-22 13:15:13.413769
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    request = HTTPRequest("url", method="GET")
    response = HTTPResponse(request, 404, "error", reason="Not Found")
    response.rethrow()


# Generated at 2022-06-22 13:15:18.633877
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = httpclient.AsyncHTTPClient(force_instance=True)
    assert not client.closed
    client.close()
    assert client.closed
    client.close()
    assert client.closed

# Generated at 2022-06-22 13:15:20.812520
# Unit test for constructor of class HTTPResponse
def test_HTTPResponse():
   response = HTTPResponse(HTTPRequest("GET","www.google.com",None),200,None,None,None,None,0)


# Generated at 2022-06-22 13:15:21.406769
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    return



# Generated at 2022-06-22 13:15:22.843604
# Unit test for function main
def test_main():
    pass

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:27.599904
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    request = HTTPRequest()
    callback = lambda x: x
    try:
        AsyncHTTPClient.fetch_impl(request, callback)
    except Exception as e:
        print(e)
        print("ok")
    else:
        raise Exception("Failed")



# Generated at 2022-06-22 13:15:37.613161
# Unit test for method rethrow of class HTTPResponse

# Generated at 2022-06-22 13:15:52.203724
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    async def async_fetch(url: str) -> AsyncResult[None]:
        request = HTTPRequest(url=url)
        # client = HTTPClient()
        response = await client.fetch(request)
        await gen.sleep(0)
        # print(response)

    client = HTTPClient()
    print("http://se.moe/s.p")
    IOLoop.current().run_sync(functools.partial(async_fetch,"http://se.moe/s.p"))



# Generated at 2022-06-22 13:15:53.894790
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    """Test for method initialize of class AsyncHTTPClient"""
    pass


# Generated at 2022-06-22 13:16:03.190226
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    # Test AsyncHTTPClient.__new__.
    from tornado.simple_httpclient import SimpleAsyncHTTPClient

    def mock_instance(io_loop: "IOLoop", force_instance: bool, **kwargs: Any) -> Any:
        io_loop.configured = True
        return object()

    class CustomHTTPClient(AsyncHTTPClient):
        pass

    AsyncHTTPClient.configure(mock_instance, max_clients=10)
    # __new__ without keyword argument
    AsyncHTTPClient()
    assert IOLoop.current().configured

    IOLoop.clear_current()
    io_loop = IOLoop()
    io_loop.make_current()
    # An instance should be cached with the current IOLoop.
    assert AsyncHTTPClient() is AsyncHTTPClient()
    assert not I

# Generated at 2022-06-22 13:16:05.624187
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    obj = AsyncHTTPClient()
    request = HTTPRequest()
    callback = lambda x : x
    obj.fetch_impl(request, callback)

# Generated at 2022-06-22 13:16:16.906068
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    if __name__ == "builtins":  # make sure not to import __main__
        from tornado.simple_httpclient import SimpleAsyncHTTPClient
        from tornado.curl_httpclient import CurlAsyncHTTPClient
        from tornado.platform.asyncio import AsyncIOMainLoop
    else:
        from .simple_httpclient import SimpleAsyncHTTPClient
        # work around pyflakes issue #13
        CurlAsyncHTTPClient = SimpleAsyncHTTPClient
        AsyncIOMainLoop = SimpleAsyncHTTPClient
    AsyncHTTPClient.configure("tornado.test.httpclient_test.CurlAsyncHTTPClient")
    http_client1 = AsyncHTTPClient(force_instance=True)
    http_client2 = AsyncHTTPClient(force_instance=True)
    assert isinstance(http_client1, CurlAsyncHTTPClient)

# Generated at 2022-06-22 13:16:22.113003
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    http_client = HTTPClient()
    try:
        response = http_client.fetch("http://www.google.com/")
        print(response.body)
    except HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    http_client.close()


# Generated at 2022-06-22 13:16:31.409355
# Unit test for function main
def test_main():
    import io
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.options import options, parse_command_line
    from tornado.web import Application, RequestHandler

    parse_command_line(['test', '--log_to_stderr=False'])

    class MockHTTPClient(HTTPClient):
        def initialize(self, io_loop=None, max_clients=10,
                       hostname_mapping=None, max_buffer_size=None,
                       resolver=None, defaults=None):
            pass

    def create_mock_httpclient():
        return MockHTTPClient()

    class HelloHandler(RequestHandler):
        def get(self):
            self.write("Hello")

    class SecondHandler(RequestHandler):
        def get(self):
            self.write("Second")


# Generated at 2022-06-22 13:16:36.240948
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    try:
        http_client.close()
    except:
        pass
    http_client = httpclient.HTTPClient()

    try:
        response = http_client.fetch("http://tornado_test:9007")
        print(response.body)
    except httpclient.HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    http_client.close()

# Test for method fetch of class HTTPClient
# Test case:
#   Send a request to an invalid URL and an exception will be thrown
test_HTTPClient_fetch()


# Generated at 2022-06-22 13:16:36.945198
# Unit test for function main
def test_main():
    assert callable(main)
    main()
main()

# Generated at 2022-06-22 13:16:48.174774
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import sys
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web
    import tornado.options
    import tornado.escape

    class NoAdditionalArgsHttp1ServerTest(tornado.testing.AsyncHTTPTestCase):
        def get_app(self):
            return tornado.web.Application([
                (r"/initialize_args", RequestHandlingHandler),
            ])

    class RequestHandlingHandler(tornado.web.RequestHandler):
        def initialize(self, **kwargs):
            self.kwargs = kwargs
            self.io_loop = tornado.ioloop.IOLoop.current()

        def get(self):
            self.write(self.kwargs)


# Generated at 2022-06-22 13:17:27.063147
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    import tornado

    _instance_cache = None  # type: Dict[IOLoop, AsyncHTTPClient]

    @classmethod
    def configurable_base(cls) -> Type[Configurable]:
        return AsyncHTTPClient

    @classmethod
    def configurable_default(cls) -> Type[Configurable]:
        from tornado.simple_httpclient import SimpleAsyncHTTPClient

        return SimpleAsyncHTTPClient

    @classmethod
    def _async_clients(cls) -> Dict[IOLoop, "AsyncHTTPClient"]:
        attr_name = "_async_client_dict_" + cls.__name__
        if not hasattr(cls, attr_name):
            setattr(cls, attr_name, weakref.WeakKeyDictionary())

# Generated at 2022-06-22 13:17:28.325339
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-22 13:17:40.786847
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import asyncio
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.test.util import unittest

    class DummyAsyncHTTPClient(AsyncHTTPClient):
        def __init__(self, test):
            self.test = test

        def fetch_impl(self, request, callback):
            pass

    class TestAsyncHTTPClient(unittest.TestCase):
        def test_async_client_dict(self):
            io_loop1 = IOLoop()
            io_loop2 = IOLoop()
            with io_loop1:
                client1 = DummyAsyncHTTPClient(self)
                client2 = AsyncHTTPClient(force_instance=True)

# Generated at 2022-06-22 13:17:41.621242
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass

# Generated at 2022-06-22 13:17:42.334439
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:17:43.066954
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass



# Generated at 2022-06-22 13:17:43.790069
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass

# Generated at 2022-06-22 13:17:44.469611
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:17:50.283772
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    # Create an instance of class AsyncHTTPClient using the contructor
    a = AsyncHTTPClient()

    # Call the method fetch of the object a 
    # Solved using keyword arguments
    r = a.fetch(raise_error = False, request = "http://www.google.com")

    # The result is of type Future[HTTPResponse]
    assert isinstance(r, Future[HTTPResponse])


# Generated at 2022-06-22 13:17:52.970752
# Unit test for function main
def test_main():
    pass


# This hack fixes the issue: https://github.com/python/mypy/issues/1409

# Generated at 2022-06-22 13:18:41.120569
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    async def async_test():  # this will be run in the task thread
        pass
    # curl the function async_test
    resp = AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")
    # close AsyncHTTPClient
    resp.close()



# Generated at 2022-06-22 13:18:45.841323
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():

    from tornado import simple_httpclient

    obj = simple_httpclient.SimpleAsyncHTTPClient()

    r = simple_httpclient.HTTPRequest('http://example.com')
    assert r.url == 'http://example.com'

    def cb(response):
        return 'Response'

    assert obj.fetch_impl(r, cb) == None

    def cb(response):
        return 'Response'

    assert obj.fetch_impl(r, cb) == None

    obj.close()


# Generated at 2022-06-22 13:18:47.721593
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    # Make sure that close doesn't raise any errors if we've
    # called fetch or fetch_multi.
    h = AsyncHTTPClient()
    h.fetch("localhost")
    h.close()

# Generated at 2022-06-22 13:18:59.767447
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.concurrent import Future
    from tornado.escape import url_escape
    from tornado import gen
    from tornado.httpclient import AsyncHTTPClient

    @gen.coroutine
    def f():
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch("http://www.google.com/")
        except Exception as e:
            print("Error: %s" % e)
        else:
            # print(response.body)
            print(response.body)
    io_loop = IOLoop.current()
    io_loop.run_sync(f)

    @gen.coroutine
    def coroutine():
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.google.com/")
        raise gen.Return

# Generated at 2022-06-22 13:19:11.905924
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.concurrent import TracebackFuture, future_set_result_unless_cancelled, future_set_exception_unless_cancelled
    import urllib.request, tornado.ioloop
    class Future(TracebackFuture):
        pass
    class AsyncHTTPClient(object):
        def fetch_impl(self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]) -> None:
            try:
                resp = urllib.request.urlopen(request.url)
                buf = BytesIO()
                while True:
                    s = resp.read(1024)
                    if s:
                        buf.write(s)
                    else:
                        break
                future_set_result_unless_cancelled(callback, buf.getvalue())
            except Exception as e:
                future_

# Generated at 2022-06-22 13:19:15.810684
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import tornado.simple_httpclient
    instance = tornado.simple_httpclient.SimpleAsyncHTTPClient()
    instance = tornado.simple_httpclient.SimpleAsyncHTTPClient(force_instance=True)


# Generated at 2022-06-22 13:19:24.135255
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    assert AsyncHTTPClient() is AsyncHTTPClient()
    assert type(AsyncHTTPClient()) is SimpleAsyncHTTPClient
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient(
        force_instance=True
    )
    assert type(AsyncHTTPClient(force_instance=True)) is SimpleAsyncHTTPClient

    class MyAsyncHTTPClient(AsyncHTTPClient):
        pass

    AsyncHTTPClient.configure(MyAsyncHTTPClient)
    assert AsyncHTTPClient() is AsyncHTTPClient()
    assert type(AsyncHTTPClient()) is MyAsyncHTTPClient
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient(
        force_instance=True
    )
    assert type(AsyncHTTPClient(force_instance=True)) is MyAsync

# Generated at 2022-06-22 13:19:37.441182
# Unit test for method __getattr__ of class _RequestProxy

# Generated at 2022-06-22 13:19:40.251845
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    client = AsyncHTTPClient()
    assert client.io_loop == IOLoop.current()
    assert client.defaults == HTTPRequest._DEFAULTS
    assert not client._closed
    assert client._instance_cache == None




# Generated at 2022-06-22 13:19:52.513969
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    # request is an instance of HTTPRequest
    request = HTTPRequest(url="hello")
    a = AsyncHTTPClient()
    a.fetch(request, raise_error=True)
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    b = AsyncHTTPClient()
    b.fetch(request, raise_error=True)

    # request is a str
    request = "http://www.google.com"
    a = AsyncHTTPClient()
    a.fetch(request, raise_error=True)
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    b = AsyncHTTPClient()
    b.fetch(request, raise_error=True)

    # with kwargs

# Generated at 2022-06-22 13:20:36.467473
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    client = AsyncHTTPClient()
    request = HTTPRequest(url="http://www.google.com")
    callback = lambda response: None # type: Callable[[HTTPResponse], None]
    client.fetch_impl(request, callback)
    client.close()

test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()
test_AsyncHTTPClient_fetch_impl()

# Generated at 2022-06-22 13:20:43.933339
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    # Tests that close will get called on the underlying client
    instance_cache = {}
    httpclient_class = type('', (AsyncHTTPClient, ), {'_instance_cache': instance_cache})
    client = httpclient_class()

    def _close():
        client._closed = True

    client._async_client = type('', (object, ), {'close': _close})
    instance_cache[client.io_loop] = client
    client.close()
    assert 'default_impl' in client._closed


# Generated at 2022-06-22 13:20:56.640169
# Unit test for function main
def test_main():
    import tornado.testing
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web
    import tornado.httpclient
    import tornado.httputil
    import tornado.netutil
    import tornado.escape
    import socket
    import sys
    import urllib.parse
    import enum
    import time
    
    if sys.version_info < (3, 5):
        sys.exit("This test must be run with python3")

    import tornado.testing
    
    
    
    
    
    
    
    
    
    
    class _TestHTTPResponse(HTTPResponse):
        def __init__(self, *args, **kwargs):
            super(_TestHTTPResponse, self).__init__(*args, **kwargs)
            self.closed = False

   

# Generated at 2022-06-22 13:21:05.276844
# Unit test for constructor of class HTTPResponse
def test_HTTPResponse():
    request = HTTPRequest(url = "")
    response = HTTPResponse(request = request, code = 200)
    assert response.body == b""
    assert response.request == request
    assert response.code == 200
    assert response.time_info == {}
    assert response.start_time is None
    assert response.request_time is None
    assert response.error is None
    assert response.headers == httputil.HTTPHeaders()
    assert response.reason == "Unknown"
    assert response.effective_url == request.url
    assert not response._error_is_response_code



# Generated at 2022-06-22 13:21:05.681345
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    pass

# Generated at 2022-06-22 13:21:16.766461
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import sys


    # __new__ should look in the cache
    origin_instance_cache = AsyncHTTPClient._async_clients()
    ioloop = IOLoop()
    client1 = AsyncHTTPClient(force_instance=True)
    client2 = AsyncHTTPClient()
    assert origin_instance_cache == {ioloop: client1, IOLoop.current(): client2}
    assert client1 is not client2
    assert client1.io_loop is ioloop
    assert client2.io_loop is IOLoop.current()
    client1.close()
    client1 = AsyncHTTPClient(force_instance=True)
    assert client1.io_loop is not ioloop
    assert origin_instance_cache == {IOLoop.current(): client2}
    client2.close()

# Generated at 2022-06-22 13:21:27.270858
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import asyncio
    from tornado.escape import json_decode
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import Application, RequestHandler
    from tornado.httpclient import AsyncHTTPClient
    def get_app():
        class HelloHandler(RequestHandler):
            def get(self):
                self.write("Hello world")
        return Application([("/", HelloHandler)])
    class HTTPClientTest(AsyncHTTPTestCase):
        def test_fetch(self):
            client = AsyncHTTPClient()
            value = json_decode(client.fetch(self.get_url("/")).body)
            self.assertEqual(value, "Hello world")
    test = HTTPClientTest()
    test.test_fetch()


# Generated at 2022-06-22 13:21:38.041689
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

# Generated at 2022-06-22 13:21:40.786392
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close(): 
    # test_AsyncHTTPClient_close()
    AsyncHTTPClient().close() 

# Generated at 2022-06-22 13:21:47.977638
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    # test for method __new__(self, force_instance=False, **kwargs) of class AsyncHTTPClient
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase, bind_unused_port
    from tornado.web import RequestHandler, Application
    import tornado.httpserver

    class HelloHandler(RequestHandler):
        def get(self):
            self.finish("Hello")

    class HTTPClientCommonTestCase(AsyncHTTPTestCase, LogTrapTestCase):

        def test_async_http_client_singleton(self):
            app = Application([("/", HelloHandler)])
            self.http_client = AsyncHTTPClient(self.io_loop)
            self.http_client.fetch(self.get_url("/"), self.stop)
            response = self.wait()
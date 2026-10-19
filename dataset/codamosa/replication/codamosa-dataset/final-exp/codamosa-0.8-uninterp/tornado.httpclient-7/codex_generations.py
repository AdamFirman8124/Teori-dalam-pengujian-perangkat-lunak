

# Generated at 2022-06-22 13:15:20.719724
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    import pytest
    import tornado
    import tornado.simple_httpclient

    def check_close(AsyncHTTPClient):
        future_cache = AsyncHTTPClient._instance_cache[IOLoop.current()]
        future_cache.close()
        assert "closed" in repr(future_cache)
        assert future_cache._closed == True

    @gen.coroutine
    def test_gen_close(AsyncHTTPClient):
        future = AsyncHTTPClient.fetch('http://www.google.com')
        future.close()
        assert "closed" in repr(future)
        assert future._closed == True

    @gen.coroutine
    def test_gen_arguments_close(AsyncHTTPClient):
        future = AsyncHTTPClient.fetch('http://www.google.com', method='GET')
        future.close()

# Generated at 2022-06-22 13:15:32.637475
# Unit test for function main
def test_main():
    import sys
    from tornado.options import define, options
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase

    define("print_infos", type=bool, default=False)
    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)

    class MainTest(AsyncHTTPTestCase, LogTrapTestCase):  # type: ignore
        def get_app(self):
            # type: () -> web.Application
            return web.Application()


# Generated at 2022-06-22 13:15:43.769780
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tensorflow as tf
    assert isinstance(tf.test.is_gpu_available(), bool)
    input_shape = (2, 3)
    x = tf.constant([[1.1, 1.2, 1.3], [1.1, 1.2, 1.3]], shape=input_shape)
    y = tf.constant([[2.1, 2.2, 2.3], [2.1, 2.2, 2.3]], shape=input_shape)
    z = x + y
    assert z.shape == (2, 3)
    assert tf.reduce_sum(z) == 12.6
    opt = tf.keras.optimizers.Adam(0.1)
    with tf.GradientTape() as tape:
        tape.watch(x)
        pred = tf

# Generated at 2022-06-22 13:15:54.656744
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    """
    >>> http_client = httpclient.HTTPClient()
    >>> try:
    ...     response = http_client.fetch("http://www.google.com/")
    ...     print(response.body)
    ... except httpclient.HTTPError as e:
    ...     # HTTPError is raised for non-200 responses; the response
    ...     # can be found in e.response.
    ...     print("Error: " + str(e))
    ... except Exception as e:
    ...     # Other errors are possible, such as IOError.
    ...     print("Error: " + str(e))
    ... http_client.close()
    """

    pass



# Generated at 2022-06-22 13:15:57.151284
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    response = http_client.fetch("http://127.0.0.1:5555")
    print(response.body)


# Generated at 2022-06-22 13:16:04.506379
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    """Test for method close of class AsyncHTTPClient."""
    async def test_AsyncHTTPClient_close_async_instance():
        """Test for method close of class AsyncHTTPClient."""
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch("http://www.google.com/")
            print(response.body)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))
        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error: " + str(e))
        http_client.close()


# Generated at 2022-06-22 13:16:08.211993
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.httpclient import AsyncHTTPClient

    def exec_callback(a, b, c):
        print(a, b, c)
    client = AsyncHTTPClient()
    client.fetch_impl(exec_callback, exec_callback, exec_callback)


# Generated at 2022-06-22 13:16:15.143791
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    import tornado
    import tornado.testing
    import tornado.web
    import urllib
    import functools
    import tornado.escape

    @tornado.testing.gen_test
    def test_main():
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch("http://www.google.com/")
        print(response.body)



# Generated at 2022-06-22 13:16:26.270850
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    url = "http://example.com"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    cl = HTTPClient()
    def responder(request):
        assert request.method == 'GET'
        assert request.host == 'example.com:80'
        assert request.path == '/'
        headers = httputil.HTTPHeaders({
            "Content-Type": "text/html; charset=utf-8"
        })
        with open(os.path.join(os.path.dirname(__file__), "hello.html"), "rb") as f:
            content = f.read()
        return HTTPResponse(request, 200, headers=headers, buffer=BytesIO(content))
    http_server = HTTPServer(responder)
    http_server.listen

# Generated at 2022-06-22 13:16:31.593426
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
    # or with force_instance:
    client = AsyncHTTPClient(force_instance=True, defaults=dict(user_agent="MyUserAgent"))
    class AsyncHTTPClient:
        def fetch_impl(self, request, callback):
            callback(request)
    a = AsyncHTTPClient()
    print(a.fetch_impl("ahoj", callback=None))

# Generated at 2022-06-22 13:16:39.337079
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:16:40.290375
# Unit test for function main
def test_main():
    pass


if __name__ == "__main__":
    test_main()

# Generated at 2022-06-22 13:16:50.619358
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.testing import AsyncHTTPTestCase
    from tornado import testing as test_modules
    from tornado import web as web_modules

    class DummyTestCase(AsyncHTTPTestCase):
        def get_app(self):
            return web_modules.Application([])
    dummy_test_case = DummyTestCase()

    http_client = AsyncHTTPClient(force_instance=True, defaults=dict(user_agent="MyUserAgent"))
    dummy_test_case.assertIsInstance(http_client, AsyncHTTPClient)

    # call __new__ twice to make sure we don't leak instances
    http_client1 = AsyncHTTPClient(force_instance=True, defaults=dict(user_agent="MyUserAgent"))
    dummy_test_case.assertIsInstance(http_client1, AsyncHTTPClient)

    # Make sure

# Generated at 2022-06-22 13:16:56.676467
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.concurrent import Future
    from tornado.httpclient import HTTPResponse
    from tornado.httputil import HTTPHeaders
    from tornado.ioloop import IOLoop
    from tornado.simple_httpclient import SimpleAsyncHTTPClient

    def test_fetch_impl(max_clients=0, force_instance=False):
        io_loop = IOLoop()
        io_loop.make_current()

        client = SimpleAsyncHTTPClient(io_loop=io_loop)

        class Request(object):
            url = ''  # type: str
            headers = HTTPHeaders()  # type: HTTPHeaders
            allow_nonstandard_methods = False  # type: bool

            def __init__(self, url: str, **kwargs: Any) -> None:
                self.url = url

# Generated at 2022-06-22 13:17:07.182828
# Unit test for method close of class AsyncHTTPClient

# Generated at 2022-06-22 13:17:16.433629
# Unit test for function main

# Generated at 2022-06-22 13:17:28.360863
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    # self = object()
    method_name = "test_AsyncHTTPClient_close"
    self = super(AsyncHTTPClient, cls)
    if self._closed:
        raise RuntimeError("fetch() called on closed AsyncHTTPClient")
    if not isinstance(request, HTTPRequest):
        request = HTTPRequest(url=request, **kwargs)
    else:
        if kwargs:
            raise ValueError(
                "kwargs can't be used if request is an HTTPRequest object"
            )
    # We may modify this (to add Host, Accept-Encoding, etc),
    # so make sure we don't modify the caller's object.  This is also
    # where normal dicts get converted to HTTPHeaders objects.
    request.headers = httputil.HTTPHeaders(request.headers)

# Generated at 2022-06-22 13:17:31.489423
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    log.info("test_AsyncHTTPClient_initialize")
    instance = AsyncHTTPClient()
    del instance


# Generated at 2022-06-22 13:17:32.139815
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()



# Generated at 2022-06-22 13:17:42.840895
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.platform.asyncio import AsyncIOMainLoop
    import asyncio, pytest
    from tornado.httpclient import AsyncHTTPClient

    def run_sync(coro):
        """Run the given coroutine in a new event loop"""
        loop = AsyncIOMainLoop()
        asyncio.set_event_loop(loop)
        loop.make_current()
        return loop.run_sync(coro)

    async def test_close():
        http_client = AsyncHTTPClient(force_instance=True)
        assert http_client._closed == False
        http_client.close()
        assert http_client._closed == True

        http_client2 = AsyncHTTPClient(force_instance=True)
        assert http_client2._closed == False
        http_client2.close()
        assert http

# Generated at 2022-06-22 13:18:23.351981
# Unit test for function main
def test_main():
    import sys
    import logging
    from tornado.testing import get_async_test_timeout
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.httpclient import AsyncHTTPClient
    from tornado.ioloop import IOLoop

    # This test is a little awkward because it is testing an application
    # (fetch_url) instead of a library (httpclient).  Ideally we would
    # run cURL in a subprocess and test the output, but this is simpler
    # and more robust in the face of occasional flakes.
    url = "http://www.google.com/"
    client = AsyncHTTPClient()
    http_stream = client.fetch(url)

    def finished():
        response = http_stream.result()
        assert response.code == 200

# Generated at 2022-06-22 13:18:34.200372
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.http1connection import HTTP1Connection

    class MyAsyncHTTPClient(AsyncHTTPClient):
        def __init__(self, **kwargs):
            super(self.__class__, self).__init__(**kwargs)
            self.conn = HTTP1Connection()

        def fetch_impl(self, request, callback):
            # `self.conn` is just a fake. We don't want to test
            # `HTTP1Connection` here, though.
            self.conn.request(request, callback)
    request = HTTPRequest('http://www.baidu.com/')
    c = MyAsyncHTTPClient()
    c.fetch_impl(request, lambda response: response)



# Generated at 2022-06-22 13:18:34.764527
# Unit test for function main
def test_main():
    main()
    print("Success")


# Generated at 2022-06-22 13:18:36.705856
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    class Test(AsyncHTTPClient):
        def configure(self):
            pass
        def fetch(self):
            pass
    _=Test()
    _.initialize()

# Generated at 2022-06-22 13:18:46.903308
# Unit test for function main
def test_main():
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    try:
        from tornado.options import Options
        from tornado.test.util import unittest
        from tornado.test.util import SkipTest
        from unittest.mock import patch
    except ImportError:
        raise SkipTest("couldn't import module")

# Generated at 2022-06-22 13:18:47.325641
# Unit test for function main
def test_main():
    main()



# Generated at 2022-06-22 13:18:59.766684
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    from tornado import httpclient
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import Application, RequestHandler
    class MainHandler(RequestHandler):
        def get(self):
            self.write("Hello, world")
    class MyHTTPClient(httpclient.AsyncHTTPClient):
        def fetch(self, url, callback=None, **kwargs):
            proxy = _RequestProxy(HTTPRequest(url=url), kwargs)
            request_arg = proxy.request_timeout
            assert request_arg == 10, "request_arg==10"
            callback(HTTPResponse(proxy.request, 599, request_time=10))
    class MyTest(AsyncHTTPTestCase):
        def get_app(self):
            return Application([("/", MainHandler)])
        def test(self):
            client = My

# Generated at 2022-06-22 13:19:06.009351
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient

    assert not hasattr(AsyncHTTPClient, '_async_client_dict_AsyncHTTPClient')
    client = AsyncHTTPClient()
    assert isinstance(client, SimpleAsyncHTTPClient)
    assert hasattr(AsyncHTTPClient, '_async_client_dict_AsyncHTTPClient')


# Generated at 2022-06-22 13:19:08.055859
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    obj = AsyncHTTPClient()
    obj.close()
    assert obj._closed == True



# Generated at 2022-06-22 13:19:18.440372
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import tornado.web
    import tornado.ioloop
    import tornado.simple_httpclient
    import tornado.curl_httpclient
    from tornado.options import options
    from tornado.httpserver import HTTPServer

    test_fd, log_filename = tempfile.mkstemp()
    # Create a dummy request object to use in testing.

    def request_callback(response):
        response.rethrow()
        self.assertTrue(response.body.startswith("TEST"))
        self.io_loop.stop()

    def get_app():
        class MainHandler(tornado.web.RequestHandler):
            @gen.coroutine
            def get(self):
                if self.request.headers.get("Range") == "bytes=0-3":
                    self.set_status(206)

# Generated at 2022-06-22 13:19:38.024989
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    def test_function(self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]) -> None:
        raise NotImplementedError()

    my_asynchttpclient = AsyncHTTPClient()
    assert my_asynchttpclient is not None
    my_asynchttpclient.fetch_impl = test_function
    assert my_asynchttpclient is not None

# Generated at 2022-06-22 13:19:39.573928
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    client=AsyncHTTPClient
    client.initialize()

# Generated at 2022-06-22 13:19:41.130965
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # Python subclasses do not define methods like this.
    pass

# Generated at 2022-06-22 13:19:52.930107
# Unit test for constructor of class HTTPRequest
def test_HTTPRequest():
    url = "example.com"
    method = "POST"
    headers = {"User-Agent": "Mozilla/5.0"}
    body = "Hello, world!"
    auth_username = "username"
    auth_password = "password"
    auth_mode = "basic"
    connect_timeout = 15.0
    request_timeout = 15.0
    if_modified_since = 123
    follow_redirects = False
    max_redirects = 10
    user_agent = "example"
    use_gzip = False
    network_interface = "127.0.0.1"
    streaming_callback = lambda x: print(x)
    header_callback = lambda x: print(x)
    prepare_curl_callback = lambda x: print(x)
    proxy_host = "localhost"
   

# Generated at 2022-06-22 13:20:00.610910
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    io_loop = IOLoop.current()
    client = AsyncHTTPClient(force_instance=True)
    client.initialize()
    assert client.io_loop is io_loop
    assert client.defaults == HTTPRequest._DEFAULTS
    assert client._closed is False

    defaults = dict(user_agent="MyUserAgent")
    client.initialize(defaults=defaults)
    assert client.defaults == HTTPRequest._DEFAULTS.copy()
    assert client.defaults["user_agent"] == "MyUserAgent"



# Generated at 2022-06-22 13:20:08.653497
# Unit test for function main
def test_main():
    args = "http://www.example.com"
    client = HTTPClient()
    for arg in args.split():
        try:
            response = client.fetch(arg)
        except HTTPError as e:
            if e.response is not None:
                response = e.response
            else:
                raise
        if options.print_headers:
            print(response.headers)
        if options.print_body:
            print(native_str(response.body))
    client.close()


# Generated at 2022-06-22 13:20:12.062149
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    response = None
    callback = lambda response: response
    request = HTTPRequest(url='')
    AsyncHTTPClient.fetch_impl(request, callback)



# Generated at 2022-06-22 13:20:15.672381
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    req = HTTPRequest(url="http://127.0.0.1:5000/")
    reqp = _RequestProxy(request=req, defaults={"method": "GET"})
    assert reqp.url == req.url
    assert reqp.method == "GET"

# Generated at 2022-06-22 13:20:20.666866
# Unit test for function main
def test_main():
    args = ['https://www.baidu.com', 'https://www.baidu.com']
    try:
        main()
    except NotImplementedError:
        assert False
test_main()


# Generated at 2022-06-22 13:20:21.731009
# Unit test for function main
def test_main():
    pass
#Unit test for member function __init__

# Generated at 2022-06-22 13:22:11.800419
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    a = AsyncHTTPClient()
    a.close()
    


# Generated at 2022-06-22 13:22:12.338312
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 13:22:13.260919
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    pass # TODO

# Generated at 2022-06-22 13:22:19.629737
# Unit test for function main
def test_main():
    import subprocess
    import tornado.options
    import os
    import pytest
    import tempfile
    from tornado.simple_httpclient import _DEFAULT_CA_CERTS
    from tornado.testing import bind_unused_port
    from tornado.test.util import unittest, skipIfNonUnix

    if os.environ.get("TRAVIS") == "true":
        # This can deadlock on the travis mac builder.
        # See https://github.com/tornadoweb/tornado/issues/1241
        pytest.skip()

    def verify_main(stdin_url, expected_code, expected_body):
        port, = bind_unused_port()

# Generated at 2022-06-22 13:22:20.522587
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:22:26.159376
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    class Request(object):
        def __init__(self, **kwargs):
            self._init_kwargs(kwargs)
        def _init_kwargs(self, _kwargs: Dict[str, Any]) -> None:
            for attr_name, attr_val in _kwargs.items():
                setattr(self, attr_name, attr_val)
    request = Request(attr1='attr1_val', attr2='attr2_val')
    defaults = {'default_attr': 'default_attr_val'}
    requestProxy = _RequestProxy(request, defaults)
    assert requestProxy.attr1 == 'attr1_val'
    assert requestProxy.attr2 == 'attr2_val'
    assert requestProxy.default_attr == 'default_attr_val'

# Generated at 2022-06-22 13:22:38.738673
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    #! /usr/bin/env python
    # Copyright (c) 2014-present, Facebook, Inc.
    # All rights reserved.
    #
    # This source code is licensed under the BSD-style license found in the
    # LICENSE file in the root directory of this source tree. An additional grant
    # of patent rights can be found in the PATENTS file in the same directory.
    #
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    from mcurl.async_http_client import AsyncHTTPClient
    from mcurl.httputil import HTTPRequest
    import tornado.testing
    class AsyncHTTPClientMock(AsyncHTTPClient):
        def __init__(self):
            self.fetched = [] 

# Generated at 2022-06-22 13:22:39.755694
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    http = HTTPClient()
    return http


# Generated at 2022-06-22 13:22:43.577158
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    try:
        from tornado.httpclient import AsyncHTTPClient
        client = AsyncHTTPClient()
        def callback(response):
            pass
        client.fetch_impl('time', callback)
        client.close()
    except:
        pass



# Generated at 2022-06-22 13:22:53.100723
# Unit test for function main
def test_main():
    import inspect
    import json
    import io
    
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    test_vars = json.load(open(filename + '.testvars.json'))
    
    sys_argv = sys.argv
    sys.argv = test_vars['sys.argv']
    out_capture = io.StringIO()
    sys.stdout = out_capture
    main()
    main_out = out_capture.getvalue()
    assert test_vars['main_out'] == main_out
    sys.argv = sys_argv

if __name__ == "__main__":
    main()
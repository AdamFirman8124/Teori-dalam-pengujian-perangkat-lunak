

# Generated at 2022-06-22 13:15:08.197062
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    async_client = AsyncHTTPClient()
    async_client.close()


# Generated at 2022-06-22 13:15:08.811988
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass


# Generated at 2022-06-22 13:15:10.615338
# Unit test for function main
def test_main():
    pass

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:17.621427
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():

    @gen.coroutine
    def f():
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch("http://www.google.com")
        except Exception as e:
            print("Error: %s" % e)
        else:
            print(response.body)

    f()



# Generated at 2022-06-22 13:15:18.984718
# Unit test for function main
def test_main():
    # this is the module level docstring
    main()

# Generated at 2022-06-22 13:15:24.695624
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    '''
    Unit test for method fetch of class HTTPClient
    '''
    http_client = HTTPClient()
    # Unit test for exception
    try:
        response = http_client.fetch("http://www.google.com/", raise_error=False)
        print(response.body)
    except HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    finally:
        http_client.close()



# Generated at 2022-06-22 13:15:26.611306
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    http_client = AsyncHTTPClient()
    http_client.close()



# Generated at 2022-06-22 13:15:29.742399
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    c = SimpleAsyncHTTPClient()
    c.initialize()


# Generated at 2022-06-22 13:15:37.761298
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    # Create a dummy request object
    request = HTTPRequest(url="https://www.google.com/")
    # Create a dummy response object
    response = HTTPResponse(request, 200, headers=None, buffer=None, effective_url=None)
    # Check that there is no error in the response object
    assert response.error == None
    # Check that response.rethrow() does nothing
    response.rethrow()
    # Check that a TypeError is raised if rethrow is called with an invalid argument
    with pytest.raises(TypeError):
        response.rethrow(None)
"""Test that the __repr__ method of class HTTPResponse does not raise any exceptions and returns a string"""

# Generated at 2022-06-22 13:15:38.161587
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass

# Generated at 2022-06-22 13:16:19.171047
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    test_main()

# Generated at 2022-06-22 13:16:19.883566
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-22 13:16:22.670925
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    with pytest.raises(NotImplementedError):
        AsyncHTTPClient().initialize()

a1 = test_AsyncHTTPClient_initialize()


# Generated at 2022-06-22 13:16:27.491074
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    http_client = HTTPClient()
    try:
        response = http_client.fetch("http://www.google.com/")
        print(response.body)
    except httpclient.HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    http_client.close()



# Generated at 2022-06-22 13:16:37.139621
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    configurable = None # type: Configurable
    callback = None # type: Callable[["HTTPResponse"], None]
    def test_AsyncHTTPClient_fetch_impl_impl(self, request, callback):
        return self.fetch_impl(request, callback)
    globals()['test_AsyncHTTPClient_fetch_impl_impl'] = test_AsyncHTTPClient_fetch_impl_impl.__get__(configurable, AsyncHTTPClient)
    globals()['test_AsyncHTTPClient_fetch_impl_impl'](request, callback)
    del globals()['test_AsyncHTTPClient_fetch_impl_impl']


_DEFAULT_CA_CERTS = None



# Generated at 2022-06-22 13:16:44.026849
# Unit test for function main
def test_main():
    import sys
    import unittest
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase
    from tornado.web import RequestHandler, Application

    class HelloWorldRequestHandler(RequestHandler):
        def get(self):
            self.write("Hello world")

    class HelloWorldRedirectHandler(RequestHandler):
        def get(self):
            self.redirect("/")

    class MainTest(AsyncHTTPTestCase, LogTrapTestCase):
        def get_app(self):
            return Application([("/", HelloWorldRequestHandler),
                                ("/redirect", HelloWorldRedirectHandler)])

        def test_main(self):
            real_stdout = sys.stdout

# Generated at 2022-06-22 13:16:44.877927
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    pass



# Generated at 2022-06-22 13:16:53.089284
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import time
    import datetime
    from tornado.concurrent import Future
    from tornado.escape import utf8, native_str
    from tornado import gen, httputil, httpclient
    from tornado.ioloop import IOLoop
    from tornado.util import Configurable
    #from tornado import simple_httpclient
    from tornado.test.util import unittest, skipOnTravis

    from typing import Type, Any, Union, Dict, Callable, Optional, cast
    #from typing import List, Tuple, Optional, Any, Generator, Callable, Type, Union
    #from typing import List, Tuple, Optional, Any, Generator, Callable, Type, Union



# Generated at 2022-06-22 13:17:01.759950
# Unit test for function main
def test_main():
    orig_logging = logging.info
    def fake_logging(msg, *args, **kwargs):
        orig_logging(msg, *args, **kwargs)
        fake_logging.logs.append(msg)
    fake_logging.logs = []
    try:
        logging.info = fake_logging
        main()
    finally:
        logging.info = orig_logging
    assert fake_logging.logs and "Asynchronous HTTP client" in fake_logging.logs[0]

# Generated at 2022-06-22 13:17:12.385352
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    if get_version() < "5.0":
        raise SkipTest("AsyncHTTPClient is only available in Tornado 5.0+")
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    # Class AsyncHTTPClient can be instantiated
    client1 = AsyncHTTPClient()
    assert isinstance(client1, AsyncHTTPClient)
    assert isinstance(client1, SimpleAsyncHTTPClient)
    # Class AsyncHTTPClient has a class member _async_client_dict_AsyncHTTPClient
    assert hasattr(AsyncHTTPClient, "_async_client_dict_AsyncHTTPClient")
    assert isinstance(
        AsyncHTTPClient._async_client_dict_AsyncHTTPClient, weakref.WeakKeyDictionary
    )
    # Class AsyncHTTPClient has an instance member _async_client_dict_SimpleAsyncHTTPClient


# Generated at 2022-06-22 13:17:45.992633
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import sys
    import os.path
    from tornado_py3.concurrent import TracebackFuture
    from tornado_py3.ioloop import IOLoop
    from tornado_py3.platform.asyncio import AsyncIOMainLoop
    if sys.platform == 'win32':
        print("AsyncIOMainLoop is not supported on %s" % sys.platform)
        return
    AsyncIOMainLoop().install()
    io_loop = IOLoop()
    io_loop.make_current()
    b = AsyncHTTPClient()
    assert isinstance(b, AsyncHTTPClient)
    assert isinstance(b, Configurable)
    assert isinstance(b.defaults, dict)
    assert isinstance(b._closed, bool)
    b.initialize()
    assert b._closed is False

# Generated at 2022-06-22 13:17:57.256541
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.httpclient import _RequestProxy
    
    import asyncio
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.httputil import HTTPServerRequest, HTTPResponse
    from tornado.concurrent import TracebackFuture

    class FatalClientException(Exception):
        pass

    class CaptureTask(asyncio.Task):

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.exc_info = None  # type: Any #mypy TODO
            super(CaptureTask, self).__init__(*args, **kwargs)

        def cancel(self) -> bool:
            if self.exc_info is None:
                self.exc_info = sys.exc_info()
            return super(CaptureTask, self).c

# Generated at 2022-06-22 13:17:59.174239
# Unit test for function main
def test_main():
    pass


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:18:08.297199
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import unittest
    
    class AsyncHTTPClientTest(unittest.TestCase):
        def test_fetch_impl(self):
            url = "http://www.google.com"
            request = HTTPRequest(url)
            def callback(response):
                pass
            # AsyncHTTPClient inherit from Configurable
            instance = AsyncHTTPClient()
            result = instance.fetch_impl(request, callback)


    unittest.main()

if __name__ == "__main__":
    test_AsyncHTTPClient_fetch_impl()

# Generated at 2022-06-22 13:18:13.176703
# Unit test for constructor of class HTTPRequest

# Generated at 2022-06-22 13:18:16.965101
# Unit test for function main
def test_main():
    main()


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:18:19.023442
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    l = AsyncHTTPClient()
    l.initialize()
    l.close()
    l.fetch_impl()

# Generated at 2022-06-22 13:18:24.501765
# Unit test for function main
def test_main():
    import sys
    import io
    from tornado.testing import AsyncHTTPTestCase

    class MainTest(AsyncHTTPTestCase):
        def get_app(self):
            return Application()

        def test_main(self):
            out = io.StringIO()
            original_stdout = sys.stdout
            sys.stdout = out
            try:
                main()
            finally:
                sys.stdout = original_stdout
            output = out.getvalue()
            self.assertIn(u'<html>', output)

    MainTest().test_main()
    print("Success of tornado.httpclient.main()")

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-22 13:18:31.669917
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    @gen.coroutine
    def f():
        http_client = AsyncHTTPClient()
        try:
            try:
                response = yield http_client.fetch("http://www.google.com")
            except Exception as e:
                print("Error: %s" % e)
            else:
                print(response.body)
        finally:
            http_client.close()
    IOLoop.current().run_sync(f)



# Generated at 2022-06-22 13:18:43.564902
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import random
    import string
    import unittest
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    class TestAsyncHTTPClient(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop.current()
            self.defaults = dict(HTTPRequest._DEFAULTS)
            self.defaults['user_agent'] = "MyUserAgent"
            kwargs = dict()
            kwargs['io_loop'] = self.io_loop
            kwargs['force_instance'] = True
            kwargs['defaults'] = dict(HTTPRequest._DEFAULTS)
            kwargs['defaults']['user_agent'] = "MyUserAgent"
            self.http_client = AsyncHTTPClient(**kwargs)

# Generated at 2022-06-22 13:19:17.480884
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.httputil import HTTPHeaders
    from tornado.ioloop import IOLoop

    client = AsyncHTTPClient()

    assert client is AsyncHTTPClient()
    assert client is not AsyncHTTPClient(force_instance=True)
    assert client._closed is False
    assert client.io_loop == IOLoop.current()

    client2 = AsyncHTTPClient(force_instance=True)
    assert client2 is not client
    assert client2._closed is False
    assert client2.io_loop == IOLoop.current()



# Generated at 2022-06-22 13:19:30.037467
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.ioloop import IOLoop
    from tornado.escape import native_str
    from tornado.httputil import HTTPHeaders
    request = HTTPRequest(
        url="https://www.baidu.com",
        headers=HTTPHeaders({"a": "b" }),
        validate_cert=False,
        proxy_host="127.0.0.1",
        proxy_port=9999,
        proxy_username="127.0.0.1",
        proxy_password="123456"
    )
    def callback(response):
        print("##########################################")
        print(response.code)
        # print(type(response))
        print(response.headers["Content-Length"])

# Generated at 2022-06-22 13:19:36.575624
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    class TestClass(AsyncHTTPClient):
        def fetch_impl(self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]) -> None:
            pass
    obj = TestClass()
    request = HTTPRequest(url='google.com')
    assert(obj.fetch_impl(request, None) == None)


# Generated at 2022-06-22 13:19:45.224897
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.util import Configurable

    class MyAsyncHTTPClient(Configurable, AsyncHTTPClient):
        pass

    class Test(AsyncTestCase):
        def test_fetch(self):
            @gen_test
            def test_function():
                AsyncHTTPClient.configure(MyAsyncHTTPClient)
                response = yield AsyncHTTPClient().fetch(HTTPRequest(url="http://www.google.com"))
                print(response.body.decode())
                yield response.release()
            test_function()



# Generated at 2022-06-22 13:19:45.995575
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass



# Generated at 2022-06-22 13:19:54.074906
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    assert isinstance(SimpleAsyncHTTPClient.configurable_default(), AsyncHTTPClient)

    # Make sure initialize() is not called as part of __init__
    class NoInitAsyncHTTPClient(AsyncHTTPClient):
        def initialize(self, **kwargs):
            raise Exception("initialize should not be called")

    # initialize() is called the first time the AsyncHTTPClient singleton
    # is created and cached, but not when the class is created or when
    # the singleton is retrieved later
    NoInitAsyncHTTPClient()
    NoInitAsyncHTTPClient.instance()



# Generated at 2022-06-22 13:20:03.136670
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    'Unit test for method close of class AsyncHTTPClient'
    from unittest.mock import patch
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    http_client = AsyncHTTPClient()
    assert http_client._instance_cache is not None
    assert http_client._instance_cache[IOLoop.current()] is http_client
    # Test that we don't crash if close() is called twice.
    http_client.close()
    assert http_client._closed
    with patch.object(SimpleAsyncHTTPClient, 'close', side_effect=Exception('close')) as close:
        http_client.close()
        assert close.called
    # Test that the cached _instance_cache is cleaned up eventually if an
    # instance is left around until the IOLoop is closed.
    http_client = AsyncHTTP

# Generated at 2022-06-22 13:20:06.569273
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    AsyncHTTPClient_obj = AsyncHTTPClient()
    if AsyncHTTPClient_obj.close():
        print(1)
    else:
        print(2)


# Generated at 2022-06-22 13:20:08.650821
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    httpclient.HTTPClient(async_client_class=None, max_clients=20, defaults=None)


# Generated at 2022-06-22 13:20:17.544023
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import tornado.httpserver

    print(id(AsyncHTTPClient()))
    print(id(AsyncHTTPClient()))
    assert AsyncHTTPClient() is AsyncHTTPClient()
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient()
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient()
    http_server = tornado.httpserver.HTTPServer(
        tornado.web.Application([]), io_loop=IOLoop.current()
    )
    print(id(AsyncHTTPClient()))
    print(id(AsyncHTTPClient()))
    assert AsyncHTTPClient() is AsyncHTTPClient()
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient()
    assert AsyncHTTPClient(force_instance=True) is not AsyncHTTPClient

# Generated at 2022-06-22 13:21:01.976883
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    aiohttpclient = AsyncHTTPClient()
    aiohttpclient.initialize()

# Generated at 2022-06-22 13:21:06.162432
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    fetchImpl = AsyncHTTPClient()
    try:
        fetchImpl.fetch_impl(HTTPRequest, None)
    except NotImplementedError:
        pass



# Generated at 2022-06-22 13:21:06.847542
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    pass

# Generated at 2022-06-22 13:21:10.341330
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    """
    
    Unit test for method close of class AsyncHTTPClient
    """
    test_AsyncHTTPClient = AsyncHTTPClient()
    test_AsyncHTTPClient.close()

# Generated at 2022-06-22 13:21:19.199175
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()
    # Method close of class AsyncHTTPClient called with arg client=AsyncHTTPClient
    # Instance of class AsyncHTTPClient has attribute _closed=True

    import io
    import os
    import sys

    import pycurl
    import unittest2

    try:
        import ssl  # type: ignore
    except ImportError:
        ssl = None

    from tornado.escape import utf8
    from tornado.httpclient import AsyncHTTPClient
    from tornado.platform.auto import Waker
    from tornado.testing import AsyncHTTPTestCase, AsyncTestCase, bind_unused_port
    from tornado.test.util import unittest, skipOnTravis, skipIfNonUnix
    from tornado.util import b, bytes_type

# Generated at 2022-06-22 13:21:21.007175
# Unit test for function main
def test_main():
    pass



# Generated at 2022-06-22 13:21:25.099492
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest('','')

# Generated at 2022-06-22 13:21:31.472496
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world")
            http_client = tornado.httpclient.AsyncHTTPClient()
            response = await http_client.fetch("https://www.google.com/")
            print(response.body)

    if __name__ == "__main__":
        app = tornado.web.Application([(r"/", MainHandler)])
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()



# Generated at 2022-06-22 13:21:43.843084
# Unit test for function main
def test_main():
    # tornado.testing.gen_test()
    import tornado.ioloop
    import tornado.testing
    import time
    import unittest
    import functools
    import socket
    # import urllib
    import http.client
    # import urllib.parse
    import urllib3.util
    import urllib3
    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.httputil import url_concat
    from tornado.httpserver import HTTPServer
    from tornado.netutil import bind_sockets
    from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase, httpclient_test
    from tornado.test.util import unittest, skipOnTravis
    from tornado.util import b, bytes_type


# Generated at 2022-06-22 13:21:53.946669
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import pytest
    import tornado
    from tornado.concurrent import Future
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import RequestHandler, Application
    
    class MainHandler(RequestHandler):
        def get(self):
            self.write("Hello, world")
    
    class SimpleServerTest(AsyncHTTPTestCase):
        def get_app(self):
            return Application([("/", MainHandler)])
    
        def test_simple_request(self):
            response = self.fetch("/")
            self.assertEqual(response.body, b"Hello, world")
    

# Generated at 2022-06-22 13:23:55.006829
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    # ...
    pass


# Generated at 2022-06-22 13:24:03.885811
# Unit test for function main
def test_main():
    import sys
    import os
    import json
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.test.util import unittest, skipOnTravis, skipIfNoNetwork
    from tornado.web import RequestHandler
    from tornado.httpserver import HTTPServer
    from tornado import gen, httpclient, ioloop
    from tornado.options import define, options
    import functools
    import threading
    import socket
    import logging
    import time
    import shutil
    import tempfile
    import subprocess
    import signal
    import errno
    import urllib
    import ssl
    import concurrent.futures
    import pprint
    import base64
    import warnings
    import email.utils
    from tornado.platform.asyncio import to_unicode, AsyncIOMainLoop


# Generated at 2022-06-22 13:24:06.173696
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = mock.Mock(HTTPRequest)
    defaults = {'request': mock.Mock(HTTPRequest), 'defaults': None}
    _RequestProxy(request, defaults)



# Generated at 2022-06-22 13:24:07.290532
# Unit test for function main
def test_main():
  main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:24:10.876855
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    client = AsyncHTTPClient()
    assert client.io_loop is not None
    assert client.defaults is not None
    assert client._closed is False
test_AsyncHTTPClient_initialize()


# Generated at 2022-06-22 13:24:14.518467
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    assertionError = AssertionError("Method fetch_impl not yet implemented")
    try:
        raise assertionError
    except AssertionError:
        print("test_AsyncHTTPClient_fetch_impl failed")

# Generated at 2022-06-22 13:24:21.169771
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import asyncio
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.httpclient import HTTPResponse
    from tornado.testing import AsyncHTTPTestCase, gen_test
    # 
    class A(AsyncHTTPTestCase):
        def test_a(self):
            return AsyncHTTPClient().fetch("https://www.google.com")
    a = A()
    print(a.test_a())
    
    
    


# Generated at 2022-06-22 13:24:30.408701
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    import datetime
    from tornado.gen import coroutine
    from tornado.httputil import HTTPHeaders
    from tornado.httpclient import HTTPRequest, HTTPResponse
    from tornado.testing import AsyncHTTPTestCase
    from tornado.testing import gen_test
    from tornado.web import Application
    from tornado.web import RequestHandler
    class MainHandler(RequestHandler):
        def get(self):
            self.write("Hello, world")
    class _RequestProxyTestCase(AsyncHTTPTestCase):
        def get_app(self):
            return Application([("/", MainHandler)])
        @gen_test
        def test_RequestProxy(self):
            url = self.get_url("/")

# Generated at 2022-06-22 13:24:34.574698
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest(
    url="www"
    )
    reqProxy = _RequestProxy(request,{
        "code":20,
        "url": "www"
    })
    print(reqProxy.code)

# Generated at 2022-06-22 13:24:38.719197
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.curl_httpclient import AsyncHTTPClient

    # close a client with its io_loop
    client = AsyncHTTPClient()
    client.close()
    assert client._closed
    # close a client with another io_loop (should not crash)
    client = AsyncHTTPClient()
    client.close()
    assert client._closed


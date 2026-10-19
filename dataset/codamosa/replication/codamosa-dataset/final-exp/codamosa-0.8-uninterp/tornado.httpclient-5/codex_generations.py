

# Generated at 2022-06-22 13:15:19.873558
# Unit test for function main
def test_main():
    from tornado import testing
    from tornado.testing import AsyncTestCase, AsyncHTTPTestCase, LogTrapTestCase, get_unused_port
    from tornado.httpclient import HTTPRequest, AsyncHTTPClient, HTTPResponse
    from tornado.httpclient import HTTPError, HTTPClientError
    from tornado.curl_httpclient import CurlAsyncHTTPClient, _DEFAULT_CA_CERTS

    import os
    import shutil
    import socket
    import sys
    import time
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    class MainTest(AsyncHTTPTestCase, LogTrapTestCase):
        def get_app(self):
            return None

        # Testing async functionality requires the full HTTP server


# Generated at 2022-06-22 13:15:31.452913
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    """
        Main method to test AsyncHTTPClient.__new__
        Returns:
            None
    """
    print('Start Test')
    _instance_cache = None
    _instance_cache = AsyncHTTPClient._instance_cache
    # _instance_cache = None
    _instance_cache = weakref.WeakKeyDictionary()
    AsyncHTTPClient._instance_cache = _instance_cache
    # self._async_client_dict_AsyncHTTPClient = weakref.WeakKeyDictionary()
    force_instance = True
    # instance_cache = None
    instance_cache = AsyncHTTPClient._async_clients()
    if instance_cache is not None and ioloop.IOLoop.current() in instance_cache:
        return instance_cache[ioloop.IOLoop.current()]
    instance = Async

# Generated at 2022-06-22 13:15:39.540477
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import tornado.httpclient

# Generated at 2022-06-22 13:15:40.202938
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass



# Generated at 2022-06-22 13:15:41.660604
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    a = AsyncHTTPClient()
    a.initialize()


# Generated at 2022-06-22 13:15:52.100493
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    print('unit test: start')
    try:
        impl = 'tornado.curl_httpclient.CurlAsyncHTTPClient'
        request = HTTPRequest()
        callback = lambda response: print('response.error: ', response.error)
        AsyncHTTPClient.configure(impl)
        client = AsyncHTTPClient()
        client.fetch_impl(request, callback)
    except NotImplementedError as err:
        print('test_AsyncHTTPClient_fetch_impl: ', err)
    finally:
        client.close()
    print('unit test: end')


# Generated at 2022-06-22 13:15:52.913580
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    pass

# Generated at 2022-06-22 13:15:56.496707
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    close_test = AsyncHTTPClient()
    close_test.close()
    #assert close_test._closed = True
    assert close_test._closed is True 


# Generated at 2022-06-22 13:15:58.134327
# Unit test for function main
def test_main(): pass  # pragma: no cover


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:16:09.667993
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    # test for __init__ of httpclient.HTTPClient
    async def make_client():
        return httpclient.AsyncHTTPClient()
    http_client = httpclient.HTTPClient()
    assert isinstance(http_client, httpclient.HTTPClient)
    # test for closed
    assert http_client._closed == False
    # test for self._io_loop
    assert isinstance(http_client._io_loop, tornado.ioloop.IOLoop)
    # test for self._async_client
    assert isinstance(http_client._async_client, httpclient.AsyncHTTPClient)
    # test for fetch
    response = http_client.fetch("http://www.google.com/")
    assert isinstance(response, httpclient.HTTPResponse)


# Generated at 2022-06-22 13:16:23.017739
# Unit test for function main
def test_main():
    # testing if options.follow_redirects is False
    try:
        with mock.patch.object(HTTPClient, 'fetch', return_value=True) as mock_method:
            HTTPClient().fetch(None, follow_redirects=False, validate_cert=True, proxy_host=None, proxy_port=None)
            mock_method.assert_called_once_with(None, follow_redirects=False, validate_cert=True, proxy_host=None, proxy_port=None)
    except HTTPError:
        pass



# Generated at 2022-06-22 13:16:31.918271
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import unittest
    import tornado

    from tornado.testing import AsyncHTTPTestCase
    from tornado.test.util import unittest

    from tornado.httpclient import AsyncHTTPClient, HTTPRequest
    from tornado.httputil import HTTPHeaders

    def fetch(self, request, callback):
        # type: (AsyncHTTPClient, HTTPRequest, Callable[[HTTPResponse], None]) -> None
        if request.url == "http://www.google.com":
            callback(HTTPResponse(request, 304))
        else:
            callback(HTTPResponse(request, 404))

# Generated at 2022-06-22 13:16:42.443048
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    def test_AsyncHTTPClient_fetch_impl():
        def test_AsyncHTTPClient_fetch_impl():
            def test_AsyncHTTPClient_fetch_impl():
                def test_AsyncHTTPClient_fetch_impl():
                    class TestAsyncHTTPClient(AsyncHTTPClient):
                        pass
                    TestAsyncHTTPClient.configure(
                        'tornado.curl_httpclient.CurlAsyncHTTPClient')
                    impl = TestAsyncHTTPClient()
                    request = HTTPRequest('http://www.google.com')
                    callback = lambda x: True
                    try:
                        impl.fetch_impl(request, callback)
                    except NotImplementedError:
                        pass
                    else:
                        raise AssertionError("Error: fetch_impl not implemented")



# Generated at 2022-06-22 13:16:45.588845
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # (self: AsyncHTTPClient, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None
    pass

# Generated at 2022-06-22 13:16:53.237782
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    from tornado.httpclient import HTTPRequest, AsyncHTTPClient, HTTPResponse
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.ioloop import IOLoop

    def test_fetch():
        global count
        count += 1
        http_client = AsyncHTTPClient()

# Generated at 2022-06-22 13:16:57.566306
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    req = HTTPRequest('www.google.com')
    res = HTTPResponse(req, code = 404)

    with pytest.raises(HTTPError):
        res.rethrow()


# Generated at 2022-06-22 13:17:02.328104
# Unit test for function main
def test_main():
    # these calls to parse_command_line() are required because
    # _optdict will be overwritten by the next call
    from tornado.options import parse_command_line
    parse_command_line([])
    parse_command_line(['http://github.com'])
    main()


# Generated at 2022-06-22 13:17:12.643989
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import tornado.testing
    import tornado.web
    import tornado.websocket
    import tornado.httpserver
    import tornado.ioloop
    import tornado.httputil
    import tornado.httpclient
    import tornado.netutil
    import tornado.util
    import tornado.iostream
    import tornado.tcpserver
    import tornado.stack_context
    import tornado.locks
    import socket
    import functools
    import json
    import copy
    import warnings
    import datetime
    import pickle
    import sys
    import unittest
    from tornado.log import gen_log
    from tornado import gen
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.test.util import unittest
    from tornado.test.util import skipOnTravis

# Generated at 2022-06-22 13:17:16.113686
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest("http://www.google.com/")
    defaults = {'auth_username':'test'}
    request_proxy = _RequestProxy(request,defaults)
    assert request_proxy.auth_username == 'test'



# Generated at 2022-06-22 13:17:25.853903
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from os import getcwd
    from os.path import join as join_path
    from inspect import currentframe, getframeinfo
    from tornado.httpclient import AsyncHTTPClient

    def test_fetch_impl():
        def test_case(kwargs):
            print("Testing Case {}".format(kwargs))
            return AsyncHTTPClient()


# Generated at 2022-06-22 13:17:33.891027
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    future = Future()
    a = AsyncHTTPClient()
    a.close()
    print("Done")


# Generated at 2022-06-22 13:17:44.958225
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    """ test __new__ magic method, returns an instance of HTTPServer """
    DefaultProxy.host = "127.0.0.1"
    DefaultProxy.port = 9999
    DefaultProxy.proxyType = ProxyType.UNKNOWN
    DefaultProxy.user = ""
    DefaultProxy.password = ""
    DefaultProxy.rdns = True

    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test
    from tornado.platform.asyncio import AsyncIOMainLoop
    import asyncio
    import aiohttp

    AsyncIOMainLoop().install()

    class HTTPServer(AsyncHTTPClient):

        async def fetch_impl(
            self, request: HTTPRequest, callback: Callable[["HTTPResponse"], None]
        ) -> None:
            loop = asyncio.get_event_loop

# Generated at 2022-06-22 13:17:55.290983
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
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

__all__ = ["HTTPRequest", "HTTPResponse", "HTTPError", "AsyncHTTPClient", "HTTPClient"]

RequestStartLine = Type[httputil.RequestStartLine]



# Generated at 2022-06-22 13:18:04.328938
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    # test without any error
    request = HTTPRequest("http://localhost:80")
    response = HTTPResponse(
        request, 200, headers=[("Content-Type", "text")], buffer=io.BytesIO(b"")
    )
    response.rethrow()
    # test with error
    response = HTTPResponse(
        request, 300, headers=[("Content-Type", "text")], buffer=io.BytesIO(b"")
    )
    with pytest.raises(HTTPError):
        response.rethrow()



# Generated at 2022-06-22 13:18:15.946772
# Unit test for function main
def test_main():
    from tornado.options import define, options, parse_command_line, Error as OptionsError
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import RequestHandler, Application
    import os
    import sys
    import logging

    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)


# Generated at 2022-06-22 13:18:17.389374
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:18:19.567393
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    @gen.coroutine
    def test_fetch_impl():
        pass
    test_fetch_impl()


# Generated at 2022-06-22 13:18:23.290040
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    async def async_test():
        http_client = httpclient.HTTPClient()
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



# Generated at 2022-06-22 13:18:36.264330
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    from tornado.testing import gen_test, AsyncHTTPTestCase
    from tornado.web import Application, RequestHandler

    class MainHandler(RequestHandler):
        def get(self):
            self.write("Hello, world")

    class SyncHandler(RequestHandler):
        @gen.coroutine
        def get(self):
            # This can't be done with @gen.engine because we want
            # to be able to call self.stop().
            client = AsyncHTTPClient()
            response = yield client.fetch("http://127.0.0.1:%d/" % self.get_port())
            self.write(utf8(response.body))
            self.finish()

    class SyncHandlerWithRaise(RequestHandler):
        @gen.coroutine
        def get(self):
            client = AsyncHTTPClient()
           

# Generated at 2022-06-22 13:18:46.523893
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, gen_test
    from tornado.web import RequestHandler

    class HelloHandler(RequestHandler):
        def get(self):
            self.write("hello")

    class TestHandler(RequestHandler):
        def get(self):
            self.write("test")

    class TestMain(AsyncHTTPTestCase):
        def get_app(self):
            return Application([("/", HelloHandler), ("/test", TestHandler)])

        @gen_test
        def test_main(self):
            self.http_client.fetch(
                self.get_url("/"), self.stop, method="HEAD", body="Hello"
            )
            response = self.wait()
            self.assertEqual(200, response.code)
            self.assertEqual("", response.body)
           

# Generated at 2022-06-22 13:19:17.552733
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    """ Test that the method close of class AsyncHTTPClient
    can close the object"""
    new_object = AsyncHTTPClient(force_instance=True)
    # Test that the method close of class AsyncHTTPClient
    # can close the object
    new_object.close()



# Generated at 2022-06-22 13:19:30.116817
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, bind_unused_port
    from tornado.web import RequestHandler, Application
    from tornado.ioloop import IOLoop
    import urllib
    import os 
    import sys
    import base64
    import time
    import re
    import subprocess
    import shutil
    import select
    import signal
    import socket
    import urllib.parse
    import tempfile
    import json
    import threading
    import logging
    import errno
    import contextlib
    import unittest
    import functools
    import importlib
    import inspect
    import concurrent.futures
    global application
    global http_client
    global http_server
    class MainHandler(RequestHandler):
        def get(self):
            self.write("Hello, world")
   

# Generated at 2022-06-22 13:19:34.741549
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest("https://www.baidu.com")
    defaults = {"method":"post"}
    _req = _RequestProxy(request,defaults)
    print(_req.method)
    print(_req.request.method)
    print(request.method)


# Generated at 2022-06-22 13:19:37.917031
# Unit test for function main
def test_main():
    main()


# These classes are defined here rather than in ioloop.py so they can
# be imported by modules that import this module.

# Generated at 2022-06-22 13:19:39.038760
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass



# Generated at 2022-06-22 13:19:49.109245
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        return


if __name__ == "__main__":
    # Unit test for function main
    test_main()


# import itertools
# import ssl
# from typing import (
#     TYPE_CHECKING,
#     Any,
#     Dict,
#     Iterable,
#     List,
#     Optional,
#     Tuple,
#     Type,
#     Union,
# )
# from urllib.parse import (
#     ParseResult,
#     SplitResult,
#     urlsplit,
#     urlunsplit,
#     parse_qsl,
#     urlencode,
#     SplitResultBytes,
#     ParseResultBytes,
# )
#
# if TYPE_CHECKING:
#    

# Generated at 2022-06-22 13:19:56.398092
# Unit test for function main
def test_main():
    main()
    return True

if __name__ == "__main__":
    main()
    # Unit test for class SimpleAsyncHTTPClient
    class Test_SimpleAsyncHTTPClient(unittest.TestCase):
        def test_fetch_impl(self):
            my_httpclient = SimpleAsyncHTTPClient()
            self.assertEqual(my_httpclient.fetch_impl(HTTPRequest("localhost")), None)
    unittest.main()

# Generated at 2022-06-22 13:20:00.661169
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    test_AsyncHTTPClient = AsyncHTTPClient()
    test_HTTPRequest = HTTPRequest("http://www.google.com")
    test_callback = lambda response: None
    test_AsyncHTTPClient.fetch_impl(test_HTTPRequest, test_callback)


# Generated at 2022-06-22 13:20:02.411041
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    impl = AsyncHTTPClient()
    impl.close()


# Generated at 2022-06-22 13:20:03.910590
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
	AsyncHTTPClient.initialize()

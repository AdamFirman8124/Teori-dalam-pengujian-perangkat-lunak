

# Generated at 2022-06-22 13:15:13.091680
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    impl = AsyncHTTPClient()
    request = HTTPRequest()
    callback = lambda : None
    impl.fetch_impl(request, callback)


# Generated at 2022-06-22 13:15:15.012379
# Unit test for function main
def test_main():
    if __name__=="__main__":
        main()
        pass
    pass

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:19.202669
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    def callback(response):
        raise RuntimeError()
    request = HTTPRequest(url="test url")

    client = AsyncHTTPClient()
    try:
        client.fetch_impl(request, callback)
    except NotImplementedError:
        pass


# Generated at 2022-06-22 13:15:22.964645
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    hc = HTTPClient()
    resp = hc.fetch('http://www.google.com/')
    assert resp is not None
    assert resp.code == 200
    hc.close()
    hc.close() # can call multiple times without error

# Unit test class method close of HTTPClient

# Generated at 2022-06-22 13:15:28.067483
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    # Test 1: If there was an error on the request, raise an `HTTPError`
    # Since we use the actual method, we just need to test the error case
    # TODO

    # Test 2: If there is no error, do not raise an HTTPError
    # TODO
    return True

# Generated at 2022-06-22 13:15:38.086629
# Unit test for function main
def test_main():
    from tornado import testing
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.web import Application, RequestHandler
    from tornado.options import parse_command_line
    import tornado.testing

    class MainTest(tornado.testing.AsyncHTTPTestCase):
        def handle_request(self, _: RequestHandler) -> None:
            self.stop()

        def test_main(self) -> None:
            parse_command_line(
                [
                    "main_test",
                    "--print_headers=False",
                    "--print_body=False",
                    self.get_url("/"),
                ]
            )
            self.http_server = HTTPServer(Application())
            self.http_server.listen(0, "127.0.0.1")

# Generated at 2022-06-22 13:15:50.826592
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    from tornado.testing import AsyncHTTPTestCase
    import tornado.web
    from tornado.escape import url_escape
    # class AsyncHTTPClient_fetch_TestCase(AsyncHTTPTestCase):
    #     def test_async_http_client_fetch(self):
    #         response = self.fetch("/")
    #         self.assertEqual(response.body, b"Hello")
    #         response = self.fetch("/foo")
    #         self.assertEqual(response.body, b"Hello")
    #         response = self.fetch("/foo", method="HEAD")
    #         self.assertEqual(response.body, b"")
    #
    #     def get_app(self):
    #         class TestHandler(tornado.web.RequestHandler):
    #             def

# Generated at 2022-06-22 13:16:01.477966
# Unit test for constructor of class HTTPRequest

# Generated at 2022-06-22 13:16:03.367062
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    obj = AsyncHTTPClient()
    request = HTTPRequest('string_url_request')
    callback = lambda x: 1
    try:
        obj.fetch_impl(request, callback)
    except NotImplementedError as e:
        assert True
    else:
        assert False


# Generated at 2022-06-22 13:16:06.474758
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    stream = native_str(b'OK')
    impl = 'OK'

    response = AsyncHTTPClient.configure(
        impl=impl,
        # stream=stream,
        force_instance=False
    )

# Generated at 2022-06-22 13:16:17.146602
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():

    response = HTTPResponse(request, code, headers, buffer, effective_url, error)
    response.rethrow()


# Generated at 2022-06-22 13:16:27.408808
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
    for arg in args:
        response = client.fetch(
                arg,
                follow_redirects=options.follow_redirects,
                validate_cert=options.validate_cert,
                proxy_host=options.proxy_host,
                proxy_port=options.proxy_port,
            )

# Generated at 2022-06-22 13:16:34.893437
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    import time
    import random
    import string
    import types
    import sys
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    header_list = [
        {
            "Content-Length":"72"},
        
    ]
    header_dict = {}
    for header in header_list:
        header_dict.update(header)
    
    import httplib

# Generated at 2022-06-22 13:16:42.181054
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from unittest.mock import Mock
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    request = HTTPRequest("www.google.com", method="GET")
    callback = Mock()
    
    async_client = SimpleAsyncHTTPClient()
    async_client.fetch_impl(request, callback)
    request.body = None
    assert request.method == "GET"
    assert request.url == "www.google.com"
    callback.assert_called

# Generated at 2022-06-22 13:16:50.728193
# Unit test for function main
def test_main():
    # test main
    import os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, 'test')))
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import Application, RequestHandler
    class HelloHandler(RequestHandler):
        def get(self):
            self.write("hello")
    class HelloApp(Application):
        def __init__(self):
            handlers = [("/", HelloHandler)]
            Application.__init__(self, handlers)
    import logging
    logging.disable(logging.CRITICAL)
    class TestMain(AsyncHTTPTestCase):
        def get_app(self):
            return HelloApp()

# Generated at 2022-06-22 13:16:51.617395
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    pass


# Generated at 2022-06-22 13:16:56.417867
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    print("Test_AsyncHTTPClient")
    def test_close(self):
        self.http_client = AsyncHTTPClient()
        self.http_client.close()
        self.assertTrue(self.http_client._closed)

        # ensure close doesn't raise an exception if called twice
        self.http_client.close()
        self.assertTrue(self.http_client._closed)

        # ensure close doesn't raise an exception if called after
        # the actual close
        AsyncHTTPClient().close()
        self.assertTrue(self.http_client._closed)



# Generated at 2022-06-22 13:17:01.666048
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import tornado.httpclient
    import tornado.ioloop
    def handle_request(response):
        print(response.body)

    http_client = tornado.httpclient.AsyncHTTPClient()
    http_client.fetch("http://www.google.com", handle_request)
    tornado.ioloop.IOLoop.instance().start()


# Generated at 2022-06-22 13:17:07.730092
# Unit test for function main
def test_main():
    response = Mock()
    response.headers = "headers"
    response.body = b"body"
    client = Mock()
    client.fetch = Mock(return_value=response)
    with patch.object(httpclient, 'HTTPResponse', return_value=response):
        with patch.object(httpclient, 'HTTPClient', return_value=client):
            main()



# Generated at 2022-06-22 13:17:16.866937
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
  asyncio.set_event_loop(None)

  # Test that we don't double-close AsyncIO clients
  # because we had a close_all_clients() method in the
  # constructor and destructor that could get called if
  # the current IOLoop was not the same as the original
  # IOLoop.
  async def test_close_all_clients():
    # this is the same code that runs on module import
    # and when the module is reloaded.
    AsyncHTTPClient.configure(
      "tornado.platform.asyncio.AsyncIOMainLoop",
    )

    AsyncHTTPClient._instance_dict.clear()
    AsyncHTTPClient._instance_cache.clear()

    http_client = AsyncHTTPClient()

    assert http_client.io_loop is asyncio.get_

# Generated at 2022-06-22 13:17:23.412422
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    import unittest

    pass



# Generated at 2022-06-22 13:17:24.816504
# Unit test for function main
def test_main():
    main()
if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:17:37.726243
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    """
    Unit test for method rethrow of class HTTPResponse
    :return:
    """
    url = "www.cad.zju.edu.cn"
    method = "GET"
    request_timeout = 5
    auth_username = ""
    auth_password = ""
    auth_mode = "basic"
    follow_redirects = True
    max_redirects = 5
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    network_interface = ""
    validate_cert = True
    ca_certs = ""
    allow_ipv6 = True
    client_key = ""

# Generated at 2022-06-22 13:17:39.331962
# Unit test for function main
def test_main():
    pass

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:17:39.993028
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close(): pass

# Generated at 2022-06-22 13:17:40.885569
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass



# Generated at 2022-06-22 13:17:52.142264
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from asyncio import coroutine
    from typing import Dict
    from tornado.curl_httpclient import AsyncHTTPClient
    from tornado.httpserver import HTTPRequest, HTTPResponse
    import asyncio
    import pytest
    from tornado.ioloop import IOLoop

    @coroutine
    def fetch_impl(request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None:
        response = HTTPResponse(request, 200)
        callback(response)

    class MyAsyncHTTPClient(AsyncHTTPClient):
        def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None:
            fetch_impl(request, callback)


# Generated at 2022-06-22 13:17:53.478150
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass


# Generated at 2022-06-22 13:18:02.853842
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase, main
    from tornado.web import RequestHandler, Application

    class MainHandler(RequestHandler):
        def get(self):
            self.write("ok")

    class MainTest(AsyncHTTPTestCase):
        def get_app(self):
            return Application([('/', MainHandler)])

        def test_main(self):
            self.http_client.fetch(self.get_url('/'), self.stop)
            response = self.wait()
            self.assertEqual('ok', response.body)
    main()



# Generated at 2022-06-22 13:18:14.699804
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.platform.epoll import EPollIOLoop
    from tornado.platform.select import SelectIOLoop
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.test.util import unittest, skipIfNonUnix
    from tornado import testing
    from tornado import httpclient

    @unittest.skip("unreliable")
    def test_async_httpclient_close(self):
        for io_loop_class in [SelectIOLoop, EPollIOLoop]:
            io_loop = io_loop_class()
            io_loop.make_current()
            client = httpclient.AsyncHTTPClient()
            if io_loop_class is not SelectIOLoop:
                # force_instance=True
                self.assertTrue(client is httpclient.AsyncHTTPClient(force_instance=True))


# Generated at 2022-06-22 13:18:37.758441
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    pass


# Generated at 2022-06-22 13:18:41.298167
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    # check the AsyncHTTPClient instance.
    ahttp = AsyncHTTPClient()
    assert ahttp.defaults == HTTPRequest._DEFAULTS



# Generated at 2022-06-22 13:18:42.701014
# Unit test for function main
def test_main():
    import tornado.testing
    tornado.testing.main()


if __name__ == "__main__":
    #print(test_main())
    main()

# Generated at 2022-06-22 13:18:43.769089
# Unit test for function main
def test_main():
    # TODO Implement test function
    ...


# Generated at 2022-06-22 13:18:44.407992
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    pass

# Generated at 2022-06-22 13:18:52.281767
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    # line 2179
    print("unit test AsyncHTTPClient.fetch")
    # line 2180
    # line 2181
    # line 2182
    # line 2183
    # GET request
    url = "http://www.google.com"
    coro = client.fetch(url)
    resp = await coro
    assert resp.code == 200
    assert resp.body != b""
    assert "google.com" in resp.effective_url

    # HEAD request
    coro = client.fetch(url, method="HEAD")
    resp = await coro
    assert resp.code == 200
    assert resp.body == b""
    assert "google.com" in resp.effective_url

    # 404 with raise_error=False

# Generated at 2022-06-22 13:18:58.534847
# Unit test for function main
def test_main():
    from tornado.options import define, options, parse_command_line
    mock_object(tornado.options, 'define')
    mock_object(tornado.options, 'options')
    mock_object(tornado.options, 'parse_command_line')
    tornado.options.parse_command_line.return_value = ['a']
    tornado.options.options.follow_redirects = True
    tornado.options.options.validate_cert = True
    tornado.options.options.proxy_host = 'a'
    tornado.options.options.proxy_port = 80
    http_client = Mock()
    mock_object(tornado.httpclient, 'HTTPClient', http_client)
    http_error = Mock()
    http_error.response = Mock()
    client_fetch = http_client.fetch.side_

# Generated at 2022-06-22 13:19:02.094760
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    client = AsyncHTTPClient(IOLoop.current())
    assert client.fetch_impl(None, None) == NotImplementedError()
    return NotImplementedError



# Generated at 2022-06-22 13:19:03.640083
# Unit test for function main
def test_main():
    main()
if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:19:06.695555
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    import tornado.testing
    client = tornado.testing.AsyncHTTPClient(
        AsyncHTTPClient,
        defaults={"validate_cert": False}
    )
    client.close()

# Generated at 2022-06-22 13:19:40.820420
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import unittest
    from unittest.mock import Mock, patch
    from tornado.httpclient import AsyncHTTPClient

    class Dummy(object):
        def fetch_impl(
            self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]
        ) -> None:
            pass  # testing this method is not the purpose of this test case

    class TestCase(unittest.TestCase):
        @patch.object(Dummy, "fetch_impl")
        def test(self, mock):
            client = AsyncHTTPClient()
            client.fetch_impl(None, None)
            mock.assert_called_with(None, None)

    unittest.main()

# Generated at 2022-06-22 13:19:43.223716
# Unit test for function main
def test_main():
    assert main() == None


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:19:53.860411
# Unit test for function main
def test_main():
    pass
# This file was generated automatically by generate_protocols.py.
# Do not modify by hand.

import base64
import binascii
import collections.abc
import functools
import hashlib
import hmac
import io
import json
import logging
import os
import re
import socket
import time
import typing
import urllib.parse
from typing import Any, Callable, Dict, List, Optional, Pattern, Tuple, Union

from typing_extensions import Protocol

from tornado.concurrent import Future
from tornado.escape import utf8
from tornado.httpclient import HTTPClient

if False:
    from typing import _T

if typing.TYPE_CHECKING:
    from typing import NoReturn
    from typing_extensions import Literal


# Generated at 2022-06-22 13:20:05.654163
# Unit test for function main
def test_main():
    # mock command line argument
    sys.argv = ['main.py', 'http://www.wikipedia.org']
    from tornado.options import define, options, parse_command_line

    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)
    args = parse_command_line()
    client = HTTPClient()

# Generated at 2022-06-22 13:20:12.775980
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request_attr = _RequestProxy(None, None)
    # Test passing of arguments.
    if request_attr is not None:
        pass
    elif request_attr.defaults is not None:
        pass
    else:
        pass
    # Test passing of arguments.
    if request_attr is not None:
        pass
    elif request_attr.defaults is not None:
        pass
    else:
        pass



# Generated at 2022-06-22 13:20:13.833713
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    AsyncHTTPClient()


# Generated at 2022-06-22 13:20:18.578391
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = cast(AsyncHTTPClient, AsyncHTTPClient(force_instance=True))
    client.initialize(defaults=dict(user_agent="MyUserAgent"))
    client.close()
    client.close()
    client.close()


# Generated at 2022-06-22 13:20:19.812929
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    assert False, "FIXME"



# Generated at 2022-06-22 13:20:30.379952
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    proxy = _RequestProxy(request=HTTPRequest("https://www.baidu.com"),defaults={})
    assert(proxy.url == "https://www.baidu.com")
    assert(proxy.headers == httputil.HTTPHeaders())
    assert(proxy.body == b"")
    assert(proxy.body_producer is None)
    assert(proxy.proxy_host is None)
    assert(proxy.proxy_port is None)
    assert(proxy.proxy_username is None)
    assert(proxy.proxy_password is None)
    assert(proxy.proxy_auth_mode is None)
    assert(proxy.auth_username is None)
    assert(proxy.auth_password is None)
    assert(proxy.connect_timeout is None)
    assert(proxy.request_timeout is None)

# Generated at 2022-06-22 13:20:35.641419
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    impl = 'tornado.curl_httpclient.CurlAsyncHTTPClient'
    AsyncHTTPClient.configure(impl)
    http_client = AsyncHTTPClient()
    http_client.close()
    assert http_client._closed == True

# Generated at 2022-06-22 13:21:06.303173
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    log = logging.getLogger('test.AsyncHTTPClient.fetch_impl')
    log.info('start test_AsyncHTTPClient_fetch_impl')
    
    log.info('end test_AsyncHTTPClient_fetch_impl')

# Generated at 2022-06-22 13:21:12.089101
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.ioloop import IOLoop
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    ioloop = IOLoop()
    client = SimpleAsyncHTTPClient(io_loop=ioloop)
    assert client._closed == False
    client.close()
    assert client._closed == True
    client.close()
    assert client._closed == True


# Generated at 2022-06-22 13:21:14.724783
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # Method fetch_impl of class AsyncHTTPClient
    # is tested in AsyncHTTPClientTestCase.test_fetch
    pass

# Generated at 2022-06-22 13:21:17.110862
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase

    class MainTests(AsyncHTTPTestCase):
        def test_main(self):
            self.http_client.fetch(self.get_url('/'), self.stop)
            response = self.wait()
            self.assertEqual(response.code, 200)

    MainTests.__test__ = False
    MainTests().test_main()
# Unit tests for class AsyncHTTPClient

# Generated at 2022-06-22 13:21:21.299661
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    # TODO: Test raises error if no default argument is given and defaults is not None
    # TODO: Test fails if IOLoop is not current
    pass

# Generated at 2022-06-22 13:21:29.859034
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # 1. 实例化一个AsyncHTTPClient对象
    http_client = AsyncHTTPClient()
    # 2. 调用fetch_impl方法
    # http_client.fetch_impl()
    # 在AsyncHTTPClient中，fetch_impl方法抛出了NotImplementedError异常
    # 在SimpleAsyncHTTPClient中，fetch_impl方法没有实现，而会调用HTTPServerConnectionDelegate.fetch方法
    # 在SimpleAsyncHTTPClient中，fetch_impl方法没有实现，而会调用HTTPS

# Generated at 2022-06-22 13:21:30.764101
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass



# Generated at 2022-06-22 13:21:33.817254
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    with pytest.raises(RuntimeError) as e:
        AsyncHTTPClient().close()
    assert "AsyncHTTPClient" in str(e.value)

# Generated at 2022-06-22 13:21:36.399208
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()
    assert True


# Generated at 2022-06-22 13:21:43.984480
# Unit test for function main
def test_main():
    import sys, os
    sys.argv = ['', 'http://www.google.com', 'http://www.facebook.com']
    import tempfile
    fd, fn = tempfile.mkstemp()
    os.write(fd, 'test_main')
    os.close(fd)
    try:
        main()
        os.unlink(fn)
    except:
        os.unlink(fn)
        raise

# Unit tests for class HTTPClient
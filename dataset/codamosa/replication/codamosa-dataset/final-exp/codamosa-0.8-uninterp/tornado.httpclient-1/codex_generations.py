

# Generated at 2022-06-22 13:15:06.085262
# Unit test for function main
def test_main():
    import doctest
    doctest.run_docstring_examples(main, globals())

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:15:17.054682
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import sys
    import io
    import contextlib

    # context manager that redirects stdout and stderr
    @contextlib.contextmanager
    def stdout_redirector(stream):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = stream
        sys.stderr = stream
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

    # Context manager that redirects stdout and stderr, then reads them
    # afterwards.
    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()

# Generated at 2022-06-22 13:15:22.099832
# Unit test for function main
def test_main():
    import sys;
    assert sys.argv[0] == "test"
    assert sys.argv[1] == "test.py"
    assert sys.argv[2] == "test_client.py"
    assert sys.argv[3] == "test_main"
    sys.argv = sys.argv[:3]
    main()

# Generated at 2022-06-22 13:15:24.845414
# Unit test for method fetch of class HTTPClient
def test_HTTPClient_fetch():
    request = 'http://www.google.com/'
    http_client = HTTPClient()
    response = http_client.fetch(request)
    http_client.close()
    assert response.code == 200


# Generated at 2022-06-22 13:15:36.265163
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    global_defaults = {
    'follow_redirects': False,
    'max_redirects': 10,
    'validate_cert': True,
    'ca_certs': None,
    'client_key': None,
    'client_cert': None,
    }
    req_def_1 = {
    'proxy_host': "localhost",
    'proxy_port': 3128,
    'proxy_username': None,
    'proxy_password': None,
    'allow_nonstandard_methods': False,
    'network_interface': None,
    'user_agent': "Test-Agent/2.0",
    'use_gzip': False,
    'use_proxy': False,
    }
    import tornado.gen
    import tornado.httpclient
    import tornado.ioloop
   

# Generated at 2022-06-22 13:15:37.761776
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    r = HTTPResponse(HTTPRequest('url'), 200)
    r.rethrow()


# Generated at 2022-06-22 13:15:38.324862
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    pass  # TODO: implement this function

# Generated at 2022-06-22 13:15:43.004662
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    import unittest
    import tornado.testing
    import tornado.web
    self = HTTPResponse()
    error = HTTPError(self.code, message=self.reason, response=self)
    with self.assertRaises(error):
        self.rethrow()
    try:
        self.rethrow()
    except Exception as e:
        assert e == error


# Generated at 2022-06-22 13:15:43.728308
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-22 13:15:46.058200
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    client = AsyncHTTPClient()
    client.close()

# Generated at 2022-06-22 13:15:54.259045
# Unit test for function main
def test_main():
    # No exception throws.
    main()



# Generated at 2022-06-22 13:15:57.201772
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    client = AsyncHTTPClient()
    client.initialize()
    assert client.defaults == client.defaults
    assert client._closed == False


# Generated at 2022-06-22 13:16:05.304204
# Unit test for method rethrow of class HTTPResponse
def test_HTTPResponse_rethrow():
    try:
        raise HTTPError(500)
    except HTTPError as exc:
        http_response = HTTPResponse(HTTPRequest('http://www.google.com'), 500, error=exc)
    try:
        http_response.rethrow()
    except HTTPError as exception:
        print(exception.code)

if __name__ == '__main__':
    test_HTTPResponse_rethrow()

# Generated at 2022-06-22 13:16:16.391552
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    """Test that the method fetch of class AsyncHTTPClient
       returns the expected response for a given url.
    """

    # define the expected response for the given url
    expected_response = { 'Content-Type': 'text/html; charset=UTF-8',
                          'Date': 'Tue, 13 Sep 2016 17:19:52 GMT',
                          'Server': 'gws',
                          'Content-Length': '220',
                          'X-XSS-Protection': '1; mode=block',
                          'Cache-Control': 'private, max-age=0',
                          'X-Frame-Options': 'SAMEORIGIN',
                          'Alternate-Protocol': '443:quic,p=1',
                          'Connection': 'close' 
                        }
    
    # define the url to be processed

# Generated at 2022-06-22 13:16:19.928845
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    client = AsyncHTTPClient()
    client.initialize(defaults=dict(user_agent="Mozilla/5.0"))
    assert client.defaults.get("user_agent") == "Mozilla/5.0" 

# Generated at 2022-06-22 13:16:27.703265
# Unit test for function main
def test_main():
    import unittest.mock as mock
    import sys
    import io

    # stubs
    sys.argv = ["httpclient_test"]
    parse_command_line = mock.Mock()

    def mock_fetch(**kwargs):
        return "response"

    def side_effect(*args, **kwargs):
        if "print_headers" in args:
            return False
        elif "print_body" in args:
            return True
        else:
            return True

    # mock objects
    client = mock.Mock()
    client.fetch.side_effect = mock_fetch
    client.close = mock.Mock()
    response = mock.Mock()
    response.headers = "response.headers"
    response.body = "response.body"

    # Monkey patching HTTPClient class

# Generated at 2022-06-22 13:16:35.037377
# Unit test for function main
def test_main():
    from tornado.testing import AsyncHTTPTestCase
    from tornado.web import RequestHandler
    from tornado.options import define, options, parse_command_line
    from tornado.testing import gen_test
    from tornado.httpclient import AsyncHTTPClient
    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)
    args = parse_command_line()
    client = HTTPClient()
    class MainHandler(RequestHandler):
        @gen_test
        def get(self):
            self.write("Hello, world")


# Generated at 2022-06-22 13:16:39.218071
# Unit test for constructor of class HTTPRequest
def test_HTTPRequest():
    # test with default parameters
    request = HTTPRequest('/')
    assert isinstance(request.headers, httputil.HTTPHeaders)

    # test with non-default parameters
    request = HTTPRequest('/', follow_redirects=False, max_redirects=10, user_agent='test')
    assert request.follow_redirects == False
    assert request.max_redirects == 10
    assert request.headers['User-Agent'] == 'test'
    assert isinstance(request.headers, httputil.HTTPHeaders)



# Generated at 2022-06-22 13:16:40.439574
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    return True



# Generated at 2022-06-22 13:16:50.745104
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    class MyClient(AsyncHTTPClient):
        def fetch_impl(
            self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]
        ) -> None:
            pass

    MyClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    async def test():
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch("http://www.google.com/")
            print(response.body)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))

# Generated at 2022-06-22 13:17:12.167557
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import asyncio
    asyncio.new_event_loop()
    impl=AsyncHTTPClient()
    def callback(callback_: HTTPResponse):
        return
    request=HTTPRequest()
    impl.fetch_impl(request=request, callback=callback)

# Generated at 2022-06-22 13:17:12.822717
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    pass

# Generated at 2022-06-22 13:17:19.789123
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    http_client = AsyncHTTPClient()
    try:
        response = async_http_client.fetch("http://www.google.com/")
        print(response.body)
    except http_client.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()


# Generated at 2022-06-22 13:17:21.722881
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    pass

# Generated at 2022-06-22 13:17:33.725658
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    AsyncHTTPClient.configure(None, max_clients=10, defaults=None)
    kwargs = dict(max_clients=10, defaults=None)
    client = AsyncHTTPClient()
    assert isinstance(client, SimpleAsyncHTTPClient)
    client.close()
    client_1 = AsyncHTTPClient()
    client_2 = AsyncHTTPClient(force_instance=True, **kwargs)
    assert isinstance(client_2, SimpleAsyncHTTPClient)
    assert id(client_1) == id(client_2)
    client_1.close()
    client_3 = AsyncHTTPClient()
    assert id(client_3) != id(client_2)
    client_3.close()


# Generated at 2022-06-22 13:17:45.658063
# Unit test for function main
def test_main():
    from tornado.options import options, define, parse_command_line
    import tornado.httpclient
    # url = "https://www.example.com"
    # url = "https://www.journaldev.com/7215/python-socket-programming-tutorial"
    url = "https://www.cbc.ca/news/"
    url = "https://www.markus-gattol.name/blog/tornado-httpclient/"
    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)

# Generated at 2022-06-22 13:17:55.383777
# Unit test for method __new__ of class AsyncHTTPClient
def test_AsyncHTTPClient___new__():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.httpclient import AsyncHTTPClient
    async def f():
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch("http://www.google.com")
        except Exception as e:
            print("Error: %s" % e)
        else:
            print(response.body)
    
    with SimpleAsyncHTTPClient() as client:
        client.fetch('http://google.com')
    f()
    #assert 0
    # pass

test_AsyncHTTPClient___new__()


# Generated at 2022-06-22 13:18:01.329489
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    global client_created
    client_created = False
    class DummyHTTPClient(AsyncHTTPClient):
        def initialize(self, defaults=None):
            global client_created
            client_created = True
            AsyncHTTPClient.initialize(self, defaults)
    DummyHTTPClient(force_instance=True)
    assert client_created


# Generated at 2022-06-22 13:18:05.127315
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    # test for incorrect argument
    error = False
    try:
        AsyncHTTPClient().fetch_impl(None, None)
    except NotImplementedError:
        error = True
    finally:
        assert error



# Generated at 2022-06-22 13:18:05.566532
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    pass



# Generated at 2022-06-22 13:18:30.776054
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.testing import AsyncHTTPTestCase

    class DummyHTTPClient(AsyncHTTPClient):
        closed = False

        def fetch_impl(self, request, callback):
            pass

        def close(self):
            self.closed = True

    class CloseTest(AsyncHTTPTestCase):
        def test_close(self):
            self.http_client = DummyHTTPClient()
            self.http_client.close()
            self.assertTrue(self.http_client.closed)
            self.assertIsInstance(self.http_client, DummyHTTPClient)

        def test_shared_client(self):
            http_client = AsyncHTTPClient()
            self.assertIsInstance(http_client, AsyncHTTPClient)


# Generated at 2022-06-22 13:18:32.384136
# Unit test for function main
def test_main():
    main()
if __name__ == "__main__":
    test_main()

# Generated at 2022-06-22 13:18:35.488911
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    instance = AsyncHTTPClient()
    instance.initialize()
    assert instance._closed == False


# Generated at 2022-06-22 13:18:44.860384
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    import unittest
    import asyncio
    async def test_asyncHTTPClient_fetch():
        def handle_response(response) -> None:
            check_result(response)
            return None
        request = HTTPRequest(url="http://www.google.com")
        client = AsyncHTTPClient()
        client.fetch_impl(request,handle_response)
    class Check(unittest.TestCase):
        def test_1(self):
            asyncio.run(test_asyncHTTPClient_fetch())
    def check_result(response):
        assert type(response) == HTTPResponse
    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-22 13:18:45.994547
# Unit test for function main
def test_main():
    sys_args = ['http://www.google.com']
    sys.argv[1:] = sys_args
    main()

# Generated at 2022-06-22 13:18:50.867759
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import unittest
    from tornado import httputil

    HTTPRequest = httputil.HTTPRequest
    @unittest.mock.patch.object(AsyncHTTPClient, '__new__')
    def test_constructor(self, __new__):
        __new__.return_value = None
        AsyncHTTPClient(**{'foo': 1, 'bar': 2})
        # Make sure the kwargs are passed on to the configurable subclass.
        __new__.assert_called_with(None, foo=1, bar=2)
        # Make sure the defaults are set.
        self.assertEqual(self._async_client.defaults,
                         HTTPRequest._DEFAULTS)



# Generated at 2022-06-22 13:19:00.515343
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    from unittest import mock
    import types

    # Make sure that class _RequestProxy.__getattr__ will return None when attr is not found.
    request = mock.MagicMock()
    defaults = mock.MagicMock()
    req_proxy = _RequestProxy(request, defaults)
    assert req_proxy.__getattr__('non_exist_attr') == None

    # Make sure that class _RequestProxy.__getattr__ will return method when attr is found.
    request.getattr = types.MethodType(lambda self: None, req_proxy.request)
    assert req_proxy.__getattr__('getattr') == req_proxy.request.getattr


# Generated at 2022-06-22 13:19:06.274392
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    import pytest
    with pytest.raises(NotImplementedError) as excinfo:
        AsyncHTTPClient().fetch_impl('request', 'handle_response')
    assert str(excinfo.value) == "fetch_impl"
    return True
print(test_AsyncHTTPClient_fetch_impl())


# Generated at 2022-06-22 13:19:17.113565
# Unit test for function main
def test_main():
    from tornado.options import define, options, parse_command_line
    from tornado.testing import bind_unused_port, AsyncHTTPSTestCase, ExpectLog
    import tornado.web

    class HelloHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("hello")

    class HelloRedirectHandler(tornado.web.RequestHandler):
        def get(self):
            self.redirect("/hello")

    class HelloRedirectCodeHandler(tornado.web.RequestHandler):
        def get(self):
            self.redirect("/hello", permanent=True)

    class AuthHandler(tornado.web.RequestHandler):
        def initialize(self, username, password):
            self.username = username
            self.password = password


# Generated at 2022-06-22 13:19:21.120948
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    request = HTTPRequest('http://localhost:8888')
    proxy = _RequestProxy(request, {'auth_username': 'username'})
    assert proxy.auth_username == 'username'
    assert proxy.url == 'http://localhost:8888'



# Generated at 2022-06-22 13:19:59.605549
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    from tornado.testing import gen_test
    from tornado.platform.asyncio import BaseAsyncIOLoop, to_asyncio_future

    from tornado import testing

    class DummyAsyncHTTPClient(AsyncHTTPClient):

        def fetch_impl(
            self, request: "HTTPRequest", callback: Callable[["HTTPResponse"], None]
        ) -> None:
            return

    @testing.gen_test
    async def test_close():
        # Make sure that closing the HTTPClient releases the
        # references to the AsyncHTTPClient class, the IOLoop, etc.
        # This is a regression test for a memory leak in
        # httpclient_test.HTTPClientCallbackTest.test_connection_limit
        io_loop = BaseAsyncIOLoop(make_current=False)

# Generated at 2022-06-22 13:20:01.101447
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    obj = AsyncHTTPClient()
    obj.initialize(defaults=None)
    obj.close()


# Generated at 2022-06-22 13:20:02.997067
# Unit test for constructor of class HTTPClient
def test_HTTPClient():
    """Unit test for constructor of class HTTPClient"""
    http_client = HTTPClient()
    return


# Generated at 2022-06-22 13:20:07.057141
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    def test_fetch_impl(self, request, callback):
        pass

    AsyncHTTPClient.fetch_impl = test_fetch_impl
    assert callable(AsyncHTTPClient.fetch_impl)



# Generated at 2022-06-22 13:20:11.848579
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()
    # Unit test for function main, will be called in io_loop
    io_loop = IOLoop.current()
    io_loop.add_callback(callback=test_main)
    io_loop.start()

# Generated at 2022-06-22 13:20:12.530839
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
	pass

# Generated at 2022-06-22 13:20:15.496665
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    defaults = {
        'connect_timeout': 0.2,
        'max_redirects': 20,
        'max_attempts': 1,
        'request_timeout': 0.1,
    }
    inst = AsyncHTTPClient()
    inst.initialize(defaults)


# Generated at 2022-06-22 13:20:21.242708
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    AsyncHTTPClient.configure(None)
    async def test():
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://www.google.com/")
        http_client.close()
    IOLoop.current().run_sync(test)


# Generated at 2022-06-22 13:20:28.947176
# Unit test for method fetch of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch():
    AsyncHTTPClient.configure()
    http_client = AsyncHTTPClient()
    try:
        response = http_client.fetch("http://www.google.com/")
        assert response.body
    except HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()



# Generated at 2022-06-22 13:20:38.479968
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    '''
    def close(self) -> None:
        """Destroys this HTTP client, freeing any file descriptors used.

        This method is **not needed in normal use** due to the way
        that `AsyncHTTPClient` objects are transparently reused.
        ``close()`` is generally only necessary when either the
        `.IOLoop` is also being closed, or the ``force_instance=True``
        argument was used when creating the `AsyncHTTPClient`.

        No other methods may be called on the `AsyncHTTPClient` after
        ``close()``.

        self._closed = False
    '''

# Generated at 2022-06-22 13:21:37.825710
# Unit test for function main
def test_main():
    # Test normal case
    with patch(
        "tornado.httpclient.HTTPClient", autospec=True
    ) as mock_httpclient:
        with patch("tornado.httpclient.parse_command_line") as mock_parse_command_line:
            mock_parse_command_line.return_value = ["test_arg"]
            main()
            mock_httpclient.assert_called()
            mock_httpclient.return_value.fetch.assert_called_with(
                "test_arg",
                follow_redirects=True,
                validate_cert=True,
                proxy_host=None,
                proxy_port=None,
            )

# Generated at 2022-06-22 13:21:43.842364
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    async_http_client = AsyncHTTPClient()
    _request = HTTPRequest("http://www.baidu.com")
    def handle_response(response: HTTPResponse) -> None:
        assert response.error == None, "response.error should be None"
    async_http_client.fetch_impl(_request, handle_response)



# Generated at 2022-06-22 13:21:52.456260
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    import asyncio
    import tornado.platform.asyncio

    async def f():
        async_client = AsyncHTTPClient()

        async def handle_response(response):
            print(response.body)

        await async_client.fetch("http://www.google.com/", callback=handle_response)
        async_client.close()

    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(f())
    loop.close()


# Generated at 2022-06-22 13:21:57.017479
# Unit test for function main
def test_main():
    args = ['a']
    client = HTTPClient()
    for arg in args:
        response = client.fetch(arg)
        print(response.status)
        print(response.headers)
        print(response.body)

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:22:04.902963
# Unit test for function main
def test_main():
    from tornado.testing import bind_unused_port, AsyncHTTPTestCase
    import urllib.request
    import urllib.parse
    import subprocess
    import os

    class MainTest(AsyncHTTPTestCase):
        def get_app(self):
            return None

        def test_main(self):
            self.http_client.fetch(self.get_url("/"), self.stop)
            response = self.wait()
            self.assertEqual(response.code, 404)

            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "tornado.httpclient",
                    self.get_url("/"),
                    "--print_headers=true",
                ]
            )

            port = self.get_http_port()
            # Proxies typically

# Generated at 2022-06-22 13:22:11.605518
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    # initialization of a AsyncHTTPClient object
    # assert the instance of AsyncHTTPClient is placed in the
    # weakkeydictionary when initialized
    client = AsyncHTTPClient()
    assert isinstance(client, AsyncHTTPClient), "should be an instance of AsyncHTTPClient"
    assert (
        AsyncHTTPClient._async_clients()[IOLoop.current()]
        is client
    ), "client should be in _async_clients"
    client.close()



# Generated at 2022-06-22 13:22:12.157015
# Unit test for function main
def test_main():
	main()

Run()

# Generated at 2022-06-22 13:22:14.695082
# Unit test for function main
def test_main():
    if __name__ == "__main__":
        main()


__all__ = [
    "AsyncHTTPClient",
    "HTTPRequest",
    "HTTPResponse",
    "HTTPError",
    "main",
]

# Generated at 2022-06-22 13:22:17.212091
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from nose.plugins.skip import SkipTest

    raise SkipTest("No test for this module yet")



# Generated at 2022-06-22 13:22:23.075363
# Unit test for function main
def test_main():
    import os
    import sys
    import contextlib
    import io
    sys.argv = ["python", "httpclient_test.py"]
    stdout = sys.stdout
    stderr = sys.stderr
    try:
        my_stdout = io.StringIO()
        my_stderr = io.StringIO()
        sys.stdout = my_stdout
        sys.stderr = my_stderr
        with contextlib.redirect_stdout(my_stdout):
            with contextlib.redirect_stderr(my_stderr):
                main()
        assert(os.path.exists('httpclient_test.py'))
    except Exception as e:
        print(e)
    finally:
        sys.stderr = stderr
        sys.std

# Generated at 2022-06-22 13:23:16.837901
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    for func_name in dir(AsyncHTTPClient):
        if func_name.startswith("__") and func_name.endswith("__"):
            continue
        if func_name.startswith("_"):
            continue
        assert hasattr(AsyncHTTPClient, func_name), "missing %s in AsyncHTTPClient" % func_name

    AsyncHTTPClient.initialize(defaults=None)


# Generated at 2022-06-22 13:23:28.309299
# Unit test for function main
def test_main():
    args = ["https://www.google.com/","https://www.microsof.com/"]
    client = HTTPClient()
    for arg in args:
        try:
            response = client.fetch(
                arg,
                follow_redirects=True,
                validate_cert=True,
                proxy_host=None,
                proxy_port=None,
            )
        except HTTPError as e:
            if e.response is not None:
                response = e.response
            else:
                raise
        if True:
            print(response.headers)
        if True:
            print(native_str(response.body))
    client.close()


if __name__ == "__main__":
    main()
    # Uncomment this if you want to unit test the function main
    #test_main()

# Generated at 2022-06-22 13:23:28.912800
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 13:23:33.122726
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    print("Starting test test_AsyncHTTPClient_close")
    AsyncHTTPClient.configure("tornado.simple_httpclient.SimpleAsyncHTTPClient")
    http_client = AsyncHTTPClient()
    assert not http_client._closed
    http_client.close()
    assert http_client._closed
    #TODO: test raise RuntimeError if called twice
    print("test test_AsyncHTTPClient_close - success")


# Generated at 2022-06-22 13:23:41.406877
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    import asyncio
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
    import tornado.web
    import tornado.ioloop
    import tornado.httpserver
    import tornado.iostream
    import tornado.options
    import tornado.httputil
    import tornado.escape
    import tornado.platform.asyncio
    import tornado.curl_httpclient
    import tornado.httpclient
    import Future
    import HTTPResponse
    import HTTPRequest
    import And
    import Or
    import Not
    from vyapp.plugins.asynchttpclient.handler import AsyncHTTPClient
    from vyapp.plugins.asynchttpclient.response import HTTPResponse

# Generated at 2022-06-22 13:23:42.527250
# Unit test for function main
def test_main():
    pass


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 13:23:45.896728
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    import gc
    http_client = AsyncHTTPClient()
    http_client.close()

# Generated at 2022-06-22 13:23:48.137917
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    client = AsyncHTTPClient()
    client.fetch_impl(HTTPRequest(),lambda x: x)

# Generated at 2022-06-22 13:23:50.244759
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    cls = AsyncHTTPClient()
    cls.close()



# Generated at 2022-06-22 13:23:51.401896
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():
    c = AsyncHTTPClient()
    c.close()

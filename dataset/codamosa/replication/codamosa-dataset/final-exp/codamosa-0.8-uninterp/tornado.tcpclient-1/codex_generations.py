

# Generated at 2022-06-22 13:27:50.041113
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    a = _Connector()
    a.clear_timeouts()
    return



# Generated at 2022-06-22 13:28:01.247913
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    import tornado.testing

    class TestConnector(tornado.testing.AsyncTestCase):
        def test_clear(self):
            self.io_loop = IOLoop.current()
            self.connect = lambda af, addr: IOStream(socket.socket())
            self.io_loop.run_sync(
                lambda: self.io_loop.add_callback(self.test_clear_func)
            )

        @gen.coroutine
        def test_clear_func(self):
            connection = _Connector(
                addrinfo=[],
                connect=self.connect,
            )
            self.assertEqual(connection.timeout, None)
            connection.set_timeout(1)
            self.assertIsInstance(connection.timeout, object)
            connection.clear_timeout()

# Generated at 2022-06-22 13:28:06.286633
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    print("Running unit test: test__Connector_on_connect_timeout")
    _Connector(None, None).on_connect_timeout()
    print("Passed unit test: test__Connector_on_connect_timeout")


# Generated at 2022-06-22 13:28:18.076544
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import unittest.mock as mock

    addrinfo = [(0, "addr"), (1, "addr")]
    addrs = [(i, "addr") for i in range(1, 3)]

    def _connect(af, addr):
        future = Future()  # type: Future[IOStream]
        if addr in addrs:
            future.set_exception(Exception("connection failed"))
        else:
            stream = mock.MagicMock()  # type: IOStream
            future.set_result(stream)
        return stream, future

    c = _Connector(addrinfo, _connect)
    c.try_connect(iter(addrs))

    assert c.remaining == 2

    # Exception should be raised by get_result()
    assert c.future.exception()


# Generated at 2022-06-22 13:28:21.192499
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    timeout = 0
    connector = _Connector
    connector.set_connect_timeout(timeout)
    timeout = 10.0
    connector.set_connect_timeout(timeout)



# Generated at 2022-06-22 13:28:24.972927
# Unit test for method on_timeout of class _Connector

# Generated at 2022-06-22 13:28:36.788209
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import unittest
    import io
    import test.mock
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.netutil import bind_sockets, bind_unix_socket

    class TCPServer(object):
        def __init__(self, io_loop, address) -> None:
            self.io_loop = io_loop
            self.sockets, self.port = bind_sockets(address, "localhost", family=socket.AF_INET)
            self.stream = None  # type: Optional[IOStream]
            for sock in self.sockets:
                self.io_loop.add_handler(
                    sock.fileno(), self.accept, self.io_loop.READ
                )


# Generated at 2022-06-22 13:28:47.772412
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import socket
    import subprocess
    import tornado.ioloop
    import sys

    from tornado.iostream import IOStream
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.concurrent import Future
    from tornado.log import app_log

    def create_connection(address: Tuple[int], timeout: int = None) -> Tuple[IOStream, Future]:
        io_loop = tornado.ioloop.IOLoop.current()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.setblocking(False)
        stream = IOStream(s, io_loop=io_loop)
        future = to_asyncio_future(stream.connect(address))
        return stream, future


# Generated at 2022-06-22 13:28:50.562881
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from .stack_context import wrap
    from .timeout_error import TimeoutError

    # if hasattr(stream, 'socket'):
    #     stream.socket.close()
    # else:
    #     stream.close()
    pass



# Generated at 2022-06-22 13:28:56.994467
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    io_loop = IOLoop()
    addrinfo = [('AF_INET', ('1.1.1.1', 1)), ('AF_INET', ('1.1.1.2', 1))]

    def connect(af: socket.AddressFamily, addr: Tuple):
        return (
            IOStream(socket.socket(af, socket.SOCK_STREAM, 0)),
            Future(),
        )

    x = _Connector(addrinfo, connect)

    for _ in range(2):
        x.try_connect(iter(addrinfo))

    x.close_streams()



# Generated at 2022-06-22 13:33:23.215084
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.testing import AsyncHTTPTestCase
    import tornado.web
    
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")
    
    class TestTCPClientConnect(AsyncHTTPTestCase):
        def get_app(self):
            urls = [
                (r"/", MainHandler),
            ]
            return tornado.web.Application(urls)

        async def test_TCPClient_connect(self):
            client = TCPClient()
            await client.connect('www.baidu.com', 80)
            client.close()
    
    test = TestTCPClientConnect()
    result = test.get_app()

if __name__ == '__main__':
    test_TCPClient_connect()

# Generated at 2022-06-22 13:33:30.431484
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    conn = _Connector([(socket.AF_INET, ("192.99.0.2", 3306), socket.IPPROTO_TCP)], None)
    future1 = conn.future
    from tornado.iostream import InvalidStateError
    future1.set_exception(InvalidStateError())
    future2 = conn.future
    future2.set_exception(InvalidStateError())


# Generated at 2022-06-22 13:33:41.413022
# Unit test for method start of class _Connector
def test__Connector_start():
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()
    test__Connector_start()

# Generated at 2022-06-22 13:33:44.280619
# Unit test for method connect of class TCPClient

# Generated at 2022-06-22 13:33:48.336585
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    import asyncio
    async def f():
        client=TCPClient()
        stream=await client.connect("www.google.com",80)
    asyncio.get_event_loop().run_until_complete(f())

# Generated at 2022-06-22 13:33:54.733998
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.testing import AsyncTestCase, gen_test

    class TestTCPClient(AsyncTestCase):

        @gen_test
        async def test_TCPClient_connect(self):
            client = TCPClient()
            try:
                for i in [0, 1, 2, 3]:
                    stream = await client.connect("localhost", 8080)
                    stream.close()
            finally:
                client.close()

    TestTCPClient().test_TCPClient_connect()
test_TCPClient_connect()

# Generated at 2022-06-22 13:34:03.682459
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    def close():
        pass
    class _s():
        def __init__(self):
            pass
        def close(self):
            close()
    class _stream(object):
        def __init__(self):
            pass
        def close(self):
            close()
        @staticmethod
        def add(stream):
            pass
    class _i():
        def __init__(self):
            pass
        @staticmethod
        def remove_timeout(self):
            close()
        @staticmethod
        def time():
            return _s()
        @staticmethod
        def add_timeout(self, timeout, callback):
            pass
    class _c():
        def __init__(self):
            pass
        @staticmethod
        def split(addrinfo):
            return _s(), _s()

# Generated at 2022-06-22 13:34:04.578173
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    pass


# Generated at 2022-06-22 13:34:14.581951
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():

    def coroutine(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return gen.coroutine(func)(*args, **kwargs)
        return wrapper

    def getaddrinfo():

        @coroutine
        def resolver(host, port, family):
            return [(socket.AF_INET, ('127.0.0.1', 8080))]
        return resolver

    def _create_stream(max_buffer_size, af, addr):
        return 'stream', 'future'

    host = '127.0.0.1'
    port = 8080

    # Test without SSL
    ssl_options = None

    myResolver = getaddrinfo()
    tcpclient = TCPClient(myResolver)
    tcpclient._create_stream = _create_stream

# Generated at 2022-06-22 13:34:23.454617
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    tcpclient = TCPClient()
    # test with IP address
    stream, future = tcpclient._create_stream(1024, socket.AF_INET, ("127.0.0.1", 1234), "127.0.0.1")
    future.result()
    assert stream.socket.family == socket.AF_INET
    assert stream.socket.getsockname() == ("127.0.0.1", 1234)
    stream.close()
    # test with hostname
    stream, future = tcpclient._create_stream(1024, socket.AF_INET, ("localhost", 1234), "127.0.0.1")
    future.result()
    assert stream.socket.family == socket.AF_INET
    assert stream.socket.getsockname() == ("127.0.0.1", 1234)
   

# Generated at 2022-06-22 13:36:14.794706
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado

    import tornado.testing

    class TCPClientTest(tornado.testing.AsyncTestCase):
        def test_TCPClient(self):
            self.http_client = tornado.httpclient.HTTPClient()
            self.assertEqual(
                self.http_client.fetch("http://www.facebook.com").code,
                200
            )

# Generated at 2022-06-22 13:36:20.272909
# Unit test for method start of class _Connector
def test__Connector_start():
    import unittest
    import socket
    import unittest.mock as mock
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase
    from tornado.test.util import unittest_run_loop

    from sockjs.tornado.conn import TCPClientConnection

    AsyncIOMainLoop().install()
    class Test_Connector(unittest.TestCase, AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.resolver = Resolver()
            self.resolver.install()
            self.mock_resolve = mock.patch.object(
                self.resolver, "resolve", return_value=Future()
            )
            self.mock_resolve.start()
            self.resolver.resolve

# Generated at 2022-06-22 13:36:28.054468
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import tornado.iostream
    import tornado.ioloop
    import socket
    import errno

    # If a connection attempt succeeds, we do not try another.
    loop = tornado.ioloop.IOLoop()
    connector = _Connector(
        [(socket.AF_INET, ("1.2.3.4", 80))],
        lambda af, addr: (  # type: ignore
            tornado.iostream.IOStream(socket.socket(af, socket.SOCK_STREAM)),
            gen.maybe_future(None),
        ),
    )
    future = connector.start()
    loop.run_sync(lambda: future)
    assert future.result()[1] == ("1.2.3.4", 80)

    # If a connection attempt fails, we try the next address.

# Generated at 2022-06-22 13:36:39.607473
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from tornado.testing import AsyncTestCase, bind_unused_port
    from mypy_extensions import TypedDict
    from .test.util import ignore_deprecation

    class FakeStream(object):
        def close(self):
            pass

    @ignore_deprecation
    class TestConnector(AsyncTestCase):
        def test_close(self):
            sock, port = bind_unused_port()
            stream = FakeStream()
            connector = _Connector(
                [(socket.AF_INET, ("127.0.0.1", port))],
                lambda af, addr: (stream, Future()),
            )
            connector.start(connect_timeout=0.2)
            self.io_loop.add_callback(sock.close)
            with self.assertRaises(TimeoutError):
                self

# Generated at 2022-06-22 13:36:52.210512
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    import unittest
    import unittest.mock
    import contextlib
    import socket
    import errno

    import tornado.testing
    import tornado.platform.asyncio
    import asyncio
    import tornado.iostream

    # Before Python 3.5.3, connection refused would be raised as a
    # ConnectionRefusedError. But since Python 3.5.3, it is raised as a
    # ConnectionResetError.
    _ERRNO_CONNECTION_REFUSED = getattr(errno, "ECONNREFUSED", errno.ECONNRESET)

    tornado.platform.asyncio.AsyncIOMainLoop().install()

    class _Resolver(Resolver):
        def close(self):
            pass


# Generated at 2022-06-22 13:37:02.818420
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    def mock_gen_try_connect(addrs):
        if addrs[0] == ('AF_INET', ('127.0.0.1', 8888)):
            return ('AF_INET', ('127.0.0.1', 8888), None)
        return ('AF_INET', ('127.0.0.1', 8888), 'test')
    addrs = [('AF_INET', ('127.0.0.1', 8888)), ('AF_INET', ('127.0.0.1', 9999))]
    connect = mock_gen_try_connect
    c = _Connector(addrs, connect)
    c.future = Future()
    c.future.done.return_value = False
    f = Future()
    f.result.return_value = 'done'
    c.future

# Generated at 2022-06-22 13:37:08.156629
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    async def client_method(port):
        client = TCPClient()
        stream = await client.connect('www.google.com', port=port)
        data = await stream.read_until_close()
        print(data)
    #return True
    if __file__ == "gen_orchestrate/tcpclient.py":
        from tornado.ioloop import IOLoop
        loop = IOLoop.current()
        loop.run_sync(lambda: client_method(80))
        #loop.run_sync(lambda: client_method(443))


# Generated at 2022-06-22 13:37:16.229324
# Unit test for method start of class _Connector
def test__Connector_start():
    def ioeloop_add_timeout(io_loop, time):
        return time
    ioloop_current = mock.MagicMock(return_value=ioeloop_current)
    ioloop_current.add_timeout = mock.MagicMock(side_effect=ioeloop_add_timeout)
    import tornado
    with mock.patch('__main__.ioloop_current', ioloop_current):
        with mock.patch.object(tornado, 'ioloop', ioloop_current):
            mock_socket = mock.MagicMock(name='socket')
            mock_socket.AF_INET = socket.AF_INET
            mock_socket.AF_INET6 = socket.AF_INET6
            mock_socket.AF_UNSPEC = socket.AF_UNSPEC
            mock_socket.SOCK

# Generated at 2022-06-22 13:37:28.386059
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    socket_address_family = socket.AddressFamily.AF_INET
    socket_address = ("127.0.0.1", 65432)
    io_stream_future = Future()
    io_stream_future.set_result(object())
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
    io_stream_future.result()
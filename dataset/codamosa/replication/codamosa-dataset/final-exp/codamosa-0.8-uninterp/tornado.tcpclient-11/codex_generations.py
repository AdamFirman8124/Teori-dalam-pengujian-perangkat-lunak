

# Generated at 2022-06-22 13:28:02.054529
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    from tornado.iostream import IOStream
    from tornado.concurrent import Future
    import socket

    def connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[IOStream, Future]:
        pass

    addrs: List[Tuple] = [
        (socket.AF_INET, ("1.1.1.1", 8008)),
        (socket.AF_INET6, ("1::1", 8008)),
        (socket.AF_INET, ("1.1.1.1", 8008)),
    ]

    class Test_Connector(_Connector):
        def __init__(self, addrinfo: List[Tuple]):
            super().__init__(
                addrinfo,
                connect,
            )
            self.io_loop = IOLoop.current()
            self.connect = connect



# Generated at 2022-06-22 13:28:14.612693
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    '''
    Runs a test of the on_timeout method of the _Connector class
    '''
    # Create a new future object and pass it to the _Connector object
    io_loop = IOLoop.current()
    future = Future()
    _connector = _Connector(
        addrinfo = [(4, ("ipv4", 123)), (6, ("ipv6", 123))],
        connect = None
    )
    _connector.future = future
    _connector.io_loop = io_loop
    # Call the on_timeout method with no handler in place
    _connector.on_timeout()
    future.set_exception(IOError("connection failed"))
    # Call the on_timeout method with a handler in place
    _connector.on_timeout()
    future.set_exception(TimeoutError())
   

# Generated at 2022-06-22 13:28:20.871294
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    resolver = Resolver()
    addrinfo = resolver.resolve('www.chinaso.com')
    constructor = lambda addr: IOStream(socket.create_connection(addr))
    future = _Connector(addrinfo, constructor).start()
    event = future.add_done_callback(lambda future: print(future.result()))
    IOLoop.current().start()
test__Connector_set_timeout()


# Generated at 2022-06-22 13:28:31.839821
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    from tornado.platform.asyncio import AsyncIOMainLoop
    import asyncio

    AsyncIOMainLoop().install()
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
    loop = asyncio.get_event_loop()

    async def set_connect_timeout():
        import logging
        import time
        from tornado.iostream import IOStream
        from tornado.tcpclient import TCPClient
        from tornado.iostream import StreamClosedError

        @gen.coroutine
        def coroutine():
            s, f = yield TCPClient().connect('127.0.0.1', 8888)

# Generated at 2022-06-22 13:28:36.892558
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    # Create a _Connector object and call method on_timeout
    addrinfo = [("AF_INET", ("127.0.0.1", 8080))]
    connect_callback = lambda x, y: None
    conn = _Connector(addrinfo, connect_callback)

# Generated at 2022-06-22 13:28:45.561031
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    io_loop = IOLoop.current()
    io_loop.time = lambda: 0.0
    # type: Callable[[float], None]
    def on_timeout():
        pass
    def on_connect_timeout():
        pass
    tc = _Connector(None, None)
    tc.io_loop = io_loop
    tc.timeout = io_loop.add_timeout(0.0, on_timeout)
    tc.connect_timeout = io_loop.add_timeout(0.0, on_connect_timeout)
    tc.clear_timeouts()
    assert tc.timeout is None
    assert tc.connect_timeout is None



# Generated at 2022-06-22 13:28:53.604717
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    resolver = Resolver()
    def test_connect(af: socket.AddressFamily, addr: Tuple) -> "Tuple[IOStream, Future[IOStream]]":
        stream = IOStream(socket.socket(af, socket.SOCK_STREAM))
        future = Future()
        future.set_result(stream)
        return stream, future
    def test_on_timeout() -> None:
        future.cancel()
    def test_future_add_done_callback(future: Future, callback: Callable) -> None:
        callback(future)
    future = Future()
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::', 80))]
    test = _Connector(addrinfo, test_connect)
    test.future = future

# Generated at 2022-06-22 13:28:57.262529
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    # TODO: Learn more about typehints to fix this
    # m = mock.Mock(spec=[_Connector])
    m = Mock()
    m.io_loop = IOLoop.current()

    m.connect_timeout = None  # type: Optional[object]
    m.set_connect_timeout(datetime.timedelta(seconds=10))
    assert m.connect_timeout is not None
    m.io_loop.remove_timeout(m.connect_timeout)

    m.connect_timeout = None  # type: Optional[object]
    m.set_connect_timeout(10)
    assert m.connect_timeout is not None
    m.io_loop.remove_timeout(m.connect_timeout)


# Generated at 2022-06-22 13:29:07.857196
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    AF_INET = socket.AF_INET
    AF_INET6 = socket.AF_INET6
    addrinfo = [
        (AF_INET, ("192.168.1.1", 80)),
        (AF_INET6, ("2001:0db8:85a3:0042:1000:8a2e:0370:7334", 80)),
    ]
    def client_callback(stream, future):
        return True
    class fake_IOLoop:
        def __init__(self):
            self.time = 0
            self.timeouts = []
        def add_timeout(self, time, callback):
            self.timeouts.append((time, callback))
            return len(self.timeouts) - 1

# Generated at 2022-06-22 13:29:13.243467
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    import unittest
    import unittest.mock as mock

    with mock.patch("tornado.ioloop.IOLoop", mock.MagicMock()) as mock_ioloop:
        _Connector(None, None).clear_timeout()



# Generated at 2022-06-22 13:29:39.202882
# Unit test for method start of class _Connector
def test__Connector_start():
    resolver=Resolver()
    io_loop=IOLoop()
    io_loop.make_current()
    connect=lambda x,y: (IOStream(socket.socket(x, socket.SOCK_STREAM), io_loop), Future())
    addrinfo=[(socket.AF_INET, ("192.160.0.1", 0)), (socket.AF_INET, ("192.160.0.2", 1))]
    connector=_Connector(addrinfo, connect) 

# Generated at 2022-06-22 13:29:51.389567
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import time
    import unittest
    import tempfile
    import functools
    from tornado.ioloop import IOLoop
    from tornado.netutil import bind_unix_socket
    from tornado.testing import AsyncTestCase

    class ConnectorTest(AsyncTestCase):
        def setUp(self):
            super(ConnectorTest, self).setUp()
            # Python 2 doesn't have a non-blocking bind option for AF_UNIX
            # sockets, so we use a temp file.
            self.socket, self.path = bind_unix_socket(tempfile.mktemp(), mode=0o600)

        def make_connector(self):
            return _Connector(
                [(socket.AF_UNIX, (self.path,))],
                self._make_connection_callback,
            )


# Generated at 2022-06-22 13:30:00.137848
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    class MockTCPConnector(_Connector):
        def __init__(
            self,
            addrinfo: List[Tuple],
            connect: Callable[
                [socket.AddressFamily, Tuple], Tuple[IOStream, "Future[IOStream]"]
            ],
        ) -> None:
            _Connector.__init__(self, addrinfo, connect)

    connector = MockTCPConnector([], None)
    class MockIOLoop():
        def __init__(self):
            self.remove_calls = []

        def remove_timeout(self, *args, **kwargs):
            self.remove_calls.append((args, kwargs))

    mock_io_loop = MockIOLoop()
    connector.io_loop = mock_io_loop
    class MockTimeout():
        pass
    timeout = MockTimeout

# Generated at 2022-06-22 13:30:08.143523
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    io_loop = IOLoop.current()

    # Test for case future is done
    future = Future()
    future.set_result(1)
    _connector = _Connector([], lambda a, b: None)
    _connector.future = future

    _connector.on_connect_timeout()

    # Test for case future is not done
    future = Future()
    future.set_result(1)
    _connector = _Connector([], lambda a, b: None)
    _connector.future = future

    _connector.on_connect_timeout()



# Generated at 2022-06-22 13:30:16.979737
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    io_loop = IOLoop.current()
    future = Future()
    def connect(af:int, addr:Tuple)->Tuple[IOStream, Future[IOStream]]:
        future.set_result(True)
        return (IOStream(socket.socket(), io_loop=io_loop), future)
    connector = _Connector([(1, 1)], connect)
    connector.io_loop = io_loop
    addrs = iter([(0, 1)])
    connector.try_connect(addrs)
    assert future.result() == True



# Generated at 2022-06-22 13:30:17.582212
# Unit test for method start of class _Connector
def test__Connector_start():
    pass



# Generated at 2022-06-22 13:30:20.064067
# Unit test for method start of class _Connector
def test__Connector_start():
    # _Connector.start(timeout=_INITIAL_CONNECT_TIMEOUT, connect_timeout=None) -> Future[Tuple[socket.AddressFamily, Any, IOStream]]
    ...



# Generated at 2022-06-22 13:30:26.323135
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    _Connector(
        addrinfo=[(socket.AF_INET, ('dns', 'bj99y.com'))],
        connect=lambda af, addr: (IOStream(socket.socket(af, socket.SOCK_STREAM)),
                                  Future())).on_connect_done(iter([(socket.AF_INET, ('dns', 'bj99y.com'))]),
                                                             socket.AF_INET,
                                                             ('dns', 'bj99y.com'),
                                                             Future())



# Generated at 2022-06-22 13:30:37.711161
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    import time
    import tornado.testing

    # Stream is a class in iostream module whereas the method accepts IOStream
    # obj as its argument. Hence we need to mock it
    # Stream class
    class Stream:
        pass

    # Future is in concurrent module
    # Future class
    class Future:
        value_set = False

        def __init__(self, value=None):
            self.value = value

        def set_exception(self, value):
            self.value = value
            self.value_set = True

    # IOLoop is in ioloop module
    # IOLoop class
    class IOLoop:
        add_timeout_called_count = 0
        remove_timeout_called_count = 0
        time_return_value = None
        timeout_add_count = 0

# Generated at 2022-06-22 13:30:47.926377
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import unittest
    from unittest.mock import patch, call

    testcase = unittest.TestCase()

    ###########################################################################
    # patched functions and classes

    class IOLoopStub():
        """Stub for tornado.ioloop.IOLoop"""

        def __init__(self):
            self.called_time_function = False
            self.time_return_value = None  # type: Optional[float]
            self.called_add_timeout = False
            self.called_remove_timeout = False
            self.called_close = False
            self.called_set_timeout = False

        def time(self) -> float:
            self.called_time_function = True
            return self.time_return_value


# Generated at 2022-06-22 13:32:36.591212
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.httpclient import AsyncHTTPClient
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncHTTPTestCase
    import tornado.web
    import tornado.gen
    import tornado.platform.asyncio
    import asyncio

    class MainHandler(tornado.web.RequestHandler):
        @tornado.web.asynchronous
        @tornado.gen.coroutine
        def get(self):
            self.finish("Hello, world")

    class TestTCPClient(AsyncHTTPTestCase):
        def hello(self, response):
            if response.error:
                raise Exception("Error: %s" % response.error)
            self.stop()

        def get_app(self):
            return tornado.web.Application([(r"/", MainHandler)])


# Generated at 2022-06-22 13:32:38.056150
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    @gen.coroutine
    def f():
        TCPClient.connect(host="127.0.0.1", port=22)
    gen.run_until_complete(f())



# Generated at 2022-06-22 13:32:47.940202
# Unit test for method start of class _Connector
def test__Connector_start():
    class FakeFuture(Future):
        def __init__(self) -> None:
            self.result = None  # type: Any

        def result(self, timeout: Optional[Union[float, datetime.timedelta]] = None) -> Any:
            return self.result

    class FakeIOStream(IOStream):
        def __init__(self, fake_future: FakeFuture) -> None:
            self.write_callback = None  # type: Optional[Callable[..., Any]]
            self.read_callback = None  # type: Optional[Callable[..., Any]]
            self.future = fake_future
            self.on_connect_timeout_called = False  # type: bool
            self.on_timeout_called = False  # type: bool


# Generated at 2022-06-22 13:32:52.035476
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    async def test_func():
        # two address are resolved for the hostname
        client = TCPClient()
        stream = await client.connect("www.google.com", 80)
        print(f"Connected to google: {stream.socket}")
        stream.close()

    try:
        import tornado.ioloop

        tornado.ioloop.IOLoop.current().run_sync(test_func)
    except RuntimeError:
        # tornado is not installed, skip this test
        pass


if __name__ == "__main__":
    test_TCPClient_connect()

# Generated at 2022-06-22 13:32:58.859739
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    test_streams = [IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                    for i in range(2)]
    test_callback = _Connector(list(), lambda x, y: (x, y))
    test_callback.streams = set(test_streams)
    test_callback.close_streams()
    assert test_streams[0].socket is None and test_streams[1].socket is None


# Generated at 2022-06-22 13:33:05.715399
# Unit test for method start of class _Connector
def test__Connector_start():
    addrinfo = [(4, (1, 2, 3, 4)), (5, (1, 2, 3, 4))]
    connect = lambda af, addr: (None, None)
    connector = _Connector(addrinfo, connect)
    connector.start()

    addrinfo = [(4, (1, 2, 3, 4))]
    connector = _Connector(addrinfo, connect)
    connector.start()

    addrinfo = []
    connector = _Connector(addrinfo, connect)
    connector.start()


# Generated at 2022-06-22 13:33:12.398344
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    first_stream = IOStream()
    second_stream = IOStream()
    connector = _Connector([(1,1), (2,2)], lambda x,y: (first_stream, Future()))
    connector.streams.add(first_stream)
    connector.streams.add(second_stream)
    assert(first_stream.closed is False)
    assert(second_stream.closed is False)
    connector.close_streams()
    assert(first_stream.closed is True)
    assert(second_stream.closed is True)



# Generated at 2022-06-22 13:33:23.497404
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import unittest
    from tornado.testing import gen_test

    class test__Connector_on_connect_done(unittest.TestCase):
        @gen_test
        async def test(self):
            from typing import Tuple
            from tornado import gen
            from tornado.iostream import IOStream
            from tornado.platform.asyncio import to_asyncio_future

            def connect(af, addr):
                from tornado.iostream import IOStream
                from tornado.platform.asyncio import to_asyncio_future

                future = to_asyncio_future(Future())

                def _connect():
                    future.set_exception(TimeoutError())

                IOLoop.current().call_later(0.1, _connect)
                return IOStream(socket.socket()), future


# Generated at 2022-06-22 13:33:26.702552
# Unit test for method start of class _Connector

# Generated at 2022-06-22 13:33:33.612185
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    def print_result(future):
        print('stream:', future.result())
    tcp_client = TCPClient()
    timeout = datetime.timedelta(seconds=3)
    # address = 'www.example.com', port = 80
    # timeout for connection, 3 seconds
    # The current program will continue to run after the connection is successful.
    tcp_client.connect('www.example.com', 80, timeout = timeout).add_done_callback(print_result)
    IOLoop.current().start()

# Generated at 2022-06-22 13:33:55.887197
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    async def async_test_TCPClient_connect():
        resolver = Resolver()
        client = TCPClient(resolver)
        stream = await client.connect('www.correodelsur.com', 80)
        assert isinstance(stream, IOStream), "stream is not a IOStream object"
        stream.close()
        client.close()
    IOLoop.current().run_sync(async_test_TCPClient_connect)


# Generated at 2022-06-22 13:34:04.386700
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from tornado import testing
    from tornado.options import options
    from tornado.iostream import StreamClosedError
    import sys
    import os

    options = options
    class DummyIOLoop():
        """Unit test for method close_streams of class _Connector
        """
        def add_timeout(self, p_timeout: Union[float, Union[float, datetime.timedelta]], func) -> None:
            pass
        def time(self) -> datetime.datetime:
            return datetime.datetime.now()
        def remove_timeout(self, p_timeout: object) -> None:
            pass

    class DummyResolver(Resolver):
        """Unit test for method close_streams of class _Connector
        """
        def __init__(self):
            pass

# Generated at 2022-06-22 13:34:10.164590
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    """
    This function tests the TCPClient() function connect
    """
    print("Testing TCPClient() function connect")
    myTCPClient = TCPClient()
    result = myTCPClient.connect('127.0.0.1', 8080)
    assert (result == None)
    print("Successful")


# Generated at 2022-06-22 13:34:11.961391
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    pass



# Generated at 2022-06-22 13:34:16.160348
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    try:
        loop = IOLoop.current()
        client = TCPClient()
        stream = client.connect('www.tornadoweb.org', 80)
        stream.read_until_close(streaming_callback=print)
        print(stream)
        loop.start()
    finally:
        loop.close()



# Generated at 2022-06-22 13:34:24.447796
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    from io import BytesIO
    import ssl
    import socket
    import unittest
    import pytest
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    import asyncio
    from tornado.iostream import StreamClosedError
    from pytype.pyc import AsyncGenerator
    from tornado.netutil import _ClientIOStream,_Connector
    import ssl
    import socket
    def error_callback(f):
        print("got error")
        #print(f.result())
        #print(f.exception())
        #raise f.exception()
    def get_cert(addr):

        return (addr,None)

# Generated at 2022-06-22 13:34:35.502989
# Unit test for method start of class _Connector
def test__Connector_start():
    import socket
    import tornado.gen
    import tornado.testing
    import unittest
    from tornado.iostream import StreamClosedError

    # type: ignore
    class TestTCPClient(tornado.testing.AsyncTestCase):
        def test_client_timeout(self):
            self.set_timeout(2)
            with self.assertRaises(TimeoutError):
                with TCPClient(io_loop=self.io_loop) as client:
                    yield client.connect(
                        "google.com", 1234, timeout=_INITIAL_CONNECT_TIMEOUT
                    )

        def test_client_timeout_callback(self):
            # type: (...) -> None
            # Add a callback to the timeout error to verify that it
            # runs after the timeout occurs.
            future = Future()


# Generated at 2022-06-22 13:34:37.853124
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    addrs=[]
    connect =None
    _Connector(addrs,connect).try_connect()
    assert True



# Generated at 2022-06-22 13:34:43.516359
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    docker_ports = [5000, 5001, 5002, 5003]
    vip = "127.0.0.1"
    port = docker_ports[0]
    client = TCPClient()
    stream = client.connect(vip, port)
    stream.write(b"hello world!")
    stream.close()
test_TCPClient_connect()


# Generated at 2022-06-22 13:34:53.950643
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    def connect_fail(af, addr):
        future = Future()
        future.set_exception(Exception("connect fail"))
        return IOStream(socket.socket()), future
    # Test primary addrs
    c = _Connector(
        [(2, ("127.0.0.1", 8080)), (2, ("127.0.0.2", 8080)), (2, ("127.0.0.3", 8080))],
        connect_fail,
    )
    c.try_connect(iter(c.primary_addrs))
    assert (
        c.future.result()[2].socket.getpeername() == ("127.0.0.1", 8080)
    ), "try_connect test fail!"


_NO_RESULT = object()



# Generated at 2022-06-22 13:35:41.721192
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import asyncio
    async def f():
        tcp=TCPClient()
        stream=await tcp.connect("localhost",12345,af=socket.AF_INET)
        return stream
    stream=asyncio.run(f())
    print("print stream:",stream)

# Generated at 2022-06-22 13:35:50.803230
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import sys
    import os
    import unittest
    import unittest.mock
    from argparse import ArgumentParser

    TEST_HOST = "www.google.com"
    TEST_PORT = 80
    TEST_ADDR_INFO = [
        (socket.AF_INET, ("216.58.217.110", 80)),
        (socket.AF_INET6, ("2607:f8b0:4009:806::2004", 80))
    ]

    test_cases = (
        ("Test IOError", lambda _: (None, unittest.mock.Mock()), IOError),
        ("Test TimeoutError", lambda _: unittest.mock.Mock(), TimeoutError),
    )

    def gen_connect(io_stream):
        def connect(af, addr):
            return

# Generated at 2022-06-22 13:35:51.227331
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    pass



# Generated at 2022-06-22 13:36:02.030320
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    from tornado.iostream import IOStream
    from tornado.platform.auto import set_close_exec
    from tornado.testing import bind_unused_port, AsyncTestCase, get_unused_port

    from typing import Any, Tuple, List
    import socket
    import random
    import time
    from tornado.netutil import add_accept_handler

    # 1.
    # test that try_connect works for all test cases in cpython

    # 1.1.
    # test that try_connect creates IOStream.close() properly
    # test that try_connect creates IOStream.socket.fileno() properly
    # test that IOStream.close() closes IOStream.socket

    class UnstableNetwork(object):
        """An unstable network connection (or a set of connections)
        """


# Generated at 2022-06-22 13:36:13.317779
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    resolver = Resolver()
    def connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[IOStream, "Future[IOStream]"]:
        stream = IOStream()
        future = stream.connect(af, addr)
        future_add_done_callback(future, lambda f: stream.set_close_callback(None))
        return stream, future

    addrinfo = resolver.resolve("localhost", 80)
    connector = _Connector(addrinfo, connect)
    stream, future = connector.connect(connector.primary_addrs[0])
    assert future.done()
    assert connector.streams == {stream}
    connector.close_streams()
    assert stream.closed()



# Generated at 2022-06-22 13:36:22.993960
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import unittest

    from .stream import TCPClient
    from .socket import create_connection

    class Test_Connector(unittest.TestCase):
        def test_on_connect_done(self):
            future = Future()
            addrinfo = [("1.1.1.1", "80"), ("2.2.2.2", "80")]
            s = _Connector(addrinfo, create_connection)
            s.try_connect(iter(s.primary_addrs))
            s.on_connect_done(iter(s.primary_addrs), "1.1.1.1", "80", future)
            self.assertEqual(s.future.result(), (("1.1.1.1", "80"),))

    unittest.main()



# Generated at 2022-06-22 13:36:29.331319
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    # Create a mock object of class Future to test the on_connect_done method
    future = _Future_Mock()
    # Create a mock object of class Iterator to test the on_connect_done method
    addrs = _Iterator_Mock()
    # Create a mock object of class IOStream to test the on_connect_done method
    stream = _IOStream_Mock()
    af = socket.AddressFamily.AF_INET
    addr = ('addr', 1)
    # Test the case when the result of future is successful
    future.result = stream
    test_connector = _Connector([], lambda x, y: None)
    # Verify the initial state of the test object
    assert test_connector.io_loop == IOLoop.current()
    assert test_connector.remaining == 1

# Generated at 2022-06-22 13:36:33.625922
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    # Test type hinting and mypy
    def connect(
        addrfamily: socket.AddressFamily, address: Tuple[str, int]
    ) -> Tuple[IOStream, Future[IOStream]]:
        return IOStream(socket.socket()), Future()

    connector = _Connector([(AF_INET, ("127.0.0.1", 80))], connect)
    connector.try_connect([(AF_INET, ("127.0.0.1", 80))])
    print("test__Connector_try_connect done")



# Generated at 2022-06-22 13:36:36.799473
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    with IOStream() as stream:
        with _Connector(((4, ("8.8.8.8", 53)), (6, ("2001:4860:4860::8888", 53))), None) as connector:
            connector.streams = set([stream])
            connector.close_streams()



# Generated at 2022-06-22 13:36:37.783732
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    pass


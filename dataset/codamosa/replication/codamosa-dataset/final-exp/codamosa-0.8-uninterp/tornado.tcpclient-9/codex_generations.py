

# Generated at 2022-06-22 13:27:48.225766
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    pass



# Generated at 2022-06-22 13:27:56.393986
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    try:
        msg = test__Connector_on_connect_done.__name__ + " "
        e = Exception(msg)
        addrs = iter([1, 2])
        af, addr = 1, 2
        future = Future()
        future.set_exception(e)
        c = _Connector([], None)
        c.on_connect_done(addrs, af, addr, future)
        assert False
    except Exception as e:
        if msg == str(e):
            assert True
        else:
            assert False



# Generated at 2022-06-22 13:28:08.591580
# Unit test for constructor of class _Connector
def test__Connector():
    # prepare
    addrinfo: List[Tuple] = [(4, ("127.0.0.1", 3306))]
    connect: Callable[
        [socket.AddressFamily, Tuple], Tuple[IOStream, "Future[IOStream]"]
    ] = lambda af, addr: (
        IOStream(socket.socket(af, socket.SOCK_STREAM, 0), io_loop=IOLoop.current()),
        Future(),
    )
    
    # construct
    connector = _Connector(addrinfo, connect)

    # check result
    assert isinstance(connector.io_loop, IOLoop)
    assert isinstance(connector.connect, Callable)
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector

# Generated at 2022-06-22 13:28:20.650914
# Unit test for method split of class _Connector
def test__Connector_split():
    # this example is copied from the split() method
    addrinfo0 = [
        (socket.AF_INET, ('1.2.3.4', 8888)),
        (socket.AF_INET6, ('fd::1', 8888)),
    ]
    case0 =_Connector.split(addrinfo0)
    assert case0[0] == [(socket.AF_INET, ('1.2.3.4', 8888))], 'case0[0] test failed'
    assert case0[1] == [
        (socket.AF_INET6, ('fd::1', 8888))
    ], 'case0[1] test failed'
    # this example is copied from the split() method

# Generated at 2022-06-22 13:28:31.610771
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from tornado.tcpclient import TCPClient
    from tornado import testing
    from tornado import platform
    from tornado.netutil import bind_sockets
    from threading import Thread

    # BEGIN OF TESTING
    # ---------------
    # STEP 1: Start a server
    server_port = 20001

    server_socket, _ = bind_sockets(server_port)
    server_socket.listen(5)

    def server_thread():
        testing.gen_test(server_loop())()

    def server_loop():
        while True:
            conn, addr = server_socket.accept()
            # conn.send(b'data')
            # conn.close()
            pass

    thread = Thread(target=server_thread)
    thread.start()
    # ---------------

    # STEP 2: Create a TCP client and try

# Generated at 2022-06-22 13:28:39.295240
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    class _Connector(object):
        """A stateless implementation of the "Happy Eyeballs" algorithm.

        "Happy Eyeballs" is documented in RFC6555 as the recommended practice
        for when both IPv4 and IPv6 addresses are available.

        In this implementation, we partition the addresses by family, and
        make the first connection attempt to whichever address was
        returned first by ``getaddrinfo``.  If that connection fails or
        times out, we begin a connection in parallel to the first address
        of the other family.  If there are additional failures we retry
        with other addresses, keeping one connection attempt per family
        in flight at a time.

        http://tools.ietf.org/html/rfc6555

        """


# Generated at 2022-06-22 13:28:50.044391
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    from tornado.testing import AsyncTestCase, get_unused_port
    import tornado
    import sys

    class _ConnectorOnTimeoutTestCase(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.sock, self.port = tornado.testing.bind_unused_port()
            self.sock.listen(1)

            def on_accept(f):
                stream, addr = f.result()
                stream.close()

            # accept on server side
            self.server_accept = self.io_loop.add_future(
                self.accept_connection(self.sock), on_accept
            )

        def tearDown(self):
            super().tearDown()
            self.sock.close()


# Generated at 2022-06-22 13:28:57.978118
# Unit test for constructor of class _Connector
def test__Connector():
    io_loop = IOLoop.current()
    ip_address = "8.8.8.8"
    port = 80
    addrinfo = [(socket.AF_INET, (ip_address, port))]

    def test_connect(af: socket.AddressFamily, addr: Any) -> Tuple[IOStream, "Future[IOStream]"]:
        s = socket.socket(af, socket.SOCK_STREAM, 0)
        stream = IOStream(s, io_loop=io_loop)
        return stream, stream.connect(addr)

    connector = _Connector(addrinfo, test_connect)
    connector.start()
    assert connector.future.done()
    assert connector.future.result() is not None
    assert connector.future.result()[0] == socket.AF_INET
    assert connector.future

# Generated at 2022-06-22 13:28:58.956920
# Unit test for method start of class _Connector
def test__Connector_start():
    pass



# Generated at 2022-06-22 13:29:08.661917
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    # type: () -> None
    io_loop = IOLoop()
    io_loop.make_current()

    def connect(af, addr):
        s = socket.socket(af, socket.SOCK_STREAM)
        stream = IOStream(s)
        future = Future()
        future.set_exception(IOError("fake error"))
        return (stream, future)

    addrinfo = [
        (socket.AF_INET, ("localhost", 0)),
        (socket.AF_INET6, ("localhost", 0)),
    ]

    connector = _Connector(addrinfo, connect)
    future = connector.start(timeout=0.05)
    io_loop.add_callback(future.result)
    io_loop.call_later(0.1, io_loop.stop)
    io_loop.start

# Generated at 2022-06-22 13:30:23.274558
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    connect_timeout = 0.5
    pass



# Generated at 2022-06-22 13:30:30.297644
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    from tornado.netutil import Resolver
    from tornado.netutil import bind_sockets, bind_unix_socket
    from tornado.testing import AsyncTestCase, bind_unix_socket, bind_sockets
    from tornado.iostream import IOStream
    from tornado.concurrent import Future
    import functools
    import socket
    import ssl

    def set_connect_timeout(self, connect_timeout):
        self.connect_timeout = self.io_loop.add_timeout(connect_timeout, self.on_connect_timeout)

    def on_connect_timeout(self):
        self.future.set_exception(TimeoutError())
        self.close_streams()
    

    from functools import partial
    from typing import Callable, List

    from tornado import gen

# Generated at 2022-06-22 13:30:42.168289
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import io
    import unittest
    import tornado

    from tornado.gen import sleep
    from tornado.iostream import IOStream
    from tornado.testing import AsyncTestCase, gen_test

    class Test_Connector(AsyncTestCase):
        def setUp(self):
            super().setUp()

            self.sock0 = io.BytesIO(b"")
            self.sock1 = io.BytesIO(b"")
            self.sock2 = io.BytesIO(b"")
            self.sock3 = io.BytesIO(b"")

            self.stream0 = IOStream(self.sock0)
            self.stream1 = IOStream(self.sock1)
            self.stream2 = IOStream(self.sock2)

# Generated at 2022-06-22 13:30:49.759478
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from unittest import mock

    m_IOStream = mock.Mock()
    m_IOStream.close = mock.Mock()

    m_Future = mock.Mock()
    m_Future.done = mock.Mock(return_value=False)
    m_Future.set_exception = mock.Mock()

    m_gen = mock.Mock()
    m_gen.TimeOutError = mock.Mock()
    m_gen.TimeOutError.return_value = "TimeOutError"

    m_ioloop = mock.Mock()
    m_ioloop.add_timeout = mock.Mock(return_value=m_ioloop._add_timeout_result)
    m_ioloop.time = mock.Mock(return_value=1)
    m_ioloop.remove_timeout = mock

# Generated at 2022-06-22 13:30:56.083613
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    foo = """
        if self.timeout is not None:
            self.io_loop.remove_timeout(self.timeout)
    """
    import ast
    if _check_ast(ast.parse(foo).body[0], "If"):
        print("True")
    else:
        print("False")
# Test unit is OK

# Test unit for method close_streams of class _Connector

# Generated at 2022-06-22 13:31:03.648602
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import pytest
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.iostream import IOStream
    from tornado.platform.asyncio import AsyncIOMainLoop
    import asyncio

    class TestTCPClient(AsyncTestCase):
        def setUp(self):
            AsyncIOMainLoop().install()
            super(TestTCPClient, self).setUp()
            self.loop = asyncio.get_event_loop()
            self.resolver = Resolver()
            self.resolver.install(self.io_loop)

        @gen.coroutine
        def run(self):
            stream, future = self.connect("127.0.0.1", 8888)
            self.assertEqual(stream.closed(), False)
           

# Generated at 2022-06-22 13:31:13.373508
# Unit test for method split of class _Connector
def test__Connector_split():
    # type: () -> None
    """Test case for _Connector.split method
    """
    import random
    import itertools
    import socket
    import tornado.testing

    af = {
        socket.AF_INET,
        socket.AF_INET6,
        socket.AF_UNIX,
        socket.AF_APPLETALK,
        socket.AF_IPX,
        socket.AF_IRDA,
    }
    addrinfo = []  # type: List[Tuple]
    for i in range(100):
        address_family = random.sample(af, 1)[0]
        addrinfo.append((address_family, i))
    if len(addrinfo) % 2 or len(addrinfo) > 50:
        # len(addrinfo) has to be even number and less than 50
        raise tornado

# Generated at 2022-06-22 13:31:25.866290
# Unit test for method start of class _Connector
def test__Connector_start():
    from .example_server import ExampleServer

    # Typing
    from typing import Any

    def connect(self, af: socket.AddressFamily, addr: Tuple) -> Tuple[socket.AddressFamily, Any]:
        return (af, addr)

    # Creating ExampleServer
    server = ExampleServer()
    server_port = server.bind(8888)

    addrinfo = [(af, (host, port)) for af, socktype, proto, canonname, (host, port) in socket.getaddrinfo(
        "localhost", server_port) if af in (socket.AF_INET, socket.AF_INET6)]

    connector = _Connector(addrinfo, connect)

    result_future = connector.start(0.3, None)
    assert result_future.result()[2] == None



# Generated at 2022-06-22 13:31:29.281167
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    # Setup
    stream = _Connector.try_connect(iter)
    bad_stream = None
    
    # Unit under test
    connected_stream = _Connector.on_connect_done(iter, stream, bad_stream)
    
    assert connected_stream == stream



# Generated at 2022-06-22 13:31:37.996086
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 8888))]
    _connector = _Connector(addrinfo, None)
    def connect(sock_family, addr) -> Tuple[IOStream, "Future[IOStream]"]:
        stream = IOStream(socket.socket(sock_family, socket.SOCK_STREAM))
        future = Future()
        stream.set_close_callback(lambda :future.set_exception(TimeoutError()))
        return stream, future
    _connector.connect = connect
    _connector.set_connect_timeout(0.5)
    _connector.start()
    IOLoop.current().run_sync(lambda :_connector.future)



# Generated at 2022-06-22 13:32:10.455245
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado import testing
    from tornado.testing import AsyncTestCase, gen_test
    import tornado
    import sys
    import os
    # Create a test application
    application = tornado.web.Application([])
    # Create an instance of an IOLoop
    io_loop = tornado.ioloop.IOLoop.current()
    # Start the IOLoop
    io_loop.start()
    # Stop the IOLoop after test
    io_loop.stop()



# Generated at 2022-06-22 13:32:16.952356
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import unittest

    class TestTCPClient(unittest.TestCase):
        def setUp(self):
            self.connector = _Connector(
                [
                    ("AF_INET", ("www.google.com", 80)),
                    ("AF_INET6", ("www.google.com", 80)),
                ],
                connect=self.connect
            )
            self.remaining = None  # type: Optional[int]
            self.last_error = None  # type: Optional[Exception]


# Generated at 2022-06-22 13:32:26.454982
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    def _future_add_done_callback(future, callback):
        if not future.done():
            future.add_done_callback(callback)
        else:
            callback(future)

    def _functools_partial(func, *args):
        return functools.partial(func, *args)


# Generated at 2022-06-22 13:32:34.225704
# Unit test for method start of class _Connector
def test__Connector_start():
    def test_param(
        timeout: float = _INITIAL_CONNECT_TIMEOUT,
        connect_timeout: Optional[Union[float, datetime.timedelta]] = None,
    ) -> None:
        self = _Connector(addrinfo, connect)
        a = timeout
        b = connect_timeout
        return self.start(
            a,
            b,
        )
    addrinfo = [
        (1, (2, 3)),
        (4, (5, 6)),
        (7, (8, 9)),
    ]
    def connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[Any, Any]:
        return af, addr
    return test_param


# Generated at 2022-06-22 13:32:43.587177
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    from tornado.testing import AsyncTestCase, ExpectLog, gen_test, bind_unused_port

    def make_socket():
        server_fd, port = bind_unused_port()
        stream = IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0),
                          io_loop=self.io_loop)
        stream.set_close_callback(lambda: server_fd.close())
        stream.connect(("127.0.0.1", port), self.stop)
        return stream

    @gen_test
    def test_clear_timeout():
        sock = make_socket()
        yield sock.read_until_close()
        yield self.close()


# Generated at 2022-06-22 13:32:49.249856
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    print("test__Connector_try_connect ... ", end='')

    import mock
    import tempfile
    import time

    class MyFuture(Future):
        def __init__(self, timeout) -> None:
            super().__init__()
            self.timeout = timeout

        def result(self, timeout=None) -> Union[None, IOStream]:
            if self.timeout:
                time.sleep(self.timeout)
            else:
                time.sleep(0.01)
            if self.exception():
                raise self.exception()
            elif self.done():
                return IOStream(mock.Mock(), mock.Mock())
            return None


# Generated at 2022-06-22 13:32:54.620634
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    #default init of TCP Client
    my_TCPClient = TCPClient()
    #Mock the object for test
    my_TCPClient.resolver.resolve = lambda host, port: [
        [
            (socket.AF_INET , ("localhost",5000)),
            (socket.AF_INET , ("localhost",6000))
        ]
    ]
    my_TCPClient._create_stream = lambda max_buffer_size, af, addr, source_ip=None, source_port=None: [
        IOStream(socket.socket(af)),
        [
            IAStream(socket.socket(af)),
            IAStream(socket.socket(af))
        ]
    ]
    my_SSLIOStream = SSLIOStream(IOStream(socket.socket(socket.AF_INET)),{})
    my_SSLIOStream

# Generated at 2022-06-22 13:33:06.421123
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    from tornado.iostream import BaseIOStream
    from unittest import mock

    # Fake class for IOStream
    class FakeStream(BaseIOStream):
        def __init__(self,
                     loop: IOLoop,
                     sock: socket.socket,
                     max_buffer_size: Union[
                         int, float
                     ] = None) -> None:
            super().__init__(sock,
                             max_buffer_size=max_buffer_size,
                             read_chunk_size=256,
                             loop=loop)


# Generated at 2022-06-22 13:33:12.326404
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    @gen.coroutine
    def fake_connect(af, addr):
        raise gen.Return(addr)

    # No error
    connector = _Connector([(1, (1, 2)), (2, (3, 4)), (1, (5, 6))], fake_connect)
    future = connector.start()
    future.add_done_callback(lambda f: f.result())
    yield future

    # Error
    connector = _Connector([(1, (1, 2)), (2, (3, 4)), (1, (5, 6))], fake_connect)
    future = connector.start()
    future.add_done_callback(lambda f: f.result())
    with pytest.raises(Exception) as e:
        yield future
        assert e == IOError



# Generated at 2022-06-22 13:33:23.497196
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import time
    # server IP & PORT
    s_host = '127.0.0.1'
    s_port = 5555
    # client IP & PORT
    c_host = '127.0.0.1'
    c_port = 6666
    # count of test case
    count = 0
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # bind to the port
    s.bind((s_host, s_port))
    # queue up to 5 requests
    s.listen(5)
    client_obj=TCPClient()
    server_thread=threading.Thread(target=server_send_msg,args=(s,))
    server_thread.setDaemon(True)
    server_thread.start

# Generated at 2022-06-22 13:36:24.281587
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    inet_socket = socket.socket(socket.AF_INET)
    inet_socket.close()
    inet_socket = socket.socket(socket.AF_INET6)
    inet_socket.close()
    inet_socket = socket.socket(socket.AF_LOCAL)
    inet_socket.close()
    inet_socket = socket.socket(socket.AF_PACKET)
    inet_socket.close()
    inet_socket = socket.socket(socket.AF_UNIX)
    inet_socket.close()

# Generated at 2022-06-22 13:36:35.967333
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    test_streams = [IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]


# Generated at 2022-06-22 13:36:43.235430
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():

    @gen.coroutine
    def connect(af, addr):
        return

    addrs = [1, 2, (socket.AF_INET, (1, 2, 3, 4)), (socket.AF_INET, (1, 2, 3, 4))]
    addrs_iter = iter(addrs)

    connector = _Connector(addrs, connect)

    connector.remaining = len(addrs)
    connector.last_error = None
    connector.future.done()

    connector.try_connect(addrs_iter)

    @gen.coroutine
    def callback_connect(addrs):
        return

    future = connector.connect(socket.AF_INET, (1, 2, 3, 4))


# Generated at 2022-06-22 13:36:54.575718
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado.testing

    class TestTCPClient(tornado.testing.AsyncTestCase):
        def test_TCPClient(self):
            io_loop = tornado.ioloop.IOLoop.current()
            client = TCPClient()
            connect = client.connect
            host = 'www.tornadoweb.org'
            port = 80
            af = socket.AF_UNSPEC
            ssl_options = None
            max_buffer_size = None
            source_ip = None
            source_port = None
            timeout = None
            result = connect(host, port, af, ssl_options, max_buffer_size, source_ip, source_port, timeout)
            result.close()

    t = TestTCPClient()
    t.test_TCPClient()

# Generated at 2022-06-22 13:36:55.628615
# Unit test for method start of class _Connector
def test__Connector_start():
    pass



# Generated at 2022-06-22 13:36:59.316405
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    resolver = Resolver()
    tcp = TCPClient(resolver)
    port = 8089
    host = "127.0.0.1"
    stream = tcp.connect(host, port)
    print(stream.socket())

# Generated at 2022-06-22 13:37:07.521902
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado.platform.asyncio
    import tornado.platform.asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    from tornado.platform.asyncio import to_asyncio_future
    client = TCPClient()
    af = socket.AddressFamily(2)
    addr = (1,2)
    ssl_options = ssl.SSLContext()
    max_buffer_size = 5
    source_ip = "127.0.0.1"
    source_port = 0
    host = "tornado"
    port = 80
    timeout = _INITIAL_CONNECT_TIMEOUT
    addrinfo = [(af,addr),(af,addr)]

    client = TCPClient()
    resolver = Resolver()
    client.resolver = resolver
    client._own_res

# Generated at 2022-06-22 13:37:16.049340
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import tornado.testing
    from tornado.tcpclient import TCPClient, _Connector, _TcpClientImpl
    from tornado.concurrent import Future
    import tornado.platform.asyncio
    import asyncio
    import mock
    import socket
    import functools

    @gen.coroutine
    def f():
        def connect(af, addr):
            return (
                IOStream(socket.socket(af, socket.SOCK_STREAM, 0),
                         io_loop=IOLoop.current()),
                Future(),
            )

        af = 0
        addr = (0, 0)
        addrs = iter([(af, addr)])
        connector = _Connector(addrs, connect)
        stream, future = connector.connect(af, addr)

# Generated at 2022-06-22 13:37:28.244119
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    async def async_connect(host, port, af=socket.AF_UNSPEC, ssl_options=None,
                      max_buffer_size=None, source_ip=None, source_port=None, timeout=None):
        tcpcl = TCPClient()
        return await tcpcl.connect(host, port, af=af, ssl_options=ssl_options,
                      max_buffer_size=max_buffer_size, source_ip=source_ip, source_port=source_port, timeout=timeout)
    ###################################################################################
    ###########                                                               ##########
    ###########                    TESTING OF CONNECT                         ##########
    ###########                                                               ##########
    ###################################################################################
    import tornado.testing

    import tornado.web
    import tornado.websocket
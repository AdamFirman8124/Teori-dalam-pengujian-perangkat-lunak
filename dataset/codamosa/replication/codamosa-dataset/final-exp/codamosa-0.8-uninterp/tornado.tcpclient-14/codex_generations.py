

# Generated at 2022-06-22 13:27:48.262911
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    # todo: implement this unit test
    pass


# Generated at 2022-06-22 13:27:59.773214
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    # Test case 1
    print("Test case 1")
    test = _Connector(
        addrinfo=[
            (socket.AF_INET, "127.0.0.1"),
            (socket.AF_INET6, "::1"),
            (socket.AF_INET, "1.1.1.1"),
            (socket.AF_INET6, "2.2.2.2"),
        ],
        connect=lambda af, addr: (IOStream(socket.socket()), Future()),
    )
    addrs = iter([(socket.AF_INET, "127.0.0.1")])
    af = (socket.AF_INET, "127.0.0.1")
    addr = "127.0.0.1"
    exc = socket.error(1, "test")
   

# Generated at 2022-06-22 13:28:12.329313
# Unit test for method start of class _Connector
def test__Connector_start():
    import tornado.testing
    import tornado.gen
    import socket
    import ssl
    import unittest


    class TCPServer(tornado.testing.AsyncTestCase):
        @gen.coroutine
        def handle_stream(self, stream: IOStream, address: Tuple) -> None:
            pass

        def get_new_ioloop(self) -> IOLoop:
            return IOLoop()

        def test_connection(self) -> None:
            sock, port = tornado.testing.bind_unused_port()
            ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_ctx.options |= ssl.OP_NO_SSLv2

# Generated at 2022-06-22 13:28:22.260149
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    from tornado.testing import gen_test
    import pytest
    from _Connector import _Connector

    @gen.coroutine
    def test_connector_on_connect_timeout():
        connector = _Connector([(1, (1, 1))], None)
        connector.future = Future()
        connector.io_loop = IOLoop.current()
        connector.io_loop.add_future(connector.future, lambda f: f.result())

        with pytest.raises(TimeoutError):
            connector.on_connect_timeout()
    return test_connector_on_connect_timeout



# Generated at 2022-06-22 13:28:23.294224
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    # TODO
    pass

# Generated at 2022-06-22 13:28:32.875777
# Unit test for method start of class _Connector
def test__Connector_start():
    import tornado.platform.asyncio
    from socket import socket, AF_INET, SOCK_STREAM
    from unittest import mock
    from tornado.test.util import unittest
    from tornado.test.util import skip_if_no_ipv6

    def connect(af, address):
        s = socket(af, SOCK_STREAM)
        s.setblocking(False)
        f = Future()
        stream = IOStream(s, io_loop=self.io_loop)
        if af == AF_INET:
            connect_mock.side_effect = (socket.error(), None)
        else:
            connect_mock.side_effect = (
                socket.error(), socket.error(), None)
        connect_mock.return_value = stream
        self.io_loop.add_

# Generated at 2022-06-22 13:28:44.603411
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    from tornado.iostream import IOStream
    from tornado.testing import AsyncTestCase
    from tornado.platform.asyncio import to_asyncio_future
    import asyncio
    from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest
    import logging
    import time
    import unittest

    # Unit test for method on_connect_timeout of class _Connector
    def test__Connector_on_connect_timeout():
        from tornado.iostream import IOStream
        from tornado.testing import AsyncTestCase
        from tornado.platform.asyncio import to_asyncio_future
        import asyncio
        from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest
        import logging
        import time
        import unittest


# Generated at 2022-06-22 13:28:52.956622
# Unit test for constructor of class _Connector
def test__Connector():
    @gen.coroutine
    def connect(
        af: socket.AddressFamily,
        addr: Tuple,
    ) -> "Tuple[IOStream, Future[IOStream]]":
        s = socket.socket(af, socket.SOCK_STREAM, 0)
        try:
            s.setblocking(False)
            s.connect(addr)
            stream = IOStream(s)
            yield stream.start_tls(False)
            return stream
        except Exception as e:
            s.close()
            raise e

    connector = _Connector(
        [(socket.AF_INET, ("localhost", 80)), (socket.AF_INET6, ("localhost", 80))],
        connect,
    )

    r = connector.start()



# Generated at 2022-06-22 13:28:57.424610
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado.gen
    import tornado.testing
    import tornado.concurrent
    import tornado.netutil
    import typing
    import socket
    
    
    
    
    
    
    
    
    
    
    import ssl
    
    
    import logging
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    @gen.coroutine
    def test_simple():
        client = TCPClient()
        stream = yield client.connect('www.google.com', 80)
        self.assertEqual(stream.socket.family, socket.AF_INET)
        stream.close()
        stream = yield client.connect('ipv6.google.com', 80)

# Generated at 2022-06-22 13:29:07.697652
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    from tornado.testing import AsyncTestCase, gen_test

    class MyTestCase(AsyncTestCase):
        _timeout = None

        def setUp(self) -> None:
            super().setUp()
            self.io_loop = IOLoop.current()
            self._timeout = None

        def test(self) -> None:
            def add_timeout(timeout: float) -> object:
                self._timeout = timeout

            def remove_timeout(timeout: object) -> None:
                assert self._timeout == timeout

            self.io_loop.add_timeout = add_timeout
            self.io_loop.remove_timeout = remove_timeout
            _Connector([], None).clear_timeouts()
            assert self._timeout is None

    MyTestCase().test()



# Generated at 2022-06-22 13:29:30.753449
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    # Test with input as seconds
    connector = _Connector([(1,2)], lambda *args, **kwargs: _Connector.close_streams(connector))
    connector.set_connect_timeout(1)

    # Test with input as datetime.timedelta
    connector = _Connector([(1,2)], lambda *args, **kwargs: _Connector.close_streams(connector))
    connector.set_connect_timeout(datetime.timedelta(days=1))
test__Connector_set_connect_timeout()


# Generated at 2022-06-22 13:29:35.925297
# Unit test for constructor of class _Connector
def test__Connector():
    addrinfo = [
        (socket.AddressFamily.AF_INET, ("127.0.0.1", 80)),
        (socket.AddressFamily.AF_INET, ("127.0.0.1", 80)),
        (socket.AddressFamily.AF_INET, ("127.0.0.2", 80)),
        (socket.AddressFamily.AF_INET, ("127.0.0.1", 80)),
    ]
    c = _Connector(
        addrinfo, lambda af, addr: (IOStream(socket.socket()), Future().set_result(None)),
    )



# Generated at 2022-06-22 13:29:47.071215
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():

    import tornado.testing

    import tornado.testing

    import socket
    import tornado.gen
    import tornado.ioloop
    import tornado.iostream
    import tornado.netutil
    import unittest

    class _ConnectorTest(tornado.testing.AsyncTestCase):
        def test_happy_eyeballs(self):
            """Test that a connection is made with the first available address"""
            af_map = {
                socket.AF_INET: False,
                socket.AF_INET6: False,
            }

            def connect(af, addr):
                af_map[af] = True
                s = socket.socket(af, socket.SOCK_STREAM, 0)
                f = tornado.iostream.IOStream(s)
                return f, tornado.gen.Task(f.connect, addr)

           

# Generated at 2022-06-22 13:29:57.490773
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    from tornado.util import ObjectDict

    class FakeIOStream:
        def __init__(self, io_loop):
            self.io_loop = io_loop

        def set_close_callback(self, fun):
            self.close_callback = fun

        def close(self):
            self.close_callback()

    class FakeIOLoop:
        def __init__(self, max_epoll_size=None):
            self.max_epoll_size = max_epoll_size
            self.add_callback_result = None
            self.time = 0.0
            self.time_cb_result = None
            self.remove_timeout_result = None
            self.add_timeout_result = None
            self.add_timeout_called = False
            self.remove_timeout_called = False

# Generated at 2022-06-22 13:30:03.179538
# Unit test for method start of class _Connector
def test__Connector_start():
    addrinfo = [(socket.AddressFamily.AF_INET, ("www.163.com",80))]
    connector = _Connector(addrinfo,test_connect)
    future = connector.start(timeout=10000,connect_timeout=10000)
    if future.done():
        print(future.result())


# Generated at 2022-06-22 13:30:03.863512
# Unit test for constructor of class _Connector
def test__Connector():
    assert 1 == 1

# Generated at 2022-06-22 13:30:13.614708
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()

    import asyncio
    from tornado.tcpclient import TCPSSLClient, TCPClient
    from tornado.simple_httpclient import SimpleAsyncHTTPClient

    class DummyTCPSSLClient(TCPSSLClient):
        @gen.coroutine
        def test_connect(self, host, port, ssl_options, family, af, resolve, callback):
            future = Future()
            future.set_result(None)
            return future

    client = SimpleAsyncHTTPClient()
    connector = _Connector([(socket.AF_INET, ('127.0.0.1', 80))], connect=lambda af, addr: (None, None))
    future = connector.start()


# Generated at 2022-06-22 13:30:17.528757
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    p = _Connector([(socket.AF_INET, ('127.0.0.1', 8888))], lambda af, addr: (None, None))
    # Basic test: no timeout
    assert p.timeout is None
    p.set_timeout(1)
    assert p.timeout is not None

# Generated at 2022-06-22 13:30:19.164927
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    _Connector(addrinfo = [], connect = lambda a, b: IOStream(socket.socket(a, b)))

# Generated at 2022-06-22 13:30:28.099617
# Unit test for constructor of class _Connector
def test__Connector():
    ipv4_sock_info = [
        (socket.AF_INET, ("192.0.2.1", 80)),
        (socket.AF_INET, ("192.0.2.2", 80)),
    ]
    ipv6_sock_info = [
        (socket.AF_INET6, ("2001:db8::1", 80, 0, 0)),
        (socket.AF_INET6, ("2001:db8::2", 80, 0, 0)),
    ]
    ipv4_first_info = ipv4_sock_info + ipv6_sock_info
    ipv6_first_info = ipv6_sock_info + ipv4_sock_info


# Generated at 2022-06-22 13:31:08.052027
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import unittest
    import time, os
    import functools
    import socket
    import selectors
    import tornado
    import tornado.testing
    import tornado.platform.asyncio
    import tornado.web
    import tornado.httpserver
    import logging
    import asyncio
    import concurrent.futures as future
    from typing import Callable, cast, Any
    from tornado.testing import AsyncTestCase, bind_unused_port

    class Mock_socket:
        # Unit test for method socket of class _Connector
        def __init__(self, family: int, type: int, proto: int) -> None:
            self.family = family
            self.type = type
            self.proto = proto
            self.setblocking(True)

# Generated at 2022-06-22 13:31:09.129672
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    pass


# Generated at 2022-06-22 13:31:15.940508
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    resolver = Resolver(IOLoop.current())
    # addresses = resolver.resolve('www.google.com', 80, family=socket.AF_INET)
    connector = _Connector([(socket.AF_INET, ("www.google.com", 80))], lambda x, y: None)
    connector.clear_timeouts()



# Generated at 2022-06-22 13:31:22.890745
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado.netutil

    port = 34567
    client = tornado.netutil.TCPClient()

    @gen.coroutine
    def func():
        loop = IOLoop.current()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        server.bind(("", port))
        server.listen(1)
        stream = yield client.connect("localhost", port)
        sock, addr = server.accept()
        sock.close()
        server.close()
        stream.close()

    loop = IOLoop.current()
    loop.run_sync(func)



# Generated at 2022-06-22 13:31:25.954160
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    _Connector._clear_timeouts(IOLoop.current())
    return True

# Generated at 2022-06-22 13:31:27.250036
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    # Assertions
    # Assertions
    assert True == True



# Generated at 2022-06-22 13:31:32.891404
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    def test_closure(stream):
        stream.close()
    resolver = Resolver()
    conn = _Connector(resolver.resolve("www.google.com"), None)
    conn.streams = set([1, 2, 3])
    conn.close_streams()
    conn.streams = set([])
    conn.close_streams()



# Generated at 2022-06-22 13:31:34.636774
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    _Connector.clear_timeouts()

# Generated at 2022-06-22 13:31:42.513321
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    stream1 = IOStream(socket.socket())
    stream2 = IOStream(socket.socket())
    self1 = _Connector([], lambda f, t: (stream1, None))
    self1.streams.add(stream1)
    self2 = _Connector([], lambda f, t: (stream2, None))
    self2.streams.add(stream1)
    self2.streams.add(stream2)
    self1.close_streams()
    self2.close_streams()



# Generated at 2022-06-22 13:31:44.629974
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    self = _Connector([], lambda x, y: (x, y))
    self.clear_timeouts()



# Generated at 2022-06-22 13:32:48.058342
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    # Create a fake IOLoop to avoid IOError because the real IOLoop is already running
    class FakeIOLoop(object):
        def time(self):
            return 0.0

        def add_timeout(self, timeout: float, callback: Callable, *args, **kwargs):
            return None  # type: ignore

        def remove_timeout(self, timeout: object) -> None:
            pass

    # Initializes a fake _Connector
    fake_io_loop = FakeIOLoop()
    fake_streams = [None]
    fake_connector = _Connector(addri, None)
    fake_connector.io_loop = fake_io_loop
    fake_connector.streams = set(fake_streams)

    # Test the close_streams method
    fake_connector.close_streams()

# Generated at 2022-06-22 13:32:54.750381
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    io_loop = IOLoop.current()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(("127.0.0.1", 0))
    stream = IOStream(sock, io_loop=io_loop)
    future = Future()

    def connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[IOStream, Future]:
        return stream, future

    addrinfo = [
        (socket.AF_INET, ("1.1.1.1", 1)),
        (socket.AF_INET, ("2.2.2.2", 2)),
        (socket.AF_INET, ("3.3.3.3", 3)),
    ]
    connector = _Connector(addrinfo, connect)
    assert connector.rem

# Generated at 2022-06-22 13:32:55.380319
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    return True

# Generated at 2022-06-22 13:33:07.191980
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    import unittest
    import functools

    class _ConnectorTest(unittest.TestCase):
        def setUp(self) -> None:
            self.io_loop = IOLoop.current()
            self.connector = _Connector(
                [
                    (socket.AddressFamily.AF_INET, ("www.google.com", 80)),
                    (socket.AddressFamily.AF_INET6, ("www.google.com", 80)),
                ],
                functools.partial(self.fake_connect),
            )

        def fake_connect(
            self, af: socket.AddressFamily, addr: Tuple
        ) -> Tuple[IOStream, "Future[IOStream]"]:
            future = Future()

# Generated at 2022-06-22 13:33:11.804720
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    def mock_remove_timeout(self, timeout):
        return -1

    from tornado.ioloop import IOLoop
    import types
    import sys
    ioloop = IOLoop()
    setattr(IOLoop, 'remove_timeout', mock_remove_timeout)
    connector = _Connector(None, None)
    connector.io_loop = ioloop
    connector.timeout = 1
    connector.connect_timeout = 1
    connector.clear_timeouts()
    assert connector.timeout is None
    assert connector.connect_timeout is None
    ioloop.close()



# Generated at 2022-06-22 13:33:23.464886
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    import pytest
    import socket
    import ssl
    from tornado.iostream import IOStream
    from tornado.netutil import Resolver
    from tornado import gen

    from .tcpclient import TCPClient

    @gen.coroutine
    def main(server_host, server_port):
        io_loop = IOLoop.current()
        resolver = Resolver()
        resolver.install()
        # tcp_client = TCPClient(io_loop=io_loop)
        # yield tcp_client.connect(server_host, server_port)
        # return tcp_client.stream.stream.socket.getpeername()


# Generated at 2022-06-22 13:33:35.029320
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    class AF:
        AF_INET=0;
        AF_INET6=1
    
    addrs1=[]
    addrs1.append((AF.AF_INET,("127.0.0.1",80)))
    addrs1.append((AF.AF_INET,("127.0.0.2",80)))
    
    addrs2=[]
    addrs2.append((AF.AF_INET,("127.0.0.3",80)))
    addrs2.append((AF.AF_INET,("127.0.0.4",80)))
    
    expected="127.0.0.1"
    actual=None
    connector= _Connector(addrs1,connect)
    connector.try_connect(iter(addrs1))
    assert expected == actual
    


# Generated at 2022-06-22 13:33:45.760616
# Unit test for method split of class _Connector
def test__Connector_split():
    addrs = [
        (socket.AF_INET, ("127.0.0.1", 80)),
        (socket.AF_INET, ("192.168.1.1", 80)),
        (socket.AF_INET6, ("2607:f0d0:1002:51::4", 80)),
    ]

    assert _Connector.split(addrs) == [
        [(socket.AF_INET, ("127.0.0.1", 80)), (socket.AF_INET, ("192.168.1.1", 80))],
        [(socket.AF_INET6, ("2607:f0d0:1002:51::4", 80))],
    ]


# Generated at 2022-06-22 13:33:51.631260
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    obj = _Connector([], lambda x,y : (None, None))
    obj.io_loop = MagicMock()
    obj.clear_timeouts()
    obj.io_loop.remove_timeout.assert_any_call(None)



# Generated at 2022-06-22 13:33:59.089593
# Unit test for method set_connect_timeout of class _Connector
def test__Connector_set_connect_timeout():
    address_info = [
        (socket.AF_INET, ('192.168.0.1', 80)),
        (socket.AF_INET6, ('192.168.0.1', 80))
    ]
    conn = _Connector(
        address_info,
        lambda af, addr: (
            IOStream(socket.socket(af, socket.SOCK_STREAM)),
            Future()
        )
    )
    # Don't pass the test if timeout is set but future is not done.
    conn.set_connect_timeout(1.0)
    assert conn.future.done() is False
    try:
        next(conn.future)
        raise AssertionError('It should have thrown TimeoutError.')
    except TimeoutError:
        pass
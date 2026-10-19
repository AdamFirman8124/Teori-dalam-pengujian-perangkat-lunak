

# Generated at 2022-06-22 13:27:51.315663
# Unit test for method start of class _Connector
def test__Connector_start():
    addrinfo = [(socket.AF_INET, ("1", "2")), (socket.AF_INET, ("3", "4"))]
    def connect(af, addr):
        fs = Future()
        fs.set_result(IOStream(socket.socket()))
        return fs, fs
    dc = _Connector(addrinfo, connect)
    dc.start()    

# Generated at 2022-06-22 13:28:03.731321
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    # testing
    # def set_timeout(self, timeout: float) -> None:
    #   self.timeout = self.io_loop.add_timeout(
    #     self.io_loop.time() + timeout, self.on_timeout)

    # mock up io_loop
    io_loop = _MockedIOLoopClass()

    # mock up on_timeout
    def on_timeout():
        return

    # mock up _Connector
    connector = _Connector([], lambda af, addr: (None, None))

    # setting
    connector.io_loop = io_loop
    connector.on_timeout = on_timeout
    timeout = 1

    # testing
    connector.set_timeout(timeout)

    assert connector.io_loop.add_timeout.called
    assert connector.io_loop.add_timeout.called_once

# Generated at 2022-06-22 13:28:15.640583
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    from . import io_loop
    from . import ioloop
    from typing import List
    from . import future
    from . import concurrent

    # TODO: we need a more general way to test for this condition
    if hasattr(socket, "AF_INET6"):
        conn = _Connector(
            [(socket.AF_INET6, ("::1", 80))],
            lambda af, addr: (IOStream(socket.socket(af, socket.SOCK_STREAM)), None),
        )
        future_result = conn.start()
        assert future_result is not None
        assert isinstance(future_result, future.Future) is True
        assert future_result.done() is False
        # future_result.add_done_callback(lambda f:io_loop.stop())
        # io_loop.start()

# Generated at 2022-06-22 13:28:28.235409
# Unit test for constructor of class _Connector
def test__Connector():
    # type: () -> None
    class FakeResolver(Resolver):
        def __init__(self):
            self.resolved_addrs = []  # type: List[Tuple[socket.AddressFamily, Tuple]]

        def resolve(self, host, port, family):
            return self.resolved_addrs

    addr_info = [(socket.AF_INET, ("0.0.0.0", 8080)), (socket.AF_INET, ("0.0.0.1", 8080))]
    resolver = FakeResolver()
    resolver.resolved_addrs = addr_info

# Generated at 2022-06-22 13:28:34.299414
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    resolver = Resolver()
    client = TCPClient(resolver)
    af = socket.AF_INET
    port = 13
    host = "time-c.nist.gov"
    ssl_options = None
    max_buffer_size = None
    source_ip = None
    source_port = None
    timeout = None
    stream = client.connect(af = af, port = port, host = host, ssl_options = ssl_options, max_buffer_size = max_buffer_size, source_ip = source_ip, source_port = source_port, timeout = timeout)
    print(stream.read())

# Generated at 2022-06-22 13:28:44.019503
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    # This test case checks if the exception is set or not
    expected = TimeoutError
    # We will try to create a connection by passing valid arguments.
    # If all is fine, the
    # exception will not be raised as the connection will be established.
    # But, if any of the parameters is invalid, the connect function will raise
    # exception and that is what we use to test if the exception is set.
    try:
        connector = _Connector(addrinfo = [], connect = _connect)
        connector.on_connect_timeout()
        result = connector.future.exception()
    except Exception as e:
        result = e
    assert(result == expected)



# Generated at 2022-06-22 13:28:52.956686
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    import time
    import tornado.gen
    from tornado.ioloop import TimeoutError
    from .tornado_unittest import TestCase
    from .tornado_testing import bind_unused_port, AsyncTestCase

    class TestConnector(AsyncTestCase):
        _Connector = None

        connector = _Connector(0, None)
        self.assertRaises(AssertionError, self.connector.set_timeout, -1)

        def test_timeout(self):
            sock, port = bind_unused_port()
            # We have to leave time for the SYN/ACK in addition to the SYN
            # to avoid false timeout failures.
            # On Windows, the select() call appears to return as soon
            # as the SYN is received, so we allow up to 0.1 seconds
            # for that.
            self

# Generated at 2022-06-22 13:28:55.672715
# Unit test for constructor of class _Connector
def test__Connector():
    connector = _Connector([(1, 2)], lambda a, b: (None, None))
    assert connector.io_loop is IOLoop.current()
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector.last_error is None
    assert connector.remaining == 1
    assert connector.primary_addrs == [(1, 2)]
    assert connector.secondary_addrs == []
    assert connector.streams == set()



# Generated at 2022-06-22 13:28:57.503916
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    o = _Connector([], None)
    o.clear_timeouts()
    pass



# Generated at 2022-06-22 13:29:01.249012
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    conn = _Connector(addrinfo=[[socket.AddressFamily.AF_INET], ["127.0.0.1"]],
                      connect=connect)



# Generated at 2022-06-22 13:29:29.026838
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    import tornado.iostream
    import tornado.netutil
    import tornado.ioloop
    import tornado.gen
    import socket
    import datetime
    import ssl
    import functools
    import asyncio
    from tornado.platform.asyncio import AsyncIOMainLoop
    from distutils.version import LooseVersion
    from tornado.test.util import unittest
    from tornado.test.util import skipOnTravis
    try:
        sslobj = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    except AttributeError:
        sslobj = ssl.SSLContext(ssl.PROTOCOL_SSLv2)
    from tornado import concurrent
    from tornado import gen
    from tornado import ioloop
    from tornado import netutil
    from tornado import simple_httpclient


# Generated at 2022-06-22 13:29:39.203153
# Unit test for constructor of class _Connector
def test__Connector():
    future = Future()
    connector = _Connector(
        [], lambda af, addr: (
            IOStream(None, None),
            future
        )
    )
    assert(connector.io_loop == IOLoop.current())
    assert(connector.connect == None)
    assert(isinstance(connector.future, Future))
    assert(connector.timeout == None)
    assert(connector.connect_timeout == None)
    assert(connector.last_error == None)
    assert(connector.remaining == 0)
    assert(connector.primary_addrs == [])
    assert(connector.secondary_addrs == [])
    assert(connector.streams == set())


# Generated at 2022-06-22 13:29:51.379423
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    from tornado.testing import gen_test

    from .unittest_mock import Mock

    class MockFuture(object):
        def __init__(self, fs):
            self.fs = fs

        def done(self):
            return False

        def set_exception(self, ex):
            self.fs.append((0, ex))

    class MockIOStream(object):
        def __init__(self, fs):
            self.fs = fs

        def close(self):
            self.fs.append((1, None))

    class MockIOLoop(object):
        def __init__(self):
            self.time_map = {}
            (H, M, S) = (3600, 60, 1)
            self.time_map[0] = 0

# Generated at 2022-06-22 13:29:57.199395
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    # Loop = IOLoop.instance()
    Addrinfo = [('AF_INET', ('8.8.8.8', 53)), ('AF_INET6', ('2001:4860:4860::8888', 53))]
    connector = _Connector(Addrinfo, tuple)
    # assert connector.clear_timeout() == None
    assert connector.timeout is None
    # assert connector.clear_timeouts() == None
    assert connector.connect_timeout is None



# Generated at 2022-06-22 13:30:09.313595
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    # When timeout is called, we should get a timeout exception
    def _test_timeout(connector):
        connector.on_timeout()
        assert connector.future.exception() is TimeoutError()

    # When timeout is called, but the future is already set, we should get no exception
    def _test_timeout_future(connector):
        connector.future.set_exception(
            Exception('hello'))
        connector.on_timeout()
        assert connector.future.exception() is not TimeoutError()

    # When on_timeout is called, but timeout is not set, we should get no exception
    def _test_on_timeout(connector):
        connector.timeout = None
        connector.on_timeout()
        assert connector.future.exception() is None

    # When on_timeout is called, but the future is already set

# Generated at 2022-06-22 13:30:13.454497
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    obj = _Connector([('af', 'addr')], 'connect')
    obj.io_loop = gen.sleep(0.1)
    obj.set_timeout(0.1)
    return obj.timeout is not None



# Generated at 2022-06-22 13:30:23.465129
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import logging
    import socket
    import asyncio
    from io import StringIO
    def test_resolver(_, hostname, port, family=socket.AF_UNSPEC, type=socket.SOCK_STREAM,
            proto=0, flags=0, callback=None):
        if hostname == 'example.com':
            callback([(socket.AF_INET, 1, 6, '', ('192.0.2.1', 80)),
                      (socket.AF_INET6, 2, 17, '', ('2001:db8::1', 80, 0, 0))])
        else:
            callback([])

    def test_connect(af, addr):
        future = Future()
        future.set_result(IOStream(socket.socket()))
        return future, future


# Generated at 2022-06-22 13:30:28.168190
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    address = ('localhost', 8000)
    connector = _Connector([(socket.AF_INET, address)], client_connect)
    connector.clear_timeouts()



# Generated at 2022-06-22 13:30:32.175284
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    connector = _Connector([(None, None)], None)
    connector.connect_timeout = 1
    connector.timeout = 2
    connector.clear_timeouts()
    assert connector.connect_timeout is None
    assert connector.timeout is None



# Generated at 2022-06-22 13:30:38.270681
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado.netutil import Resolver
    from tornado.iostream import IOStream
    from tornado.testing import AsyncTestCase, gen_test

    AsyncIOMainLoop().install()

    async def asyncio_dummy_resolve(
        host: str, port: int, af: socket.AddressFamily = socket.AF_UNSPEC
    ) -> List[Tuple[socket.AddressFamily, Tuple]]:
        return [(socket.AF_INET, ("127.0.0.1", 7777))]


# Generated at 2022-06-22 13:30:58.215510
# Unit test for method split of class _Connector
def test__Connector_split():
    test_addrinfo = [(socket.AF_INET, ('127.0.0.1', 8080))]
    primary, secondary = _Connector.split(test_addrinfo)
    assert primary == [(socket.AF_INET, ('127.0.0.1', 8080))]
    assert secondary == []


# Generated at 2022-06-22 13:31:01.198705
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    """Unit test for method clear_timeouts of class _Connector"""
    obj = _Connector([0, 1], 0)
    obj.clear_timeouts()
    obj.clear_timeouts()
    assert obj.timeout == None
    assert obj.connect_timeout == None


# Generated at 2022-06-22 13:31:10.674494
# Unit test for method split of class _Connector
def test__Connector_split():
    addrinfo1 = [(1, 1), (2, 2), (3, 3), (4, 4)]
    addrinfo2 = [(5, 5), (6, 6), (7, 7), (8, 8)]
    res = _Connector.split(addrinfo1)
    assert res[0] == [(1, 1)]
    assert res[1] == [(2, 2), (3, 3), (4, 4)]
    res = _Connector.split(addrinfo2)
    assert res[0] == [(5, 5), (6, 6), (7, 7), (8, 8)]
    assert res[1] == []



# Generated at 2022-06-22 13:31:15.816964
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.tcpserver import TCPServer

    class EncryptionTestServer(TCPServer):
        def __init__(self, io_loop=None, ssl_options=None):
            super().__init__(io_loop=io_loop)
            self.ssl_options = ssl_options

        def handle_stream(self, stream, address):
            EncryptionTestConnection(stream, self.ssl_options)

    class EncryptionTestConnection(IOStream):
        def __init__(self, stream, ssl_options=None):
            super().__init__(stream, ssl_options=ssl_options)
            self.close_called = False
            self.shutdown_called = False
            self.closed = False
            stream.set_close_callback

# Generated at 2022-06-22 13:31:20.016391
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    stream = IOStream(socket.socket())
    future = stream.connect(("www.google.com", 80))
    def on_future(f):
        assert f.exception() is not None
        print("done")
        IOLoop.current().stop()
    future.add_done_callback(on_future)
    IOLoop.current().start()


# Generated at 2022-06-22 13:31:32.415816
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    def _test():
        # setup
        future_result = IOStream(socket.socket())
        future = Future()
        valid_addrs = iter([(socket.AddressFamily.AF_INET, ("1.1.1.1", 8888))])
        af = socket.AddressFamily.AF_INET
        addr = ("1.1.1.1", 8888)
        future.set_result(future_result)
        # test
        connector = _Connector(
            addrinfo=[(socket.AddressFamily.AF_INET, ("1.1.1.1", 8888))],
            connect=lambda af, addr: (None, None),
        )
        connector.on_connect_done(
            addrs=valid_addrs, af=af, addr=addr, future=future
        )
        assert connector.rem

# Generated at 2022-06-22 13:31:44.984554
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import pytest
    from . import TCPClient
    from . import _Connector
    from . import _Connector
    from functools import partial
    from tornado.iostream import IOStream
    from tornado.concurrent import Future
    from typing import Any, Union, Dict, Tuple, List, Callable, Iterator, Optional, Set
    from tornado.testing import AsyncTestCase, gen_test

    class Test_Connector(AsyncTestCase):
        @gen_test
        async def test_try_connect(self) -> None:
            client = TCPClient()
            addrinfo = [(socket.AF_INET, ('127.0.0.1', 8080)),
                        (socket.AF_INET, ('127.0.0.1', 8081))]
            """Unit test for method try_connect of class _Connector."""
           

# Generated at 2022-06-22 13:31:49.226315
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    class FakeIOLoop(object):
        def add_timeout(self, t, c):
            pass

        def remove_timeout(self, t):
            pass

        def time(self):
            pass

    class FakeStream(object):
        def close(self):
            pass

    def fake_connect(af, addr):
        return FakeStream(), Future()

    a = _Connector([(socket.AF_INET, ("1", 1))], fake_connect)
    a.io_loop = FakeIOLoop()
    a.timeout = object()
    a.clear_timeout()
    a.connect_timeout = object()
    a.clear_timeouts()


# Generated at 2022-06-22 13:31:54.562950
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    from tornado.testing import *

    client = TCPClient()
    # ipv4
    stream = gen.coroutine(client.connect)("localhost", 80)
    # ipv6
    stream = gen.coroutine(client.connect)("::1", 80)
    # no ssl
    stream = gen.coroutine(client.connect)("localhost", 80, ssl_options=None)
    # ssl
    stream = gen.coroutine(client.connect)("localhost", 443, ssl_options=dict())
    # max buffer size
    stream = gen.coroutine(client.connect)("localhost", 80, max_buffer_size=10000)
    # source ip
    stream = gen.coroutine(client.connect)("localhost", 80, source_ip="127.0.0.1")
    # source port
    stream

# Generated at 2022-06-22 13:31:58.748214
# Unit test for method start of class _Connector
def test__Connector_start():

    resolver = Resolver()
    stream = IOStream(socket.socket(), io_loop=IOLoop.current())
    future = Future()
    connector = _Connector([(socket.AF_INET, ("127.0.0.1", 12345))], lambda x, y: (stream, future))

    future.set_result(stream)
    connector.start()
    future.set_exception(Exception())
    connector.start()


# Generated at 2022-06-22 13:32:34.164298
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    resolver = Resolver()
    tcp_client = TCPClient(resolver)
    stream = tcp_client._create_stream(1024, socket.AF_INET, ("127.0.0.1", 8080))
    assert stream[0].socket.family == socket.AF_INET and stream[0].socket.connect_ex(("127.0.0.1", 8080)) == 0

# Generated at 2022-06-22 13:32:43.964126
# Unit test for method start of class _Connector
def test__Connector_start():
    # test case 1:
    # if self.timeout is not None:
    #     # If the first attempt failed, don't wait for the
    #     # timeout to try an address from the secondary queue.
    #     self.io_loop.remove_timeout(self.timeout)
    #     self.on_timeout()
    pass

    # test case 2:
    # self.clear_timeout()
    pass

    # test case 3:
    # if not self.future.done():
    #     self.try_connect(iter(self.secondary_addrs))
    pass

    # test case 4:
    # self.io_loop.remove_timeout(self.timeout)
    # self.on_timeout()
    pass


# Generated at 2022-06-22 13:32:52.096580
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import unittest
    import inspect
    import sys
    import io
    import types

    class MockSocket:
        def __init__(self, family : int, type : int, proto : int) -> None:
            self.family = family
            self.type = type
            self.proto = proto

        def connect(self, addr : Tuple[str, int]) -> None:
            self.addr = addr
            return None

    class MockIOStream(io.IOBase):
        def __init__(self, sock : MockSocket) -> None:
            self._sock = sock

        @property
        def socket(self) -> MockSocket:
            return self._sock

        def close(self) -> None:
            pass

    class MockFuture:
        def __init__(self) -> None:
            self.done_

# Generated at 2022-06-22 13:33:03.347901
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import logging
    import sys

    # Setting up logger
    logger = logging.getLogger()
    logger.disabled = True
    del logger.handlers[:]
    logger.setLevel(logging.CRITICAL)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False

    # Setting up logger
    logger1 = logging.getLogger('tornado.application')
    logger1.disabled = True
    del logger1.handlers[:]
    logger1.setLevel(logging.CRITICAL)

# Generated at 2022-06-22 13:33:10.908905
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    addrinfo = [
        ("af_a", ("host_a", 80)),
        ("af_b", ("host_b", 80)),
        ("af_a", ("host_a2", 80)),
    ]

    def test_connect(af: socket.AddressFamily, addr: Any) -> Tuple[IOStream, "Future[IOStream]"]:
        io_stream = IOStream(socket.socket())
        future = Future()
        future.set_result(io_stream)
        return io_stream, future

    def test_timeout():
        print("test time out")

    def test_connect_timeout():
        print("test conncet time out")

    connector = _Connector(addrinfo, test_connect)
    connector.start()
    connector.timeout = test_timeout
    connector.connect_timeout = test_connect_timeout

# Generated at 2022-06-22 13:33:23.214457
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    import random

    c = _Connector.__new__(_Connector)
    c.io_loop = IOLoop.current()
    c.connect = lambda x: (None, Future())

    def test_case(result, expect_set_result, expect_close_streams):
        # type: (bool, bool, bool) -> None
        f2 = Future()
        f2.set_result(result)
        c.future = Future()
        c.remaining = 3
        c.last_error = None
        c.streams = set()
        c.set_timeout = lambda x: None
        c.clear_timeout = lambda: None
        c.close_streams = lambda: c.streams.add(42)

# Generated at 2022-06-22 13:33:28.733195
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    # TODO: This requires a backport of https://github.com/tornadoweb/tornado/pull/2180
    # assert False, "TODO: This requires a backport of https://github.com/tornadoweb/tornado/pull/2180"
    pass



# Generated at 2022-06-22 13:33:33.611228
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    class IOStreamMock(object):
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    s = IOStreamMock()

    c = _Connector([(1, 1)], None)
    c.streams.add(s)

    c.close_streams()
    assert s.closed



# Generated at 2022-06-22 13:33:45.419236
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    @gen.coroutine
    def test_case():
        definitions = {
            "stream0": IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM)),
            "stream1": IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM)),
        }
        stream0 = definitions["stream0"]
        stream1 = definitions["stream1"]
        connector = _Connector(
            [(1, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))],
            lambda _a, _b: (stream0, stream1),
        )
        assert(stream0.closed and stream1.closed)
        yield test_coroutine(
            connector.start()
        )
        assert(not stream0.closed and not stream1.closed)
       

# Generated at 2022-06-22 13:33:47.039122
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    obj = _Connector(None, None)
    obj.clear_timeouts()


# Generated at 2022-06-22 13:34:58.572389
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    import unittest
    from tornado import test
    from tornado.test import async_test
    from tornado.test import gen_test
    from tornado.test import io_loop_with_timeout
    from tornado.util import PY3
    from tornado.httpclient import AsyncHTTPClient

    # NOTE: These may fail if run against a real server. The requests
    # made are the same regardless of HTTP or HTTPS, so only one test is
    # needed.
    @test.skipIf(PY3, "not well-tested on Python 3")
    class _ConnectorTest(unittest.TestCase):
        def setUp(self):
            self.setUpClass()

        def tearDown(self):
            self.tearDownClass()


# Generated at 2022-06-22 13:35:10.063303
# Unit test for method start of class _Connector
def test__Connector_start():
    from tornado.testing import gen_test

    # Unit test for method start of class _Connector
    # This tests the timeouts for the _Connector not for the Connection class below
    # We test the timeouts by passing an empty generator to try_connect
    # This means that the address families are exhausted, so we can test the timeouts

    # A dummy method to pass to try_connect
    def dummy_connect(af, addr):
        return IOStream(socket.socket(af, socket.SOCK_STREAM))

    # Set the timeouts to a small value
    timeout = 0.3
    connect_timeout = 0.2

    # Create a Connector and start
    conn = _Connector([(socket.AF_INET, (1, 2, 3, 4))], dummy_connect)

# Generated at 2022-06-22 13:35:20.748840
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    future = Future()
    global flag
    flag = False
    global flag2
    flag2 = False
    print("initiated")
    def on_timeout():
        flag = True
    def on_connect_timeout():
        flag2 = True
    io_loop = IOLoop.current()
    io_loop.add_timeout(io_loop.time()+5, on_timeout)
    io_loop.add_timeout(io_loop.time()+10, on_connect_timeout)
    io_loop.clear_timeouts(io_loop.time())

    def handle_timeout():
        assert flag == False
        assert flag2 == False
        future.set_result(True)

    io_loop.add_timeout(
        io_loop.time()+20, handle_timeout)
    future.result()


# Generated at 2022-06-22 13:35:23.008896
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    io_loop = IOLoop.current()
    io_loop.add_callback(io_loop.stop)
    io_loop.start()


# Generated at 2022-06-22 13:35:29.386353
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    """
    Unit test for method set_timeout of class _Connector
    """
    timeout = 10
    io_loop = IOLoop.current()
    c = _Connector(
        [],
        functools.partial(connect),
    )
    c.start(timeout)
    c.set_timeout(timeout)
    assert c.timeout == io_loop.add_timeout(
        io_loop.time() + 10, c.on_timeout
    )


# Generated at 2022-06-22 13:35:39.495039
# Unit test for method split of class _Connector
def test__Connector_split():
    a_list = []
    a_list.append((socket.AF_INET, ('127.0.0.1', 8080)))
    a_list.append((socket.AF_INET, ('127.0.0.1', 8081)))
    a_list.append((socket.AF_INET6, ('::1', 8080)))
    a_list.append((socket.AF_INET6, ('::1', 8081)))
    a_list.append((socket.AF_INET6, ('::1', 8082)))
    splitted_a_list = _Connector.split(a_list)
    assert len(splitted_a_list) == 2
    assert len(splitted_a_list[0]) == 2
    assert len(splitted_a_list[1]) == 4
    assert splitted_

# Generated at 2022-06-22 13:35:49.853238
# Unit test for constructor of class _Connector
def test__Connector():
    import pytest
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()

    addrinfo = [(1, ("2", 3)), (4, ("5", 6))]
    future = Future()

    def connect(af, addr):
        return (IOStream(socket.socket(af, socket.SOCK_STREAM)), future)

    connector = _Connector(addrinfo, connect)
    assert (connector.io_loop is IOLoop.current())
    assert (connector.connect == connect)
    assert (isinstance(connector.future, Future))
    assert (connector.timeout is None)
    assert (connector.connect_timeout is None)
    assert (connector.last_error is None)
    assert (connector.remaining == 2)

# Generated at 2022-06-22 13:35:54.268923
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import unittest
    import tornado.testing

    class Test_test__Connector_try_connect(unittest.TestCase):
        def test_test__Connector_try_connect(self):
            self.fail("Not implemented")

    tornado.testing.main()

# Generated at 2022-06-22 13:35:56.138167
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    hostname="localhost"
    port=80
    ip="::"
    try:
        a=TCPClient()
        b=a.connect(hostname,port,ip)
        assert(not b is None)
    except Exception as err:
        assert(err is None)


# Generated at 2022-06-22 13:35:57.368146
# Unit test for method start of class _Connector
def test__Connector_start():
    pass


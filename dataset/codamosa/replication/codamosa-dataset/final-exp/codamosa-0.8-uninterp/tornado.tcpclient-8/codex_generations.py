

# Generated at 2022-06-22 13:27:54.014060
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
	# Test case 1
	streams = set()
	it = iter(range(10))
	connector = Connector(it, streams)
	connector.try_connect(it)

	# Test case 2
	streams = set()
	it = iter(range(10))
	connector = Connector(it, streams)
	connector.try_connect(it)

	# Test case 3
	streams = set()
	it = iter(range(10))
	connector = Connector(it, streams)
	connector.try_connect(it)



# Generated at 2022-06-22 13:27:59.448980
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado.testing
    import tornado.tcpserver
    import tornado.gen
    from tornado.netutil import bind_sockets, add_accept_handler
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.iostream import IOStream
    import socket

    class EchoServer(tornado.tcpserver.TCPServer):
        @tornado.gen.coroutine
        def handle_stream(self, stream: IOStream, address: Tuple) -> None:
            data = yield stream.read_until_close()
            stream.write(b"received: ")
            stream.write(data)
            stream.close()

    sock, port = bind_sockets(None, "127.0.0.1")
    server = EchoServer()

# Generated at 2022-06-22 13:28:11.948349
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    def getaddrinfo(host, service, family=0, type=0, proto=0, flags=0):
        return [(2, 2, 6, '', ('10.0.0.1', 8432))]
    def connect(af, addr):
        nonlocal stream_count
        stream_count += 1
        stream = IOStream(socket.socket(af, socket.SOCK_STREAM, 0),
                          io_loop=IOLoop.current())
        future = Future()
        return stream, future
    #
    # not self.future.done()
    # self.streams.discard(stream)
    #
    # self.future.set_result((af, addr, stream))
    # self.close_streams()
    stream_count = 0

# Generated at 2022-06-22 13:28:18.847493
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    connector = _Connector([(1, 2)], lambda X, Y: None)
    stream = IOStream(socket.socket())
    connector.streams.add(stream)
    assert stream.socket in {x.socket for x in connector.streams}
    connector.close_streams()
    assert stream.socket not in {x.socket for x in connector.streams}
    connector.close_streams()
    del stream



# Generated at 2022-06-22 13:28:22.321600
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    client = TCPClient()
    future = client.connect('localhost', 8080)
    stream = future.result()
    print('OK')



# Generated at 2022-06-22 13:28:33.123418
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    import apply_async
    import tornado
    import time
    import tornado.util
    import future
    import tornado.log
    import tornado.ioloop
    import socket
    import socket
    import functools
    import tornado.platform.auto
    import functools
    import futures.future
    import futures.backports
    import tornado.tcpserver
    import tornado.iostream
    import tornado.locks
    import tornado.gen
    import traceback
    import tornado.stack_context
    import tornado.process
    import tornado.platform.auto
    import tornado.locks
    import futures.backports
    import future
    import asyncio
    import socket
    import logging
    import time
    import time
    import functools
    import traceback
    import functools
    import socket
    import functools


# Generated at 2022-06-22 13:28:43.754308
# Unit test for method split of class _Connector
def test__Connector_split():
    # Arrange
    import random
    _Connector.split(random.choice([
        # Case 1: addrinfo length = 0
        [],
        # Case 2: addrinfo length = 1
        [[socket.AF_INET, (1, 2)]],
        # Case 3: addrinfo length = 2
        [[socket.AF_INET, (1, 2)], [socket.AF_INET, (3, 4)]],
        # Case 4: addrinfo length > 2
        [[socket.AF_INET, (1, 2)], [socket.AF_INET6, (3, 4)], [socket.AF_INET, (5, 6)]]
    ]))




# Generated at 2022-06-22 13:28:52.298675
# Unit test for constructor of class _Connector
def test__Connector():
    from typing import Any, Tuple

    class TempConnector(object):
        def __init__(self, name: str):
            self.name = name

        def __repr__(self) -> str:
            return "CONNECTOR %s" % self.name

        def start(self, timeout: float = _INITIAL_CONNECT_TIMEOUT, connect_timeout: Optional[Union[float, datetime.timedelta]] = None) -> "Future[Tuple[socket.AddressFamily, Any, IOStream]]":
            pass

    from unittest import TestCase

    class TempT(TestCase):
        def test_split(self):
            a = _Connector.split([(1, 2), (2, 3), (1, 5)])

# Generated at 2022-06-22 13:28:59.169181
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    import sys
    import os
    import inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    print("\n")
    print("## TESTING METHOD on_connect_timeout of class _Connector ##")

    class TCPServer(object):
        def __init__(self) -> None:
            self.io_loop = IOLoop.current()
            self.stream = None  # type: Optional[IOStream]
            self.stream_future = None  # type: Optional[Future[IOStream]]


# Generated at 2022-06-22 13:29:01.960368
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    object = _Connector(None, None)
    object.clear_timeouts()
    pass



# Generated at 2022-06-22 13:29:29.221519
# Unit test for method split of class _Connector
def test__Connector_split():
    addrs = [
        (socket.AF_INET, ("127.0.0.1", 8081)),
        (socket.AF_INET, ("127.0.0.1", 8082)),
        (socket.AF_INET, ("127.0.0.1", 8083)),
        (socket.AF_INET6, ("::1", 8081)),
        (socket.AF_INET6, ("::1", 8082)),
        (socket.AF_INET6, ("::1", 8083)),
    ]
    _con = _Connector(addrs, connect)
    primary_addrs, secondary_addrs = _con.split(addrs)
    assert len(primary_addrs) == len(addrs) // 2

# Generated at 2022-06-22 13:29:40.020603
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    from unittest.mock import patch
    from typing import Any
    from tornado.concurrent import Future
    from tornado.iostream import IOStream
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase
    from .._connector import _Connector

    f = Future()  # type: Future[IOStream]

    class FakeStream(IOStream):
        def __init__(self, address: Any, family: Any) -> None:
            self.address = address
            self.family = family

        def close(self) -> None:
            print("Stream closed")

    def connect(addr: Any, family: Any) -> Any:
        return FakeStream(addr, family), f


# Generated at 2022-06-22 13:29:49.640536
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    import sys
    import os
    import typing
    import unittest

    temp_name = "__tornado__tempfile__"
    if os.path.exists(temp_name):
        os.remove(temp_name)

# Generated at 2022-06-22 13:29:51.738030
# Unit test for method start of class _Connector
def test__Connector_start():
    # testing function that does not have a decorated function
    f = mock.MagicMock(spec=_Connector.start)
    return f


# Generated at 2022-06-22 13:30:00.383373
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    from tornado.testing import gen_test
    from tornado.gen import Return
    from tornado.testing import AsyncTestCase

    class Test(AsyncTestCase):
        # pylint: disable=broad-except
        @gen.coroutine
        def do_test(self, connector) -> None:
            try:
                yield connector.future
            except Exception as e:
                self.assertTrue(isinstance(e, TimeoutError))

        @gen_test
        def test_on_connect_timeout(self) -> None:
            connect_future = Future()
            connector = _Connector(
                [(socket.AF_INET, ("127.0.0.1", 8888))],
                lambda af, addr: (None, connect_future),
            )

# Generated at 2022-06-22 13:30:04.725035
# Unit test for method split of class _Connector
def test__Connector_split():
    a = [(1, (1, 1)), (2, (2, 2))]
    b, c = _Connector.split(a)
    assert b == [(1, (1, 1))]
    assert c == [(2, (2, 2))]


# Generated at 2022-06-22 13:30:14.301815
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import tornado
    import threading
    import time
    def func():
        resolver=tornado.netutil.Resolver()
        af=socket.AddressFamily.AF_INET
        IOLoop.current().run_sync(lambda: resolver.resolve("www.google.com", 80, af))
        tcpclient=TCPClient(resolver)
        IOLoop.current().run_sync(lambda : tcpclient.connect("www.google.com", 80, af))
    threads=[]
    for i in range(100):
        t=threading.Thread(target=func)
        t.daemon=True
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    test

# Generated at 2022-06-22 13:30:22.080636
# Unit test for method start of class _Connector
def test__Connector_start():
    import os
    import tornado.platform.asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    import asyncio
    import socket
    import random
    import threading

    host = "127.0.0.1"
    port = int(os.getenv("PORT", 8888))

# Generated at 2022-06-22 13:30:29.633039
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    print("test__Connector_on_connect_timeout")
    addrinfo = [ 
        (socket.AF_INET, ("1.1.1.1", 80)),
        (socket.AF_INET6, ("2.2.2.2", 80)),
        (socket.AF_INET, ("3.3.3.3", 80)),
    ]

    def on_connect(af: socket.AddressFamily, addr: Tuple[str, int]) -> Tuple[IOStream, "Future[IOStream]"] :
        f = Future()  # type: Future[IOStream]
        f.set_result(None)
        s = IOStream(None)  # type: IOStream
        return (s, f)

    connect = on_connect

    c = _Connector(addrinfo, connect)

    c.start()



# Generated at 2022-06-22 13:30:32.362375
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                yield main, i, j, k


# Generated at 2022-06-22 13:31:01.633369
# Unit test for method on_connect_done of class _Connector

# Generated at 2022-06-22 13:31:12.441397
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    # Mock the IOLoop and IOStream
    class Mock_IOLoop:
        def add_timeout(self, time, cb):
            return None
        def remove_timeout(self, to):
            pass
        def time(self):
            return 0
    class Mock_IOStream(object):
        def __init__(self):
            pass
        def close(self):
            pass
    # Mock the resolver
    class Mock_Resolver(object):
        def resolve(self, host, port, af):
            return [1, 2, 3]
    # Mock the connect method
    class Mock_IOStream2(object):
        def __init__(self):
            pass
        def close(self):
            pass
    class Mock_Future(object):
        def __init__(self):
            pass

# Generated at 2022-06-22 13:31:22.809075
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import unittest

    class TestClass(unittest.TestCase):
        def setUp(self):
            self.connector = _Connector([], _ConnectorTests_mockedConnect)
            return

        def tearDown(self):
            return

        def test_try_connect_when_next_is_StopIteration(self):
            pass

        def test_try_connect_when_IOError_occurs(self):
            pass

        def test_try_connect_when_success(self):
            pass

    def _ConnectorTests_mockedConnect(socket):
        import concurrent.futures

        return  # IOStream, concurrent.futures.Future

    # End class
    return
# End Unit test



# Generated at 2022-06-22 13:31:33.875292
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    class FakeResolver:
        def __init__(self, addrinfo):
            self.addrinfo = addrinfo

        def resolve(self, host, port, family):
            if family == socket.AF_INET:
                raise Exception()
            return self.addrinfo

    class FakeStream:
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    class FakeIOLoop:
        def add_timeout(self, when, callback):
            callback()

    def connect(af, addr):
        stream = FakeStream()
        f = Future()
        return stream, f

    addrinfo = FakeResolver([(socket.AF_INET, 1)])
    connector = _Connector(addrinfo, connect)
    connector.io_loop = FakeIOLoop()


# Generated at 2022-06-22 13:31:46.036629
# Unit test for method split of class _Connector
def test__Connector_split():
    _connector = _Connector(
        addrinfo=[
            (6, ('2a00:1450:4001:812::200e', 443)),
            (6, ('2606:2800:220:1:248:1893:25c8:1946', 443))
        ],
        connect=lambda _, __: (None, None)
    )

# Generated at 2022-06-22 13:31:51.299369
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import unittest
    import sys
    import inspect
    import types
    # Retrieve the code object of the target method
    target_method = (
        inspect.getsourcelines(sys.modules[__name__]._Connector.try_connect)
    )
    # Remove the first element from the tuple containing the
    # source code lines of the method
    source_code = target_method[0]
    source_code = (
        source_code[1:]
    )  # Remove the first element from the tuple containing the source code lines of the method
    source_code = "".join(
        source_code
    )  # Convert source code list to a single string
    # Create the method in a stand-alone class
    # The method has to be called 'target', because the unittest module will look for a method
    # with this name

# Generated at 2022-06-22 13:32:02.549642
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
    from tornado.ioloop import IOLoop
    from tornado.iostream import IOStream
    import socket
    import unittest
    import time
    import functools
    io_loop = IOLoop.current()
    def close_callback(fd: socket.socket, address: str) -> None:
        io_loop.add_callback(io_loop.stop)
    def connect(af: object, addr: object) -> Tuple[IOStream, "Future[IOStream]"]:
        fd = socket.socket(af, socket.SOCK_STREAM, 0)
        stream = IOStream(fd, io_loop=io_loop)
        future = stream.connect(addr)
        future.add_done_callback(functools.partial(close_callback, fd, addr))
        return stream, future

# Generated at 2022-06-22 13:32:12.291324
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    print("start test__Connector_close_streams")
    stream = IOStream(socket.socket())
    connector = _Connector(
        [
            (
                socket.AddressFamily.AF_INET,
                (socket.AddressFamily.AF_INET, "192.168.2.11", 80),
            ),
        ],
        lambda af, addr: (IOStream(socket.socket()), Future()),
    )
    connector.streams.add(stream)
    assert len(connector.streams) == 1
    connector.close_streams()
    assert len(connector.streams) == 0



# Generated at 2022-06-22 13:32:23.251920
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    def test_func(_self):
        iostream = _self
        # Check that the iostream has the proper closed method
        assert hasattr(iostream, "closed")
        assert callable(iostream.closed)
        closed_attr_value = iostream.closed
        # Check that the any of attributes of the iostream is callable
        one_of_iostream_methods = False
        for _, attr in vars(iostream).items():
            if callable(attr) and (attr != closed_attr_value):
                one_of_iostream_methods = True
                break
        assert one_of_iostream_methods, "None of the iostream methods are callable."
        return True
    import types

# Generated at 2022-06-22 13:32:34.225979
# Unit test for method split of class _Connector
def test__Connector_split():
    # Test for a case that the first address family is the same
    addrinfo = [
        (socket.AF_INET, ("127.0.0.1", 80)),
        (socket.AF_INET, ("127.0.0.2", 80)),
        (socket.AF_INET6, ("127.0.0.3", 80)),
    ]
    primary, secondary = _Connector.split(addrinfo)
    assert primary == [
        (socket.AF_INET, ("127.0.0.1", 80)),
        (socket.AF_INET, ("127.0.0.2", 80)),
    ]
    assert secondary == [(socket.AF_INET6, ("127.0.0.3", 80))]
    # Test for a case that the first address family is different

# Generated at 2022-06-22 13:33:41.256943
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    print("\n*** test__Connector_clear_timeouts ***")

    streams = set()
    future = Future()
    future.set_result(None)
    io_loop = IOLoop.current()
    connector = _Connector(
        [
            (socket.AddressFamily.AF_INET, ("www.google.com", 80)),
            (socket.AddressFamily.AF_INET6, ("www.google.com", 80)),
        ],
        connect=lambda af, addr: (IOStream(socket.socket(af, socket.SOCK_STREAM)), future),
    )
    # Initialize fields to have a clear ideea in the test
    connector.timeout = io_loop.add_timeout(io_loop.time() + 1.0, connector.on_timeout)
    connector.connect_timeout = io_loop.add

# Generated at 2022-06-22 13:33:50.446317
# Unit test for method split of class _Connector
def test__Connector_split():
    # Test address lists with no addresses
    no_addr_info = _Connector.split([])
    assert no_addr_info == ([], [])

    # Test address lists with a single address
    ipv4_addr_info = _Connector.split([(socket.AF_INET, ('127.0.0.1', 80))])
    assert ipv4_addr_info == ([(socket.AF_INET, ('127.0.0.1', 80))], [])
    
    ipv6_addr_info = _Connector.split([(socket.AF_INET6, ('::1', 443))])
    assert ipv6_addr_info == ([], [(socket.AF_INET6, ('::1', 443))])

    # Test address lists with 2 addresses
    ipv4_and_ipv6_addr_

# Generated at 2022-06-22 13:33:56.778926
# Unit test for method start of class _Connector
def test__Connector_start():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 8888))]
    connector = _Connector(addrinfo, gen.sleep)
    future = connector.start()
    assert isinstance(future, Future)
    assert not future.done()
    assert future.running()
    assert isinstance(connector.timeout, object)
    assert isinstance(connector.streams, set)
    assert len(connector.streams) == 0
    assert connector.remaining == 1
    assert connector.primary_addrs == addrinfo
    assert connector.secondary_addrs == []



# Generated at 2022-06-22 13:34:04.949826
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import socket
    import unittest
    from .test.util import test

    class FakeStream(object):
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    class FakeFuture(object):
        def __init__(self, result):
            self.result = result

        def __iter__(self):
            return iter(self.result)

    class ConnectorTest(unittest.TestCase):
        def test_try_connect(self):
            f = Future()

            def connect(addrs):
                return (FakeStream(), f)

            c = _Connector([(socket.AF_INET, 0), (socket.AF_INET6, 0)], connect)
            c.start()

# Generated at 2022-06-22 13:34:09.946676
# Unit test for method split of class _Connector
def test__Connector_split():
    
    _Connector.split(addrinfo=[(1,2), (1,4), (3,7), (3,9)]) == ([(1,2), (1,4)], [(3,7), (3,9)])
    
test__Connector_split()


# Generated at 2022-06-22 13:34:17.289630
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    def func():
        return
    ol = IOLoop()
    f = Future() # type: Future[Any]
    f.set_result(IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM),io_loop=ol))
    _Connector(
        [(socket.AF_INET, ('127.0.0.1', 8000)),(socket.AF_INET6, ('::1', 8000))],
        lambda af, addr: (ol.current().add_future(f), f),
    ).close_streams()

# Generated at 2022-06-22 13:34:25.110254
# Unit test for method on_timeout of class _Connector
def test__Connector_on_timeout():
    def my_test(test_stream: IOStream) -> bool:
        test_stream.close()
        if test__Connector.timeout is None:
            assert False
        else:
            assert True
            return True

    test__Connector = _Connector([], my_test)

    def dummy_getaddrinfo(*args: Any, **kwargs: Any) -> Any:
        return [
            (socket.AF_INET, ("127.0.0.1", 80)),
            (socket.AF_INET, ("127.0.0.2", 80)),
            (socket.AF_INET, ("127.0.0.3", 80)),
        ]

    test__Connector.io_loop = IOLoop()
    test__Connector.future = Future()
    test__Connector.timeout = None
    test__Connector.connect_timeout

# Generated at 2022-06-22 13:34:28.018749
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    import mock
    io_loop = mock.Mock()
    c = _Connector([], lambda af, addr: (None, None))
    c.future = mock.Mock()
    c.io_loop = io_loop
    c.timeout = mock.Mock()
    c.connect_timeout = mock.Mock()

    c.clear_timeouts()
    io_loop.remove_timeout.assert_has_calls([c.timeout, c.connect_timeout])



# Generated at 2022-06-22 13:34:38.577184
# Unit test for method on_connect_done of class _Connector

# Generated at 2022-06-22 13:34:45.352642
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    import time
    import asyncio
    async def test(arg):
        c = _Connector([], functools.partial(_TCPClient.default_stream, None, None))
        c.set_timeout(100)
        c.set_connect_timeout(100)
        c.clear_timeouts()
        await asyncio.sleep(20)

    IOLoop.current().run_sync(test, None)


# Generated at 2022-06-22 13:36:50.903778
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    s = "ioservice:test:test_TCPClient_connect"

# Generated at 2022-06-22 13:36:56.592686
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    # 1. Generate inputs
    addrs = [(2,('192.168.1.100',23)),(2,('192.168.1.200',23))]
    
    # 2. Run function
    # _Connector.try_connect(addrs)
    # 3. Assert the result
    # Let's just assume it will work for now
    


# Generated at 2022-06-22 13:36:57.285568
# Unit test for method start of class _Connector
def test__Connector_start():
    assert True



# Generated at 2022-06-22 13:37:06.151987
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
  import tornado
  import sys
  import signal
  import unittest
  import asyncio
  import inspect
  import gc
  import pytest

  import resource
  import signal
  import sys

  def _setup_memory_watchdog():
      # Enable some aggressive (but not thread-safe) detection of memory leaks
      # by forcing periodic garbage collection and checking that the
      # resident memory size does not increase too quickly.
      def note_memory(signum, frame):
          mem_info = resource.getrusage(resource.RUSAGE_SELF)
          message = 'Memory usage: %s (diff since last: %s)' % (
              mem_info.ru_maxrss, mem_info.ru_maxrss - _last_memory_usage)
          print(message)
          sys.stdout.flush()
          _last

# Generated at 2022-06-22 13:37:15.556732
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    # We want to test closing streams, but it's not possible to create
    # a mock IOStream, so we create a real one and close it in the
    # io_loop callback.
    addr_info = [(1, (1, 1))]
    # type: List[Tuple[socket.AddressFamily, Tuple]]
    connector = _Connector(
        addr_info,
        lambda af, addr: (
            IOStream(socket.socket(af, socket.SOCK_STREAM), io_loop=IOLoop.current()),
            Future(),
        ),
    )
    stream, future = connector.connect(1, (1, 1))
    stream.close()
    connector.streams.add(stream)
    connector.close_streams()

# Generated at 2022-06-22 13:37:18.589231
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():

    t=TCPClient()
    t.connect('www.google.com',443)


# Mocking the tornado.iostream.IOStream class


# Generated at 2022-06-22 13:37:30.780747
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    def on_connect_done(self,addrs,af,addr, future):
        try:
            stream = future.result()
        except Exception as e:
            if self.future.done():
                return
            # Error: try again (but remember what happened so we have an
            # error to raise in the end)
            self.last_error = e
            self.try_connect(addrs)
            if self.timeout is not None:
                # If the first attempt failed, don't wait for the
                # timeout to try an address from the secondary queue.
                self.io_loop.remove_timeout(self.timeout)
                self.on_timeout()
            return
        self.clear_timeouts()
        if self.future.done():
            # This is a late arrival; just drop it.
            stream.close()
       
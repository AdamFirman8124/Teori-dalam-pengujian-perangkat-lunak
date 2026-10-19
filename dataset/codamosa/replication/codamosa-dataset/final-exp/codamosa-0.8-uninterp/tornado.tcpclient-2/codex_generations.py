

# Generated at 2022-06-22 13:27:48.085227
# Unit test for constructor of class _Connector
def test__Connector():
    # type: () -> None

    def _connect(af, addr):
        return (None, None)

    _Connector([], _connect)
    _Connector([(123, ("123", "456"))], _connect)


# Generated at 2022-06-22 13:27:59.629452
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import pytest
    from .util import ObjectDict
    from .util import FakeSocket

    class FakeIOStream:
        def __init__(self, socket):
            self.socket = socket

        def set_close_callback(self, callback):
            pass

        def close(self):
            pass

    class FakeSSLIOStream(FakeIOStream):
        def __init__(self, socket):
            super(FakeSSLIOStream, self).__init__(socket)
            self.closed = False
            self._on_connect(_SSLConnecting())

        def close(self):
            self.closed = True
            self.socket.close()

    class FakeSSLSocket(FakeSocket):
        def dup(self):
            return self

    class FakeSSLObject(object):
        def __init__(self):
            self.do_

# Generated at 2022-06-22 13:28:12.149856
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    from tornado.testing import AsyncTestCase
    from tornado.testing import gen_test

    class TestCase(AsyncTestCase):
        def _on_connect_done(self, future):
            def callback(future):
                callback.flag = True

            def callback_gen():
                callback_gen.flag = True

            callback.flag = False
            callback_gen.flag = False
            self.io_loop.add_callback(callback, future)
            self.io_loop.add_callback(callback_gen)

        @gen_test
        def test_on_connect_done(self):
            # success case
            future = Future()
            future.set_result("stream")

# Generated at 2022-06-22 13:28:14.096964
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    del self.connect_timeout
    del self.timeout



# Generated at 2022-06-22 13:28:26.816693
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    # test case 1: None value
    test1_connector = _Connector(None, None)
    test1_connector.timeout = None
    test1_connector.connect_timeout = None
    test1_connector.clear_timeouts()
    assert test1_connector.timeout is None and test1_connector.connect_timeout is None

    # test case 2: timeout value is not None
    test2_connector = _Connector(None, None)
    test2_connector.timeout = 1
    test2_connector.connect_timeout = 1

    test2_ioloop = MagicMock()
    test2_ioloop.remove_timeout = MagicMock(return_value=None)
    test2_connector.io_loop = test2_ioloop

    test2_connector.clear_timeouts()

# Generated at 2022-06-22 13:28:29.938292
# Unit test for method on_connect_timeout of class _Connector
def test__Connector_on_connect_timeout():
  obj = _Connector([(socket.AddressFamily.AF_INET, ('localhost', 80)), (socket.AddressFamily.AF_INET6, ('localhost', 80))], None)
  obj.on_connect_timeout()


# Generated at 2022-06-22 13:28:33.975009
# Unit test for method set_timeout of class _Connector
def test__Connector_set_timeout():
    set_timeout_obj = _Connector(None, None)
    if(set_timeout_obj):
        timeout = 1.1
        set_timeout_obj.set_timeout(timeout)



# Generated at 2022-06-22 13:28:45.019064
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    import tornado.testing
    import types
    import random
    import socket

    class Stream:
        def __init__(self) -> None:
            self.dirty = False
            pass

        def close(self) -> None:
            self.dirty = True

    class Test__Connector(tornado.testing.AsyncTestCase):
        def test__Connector(self):
            stream_list = [Stream(), Stream(), Stream(), Stream()]
            connector = _Connector([], None)
            connector.streams = set(stream_list)
            for stream in stream_list:
                assert not stream.dirty
                pass
            connector.close_streams()
            for stream in stream_list:
                assert stream.dirty
                pass
            pass

    tornado.testing.main()
    return

# Generated at 2022-06-22 13:28:53.247635
# Unit test for method clear_timeouts of class _Connector
def test__Connector_clear_timeouts():
    print("Test case: clear_timeouts() is called")
    io_loop = IOLoop.instance()
    io_loop.add_timeout(0, lambda: None)
    io_loop.add_callback(lambda: None)
    # test clear_timeouts()
    print("Test clear_timeouts() in _Connector")
    my_connector = _Connector(None, None)
    my_connector.io_loop = io_loop
    my_connector.timeout = io_loop.add_timeout(io_loop.time() + 180, lambda: None)
    my_connector.connect_timeout = io_loop.add_timeout(io_loop.time() + 180, lambda: None)
    my_connector.clear_timeouts()
    print("Finished testing _Connector.clear_timeouts()")



# Generated at 2022-06-22 13:28:54.440461
# Unit test for method clear_timeout of class _Connector
def test__Connector_clear_timeout():
    con = _Connector([], lambda f, a: None)
    con.timeout = 100
    con.clear_timeout()
    assert con.timeout == None


# Generated at 2022-06-22 13:29:14.710844
# Unit test for constructor of class _Connector
def test__Connector():
    addrinfo = [
        (socket.AF_INET, ("127.0.0.1", 80)),
        (socket.AF_INET6, ("::1", 80)),
    ]
    connect = lambda af, addr: (None, None)
    connector = _Connector(addrinfo, connect)



# Generated at 2022-06-22 13:29:26.684362
# Unit test for constructor of class _Connector
def test__Connector():
    """
    Note: There is no way to test the constructor of class _Connector
    directly, so this is a "test" of the constructor.
    """
    addrinfo = [
        (socket.AF_INET, ("localhost", 8830)),
        (socket.AF_INET6, ("localhost", 8830)),
        (socket.AF_INET, ("localhost", 8831)),
        (socket.AF_UNIX, ("localhost", 8831)),
        (socket.AF_UNIX, ("localhost", 8832)),
    ]
    expected_primary_addrs = [
        (socket.AF_INET, ("localhost", 8830)),
        (socket.AF_INET, ("localhost", 8831)),
    ]

# Generated at 2022-06-22 13:29:38.472881
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import sys
    import unittest

    class _ConnectorTestCase(unittest.TestCase):
        def test__Connector_try_connect(self):
            """Tests that Connector.try_connect only contacts addresses in primary
            """
            io_loop = IOLoop()
            io_loop.make_current()
            io_loop.install()
            future = Future()
            connector = _Connector(
                [(socket.AF_INET, ("localhost", 80))],
                lambda af, addr: (io_loop.add_callback(future.set_result, (af, addr)), future),
            )
            addrs = iter([(socket.AF_INET, ("1.2.3.4", 80)), (socket.AF_INET, ("4.3.2.1", 80))])
            connector.try_connect

# Generated at 2022-06-22 13:29:51.043052
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import struct
    import asyncio
    async def coroutine():
        client = TCPClient()
        stream = await client.connect("www.google.com", 80)
        await stream.write(b"GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n")
        header_data = await stream.read_bytes(4)
        header_size = struct.unpack(">L", header_data)[0]
        header_bytes = await stream.read_bytes(header_size)
        header = header_bytes.decode("utf-8")
        print("%d bytes received" % len(header))
        client.close()
        return header
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(coroutine())

# Generated at 2022-06-22 13:29:56.567623
# Unit test for constructor of class _Connector
def test__Connector():
    connector = _Connector(None, None)
    assert connector.future.done() == False
    assert connector.connect == None
    assert connector.timeout == None
    assert connector.connect_timeout == None
    assert connector.last_error == None
    assert connector.remaining == None
    assert connector.primary_addrs == None
    assert connector.secondary_addrs == None
    assert connector.streams == set()


# Generated at 2022-06-22 13:30:09.194074
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import time
    import functools
    import time
    import logging
    import tornado
    import tornado.httpclient
    import tornado.testing
    import tornado.platform.asyncio
    import tornado.testing

    tornado.platform.asyncio.AsyncIOMainLoop().install()
    import asyncio
    import tornado.ioloop

    async def _test():
        req = tornado.httpclient.HTTPRequest("http://www.google.com/")
        client = tornado.httpclient.AsyncHTTPClient(force_instance=True)
        start = time.time()
        resp = await client.fetch(req)
        print("%r" % resp)
        print("%r" % (time.time() - start))


# Generated at 2022-06-22 13:30:19.667909
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    global mock_af_addr_queue
    global mock_stream_future_queue
    global mock_stream_future

    global mock_af_addr
    global mock_af
    global mock_addr
    global mock_remaining
    global mock_stream
    global mock_future_done

    global mock_try_connect
    global mock_set_timeout
    global mock_set_connect_timeout
    global mock_future
    global mock_on_connect_done

    # Case 0: exception in getattrinfo
    mock_af_addr_queue = iter(
        [
            (socket.AF_INET, ("localhost", 8000)),
            (socket.AF_INET6, ("localhost", 8000)),
        ]
    )
    mock_stream_future_queue = iter([(None, None)])

# Generated at 2022-06-22 13:30:21.331154
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    import asyncio
    async def main():
        client = TCPClient()
        stream = await client.connect('localhost', 8080)
        print(stream)
    asyncio.run(main())

if __name__ == '__main__':
    test_TCPClient_connect()

# Generated at 2022-06-22 13:30:26.778371
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    io_loop = IOLoop.current()
    addr = ("1.1.1.1", 80)
    stream, future = IOStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM), io_loop)
    c = _Connector(addrinfo=list(), connect=(lambda s: (stream, future)))
    c.streams = {stream}
    c.close_streams()
    f = future
    assert f.cancelled()

# Generated at 2022-06-22 13:30:31.841927
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    class stream:
        def close(self):
            pass
    ds = _Connector([(socket.AF_INET, ("127.0.0.1", 20))], lambda x,y: (stream(), Future()))
    ds.streams = {stream()}
    ds.close_streams()

# Generated at 2022-06-22 13:31:51.299603
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    class Mocked_Future:
        def __init__(self, result):
            self.result = result
        def result(self):
            return self.result
    for result_list in [["stream1"], ["stream2"], ["stream3"]]:
        test_iterator = iter(result_list)
        connector = _Connector(
            [], lambda af, addr: (None, Mocked_Future(next(test_iterator)))
        )
        temp_streams = ["stream0", "stream1", "stream2", "stream3"]
        temp_streams.append(None)
        connector.streams = set(temp_streams)
        connector.remaining = len(result_list)
        connector.future = Future()
        connector.try_connect(test_iterator)
        connector.clear_timeouts()

# Generated at 2022-06-22 13:32:01.928241
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    c = _Connector([(1, (1,1)), (2, (2,2)), (3, (3,3))], None)
    #
    # with non-trivial connect function
    def connect(af, addr):
        return None, None
    # without timeout
    c.try_connect(c.primary_addrs)
    # with timeout
    c.try_connect(c.primary_addrs)
    #
    # with trivial connect function
    def connect(af, addr):
        return None, None
    # without timeout
    c.try_connect(c.primary_addrs)
    # with timeout
    c.try_connect(c.primary_addrs)
    print("test__Connector_try_connect() called")


# Generated at 2022-06-22 13:32:14.374898
# Unit test for method start of class _Connector

# Generated at 2022-06-22 13:32:25.382015
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    """Unit test for method on_connect_done of class _Connector"""
    import time
    import tornado

    async def async_test():
        addrinfo = list()
        addrinfo.append((socket.AF_INET, ('0.0.0.0', 0)))
        addrinfo.append((socket.AF_INET6, ('0.0.0.0', 0)))

        def connect(af, addr):
            f = Future()
            if af == socket.AF_INET:
                f.set_result(None)
            else:
                f.set_exception(Exception())
            return None, f

        c = _Connector(addrinfo, connect)
        try:
            r = await c.start()
        except Exception as e:
            print('[FAILED]')
            raise e

    tornado.iol

# Generated at 2022-06-22 13:32:33.634602
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    try_connect = _Connector.try_connect
    assert try_connect.__name__ == "_Connector.try_connect"

    c = _Connector([], lambda af, addr: None)
    c.future = Future()
    c.future.set_exception(Exception("a"))

    def f(addr : Tuple[socket.AddressFamily, Tuple]) -> None:
        # Python 3.5+: change parameter to a generator function
        if addr:
            raise StopIteration
        return None

    c.try_connect(f)

    try:
        c.try_connect(None)
    except TypeError as err:
        assert str(err) == 'unexpected type: "NoneType"'

# Generated at 2022-06-22 13:32:43.718928
# Unit test for method start of class _Connector
def test__Connector_start():
    # This function will be converted to a unit test.
    # The argument names will be adjusted to match the
    # parameter names in the implementation.
    def run(
        self,
        timeout,
        connect_timeout,
        addrinfo,
        connect,
        IOStream,
        IOLoop,
    ):
        # type: (Any, float, Optional[Union[float, datetime.timedelta]], List[Tuple], Callable[[socket.AddressFamily, Tuple], Tuple[IOStream, "Future[IOStream]"]], Any, Any) -> "Future[Tuple[socket.AddressFamily, Any, IOStream]]"
        return _Connector(addrinfo, connect).start(
            timeout=timeout, connect_timeout=connect_timeout
        )



# Generated at 2022-06-22 13:32:45.736960
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    connector = _Connector("", "")
    connector.streams = [1,2,3]
    connector.close_streams()
    assert(connector.streams == [])
test__Connector_close_streams()



# Generated at 2022-06-22 13:32:53.352835
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.httputil import HTTPHeaders
    from tornado.options import options
    import tornado.testing
    import urllib.parse

    def get_new_ioloop():
        return tornado.testing.AsyncTestCase().get_new_ioloop()

    req = HTTPRequest('http://www.yahoo.com', method='GET', headers=HTTPHeaders({'User-Agent': 'Mozilla/5.0'}))
    client = SimpleAsyncHTTPClient(ioloop=get_new_ioloop(), force_instance=True, defaults=dict(request_timeout=3600.0, connect_timeout=3600.0, max_clients=100, max_buffer_size=10000000))

# Generated at 2022-06-22 13:33:05.196611
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    class _MockIOLoop(object):
        def __init__(self):
            self.time_ = 0

        def time(self):
            return self.time_

        def add_timeout(self, timeout, callback, *args, **kwargs):
            if callable(timeout):
                # First argument is a timedelta.
                return self.add_timeout(self.time() + timeout.total_seconds(),
                                        callback, *args, **kwargs)
            else:
                return 0

        def remove_timeout(self, timeout):
            pass

    class _MockIOStream(object):
        def __init__(self, socket):
            self.socket = socket

        def set_close_callback(self, callback):
            pass

        def close(self):
            pass

    # Scenario: _Connector.on

# Generated at 2022-06-22 13:33:07.641433
# Unit test for method start of class _Connector
def test__Connector_start():
    """
    Test case for _Connector.start
    """
    connector = _Connector([], lambda a, b: (None, Future()))
    timeout = 0
    connect_timeout = None
    assert connector.start(timeout, connect_timeout) is not None


# Generated at 2022-06-22 13:33:32.074878
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    def on_connect(stream, address):
        print("connect to", address)

    def on_connect_failure(exc):
        print("error occurred: %r" % exc)

    client = TCPClient()
    try:
        stream = client.connect("localhost", 8888)
        stream.set_close_callback(on_connect)
        stream.set_close_callback(on_connect_failure)
    except Exception as e:
        print(e)


# Generated at 2022-06-22 13:33:38.243475
# Unit test for method on_connect_done of class _Connector
def test__Connector_on_connect_done():
    stream = gen.sleep(1)
    future = Future()
    addrs = iter(())
    af = socket.AF_INET
    addr = ()
    future.set_exception(Exception("abcd"))
    test = _Connector(addrs, future)
    test.try_connect(addrs)
    test.streams.add(stream)
    assert test.on_connect_done(addrs, af, addr, future) == None



# Generated at 2022-06-22 13:33:48.495272
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    """
    Test case to test the functionality of connect method in the class TCPClient.
    """
    resolver = Resolver()
    tcp_client = TCPClient(resolver)
    af = socket.AF_INET
    host = "www.python.org"
    port = 80
    ssl_options = None
    max_buffer_size = 1000
    source_ip = "::1"
    source_port = "8080"
    timeout = 20
    stream = tcp_client.connect(host, port, af, ssl_options, max_buffer_size,
                                source_ip, source_port, timeout)
    if stream:
        print("Stream is a success ")
    else:
        print("Stream is a failure")

# Generated at 2022-06-22 13:33:49.988099
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    # mypy
    c = _Connector([(socket.AF_INET, ('127.0.0.1', 1234))], connect)
    c.try_connect([(socket.AF_INET, ('127.0.0.1', 1234))].__iter__())



# Generated at 2022-06-22 13:33:58.342939
# Unit test for method close_streams of class _Connector
def test__Connector_close_streams():
    def test_scenario(
        msg: str,
        connect: List[IOStream],
        result: List[IOStream],
        close_times: int,
    ):
        import pytest
        from tornado.iostream import _StreamClosedError
        import mock

        io_loop = IOLoop.current()

        def connecter(af: int, addr: Tuple) -> Tuple[IOStream, Future[IOStream]]:
            io_stream = connect.pop(0)
            io_stream._closed_exc = _StreamClosedError()
            return io_stream, Future()

        # Create a Connector instance to close
        connector = _Connector([(0, (1, 2))], connecter)
        # Check that the connector has a set of streams
        assert connect == []

# Generated at 2022-06-22 13:34:01.970373
# Unit test for method start of class _Connector
def test__Connector_start():
    def test_if_method_return_future(addrinfo: List[Tuple]) -> None:
        if __name__ == "__main__":
            future = _Connector(addrinfo, None).start()
            assert isinstance(future, Future)

    test_if_method_return_future([])



# Generated at 2022-06-22 13:34:07.430864
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import threading
    import time
    import tornado.testing
    import unittest

    class MyTestCase(tornado.testing.AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.loop = tornado.ioloop.IOLoop()
            self.loop.make_current()
            self.test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.test_socket.bind(("127.0.0.1", 0))
            self.test_socket.listen(5)
            self.port = self.test_socket.getsockname()[1]
            print("port =", self.port)
            self.connect = self.connect_mock


# Generated at 2022-06-22 13:34:15.979624
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    try:
        __import__("ioloop")
        __import__("iostream")
    except Exception:
        return
    def verify_force_timeout(
        tmo: float,
        primary_size: int,
        secondary_size: int,
        expected_count: int,
        expected_last_error: Optional[Exception],
    ) -> None:
        """Mock the ioloop and verify that _Connector works as expected."""

        try:
            from unittest.mock import Mock
        except ImportError:
            from mock import Mock

        io_loop = Mock()
        io_loop.time.return_value = 0
        io_loop.add_timeout.side_effect = [
            "timeout",
            "connect_timeout",
        ][: expected_count]
        io_loop.remove_timeout

# Generated at 2022-06-22 13:34:26.372213
# Unit test for method start of class _Connector
def test__Connector_start():
    __tracebackhide__ = True  # noqa: F821 pylint:disable=used-before-assignment
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 8888))]
    f = Future()
    f.set_result(('127.0.0.1', 8888))
    m = MagicMock()
    stream = m.return_value = MagicMock()
    stream.socket = MagicMock()
    c = _Connector(addrinfo, m)
    f = c.start()
    assert f.result() == ('127.0.0.1', 8888, stream)
    assert m.call_count == 1
    assert stream.socket.connect.call_count == 1

# Generated at 2022-06-22 13:34:37.070967
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    from tornado.concurrent import Future
    from tornado.iostream import IOStream

    class DummySocket(object):
        def __init__(self, family: int, type_: int, proto: int) -> None:
            self.family = family
            self.type = type_
            self.proto = proto

        def getpeername(self) -> Tuple:
            return None

    def fake_connect(
        address_family: socket.AddressFamily, address: Tuple
    ) -> Tuple[IOStream, Future[IOStream]]:
        future = Future()
        future.set_result(IOStream(DummySocket(address_family, 0, 0)))
        return None, future


# Generated at 2022-06-22 13:36:33.554107
# Unit test for method start of class _Connector
def test__Connector_start():
    rs = Resolver()
    afs = list(rs.resolve_future(0))
    afs[2] = 1
    fa = afs[1]
    def test_connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[IOStream, "Future[IOStream]"]:
        pass
    test_connector = _Connector(afs, test_connect)
    f = test_connector.start(0.3, 0.5)
    f.result()



# Generated at 2022-06-22 13:36:41.446518
# Unit test for method try_connect of class _Connector
def test__Connector_try_connect():
    import tornado.testing
    import logging
    import functools
    import ioloop

    # Test of method try_connect of class _Connector.
    # Test of the case where the first connection is successful.

    async def test_case_1(ioloop: 'ioloop.IOLoop'):
        ioloop.logger = logging.getLogger('IOLoop')
        ioloop.logger.setLevel(logging.DEBUG)
        future = Future()

        def connect(af: socket.AddressFamily, addr: Tuple[Any]) -> Tuple[IOStream, Future]:
            stream = IOStream(socket.socket(af, socket.SOCK_STREAM))
            stream.connect(addr)
            return (stream, future)

# Generated at 2022-06-22 13:36:48.233728
# Unit test for method connect of class TCPClient
def test_TCPClient_connect(): 
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    instance = TCPClient()
    assert isinstance(instance, TCPClient)
    stream = event_loop.run_until_complete(instance.connect('www.google.com', 80, timeout='100'))
    assert isinstance(stream, IOStream)
    event_loop.run_until_complete(stream.close())

# Generated at 2022-06-22 13:36:59.768886
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    # Instantiation of the needed objects
    my_TCPClient = TCPClient()
    my_delta = datetime.timedelta(seconds=10)
    # Test the function without arguments
    my_IOStream = my_TCPClient.connect(host="www.tornadoweb.org", port=80)
    my_IOStream = my_TCPClient.connect(host="www.tornadoweb.org", port=80, af=socket.AF_INET)
    my_IOStream = my_TCPClient.connect(host="www.tornadoweb.org", port=80, ssl_options=dict())
    my_IOStream = my_TCPClient.connect(host="www.tornadoweb.org", port=80, max_buffer_size=20)
    my_IOStream = my_TCPClient.connect

# Generated at 2022-06-22 13:37:05.212129
# Unit test for method start of class _Connector
def test__Connector_start():
    import unittest
    from unittest import mock

    from tornado import gen
    from tornado import testing

    from tornado.iostream import StreamClosedError

    from tornado.netutil import Resolver
    from tornado.netutil import test_utils

    def make_add_done_callback(future_obj, raises=False):
        def callback(future):
            if raises:
                future.set_exception(Exception("error"))
            else:
                future.set_result("success")

        future_obj.add_done_callback(callback)

    class _ConnectorTest(testing.AsyncTestCase):
        # XXX: mock Resolver
        @testing.gen_test
        def test_happy_eyeballs(self):
            resolver = Resolver()

# Generated at 2022-06-22 13:37:14.115045
# Unit test for method start of class _Connector
def test__Connector_start():
    addrs = [(socket.AF_INET, ('100.102.103.104', '200'))]
    port = None
    ssl_options = None
    resolver = Resolver()
    io_loop = IOLoop.current()


    def connect(af: socket.AddressFamily, addr: Tuple) -> Tuple[IOStream, Future]:
        return IOStream(socket.socket(af), io_loop=io_loop), Future()

    connector = _Connector(addrs, connect)
    future = connector.start()
    result = future.result()
    assert len(result) == 3



# Generated at 2022-06-22 13:37:26.524547
# Unit test for method connect of class TCPClient
def test_TCPClient_connect():
    """

    :return:
    """
    import asyncio

    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    from tornado.web import Application
    from tornado.web import RequestHandler
    from tornado.web import asynchronous

    class TestHandler(RequestHandler):
        @asynchronous
        async def get(self):
            self.write("Hello, world")
            self.finish()

    class MyServer(object):
        def __init__(self, port):
            self.app = Application([
                (r"/", TestHandler),
            ])
            self.server = HTTPServer(self.app)
            self.server.listen(port)
            self.ioloop = IOLoop.current()

        def start(self):
            self.ioloop.start()

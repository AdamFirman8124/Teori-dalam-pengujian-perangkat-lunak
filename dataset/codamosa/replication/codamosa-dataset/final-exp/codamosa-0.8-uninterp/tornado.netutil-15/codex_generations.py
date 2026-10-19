

# Generated at 2022-06-14 12:31:44.759623
# Unit test for function add_accept_handler
def test_add_accept_handler():
    io_loop = IOLoop.current()
    io_loop.make_current()
    server_sock,client_sock = socket.socketpair()
    ioloop_callback_called = False
    def ioloop_callback(connection,address):
        nonlocal ioloop_callback_called
        ioloop_callback_called = True
        assert connection is client_sock
        assert address == client_sock.getsockname()
    handler_callback = add_accept_handler(server_sock,ioloop_callback)
    client_sock.send(b"hello")
    io_loop.add_callback(handler_callback)
    io_loop.add_callback(io_loop.stop)
    io_loop.start()


# Generated at 2022-06-14 12:31:56.939564
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    mapping = {
        # Hostname to host or ip
        "example.com": "127.0.1.1",

        # Host+port to host+port
        ("login.example.com", 443): ("localhost", 1443),

        # Host+port+address family to host+port
        ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
    }


    class DummyResolver(Resolver):
        def resolve(
            self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
        ) -> Awaitable[List[Tuple[int, Any]]]:
            return []

        def close(self) -> None:
            pass

    resolver = DummyResolver()

# Generated at 2022-06-14 12:32:07.808778
# Unit test for function add_accept_handler
def test_add_accept_handler():
    from tornado.testing import AsyncTestCase
    from pprint import pprint

    class TestAddAcceptHandler(AsyncTestCase):
        def test_add_accept_handler(self):
            port = 8888
            def callback(connection: socket.socket, address: Any) -> None:
                print(connection)
                print(address)
                io_loop.stop()
            io_loop = IOLoop.current()
            sockets = bind_sockets(port)
            add_accept_handler(sockets[0], callback)
            io_loop.start()
            io_loop.stop()
    test=TestAddAcceptHandler()
    # test.test_add_accept_handler()



# Generated at 2022-06-14 12:32:19.280033
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = Resolver.configure('tornado.netutil.ThreadedResolver')
    host = 'example.com'
    port = 80
    family = socket.AF_INET
    test_override = OverrideResolver(resolver,{'example.com':'127.0.1.1'})
    f = test_override.resolve(host, port, family)
    result = f.result()
    assert len(result) == 1, "The length of result is 1"
    assert result[0][1][0] == '127.0.1.1', "The hostname has been changed"
    assert result[0][1][1] == 80, "The port has been changed"


# Generated at 2022-06-14 12:32:27.302170
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    import tornado.platform.asyncio
    from tornado.platform.asyncio import BaseAsyncIOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    # BaseAsyncIOLoop.current() is not a coroutine.
    # Instead of making it a coroutine, we use the function run_coroutine_threadsafe.
    coroutine1 = BaseAsyncIOLoop.current()
    event_loop = asyncio.get_event_loop()
    future1 = asyncio.run_coroutine_threadsafe(coroutine1, event_loop)
    io_loop = future1.result()
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver = ExecutorResolver(executor=executor)
    resolver.close()
    return

# Generated at 2022-06-14 12:32:29.256961
# Unit test for function add_accept_handler
def test_add_accept_handler():
    def callback(connection, address):
        print(connection, address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remove_handler = add_accept_handler(sock, callback)



# Generated at 2022-06-14 12:32:32.880839
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    d = DefaultExecutorResolver()
    async def t():
        print("start resolving")
        r = await d.resolve("127.0.0.1", 80)
        print("resolved:", r)
    IOLoop.current().run_sync(t)

test_DefaultExecutorResolver_resolve()



# Generated at 2022-06-14 12:32:40.689588
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    ssl_options = {
        "ssl_version" : 3,
        "certfile" : "certfile",
        "keyfile" : "keyfile",
        "cert_reqs" : 2,
        "ca_certs" : "ca_certs",
        "ciphers" : "ciphers",
    }
    context = ssl_options_to_context(ssl_options)
    assert context is not None



# Generated at 2022-06-14 12:32:45.848249
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    """Test for initialize of class ExecutorResolver"""
    executor = concurrent.futures.ThreadPoolExecutor(3)
    resolver = ExecutorResolver(executor=executor, close_executor=True)
    resolver.initialize(executor=executor, close_executor=True)
    assert isinstance(resolver, ExecutorResolver)


# Generated at 2022-06-14 12:32:53.217229
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_socket.connect(('sni.velox.ch', 443))
    assert isinstance(
        ssl_wrap_socket(test_socket, {'ssl_version': ssl.PROTOCOL_TLSv1}, 'sni.velox.ch'), ssl.SSLSocket
    )

# Generated at 2022-06-14 12:33:26.887173
# Unit test for function bind_sockets
def test_bind_sockets():
    import tornado.testing
    import tornado.netutil
    import socket
    import tornado.ioloop

    def bind_both_ports(port, reuse_port):
        print("Binding port {} with reuse port {}".format(port, reuse_port))
        sockets = bind_sockets(port, reuse_port=reuse_port)
        #print(sockets)
        assert len(sockets) > 0
        assert sockets[0].getsockname()[1] == port
        sock = sockets[0]

        def try_accept():
            conn, addr = sock.accept()
            print("Accepted connection from {}".format(addr))
            conn.close()
            io_loop.stop()

        io_loop = tornado.ioloop.IOLoop.current()

# Generated at 2022-06-14 12:33:29.887521
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    r = Resolver()
    try:
        r.resolve('www.baidu.com', 80)
    except NotImplementedError:
        pass


# Generated at 2022-06-14 12:33:33.586920
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    host = "httpbin.org"
    port = 80
    family = socket.AF_UNSPEC
    r = Resolver()
    out = r.resolve(host, port, family)
    print(out)


# Generated at 2022-06-14 12:33:40.698621
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    import asyncio
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    policy = AnyThreadEventLoopPolicy()
    policy.set_event_loop(loop)
    AsyncIOMainLoop().install()
    
    
    # call initialize method
    resolver = ExecutorResolver()
    executor = concurrent.futures.ThreadPoolExecutor(3)
    resolver.initialize(executor)



# Generated at 2022-06-14 12:33:52.954245
# Unit test for method resolve of class Resolver

# Generated at 2022-06-14 12:33:55.792841
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    r = ExecutorResolver()
    r2 = ExecutorResolver()
    assert r.close_executor == True
    assert r2.close_executor == True



# Generated at 2022-06-14 12:34:06.325535
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    # Insert your test code here to test method resolve of class DefaultExecutorResolver
    #
    # For example:
    #
    # from tornado.testing import AsyncTestCase, gen_test
    # from tornado.netutil import DefaultExecutorResolver
    # from tornado.platform.asyncio import to_asyncio_future
    # class MyTestCase(AsyncTestCase):
    #     @gen_test
    #     def test_resolve(self):
    #         r = DefaultExecutorResolver()
    #         ret = await to_asyncio_future(r.resolve("localhost", 80))
    #         self.assertEqual("expected result", ret)

    pass



# Generated at 2022-06-14 12:34:13.497195
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    # must be called before any invoke of loop()
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    return_value = loop.run_until_complete(ExecutorResolver().resolve('127.0.0.1', 8000))
    assert return_value == [(2, ('127.0.0.1', 8000))], return_value
test_ExecutorResolver_resolve()


# Generated at 2022-06-14 12:34:26.889229
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    import time
    import sys
    import asyncio
    class resolver(Resolver):
        def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
            return asyncio.get_event_loop().call_later(1, lambda : None)
            # return None
    host = 'google.com'
    port = 443
    resolver = DefaultExecutorResolver()
    future = resolver.resolve(host, port)
    loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(future)
    time_start = time.time()
    result = loop.run_until_complete(future)
    time_end = time.time()

# Generated at 2022-06-14 12:34:34.501846
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    # method Resolver.resolve in class Resolver should have
    # signature Resolver.resolve(self, host, port, family=socket.AF_UNSPEC)
    # -> Future[List[Tuple[int, Any]]]
    resolver = Resolver()

# Generated at 2022-06-14 12:34:56.713748
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    import tornado.platform.asyncio
    import tornado.platform.asyncio

    def test(exect: bool) -> None:
        import concurrent.futures
        resolver = ExecutorResolver()
        executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=3, thread_name_prefix="Thread-1"
        )
        resolver.initialize(executor, exect)
        assert resolver.executor is executor
        assert resolver.io_loop is IOLoop.current()
        assert resolver.close_executor is exect
    test(exect=True)



# Generated at 2022-06-14 12:34:59.335006
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
	resolver = ExecutorResolver(dummy_executor)	
	assert resolver.close_executor == True
	assert resolver.close_executor == True



# Generated at 2022-06-14 12:34:59.879160
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    #
    assert False



# Generated at 2022-06-14 12:35:05.204372
# Unit test for function add_accept_handler
def test_add_accept_handler():
    io_loop = IOLoop()

    def callback(sock: socket.socket, address: str) -> None:
        pass

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    remove_handler = add_accept_handler(sock, callback)
    remove_handler()

    io_loop.close()


# Generated at 2022-06-14 12:35:09.811268
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    print("Test for method 'resolve' of class 'DefaultExecutorResolver'")
    der = DefaultExecutorResolver()
    print(der.resolve("www.google.com",80))
    print(der.resolve("localhost", 80))


# Generated at 2022-06-14 12:35:19.985287
# Unit test for function add_accept_handler
def test_add_accept_handler():
    io_loop = IOLoop.current()
    async def test_main():
        s = socket.socket()
        s.bind(("localhost", 8888))
        s.listen(10)
        def handler(connection, address):
            print("accept:", address)
            connection.send("welcome".encode("utf-8"))
            connection.close()
        remove_handler = add_accept_handler(s, handler)
        remove_handler()
    io_loop.run_sync(test_main)
# Unit test code for function test_add_accept_handler.
# It will respond "welcome" to every connection and then close it.
# To run test:
# python3 -c "from netutil import *; test_add_accept_handler()"



# Generated at 2022-06-14 12:35:21.478886
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = OverrideResolver()
    resolver.initialize(resolver, {'test1': 'test2'})
    results = resolver.resolve('test3', 80)
    assert results is not None


# Generated at 2022-06-14 12:35:25.289577
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    # Test with executor
    executor = dummy_executor
    resolver = ExecutorResolver(executor = executor)
    assert resolver.executor == executor
    assert resolver.close_executor == True
    # Test without executor
    resolver = ExecutorResolver()
    assert resolver.executor == dummy_executor
    assert resolver.close_executor == False


# Generated at 2022-06-14 12:35:28.230060
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    sock = bind_unix_socket("test_bind_unix_socket.sock")
    sock.close()
    os.remove("test_bind_unix_socket.sock")



# Generated at 2022-06-14 12:35:35.691105
# Unit test for function add_accept_handler
def test_add_accept_handler():
    client_socket, server_socket = socket.socketpair()
    server_socket.setblocking(False)
    def accept_handler(client_socket: socket.socket, address: Any) -> None:
        client_socket.close()
    add_accept_handler(server_socket, accept_handler)
    IOLoop.current().add_callback(IOLoop.current().add_callback, client_socket.send,b'A')
    IOLoop.current().start()
    client_socket.close()
    server_socket.close()



# Generated at 2022-06-14 12:36:01.262159
# Unit test for function add_accept_handler
def test_add_accept_handler():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.platform.asyncio import AsyncIOMainLoop

    class TestAddAcceptHandler(AsyncTestCase):
        def setUp(self):
            AsyncIOMainLoop().install()

            super(TestAddAcceptHandler, self).setUp()

            self.ios = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ios.bind(("127.0.0.1", 0))
            self.ios.listen(1)

            self.ios_port = self.ios.getsockname()[1]

            self.io_loop = IOLoop.current()

            self.accept_num = 0

        def tearDown(self):
            self.ios.close()

# Generated at 2022-06-14 12:36:10.824942
# Unit test for function add_accept_handler
def test_add_accept_handler():
    import tempfile
    import threading
    import socket
    import tornado.ioloop
    import unittest
    import time

    class Test(unittest.TestCase):
        def setUp(self):
            super(Test, self).setUp()
            self.ioloop = tornado.ioloop.IOLoop() 

        def tearDown(self):
            self.ioloop.close(all_fds=True)
            super(Test, self).tearDown()

        def test_add_accept_handler(self):
            # Create a listening socket.
            sock, port = bind_unix_socket(None)

            # Start a thread to connect to it.
            connections = []  # type: List[socket.socket]
            connected_event = threading.Event()

            def client_thread():
                client = socket

# Generated at 2022-06-14 12:36:17.534969
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    def test_configurable_default_is_DefaultExecutorResolver():
        # DefaultExecutorResolver is a subclass of DefaultExecutorResolver and Resolver
        assert issubclass(DefaultExecutorResolver,Resolver) and issubclass(DefaultExecutorResolver,DefaultExecutorResolver)
        assert Resolver.configurable_base is Resolver
        assert Resolver.configurable_default is DefaultExecutorResolver
    def test_resolve_method():
        resolver = Resolver()
        # Resolver.resolve is abstract class, to be implemented by subclasses.
        # Resolver.resolve takes three arguments, host, port, family
        assert callable(resolver.resolve) and len(signature(resolver.resolve).parameters)==3
    test_configurable_default_is_DefaultExecutorResolver()

# Generated at 2022-06-14 12:36:24.253334
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    context = ssl_options_to_context({})
    assert isinstance(context, ssl.SSLContext)

    # Ensure conversion to SSLContext actually works
    with open(os.path.join(os.path.dirname(__file__), "test.crt")) as f:
        cert = f.read()
    with open(os.path.join(os.path.dirname(__file__), "test.key")) as f:
        key = f.read()


# Generated at 2022-06-14 12:36:26.276949
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    resolver = ExecutorResutor()
    resolver.close()


# Generated at 2022-06-14 12:36:29.633482
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    with OverrideResolver() as resolver:
        assert(resolver.resolve("test_hostname", 80, socket.AF_INET) is None)



# Generated at 2022-06-14 12:36:35.525849
# Unit test for function bind_sockets
def test_bind_sockets():
    from tornado.netutil import bind_sockets
    try:
        bind_sockets(None)
        assert False, "Must provide a port"
    except ValueError:
        pass
    try:
        bind_sockets(9999999)
        assert False, "Must provide a valid port"
    except socket.error:
        pass
    try:
        bind_sockets(9999999, "127.0.0.1", socket.AF_UNSPEC)
        assert False, "Must provide a valid port"
    except socket.error:
        pass



# Generated at 2022-06-14 12:36:37.485901
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    pass



# Generated at 2022-06-14 12:36:46.866982
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    resolver = DefaultExecutorResolver()
    loop = IOLoop.current()
    result = loop.run_sync(resolver.resolve, "example.com", "80", socket.AF_UNSPEC)
    print(result)


async def _resolve_addr_future(
    host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
) -> List[Tuple[int, Any]]:
    return await asyncio.get_event_loop().run_in_executor(
        None, _resolve_addr, host, port, family
    )



# Generated at 2022-06-14 12:36:48.632710
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    DefaultExecutorResolver().resolve("www.google.com", 80)


# Generated at 2022-06-14 12:37:22.600429
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    r = DefaultExecutorResolver()
    # ip = socket.gethostbyname('www.tornadoweb.org')
    # ip = socket.gethostbyname('www.python.org')
    # ip = socket.gethostbyname('www.wikipedia.org')
    ip = socket.gethostbyname('www.google.com')
    futures = r.resolve(ip, 80)
    print(futures)



# Generated at 2022-06-14 12:37:23.595481
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    Resolver.close()

# Generated at 2022-06-14 12:37:27.491168
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = OverrideResolver(0, {"lolipoop.co":"127.0.0.1"})
    result = resolver.resolve("lolipoop.co", 0)
    if result != host:
        raise Exception(result)

    # Unit test for method close of class OverrideResolver

# Generated at 2022-06-14 12:37:34.270332
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    import warnings
    warnings.warn(
        "test_DefaultExecutorResolver_resolve is deprecated; use test_DefaultExecutorResolver_resolve_async",
        DeprecationWarning,
        stacklevel=2
    )
    from tornado.ioloop import IOLoop
    from functools import partial
    loop = IOLoop.current()
    resolver = DefaultExecutorResolver()
    cb = partial(lambda x: loop.stop(), None)
    rst = resolver.resolve("localhost", 9999)
    # type: ignore
    try:
        loop.run_until_complete(asyncio.ensure_future(rst, loop=loop))
    except:
        return False
    return True
executor.run(test_DefaultExecutorResolver_resolve)


# Generated at 2022-06-14 12:37:36.293033
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    try:
        res = ExecutorResolver()
        res.close()
    except Exception:
        assert True



# Generated at 2022-06-14 12:37:46.577368
# Unit test for function bind_sockets
def test_bind_sockets():
    sock = bind_sockets(8888)[0]
    assert sock.getsockname()[0] == "0.0.0.0"
    assert sock.getsockname()[1] == 8888
    sock.close()
    sock = bind_sockets(8000,"127.0.0.1")[0]
    assert sock.getsockname()[0] == "127.0.0.1"
    assert sock.getsockname()[1] == 8000
    sock.close()
    #assert bind_sockets(0) == 2
    #assert bind_sockets(0, "localhost") == 2
    #assert bind_sockets(0, "localhost", socket.AF_INET) == 1
    #assert bind_sockets(0, "localhost", socket.AF_INET6) == 1
    #

# Generated at 2022-06-14 12:37:48.992343
# Unit test for function bind_sockets
def test_bind_sockets():
    sockets = bind_sockets(8888)
    print([s.getsockname() for s in sockets])
# test_bind_sockets()


# Generated at 2022-06-14 12:37:58.737392
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    
    from tornado.concurrent import dummy_executor
    from tornado.platform.asyncio import to_asyncio_future
    #
    import concurrent.futures
    import asyncio
    #
    #
    loop = asyncio.get_event_loop()
    #
    def func1(a, b, c=None):
        print('func1')
        return a, b, c
    
    def func2():
        raise RuntimeError
    #
    #
    executor = dummy_executor
    #
    result = None
    ex = None
    done = False
    try:
        exc = ExecutorResolver(executor=executor)
        #
        result = exc.resolve('127.0.0.1', 20007)
        #
    except Exception as e:
        ex

# Generated at 2022-06-14 12:38:07.627216
# Unit test for function add_accept_handler
def test_add_accept_handler():
    io_loop = IOLoop.current()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))

    def accept_handler(connection, address):
        print("%s:%s" % (connection, address))
        # connection.close()

    add_accept_handler(sock, accept_handler)
    io_loop.start()


# test_add_accept_handler()



# Generated at 2022-06-14 12:38:14.563601
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    """

    :return:
    """
    import tornado.ioloop
    import tornado.httpserver
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world")

    resolver = Resolver()

    # 通过Input对象的的read方法读取控制台的输入，这里阻塞了
    input()
    resolver.resolve('google.com',80)
    tornado.ioloop.IOLoop.instance().start()


# Generated at 2022-06-14 12:38:28.578832
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = OverrideResolver(resolver, mapping)
    resolver.resolve(host, port, family)


# Generated at 2022-06-14 12:38:33.129287
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    sock = bind_unix_socket(file = "/tmp/aaa", mode = 0o600, backlog = _DEFAULT_BACKLOG)
    sock.close()
    if os.path.exists("/tmp/aaa"):
        os.remove("/tmp/aaa")


# Generated at 2022-06-14 12:38:39.750564
# Unit test for function add_accept_handler
def test_add_accept_handler():

    import functools

    import zmq

    from tornado.ioloop import IOLoop

    from tornado.testing import AsyncTestCase, gen_test, bind_unix_socket

    class _BindUnixSocket(AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.test_file = self.get_temp_file()
            self.server_sock = bind_unix_socket(
                self.test_file, mode=0o700, backlog=100
            )
            self.addCleanup(self.server_sock.close)
            self.addCleanup(
                functools.partial(
                    os.remove, self.test_file
                )
            )

        # Callbacks

# Generated at 2022-06-14 12:38:45.987229
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    with pytest.raises(NotImplementedError):
        d = DefaultExecutorResolver()
        result = d.resolve("localhost", 8080, socket.AF_INET)
        assert result == [
            (
                socket.AF_INET,
                ("127.0.0.1", 8080, 0, 0)
            )
        ]



# Generated at 2022-06-14 12:38:54.947929
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, gen_test
    import tornado.web
    import asyncio
    import aiohttp

    class MainHandler(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world ")

    class MainHandler2(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world 2 ")
            print(self.request.host)

    class MainHandler3(tornado.web.RequestHandler):
        async def get(self):
            self.write("Hello, world 3 ")
            print(self.request.host)


# Generated at 2022-06-14 12:38:56.882696
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    ...


# Test class Resolver

# Generated at 2022-06-14 12:39:07.899278
# Unit test for function add_accept_handler
def test_add_accept_handler():
    # add_accept_handler() isn't a function
    # (it's a method of class IOStream), but it looks like one
    # so we can apply the same unit test as for functions.
    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test

    class TestAddAcceptHandler(AsyncTestCase):

        def test_add_accept_handler(self):
            sock, port = bind_unused_port()
            # add_accept_handler doesn't call setblocking(False)
            sock.setblocking(False)
            callback = make_mock_callback(self)
            remove_handler = add_accept_handler(sock, callback)
            self.assertTrue(not remove_handler())
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
           

# Generated at 2022-06-14 12:39:18.929729
# Unit test for function is_valid_ip
def test_is_valid_ip():
    assert is_valid_ip("1.2.3.4")
    assert is_valid_ip("255.255.255.255")
    assert not is_valid_ip("300.2.3.4")
    assert not is_valid_ip("1.2.3")
    assert not is_valid_ip("1.2.3.4.5")
    assert not is_valid_ip("")
    assert not is_valid_ip(".1.2.3.4")
    assert not is_valid_ip("1.2.3.4.")
    assert is_valid_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

# Generated at 2022-06-14 12:39:24.516655
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8888))
    sock.listen(128)
    remove_handler=add_accept_handler(sock, callback=None)
    remove_handler()


# Generated at 2022-06-14 12:39:31.356671
# Unit test for function add_accept_handler
def test_add_accept_handler():
    import _socket
    def callback(connection, address):
        """Callback example"""
        x = connection
        y = address

    io_loop = IOLoop.current()
    io_loop.make_current()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.setblocking(False)
    sock.bind(("", 5432))

    func = add_accept_handler(sock, callback)
    func()



# Generated at 2022-06-14 12:40:23.607670
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = OverrideResolver(resolver=DefaultExecutorResolver(), mapping={})
    resolver.resolve(host="www.google.com", port=443)

# Generated at 2022-06-14 12:40:24.362372
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    pass



# Generated at 2022-06-14 12:40:30.863846
# Unit test for function add_accept_handler
def test_add_accept_handler():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(5)
    port = s.getsockname()[1]
    sock, address = s.accept()
    assert address == ('127.0.0.1', port)


# Generated at 2022-06-14 12:40:36.066751
# Unit test for function bind_sockets
def test_bind_sockets():
    import tornado.httpserver
    import tornado.simple_httpclient
    import tornado.testing
    
    def get_free_ports(host, count):
        ports = set()
        while len(ports) < count:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, 0))
            ports.add(s.getsockname()[1])
            s.close()
        return sorted(ports)

    def test_passive_bind(host, port):
        sockets = bind_sockets(port, host)
        for s in sockets:
            host, actual_port = s.getsockname()[:2]
            assert host == host
            assert actual_port == port

# Generated at 2022-06-14 12:40:38.539951
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    resolver = ExecutorResutor() 
    resolver.close()
    assert resolver.executor == None




# Generated at 2022-06-14 12:40:44.926205
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    import sys
    import logging
    import tornado.ioloop
    import tornado.platform.asyncio
    import asyncio

    logging.basicConfig(level=logging.DEBUG)

    async def test_resolve():
        resolver = DefaultExecutorResolver()
        addr_info = await resolver.resolve('www.google.com', 80)
        print(addr_info)
        resolver.close()
        tornado.ioloop.IOLoop.current().stop()

    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop.run_until_complete(test_resolve())


# Generated at 2022-06-14 12:31:41.406878
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    ls = DefaultExecutorResolver()
    assert isinstance(ls.resolve('www.google.com', 80), Awaitable)



# Generated at 2022-06-14 12:31:53.297502
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    check_logging_options_and_cleanup()
    from tornado import concurrent
    from tornado.netutil import Resolver
    import asyncio
    
    class TestResolver(Resolver):
        def __init__(self, *args, **kwargs):
            self.results = kwargs.pop('results')
            super().__init__(*args, **kwargs)
    
        def resolve(self, host, port, family=socket.AF_UNSPEC):
            future = concurrent.Future()
            future.set_result(self.results)
            return future
    
    io_loop = IOLoop.current()
    address = "http://www.yahoo.com"
    resolver = TestResolver(io_loop=io_loop)

# Generated at 2022-06-14 12:32:02.966916
# Unit test for function bind_sockets
def test_bind_sockets():
    port = 8888
    address = "127.0.0.1"
    family = socket.AF_INET
    backlog = 1024
    flags = socket.AI_PASSIVE
    reuse_port = False

    sockets = bind_sockets(port, address, family, backlog, flags, reuse_port)
    s = sockets[0]
    print(s.getsockname())
    print(s.family)
    print(s.type)
    print(s.proto)
    print(s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
    s.close()
# test_bind_sockets()



# Generated at 2022-06-14 12:32:04.999010
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    resolver = Resolver
    resolver.resolve("www.baidu.com", 80)


# Generated at 2022-06-14 12:32:10.615370
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    tornado.netutil.Resolver.configure('tornado.netutil.ExecutorResolver')
    resolver = tornado.netutil.Resolver()
    assert type(resolver) == tornado.netutil.ExecutorResolver
    resolver.close()
    tornado.netutil.Resolver.configure('tornado.netutil.DefaultExecutorResolver')
test_ExecutorResolver_initialize()



# Generated at 2022-06-14 12:32:17.934902
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    executor: Optional[concurrent.futures.Executor] = dummy_executor
    close_executor: bool = True
    res = ExecutorResolver()
    res.initialize(executor, close_executor)
    assert res.io_loop == IOLoop.current()
    assert res.executor == dummy_executor
    assert res.close_executor == True


# Generated at 2022-06-14 12:32:30.078226
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    from tornado.testing import AsyncTestCase, gen_test
    import asyncio
    import functools
    class TestDefaultExecutorResolver(AsyncTestCase):
        def test_DefaultExecutorResolver(self):
            awaitable = DefaultExecutorResolver().resolve('localhost', 8080)
            coroutine = asyncio.coroutine(functools.partial(asyncio.ensure_future, awaitable))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(coroutine())
            #assert awaitable == [(2, ('127.0.0.1', 8080))]
            assert awaitable._state == 'FINISHED'

            with self.assertRaises(NotImplementedError):
                DefaultExecutorResolver().close()

# Generated at 2022-06-14 12:32:31.220273
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    resolver = ExecutorResutor()
    resolver.close()
    pass



# Generated at 2022-06-14 12:32:35.221816
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    resolver = Resolver()
    print(resolver.resolve('google.com', 80)) # DeferFuture(<Future at 0x1fa5c88 state=finished returned list>)


# Generated at 2022-06-14 12:32:46.840671
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    import asyncio
    import socket
    test_map = {
        'a.com': '127.0.0.1',
        ('b.com',80): ('localhost',8080),
        ('c.com',80,socket.AF_INET): ('google.com',80,socket.AF_INET)
    }
    test_web1 = 'http://a.com/'
    test_web2 = 'http://b.com/'
    test_web3 = 'http://c.com/'

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()


# Generated at 2022-06-14 12:33:11.287970
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    port = None
    address = None
    family = socket.AF_UNSPEC
    backlog = _DEFAULT_BACKLOG
    flags = None
    reuse_port = False
    sockets = []
    if address == "":
        address = None
    if not socket.has_ipv6 and family == socket.AF_UNSPEC:
        # Python can be compiled with --disable-ipv6, which causes
        # operations on AF_INET6 sockets to fail, but does not
        # automatically exclude those results from getaddrinfo
        # results.
        # http://bugs.python.org/issue16208
        family = socket.AF_INET
    if flags is None:
        flags = socket.AI_PASSIVE
    bound_port = None
    unique_addresses = set()  # type: set

# Generated at 2022-06-14 12:33:17.271636
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    from concurrent.futures import ThreadPoolExecutor
    from tornado.ioloop import IOLoop
    from tornado import gen
    from netutil import ExecutorResolver
    # Create an executor that we can close
    pool = ThreadPoolExecutor(1)
    # Try the close twist - pass an executor that we don't close
    executor = ExecutorResolver(pool, False)
    executor.io_loop
    loop = IOLoop.current()
    results = []

    @gen.coroutine
    def resolve(address):
        result = yield executor.resolve(address, 80)
        results.append(result)
    loop.run_sync(lambda: resolve("localhost"))
    executor.close()  # explicitly close the executor
    pool.shutdown()  # but we don't shut down the underlying pool



# Generated at 2022-06-14 12:33:24.471486
# Unit test for function is_valid_ip
def test_is_valid_ip():
    assert is_valid_ip("1.2.3.4")
    assert is_valid_ip("123.123.123.123")
    assert is_valid_ip("255.255.255.255")
    assert is_valid_ip("0.0.0.0")
    assert not is_valid_ip("0.0.0.256")
    assert not is_valid_ip("0.0.0.0.0")
    assert is_valid_ip("fe80::1")
    assert not is_valid_ip("fe80::0::1")
    assert is_valid_ip("::1")
    assert is_valid_ip("2001:db8:0:0:1:0:0:1")
    assert is_valid_ip("2001:41d0:2:a141::1")
   

# Generated at 2022-06-14 12:33:36.107735
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)

    connections = []
    addresses = []

    def handle_connection(connection, address):
        connections.append(connection)
        addresses.append(address)
        connection.close()

    remove_handler = add_accept_handler(sock, handle_connection)

    cond_var = threading.Condition()
    client = None

    def connect_to_server():
        nonlocal client
        loop = IOLoop()

# Generated at 2022-06-14 12:33:40.946495
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    context = ssl_options_to_context({'ssl_version': 2, 'ca_certs': 'ca_certs', 'keyfile': 'keyfile', 'keyfie': 'keyfie', 'close_executor': 'close_executor', 'cert_reqs': 5, 'ciphers': 'ciphers'})
    # TODO check value context.
    pass

# Generated at 2022-06-14 12:33:43.795820
# Unit test for function bind_sockets
def test_bind_sockets():
    sockets = bind_sockets(8888, address="")
    assert type(sockets) == list
    assert type(sockets[0]) == socket.socket
# End of test_bind_sockets


# Generated at 2022-06-14 12:33:44.450549
# Unit test for function add_accept_handler
def test_add_accept_handler():
    pass



# Generated at 2022-06-14 12:33:53.181956
# Unit test for function add_accept_handler
def test_add_accept_handler():
    ioloop=IOLoop.current()
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8888))
    sock.listen(2)
    def callback(connection,address):
        print(connection,address)
        remove_handler()
    remove_handler=add_accept_handler(sock,callback)
    ioloop.start()
    return
#test_add_accept_handler()

# Generated at 2022-06-14 12:33:56.694400
# Unit test for function is_valid_ip
def test_is_valid_ip():
	assert is_valid_ip("localhost") == False
	assert is_valid_ip("127.0.1.1")
	assert is_valid_ip("") == False
	assert is_valid_ip("http://example.com") == False

# Generated at 2022-06-14 12:34:03.720419
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    # mock 
    mapping = {
            "example.com": "127.0.1.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443)
        }
    resolver = mock.mock(Resolver)
    resolver.resolve.side_effect = lambda host, port, family: host
    resolver.close.side_effect = lambda: None

    overrideResolver = OverrideResolver(resolver, mapping)
    overrideResolver.resolve('www.example.com', 443, socket.AF_INET6)
    assert overrideResolver.resolve('www.example.com', 443, socket.AF_INET6) == "::1"

# Generated at 2022-06-14 12:34:25.978064
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))
    sock.listen(5)
    port = sock.getsockname()[1]

    client_fd, addr = sock.accept()
    assert isinstance(addr, tuple)
    assert addr[0] == "127.0.0.1"
    assert addr[1] == port
    assert isinstance(client_fd, socket.socket)


# Generated at 2022-06-14 12:34:30.336216
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    my_dummy_executor = dummy_executor
    resolver_instance = ExecutorResolver()
    resolver_instance.initialize(executor=my_dummy_executor)
    resolver_instance.close()
    assert resolver_instance.executor == None
    assert resolver_instance.close_executor == False

# Generated at 2022-06-14 12:34:43.609573
# Unit test for function bind_sockets
def test_bind_sockets():
    import unittest
    def check_bind(port, address, expected_port):
        sockets = bind_sockets(port, address, flags=socket.AI_NUMERICHOST)
        self.assertEqual(len(sockets), 1)
        s = sockets[0]
        self.assertEqual(s.getsockname()[1], expected_port)
        s.close()
        sockets = bind_sockets(port, address, family=socket.AF_INET)
        self.assertEqual(len(sockets), 1)
        s = sockets[0]
        self.assertEqual(s.getsockname()[1], expected_port)
        s.close()
        sockets = bind_sockets(port, address, family=socket.AF_INET6)

# Generated at 2022-06-14 12:34:52.352681
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    cfg = '''
    resolver:
      mapping:
        login.example.com:9090: localhost:8080
    '''
    app_name = 'test_OverrideResolver_resolve'
    with app_config(cfg, app_name):
        default_resolver = config(app_name).resolver.get_resolver()
        mapping = {("login.example.com", 9090): ("localhost", 8080)}
        resolver = OverrideResolver(default_resolver, mapping)
        loop = IOLoop.current()
        f = resolver.resolve("login.example.com", 9090)
        result = loop.run_until_complete(f)
        assert result == [(socket.AF_INET, ("localhost", 8080))]
        resolver.close()



# Generated at 2022-06-14 12:34:53.881957
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
        res = ExecutorResolver()
        assert res != None



# Generated at 2022-06-14 12:34:59.249865
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    import ssl
    ssl_options = {
        "keyfile": "certs/demo.key",
        "certfile": "certs/demo.crt",
        "cert_reqs": ssl.CERT_REQUIRED,
        "ca_certs": "certs/ca.crt",
        "ssl_version": ssl.PROTOCOL_SSLv23,
        "ciphers": "ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP:+eNULL",
    }

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 0))
    client_socket = ssl_

# Generated at 2022-06-14 12:35:06.510640
# Unit test for function bind_sockets
def test_bind_sockets():
    # bind_sockets((80, '127.0.0.1', None, True))
    print(bind_sockets(80, '127.0.0.1', family=socket.AF_INET, backlog=_DEFAULT_BACKLOG, reuse_port=True))
    # bind_sockets(([80, 443], '127.0.0.1', None, True))
    print(bind_sockets([80, 443], '127.0.0.1', family=socket.AF_INET, backlog=_DEFAULT_BACKLOG, reuse_port=True))
    print(bind_sockets('8080,8081,8082', '127.0.0.1', family=socket.AF_INET, backlog=_DEFAULT_BACKLOG, reuse_port=True))

# Generated at 2022-06-14 12:35:12.275475
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    # Test the method initialize of class ExecutorResolver
    obj = ExecutorResolver()
    executor = None
    close_executor = True
    obj.initialize(executor, close_executor)
    executor = dummy_executor
    close_executor = False
    obj.initialize(executor, close_executor)


# Generated at 2022-06-14 12:35:22.232708
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.bind(("localhost", 0))
    sock.listen(64)
    port = sock.getsockname()[1]
    closed = False
    def accept_handler(sock, address):
        sock.send(b"OK")
        sock.close()
        nonlocal closed
        closed = True
    remove_handler = add_accept_handler(sock, accept_handler)

    def client_run():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        client.connect(("localhost", port))
        client.recv(2)
        client.close()
    thread = Thread(target=client_run)
    thread

# Generated at 2022-06-14 12:35:28.342900
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    import tornado
    import ssl
    ssl_options = {
        'ssl_version': ssl.PROTOCOL_SSLv3,
        'certfile': "tests/test.crt",
        'keyfile': "tests/test.key",
        'cert_reqs': ssl.CERT_NONE,
        'ca_certs': "tests/ca-certs.crt",
        'ciphers': "ALL,!SSLv2"
    }
    c = tornado.netutil.ssl_options_to_context(ssl_options)
    assert c.protocol == ssl.PROTOCOL_SSLv3
    assert c.get_cert_chain_file() == "tests/test.crt"
    assert c.get_privatekey_file() == "tests/test.key"


# Generated at 2022-06-14 12:36:07.160532
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    pass

# Generated at 2022-06-14 12:36:18.541937
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    from concurrent.futures import Executor
    from weakref import WeakSet
    import time

    class _FakeExecutor(Executor):
        def __init__(self):
            super().__init__()
            self._shutdown = False
            self._shutdown_lock = threading.Lock()
            self._shutdown_threads = WeakSet()

        def shutdown(self, wait=True):
            self._shutdown_lock.acquire()
            try:
                self._shutdown = True
            finally:
                self._shutdown_lock.release()
            if wait:
                self.join()

        def submit(self, fn, *args, **kwargs):
            if self._shutdown:
                raise RuntimeError("cannot schedule new futures after shutdown")

            f = concurrent.futures.Future()


# Generated at 2022-06-14 12:36:26.284071
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    # Test class of method close of class ExecutorResolver
    # Input:
    #     self: a ExecutorResolver object
    class TestExecutorResolver(ExecutorResolver):
        def __init__(self):
            super().__init__()
            self.close_executor = True
    resolver = TestExecutorResolver()
    resolver.close()
    if resolver.executor == None:
        print("Pass")
    else:
        print("Fail")



# Generated at 2022-06-14 12:36:32.213626
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    fake_context = ssl_options_to_context({"ssl_version": ssl.PROTOCOL_TLSv1})
    assert isinstance(fake_context, ssl.SSLContext)

    with pytest.raises(AssertionError):
        ssl_options_to_context({"fake_key": "fake_value"})



# Generated at 2022-06-14 12:36:38.901179
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    """Tests close method of class ExecutorResolver."""
    from concurrent.futures import ThreadPoolExecutor
    import os
    import sys
    from tornado.platform.asyncio import AsyncIOMainLoop

    if not hasattr(sys, "_called_from_test") or sys._called_from_test == False:
        pytest.skip("Use `pytest --runxfail` to run the failed tests")

    # Below codes are to prevent issue of "AttributeError: module 'tornado.platform.asyncio' has no attribute '_selector'"
    #  Ref: https://github.com/tornadoweb/tornado/issues/2455

# Generated at 2022-06-14 12:36:40.839271
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    assert bind_unix_socket("test_unix_socket")



# Generated at 2022-06-14 12:36:45.283434
# Unit test for function bind_sockets
def test_bind_sockets():
    sockets = bind_sockets(port=None, address=None)
    print(sockets)
    sockets = bind_sockets(port=80, address="localhost")
    print(sockets)

# test_bind_sockets()



# Generated at 2022-06-14 12:36:48.886710
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    print('testing method initialize of class ExecutorResolver...')
    R = ExecutorResolver()
    R.initialize()
    assert R.io_loop == IOLoop.current() and R.executor == dummy_executor and R.close_executor == False

# Generated at 2022-06-14 12:36:53.474058
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import to_asyncio_future
    AsyncIOMainLoop().install()
    import asyncio
    loop = asyncio.get_event_loop()
    h = Resolver()
    x = h.resolve('www.google.com', '80')
    print(type(x))
    x.add_done_callback(lambda f: print(f.result()))
    loop.run_forever()



# Generated at 2022-06-14 12:37:04.234237
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    import asyncio
    resolver = OverrideResolver()
    mapping = {"example.com": "127.0.1.1", ("login.example.com", 443): ("localhost",
               1443), ("login.example.com", 443, socket.AF_INET6): ("::1",
               1443), ("login.example.com", 80): ("localhost", 1043)}
    resolver.initialize(resolver, mapping)
    host = "login.example.com"
    port = 443
    family = socket.AF_INET6
    asyncio.get_event_loop().run_until_complete(resolver.resolve(host, port, family))
    assert True



# Generated at 2022-06-14 12:37:39.842185
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    F = bind_unix_socket
    assert F

### context manager
_assert_hostname = ssl.match_hostname


# Generated at 2022-06-14 12:37:43.139051
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    assert isinstance(ssl_options_to_context({}), ssl.SSLContext)
    assert ssl_options_to_context({}).verify_mode == ssl.CERT_NONE



# Generated at 2022-06-14 12:37:50.674057
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    # Unit test for method initialize of class ExecutorResolver
    executor = dummy_executor
    close_executor = True
    test=ExecutorResolver()
    test.initialize(executor,close_executor)
    assert hasattr(test,'io_loop')
    assert hasattr(test,'executor')
    assert hasattr(test,'close_executor')
    assert test.io_loop is IOLoop.current()
    assert test.executor is executor
    assert test.close_executor is True



# Generated at 2022-06-14 12:37:56.078523
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    resolver = DefaultExecutorResolver()
    async def aio_call(host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC):
        return await resolver.resolve(host, port, family)
    results = IOLoop.current().run_sync(aio_call, "baidu.com", 80)
    print(results)



# Generated at 2022-06-14 12:37:57.055661
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    resolver = ExecutorResolver()
    assert(resolver.resolve('localhost', 80))


# Generated at 2022-06-14 12:38:09.074276
# Unit test for function bind_sockets
def test_bind_sockets():
    sockets = bind_sockets(8080)
    assert len(sockets) == 1
    assert sockets[0].family == socket.AF_INET
    sockets[0].close()

    sockets = bind_sockets(8080, "localhost")
    assert len(sockets) == 1
    assert sockets[0].family == socket.AF_INET
    sockets[0].close()

    sockets = bind_sockets(8080, "")
    assert len(sockets) == 2
    sockets[0].close()
    sockets[1].close()

    sockets = bind_sockets(8080, "", family=socket.AF_INET)
    assert len(sockets) == 1
    assert sockets[0].family == socket.AF_INET
    sockets[0].close()


# Generated at 2022-06-14 12:38:13.238313
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    socket_ = socket.socket()
    kwargs = {'server_hostname':'cuiqingcai.com', 'do_handshake_on_connect':True}
    ssl_options = {
        "cert_reqs": ssl.CERT_NONE,
        "check_hostname": False,
    }
    print(ssl_wrap_socket(socket_, ssl_options, **kwargs))
    print(ssl_options)

# test_ssl_wrap_socket()

# We set this as a default for the simple_httpclient, but it can also be
# configured for the curl_httpclient
MaxTotalConnections = 50  # type: int

# We set this as a default for the simple_httpclient, but it can also be
# configured for the curl_httpclient
MaxHostConnections

# Generated at 2022-06-14 12:38:18.295807
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    import pdb
    pdb.set_trace()
    # test case #1
    resolver = ExecutorResolver()
    print(resolver.resolve('baidu.com', 80))
    # test case #2
    resolver = ExecutorResolver()
    print(resolver.resolve('baidu.com', 443))



# Generated at 2022-06-14 12:38:30.255163
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock, client = socket.socketpair()
    io_loop = IOLoop.instance()
    remove_handler = add_accept_handler(sock, lambda conn, addr: io_loop.stop())
    io_loop.start()
    assert client.recv(1) == b""  # connection closed
    client.close()
    sock.close()
    remove_handler()
    assert io_loop._handlers == {}
    assert io_loop._events == {}
    # Check that calling accept with no pending connections
    # doesn't result in an error
    sock, client = socket.socketpair()
    remove_handler = add_accept_handler(sock, lambda conn, addr: io_loop.stop())
    io_loop.add_timeout(time.time(), io_loop.stop)
    io_loop.start()
   

# Generated at 2022-06-14 12:38:41.670759
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    resolver = DefaultExecutorResolver()
    result = resolver.resolve('www.baidu.com', 80)
    assert result is not None
    print(result)

test_DefaultExecutorResolver_resolve()



# Generated at 2022-06-14 12:39:17.553438
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    # Set value of host and port to test method resolve
    host = 'localhost'
    port = 1234
    family = socket.AF_INET
    results = DefaultExecutorResolver().resolve(host, port, family)
    while True:
        try:
            # sleep for 0.5 seconds
            time.sleep(0.5)
            # If result is not empty, continue
            if results.done():
                if(results.result()):
                    print("Test pass")
                    break
                else:
                    print("Test fail")
                    break
        except Exception as exception:
            print("Got exception as %s" % exception)
            break 



# Generated at 2022-06-14 12:39:28.198263
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    loop = TornadoLoop()
    d = DefaultExecutorResolver()
    r = loop.run_until_complete(d.resolve('localhost',8000))
    for fam, addr in r:
        print(fam,addr)
    r2 = loop.run_until_complete(d.resolve('www.baidu.com',443))
    for fam, addr in r2:
        print(fam,addr)
    r3 = loop.run_until_complete(d.resolve('tencent.com',443))
    for fam, addr in r3:
        print(fam,addr)
    loop.close()

test_DefaultExecutorResolver_resolve()


# Generated at 2022-06-14 12:39:30.032827
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    resolver = ExecutorResutor()
    resolver.close()
    assert resolver.executor is None


# Generated at 2022-06-14 12:39:30.719551
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    pass

# Generated at 2022-06-14 12:39:40.580601
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    import tornado
    import tornado.netutil
    import tornado.simple_httpclient
    import tornado.locks
    import tornado.queues
    import socket
    import asyncio
    import tornado.platform.asyncio
    async def test_Resolver_resolve_coro():
        # Unit test for method resolve of class Resolver
        my_Resolver = Resolver()
        my_host = "www.google.com"
        my_port = 80
        # my_family= socket.AF_UNSPEC
        # print(locals())
        my_result = await my_Resolver.resolve(
            my_host, my_port
        )  # type: List[Tuple[int, Any]]
        return my_result

    my_loop = asyncio.get_event_loop()
    my_result = my_loop

# Generated at 2022-06-14 12:39:47.419295
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    @run_on_executor
    def resolve(
        host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
    ) -> List[Tuple[int, Any]]:
        return _resolve_addr(host, port, family)
    host = '127.0.0.1'
    port = '80'
    family = socket.AF_INET
    resolve(host,port,family)
# test_ExecutorResolver_resolve()


# Generated at 2022-06-14 12:39:54.602733
# Unit test for function add_accept_handler
def test_add_accept_handler():
    def func(connection: socket.socket, address: Any):
        pass
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 9876))
    sock.listen(0)
    remove_handler = add_accept_handler(sock, func)
    remove_handler()
    IOLoop.current().stop()
    assert not IOLoop.current().impl.handlers


# Generated at 2022-06-14 12:39:58.536017
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    host = "www.baidu.com"
    port = 80
    rs = _resolve_addr(host, port)
    print(rs)
test_ExecutorResolver_resolve()


# Generated at 2022-06-14 12:39:59.437871
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    pass



# Generated at 2022-06-14 12:40:03.975216
# Unit test for function add_accept_handler
def test_add_accept_handler():
    def test_callback(connection, address):
        print(connection, address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7777))
    sock.listen(5)
    remove_handler = add_accept_handler(sock, test_callback)



# Generated at 2022-06-14 12:40:32.432939
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    executor = ExecutorResolver.initialize()
    dummy_executor = ExecutorResolver.initialize()
    executor == dummy_executor
test_ExecutorResolver_initialize()

# Generated at 2022-06-14 12:40:39.174140
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    import concurrent.futures
    import socket
    import pytest
    resolver = ExecutorResolver(
        executor=concurrent.futures.ThreadPoolExecutor(),
        close_executor=False)
    assert await resolver.resolve("www.google.com", 80) == [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET, ('127.0.0.2', 80))
    ]




# Generated at 2022-06-14 12:31:39.080246
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    import unittest
    import ssl
    import os
    class TestSSLWrapSocket(unittest.TestCase):
        def test_ssl_wrap_socket(self):
            test_args = {
                "ssl_options": "ssl_context",
                "server_hostname": "google.com",
                "do_handshake_on_connect": True,
                "suppress_ragged_eofs": True,
                "ciphers": "ALL"
            }
            certfile_path = os.path.join(os.path.dirname(__file__), 'test.crt')
            keyfile_path = os.path.join(os.path.dirname(__file__), 'test.key')
            myssl = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# Generated at 2022-06-14 12:31:47.608772
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    host = "www.google.com"
    port = 80
    class MockResolver(Resolver):
        def resolve(
            self, host, port, family=socket.AF_UNSPEC,
        ):
            # try:
            #     test_addr = socket.getaddrinfo(host, port, family, socket.SOCK_STREAM, socket.SOL_TCP)
            # except Exception as e:
            #     return e
            # return test_addr
            return socket.getaddrinfo(host, port, family, socket.SOCK_STREAM, socket.SOL_TCP)
    resolver = MockResolver()
    test_resolve = resolver.resolve(host, port)
    print(test_resolve)


# method: add_accept_handler
# Added an `.IOLoop` event

# Generated at 2022-06-14 12:31:50.764596
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    class DummyExecutor:
        def shutdown(self):
            pass
    exec_resolver = ExecutorResolver()
    exec_resolver.initialize(DummyExecutor(), True)
    exec_resolver.close()


# Generated at 2022-06-14 12:31:53.564390
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    o = OverrideResolver(resolver= None, mapping={})
    assert o.resolve(host="host", port=80, family=socket.AF_INET)

# Generated at 2022-06-14 12:31:58.917239
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    class TestSSLContext(object) :
        ssl_version = "v1.1"
        certfile="None.crt"
        keyfile="None.key"
        cert_reqs=ssl.VERIFY_NONE
        ca_certs="None_CA.crt"
        ciphers="ALL"

    ssl_options_to_context(TestSSLContext())

# Generated at 2022-06-14 12:32:04.619960
# Unit test for function bind_sockets
def test_bind_sockets():
    with open("test.txt", 'w') as f:
        for _ in bind_sockets(port=8888):
            f.write("Hello World")
    with open("test.txt", 'r') as f:
        content = f.read()
    print(content)

#test_bind_sockets()



# Generated at 2022-06-14 12:32:15.381116
# Unit test for function is_valid_ip
def test_is_valid_ip():
    assert is_valid_ip('127.0.0.1') == True
    assert is_valid_ip('127.0.0.0') == True
    assert is_valid_ip('0.0.0.0') == True
    assert is_valid_ip(':') == False
    assert is_valid_ip('::1') == True
    assert is_valid_ip('::') == True
    assert is_valid_ip('1:2:3:4:5:6:7:8') == True
    assert is_valid_ip('1:2:3:4:5:6:7:0') == True
    assert is_valid_ip('1:2:3:4:5:6:0:8') == True

# Generated at 2022-06-14 12:32:16.978590
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    return bind_unix_socket('/tmp/net_util')


# Generated at 2022-06-14 12:32:19.925831
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    #resolver = ExecutorResolver()
    print(str(os.getpid())+"testing "+inspect.stack()[0][3])
    result = 1
    #assert result == 1


# Generated at 2022-06-14 12:32:27.760622
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    url = "http://127.0.0.1:8888/add_event_loop?name=loop1&policy=default"
    response = requests.get(url)
    unit_test_utils.assert_status_code(response)
    unit_test_utils.assert_in_text(response, '"status": 200')
    body = response.json()

    url = "http://127.0.0.1:8888/add_executor?name=executor1&policy=default"
    data = {'event_loop_name': body['event_loop_name'],}
    response = requests.post(url, data=data)
    unit_test_utils.assert_status_code(response)
    unit_test_utils.assert_in_text(response, '"status": 200')


# Generated at 2022-06-14 12:32:54.292037
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    # class Resolver:
    #     @classmethod
    #     def configurable_base(cls) -> Type[Resolver]:
    #         return Resolver
    #     @classmethod
    #     def configurable_default(cls) -> Type[Resolver]:
    #         return DefaultExecutorResolver
    #     def resolve(self, host: str, port: int, family=socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
    #         raise NotImplementedError()
    #     def close(self) -> None:
    #         pass
    #
    pass



# Generated at 2022-06-14 12:33:03.188692
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = Resolver
    mapping = dict()
    host = "localhost"
    port = 12
    family = socket.AF_INET
    def initialize(self, resolver, mapping):
        self.resolver = resolver
        self.mapping = mapping

    if (host, port, family) in mapping:
        host, port = self.mapping[host, port, family]
    elif (host, port) in mapping:
        host, port = self.mapping[(host, port)]
    elif host in mapping:
        host = mapping[host]
    self.resolver.resolve(host, port, family)



# Generated at 2022-06-14 12:33:07.519911
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
    loop = IOLoop()
    resolver = DefaultExecutorResolver(io_loop=loop)
    result = loop.run_until_complete(resolver.resolve("www.google.com", 80))
    assert result[0][0] == socket.AF_INET

if hasattr(IOLoop, "run_in_executor") and not config.get(
    "tornado_py37_asyncio_compatibility", False
):
    Resolver.configure("tornado.netutil.DefaultExecutorResolver")

# Generated at 2022-06-14 12:33:12.435963
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    import sys
    import ssl
    from tornado.util import ssl_options_to_context
    from unittest import mock

    def check_ssl_options_to_context(ssl_options: dict, **kwargs: Any) -> None:
        context = ssl_options_to_context(ssl_options)
        for key, value in kwargs.items():
            assert getattr(context, key) == value

    def mock_wrap_socket(**kwargs: Any) -> ssl.SSLContext:
        context = ssl_options_to_context(kwargs)
        context.wrap_socket = mock.MagicMock(name=kwargs)
        return context


# Generated at 2022-06-14 12:33:14.153244
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    c = ExecutorResolver()
    assert c.close_executor == True
    assert c.executor != None
    assert c.io_loop != None


# Generated at 2022-06-14 12:33:16.420643
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    eRes1 = ExecutorResolver(io_loop=IOLoop.current())
    eRes1.close()

if __name__ == "__main__":
    test_ExecutorResolver_close()



# Generated at 2022-06-14 12:33:23.139162
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        addr = sock.getsockname()
        wrapped = ssl_wrap_socket(sock, dict(ssl_version=ssl.PROTOCOL_TLSv1))
        assert isinstance(wrapped, ssl.SSLSocket)
        wrapped.close()



# Generated at 2022-06-14 12:33:24.074062
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    _resolve_addr("server.example.com", 80)



# Generated at 2022-06-14 12:33:25.766585
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    from concurrent.futures import Executor
    executor_resolver = ExecutorResolver()
    assert executor_resolver.close_executor == True


# Generated at 2022-06-14 12:33:37.328084
# Unit test for function add_accept_handler
def test_add_accept_handler():
    import unittest
    import tornado.ioloop
    import threading
    import time
    import errno
    import ssl
    import socket
    import os.path

    def test_sock():
        if os.path.exists(os.path.abspath('tests/test_netutil_data/unix_socket_test')):
            os.remove(os.path.abspath('tests/test_netutil_data/unix_socket_test'))
        server_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
        server_sock.bind(os.path.abspath('tests/test_netutil_data/unix_socket_test'))
        server_sock.listen(1)
        return server_sock


# Generated at 2022-06-14 12:33:54.814851
# Unit test for function bind_unix_socket
def test_bind_unix_socket():
    sock = bind_unix_socket('/tmp/logs.sock')
    assert sock
    sock.close()
    import os
    os.remove('/tmp/logs.sock')



# Generated at 2022-06-14 12:33:56.517108
# Unit test for function add_accept_handler
def test_add_accept_handler():
    def test_accept_handler(connection, address):
        pass
    remove_handler = add_accept_handler(socket.socket(), test_accept_handler)
    remove_handler()
    assert True  # to make pyflakes happy



# Generated at 2022-06-14 12:34:07.442363
# Unit test for function add_accept_handler
def test_add_accept_handler():
    """Unit test for `add_accept_handler`"""
    from tornado.testing import gen_test

    execute_add_accept_handler_called = False

    @gen_test
    async def execute_add_accept_handler():
        execute_add_accept_handler_called = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sock.bind(("127.0.0.1", 0))
        sock.listen(128)

        def accept_handler(conn, addr):
            pass

        remove_handler = add_accept_handler(sock, accept_handler)
        assert callable(remove_handler)
        remove_handler()

    await execute_add_accept_handler()
    assert execute_add_accept_handler_called



# Generated at 2022-06-14 12:34:09.777290
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    context = ssl_options_to_context({"ssl_version": ssl.PROTOCOL_TLSv1})

# Generated at 2022-06-14 12:34:20.124189
# Unit test for function add_accept_handler
def test_add_accept_handler():
    callback = lambda x, y: None
    io_loop = IOLoop.current()
    sock = socket.socket()
    sock.bind(("localhost", 0))
    sock.listen(1)
    port = sock.getsockname()[1]
    remove_handler = add_accept_handler(sock, callback)
    connection = socket.create_connection(("127.0.0.1", port))
    io_loop.run_sync(lambda: None)
    assert connection.recv(0) == b""
    remove_handler()
    io_loop.close()



# Generated at 2022-06-14 12:34:30.856885
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = Resolver()
    mapping = dict()
    # test empty dict
    overrideResolver = OverrideResolver(resolver, mapping)
    # test normal
    mapping["login.example.com"] = ("localhost", 1443)
    mapping[("login.example.com", 443)] = ("localhost", 1443)  
    mapping[("login.example.com", 443, socket.AF_INET6)] = ("::1", 1443)
    overrideResolver = OverrideResolver(resolver, mapping)
    host1 = "login.example.com"
    host2 = "example.com"
    port1 = 443
    port2 = 80

# Generated at 2022-06-14 12:34:33.874457
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    r = ExecutorResolver()
    r.close()
    # Test that the function call doesn't throw an error



# Generated at 2022-06-14 12:34:40.676008
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    class MockResolver:
        address: str

        async def resolve(
            self, host: str, port: int,
            family: socket.AddressFamily = socket.AF_UNSPEC,
        ) -> List[Tuple[int, Any]]:
            self.address = host
            if host == 'host1':
                return [('host', 'port')]
            else:
                print(host)
                return [('host', 'port')]

    resolver = MockResolver()
    overrides = {
        "example.com": "127.0.1.1",
        ("login.example.com", 443): ("localhost", 1443),
        ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
    }

# Generated at 2022-06-14 12:34:45.482608
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    r = OverrideResolver()
    ioloop = IOLoop()
    ioloop.make_current()
    async def test():
        result = await r.resolve('test.test', 80, 0)
        assert result == [], "test failed"
    ioloop.run_sync(test, timeout=10)
test_OverrideResolver_resolve()


# Generated at 2022-06-14 12:34:53.315369
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    import tornado.test.util as test_util
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase

    test_util.skip_if_no_ipv6()

    class TestResolver(Resolver):
        EXAMPLE_COM_IPV4 = [
            ('example.com', 80), ('example.com', 1234), ('example.com', 443)
        ]
        EXAMPLE_COM_IPV6 = [
            ('example.com', 80), ('example.com', 1234), ('example.com', 443)
        ]

        async def resolve(self, host, port, family=socket.AF_UNSPEC):
            if (host, port) == ('example.com', 80):
                return self.EXAMPLE_COM_IPV4

# Generated at 2022-06-14 12:35:25.568113
# Unit test for function bind_sockets
def test_bind_sockets():
    sockets = bind_sockets(0, address=None, backlog=None, reuse_port=True)
    for i in range(len(sockets)):
        sockets[i].close()



# Generated at 2022-06-14 12:35:34.690259
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock = socket.socket()
    sock.bind(("localhost", 0))
    sock.listen(5)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    client.connect(("localhost", sock.getsockname()[1]))
    client.send("hello")

    called = [False]

    def callback(conn: socket.socket, addr: str) -> None:
        data = conn.recv(5)
        assert data == b"hello"
        called[0] = True

    add_accept_handler(sock, callback)()
    IOLoop.current().start()
    assert called[0]



# Generated at 2022-06-14 12:35:37.473478
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize(): 
    r = ExecutorResolver()
    assert r.close_executor == True
    assert r.executor == dummy_executor
    assert r.io_loop == IOLoop.current()


# Generated at 2022-06-14 12:35:45.436423
# Unit test for function add_accept_handler
def test_add_accept_handler():
    import socket
    import tornado.platform.asyncio
    import asyncio
    # You need to import tornado.platform.asyncio before asyncio
    # if you want tornado to be initialized at first.
    asyncio.set_event_loop_policy(tornado.platform.asyncio.AnyThreadEventLoopPolicy())
    loop=asyncio.get_event_loop()
    loop.run_until_complete(add_accept_handler_test(loop))
    loop.close()

async def add_accept_handler_test(loop):
    sock=socket.socket()
    sock.bind(('127.0.0.1',0))
    sock.listen(0)
    port=sock.getsockname()[1]
    def callback(connection,address):
        print(port)

# Generated at 2022-06-14 12:35:57.188955
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    # OverrideResolver.resolve(host, port, family)
    #   if host, port, family in self.mapping:
    #       host, port = self.mapping[(host, port, family)]
    #   elif host, port in self.mapping:
    #       host, port = self.mapping[(host, port)]
    #   elif host in self.mapping:
    #       host = self.mapping[host]
    #   return self.resolver.resolve(host, port, family)

    # Generate the resolver for test
    overrideResolver = OverrideResolver()
    resolver = Resolver()
    overrideResolver.resolver = resolver

    # Testing case 1: host is in self.mapping

# Generated at 2022-06-14 12:36:01.355371
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = Resolver()
    mapping = {('login.example.com', 443): ('localhost', 1443)}
    r = OverrideResolver(resolver, mapping)
    assert r.resolve("login.example.com", 443)



# Generated at 2022-06-14 12:36:06.867220
# Unit test for function bind_sockets
def test_bind_sockets():
    socks = bind_sockets(8088)
    for sock in socks:
        print(sock)
        sock.close()
# test_bind_sockets()

_socket_options = [
    (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1),
    (socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),
]



# Generated at 2022-06-14 12:36:14.349483
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    # after "Configurable" and "Configurable.configure"
    class A(Configurable):
        def __init__(self, name, number):
            self.name = name
            self.number = number

        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return A

        @classmethod
        def configurable_type(cls):
            return "a"

        def __repr__(self):
            return "%s(%r, %r)" % (self.__class__.__name__, self.name, self.number)

        def method(self):
            return self.name + str(self.number)

    a = A('a', 1)
    assert(a.method() == 'a1')



# Generated at 2022-06-14 12:36:15.128407
# Unit test for method initialize of class ExecutorResolver
def test_ExecutorResolver_initialize():
    f = ExecutorResolver().initialize()
    assert f != None

# Generated at 2022-06-14 12:36:17.041515
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    # self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
    pass

# Generated at 2022-06-14 12:36:51.268707
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    def fake_resolve(host, port, family):
        return host, port, family
    executor = Mock()
    executor.submit = Mock(return_value=host)
    resolver = ExecutorResolver(executor=executor)
    resolver.resolve('localhost', 80)
    assert resolver.io_loop is IOLoop.current()
    executor.submit.assert_called_once_with(
        fake_resolve, 'localhost', 80, socket.AF_UNSPEC)
    assert executor is resolver.executor
    assert resolver.close_executor is True
    resolver.close()
    executor.shutdown.assert_called_once_with()
    assert resolver.executor is None

test_ExecutorResolver_resolve()

# Generated at 2022-06-14 12:37:02.547947
# Unit test for function ssl_wrap_socket
def test_ssl_wrap_socket():
    ssl_wrap_socket(1,1)

if hasattr(ssl, "match_hostname") and hasattr(ssl, "CertificateError"):

    def ssl_match_hostname(cert: Union[ssl.SSLSocket, ssl.Certificate], hostname: str):
        """Verify that *cert* (in decoded format as returned by
        ``SSLSocket.getpeercert()``) matches the *hostname*.  RFC 2818
        rules (and IDNA encoding) are used.  CertificateError is raised
        on failure. On success, the function returns nothing.
        """
        return ssl.match_hostname(cert, hostname)

# Generated at 2022-06-14 12:37:09.057270
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    # test the resolve method of the Resolver class.
    host = "127.0.0.1"
    port = 123
    family = "A"
    resolver = tornado.netutil.Resolver()
    try:
        resolver.resolve(host, port, family)
    except NotImplementedError as e:
        print(e)
    assert resolver.self == resolver



# Generated at 2022-06-14 12:37:11.231377
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    resolver = ExecutorResutor()
    resolver.close()



# Generated at 2022-06-14 12:37:22.770832
# Unit test for function bind_sockets
def test_bind_sockets():
    from ..testing import bind_unused_port

    def test_tcp_sockets(family, port, backlog, reuse_port=False):
        print("specify port", port)
        sockets = bind_sockets(
            port=port,
            address="localhost",
            family=family,
            backlog=backlog,
            reuse_port=reuse_port,
        )
        print("sockets:", sockets)
        assert len(sockets) == 1

        if sys.platform != "cygwin":
            # Cygwin doesn't support SO_REUSEPORT, and Python
            # doesn't check for that case and just throws an
            # error in getsockopt.
            assert sockets[0].getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == reuse_port

       

# Generated at 2022-06-14 12:37:26.708793
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    import tornado
    async def async_example():
        resolver = tornado.netutil.DefaultExecutorResolver()
        result = await resolver.resolve(host='', port=80, family=socket.AF_INET6)
        print(result)
    asyncio.run(async_example())

# Generated at 2022-06-14 12:37:33.880388
# Unit test for function is_valid_ip
def test_is_valid_ip():
    assert is_valid_ip("0.0.0.0") == True
    assert is_valid_ip("127.0.0.1") == True
    assert is_valid_ip("255.255.255.255") == True
    assert is_valid_ip("256.256.256.256") == False
    assert is_valid_ip("1.2.3.4.5") == False
    assert is_valid_ip("12345") == False
    assert is_valid_ip("") == False
    assert is_valid_ip("google.com") == False
    assert is_valid_ip("localhost") == False
    assert is_valid_ip("127.0.0.1.google.com") == False
    assert is_valid_ip("::1") == True

# Generated at 2022-06-14 12:37:34.679562
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    obj = Resolver()
    obj.close()
    pass



# Generated at 2022-06-14 12:37:42.417562
# Unit test for method resolve of class ExecutorResolver
def test_ExecutorResolver_resolve():
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.platform.asyncio import AsyncIOEventLoop
    import asyncio
    loop = AsyncIOEventLoop()
    faces = loop.create_task(ExecutorResolver().resolve("localhost", 8080))
    print("faces: ",faces)
    asyncio.ensure_future(faces)
    loop.run_forever()
    
try:
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    ThreadPoolExecutor = None



# Generated at 2022-06-14 12:37:44.620716
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    with pytest.raises(NotImplementedError):
        ExecutorResolver().close()

# Generated at 2022-06-14 12:38:40.486266
# Unit test for function ssl_options_to_context

# Generated at 2022-06-14 12:38:42.683169
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    '''
    This is a test case for the method close in class ExecutorResolver
    '''
    er = ExecutorResolver()
    er.initialize()
    er.close()



# Generated at 2022-06-14 12:38:53.234173
# Unit test for function add_accept_handler
def test_add_accept_handler():
    from tornado import ioloop
    import socket
    import time
    port = 8888
    address = ("127.0.0.1", port)
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setblocking(False)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(address)
    server_sock.listen(128)

    def on_connect(connection, address):
        print("Connected", connection, address)

    io_loop = ioloop.IOLoop.current()
    io_loop.add_callback(add_accept_handler, server_sock, on_connect)
    io_loop.start()

# Generated at 2022-06-14 12:39:03.640344
# Unit test for function ssl_options_to_context
def test_ssl_options_to_context():
    ssl_options = {
        'ssl_version': ssl.PROTOCOL_TLSv1,
        'certfile': '../cert/server.crt',
        'keyfile': '../cert/server.key',
        'cert_reqs': ssl.CERT_NONE,
        'ca_certs': '../cert/ca.crt',
        'ciphers': None,
    }
    context = ssl_options_to_context(ssl_options)
    print(context)
# test_ssl_options_to_context()

# Generated at 2022-06-14 12:39:07.636826
# Unit test for method resolve of class Resolver
def test_Resolver_resolve():
    import asyncio
    host = 'localhost'
    port = '80'
    async def test_resolve():
        addr_info = await DefaultExecutorResolver().resolve(host, 80)
        assert addr_info
    asyncio.run(test_resolve())


# Generated at 2022-06-14 12:39:13.675815
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    resolver = OverrideResolver(resolver = ThreadedResolver(), mapping = { ("login.example.com", 443, socket.AF_INET6): ("127.0.1.1", 1443) })
    assert '127.0.1.1' in resolver.resolve('login.example.com', 443, socket.AF_INET6)



# Generated at 2022-06-14 12:39:15.403090
# Unit test for method close of class ExecutorResolver
def test_ExecutorResolver_close():
    '''
    Unit test for method close of class ExecutorResolver.
    '''
    er = ExecutorResolver()
    er.close()
    assert er.executor is None
    assert er.close_executor is False



# Generated at 2022-06-14 12:39:17.355933
# Unit test for method resolve of class DefaultExecutorResolver
def test_DefaultExecutorResolver_resolve():
	resolver = DefaultExecutorResolver()
	asyncio.run(resolver.resolve("localhost",8888))


# Generated at 2022-06-14 12:39:20.672758
# Unit test for function add_accept_handler
def test_add_accept_handler():
    sock = socket.socket()
    def callback(connection, address):
        print("Connected", connection)
        print("Address", address)
    print(add_accept_handler(sock, callback))
        #TODO: How do we test this?
    #  accept_handler(sock, None)


# Generated at 2022-06-14 12:39:32.148927
# Unit test for method resolve of class OverrideResolver
def test_OverrideResolver_resolve():
    def io_loop(self):
        return self.IOLoop.current()

    class resolver(object):
        def __init__(self):
            pass
        
        async def resolve(self, *arg, **kwargs):
            return []

    class mapping():
        def __init__(self):
            pass

        def __contains__(self, key):
            return True

        def __getitem__(self, key):
            return [0, 0]

    reso = resolver()
    mapin = mapping()
    reso1 = OverrideResolver()
    reso1.resolver = reso
    reso1.mapping = mapin
    reso1.io_loop = io_loop
    reso1.IOLoop = IOLoop
    reso1.resolve('', 0)
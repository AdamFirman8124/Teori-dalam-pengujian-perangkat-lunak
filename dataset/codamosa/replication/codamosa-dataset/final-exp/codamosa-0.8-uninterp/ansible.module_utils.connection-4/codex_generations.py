

# Generated at 2022-06-13 00:09:55.087163
# Unit test for function recv_data
def test_recv_data():
    # Test that recv_data returns expected data
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(b'/tmp/test_socket')

    data = b'hello'
    send_data(s, data)
    assert(data == recv_data(s))

    data = b''
    send_data(s, data)
    assert(data == recv_data(s))

    data = b'1234567890'
    send_data(s, data)
    assert(data == recv_data(s))

    data = b'abcdefghijklmnopqrstuvwxyz'
    send_data(s, data)
    assert(data == recv_data(s))


# Generated at 2022-06-13 00:10:00.888182
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    # First test case
    # Create Connection instance
    conn = Connection(
        socket_path="./ansible_connection.sock"
    )

    # Create instance variables
    conn._exec_jsonrpc = Connection._exec_jsonrpc
    conn._exec_jsonrpc.return_value = {
        "result": "result of rpc method test_method_name",
        "jsonrpc": "2.0",
        "id": "f60ac2f7-e566-4768-8e90-21c9a9a9d4a4"
    }

    # Execute method __rpc__
    res = conn.__rpc__(name="test_method_name")

    # Check results
    assert(res == "result of rpc method test_method_name")

    # Second test

# Generated at 2022-06-13 00:10:04.155411
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    """Tests for Connection class and its method __rpc__"""
    from ansible.module_utils.connection import exec_command
    module_mock = type('MockModule', (), {'_socket_path': '/tmp/some_socket_path'})
    command = "some_command"
    result = exec_command(module_mock, command)
    print(result)

# Generated at 2022-06-13 00:10:13.758102
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(b"/tmp/unix-test.sock")
    s.listen(0)
    def recv_thread():
        sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sf.connect(b"/tmp/unix-test.sock")
        send_data(sf, b'1234')
        send_data(sf, b'1234')
        sf.close()
    import threading
    t = threading.Thread(target=recv_thread)
    t.start()
    (sf, addr) = s.accept()
    assert recv_data(sf) == b'1234'

# Generated at 2022-06-13 00:10:21.195715
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    connection = Connection('/tmp/foo')
    connection.send = lambda x: json.dumps({'id': '1234', 'result': x})
    output = connection._exec_jsonrpc('some_method', 'arg1', arg2='value2')
    assert output['id'] == '1234'
    assert output['result']['method'] == 'some_method'
    assert output['result']['jsonrpc'] == '2.0'



# Generated at 2022-06-13 00:10:24.252495
# Unit test for function exec_command
def test_exec_command():
    assert exec_command(None, 'mock_command') == (0, 'mock_command\n', '')

# Generated at 2022-06-13 00:10:34.229900
# Unit test for function recv_data
def test_recv_data():
    # Bind to a temporary socket we control
    # We do this so we can use a tempfile instead of a socket.
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind('/tmp/_unittest_ansible')
    s.listen(1)

    # Connect to the socket we bound to
    s2 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s2.connect('/tmp/_unittest_ansible')

    # Accept the incoming connection
    sc, sa = s.accept()

    # Send test data
    send_data(sc, b'test')

    # Receive the test data
    assert recv_data(s2) == b'test'

    # Send data with a specific length
    send_data

# Generated at 2022-06-13 00:10:47.224009
# Unit test for method send of class Connection
def test_Connection_send():
    # Create a new connection object
    obj = Connection("/tmp/anstest")

    # Get data to send over connection
    data = "some test data"

    # Create a mock socket
    class fake_socket(object):
        def __init__(self):
            self.type = None
            self.family = None
            self.proto = None
            self.fileno = None
            self.timeout = None
            self.close = None
            self.connect = None
            self.recv = None
            self.send = None
            self.sendall = None
            self.shutdown = None

        def socket(self, *args, **kwargs):
            if args == (socket.AF_UNIX, socket.SOCK_STREAM):
                self.return_value = "FakeSocket"
            else:
                self

# Generated at 2022-06-13 00:10:47.818802
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    pass

# Generated at 2022-06-13 00:10:55.266933
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class obj(object):
        pass
    module = obj()
    module.socket_path = 'test_socket_path'
    connection = Connection(module.socket_path)
    connection.send = lambda x: '{"jsonrpc": "2.0", "result": "", "id": "5d3c8102-7b41-4a1f-b3f3-2e9bd4d48f4a"}'
    assert connection.exec_command('net_get_version') == ''


# Generated at 2022-06-13 00:11:02.701714
# Unit test for function recv_data
def test_recv_data():
    b_data = b'\x00\x00\x00\x00\x00\x00\x00\x04' + b'data'
    e_data = b'data'

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('/tmp/ansible_test_sock')

    # sock.sendall(b_data)
    send_data(sock, b_data)
    data = recv_data(sock)
    assert data == e_data

# Generated at 2022-06-13 00:11:09.577572
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    socket_path = '/path/to/socket.json'
    conn = Connection(socket_path)
    assert conn.socket_path == socket_path

    class mock_response:
        def __init__(self, id, result):
            self.id = id
            self.result = result

    req_id = str(uuid.uuid4())
    mock_json = json.dumps({'jsonrpc': '2.0', 'method': 'rpc_method', 'id': req_id,
                           'params': (args, kwargs)}, cls=AnsibleJSONEncoder)

    mock_response = json.loads(mock_json)
    mock_response['id'] = req_id
    mock_response['result'] = 'Success'
    mock_response['result_type'] = 'type'

# Generated at 2022-06-13 00:11:20.368814
# Unit test for function recv_data
def test_recv_data():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect(("127.0.0.1", port))
    s2, addr = s.accept()
    # Smoke test
    data = to_bytes("foo")
    send_data(s1, data)
    assert data == recv_data(s2)
    s1.close()
    s2.close()
    s.close()

# Generated at 2022-06-13 00:11:20.912629
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    pass

# Generated at 2022-06-13 00:11:29.504049
# Unit test for function recv_data
def test_recv_data():
    # Prepare a server socket
    ss = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sname = "/tmp/tcp-socket-rpc-test-{0}".format(uuid.uuid4())

# Generated at 2022-06-13 00:11:40.289891
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    # Defining the mock class
    class MockNetworkModule():
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.params['host'] = 'host1'
            self.params['destination'] = 'host2'
            self.params['username'] = 'user1'
            self.params['password'] = 'test'
            self.params['port'] = 22
            self.params['timeout'] = 10
            self.params['provider'] = None
            self.params['use_ssl'] = True
            self.params['authorized_key_file'] = '/var/home/.ssh/id_rsa'
            self.params['private_key_file'] = '/var/home/.ssh/id_rsa'
            self.params['ssh_strict'] = False

       

# Generated at 2022-06-13 00:11:46.173571
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    con = Connection("test")
    val = con._exec_jsonrpc("test", "foo", "bar")
    assert type(val) is dict
    assert "what_am_i" in val["result"]
    assert val["result"]["what_am_i"] == "foo"
    assert val["result"]["and"] == "bar"

# Generated at 2022-06-13 00:11:57.087610
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    """Unit test for rpc method inside Connection with parametrized requests.
    This unit test can use either the mock_connection provided by the
    test/units/modules/utils.py module or Ansible's connection plugin
    implementation.

    The test will run the rpc method of the connection plugin with below
    parameters:

    * single positional argument
    * multiple positional arguments
    * single keyword argument
    * multiple keyword arguments
    * positional and keyword arguments

    The test will raise an error if the rpc method returns a non-zero status code.
    """
    ansible_connection_module = 'ansible_connection.connection'
    # The test plugins are located at tests/units/module_utils/network/ansible_connection/
    # so we need to add it to the module search path in order to load ansible_connection
    module_utils_path

# Generated at 2022-06-13 00:12:00.550204
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    conn = Connection('/tmp/socket')
    conn._exec_jsonrpc = lambda x: {"result": None}
    result = conn.__rpc__('exec_command', 'show version')
    assert result is None



# Generated at 2022-06-13 00:12:12.322288
# Unit test for function recv_data
def test_recv_data():
    # No data to begin with
    data = to_bytes("")
    header_len = 8

    # Socket with no data
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    assert recv_data(s) is None
    s.close()

    # Socket with partial data
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    out = struct.pack('!LLLL', 0, 1, 2, 3)
    s.sendall(out[:header_len - 1])
    assert recv_data(s) is None
    s.close()
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Socket with partial data and then some

# Generated at 2022-06-13 00:12:27.944756
# Unit test for method send of class Connection
def test_Connection_send():
    """ Verify that Connection.send correctly handles errors encountered
        while sending data to the remote peer via a socket connection.
    """
    # Create a Connection object and mock the socket file
    conn = Connection(socket_path="")
    conn.socket_path = "/tmp/ansible_test"
    conn.sf = mock.MagicMock()

    # Verify that socket error is raised when the socket is not connected
    conn.sf.sendall = mock.MagicMock(side_effect=socket.error)
    with pytest.raises(ConnectionError):
        conn.send(mock.MagicMock())
    conn.sf.sendall.assert_called_once()

    # Verify that socket error is raised when the socket is closed
    conn.sf.sendall = mock.MagicMock(side_effect=socket.error)

# Generated at 2022-06-13 00:12:39.304261
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind('test.socket')
    s.listen(1)
    (test_sock, test_addr) = s.accept()

    test_sock.sendall(struct.pack('!Q', 1))
    test_sock.sendall(b'a')
    test_sock.sendall(struct.pack('!Q', 3))
    test_sock.sendall(b'foo')
    test_sock.sendall(struct.pack('!Q', 0))

    data = recv_data(test_sock)
    assert data == b'a'
    data = recv_data(test_sock)
    assert data == b'foo'

# Generated at 2022-06-13 00:12:43.952978
# Unit test for function recv_data
def test_recv_data():
    for i in range(0, 10):
        assert recv_data(None) is None
        assert recv_data(1) is None
        assert recv_data(socket.socket(socket.AF_INET)) is None
        assert recv_data(socket.socket(socket.AF_INET6)) is None
        assert recv_data(socket.socket(socket.AF_UNIX)) is None
        assert recv_data(socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)) is None

# Generated at 2022-06-13 00:12:56.173491
# Unit test for method send of class Connection
def test_Connection_send():
    # Testing sending data over unix socket
    try:
        sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socket_path = "/tmp/connection_send.sock"
        sf.bind(socket_path)
        sf.listen(1)

        connection = Connection(socket_path)
        connection.send("test_message")

        # Accept connection
        (conn, addr) = sf.accept()
        received_data = to_text(recv_data(conn))
        assert received_data == "test_message"
        conn.close()

    except socket.error as e:
        sf.close()
        traceback.print_exc()
        assert False
    finally:
        sf.close()
        os.remove(socket_path)

   

# Generated at 2022-06-13 00:12:59.061686
# Unit test for function exec_command
def test_exec_command():
    module = object()
    module._socket_path = '/tmp/debug'

    with open('/tmp/debug') as f:
        exec_command(module, f.read())

# Generated at 2022-06-13 00:13:05.278034
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))

    send_data(s, b'hello world')
    assert recv_data(s) == b'hello world'

    send_data(s, b'bye')
    assert recv_data(s) == b'bye'

    s.close()

# Generated at 2022-06-13 00:13:10.518627
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    sock_path = ''
    c = Connection(sock_path)
    setattr(c, '_exec_jsonrpc', lambda *args, **kwargs: {'result': None, 'id': '0'})
    assert c.__rpc__('module_exec_arg') == None


# Generated at 2022-06-13 00:13:21.952664
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class MyConnection(Connection):
        def send(self, data):
            if 'expando' in data:
                return '{"id": "unittest", "result": {"expando": 0}, "jsonrpc": "2.0"}'
            return '{"id": "unittest", "result": false, "jsonrpc": "2.0"}'
    c = MyConnection(None)
    assert c.expando() == {'expando': 0}
    assert c.expando(1) == {'expando': 0}
    assert c.expando(expando=2) == {'expando': 0}
    assert c.expando(1, 2) == {'expando': 0}
    assert c.expando(1, 2, expando=3) == {'expando': 0}
    assert c

# Generated at 2022-06-13 00:13:28.584826
# Unit test for function exec_command
def test_exec_command():
    from ansible.plugins.connection.network_cli import Connection as network_cli
    from ansible.module_utils.connection import Connection, ConnectionError

    module = None
    # this is how Mocking works in ansible
    # monkey patching
    Connection._Connection.exec_command = lambda self, command: "hostname"

    # this works in 2.3 and 2.4+, in 2.5+, will be
    # Connection._Connection.__init__ = lambda self, module: None
    # here we just reuse the implementation by network_cli
    Connection._Connection.__init__ = network_cli.__init__

    command = "show version"
    expected_rc = 0
    expected_out = "hostname"
    expected_err = ""
    rc, out, err = exec_command(module, command)

    assert rc == expected_

# Generated at 2022-06-13 00:13:33.697768
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind('\0test_recv_data')
    s.listen(1)

    conn, addr = s.accept()

    send_data(conn, b'test')
    data = recv_data(conn)

    assert data == b'test'

# Generated at 2022-06-13 00:13:55.385872
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 0))
    s.listen(1)
    worker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker.connect(("0.0.0.0", s.getsockname()[1]))
    worker_data = worker.recv(1024)
    test_data = recv_data(s.accept()[0])
    assert worker_data == test_data

# Generated at 2022-06-13 00:13:59.051493
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    connection = Connection(None)
    try:
        connection._exec_jsonrpc('command', 'show version')
        assert False
    except ConnectionError:
        assert True
    else:
        assert False



# Generated at 2022-06-13 00:13:59.992377
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    pass



# Generated at 2022-06-13 00:14:08.026939
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class _Connection(Connection):
        def _exec_jsonrpc(self, name, *args, **kwargs):
            self.exec_jsonrpc = '{0}({1}, {2})'.format(name, args, kwargs)
            return dict(result='OK', id=1)

    fixture = {'socket_path': ''}
    cnx = _Connection(**fixture)
    expected_exec_jsonrpc = 'cmd(args, {foo=bar})'
    cnx.cmd('args', foo='bar')
    assert cnx.exec_jsonrpc == expected_exec_jsonrpc
    assert cnx.cmd == cnx.__getattr__('cmd')

# Generated at 2022-06-13 00:14:13.161558
# Unit test for function recv_data
def test_recv_data():
    sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sf.connect('/tmp/ansible.sock')
    data = 'hello'
    send_data(sf, data)
    assert recv_data(sf) == data
    sf.close()

# Generated at 2022-06-13 00:14:21.131701
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    from ansible.plugins.loader import connection_loader

    # Setup plugin and connection
    plugin = connection_loader.get('local')
    conn = Connection(plugin._connection_internal_socket_path)

    # Setup ansible runner for connection
    from ansible.runner.return_data import ReturnData

    runner = plugin._load_runner_plugin()

    # Execute exec_command over connection plugin
    def exec_command(cmd):
        runner.run = lambda _, job_vars, play_context: ReturnData(conn=conn, comm_ok=True, result={'stdout': cmd},
                                                                  runner_ok=True)
        code, out, err = plugin.exec_command(cmd)

        assert code == 0
        assert err == ''
        assert out == cmd

    exec_command('hello')
    exec_command

# Generated at 2022-06-13 00:14:31.131153
# Unit test for function recv_data
def test_recv_data():

    # Test for ValueError as the data may be invalid
    def raise_value_error(*args, **kwargs):
        raise ValueError()

    def test_bad_data():
        sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socket.socket.recv = raise_value_error
        assert None is recv_data(sf)

    def test_good_data():
        sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socket.socket.recv = lambda *args, **kwargs: to_bytes('good_data')
        assert 'good_data' == to_text(recv_data(sf))


    test_bad_data()
    test_good_data()

# Generated at 2022-06-13 00:14:34.886438
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class MockConnection():
        def __init__(self):
            self.conn = Connection('/path/to/socket')
            self.methods = []

        def exec_command(self, command):
            self.methods.append(command)
            return command

    mockConnection = MockConnection()
    assert mockConnection.conn.exec_command('hello') == 'hello'
    assert mockConnection.methods == ['hello']



# Generated at 2022-06-13 00:14:39.485982
# Unit test for method send of class Connection
def test_Connection_send():
    # it should send the string to socket file
    sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sf.bind('/tmp/ansible_test_unix_socket')
    sf.listen(1)

    obj = Connection('/tmp/ansible_test_unix_socket')

    def thread_func():
        (conn, addr) = sf.accept()
        obj.send('sample data')

    thread = Thread(target=thread_func)
    thread.start()
    thread.join()

    (conn, addr) = sf.accept()
    header = conn.recv(8)
    data_len = struct.unpack('!Q', header)[0]
    data = conn.recv(data_len)

    conn.close()
   

# Generated at 2022-06-13 00:14:47.709534
# Unit test for function recv_data
def test_recv_data():
    message = "test"
    data = json.dumps(message)
    packed_len = struct.pack('!Q', len(data))
    sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sf.connect("/tmp/ansible_test")
    sf.sendall(packed_len+to_bytes(data))
    assert message == json.loads(to_text(recv_data(sf), errors='surrogate_or_strict'))
    sf.close()


# Generated at 2022-06-13 00:15:03.488070
# Unit test for function recv_data
def test_recv_data():
    pass

# Generated at 2022-06-13 00:15:07.679403
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    connection = Connection('/var/tmp/random')

    try:
        response = connection.__rpc__('testcase')
    except Exception as e:
        assert isinstance(e, ConnectionError)



# Generated at 2022-06-13 00:15:18.871254
# Unit test for function recv_data
def test_recv_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)
    port = sock.getsockname()[1]
    current_state = {
        'data': None,
        'bytes_received': 0,
        'bytes_sent': 0,
        'server_sock': sock,
        'client_sock': None,
        'client_addr': None,
        'total_bytes': 2000
    }


# Generated at 2022-06-13 00:15:24.725388
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind('./test')
    s.listen(1)
    s.settimeout(5)
    sf, addr = s.accept()
    data = '12345678'
    send_data(sf, data)
    assert recv_data(sf) == data
    sf.close()
    s.close()
    assert recv_data(sf) is None

# Generated at 2022-06-13 00:15:28.320497
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class MockConnection(Connection):
        def _exec_jsonrpc(self, name, *args, **kwargs):
            return {'id': '1', 'result': 'success'}

    connection = MockConnection('socket_path')
    result = connection.__rpc__('test', 'arg1', 'arg2', kwarg1='abc', kwarg2='xyz')
    assert result == 'success', result

# Generated at 2022-06-13 00:15:39.038773
# Unit test for method send of class Connection
def test_Connection_send():
    import shutil
    temp_dir = tempfile.mkdtemp()
    socket_path = os.path.join(temp_dir, 'test')
    with contextlib.closing(socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)) as server:
        server.bind(socket_path)
        server.listen(5)

        connection = Connection(socket_path)
        response = connection.send('{"jsonrpc": "2.0", "method": "hello", "id": "42"}')
        assert response == '{"jsonrpc": "2.0", "result": "world", "id": "42"}'

        shutil.rmtree(temp_dir)

# Generated at 2022-06-13 00:15:43.012308
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class object_:
        def __init__(self, connection):
            self._connection = connection
    module_ = object_(None)
    module_._socket_path = 'test/socket/path'
    connection = Connection(module_._socket_path)
    assert connection._exec_jsonrpc.__name__ == '_exec_jsonrpc'


# Generated at 2022-06-13 00:15:53.686165
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    '''
    Test for method __rpc__ of class Connection
    '''
    test_obj = Connection('ansible-connection')
    method_args = [{'arg': 'value'}, 'another_arg']
    method_kwargs = {'kwarg': 'value'}

    reqid = str(uuid.uuid4())
    req = {'jsonrpc': '2.0', 'method': 'test_method', 'id': reqid}
    req['params'] = (method_args, method_kwargs)
    req_json = json.dumps(req, cls=AnsibleJSONEncoder)

    test_obj.send = lambda x: req_json

    response = test_obj._exec_jsonrpc('test_method', *method_args, **method_kwargs)

# Generated at 2022-06-13 00:16:00.790357
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    import hashlib
    class FakeConnection(Connection):
        def send(self, data):
            return data
    fake_socket_path = '/path/to/socket'
    fake_class = FakeConnection(socket_path=fake_socket_path)
    method = 'my_method'
    jsonrpc_id = str(uuid.uuid4())
    expected = {'jsonrpc': '2.0',
                'method': method,
                'id': jsonrpc_id,
                'params': (['arg1', 'arg2'], {'kwarg1': 'kwarg1_value'})}

# Generated at 2022-06-13 00:16:10.265458
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    sock_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_class_socket_path')


# Generated at 2022-06-13 00:16:48.023016
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    import platform
    import mock
    try:
        import __builtin__ as builtins  # python2
    except ImportError:
        import builtins  # python3

    test_connection = Connection('/tmp/ansible-connection-mock')
    command = 'uname'
    expected_output = 'Linux'

    with mock.patch.dict(os.environ, ANSIBLE_CONNECTION_SOCKET_PATH="/tmp/ansible-connection-mock"):
        with mock.patch.dict(builtins.__dict__, {'open': open}):
            ansible_output = test_connection.exec_command(command)
    assert ansible_output == expected_output, 'test for exec_command() method of class Connection failed!'

# Generated at 2022-06-13 00:16:58.922764
# Unit test for method send of class Connection
def test_Connection_send():
    class MockSocketFile(object):
        def close(self):
            pass

        def recv(self, count):
            return "{\"jsonrpc\":\"2.0\", \"result\":{\"username\":\"admin\", \"password\":\"$1$AYLd/p$1j.cJTMxprx.BPo5JE7Yb.\"}, \"id\":\"9f18c2e3-de5c-4f7e-aada-4c7d4bae2aaf\"}"

        def sendall(self, data):
            pass

        def connect(self, socket_path):
            pass

    class MockSocket(object):
        @staticmethod
        def socket(family, type):
            return MockSocketFile()


# Generated at 2022-06-13 00:17:04.790446
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class TestConnection(Connection):
        def __init__(self, socket_path):
            self.socket_path = socket_path
            self.response = {}

    test_conn = TestConnection("/tmp/test_connection")
    test_conn.response = {"id": "123", "result": "Connection Test"}
    assert test_conn._exec_jsonrpc("test_method") == test_conn.response



# Generated at 2022-06-13 00:17:05.576944
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    result = Connection.__rpc__(None, 'get')
    assert result is None


# Generated at 2022-06-13 00:17:16.477638
# Unit test for function recv_data
def test_recv_data():
    # Create mock socket fd
    sf = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    # Create mock socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    # Bind sock to mock socket
    sock.bind(sf.getsockname())
    # Listen on sock
    sock.listen(1)

    # Connect sf to mock socket
    sf.connect(sock.getsockname())
    conn, addr = sock.accept()

    # Create test data
    data = '{"jsonrpc": "2.0", "id": "5553ac90-68a0-11e7-805d-0050569a7968", "method": "hello"}'

    # Send data
    send_data(conn, data)



# Generated at 2022-06-13 00:17:17.297247
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    connection = Connection('')
    assert connection.__rpc__('exec_command', "ls -l")

# Generated at 2022-06-13 00:17:20.821361
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    """
    Tests __rpc__ method of class Connection
    """
    connection = Connection(os.environ['NET_TEST_SOCKET_PATH'])
    response = connection.__rpc__('get_option', 'host')
    assert response == {u'host': u'localhost'}



# Generated at 2022-06-13 00:17:25.078848
# Unit test for function exec_command
def test_exec_command():
    import sys

    module = AnsibleModule(argument_spec={})

    cmd = "echo hello world"
    code, out, err = exec_command(module, cmd)
    assert code == 0
    assert out.strip() == "hello world"
    assert err == ""

# Generated at 2022-06-13 00:17:31.363659
# Unit test for function recv_data
def test_recv_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        s.setblocking(False)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.connect(('127.0.0.1', s.getsockname()[1]))

            c.sendall(struct.pack('!Q', 5) + b'12345')

            cl, ca = s.accept()
            data = recv_data(cl)

            assert(data == b'12345')

# Generated at 2022-06-13 00:17:37.389076
# Unit test for function recv_data
def test_recv_data():
    import socket
    from ansible.module_utils.ec2 import has_boto3
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection

    module = AnsibleModule(
        argument_spec=dict(
            socket_path=dict(required=True, type='str')
        )
    )

    key = 'ec2_key_id'
    secret = 'ec2_secret_key'

    socket_path = module.params['socket_path']

    # Create a unix domain socket
    infd = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    infd.bind(socket_path)
    infd.listen(1)

# Generated at 2022-06-13 00:18:47.322221
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    conn = Connection(None)
    assert conn._exec_jsonrpc('ping') == {'id': '098b8a53-e883-4c24-a493-7f65367d9947', 'jsonrpc': '2.0',
                                          'result': 'pong', 'error': None}

# Generated at 2022-06-13 00:18:52.784474
# Unit test for function recv_data
def test_recv_data():

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind('\0test')
    sock.listen(1)

    data = os.urandom(1024)
    packed_len = struct.pack('!Q', len(data))

    connect, addr = sock.accept()
    connect.sendall(packed_len + data)

    connect.shutdown(socket.SHUT_RDWR)
    connect.close()
    sock.close()

    assert data == recv_data(connect)


# Generated at 2022-06-13 00:18:55.789798
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    # There are no python unit tests for the connection plugin
    # cPickle errors with py3.5
    pass

# Generated at 2022-06-13 00:19:01.612385
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect('/tmp/ansible_test_socket')
    sockfile = s.makefile('rb', 0)
    sockfile.write(struct.pack('!Q', 8))
    sockfile.write(b'abcdefg')
    sockfile.flush()
    data = recv_data(s)
    s.close()
    assert data == b'abcdefg'

# Generated at 2022-06-13 00:19:06.938174
# Unit test for function recv_data
def test_recv_data():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind('/tmp/test_socket')
    s.listen(1)
    send_s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    send_s.connect('/tmp/test_socket')

    data = os.urandom(1024)
    send_data(send_s, data)

    recv_s, addr = s.accept()

    assert recv_data(recv_s) == data

# Generated at 2022-06-13 00:19:12.413317
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    from tempfile import mkdtemp
    from ansible.module_utils.connection import Connection
    from ansible.module_utils._text import to_bytes, to_text
    module_socket_path = mkdtemp(prefix='ansible_test_socket_')
    connection = Connection(module_socket_path)
    local_version = connection.send(to_bytes(json.dumps({'method': 'local_version'})))
    local_version = json.loads(to_text(local_version))
    if local_version['id'] != 0:
        raise AssertionError('local_version id is not 0')
    if local_version['result']['version'] != -1:
        raise AssertionError('local_version version is not -1')

# Generated at 2022-06-13 00:19:21.101821
# Unit test for function recv_data
def test_recv_data():
    class FakeSocket(object):
        def __init__(self, data):
            self.data = data
            self.reads = 0

        def recv(self, size):
            if size > len(self.data) - self.reads:
                size = len(self.data) - self.reads
            out = self.data[self.reads:self.reads+size]
            if not out:
                return None
            self.reads += size
            return out

    s = FakeSocket(b'1234567890ABCDE')
    assert recv_data(s) == b'1234567890ABCDE'

    s = FakeSocket(b'12345678901234567890ABCDE')
    assert recv_data(s) == b'1234567890ABCDE'
    assert s.reads == 18

    s

# Generated at 2022-06-13 00:19:22.351449
# Unit test for method send of class Connection
def test_Connection_send():
    con = Connection('test')
    assert con.send('test') == 'test'

# Generated at 2022-06-13 00:19:33.183891
# Unit test for method __rpc__ of class Connection
def test_Connection___rpc__():
    class_name = 'Connection'
    method_name = '__rpc__'
    class_inst = Connection('socket_path')

    try:
        class_inst.__getattr__('exec_command')('a')
    except ConnectionError as err:
        if err.code == 1:
            assert(err.err == '{"result": "a"}')
        else:
            assert(False)
    else:
        assert(False)

    try:
        class_inst.__getattr__('exec_command')('a', 'b')
    except ConnectionError as err:
        if err.code == 1:
            assert(err.err == '{"result": "ab"}')
        else:
            assert(False)
    else:
        assert(False)

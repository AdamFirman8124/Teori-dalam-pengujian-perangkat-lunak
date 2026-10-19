

# Generated at 2022-06-12 20:43:32.162964
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    '''
    Unit test for method run of class ConnectionProcess
    '''
    log_messages = True

# Generated at 2022-06-12 20:43:39.750724
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    lock_path = '/tmp/test_ConnectionProcess_shutdown'
    if os.path.exists(lock_path):
        os.remove(lock_path)
    if os.path.exists(lock_path+'_1'):
        os.remove(lock_path+'_1')
    if os.path.exists(lock_path+'_2'):
        os.remove(lock_path+'_2')

    if not os.path.exists(lock_path+'_1'):
        os.mknod(lock_path+'_1')
    if not os.path.exists(lock_path+'_2'):
        os.mknod(lock_path+'_2')
    if not os.path.exists(lock_path):
        os.mkn

# Generated at 2022-06-12 20:43:40.673835
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-12 20:43:43.098568
# Unit test for function main
def test_main():
    sys.stdin = open('tests/unit/lib/ansible_test/_data/control_plane/init.json', 'rb')
    sys.argv = [0, 0, None]
    main()
    assert os.path.exists(unfrackpath(C.PERSISTENT_CONTROL_PATH_DIR))



# Generated at 2022-06-12 20:43:47.022087
# Unit test for function file_lock
def test_file_lock():
    lock_path = 'lockfile'
    lock_fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    fcntl.lockf(lock_fd, fcntl.LOCK_EX)
    with file_lock(lock_path):
        pass

# Generated at 2022-06-12 20:43:50.566504
# Unit test for function read_stream
def test_read_stream():
    try:
        return_value = read_stream(to_bytes(sys.stdin))
        print(return_value)
    except Exception as e:
        print(e)


# Generated at 2022-06-12 20:44:01.475414
# Unit test for function read_stream
def test_read_stream():
    test_data = '''
    # ACCESS_KEY_ID
    AKIAIOSFODNN7EXAMPLE
    # SECRET_ACCESS_KEY
    wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    '''
    r = StringIO()
    data = to_bytes(test_data)
    r.write(to_bytes("{0}\n".format(len(data))))
    r.write(data)
    r.write(to_bytes("{0}\n".format(hashlib.sha1(data).hexdigest())))
    r.seek(0)
    r_data = read_stream(r)
    assert r_data == data



# Generated at 2022-06-12 20:44:12.189019
# Unit test for function main
def test_main():
    # Test with stdin as file object
    stdin = open(os.path.join(os.path.dirname(__file__), os.path.normpath("t/unit/files/connection_process/cp.txt")))
    wfd = open("/tmp/stdout", "w")
    sys.stdin = stdin

# Generated at 2022-06-12 20:44:18.957743
# Unit test for function main
def test_main():
    # Test case: Default
    # Test if 'main' function returns expected value.
    # Arrange
    sys.argv = ['ansible-connection', '12345', 'asd_asd_asd']
    r = StringIO()
    sys.stdout = r
    # Act
    main()
    # Assert
    assert r.getvalue() == '{"messages": [], "socket_path": null}\n'

# Generated at 2022-06-12 20:44:26.164479
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    '''
    test method to test the functionality of the shutdown method of class ConnectionProcess
    '''
    fd = StringIO()
    play_context = PlayContext()
    socket_path = str(os.path.abspath(__file__)).replace('.py', '')
    original_path = os.path.dirname(socket_path)
    task_uuid = hashlib.sha1(os.urandom(64)).hexdigest()
    ansible_playbook_pid = os.getpid()
    conn_proc = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid=task_uuid, ansible_playbook_pid=ansible_playbook_pid)
    conn_proc.shutdown()
    assert os.path.exists(socket_path) != True




# Generated at 2022-06-12 20:44:50.598272
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    pass



# Generated at 2022-06-12 20:45:00.224839
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    fd = StringIO()
    play_context = PlayContext()
    socket_path = '/tmp/cp-test_ConnectionProcess_shutdown'
    task_uuid = None

    os.makedirs('/tmp/cp-test_ConnectionProcess_shutdown_dir')
    with open(socket_path, "w") as test_socket:
        test_socket.write('test-socket')

    cp = ConnectionProcess(fd, play_context, socket_path, '/tmp/cp-test_ConnectionProcess_shutdown_dir',
                           task_uuid=task_uuid)
    cp.sock = os.fdopen(os.open(socket_path, os.O_RDONLY|os.O_NONBLOCK), 'r')
    cp.connection = Connection()


# Generated at 2022-06-12 20:45:09.111674
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
  fd = StringIO()
  play_context = PlayContext()
  play_context.connection = 'network_cli'
  play_context.network_os = 'ios'
  play_context.host = '10.122.1.1'
  play_context.port = 22
  play_context.remote_user = 'user'
  play_context.password = 'pass'
  play_context.become = True
  play_context.become_method = 'enable'
  play_context.become_user = 'privileged_user'
  play_context.become_password = 'privileged_pass'
  play_context.check_mode = True
  play_context.timeout = 10
  play_context.network_debug = False
  play_context.persistent_command_timeout = 60
  play_

# Generated at 2022-06-12 20:45:20.219942
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    log_messages = False
    original_path = '~'
    socket_path = '/tmp/.ansible_pc/tmpQ2O2Yv'
    connection = os.path.join('/tmp/ansible_test_payload', 'mock')
    def __init__(self, fd, play_context, socket_path, original_path, task_uuid=None, ansible_playbook_pid=None):
        pass
    def set_options(variables):
        pass
    def get_option(self, key, default=None):
        if key == 'persistent_log_messages':
            return log_messages
    def pop_messages():
        return []
    def _connect():
        pass
    def handle_request(data):
        return data
    # monkey patch ConnectionProcess class


# Generated at 2022-06-12 20:45:32.772494
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    # Create a ConnectionProcess object
    fd = StringIO()
    play_context = ansible.playbook.play_context.PlayContext()
    socket_path = '/var/tmp/test_socket'
    original_path = '/var/tmp'
    task_uuid = '4ab2c4f8-e00d-44cc-9f9f-7e009f71a81b'
    ansible_playbook_pid = 1234567890
    cp = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

    # Put the object in a with statement
    display.display('called before the connection process is started')
    with cp:
        display.display('called after the connection process is started')

    # This test will only pass if the exception

# Generated at 2022-06-12 20:45:40.651145
# Unit test for function read_stream
def test_read_stream():
    '''
    unit recv_data
    :return:
    '''
    data = b'{"a": "Hello, Ansible"}'
    data_hash = hashlib.sha1(data).hexdigest()
    buffer = to_bytes(str(len(data))) + b"\n" + data + b"\n" + to_bytes(data_hash) + b"\n"
    buffer_stream = StringIO(buffer)
    assert(read_stream(buffer_stream) == data)
    buffer_stream.close()

    data = b'{"a": "Hello, Ansible\r"}'
    data_hash = hashlib.sha1(data).hexdigest()

# Generated at 2022-06-12 20:45:53.841093
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    with open('/var/tmp/ansible/ansible_modlib.copy_f5aa4a01b4d69c60a6b61c6d4b6d4a.pytest_0.tmp', 'rb') as f:
        vars = cPickle.load(f)
    play_context = PlayContext(vars=vars['vars'])
    socket_path = '/var/tmp/ansible/ansible_modlib.copy_f5aa4a01b4d69c60a6b61c6d4b6d4a.pytest_0.socket'
    original_path = '.'
    connproc = ConnectionProcess(sys.stdout, play_context, socket_path, original_path)
    connproc.command_timeout(signal.SIGALRM, None)


# Generated at 2022-06-12 20:46:00.894351
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    """
    Unit test for method connect_timeout of class ConnectionProcess.
    """
    connection_process = ConnectionProcess(None, None, None, None, None)

    import sys
    from types import ModuleType
    from ansible.module_utils.six import with_metaclass

    class moduleType(type):
        def __getattribute__(self, name):
            return object

    class fakeModule(with_metaclass(moduleType, object)):
        _ansible_module_name = "fake"

    fakeModule = fakeModule()
    fakeModule.fail_json = ModuleType('fake_fail_json')
    fakeModule.exit_json = ModuleType('fake_exit_json')
    fakeModule.params = {"path": "fake_path"}

# Generated at 2022-06-12 20:46:08.878419
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    fd = StringIO()
    play_context = PlayContext()
    socket_path = StringIO()
    task_uuid = StringIO()
    original_path = StringIO()
    ansible_playbook_pid = StringIO()
    variables = StringIO()
    cp = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)
    cp.start(variables)
    cp.run()
    cp.shutdown()


# Generated at 2022-06-12 20:46:18.364953
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    """
    unit test for the shutdown method
    """
    fd = open(os.devnull, 'w')
    play_context = PlayContext()
    socket_path = "/tmp/ansible/test/socket"
    original_path = "/tmp/ansible/test"
    cp = ConnectionProcess(fd, play_context, socket_path, original_path)
    cp.connection = MockConnection(host="host1", port="22", user="admin")
    cp.sock = MockSock()
    cp.sock.close = Mock(return_value=None)
    cp.shutdown()
    assert not os.path.exists(socket_path)
    assert cp.connection.close.call_count == 1
    assert cp.sock.close.call_count == 1



# Generated at 2022-06-12 20:46:56.305261
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    """
    Test for the shutdown of ConnectionProcess
    """
    cwd = os.getcwd()
    fd = StringIO()

# Generated at 2022-06-12 20:46:56.963389
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    pass


# Generated at 2022-06-12 20:47:04.027698
# Unit test for function read_stream
def test_read_stream():
    b = StringIO()

    data = to_bytes("some string with \r\n")
    checksum = hashlib.sha1(data).hexdigest()
    data = data.replace(b'\r', br'\r')

    b.write(to_bytes("{0}\n".format(len(data))))
    b.write(data)
    b.write(to_bytes("{0}\n".format(checksum)))
    b.seek(0)

    assert read_stream(b) == to_bytes("some string with \r\n")

# Generated at 2022-06-12 20:47:15.236777
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    fd = "fd"
    play_context = "play_context"
    socket_path = "persistent-connections/ansible_pc/asdf"
    original_path = "original_path"
    task_uuid = "task_uuid"
    ansible_playbook_pid = "ansible_playbook_pid"

    with ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid) as test:
        assert test.fd == fd
        assert test.play_context == play_context
        assert test.socket_path == socket_path
        assert test.original_path == original_path

        assert test.srv != None
        assert test.sock == None
        assert test.connection == None
        assert test.current_command == None

# Generated at 2022-06-12 20:47:21.051287
# Unit test for function main
def test_main():
    try:
        conn_class = connection_loader.get('local')
    except Exception as excep:
        print("Failed to load local connection plugin: %s" % excep)
        return 1

    # Write binary data, in case this is run from python3
    if PY3:
        data = bytes(conn_class.__name__, 'utf-8')
    else:
        data = bytes(conn_class.__name__)

    data = zlib.compress(data)
    data = struct.pack('!Q', len(data)) + data
    sys.stdin.write(data)
    sys.stdin.flush()

    pc = PlayContext()
    pc.connection = 'local'

    # Write binary data, in case this is run from python3
    if PY3:
        pc_data

# Generated at 2022-06-12 20:47:24.708969
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    # Check default behavior
    connection = ConnectionProcess(fd=None, play_context=None, socket_path=None, original_path=None, task_uuid=None, ansible_playbook_pid=None)
    assert connection.shutdown() == True



# Generated at 2022-06-12 20:47:27.922210
# Unit test for function file_lock
def test_file_lock():
    with file_lock("test_file_lock.txt"):
        pass
    os.remove("test_file_lock.txt")


# Generated at 2022-06-12 20:47:38.988503
# Unit test for method run of class ConnectionProcess

# Generated at 2022-06-12 20:47:43.446438
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    # Create a ConnectionProcess object
    cp = ConnectionProcess(None, None, None, None)
    msg = 'persistent connection idle timeout triggered, timeout value is %s secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide.' % cp.connection.get_option('persistent_connect_timeout')
    # run the method and check if it raises exception
    assert cp.command_timeout(None, None) == Exception(msg)

# Generated at 2022-06-12 20:47:48.347663
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    # Create a fake connection object to use with ConnectionProcess.
    class FakeConnection(Connection):
        def __init__(self, play_context, new_stdin, task_uuid=None, prompt=None, ansible_playbook_pid=None):
            super(FakeConnection, self).__init__(play_context, new_stdin, task_uuid=None, prompt=None, ansible_playbook_pid=None)
            self._connected = False
            self._conn_closed = False
            self._socket_path = None
            self._persistent = True

        def connect(self, params, kickstart=True, **kwargs):
            self._connected = True
            return None

        def exec_command(self, cmd):
            return Response(0, b'', b'')


# Generated at 2022-06-12 20:48:10.823032
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    mock_sock = MockSocket()
    mock_sock.return_value = mock_sock

    mock_connection = MockConnection()
    mock_connection.return_value = mock_connection

    cp = ConnectionProcess(object, object, '/tmp/ansible-PC.socket', '/tmp')
    cp.sock = mock_sock
    cp.connection = mock_connection

    cp.shutdown()
    mock_sock.close.assert_called_once()
    mock_connection.close.assert_called_once()



# Generated at 2022-06-12 20:48:20.875310
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    # Create a dummy module to pass to the connection object
    class DummyModule(object):
        def __init__(self):
            self.socket_path = "/junk/path"

    assert PY3
    # Try to connect to an already deleted socket
    socket_path = "/junk/path"
    conn = ConnectionProcess(socket_path)
    conn.run()

    # Send incomplete data
    conn = ConnectionProcess(socket_path)
    data = json.dumps({'method': 'foo', 'params': []})
    conn.sock.sendall(to_bytes(data[:10]))
    conn.run()

    # Send complete data but with a bad json
    conn = ConnectionProcess(socket_path)
    data = json.dumps({'method': 'foo', 'params': []})

# Generated at 2022-06-12 20:48:25.131446
# Unit test for function file_lock
def test_file_lock():
    test_lock_path = '/tmp/test.lock'
    with file_lock(test_lock_path):
        assert os.path.exists(test_lock_path)
    assert not os.path.exists(test_lock_path)



# Generated at 2022-06-12 20:48:31.538942
# Unit test for function read_stream
def test_read_stream():
    test_data = b'{ "test": true }'
    # Escape \r and add a checksum
    stream = StringIO(
        b'{0}\n{1}\n'.format(
            len(test_data),
            hashlib.sha1(test_data.replace(b'\r', br'\r')).hexdigest()
        )
    )
    stream.write(test_data.replace(b'\r', br'\r'))
    stream.seek(0)
    data = read_stream(stream)
    assert data == test_data


# Generated at 2022-06-12 20:48:40.485743
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    debug_messages = []

    class MockSocket(object):
        def close(self):
            debug_messages.append('socket closed')

    class MockOs(object):
        def path(self):
            return self

        def exists(self, path):
            debug_messages.append('checking path %s' % path)
            return True

        def remove(self, path):
            debug_messages.append('removing path %s' % path)

    class MockConnection(object):
        def __init__(self):
            self.debug_messages = []
            self._socket_path = 'path/to/socket'
            self._connected = True

        def pop_messages(self):
            raise Exception('error while popping messages')
            yield

        def close(self):
            self.debug_messages.append

# Generated at 2022-06-12 20:48:46.590713
# Unit test for function file_lock
def test_file_lock():
    with open('/tmp/testlock', 'w+') as lock_file:
        with file_lock('/tmp/testlock'):
            assert lock_file.read() == ''
            lock_file.write('locked')
            lock_file.seek(0)
            assert lock_file.read() == 'locked'



# Generated at 2022-06-12 20:48:53.050577
# Unit test for function file_lock
def test_file_lock():
    def test_lock(lock_path):
        try:
            lock_fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        except:
            raise Exception('File lock cannot be obtained!')
        try:
            fcntl.lockf(lock_fd, fcntl.LOCK_EX)
        except:
            raise Exception('File lock cannot be obtained!')
        try:
            fcntl.lockf(lock_fd, fcntl.LOCK_UN)
        except:
            raise Exception('File lock cannot be released!')
        os.close(lock_fd)


# Generated at 2022-06-12 20:49:01.872972
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    import signal
    import signal
    import traceback
    import time
    import os
    import os
    import socket
    import socket
    import sys
    import sys
    import threading
    import threading
    from mock import Mock
    from mock import patch
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cPickle, StringIO
    from ansible.module_utils.service import fork_process
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader
    from ansible.utils.path import unfrackpath, makedirs_safe
    from ansible.utils.display import Display

# Generated at 2022-06-12 20:49:05.533277
# Unit test for function read_stream
def test_read_stream():
    data = b"1234567890"
    stream = StringIO()
    stream.write(to_bytes(len(data)))
    stream.write(b"\n")
    stream.write(data)
    stream.write(b"\n")
    stream.write(to_bytes(hashlib.sha1(data).hexdigest()))
    stream.write(b"\n")

    stream.seek(0)

    assert read_stream(stream) == data



# Generated at 2022-06-12 20:49:10.098151
# Unit test for function read_stream
def test_read_stream():
    b = "4\r\nthis\n4\r\n4148\ndone\n"

    buf = StringIO(b)
    buf.seek(0)
    assert read_stream(buf) == b'this'

    buf.seek(0)
    assert read_stream(buf) == b'this'


# Generated at 2022-06-12 20:49:55.972960
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    fd = StringIO()
    play_context = PlayContext()
    socket_path = "/foo/bar"
    original_path = "/foo/bar2"
    task_uuid = "foobar"
    connection = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid)
    connection._ansible_playbook_pid = "foo"
    connection.sock = True
    connection.connection = True
    connection.sock.close = lambda: None
    connection.connection.close = lambda: None
    connection.connection.get_option = lambda: True
    connection.connection.pop_messages = lambda: (("foo", "bar"),)

    connection.shutdown()

    assert not hasattr(connection, "_socket_path")
    assert not hasattr(connection, "_connected")


# Generated at 2022-06-12 20:50:00.039626
# Unit test for function file_lock
def test_file_lock():
    # setup
    lock_path = os.path.join(C.DEFAULT_LOCAL_TMP, 'test_file_lock')
    with file_lock(lock_path):
        try:
            with file_lock(lock_path):
                raise Exception("file_lock failed to block")
        except IOError as e:
            if e.errno != errno.EAGAIN:
                raise
    # teardown
    if os.path.exists(lock_path):
        os.unlink(lock_path)



# Generated at 2022-06-12 20:50:00.719911
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    pass

# Generated at 2022-06-12 20:50:09.185757
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    class Fake_connection():
        """ Fake class for ConnectionProcess unit test """
        def __init__(self):
            self._connected = False
            self.e_string = None
        def close(self):
            self._connected = False
        def pop_messages(self):
            for i in range(3):
                yield i, i
        def get_option(self, var):
            return 0
    class Fake_sock():
        """ Fake class for ConnectionProcess unit test """
        def __init__(self):
            self.close_called = False
            self.e_string = None
        def close(self):
            self.close_called = True
    class Fake_socket():
        """ Fake class for ConnectionProcess unit test """
        def __init__(self):
            self.exists_called = False

# Generated at 2022-06-12 20:50:17.119328
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    _ConnectionProcess = getattr(sys.modules[__name__], 'ConnectionProcess')
    _ConnectionProcess('_fd', '_play_context', '_socket_path', '_original_path', '_task_uuid', '_ansible_playbook_pid')
    _ConnectionProcess().shutdown()
    assert False, "Cannot find '%s' in '%s'" % ('shutdown', 'ConnectionProcess')


# Generated at 2022-06-12 20:50:25.794399
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    try:
        fd = StringIO()
        play_context = PlayContext()
        socket_path = '/some/socket/path'
        original_path = '/some/original/path'
        task_uuid = None
        ansible_playbook_pid = None

        connection_process = ConnectionProcess(
            fd,
            play_context,
            socket_path,
            original_path,
            task_uuid,
            ansible_playbook_pid
        )

        connection_process.connect_timeout(signum =1, frame = None)

    except Exception:
        assert True


# Generated at 2022-06-12 20:50:28.776121
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    conn = ConnectionProcess(sys.stdout, PlayContext(), "/tmp/ansible-pc-connect-test", "/tmp")
    conn.command_timeout("SIGALRM", None)


# Generated at 2022-06-12 20:50:40.670872
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    stream = StringIO()
    display = Display()
    display.verbosity = 4

# Generated at 2022-06-12 20:50:47.972805
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    # Create the args used to setup the object.
    # Create the fd used in the object.
    fd = TestFD()
    play_context = TestPlayContext()
    socket_path = "/var/run/ansible-conn/"
    original_path = "/var/run/ansible-conn/original"
    task_uuid = "68f4a922-5e5d-49a8-99a6-f5d7dc1bebe8"
    ansible_playbook_pid = 1234
    # Setup the object.
    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)
    # Check that the socket_path attribute is setup correctly.
    assert connection_process.socket_path == socket_path
    #

# Generated at 2022-06-12 20:50:56.249784
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    '''
    Unit test for ConnectionProcess.run() method
    '''
    options_str = "{\"persistent_command_timeout\": 1, \"persistent_connect_timeout\": 1, \"persistent_log_messages\": true, \"remote_addr\": \"localhost\"}"
    options = json.loads(options_str)

    play_context = PlayContext()
    play_context.connection = options['persistent_connection']
    play_context.network_os = 'ios'
    play_context.remote_addr = options['remote_addr']
    play_context._play_prereqs = True
    play_context.verbosity = 4
    play_context.become = False
    play_context.become_method = 'enable'
    play_context.become_user = 'ansible'
    play_context.private


# Generated at 2022-06-12 20:43:30.664489
# Unit test for function read_stream
def test_read_stream():
    import io
    data = b"hello world!\nhow are you?"
    chk = hashlib.sha1(data).hexdigest()
    #data += b'\n'
    sio = io.BytesIO()
    print(data, len(data), chk)
    sio.write(b'{0}\r\n{1}\r\n'.format(len(data), data, chk))
    sio.seek(0)
    data1 = read_stream(sio)
    print(data1)
    assert data == data1
# test_read_stream()
# raise SystemExit


# Generated at 2022-06-12 20:43:38.731170
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    from tests.unit.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    display = Display()
    connection_loader.add_connection('local', LocalConnection)
    connection = connection_loader.get('local', play_context, '/dev/null')
    connection._socket_path = socket_path
    connection._tqm = TaskQueueManager(inventory=inventory, variable_manager=variable_manager, loader=loader,
                                       options=options, passwords=passwords, stdout_callback=results_callback,
                                       run_tree=False)
    connection

# Generated at 2022-06-12 20:43:47.021876
# Unit test for function read_stream
def test_read_stream():
    test_data = '''100

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
89a8b5d5bb1ccacf54a15c395a8da9bb946e4fef
\n'''
    test_data_real = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n'
    stream = StringIO(test_data)
    data = read_stream(stream)
    assert data == test

# Generated at 2022-06-12 20:43:53.575175
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    display = Display()
    source = "/home/bin/ansible-playbook"
    dest = "/home/ansible/bin/ansible-playbook"
    play_context = PlayContext()
    play_context.become = True
    play_context._play_context = dict()
    play_context._play_context["become"] = True
    play_context._play_context["become_method"] = "sudo"
    play_context._play_context["become_user"] = "root"
    play_context.connection = "local"
    play_context.network_os = "ios"
    play_context.remote_addr = "127.0.0.1"
    play_context.port = 22
    play_context.remote_user = "root"

# Generated at 2022-06-12 20:43:58.130756
# Unit test for function main
def test_main():
    result = Exception('foo')
    msg = 'bar'
    try:
        raise result
    except Exception as e:
        if result != e:
            if getattr(e, 'args', None):
                e.args = (msg,) + e.args
            else:
                e.args = (msg,)
        raise


if __name__ == '__main__':
    main()

# Generated at 2022-06-12 20:44:05.691470
# Unit test for function main
def test_main():
    import sys
    import os
    import tempfile
    import shutil
    import subprocess
    import psutil
    import signal

    def kill_children(p):
        print('killing %s' % p.pid)
        for child in p.children():
            os.kill(child.pid, signal.SIGTERM)
        os.kill(p.pid, signal.SIGTERM)
        p.wait()


    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-12 20:44:17.580030
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    fd, cpath = tempfile.mkstemp()
    os.close(fd)
    args = [cpath, 'path', 'path']
    lock_path = unfrackpath("%s/.ansible_pc_lock_%s" % os.path.split(args[0]))
    os.remove(cpath)
    cp = ConnectionProcess(args[0], args[1], args[2])
    cp.start()
    # Test for when socket.accept fails
    cp.run()
    assert cp._exception is None
    # Test for when sock.accept returns with data
    open(cpath, 'wb').close()
    cp.run()
    assert cp._exception is None
    # Test for when sock.accept returns without data
    cp.run()
    assert cp._exception is None
    #

# Generated at 2022-06-12 20:44:21.184353
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    display = Display()
    class connection:
        def get_option(self, option):
            return 5

    play_context = PlayContext()

    socket_path = "/test/test"
    original_path = "/test/test"

    # Set values of Ansible globals
    setattr(C, 'HOST_KEY_CHECKING', False)

    cp = ConnectionProcess(sys.stdout, play_context, socket_path, original_path, task_uuid=None, ansible_playbook_pid=None)
    cp.connection = connection()
    cp.handler(signal.SIGALRM, None)

# Generated at 2022-06-12 20:44:31.573995
# Unit test for function read_stream
def test_read_stream():
    # This test was written to prove that a sha1 hex check string
    # can be used to validate the integrity of data read from a socket.
    # If you want to replace the sha1 hex check string with the md5 version,
    # then you will also need to update read_stream and write_stream with the
    # following changes.  Otherwise, you will fail the check that verifies
    # the integrity of the data.
    #
    # Replace...
    #   hashlib.sha1(data).hexdigest()
    # With...
    #   hashlib.md5(data).hexdigest()
    stream = StringIO()
    data = "Hello World\n"
    data_hash = hashlib.sha1(data.encode('utf-8')).hexdigest()

# Generated at 2022-06-12 20:44:41.125289
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    hostname = 'testhost'
    display = Display()
    pc = PlayContext()
    socket_path = '/home/bentarzi/git_repo/ansible/test/unit/module_utils/connection_plugins/persistent_control.py'
    original_path = '/home/bentarzi/git_repo/ansible/test/unit/module_utils/connection_plugins/persistent_control.py'
    task_uuid = 12
    pid = 14
    p = ConnectionProcess(pc, socket_path, original_path, task_uuid, pid, hostname)
    p.connect_timeout()

# Generated at 2022-06-12 20:45:20.553154
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    variables = {'ansible_shell_type': 'csh', 'ansible_user': 'vagrant', 'ansible_port': '22', 'ansible_host': '127.0.0.1', 'ansible_network_os': 'ios', 'ansible_connection': 'network_cli'}
    play_context = PlayContext()
    play_context.become=False
    play_context.become_method='disable'
    play_context.become_user='root'
    play_context.remote_addr=None
    play_context.connection='network_cli'
    play_context.check_mode=False
    play_context.diff=False
    play_context.inventory=None
    play_context.only_tags=None
    play_context.skip_tags=None
    play_context.only

# Generated at 2022-06-12 20:45:25.426828
# Unit test for function file_lock
def test_file_lock():
    # Test Context Manager
    with file_lock("/tmp/test.lock"):
        pass
    # Test Object
    obj = file_lock("/tmp/test.lock")
    obj.__enter__()
    obj.__exit__()



# Generated at 2022-06-12 20:45:30.243213
# Unit test for function main
def test_main():
    from ansible.errors import AnsibleConnectionFailure

    try:
        main()
    except AnsibleConnectionFailure as e:
        assert 'unable to decode JSON' in to_text(e)
    except Exception as e:
        assert False, to_text(e)

# Generated at 2022-06-12 20:45:33.318420
# Unit test for function file_lock
def test_file_lock():
    lock_file = 'test_file_lock_lock'
    try:
        with file_lock(lock_file):
            assert not os.path.exists(lock_file)
    finally:
        if os.path.exists(lock_file):
            os.remove(lock_file)



# Generated at 2022-06-12 20:45:44.821331
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    """
    Test if the shutdown method works as expected
    :return:
    """
    fd, fd_path = tempfile.mkstemp()
    os.close(fd)

    ctx = PlayContext()
    ctx._socket_path = 'test/playbook.retry'
    os.makedirs('test')
    open(ctx._socket_path, 'a').close()

    cp = ConnectionProcess(fd_path, ctx, 'test/playbook.retry', 'test')

    cp.shutdown()
    assert not os.path.exists('test/playbook.retry')
    assert not os.path.exists('test/.ansible_pc_lock_test/playbook.retry')
    shutil.rmtree('test')



# Generated at 2022-06-12 20:45:45.482787
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    pass

# Generated at 2022-06-12 20:45:57.594181
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import sys
    import traceback
    from ansible.utils.display import Display
    display = Display()

    fd = None
    self = ConnectionProcess(fd, None, None, None)
    self.fd = sys.stdout
    self.sock = None
    self.connection = None
    self.connection = None
    self.exception = None
    self.play_context = None
    self.socket_path = None
    self.original_path = None
    self.srv = None
    self._task_uuid = None
    if os.path.exists(self.socket_path):
        if self.sock:
            try:
                self.sock.close()
            except Exception:
                pass
        if self.connection:
            self.connection.close()

# Generated at 2022-06-12 20:46:02.565498
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    host = 'localhost'
    original_path = '/Users/prashanth/.ansible/tmp/ansible-tmp-1508356328.27-31551665488875/'
    socket_path = '/Users/prashanth/.ansible/pc/0b2de9ecb5'
    task_uuid = 'e6eb1e03-373b-4808-8d1b-9a7b2396a6d0'
    ansible_playbook_pid = None

    play_context = PlayContext()
    play_context.network_os = 'ios'
    play_context.remote_addr = host
    play_context.remote_port = 22
    play_context.connection = 'network_cli'
    play_context.become = None

# Generated at 2022-06-12 20:46:05.414648
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    pass



# Generated at 2022-06-12 20:46:07.279334
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    fd = StringIO()
    play_context = PlayContext()

# Generated at 2022-06-12 20:46:45.246134
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    pass


# Generated at 2022-06-12 20:46:46.898159
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    cp = ConnectionProcess(None, None, None, None)
    cp.handler(None, None)



# Generated at 2022-06-12 20:46:52.351438
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():

    # Setup mocks and fakes
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(self.socket_path)
    s.listen(1)
    timeout = 10
    s.settimeout(timeout)
    
    try:
        # Testing the method connect_timeout in class ConnectionProcess
        s.accept()

    except socket.timeout:
        print('Timeout')

    finally:
        s.close()

# Generated at 2022-06-12 20:46:53.813814
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    pass

# Generated at 2022-06-12 20:46:55.541299
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    pass



# Generated at 2022-06-12 20:47:04.867757
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    # test with existing socket file.
    with open('./_test_ConnectionProcess_shutdown.sock', 'w'):
        assert os.path.exists('./_test_ConnectionProcess_shutdown.sock')
        with ConnectionProcess(sys.stdout, PlayContext(), './_test_ConnectionProcess_shutdown.sock', './') as cp:
            cp.shutdown()
            assert not os.path.exists('./_test_ConnectionProcess_shutdown.sock')

    # test with no socket file.
    with ConnectionProcess(sys.stdout, PlayContext(), './_test_ConnectionProcess_shutdown.sock', './') as cp:
        cp.shutdown()
        assert not os.path.exists('./_test_ConnectionProcess_shutdown.sock')


# Generated at 2022-06-12 20:47:06.700722
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
   with ConnectionProcess(self):
        self.connection.close()
        self.connection.shutdown()


# Generated at 2022-06-12 20:47:16.967914
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    class _Display:
        def __init__(self):
            self.messages = []

        def display(self, msg, log_only=None, color=None, screen_only=None, stderr=None):
            self.messages.append(msg)

    class _StringIO(StringIO):
        def __init__(self, *args, **kwargs):
            pass

        def getvalue(self):
            return ''

    display = _Display()
    setattr(C, 'display', display)
    setattr(sys, 'stdout', _StringIO())
    variables = {}
    play_context = PlayContext()
    original_path = os.path.abspath('.')
    fd = StringIO()

# Generated at 2022-06-12 20:47:17.847449
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-12 20:47:28.864380
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    try:
        os.remove("/tmp/testfilelocation")
        os.remove("/tmp/testfilelocation.lock")
    except FileNotFoundError:
        pass
    except OSError:
        pass
    makedirs_safe("/tmp", 0o700)
    with open("/tmp/testfilelocation", "w") as f:
        f.write("test")

    play_context = PlayContext()
    conn_proc = ConnectionProcess(fd=sys.stdout,
                                  play_context=play_context,
                                  socket_path="/tmp/testfilelocation",
                                  original_path="/tmp",
                                  task_uuid="1234567890")
    conn_proc.connection = MockConnection(play_context)
    conn_proc.sock = MockSocket()


# Generated at 2022-06-12 20:48:24.961429
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    from mock import patch
    from StringIO import StringIO
    fh_stdout = StringIO()
    with patch('ansible.plugins.connection.persistent.Display.display') as patched_disp:
        patched_disp.return_value = None
        p_cp = ConnectionProcess(fh_stdout, PlayContext(), "/tmp/test_connect_timeout.socket", "/tmp")
        with patch('ansible.plugins.connection.persistent.socket.socket') as patched_socket:
            patched_socket.return_value = get_mocked_socket()
            p_cp.connect_timeout(None, None)

# Generated at 2022-06-12 20:48:34.094155
# Unit test for function main
def test_main():
    import sys
    from ansible.plugins.connection.network_cli import Connection as NetworkCliConnection
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.connection import Connection as CommonConnection
    from ansible_collections.ansible.netcommon.plugins.module_utils.connection.connection import Connection as CommonConnectionNew

    class MockAnsibleModule:
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('AnsibleModule.fail_json: %s' % kwargs['msg'])


# Generated at 2022-06-12 20:48:40.038335
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    class MockConnection:
        connected = False
        _conn_closed = False
        _socket_path = False

        def __init__(self, play_context, new_stdin, task_uuid=None, ansible_playbook_pid=None):
            self.play_context = play_context
            self.new_stdin = new_stdin
            self.task_uuid = task_uuid
            self._ansible_playbook_pid = ansible_playbook_pid

        def get_option(self, option):
            return 'timeout'

        @staticmethod
        def handle_request(data):
            return data

    class MockSocket:
        def __init__(self):
            self.socket_path = 'test_socket_path'


# Generated at 2022-06-12 20:48:49.549598
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    fd = open(os.devnull, "wb")
    play_context = PlayContext()
    socket_path = "/tmp/ansible_control"
    original_path = "/home/user/"
    task_uuid = "a3b3c2d2e1f1a1b1"
    ansible_playbook_pid = "1234"
    C = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)
    assert os.path.exists(socket_path)

    C.shutdown()
    assert not os.path.exists(socket_path)

    C.shutdown()
    assert not os.path.exists(socket_path)



# Generated at 2022-06-12 20:48:50.253212
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    pass



# Generated at 2022-06-12 20:49:00.162793
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    from ansible import constants as C

    C.ANSIBLE_SSH_CONTROL_PATH = '/tmp/ansible-ssh-%%h-%%p-%%r'

    # proxy_socket is a os.pipe() fd which is used to send socket path information over to the parent process
    proxy_socket = os.pipe()

    # child is the child pid which is actually the real ssh connection process
    child = os.fork()

    def start_ssh_connect(play_context, fd, pty):
        context = PlayContext()

        conn = ConnectionProcess(fd, context, '/foo', '/bar', '10')
        conn.start({})
        os._exit(0)


# Generated at 2022-06-12 20:49:01.393043
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    my_ConnectionProcess = ConnectionProcess(1, 1, 1, 1)
    my_ConnectionProcess.shutdown()

# Generated at 2022-06-12 20:49:04.657494
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    """
    Test handler method of ConnectionProcess class
    """
    test_obj = ConnectionProcess(None, None, None, None)
    assert test_obj.handler(12, None) == None


# Generated at 2022-06-12 20:49:13.338644
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():

    # unit test for method start of class ConnectionProcess
    play_context = PlayContext()


    try:
        if sys.version_info < (2, 7):
            import unittest2 as unittest
        else:
            import unittest
    except ImportError:
        print("unittest is missing. pip install unittest2 to run the tests")
        raise
    from ansible.module_utils.six.moves import StringIO

    # create test stubs

    class connection_loader(object):
        def __init__(self):
            pass

        def get(self, *args, **kwargs):
            return connection_loader.get(*args, **kwargs)

    class connection_loader_get(object):
        def __init__(self):
            pass


# Generated at 2022-06-12 20:49:22.898216
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import docstring_to_snippet
    from ansible.executor.process.worker import TaskExecutor
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import action_loader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.utils.color as color

# Generated at 2022-06-12 20:50:29.582439
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    fd = os.open("../test_results/test_result", os.O_RDWR | os.O_CREAT, 0o600)
    play_context = PlayContext()
    socket_path = "/path/to/socket"
    original_path = "/original/path"
    cp = ConnectionProcess(fd, play_context, socket_path, original_path)
    # cp.fd = fd
    cp.fd.write(json.dumps(cp.start({}), cls=AnsibleJSONEncoder))
    cp.fd.close()
    fd = os.open("../test_results/test_result", os.O_RDWR | os.O_CREAT, 0o600)
    assert fd is not None


# Generated at 2022-06-12 20:50:36.321251
# Unit test for function file_lock
def test_file_lock():
    try:
        lock_file = "/tmp/lock_file"
        with file_lock(lock_file):
            assert os.path.exists(lock_file)
        assert not os.path.exists(lock_file)
    finally:
        if os.path.exists(lock_file):
            os.remove(lock_file)



# Generated at 2022-06-12 20:50:40.948729
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid = init_parameters()
    conn = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)
    conn.shutdown()
    assert not os.path.exists(socket_path)


# Generated at 2022-06-12 20:50:42.036793
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-12 20:50:48.834838
# Unit test for function read_stream

# Generated at 2022-06-12 20:51:00.765965
# Unit test for function read_stream

# Generated at 2022-06-12 20:51:08.140921
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    fd = StringIO()
    play_context = PlayContext()
    socket_path = 'test_socket_path'
    original_path = '/home/user'
    task_uuid = 'test_task_uuid'
    ansible_playbook_pid = None
    variables = 'test_variables'
    cp = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)
    cp.run()



# Generated at 2022-06-12 20:51:09.440199
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    pass


# Generated at 2022-06-12 20:51:22.094777
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    # Initialize the class.
    fd = None
    play_context = None
    socket_path = None
    original_path = None
    task_uuid = None
    ansible_playbook_pid = None

    cp = ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

    assert cp is not None
    assert cp.play_context is None
    assert cp.socket_path is None
    assert cp.original_path is None
    assert cp._task_uuid is None
    assert cp.fd is None
    assert cp.exception is None
    assert cp.srv is not None
    assert cp.sock is None
    assert cp.connection is None
    assert cp._ansible_playbook_pid is None

    # Run the start

# Generated at 2022-06-12 20:51:31.829779
# Unit test for function read_stream
def test_read_stream():
    class ReadStream:
        def __init__(self, data):
            self.buf = data
            self.pos = 0
        def read(self, size):
            if self.pos + size > len(self.buf):
                size = len(self.buf) - self.pos
            data = self.buf[self.pos:self.pos+size]
            self.pos += size
            return data
        def readline(self):
            newline_pos = self.buf.find(b'\n', self.pos)
            if newline_pos != -1:
                data = self.buf[self.pos:newline_pos]
                self.pos = newline_pos + 1
            else:
                data = self.buf[self.pos:]
                self.pos = len(self.buf)
            return data

# Generated at 2022-06-12 20:52:56.168337
# Unit test for function main
def test_main():
    this_dir, this_filename = os.path.split(__file__)
    test_data = os.path.join(this_dir, 'test_data', 'jsonrpc_persistence_play_context_vars.json')
    sys.argv = ['jsonrpc_persistence.py']

    with open(test_data, 'r') as f:
        test_data = json.load(f)

    # Set up the test data
    init_data = test_data['init_data']
    vars_data = test_data['vars_data']
    expected_results = test_data['expected_results']
    expected_messages = expected_results['messages']
    expected_rc = expected_results['rc']
    expected_out = expected_results['out']

    # step 1 to 3 of
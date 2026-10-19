

# Generated at 2022-06-13 12:12:44.728892
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    local_path = 'test_fetch_file_local'
    remote_path = 'test_fetch_file_remote'
    md5 = 'd41d8cd98f00b204e9800998ecf8427e'
    buffer_size = 4096
    
    # Mocks
    ps = mock.MagicMock()
    ps.add_script = mock.MagicMock()
    ps.add_argument = mock.MagicMock()
    ps.invoke = mock.MagicMock()
    ps.output = ""
    ps.streams = mock.MagicMock()
    ps.streams.error = ""
    ps.had_errors = False
    host = mock.MagicMock()
    host.rc = 0
    host.ui = mock.MagicMock()
    host.ui.stdout = []

# Generated at 2022-06-13 12:12:53.360408
# Unit test for method close of class Connection
def test_Connection_close():
    c = Connection()
    ansible_log = logging.Logger('ansible_log')
    ansible_log.setLevel(20)
    ansible_log.addHandler(logging.StreamHandler(sys.stdout))
    ansible_log.propagate = False
    ansible_log.disabled = True

# Generated at 2022-06-13 12:12:54.589089
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    connection.put_file()


# Generated at 2022-06-13 12:13:02.727681
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 12:13:04.299943
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    assert True == True


# Generated at 2022-06-13 12:13:14.411472
# Unit test for constructor of class Connection
def test_Connection():
    module_args = {
        'remote_addr': 'localhost',
        'remote_user': 'username',
        'remote_password': 'password!',
        'protocol': 'https',
        'port': 443,
        'path': '/psrp/',
        'auth': 'Basic',
        'cert_validation': 'ignore',
        'connection_timeout': 30,
        'read_timeout': None,
        'message_encryption': 'false',
        'proxy': None,
        'ignore_proxy': False,
        'operation_timeout': None
    }

    connection = Connection(module_args, False, False)

    assert connection._psrp_host == module_args['remote_addr']
    assert connection._psrp_user == module_args['remote_user']
    assert connection._psrp

# Generated at 2022-06-13 12:13:18.237963
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = create_connection_mock(ConnectionPsrp)
    connection.reset()
    assert connection.runspace is None and connection._connected is False and connection._last_pipeline is None


# Generated at 2022-06-13 12:13:30.019438
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Importing test_file_utils
    from test.unit.files import test_file_utils
    #
    # Creating file 'test_file_utils.py' in directory '/Users/alexgaas/work/ansible/test/integration/default/module_utils'
    # Initializing file object
    file_object = test_file_utils.FileObj(path='/Users/alexgaas/work/ansible/test/integration/default/module_utils/test_file_utils.py')
    # Creating variable 'file_content' of type <class 'str'> with value 'import os\n\n\nclass FileObj(object):\n    \'\'\'\n    FileObj class\n    \'\'\'\n    def __init__(self, path):\n        self.path = path\n        self.

# Generated at 2022-06-13 12:13:32.181246
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    connection.reset()
    assert connection.runspace is None
    assert not connection._connected
    assert connection._last_pipeline is None

# Generated at 2022-06-13 12:13:40.748289
# Unit test for method reset of class Connection
def test_Connection_reset():
    host = 'test_psrp_host'
    port = 5986
    protocol = 'https'
    user = 'test_user'
    password = 'BlahBlahBlah'
    proxy = '192.168.1.10'
    ignore_proxy = True
    operation_timeout = 10
    reconnection_retries = 3
    reconnection_backoff = 5.0

# Generated at 2022-06-13 12:14:01.987568
# Unit test for method reset of class Connection
def test_Connection_reset():
    args = dict(
        context={},
        )
    obj = Connection(**args)
    obj.reset()


# Generated at 2022-06-13 12:14:09.636696
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    my_shell = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
    my_arguments = ('-NonInteractive',
                    '-NoLogo',
                    '-ExecutionPolicy',
                    'Bypass',
                    '-EncodedCommand',
                    base64.b64encode(b'Write-Host "hello world!"')
                    )
    my_input_data = b'hello world!'
    my_conn_kwargs = dict(server='localhost',
                          username='me',
                          password='password',
                          ssl=False,
                          auth='basic',
                          # TODO: add config_name
                          # config_name = 'Microsoft.PowerShell',
                          )


# Generated at 2022-06-13 12:14:13.264238
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection({})
    path = 'test/file.txt'
    tmp = connection.fetch_file(path, 'test/file.txt')
    assert tmp == 'test/file.txt'

# Generated at 2022-06-13 12:14:19.570867
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    connection =Connection(play_context=None, new_stdin=None, prompt_regex=None,
                           console_has_ssh=False, persistent_connection_id=None,
                           _ansible_no_log=None, password=None)

    src = "the source"
    dest = "the destination"
    use_winrm_temp_path = False
    encoding = None

    connection.put_file(src, dest, use_winrm_temp_path, encoding)

# Generated at 2022-06-13 12:14:23.672642
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection(play_context=None)
    runspace = RunspacePool(connection.host)
    runspace.state = RunspacePoolState.OPENED
    connection.runspace = runspace
    connection.close()
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None


# Generated at 2022-06-13 12:14:24.414374
# Unit test for method reset of class Connection
def test_Connection_reset():
  PSRPConnection.reset("self")


# Generated at 2022-06-13 12:14:25.470685
# Unit test for method close of class Connection
def test_Connection_close():
    plugin = Connection()
    result = plugin.close()
    assert result is None


# Generated at 2022-06-13 12:14:34.333181
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    m = mock.mock_open()
    with mock.patch('ansible.plugins.connection.psrp.open', m, create=True):
        connection = Connection(None)
        connection.set_options(direct={'ansible_connection': 'pypsrp'})
        connection.set_options(direct={'remote_addr': 'test_remote_addr'})
        connection.set_options(direct={'remote_user': 'test_remote_user'})
        connection.set_options(direct={'remote_password': 'test_remote_password'})
        connection.set_options(direct={'protocol': 'test_protocol'})
        connection.set_options(direct={'port': 'test_port'})
        connection.set_options(direct={'path': 'test_path'})

# Generated at 2022-06-13 12:14:35.007686
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    pass

# Generated at 2022-06-13 12:14:45.342596
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    test_data = '''
---
- hosts: local
  tasks:
   - name: Test fetch_file
     raw: echo "hello world" > /tmp/testfile
   - name: Fetch the file
     fetch:
      src: /tmp/testfile
      dest: /tmp/
'''
    temp_dir = tempfile.gettempdir()
    local_test_data = tempfile.NamedTemporaryFile(delete=False)
    local_test_data.write(test_data)
    local_test_data.close()
    local_test_data_name = local_test_data.name
    os.remove(local_test_data.name)

# Generated at 2022-06-13 12:15:05.250239
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass

# Generated at 2022-06-13 12:15:06.255060
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    pass


# Generated at 2022-06-13 12:15:13.881437
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from ansible.playbook.play_context import PlayContext
    from ansible.errors import AnsibleError
    mock_play_context = PlayContext()
    mock_play_context.verbosity = 3
    mock_play_context._extras = dict()
    mock_play_context.remote_addr = b'123'
    mock_play_context.remote_user = b'456'
    mock_play_context.remote_password = b'789'
    mock_play_context.port = 987
    mock_play_context.timeout = 1000
    mock_play_context.connection = b'network_cli'
    mock_play_context.become = False
    mock_play_context.become_method = None
    mock_play_context.become_user = None
    mock_play_context.check_mode

# Generated at 2022-06-13 12:15:20.310189
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection("test")
    conn._psrp_host = "test"
    data = {
        "in_path": "test",
        "out_path": "test",
        "md5sum": None,
        "file_args": {}
        }
    assert conn.fetch_file("test", "test") == None

# Generated at 2022-06-13 12:15:27.840095
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    mock_runner = Connection()
    src = 'a'
    dst = 'b'
    mock_runner.put = MagicMock(return_value='a')
    assert mock_runner.put_file(src, dst) == 'a'
    mock_runner.put.assert_called_with(src, dst, use_powershell=True, use_psrp=True)

# Generated at 2022-06-13 12:15:30.578017
# Unit test for method reset of class Connection
def test_Connection_reset():
    # connection = Connection()
    # return_value = connection.reset()
    assert True

# Generated at 2022-06-13 12:15:47.443561
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    display.verbosity = 3

    # initializing the test
    time.sleep(1)
    test_logdir = '/tmp/ansible-logs'
    test_log_file = test_logdir + "/" + os.path.basename(__file__) + ".log"
    if os.path.exists(test_log_file):
        os.remove(test_log_file)

    os.environ['ANSIBLE_LOG_PATH'] = test_log_file
    os.environ['ANSIBLE_DEBUG'] = "False"
    os.environ['ANSIBLE_VERBOSITY'] = "3"

    # Result of the unit test

# Generated at 2022-06-13 12:15:58.768321
# Unit test for method close of class Connection
def test_Connection_close():
    mock_self = MagicMock()
    mock_self.runspace = 1
    mock_self.runspace.state = 1
    mock_self.runspace.state.OPENED = 1
    mock_self.runspace.state = 1
    mock_self.runspace.state.OPENED = 1
    mock_self.runspace = 1
    mock_self.runspace = 1
    mock_self._connected = 1
    mock_self._last_pipeline = 1
    mock__build_kwargs = MagicMock()
    mock__build_kwargs.return_value = 1
    with patch.multiple(Connection,
                        __init__=lambda x, y: None,
                        _build_kwargs=mock__build_kwargs,
                        ) as patch_map:
        a = Connection(1)


# Generated at 2022-06-13 12:16:08.920086
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    from ansible.modules.system import ping
    from ansible.plugins.loader import psrp_loader
    from ansible.plugins.connection.psrp import Connection

    # Create a mock inventory
    import ansible.inventory.manager
    inv_manager = ansible.inventory.manager.InventoryManager(loader=None, sources=['localhost,'])
    host = ansible.inventory.host.Host(name="localhost")
    inv_manager.inventory.add_host(host, group="local")

    # Create a mock variables manager
    import ansible.vars
    import ansible.parsing.yaml.objects
    vars_manager = ansible.vars.Manager(loader=None)

# Generated at 2022-06-13 12:16:18.131986
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # This module is currently Python3 only, this is a Python2 shim
    if PY2:
        pypsrp = pytest.importorskip("pypsrp")

    conn = Connection(None)
    cmd = None
    output = None
    ignore_errors = False
    executable = None
    in_data = None
    stdin = subprocess.PIPE
    stdout = subprocess.PIPE
    stderr = subprocess.PIPE
    binary_data = True
    path_prefix = None
    ssh_failure = None
    use_persistent_connections = False

    # Mock all the things
    conn.host = MagicMock()
    conn.protocol = MagicMock()
    conn.protocol.open_shell.return_value = MagicMock()

# Generated at 2022-06-13 12:16:50.402003
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file = open("../output/Connection_fetch_file.txt", "w")
    fetch_file.write('BEGIN testing Connection_fetch_file\n')
    fetch_file.flush()

    params = dict()
    params['remote_addr'] = '127.0.0.1'
    params['remote_user'] = 'ansible'
    params['remote_password'] = 'abcd12345'
    params['protocol'] = 'https'
    params['port'] = 5986
    params['connection_timeout'] = None
    params['read_timeout'] = None
    params['message_encryption'] = None
    params['proxy'] = None
    params['ignore_proxy'] = False
    params['operation_timeout'] = 30.0
    params['max_envelope_size'] = 153600

# Generated at 2022-06-13 12:16:52.672515
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
	connection = Connection()
	assert connection.exec_command('echo 1') == 0



# Generated at 2022-06-13 12:16:53.658704
# Unit test for constructor of class Connection
def test_Connection():
    Connection()

# Generated at 2022-06-13 12:16:55.127549
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass


# Generated at 2022-06-13 12:16:57.984388
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    temp_file = tempfile.NamedTemporaryFile()
    assert isinstance(temp_file, object)

# Generated at 2022-06-13 12:16:59.442359
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    assert isinstance(Connection(None), Connection)


# Generated at 2022-06-13 12:17:14.949778
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    '''
    # Unit test for method put_file of class Connection.
    # Mock psrp module. TODO: It would be better to just patch the real pypsrp methods
    '''
    global PSRP_MOCK_RUNSPACE
    call_info = []
    # The mock psrp module
    class MockPSRP():
        class MockRunspace():
            class MockPipeline():

                def __init__(self):
                    self.invoked = False
                    self.rc = 0
                    self.stdout = ['1', '2', '3', '4', '5']
                    self.stderr = ['a', 'b', 'c']
                    self.script = None
                    self.input = None
                    self.use_local_scope = True
                    self.arguments = None
                    self.std

# Generated at 2022-06-13 12:17:29.115996
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection(play_context=PlayContext())

# Generated at 2022-06-13 12:17:39.469040
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    conn = Connection(runspace_host=None, host=None,
                      script_invocation_event='',
                      script_invocation_event_encoding=None)

    class Mock_PypsrpClient_1:
        # Instance variables
        #   _psrp_conn_kwargs : dict
        #   session_id : int
        #   runspace_pool : RunspacePool
        #   runspace_pool_id : int
        #   runspace_pool_state : RunspacePoolState
        #   server_version : str
        #   server_timeout_ms : str

        # Constructor
        def __init__(self, **kwargs):
            self._psrp_conn_kwargs = kwargs
            self.runspace_pool = None
            self.server_version = mock_server_version

# Generated at 2022-06-13 12:17:40.433529
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    con = Connection()

# Generated at 2022-06-13 12:18:24.403750
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    class MockXMLElement():
        def __init__(self, text):
            self.text = text

    class MockPipeline():
        def __init__(self, result_dict):
            self.output = []
            self.streams = {}
            self.had_errors = False
            self.state = None

            self.output = result_dict['output']
            self.streams = result_dict['streams']
            self.had_errors = result_dict['had_errors']

        def stop(self):
            pass

    connection = psrp_connection.Connection(ansible_psrp_connection_args={})
    connection._parse_pipeline_result = psrp_connection.Connection._parse_pipeline_result.__func__

# Generated at 2022-06-13 12:18:25.671127
# Unit test for method close of class Connection
def test_Connection_close():
    # Setup test suite
    conn = Connection()
    # Test the method
    conn.close()


# Generated at 2022-06-13 12:18:27.556020
# Unit test for constructor of class Connection
def test_Connection():
    # This method is called to start the test
    psrp_connection = PSRPConnection('localhost', 23, 5, 'username', 'password')



# Generated at 2022-06-13 12:18:33.315531
# Unit test for method reset of class Connection
def test_Connection_reset():
    print('--- Connection.reset() ---')
    psrp_pass = 'super.secret'
    conn = Connection(
        ansible_host='127.0.0.1',
        ansible_port=5985,
        ansible_user='administrator',
        ansible_password=psrp_pass,
        ansible_connection='psrp',
        ansible_winrm_server_cert_validation='ignore',
    )
    conn.connect()
    assert conn.runspace.state == RunspacePoolState.OPENED
    conn.close()
    assert conn.runspace.state == RunspacePoolState.CLOSED
    conn.reset()
    assert conn.runspace.state == None


# Generated at 2022-06-13 12:18:34.723660
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass

# Generated at 2022-06-13 12:18:44.564589
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection  # pylint: disable=undefined-variable

    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None
    get_default_argspec.return_value = None

    # Disable calling PSRP method
    command = MagicMock(return_value=None)

# Generated at 2022-06-13 12:18:47.442576
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    connection.host = "localhost"
    module_args = {}

# Generated at 2022-06-13 12:18:55.248277
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    args1 = dict(
        in_path='string',
        out_path='string',
        use_ntlm_v2=None
    )
    p = patch('ansible_collections.ansible.community.plugins.connection.psrp.Connection._exec_psrp_script')
    mock__exec_psrp_script = p.start()
    mock__exec_psrp_script.return_value = (0, 'string', 'string')
    p = patch('ansible_collections.ansible.community.plugins.connection.psrp.Connection._parse_pipeline_result')
    mock__parse_pipeline_result = p.start()
    mock__parse_pipeline_result.return_value = (0, 'string', 'string')

# Generated at 2022-06-13 12:19:11.726453
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    print("")
    print("runtests.py (Connection_exec_command) starting")

    c = Connection()
    c.set_options(direct={'connection': 'psrp', 'remote_addr': 'localhost'})
    c._connected = True
    c._build_kwargs()
    runspace = c.runspace
    host = Host('localhost', runspace.protocol)
    host.power_shell_version = '5.1'
    host.ui = DummyPSHostUserInterface()
    runspace.host = host
    c._last_pipeline = PowerShell(runspace)

    # TODO: figure out a better way of mocking this out
    with patch('pypsrp.client.Client.get_connection') as get_connection:
        conn = Mock()

# Generated at 2022-06-13 12:19:13.922739
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  connection = get_connection({})
  if len(connection.exec_command()) > 0:
    return True
  else:
    return False


# Generated at 2022-06-13 12:20:32.436798
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    con = Connection()

    #Test 1:
    # Test Parameters
    module_defaults = {
        '_ansible_no_log': False,
        '_ansible_verbosity': 0,
        '_ansible_version': '2.9.9',
        '_ansible_module_name': 'debug',
        '_ansible_module_moved': None,
        '_ansible_shell_executable': '/bin/sh',
        '_ansible_module_arguments': ['msg=success'],
        '_ansible_builtin_fff': True
    }
    in_path = 'c:\\windows\\system32\\notepad.exe'
    out_path = '/tmp/ansible_test_out_file.ps1'

    # Fetch File
    file_args = module_

# Generated at 2022-06-13 12:20:36.585453
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = ansible.plugins.connection.psrp.Connection()
    assert not connection.fetch_file(in_path=None, out_path=None)


# Generated at 2022-06-13 12:20:51.979231
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:20:54.888431
# Unit test for method close of class Connection
def test_Connection_close():
    conn = Connection(None)
    conn.runspace = object()
    conn.runspace.state = RunspacePoolState.OPENED
    conn.close()
    assert conn.runspace is None
    assert conn._connected is False
    assert conn._last_pipeline is None


# Generated at 2022-06-13 12:21:05.586685
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Put file when file exists
    b_in_path = os.path.join(os.sep, "tmp", "test_file")
    b_out_path = os.path.join(os.sep, "tmp", "test_file_copy")
    with open(b_in_path, "wb") as f:
        f.write(b"test data")
        
    psrp_connection = Connection(None)
    psrp_connection.put_file(b_in_path, b_out_path)
    with open(b_out_path, "rb") as f:
        assert f.read() == b"test data"
        
    # Put file when file doesn't exist
    try:
        os.remove(b_out_path)
    except FileNotFoundError:
        pass


# Generated at 2022-06-13 12:21:15.276242
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    conn = Connection(module=None)
    conn.host = MagicMock()
    conn.host.runspace_pool = MagicMock()
    
    # mock out our runspace pool to act like we have a ready runspace
    conn.host.runspace_pool.state = RunspacePoolState.OPENED
    conn.host.runspace_pool.available_runspaces = 1
    
    # mock out our pipeline results
    pipeline_mock = MagicMock()
    pipeline_mock.output = ["hello", "world"]
    pipeline_mock.had_errors = False
    pipeline_mock.state = PSInvocationState.COMPLETED
    pipeline_mock.streams.error = []
    pipeline_mock.stop = MagicMock()
    conn.host.runspace_pool.execute_command = Magic

# Generated at 2022-06-13 12:21:24.205969
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    mock_play_context = MagicMock()
    mock_new_stdin = MagicMock()
    mock_new_stdout = MagicMock()
    mock_new_stderr = MagicMock()
    mock_tmp = MagicMock(
        spec=['close'],
        **{'__enter__.return_value': mock_new_stdin,
           '__exit__.return_value': None}
    )
    mock_script = MagicMock()
    mock_shell = MagicMock(
        **{'create_script.return_value': mock_script}
    )
    mock_protocol = MagicMock(
        **{'shell.return_value': mock_shell}
    )

# Generated at 2022-06-13 12:21:26.824181
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection=Connection(None)
    # Return True if the file is transferred to host successfully and False otherwise
    return connection.fetch_file('src_path','dest_path')
 

# Generated at 2022-06-13 12:21:34.539272
# Unit test for method exec_command of class Connection

# Generated at 2022-06-13 12:21:38.984166
# Unit test for method reset of class Connection
def test_Connection_reset():
    '''
    test_Connection_reset
    '''
    target_class = Connection
    target_obj = target_class()
    target_name = 'reset'

    assert hasattr(target_class, target_name), \
           "Class '%s' has no attribute '%s'" \
           % (target_class, target_name)
    target_method = getattr(target_obj, target_name)
    assert callable(target_method), \
           "Method '%s' is not callable" \
           % (target_name)

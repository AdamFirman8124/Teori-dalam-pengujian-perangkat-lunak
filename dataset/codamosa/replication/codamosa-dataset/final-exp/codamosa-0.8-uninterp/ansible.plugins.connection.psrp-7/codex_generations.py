

# Generated at 2022-06-13 12:12:49.546605
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pytest.skip("Method Connection.fetch_file() needs a unit test")

# Generated at 2022-06-13 12:12:50.838217
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    pass  # TODO: Write a unit test for this method

# Generated at 2022-06-13 12:12:56.281315
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # input parameters
    params = dict()
    params['cmd'] = '/bin/echo test_exec_command'
    params['in_data'] = ''
    params['chdir'] = None
    params['stdin'] = None
    params['stdout'] = None
    params['stderr'] = None
    params['environ_update'] = None
    params['binary_data'] = False

    # invoke method with sample input parameters
    rc, out, err = exec_command(**params)
    assert isinstance(rc, int)
    assert rc == 0
    assert isinstance(out, bytes)
    assert isinstance(err, bytes)

# Generated at 2022-06-13 12:13:03.850673
# Unit test for method reset of class Connection

# Generated at 2022-06-13 12:13:05.745303
# Unit test for method reset of class Connection
def test_Connection_reset():
    obj = Connection
    connection_result = obj.reset()
    assert connection_result == None


# Generated at 2022-06-13 12:13:15.457198
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
      from psrp.client import RunspacePoolState

     # Class arguments and attributes
      conn = Connection()
      conn.runspace = None
      conn._connected = False
      conn._last_pipeline = None
      host = "%s://%s:%s@%s" % ('http', 'username', 'password', 'localhost')
      conn._play_context = PlayContext()
      conn._play_context.verbosity = 2
      conn._play_context.connection = 'local'
      conn._psrp_auth = 'basic'
      conn.protocol = 'http'
      conn._psrp_user = 'username'
      conn._psrp_pass = 'password'
      conn._psrp_port = 5985
      conn._psrp_path = ''

# Generated at 2022-06-13 12:13:28.478433
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    print("Analyzing code for Connection.put_file...")
    current_module = inspect.getmodule(Connection.put_file)
    print(current_module.__name__)
    module_arg_spec = inspect.getfullargspec(current_module)
    print(module_arg_spec)
    current_class = inspect.getclass(Connection.put_file)
    print(current_class)
    class_arg_spec = inspect.getfullargspec(current_class)
    print(class_arg_spec)
    method_arg_spec = inspect.getfullargspec(Connection.put_file)
    print(method_arg_spec)
    print("Connection.put_file has the following parameters: ", end='')
    print(method_arg_spec.args)

# Generated at 2022-06-13 12:13:36.855618
# Unit test for method put_file of class Connection
def test_Connection_put_file():
	from tempfile import TemporaryFile
	from ansible.module_utils._text import to_bytes
	from ansible.plugins.connection.psrp import Connection
	from ansible.inventory.host import Host

	config = {
		'remote_addr': 'localhost',
		'remote_user': 'Administrator',
		'remote_password': 'vagrant',
		'port': 5986,
		'protocol': 'https',
		'connection_timeout': 10,
	}

	def _exec_psrp_script(self, script, input_data=None, use_local_scope=True,
						  arguments=None):
		self._exec_script_count += 1
		return 0, '', ''
	

# Generated at 2022-06-13 12:13:39.107335
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = PSRPConnection(play_context=PlayContext())
    connection._connected = True
    assert connection.put_file(in_path="t", out_path="t") == None



# Generated at 2022-06-13 12:13:42.262162
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    f_out_path = ""
    in_path = ""
    out_path = ""

# Generated at 2022-06-13 12:14:08.373538
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    b_test_server = '192.168.1.34'
    b_test_user = 'Administrator'
    b_test_password = 'Password123!'
    
    # test with basic authentication
    c = Connection(b_test_server, b_test_user, b_test_password,
                   connect_kwargs={'auth': 'basic'})
    c.exec_command('echo "Successfully connected with basic authentication"')
    
    # test with digest authentication
    c = Connection(b_test_server, b_test_user, b_test_password,
                   connect_kwargs={'auth': 'digest'})
    c.exec_command('echo "Successfully connected with digest authentication"')


# Generated at 2022-06-13 12:14:14.837548
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    host = 'targethost'
    psrp_user = 'test'
    pswd = 'test'
    psrp_protocol='https'
    psrp_port='5986'
    psrp_path='wsman'
    psrp_cert_validation = None #'ignore'
    psrp_message_encryption = None #'always'
    psrp_configuration_name = ''
    psrp_connection_timeout = 120
    psrp_read_timeout = None
    psrp_proxy = None
    psrp_ignore_proxy = True
    psrp_operation_timeout = None
    psrp_max_envelope_size = None
    psrp_reconnection_retries = 0

# Generated at 2022-06-13 12:14:20.843413
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Create an object of class Connection
    test_object = Connection()
    # Call the method put_file with arguments in_path, out_path, and validate
    # the return value
    # The following line will raise an exception if the method put_file of
    # class Connection does not accept arguments in_path, out_path
    # as specified
    assert test_object.put_file(in_path='in_path', out_path='out_path') is None


# Generated at 2022-06-13 12:14:26.743415
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    from ansible.module_utils.six.moves import cStringIO
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    p = connection_loader.get('winrm', None)
    assert p is not None
    assert type(p) == PSRPConnection

    context = PlayContext()
    context._play_context = context
    context._play = dict(connection='winrm')
    context.connection = 'winrm'
    context.remote_addr = 'remote_addr'
    context.remote_user = 'remote_user'
    context.password = 'password'
    context.port = 'port'

    display = Display()
    display.verbosity = 1

# Generated at 2022-06-13 12:14:27.726477
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    assert connection.fetch_file() == None

# Generated at 2022-06-13 12:14:38.948049
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    #fetch_file_conn = Connection()
    import psrp_playbook.connection as connection

# Generated at 2022-06-13 12:14:47.586811
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection()
    command = "command"
    in_data = "in data"
    stdout = b"stdout"
    stderr = b"stderr"
    rc = 1
    ps_out = _Pipeline(command, rc=rc, stdout=stdout, stderr=stderr, )
    ps_in = _Pipeline(command, rc=rc, stdout=stdout, stderr=stderr, )

    connection._exec_psrp_script = MagicMock(
        side_effect=[(ps_out, ps_in)])
    connection._build_kwargs = MagicMock(return_value=None)
    connection.psrp_version = None
    connection.get_option = MagicMock(return_value=None)
    connection.set_

# Generated at 2022-06-13 12:14:49.972608
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:14:59.980241
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():

    connection_local = Connection(play_context=PlayContext())
    connection_local.close()
    protocol = connection_local.connection._psrp_protocol
    port = connection_local.connection._psrp_port
    host = connection_local.connection._psrp_host
    user = connection_local.connection._psrp_user
    password = connection_local.connection._psrp_pass
    path = connection_local.connection._psrp_path
    message_encryption = connection_local.connection._psrp_message_encryption
    protocol = None
    port = None
    operation_timeout = None
    connection_timeout = None
    read_timeout = None
    auth = None
    cert_validation = None
    max_envelope_size = None
    path = None
    proxy = None

# Generated at 2022-06-13 12:15:03.398199
# Unit test for method put_file of class Connection
def test_Connection_put_file():

# Put file in the current directory
    c=Connection(None)
    c.put_file("./test.txt","test.txt")
# Put File in a directory of your choice
    c.put_file("./test.txt","test.txt","C:\\Users\\Me\\Documents\\")
    print("test_put_file successful")



# Generated at 2022-06-13 12:15:43.887066
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection(local_port=5986)
    connection.reset()
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None


# Generated at 2022-06-13 12:15:48.669031
# Unit test for method close of class Connection
def test_Connection_close():
    def test_close_mock(*args, **kwargs):
        # code for the mock
        raise Exception("This method hasn't been implemented")
    psrp = Connection()
    psrp.set_options = lambda *args, **kwargs: None
    psrp.runspace = mock.MagicMock()
    psrp._exec_psrp_script = lambda *args, **kwargs: None
    psrp.close = test_close_mock
    # check for the correct return value
    assert psrp.close() == None



# Generated at 2022-06-13 12:15:54.127015
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    args = dict(host=dict(port=5986))
    ps = Connection(play_context=PlayContext(become_method='runas'), **args)
    ps._build_kwargs()
    with pytest.raises(AnsibleConnectionFailure):
        ps.fetch_file(src="test", dest="test")

# Generated at 2022-06-13 12:16:02.936040
# Unit test for method put_file of class Connection
def test_Connection_put_file():
  fd = os.open('tests/put_file', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
  with os.fdopen(fd, 'wb') as temp_file:
    temp_file.write(b'test123')
  connection = Connection()
  connection.put_file('tests/put_file', '/tmp/tgt_file')
  assert os.path.exists('/tmp/tgt_file')
  assert open('/tmp/tgt_file', 'rb').read() == b'test123'
  os.unlink('/tmp/tgt_file')
  os.unlink('tests/put_file')


# Generated at 2022-06-13 12:16:10.536239
# Unit test for method reset of class Connection
def test_Connection_reset():
    p = pytest.importorskip("ansible_collections.ansible.powershell.plugins.connection.psrp")

    conn = p.Connection(play_context=dict())

    # call the method under test
    conn._build_kwargs()
    conn._open_runspace()
    conn._exec_psrp_script('Get-ExecutionPolicy')
    conn._exec_psrp_script('Set-ExecutionPolicy Unrestricted')

    assert conn._last_pipeline.state == PSInvocationState.RUNNING

    conn.reset(None)

    assert conn._last_pipeline.state == PSInvocationState.STOPPED
    assert conn.runspace.state == RunspacePoolState.OPENED
    assert conn._connected

    assert conn._psrp_host == dict()

   

# Generated at 2022-06-13 12:16:11.386075
# Unit test for method close of class Connection
def test_Connection_close():
    pass


# Generated at 2022-06-13 12:16:14.543760
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection(None)
    conn.put_file(
        in_path='/var/folders/cj/g5wbhhwj31b990zvbyd5ztfr0000gn/T/tmpxitfs9',
        out_path='/tmp/AnsiballZ_test.ps1'
    )



# Generated at 2022-06-13 12:16:21.533910
# Unit test for method reset of class Connection
def test_Connection_reset():
  import dotnet
  dotnet.reset_output()
  # x = psrp.Ansible_psrp_Connection(ansible_play_context=None, ansible_connection_user=None, ansible_connection_password=None, ansible_connection_https_use_envvar=None, ansible_connection_port=None, ansible_connection_host=None, ansible_connection_unix_socket=None, ansible_connection_local=None, ansible_connection_stack_trace=None, ansible_connection_debug=None, ansible_connection_timeout=None, ansible_connection_allow_executable=None, ansible_connection_keepalive=None, ansible_connection_path=None, ansible_connection_auth=None, ansible_connection_cert_validation=None, ansible_connection_

# Generated at 2022-06-13 12:16:28.817729
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    conn = Connection()
    assert conn.exec_command("whoami") == 0
    assert conn.exec_command("whoami", stdin=None) == 0
    assert conn.exec_command("whoami", stdin="") == 0
    assert conn.exec_command("whoami", stdin="ls") == 0
    assert conn.exec_command("whoami", stdin="ls", in_data=None) == 0


# Generated at 2022-06-13 12:16:31.517874
# Unit test for method reset of class Connection
def test_Connection_reset():
    from ansible.plugins.connection.psrp import Connection

    # set up object
    c = Connection()

    # test
    c.reset()


# Generated at 2022-06-13 12:17:17.809168
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Test with unsupported protocol
    # Failure expected
    failed = False
    try:
        transport = "psrp"
        connection = Connection(transport=transport)
        connection.fetch_file(in_path="C:\in_file.txt", out_path="C:\out_file.txt")
    except AnsibleError:
        failed = True
    assert failed
    # Test with unsupported protocol
    # Failure expected
    failed = False
    try:
        transport = "ssh"
        connection = Connection(transport=transport)
        connection.fetch_file(in_path="C:\in_file.txt", out_path="C:\out_file.txt")
    except AnsibleError:
        failed = True
    assert failed
    # Test with successful execution
    # Success expected
    transport = "local"


# Generated at 2022-06-13 12:17:31.260029
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    import os
    import shutil
    import tempfile
    import ansible.parsing
    import ansible.utils
    import ansible.errors
    import ansible_psrp.connection

    # create a temp directory and files
    temp_dir = tempfile.mkdtemp(prefix='ansible-psrp-test-')
    temp_src_path = os.path.join(temp_dir, 'test-src')
    temp_dst_path = os.path.join(temp_dir, 'test-dst')
    temp_arg_path = os.path.join(temp_dir, 'test-arg')
    temp_arg_b64_path = os.path.join(temp_dir, 'test-arg-b64')

# Generated at 2022-06-13 12:17:31.946979
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    assert True


# Generated at 2022-06-13 12:17:36.291137
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = create_Connection()
    params = {}
    filename = '/home/user/Desktop/inventory.txt'
    remote_filename = '/home/user/inventory.txt'
    test_it = connection.put_file(filename, remote_filename)
    assert test_it == None


# Generated at 2022-06-13 12:17:39.552112
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection()
    result = connection.exec_command("")
    assert result.rc == 0
    assert result.stdout == ""
    assert result.stderr == ""

# Generated at 2022-06-13 12:17:40.882870
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    connection.close()

# Generated at 2022-06-13 12:17:50.043515
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    #print('Connection.put_file()')

    # Create connection object
    ansible_psrp_host = 'server01'
    connection = Connection(ansible_psrp_host)

    # Create a temporary file
    fd, temp_path = tempfile.mkstemp(prefix='ansible-test-put-file')
    with os.fdopen(fd, 'wb') as file_obj:
        file_obj.write(b"test")

    # Copy the file to a remote tempfile
    in_path = temp_path
    out_path = "/tmp/ansible-test-put-file"
    remote_path = os.path.dirname(out_path)
    connection.put_file(in_path, out_path)

    # Remove the remote tempfile
    command = "rm %s"

# Generated at 2022-06-13 12:17:59.922237
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    # Arrange
    destination = 'C:\\Ansible\\test.txt'
    data = 'Test text'
    local_path = 'C:\\Ansible\\test.txt'
    mode = None

    # Arrange - Mock connection
    psrp_conn = MagicMock(spec=PSRPRunspacePool)
    psrp_conn.runspace = MagicMock()
    psrp_conn.runspace.state = RunspacePoolState.OPENED

    # Arrange - Mock AnsibleConnection
    psrp_connection = Connection(MagicMock(), MagicMock())
    psrp_connection.psrp_conn = psrp_conn

    # Act
    psrp_connection.put_file(destination, data)

    # Assert
    psrp_conn._exec_

# Generated at 2022-06-13 12:18:02.431454
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    connection.close()


# Generated at 2022-06-13 12:18:05.986688
# Unit test for method reset of class Connection
def test_Connection_reset():
#{{{
    mo = mock_open(read_data="test-data")
    with patch("ansible_collections.ansible.community.plugins.connection.psrp.open", mo, create=True):
        conn = Connection(None)
        conn.reset()
        mo.assert_called_once_with("test-data", "rb")
#}}}

# unit tests for Connection class

# Generated at 2022-06-13 12:19:24.018367
# Unit test for method reset of class Connection
def test_Connection_reset():
    from ansible.plugins.connection.psrp import Connection
    connection_psrp = Connection()
    connection_psrp.reset()

# Generated at 2022-06-13 12:19:26.866447
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    psrp_connection.put_file(in_path=None, out_path='string', preserve_mode=None, preserve_times=None, directory_mode=None)


# Generated at 2022-06-13 12:19:36.228685
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    import mock
    import io
    import tempfile
    import os.path
    
    # This is creating a mock object
    temp_file = mock.Mock()
    # This is setting the attribute side_effect of the mock object to a file object
    temp_file.side_effect = lambda: io.FileIO(tempfile.mktemp(dir='.'), 'w')
    
    m = mock.mock_open()
    # This is setting the open function of the os module to m
    os.open = m
    
    # This is setting the attribute side_effect of the mock object to a file object
    m.side_effect = temp_file
    # This is setting the open function of the builtins module to m
    builtins.open = m
    # This is setting the rename function of the os module to m

# Generated at 2022-06-13 12:19:47.428559
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    remote_addr = 'dev.azure.com'
    remote_user = 'testadmin'
    remote_password = 'testpassword'
    port = '5986'
    protocol = 'https'
    path = 'wsman'
    auth = 'basic'
    connection_timeout = '12'
    read_timeout = '12'
    max_envelope_size = '153600'
    operation_timeout = '300'
    read_reconnection_retries = '3'
    read_reconnection_backoff = '1'
    credssp_auth_mechanism = 'negotiate'
    credssp_disable_tlsv1_2 = 'false'
    credssp_minimum_version = '2'
    negotiate_send_cbt = 'false'

# Generated at 2022-06-13 12:19:58.204608
# Unit test for method fetch_file of class Connection

# Generated at 2022-06-13 12:19:58.864516
# Unit test for method close of class Connection
def test_Connection_close():
    pass


# Generated at 2022-06-13 12:20:01.609606
# Unit test for method reset of class Connection
def test_Connection_reset():
    # Setup test
    connection = Connection(transport='http')

    # Invoke method
    connection.reset()

    # Validate
    assert connection != None


# Generated at 2022-06-13 12:20:04.025033
# Unit test for method reset of class Connection
def test_Connection_reset():
    conn = Connection()
    result = conn.reset()
    assert result is None



# Generated at 2022-06-13 12:20:05.519427
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection(None, None, None)
    # The actual test is done in the class method
    assert True

# Generated at 2022-06-13 12:20:13.041103
# Unit test for method reset of class Connection
def test_Connection_reset():
  con = Connection()
  con.close()
  con._connected = True
  con._last_pipeline = u'PSRP Pipeline'
  con._build_kwargs()
  con._psrp_host = 'localhost'
  con._psrp_user = u'username'
  con._psrp_pass = u'password'
  con._psrp_protocol = u'https'
  con._psrp_port = 5986
  con._psrp_path = u'/wsman'
  con._psrp_auth = u'ntlm'
  con._psrp_cert_validation = True
  con._psrp_connection_timeout = 30
  con._psrp_read_timeout = None
  con._psrp_message_encryption = u'auto'
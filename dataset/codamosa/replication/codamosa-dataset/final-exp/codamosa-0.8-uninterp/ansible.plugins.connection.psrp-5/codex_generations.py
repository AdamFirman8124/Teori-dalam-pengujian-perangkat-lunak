

# Generated at 2022-06-13 12:12:43.928068
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection(play_context=play_context(connection='local'))
    command = 'echo hello'
    result = connection.exec_command(command)
    assert result
    assert not bool(result.rc)
    assert result.stdout == "hello"
    assert result.stderr == ""


# Generated at 2022-06-13 12:12:52.803136
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    aconn = Connection('localhost')
    aconn._build_kwargs = lambda: None
    aconn._fetch_file = lambda: None
    aconn._exec_psrp_script = lambda: (0, 'success', '')
    aconn._parse_pipeline_result = lambda x: (0, b'success', b'')
    aconn.runspace = RunspacePool()
    aconn.runspace.state = RunspacePoolState.OPENED
    aconn.host = OutputStream()
    aconn._last_pipeline = None


# Generated at 2022-06-13 12:12:54.674789
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    c = Connection()
    assert c.fetch_file("foo", "bar") == (1, "test")

# Generated at 2022-06-13 12:13:03.709212
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    # Test basic connection functionality
    ansible_mock = mock.MagicMock()
    transport_mock = mock.MagicMock()
    winrm_host_mock = mock.MagicMock()
    tempfile_mock = mock.MagicMock()
    tempfile_mock.gettempdir.return_value = "/tmp"
    tempfile_mock.mkstemp.return_value = (0, "/tmp/debug.txt")
    connection = winrm.Connection(ansible_mock, transport_mock, winrm_host_mock, tempfile_mock)

    # Test null conditionals
    connection.put_file(None, None)

    # Test transport write_file
    transport_mock.write_file.assert_called_with(None, "/tmp/debug.txt")

# Unit

# Generated at 2022-06-13 12:13:08.578007
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()

    reset_method = inspect.getmember(Connection, 'reset')
    assert reset_method is not None


# Generated at 2022-06-13 12:13:16.891519
# Unit test for method close of class Connection
def test_Connection_close():
    try:
        from units.compat.mock import patch
    except ImportError:
        from unittest.mock import patch

    # Instantiate mock classes / objects
    ansible_module_utils_powershell_common_runspace = mock.Mock()
    type(ansible_module_utils_powershell_common_runspace).state = PropertyMock(return_value=RunspacePoolState.OPENED)
    mock_ansible_module_utils_powershell_common_runspace = ansible_module_utils_powershell_common_runspace()

    ansible_module_utils_powershell_common_display = mock.Mock()
    type(ansible_module_utils_powershell_common_display).v = PropertyMock(return_value=None)
    mock_ansible_module_utils_powershell

# Generated at 2022-06-13 12:13:29.165831
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection=Connection(None, "ucpd.ut.com", "root", "passwd", False, False)
    in_path="/home/root/Ansible/tests/test_data/put_file_src.txt"
    out_path="/home/root/put_file_dst.txt"
    connection.put_file(in_path,out_path)
    assert connection._psrp_host == "ucpd.ut.com"
    assert connection._psrp_user == "root"
    assert connection._psrp_pass == "passwd"
    assert connection._psrp_port == 5961
    assert connection._psrp_path == "/wsman"
    assert connection._psrp_auth == "basic"
    assert connection._psrp_protocol == "http"

# Generated at 2022-06-13 12:13:36.556549
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
#    m = mock_open()
#    with patch('builtins.open', m, create=True):
#        with patch('psrp.connection.Connection.exec_command', return_value=''):
#            con = Connection(None, None, None)
#            result = con.exec_command(None)
#            assert result == ''

    m = mock_open(read_data='{"abc":[null,"abc",1234,true]}')
    with patch('builtins.open', m, create=True):
        con = Connection(None, None, None)
        result = con.exec_command(None)
        assert result == '{"abc":[null,"abc",1234,true]}'


# Generated at 2022-06-13 12:13:45.125802
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    tempdir = tempfile.mkdtemp()
    src_file_name = "_my_file.txt"
    src_file_path = os.path.join(tempdir, src_file_name)

    src_file_data = "This is the data in my test file."
    with open(src_file_path, "w") as file:
        file.write(src_file_data)

    dest_file_name = src_file_name
    dest_file_path = os.path.join(tempdir, dest_file_name)

    my_connection = Connection(play_context=None)

    dest_file_data = None


# Generated at 2022-06-13 12:13:49.712940
# Unit test for method reset of class Connection
def test_Connection_reset():
    """
    reset()
    """
    # Set up mock
    connection = Connection()

    connection._connected = True
    connection.runspace = mock.MagicMock()

    # Invoke method
    connection.reset()

    # Check return value
    assert isinstance(connection._connected, bool)
    assert connection._connected == False

    assert isinstance(connection.runspace, mock.MagicMock)
    assert connection.runspace.id == 1

    assert connection.runspace.close.call_count == 1
    # Assert function calls
    connection.runspace.close.assert_called_once_with(
    )

# Generated at 2022-06-13 12:14:13.891284
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    imp = Importer()
    imp.initialize()
    main_connection = imp.load_module('connection')

    c = main_connection.Connection()
    c.set_options()
    c._build_kwargs()
    c._connect()

    class MyPSRPHost(BasePSRPHost):
        script_dir = os.path.dirname(os.path.abspath(__file__))

    c.host = MyPSRPHost(c._psrp_conn_kwargs, psrp_module=pypsrp)

    remote_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "test", "integration", "targets", "test_smb_connection")

# Generated at 2022-06-13 12:14:23.109555
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Setup test case
    # Argument Parsing
    module_args = dict(
        a=dict(type='str', required=False, default=None),
        b=dict(type='str', required=False, default=None),
    )
    module = AnsibleModule(argument_spec=module_args)
    module_output = dict()
    # Connection test
    host = 'localhost'
    user = 'testuser'
    psrp_pass = 'testpass'
    psrp_port = 1
    psrp_path = 'testpath'
    psrp_protocol = 'testprotocol'
    psrp_auth = 'testauth'
    psrp_cert_validation = True
    psrp_connection_timeout = 1
    psrp_read_timeout = 1
    psr

# Generated at 2022-06-13 12:14:24.589487
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file = Connection()
    expected = fetch_file
    actual = fetch_file.fetch_file()
    assert actual == expected

# Generated at 2022-06-13 12:14:33.214643
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    def test_fetch_file_replace():
        """
        Instrumentation to replace fetch_file method so we can assert its input parameters.
        """
        msg = "invoked fetch_file with self: {}, in_path: '{}', (b)out_path: '{}', mode: '{}', bufsize: {}"
        display.vvvv(msg.format(self, in_path, b_out_path, mode, bufsize))

        # Return expected output
        return True, 0, 0

    mocked_fetch_file = types.MethodType(test_fetch_file_replace, Connection)

    # Make sure the class is tested here
    connection = Connection(None, 'psrp')
    assert connection is not None
    # Set our mocked method
    connection.fetch_file = mocked_fetch_file

# Generated at 2022-06-13 12:14:36.949410
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  # Initialize a Connection object
  conn = Connection()
  # There should be no exception if the following code is executed
  try:
    conn.exec_command('echo test')
  except:
    raise

# Generated at 2022-06-13 12:14:37.359075
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    assert True


# Generated at 2022-06-13 12:14:38.948053
# Unit test for method close of class Connection
def test_Connection_close():
    connection=Connection(None)
    assert connection.close() ==None

# Generated at 2022-06-13 12:14:43.593901
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connect_mock = MagicMock()
    connect_mock.runspace = MagicMock()
    connect_mock.runspace.available = True
    connect_mock.runspace.id = MagicMock()
    connect_mock.runspace.state = MagicMock()
    connect_mock.has_pipelining = MagicMock(return_value=True)
    connect_mock.get_option = MagicMock(return_value=True)
    connect_mock._exec_psrp_script = MagicMock(return_value=(0, ("output"), ("err")))

    psrp_connection = Connection(play_context=play_context)
    psrp_connection.__dict__["_connected"] = True
    psrp_connection.__dict__["_last_pipeline"]

# Generated at 2022-06-13 12:14:50.628842
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    if not pytest.config.getoption("--psrp"):
        pytest.skip("test requires the --psrp option to run")

    psrp_host = pytest.config.getoption("psrp_host")
    psrp_user = pytest.config.getoption("psrp_user")
    psrp_pass = pytest.config.getoption("psrp_pass")

    psrp_conn = Connection(psrp_host, psrp_user, psrp_pass, "")
    psrp_conn.connect()
    psrp_conn.mkdir("$env:TEMP\ansible-test", False)

# Generated at 2022-06-13 12:15:00.374213
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    remote_addr = '192.168.1.1'
    remote_port = 5986
    psrp_protocol = 'https'
    psrp_path = "wsman"
    psrp_user = "Administrator"
    psrp_pass = 'password'
    psrp_connection_timeout = 60
    psrp_read_timeout = 30
    psrp_cert_validation = False


# Generated at 2022-06-13 12:15:25.152358
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connector()
    cmd = "echo test"
    rc, stdout, stderr = connection.exec_command(cmd)
    assert rc == 0
    assert stdout == b"test\n"
    assert stderr == b""

# Generated at 2022-06-13 12:15:32.864226
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:15:37.647612
# Unit test for method reset of class Connection
def test_Connection_reset():
    """
    Connection - reset
    """
    _connection = Connection()

    # Place your implementation here
    try:
        pass
    except AttributeError:
        pass
    except NotImplementedError:
        pass
    except NameError:
        pass
    else:
        _connection.reset()


# Generated at 2022-06-13 12:15:46.581974
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    fetch_file(self, in_path, out_path, remotepath=None, use_sudo=False, diff_peek=False, follow=False)
    """
    con = Connection()
    con.get_option = MagicMock(return_value=None)
    con.become = MagicMock(return_value=False)
    con.put_file = MagicMock()
    in_path = 'test'
    out_path = 'test'
    remotepath = None
    use_sudo = False
    diff_peek = False
    follow = False
    con.set_file_attributes_if_different = MagicMock()

    con.fetch_file(in_path, out_path, remotepath, use_sudo, diff_peek, follow)
    con

# Generated at 2022-06-13 12:15:57.890877
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    args = {}
    options_psrp = module_utils.connection.Options()
    options_psrp.connection = 'ansible.windows.winrm'
    options_psrp.username = 'ansible'
    options_psrp.password = 'supersecret'
    options_psrp.remote_addr = '192.168.0.10'
    transport = 'https'
    port = 5986
    url = 'http://192.168.0.10:5985/wsman'
    path = '/wsman'
    config = 'ansible'
    default_transport = 'https'
    default_port = 5986
    connection = Connection(module_args=args, supports_check_mode=False,
                            connection_options=options_psrp)

# Generated at 2022-06-13 12:16:02.284435
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # simple test
    c = Connection()
    display.vvvvv("Testing exec_command")
    assert c.exec_command("echo hello") == (0, b'hello\r\n', b'')

# Generated at 2022-06-13 12:16:11.733736
# Unit test for method exec_command of class Connection

# Generated at 2022-06-13 12:16:19.769041
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # default parameter values
    kwargs = dict()
    kwargs['cmd']=None
    kwargs['in_data']=None

    # parameter values to override
    overrides = dict()
    overrides['cmd']=None
    overrides['in_data']=None

    # instance to run the test on
    c = Connection(**kwargs)

    # run the test
    c.exec_command(**overrides)

    # update the overrides
    overrides['cmd']='ipconfig'
    overrides['in_data']=None

    # run the test
    c.exec_command(**overrides)

    # update the overrides
    overrides['cmd']='ipconfig'
    overrides['in_data']=None

    # run the test

# Generated at 2022-06-13 12:16:31.480538
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    mock_runspace = Mock()
    mock_runspace.id = 'runspaceID'
    mock_runspace.state = RunspacePoolState.OPENED

    mock_runspace_pool = Mock()
    mock_runspace_pool.get_runspaces.return_value = [mock_runspace]
    mock_runspace_pool.run.return_value = mock_runspace
    mock_runspace_pool.id = 'runspacePoolID'

    mock_wsman = Mock()
    mock_wsman.create_runspace_pool.return_value = ('runspacePoolID', mock_runspace_pool)
    mock_wsman.run_shell.return_value = ('runspaceID', mock_runspace)
    mock_wsman.close_runspace_pool.return_value = None
    mock

# Generated at 2022-06-13 12:16:39.144119
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    host = {}
    host['ansible_connection'] = 'psrp'
    host['ansible_user'] = 'Administrator'
    host['ansible_password'] = 'M0d3l3r22'
    host['address'] = 'localhost'
    host['port'] = 5985
    
    c = psrp.Connection(host)
    c._connected = True
    c._play_context = c
    c._play_context.verbosity = 1
    c.runspace = c
    c.runspace.state = RunspacePoolState.OPENED
    c.host = c
    c.host.ui = c
    
    cmd = "write-output $true"
    rc, out, err = c.exec_command(cmd)
    assert rc == 0

# Generated at 2022-06-13 12:17:27.284434
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection(play_context=PlayContext(connection='psrp', remote_addr='0.0.0.0', protocol='https', port=5986, remote_user='test', password='test',), _extras={'ansible_psrp_user': 'test', 'ansible_psrp_pass': 'test', 'ansible_psrp_port': 5986, 'ansible_psrp_host': '0.0.0.0', 'ansible_psrp_ssl': 'True', 'ansible_psrp_connection': 'psrp', 'ansible_psrp_auth': 'basic'})
    assert connection._build_kwargs() == None
    # TODO: Add proper asserts for command arguments
    # assert connection._exec_psrp_script(script, input_data=None

# Generated at 2022-06-13 12:17:28.579618
# Unit test for method close of class Connection
def test_Connection_close():
    print("\nTesting close")
    myconn = Connection()
    myconn.close()
    
    

# Generated at 2022-06-13 12:17:35.742583
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = ConnectionPsrp()
    command = 'whoami'
    rc = 0
    stdout = 'stdout'
    stderr = 'stderr'
    input_data = 'input'
    out = connection.exec_command(command, command, input_data, sudoable=True)
    assert out[0] == rc
    assert out[1] == stdout
    assert out[2] == stderr
    assert out[3] == stdout
if __name__ == '__main__':
    test_Connection_exec_command()

# Generated at 2022-06-13 12:17:45.006763
# Unit test for method close of class Connection
def test_Connection_close():
    host = 'myhost'
    psrp_host = 'host'
    psrp_user = 'user'
    psrp_pass = 'password'
    psrp_path = 'path'
    connection_timeout = 10
    read_timeout = 10
    max_envelope_size = 153600
    operation_timeout = 3600
    reconnection_retries = 5
    reconnection_backoff = 5
    psrp_port = 5985
    psrp_protocol = 'https'
    psrp_auth = 'basic'
    psrp_cert_validation = 'ignore'
    psrp_message_encryption = 'auto'
    psrp_proxy = 'username:password@myproxy.net:5555'
    psrp_ignore_proxy = False
   

# Generated at 2022-06-13 12:17:52.995669
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  psrp_conn = Connection('psrp')
  # Make psrp_host, psrp_user, psrp_pass, psrp_port available to relevant methods
  psrp_conn._psrp_host = 'psrp_host'
  psrp_conn._psrp_user = 'psrp_user'
  psrp_conn._psrp_pass = 'psrp_pass'
  psrp_conn._psrp_port = 5985
  psrp_conn.runspace = None
  psrp_conn._connected = False

  # Init runspace pool with 1 runspace
  psrp_conn._init_runspace_pool(1, True)
  assert psrp_conn.runspace is not None

  # Check if the runspace is

# Generated at 2022-06-13 12:18:00.518955
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    in_path = u'test_in.txt'
    out_path = u'test_out.txt'
    fetch_file = patch('ansible.plugins.connection.psrp.Connection.fetch_file').start()
    host = 'test_windows'
    connection = Connection(host)
    assert fetch_file.call_count == 0
    connection.fetch_file(in_path, out_path)
    assert fetch_file.call_count == 1
    assert fetch_file.call_args[0][0] == in_path
    assert fetch_file.call_args[0][1] == out_path

# Generated at 2022-06-13 12:18:06.782461
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Test the method named exec_command of class Connection
    """
    # Testcase 1: When host is not specified, it should raise an ArgumentError

# Generated at 2022-06-13 12:18:22.615142
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Initialize a connection
    p = Connection(play_context=dict(remote_addr='host'))
    # Execute a command, the returned value is a tuple (return code, standard output, standard error)
    result = p.exec_command('dir')
    # Expected output
    print(result)

# Generated at 2022-06-13 12:18:24.152845
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = PSRPAuthentication()
    result = connection.exec_command('ls')
    assert result == None


# Generated at 2022-06-13 12:18:30.936373
# Unit test for method close of class Connection
def test_Connection_close():
    remote_addr = None
    remote_user = None
    remote_password = None
    transport = None
    port = None
    psrp_path = None
    psrp_auth = None
    psrp_cert_validation = None
    psrp_connection_timeout = None
    psrp_read_timeout = None
    psrp_message_encryption = None
    psrp_proxy = None
    psrp_ignore_proxy = None
    psrp_operation_timeout = None
    psrp_max_envelope_size = None
    psrp_configuration_name = None
    psrp_reconnection_retries = None
    psrp_reconnection_backoff = None
    psrp_certificate_key_pem = None
    psrp_

# Generated at 2022-06-13 12:19:16.801495
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    stdout = b"""PS C:\\Windows\\system32> C:\\Users\\TestAdmin\\psrp-test-upload-file.ps1
Finished uploading file

PS C:\\Windows\\system32> """
    stderr = b"""
"""

# Generated at 2022-06-13 12:19:28.067560
# Unit test for method reset of class Connection
def test_Connection_reset():
    #
    # Tests for reset()
    #
    # stdout = to_bytes(stdout, encoding='utf-8')
    # stderr = to_bytes(stderr, encoding='utf-8')
    #
    # Test reset() with no parameters
    #
    test_Connection_reset_instance = Connection()
    test_Connection_reset_instance.reset()
    # 
    # Test reset() with no parameters
    #
    test_Connection_reset_instance = Connection()
    test_Connection_reset_instance.reset()
    # 
    # Test reset() with no parameters
    #
    test_Connection_reset_instance = Connection()
    test_Connection_reset_instance.reset()
    # 
    # Test reset() with no parameters
    #
    test_Connection_reset_instance = Connection()

# Generated at 2022-06-13 12:19:33.675567
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    print("Executing test_Connection_put_file")
    # Fixture data
    test_file_path = "./test_put.txt"
    # If a file already exists, delete it.
    try:
        os.remove(test_file_path)
    except OSError:
        pass

    # Testing the method
    # We need at least a connection object to test the method
    conn = requests.Connection()
    # Put file
    conn.put_file(test_file_path, b"test data")

    # Validation
    # Check if the file was created
    assert os.path.isfile(test_file_path)
    # Check if the file has the correct content
    assert b"test data" == open(test_file_path, 'rb').read()
    # Clean up
    # Delete the

# Generated at 2022-06-13 12:19:45.078186
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  connection = Connection(
    module=None,
    play_context=None,
    new_stdin=None,
    shell=None
  )
  command = b"dir"
  result = connection.exec_command(command)
  assert(result[0] == int(0))
  assert(len(result[1]) == 2)
  assert(len(result[2]) == 0)
  print(result)

# Generated at 2022-06-13 12:19:51.819616
# Unit test for method close of class Connection
def test_Connection_close():
    psrp_host = 'localhost'
    psrp_port = 5985
    psrp_path = '/wsman'
    psrp_user = 'vagrant'
    psrp_pass = 'vagrant'
    psrp_protocol = 'http'
    psrp_connection_timeout = 30
    psrp_read_timeout = 30
    psrp_message_encryption = False
    psrp_operation_timeout = 30
    psrp_max_envelope_size = 153600
    psrp_cert_validation = False
    psrp_reconnection_retries = 2
    psrp_reconnection_backoff = 0.2
    psrp_configuration_name = 'Microsoft.PowerShell'

    from ansible.plugins.connection import ConnectionBase

# Generated at 2022-06-13 12:19:57.913920
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection({})
    assert not connection.connected

    # Reset the connection
    connection.connected = True
    connection.reset()
    assert not connection.connected

    # Close the runspace to ensure it is destroyed, this needs to be
    # tested separately from the reset method as it is called from within
    # the reset method.
    connection._build_kwargs()
    connection._connect()
    connection.close()
    assert connection.runspace is None


# Generated at 2022-06-13 12:20:06.132480
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Test when the destination is a folder
    destination = '/Users/mike/Desktop/Notebooks/'
    # Test when the destination is a file
    # destination = '/Users/mike/Desktop/NewTextFile.txt'
    # Test when the destination is a new file
    # destination = '/Users/mike/Desktop/NewFile.txt'
    directory = '/Users/mike/Desktop/'
    
    # We only test if the put_file method works
    return put_file(directory, destination)
# Testing the put_file method of Connection class
test_Connection_put_file()


# Generated at 2022-06-13 12:20:11.862220
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    #From mock_module.py: def fetch_file(self, in_path, out_path):
    connection = PsrpConnection()
    connection.host = mock_module.MockModule(shell='powershell')
    connection.port = 5985
    in_path = 'C:\\Program Files\\Hashicorp\\Vagrant\\bin\\vagrant.exe'
    out_path = 'C:\\Users\\vagrant\\AppData\\Local\\Temp\\ansible_VBZp0b\\vagrant.exe'
    assert connection.fetch_file(in_path, out_path) != None


# Generated at 2022-06-13 12:20:21.538345
# Unit test for method reset of class Connection
def test_Connection_reset():
    host = 'localhost'
    # Skip test for connection=local
    if host == 'localhost':
        pass
    # Initialize the target class
    psrp_connection = Connection()
    # Run the method as a test tuple
    args = ()  # No args
    kwargs = {}  # No kwargs
    # Run the method as a test
    res = psrp_connection.reset(*args, **kwargs)
    # Basic test assertion
    # No result/return value from the target class so this test is a pass-thru for now
    assert res is None

# Generated at 2022-06-13 12:20:24.634778
# Unit test for method reset of class Connection
def test_Connection_reset():
    '''
    Unit test for function Connection.reset
    '''
    _connection = Connection()

    _connection.reset()



# Generated at 2022-06-13 12:21:34.893274
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    fetch_file(self, in_path, out_path, use_ntlm=False)
    """
    print("not implemented")
    # connection = None
    # in_path = None
    # out_path = None
    # use_ntlm = None
    # expected = None
    # actual = connection.fetch_file(in_path, out_path, use_ntlm)
    # assertEqual(expected, actual)


# Generated at 2022-06-13 12:21:45.498620
# Unit test for method reset of class Connection
def test_Connection_reset():
    conn = psrp_connection.Connection(None)
    conn.reset()

    with pytest.raises(AnsibleError) as excinfo:
        conn.play_context.connection = 'blah'
        conn.play_context.network_os = 'blah'
        conn.play_context.remote_addr = 'blah'
        conn.play_context.port = 'blah'
        conn.play_context.remote_user = 'blah'
        conn.play_context.password = 'blah'
        conn.play_context.private_key_file = 'blah'
        conn.play_context.connection_user = 'blah'
        conn.play_context.become = 'blah'
        conn.play_context.become_method = 'blah'
        conn.play_

# Generated at 2022-06-13 12:21:54.913923
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection(None)
    conn._exec_psrp_script = Mock()
    conn._parse_pipeline_result = Mock(return_value=(0, 'abc', 'def'))
    conn.fetch_file(None, None)
    conn._exec_psrp_script.assert_has_calls([call('$ab = $fs.GetType().Assembly.Location', use_local_scope=True),
                                             call('$b=[System.Convert]::FromBase64String', use_local_scope=True,
                                                  arguments=[u'ABC==']),
                                             call('$fs.Write($b, 0, $b.Length)', use_local_scope=True),
                                             call('$fs.Close()', use_local_scope=True)])
    conn._parse_

# Generated at 2022-06-13 12:22:11.984739
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    import tempfile
    tmp_dir = tempfile.gettempdir()
    tmp_file_path = tempfile.mktemp(dir=tmp_dir)
    tmp_file = open(tmp_file_path, 'w')
    tmp_file.write("test_Connection_put_file")
    tmp_file.close()
    print(type(tmp_file_path))
    print(type(tmp_file_path))
    instance = Connection(module=None, play_context=None, new_stdin=None, _ansible_connection_closed=False)
    instance._build_kwargs()
    instance._connect()
    #instance.put_file(in_path=tmp_file_path, out_path=tmp_file_path)
    #instance.close()

# Generated at 2022-06-13 12:22:19.192877
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # initialize
    test_conn=Connection()
    test_conn.run()
    # test
    test_conn.put_file(in_path=tmp_path + "/local/mydir/mydir_file", out_path=tmp_path + "/remote/mydir/mydir_file")
    print("Test Result:")
    print("------------")
    print("file_put_result:")
    with open(tmp_path + "/remote/mydir/mydir_file") as f:
        for line in f:
            print(line)
    print("------------")
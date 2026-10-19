

# Generated at 2022-06-13 12:12:49.020843
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    connection__put_file_dict = {}

    connection__put_file_dict['in_path'] = 'fake-in_path'

    connection__put_file_dict['out_path'] = 'fake-out_path'

    connection__put_file_dict['in_data'] = b'fake-in_data'

    connection__put_file_dict['out_data'] = 'fake-out_data'

    connection__put_file_dict['mode'] = 'fake-mode'

    connection__put_file_dict['content'] = 'fake-content'

    connection__put_file_dict['content_type'] = 'fake-content_type'

    connection__put_file_dict['content_encoding'] = 'fake-content_encoding'


# Generated at 2022-06-13 12:12:57.599454
# Unit test for method reset of class Connection
def test_Connection_reset():
    # setup test
    mock_transport = 'mock_transport'
    mock_ssh_proxy = 'mock_ssh_proxy'
    mock_internal_port = 'mock_internal_port'
    mock_no_log = 'mock_no_log'
    mock_accelerate_port = 'mock_accelerate_port'
    mock_accelerate_ipv6 = 'mock_accelerate_ipv6'
    mock_accelerate_fqdn = 'mock_accelerate_fqdn'
    mock_ports = 'mock_ports'
    mock_control_path = 'mock_control_path'
    mock_control_path_dir = 'mock_control_path_dir'
    mock_ssh_args = 'mock_ssh_args'


# Generated at 2022-06-13 12:13:05.878604
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.six.moves import StringIO

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()
    display.verbosity = 3

    # source of test file
    source_file = 'test_file'
    src_content = to_bytes('test')

    # destination of test file
    dest_path = 'C:\\temp\\test_file'
    # destination of test file (as seen by the remote system)
    dest_path_remote = '\\\\windows-pc\\c$\\temp\\test_file'

# Generated at 2022-06-13 12:13:15.009923
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Test method exec_command of class Connection
    """
    # pylint: disable=protected-access

    connection = Connection(module_name='test_Connection_exec_command')
    connection._build_kwargs = MagicMock(return_value={})
    connection._create_runspace_pool = MagicMock(return_value={})
    connection._exec_psrp_script = MagicMock(return_value=('1', '2', '3'))


    connection.exec_command('test')

    connection._exec_psrp_script.assert_called_once_with(
        'test',
        arguments=None,
        input_data=None,
        use_local_scope=True
    )


# Generated at 2022-06-13 12:13:18.104796
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection=Connection()
    assert connection.exec_command("powershell.exe", "ipconfig /all") is not None


# Generated at 2022-06-13 12:13:24.319953
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection()
    remote_path = "C:\\temp\\test.txt"
    in_path = conn.playbook_path+"/test.txt"
    conn.put_file(in_path, remote_path)
    assert os.path.exists('C:/temp/test.txt') is True
    os.remove('C:/temp/test.txt')

# Generated at 2022-06-13 12:13:27.740057
# Unit test for method close of class Connection
def test_Connection_close():
    """
    Test case for the method close
    of the class psrp.Connection
    """
    # Execute the method by passing correct parameters
    connection_instance.close()

# Generated at 2022-06-13 12:13:28.352966
# Unit test for method close of class Connection
def test_Connection_close():
    assert True == True

# Generated at 2022-06-13 12:13:29.366946
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass


# Generated at 2022-06-13 12:13:37.579381
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    import io

    mock_io = io.BytesIO(b"test\n")
    out_path = u"C:\\Temp\\test.txt"

    # mock the psrp client and connection objects
    psrp_client_mock = mock.MagicMock(spec=pypsrp.client.Client)
    psrp_client_mock.protocol_version = '2.2'
    psrp_client_mock.run.side_effect = [
        b"5",  # save-string cmdlet will return the number of bytes written if errorlevel=0
        b"0",  # get-process cmdlet will return errorlevel=0 if successful
        b""  # close cmdlet returns nothing
    ]
    psrp_conn_mock = mock.MagicMock(spec=Connection)
   

# Generated at 2022-06-13 12:13:59.049920
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    """
    Test put_file.
    """
    connection = Connection()
    connection.put_file(in_path='test', out_path='test', mode='test')


# Generated at 2022-06-13 12:13:59.977809
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pytest.skip()



# Generated at 2022-06-13 12:14:06.235250
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():

    conn = Connection(None)
    # Populate the remote path and local path for file transfer
    remote_path = "/c/Users/Administrator/Desktop/Ansible/ansible/inventory/Hosts/hosts"
    local_path = "./hosts"
    conn.fetch_file(remote_path, local_path)
    # Check if the file is transferred properly or not
    assert os.path.isfile(local_path), "PSRP connection not able to fetch file"

if __name__ == "__main__":
    test_Connection_fetch_file()

# Generated at 2022-06-13 12:14:13.047377
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    CONNECTION_CLASS = None
    mock_runner = Mock()
    mock_runner.task_vars = dict()
    mock_runner.task_vars['ansible_psrp_server'] = 'MOCK_PSRP_HOST'
    mock_runner.task_vars['ansible_psrp_port'] = 'MOCK_PSRP_PORT'
    mock_runner.task_vars['ansible_psrp_path'] = 'MOCK_PSRP_PATH'
    mock_runner.task_vars['ansible_psrp_username'] = 'MOCK_USERNAME'
    mock_runner.task_vars['ansible_psrp_password'] = 'MOCK_PASSWORD'

# Generated at 2022-06-13 12:14:22.459147
# Unit test for method reset of class Connection
def test_Connection_reset():
    def test_impl():
        from __main__ import display
        # Create a random tmp_path
        tmp_path = 'tmp_path'
        # Create a random value for self.runspace
        self_runspace = 'self_runspace'
        # Create a random value for self.protocol
        self_protocol = 'self_protocol'
        # Create a random value for self.shell_id
        self_shell_id = 'self_shell_id'

        connection = psrp_connection.Connection(display, tmp_path)
        connection.reset()

        assert connection.runspace == None
        assert connection.protocol == self_protocol
        assert connection.shell_id == self_shell_id

    def return_none():
        return

    psrp_connection.reset = return_none
    psrp

# Generated at 2022-06-13 12:14:27.962961
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from ansible.errors import AnsibleError
    from io import BytesIO, StringIO
    from ansible.module_utils.six.moves import StringIO
    import ansible.utils.psrp.protocol.https as https
    import ansible.utils.psrp.protocol.http as http
    import ansible.utils.psrp.protocol.wsman as wsman
    
    # Set up mock FSM
    fsm = mock.MagicMock()
    fsm.state = RunspacePoolState.OPENED
    fsm.id = 1
    
    # Set up mock PowerShell
    powerShell = mock.MagicMock()
    powerShell.invoke.return_value = 0
    powerShell.streams.error = []
    powerShell.output = []

# Generated at 2022-06-13 12:14:39.233958
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    connection.close()
    with pytest.raises(AnsibleConnectionFailure):
        connection.exec_command('hostname')
    connection.reset()
    connection.exec_command('hostname')
    with pytest.raises(AnsibleConnectionFailure):
        connection.exec_command('')
    connection.close()
    with pytest.raises(AnsibleConnectionFailure):
        connection.exec_command('hostname')
    connection.reset()
    connection.exec_command('hostname')
    with pytest.raises(AnsibleConnectionFailure):
        connection.exec_command('')
    connection.close()
    with pytest.raises(AnsibleConnectionFailure):
        connection.exec_command('hostname')
    connection.close()

# Generated at 2022-06-13 12:14:39.896528
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass

# Generated at 2022-06-13 12:14:41.968109
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    connection.reset()

    with pytest.raises(AttributeError):
        connection.runspace



# Generated at 2022-06-13 12:14:49.577226
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()

    # Test with no parameters
    connection.reset()
    assert connection._psrp_protocol == 'http'
    assert connection._psrp_port == 5985
    assert connection._psrp_cert_validation is True
    assert connection._psrp_message_encryption == 'auto'
    assert connection._psrp_auth == 'basic'
    assert connection._psrp_configuration_name == 'Microsoft.PowerShell'
    assert connection._psrp_operation_timeout == 5
    assert connection._psrp_max_envelope_size == 153600
    assert connection._psrp_reconnection_retries is None
    assert connection._psrp_reconnection_backoff is None
    assert connection._psrp_certificate_key_pem is None

# Generated at 2022-06-13 12:15:27.719470
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection(path=None, port=None)
    # TODO: Add more tests
    assert True

# Generated at 2022-06-13 12:15:29.205038
# Unit test for method close of class Connection
def test_Connection_close():
    from ansible.plugins.connection import Connection
    con = Connection()
    con.close()

# Generated at 2022-06-13 12:15:45.683250
# Unit test for method reset of class Connection

# Generated at 2022-06-13 12:15:46.903302
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # connection = Connection()
    # assert False # TODO: implement your test here
    return


# Generated at 2022-06-13 12:15:49.627626
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection()
    try:
        connection.exec_command("cmd", "arg1", "arg2")
    except Exception:
        pass

# Generated at 2022-06-13 12:15:58.479823
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    script = '$data = Get-Content -Encoding Byte -ReadCount 0 -TotalCount %d -Raw -Path "%s";' \
             'Write-Output ([System.Convert]::ToBase64String($data))'

    # connection.runspace has not been initialized, so that the assertEqual test case failed.
    if connection.runspace is None:
        connection.runspace = RunspacePool()
    rc, stdout, stderr = connection._exec_psrp_script(script % (100, 'c:/temp/b'))
    assert rc

# Generated at 2022-06-13 12:16:03.817588
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection(play_context=None, new_stdin=None)
    result = connection.reset(conn=None)
    assert result is None
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None

# Generated at 2022-06-13 12:16:14.427713
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    psrp_conn = Connection(None)
    psrp_conn.runspace = (123,456)
    psrp_conn.host = Host(None)
    psrp_conn.host.ui = PSRPConsoleUi()
    psrp_conn._read_script = "read_script"
    psrp_conn._psrp_host = "1.1.1.1"
    psrp_conn._exec_psrp_script = MagicMock()
    psrp_conn.fetch_file("in_remote_path","out_local_path")
    psrp_conn._exec_psrp_script.assert_called_with("open_script", None, True, None)

# Generated at 2022-06-13 12:16:17.779071
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection()
    assert conn.put_file == None


# Generated at 2022-06-13 12:16:25.702265
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection(None)
    connection._connected = True
    connection._psrp_host = 'x'
    connection._psrp_user = 'x'
    connection._psrp_pass = 'x'
    connection._psrp_protocol = 'x'
    connection._psrp_port = 5986
    connection._psrp_path = 'x'
    connection._psrp_auth = 'x'
    connection._psrp_cert_validation = True
    connection._psrp_connection_timeout = 1
    connection._psrp_read_timeout = 1
    connection._psrp_message_encryption = 'x'
    connection._psrp_proxy = 'x'
    connection._psrp_ignore_proxy = True

# Generated at 2022-06-13 12:17:39.688050
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection(None)

    # TODO: initialise values for test
    conn.runspace = None
    conn.host = None

    # TODO: add test statements


# Generated at 2022-06-13 12:17:47.734716
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    mock_psrp_version = MagicMock()
    mock_psrp_version.return_value = '1.0.0'
    mock_psrp_version.feature_set = MagicMock()
    mock_psrp_version.feature_set.return_value = 0
    mock_psrp_version.feature_set_has_value = MagicMock()
    mock_psrp_version.feature_set_has_value.return_value = False

    mock_powershell_host = MagicMock(spec=BaseHost)
    mock_powershell_host.ui = MagicMock()
    mock_powershell_host.ui.stderr = []
    mock_powershell_host.ui.stdout = []
    mock_powershell_host.rc = 0


# Generated at 2022-06-13 12:17:58.467781
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Invoke method
    ans = Connection()
    ans.runspace = pypsrp.runspace.RunspacePool(ans.psrp_conn)

    with patch('pypsrp.client.Client') as mock_Client:
        with patch('pypsrp.wsman.WSMan') as mock_WSMan:
            mock_WSMan.return_value.create_runspace_pool.return_value = \
                pypsrp.runspace.RunspacePool(mock_Client.return_value)
            mock_WSMan.return_value.create_runspace_pool.return_value.open.return_value = None
            ans._exec_psrp_script = MagicMock(return_value=(0, '', ''))
            ans.fetch_file('in_path','out_path')
	

# Generated at 2022-06-13 12:18:03.122871
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from io import BytesIO
    connection = Connection()
    connection.put_file('test.json', BytesIO(b'{"test": [1, 2, 3]}'))
    stats = os.stat('test.json')
    assert stats.st_size == 23

# Generated at 2022-06-13 12:18:05.554208
# Unit test for method reset of class Connection
def test_Connection_reset():
    mocker = Mocker()
    con = Connection({})
    mocker.replay()
    con.reset()
    con.close()
    assert not con._connected

# Generated at 2022-06-13 12:18:10.002254
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection(play_context=None)

    with pytest.raises(AnsibleError):
        conn.fetch_file('source', 'dest')

# Generated at 2022-06-13 12:18:23.685268
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    mock_module = AnsibleModule(argument_spec={})
    setattr(mock_module, '_psrp_host', 'my_host')
    connection._exec_psrp_script.return_value = (0, '123', '')
    with patch('tempfile.NamedTemporaryFile', mock_open()) as m:
        connection.fetch_file('in_path', 'out_path', tmp='tmp_path',
                              enforce_extras=False)
        m.assert_called_once_with(delete=False, dir='tmp_path')
        connection._exec_psrp_script.assert_has_calls(
            [call(read_script % 0), call("$fs.Close()")], any_order=False)



# Generated at 2022-06-13 12:18:30.492679
# Unit test for method reset of class Connection
def test_Connection_reset():
	base_dir = 'tests'
	mock_dir = os.path.join(base_dir, 'mock_objects')
	modules_path = os.path.join(base_dir, 'modules')
	module_utils_path = os.path.join(base_dir, 'module_utils')

	args = argparse.Namespace()
	args.module_path=None
	args.connection='psrp'
	args.remote_user='Administrator'
	args.private_key_file=None
	args.timeout=10
	args.remote_pass=None
	args.remote_port=None
	args.no_log=False
	args.connection_timeout=30
	args.force_handlers=False
	args.become=False
	args.become_user=None

# Generated at 2022-06-13 12:18:31.718952
# Unit test for method reset of class Connection
def test_Connection_reset():
  conn = Connection('http://localhost', 'vagrant', 'vagrant')
  conn.reset()

# Generated at 2022-06-13 12:18:37.776617
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    test_db = [
        {
            'connection':
                Connection(
                    module_args=dict(
                        ansible_connection='winrm',
                        ansible_host='localhost',
                        ansible_port=5985,
                        ansible_user='vagrant',
                        ansible_password='vagrant',
                        ansible_winrm_transport='plaintext',
                    )),
            'files': [{
                'in_path': 'c:\\unittest_file.txt',
                'out_path': '/tmp/unittest_file.txt',
            }],
        },
    ]
    for test_case in test_db:
        test_connection = test_case['connection']
        test_connection.connect()
        for test_file in test_case['files']:
            test_connection.f

# Generated at 2022-06-13 12:21:06.946561
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file_script = """
    $url = "%s"
    $target = "%s"
    $wc = New-Object System.Net.WebClient
    $wc.UseDefaultCredentials = $true
    $wc.DownloadFile($url, $target)
    """

# Generated at 2022-06-13 12:21:16.042267
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    try:
        # Initialize the Fixture for Connection
        connection = Connection()
        # Setup Mock for MockAddHostInfo()
        _setup_mock_for_mockaddhostinfo(connection)
        # Setup Mock for MockGetOption()
        _setup_mock_for_mockgetoption(connection)
        # Setup Mock for MockConnect()
        _setup_mock_for_mockconnect(connection)
        # Initialize the Fixture for PlayContext
        play_context = PlayContext()

        # Call fetch_file()
        connection.fetch_file('file', 'local_out_file')

    except Exception as e:
        assert False



# Generated at 2022-06-13 12:21:26.784161
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
	from ansible.errors import AnsibleError
	from ansible.module_utils._text import to_native
	from pypsrp.exceptions import RunspacePoolState
	from pypsrp.wsman.transport import AuthMethod
	from pypsrp.wsman.transport import OperationTimeoutError
	from pypsrp.wsman.transport import ReconnectionRetriesError
	from pypsrp.wsman.transport import SSLValidationError
	from pypsrp.wsman.transport import WinRMTransportError
	from pypsrp.wsman.transport import WinRMOperationTimeoutError
	connection = Connection()
	connection._psrp_host = '127.0.0.1'
	connection.psrp_protocol = 'https'
	connection.psrp_port

# Generated at 2022-06-13 12:21:34.505127
# Unit test for method reset of class Connection
def test_Connection_reset():
    from __main__ import display
    import pypsrp
    # set up object
    c = Connection(display)
    c.accelerate = None
    c._psrp_host = None
    c._psrp_user = None
    c._psrp_pass = None
    c._psrp_protocol = None
    c._psrp_port = None
    c._psrp_path = None
    c._psrp_auth = None
    c._psrp_cert_validation = None
    c._psrp_connection_timeout = None
    c._psrp_read_timeout = None
    c._psrp_message_encryption = None
    c._psrp_proxy = None
    c._psrp_ignore_proxy = None
    c._psr

# Generated at 2022-06-13 12:21:39.026100
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection_psrp_mock = {
        'reset.return_value': None,
        'close.return_value': None
    }
    connection_mock = MagicMock()
    connection_mock.configure_mock(**connection_psrp_mock)

    with patch('ansible.plugins.connection.psrp.Connection', connection_mock):
        pc = Connection(play_context=dict(remote_addr='127.0.0.1'), new_stdin=None)
        pc.reset()

        connection_mock.close.assert_called_once_with()
        connection_mock.reset.assert_called_once_with()


# Generated at 2022-06-13 12:21:50.463382
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    # Create an instance of class Connection to test
    connection = Connection()

    # test with invalid/empty command parameter
    result = connection.exec_command(command=None)
    assert result[0] == 1
    assert result[1] is None
    assert result[2].startswith("parameter command cannot be None")

    result = connection.exec_command(command='')
    assert result[0] == 1
    assert result[1] is None
    assert result[2].startswith("parameter command cannot be empty")


    # test with invalid/empty executable parameter
    result = connection.exec_command(command='Get-ChildItem', executable=None)
    assert result[0] == 1
    assert result[1] is None
    assert result[2].startswith("parameter executable cannot be None")

    result = connection

# Generated at 2022-06-13 12:21:51.083213
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass

# Generated at 2022-06-13 12:21:58.860131
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection(None, None, run_async=False)
    conn.runspace = None
    conn.runspace = RunspacePool()
    conn.runspace.remote_host = 'L-CCH00758597D.corp.microsoft.com'
    conn.runspace.remote_port = 5985
    conn.runspace.message_encryption = True
    conn.runspace.transport = SessionTransport(USERNAME, PASSWORD)
    conn.runspace.open()
    file_stat_obj = FileStat(conn, '/home/ansible/test_psrp/test.txt')
    conn.fetch_file('/home/ansible/test_psrp/test.txt', '/home/ansible/test_psrp/test.txt')
    conn.close()
# Unit test

# Generated at 2022-06-13 12:22:04.192167
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection_psrp = Connection('psrp')
    connection_psrp.reset()

    assert connection_psrp._connected is False
    assert connection_psrp.runspace is None
    assert connection_psrp.get_option('protocol') is None
    assert connection_psrp.get_option('remote_addr') is None
    assert connection_psrp.get_option('remote_password') is None
    assert connection_psrp.get_option('remote_user') is None
    assert connection_psrp._psrp_conn_kwargs == {}


# Generated at 2022-06-13 12:22:15.502916
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Test fixture:
    conn = Connection()
    conn.shell = Mock()
    conn.shell.runspace_id = 0
    conn.shell._invoke = Mock()
    conn.remote_addr = 'localhost'
    conn.remote_user = 'admin'
    conn.remote_password = 'password'
    conn.protocol = 'https'
    conn.port = 5985
    conn.credssp_disable_tlsv1_2 = True
    conn._build_kwargs = Mock()
    conn._build_kwargs.return_value = None
    conn._exec_psrp_script = Mock()
    conn._exec_psrp_script.return_value = (0, 'stdout', 'stderr')
    command = 'dir'

    # Test execution:
    rc, stdout, st
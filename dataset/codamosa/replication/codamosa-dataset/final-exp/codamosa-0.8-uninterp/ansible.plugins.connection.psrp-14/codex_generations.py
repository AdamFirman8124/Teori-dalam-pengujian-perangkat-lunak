

# Generated at 2022-06-13 12:12:47.328626
# Unit test for method fetch_file of class Connection

# Generated at 2022-06-13 12:12:53.871175
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    connection = psrp.Connection('ansible', 'ansible', 'ansible', 'ansible','ansible','ansible','ansible','ansible','ansible','ansible','ansible')
    test_suite.addTest(unittest.makeSuite(test_Connection_fetch_file.test_Connection_fetch_file))
    runner.run(test_suite)


# Generated at 2022-06-13 12:13:02.177594
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:13:13.278694
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    args = {}
    obj = Connection(args)

    # Test with proper parameters
    obj.runspace = Mock(**{'state': 'OPENED'})
    obj._psrp_host = 'localhost'
    b_in_path = to_bytes(b"some_path")
    b_out_path = to_bytes(b"/some/other/path")
    b_module_path = to_bytes(b"/some/module/path")
    args2 = {'module_utils': Mock(**{'_get_module_path.return_value': b_module_path}), '_exec_psrp_script.return_value': (0, b"", b""), '_build_kwargs.return_value': None}

# Generated at 2022-06-13 12:13:14.301230
# Unit test for method reset of class Connection
def test_Connection_reset():
    conn = Connection()
    conn.reset()
    assert True


# Generated at 2022-06-13 12:13:21.181539
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    host = Connection()
    in_path = ''
    out_path = ''
    force = True
    try:
        host.fetch_file(in_path,out_path,force)
        assert(False)
    except Exception as e:
        assert(True)

if __name__ == '__main__':
    test_Connection_fetch_file()

# Generated at 2022-06-13 12:13:21.976948
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    assert True

# Generated at 2022-06-13 12:13:32.233130
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # set input for the method call
    script = 'Get-Process'
    use_local_scope = True
    arguments = None

    # call the method being tested
    psrp.Connection._exec_psrp_script(script, use_local_scope, arguments)

if __name__ == "__main__":
    # unit test execution code
    args = sys.argv
    del args[0]
    if args[0] == 'test_Connection_exec_command':
        test_Connection_exec_command()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-13 12:13:38.561722
# Unit test for method close of class Connection
def test_Connection_close():
	hostname = "localhost"
	username = "root"
	password = "root"
	port = 5986
	proto = 'https'
	connection = Connection(host=hostname, user=username, port=port, password=password, protocol=proto)
	assert connection.runspace is None
	assert connection._connected == False
	assert connection._last_pipeline == None
	connection.close()
	assert connection.runspace == None
	assert connection._connected == False
	assert connection._last_pipeline == None


# Generated at 2022-06-13 12:13:39.655525
# Unit test for method reset of class Connection
def test_Connection_reset():
    a = get_test_connection()
    a.reset()


# Generated at 2022-06-13 12:14:06.736525
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    remote_addr = None
    remote_user = None
    protocol = None
    remote_password = None
    look_for_keys = None
    port = None
    private_key_file = None
    connection = Connection(remote_addr, remote_user, protocol, remote_password, look_for_keys, port, private_key_file)
    src = None
    dest = None
    connection._psrp_host = None
    connection._psrp_user = None
    connection._psrp_pass = None
    connection._psrp_protocol = None
    connection._psrp_port = None
    connection._psrp_path = None
    connection._psrp_auth = None
    connection._psrp_cert_validation = None
    connection._psrp_connection_timeout = None
   

# Generated at 2022-06-13 12:14:09.865395
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    :return:
    """
    file = 'C:/Users/Lena/Desktop/test.txt'
    dest = 'C:/Users/Lena/Desktop/test_out.txt'
    fetch_file(file, dest, use_module=True)
 

# Generated at 2022-06-13 12:14:20.277784
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    runspace = RunspacePoolState.OPENED
    ps = PowerShell(runspace)
    pipeline = pipeline.runspace = runspace
    pipeline.state = PSInvocationState.RUNNING
    pipeline.output = ['[1,2,3]']
    pipeline.streams.error = [error]
    pipeline.had_errors = True
    pipeline.add_script(script)
    pipeline.add_script(script, use_local_scope=True)
    pipeline.add_argument(arg)
    pipeline.input = input_data
    pipeline.invoke(input=input_data)
    connection = Connection(None)
    assert connection.runspace == runspace
    assert connection.runspace.state == runspace.state
    assert connection.runspace.id == runspace.id
    assert connection._last_pipeline == pipeline

# Generated at 2022-06-13 12:14:27.390919
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    '''
    Test Connection._fetch_file() method with input parameters and expected results
    :return:
    '''
    _psrp_host = "test_psrp_host"
    _psrp_user = "test_psrp_user"
    _psrp_pass = "test_psrp_pass"
    _psrp_protocol = "test_psrp_protocol"
    _psrp_port = "test_psrp_port"
    _psrp_path = "test_psrp_path"
    _psrp_auth = "test_psrp_auth"
    _psrp_cert_validation = "test_psrp_cert_validation"

# Generated at 2022-06-13 12:14:28.240729
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    Connection.fetch_file()

# Generated at 2022-06-13 12:14:39.607900
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:14:48.028587
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Setup
    options = MagicMock()
    options.connection = 'psrp'
    options.persistent_command_timeout = 10
    options.remote_addr = 'test_host'
    options.remote_user = 'test_user'
    options.remote_password = 'test_password'
    options.port = 0
    options.connection_timeout = 30
    options.read_timeout = 0
    options.cert_validation = None
    options.ca_cert = None
    options.message_encryption = None
    options.proxy = None
    options.ignore_proxy = None
    options.operation_timeout = None
    options.max_envelope_size = None
    options.configuration_name = None
    options.reconnection_retries = 0
    options.reconnection_backoff = None
   

# Generated at 2022-06-13 12:14:52.370597
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    with open(PATH_TO_TEST_FILE, 'rb') as test_file:
        data = test_file.read()
    connection.put_file(PATH_TO_REMOTE_TEST_FILE, data)
    connection.close()


# Generated at 2022-06-13 12:14:54.081911
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    with pytest.raises(TypeError):
        Connection.put_file()


# Generated at 2022-06-13 12:14:56.770488
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    print ("Testing Connection.fetch_file()")
    
    
    
    
if __name__ == '__main__':
    test_Connection_fetch_file()

# Generated at 2022-06-13 12:15:43.548786
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # set up object
    test_conn = Connection()

    # set up mocks
    test_conn.runspace = Mock(spec=RunspacePool)
    test_conn.host = Mock(spec=AnsibleHost)
    test_input_data = 'data'

    # define test values
    test_runspace_id = 36029
    test_script = 'Script'
    test_rc = 0
    test_stdout = 'STDOUT'
    test_stderr = 'STDERR'

    # define mock behavior
    type(test_conn.runspace).id = PropertyMock(return_value=test_runspace_id)
    type(test_conn)._exec_psrp_script = Mock(return_value=(test_rc, test_stdout, test_stderr))

    # execute test
   

# Generated at 2022-06-13 12:15:51.808516
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    global connection
    src = "/home/jjohnson/src.txt"
    remote = "/tmp/dst.txt"

    f = open(src, "w")
    f.write("Hello Ansible. This is a local src file.")
    f.close()
    
    connection.put_file(src, remote)
    connection.close()


# Generated at 2022-06-13 12:16:02.473647
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fake_module = FakeModule()
    fake_module._name = 'test'

    try:
        import unittest.mock as mock
    except ImportError:
        import mock
    psrp_mock = mock.MagicMock()
    runspace_mock = mock.MagicMock()
    runspace_pool_mock = mock.MagicMock()
    pypsrp_conn_mock = mock.MagicMock()
    pypsrp_session_mock = mock.MagicMock()
    pypsrp_shell_mock = mock.MagicMock()
    conn = Connection(fake_module, psrp=psrp_mock)
    conn._psrp_host = 'localhost'
    conn._connected = True
    conn._psrp_user = 'user'
   

# Generated at 2022-06-13 12:16:07.013932
# Unit test for method reset of class Connection
def test_Connection_reset():
    # Test a positive case: try and reset a connection
    # Arrange
    connection_mock_obj = mock.Mock(spec=Connection, psrp_options=None, runspace=None)
    # Act
    connection_mock_obj.reset()
    # Assert
    assert connection_mock_obj.remote_addr is not None

# Generated at 2022-06-13 12:16:08.632633
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    connection.reset()



# Generated at 2022-06-13 12:16:18.007752
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    Test fetch_file method of Ansible-PSRP Connection
    """
    # Second argument of the os.path.join will be stripped,
    # this is a way to simulate non-existent remote path
    # in the _psrp_path of the Connection.
    remote_file_path = os.path.join("C:\\temp\\",
                                    "nonexistent")
    local_file_path = os.path.join(tempfile.gettempdir(),
                                   "ansible.txt")
    connection = Connection(None)
    # Execute method, this should raise an exception
    with pytest.raises(Exception) as excinfo:
        connection.fetch_file(remote_file_path, local_file_path)
    assert excinfo.value.args[0] == "The remote file does not exist"

# Generated at 2022-06-13 12:16:25.760462
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    module = object()
    tmpdir = tempfile.mkdtemp()
    c = Connection(module)
    c._build_kwargs()
    c._set_transport_options()
    c._connect()
    c.runspace = pypsrp.client.RunspacePool(**c._psrp_conn_kwargs)
    c._psrp_host = 'localhost'
    in_path = 'C:/Windows/System32/WindowsPowerShell/v2.0/powershell.exe'
    out_path = '%s/powershell.exe' % (tmpdir)
    c.fetch_file(in_path, out_path)
    assert(os.path.isfile(out_path))
    shutil.rmtree(tmpdir)



# Generated at 2022-06-13 12:16:29.820959
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Tests put_file() with default arguments.
    result = pypsrp.connection.Connection().put_file(in_path="/path/to/file", out_path="/path/to/remote/file")
    assert result == True

# Generated at 2022-06-13 12:16:38.034615
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    import pytest
    mock_tqm = MagicMock()
    mock_tqm._stdout_callback = MagicMock()
    mock_inventory = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_options = MagicMock()
    mock_options.connection='psrp'
    mock_options.module_path=None
    mock_options.forks=None
    mock_options.become=None
    mock_options.become_method=None
    mock_options.become_user=None
    mock_options.check=None
    mock_options.diff=None
    mock_options.private_key_file=None
    mock_options.remote_user=None
    mock_options.timeout=None

# Generated at 2022-06-13 12:16:42.309303
# Unit test for method close of class Connection
def test_Connection_close():
    # Creating class object for testing
    con = Connection();

    # Testing if the response from the API is correct
    assert con.close() == None;


# Generated at 2022-06-13 12:18:02.608467
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    output = None

    # dummy logger
    logger = logging.Logger("dummy")
    logger.setLevel(logging.DEBUG)

    # create mock transport object with dummy logger
    transport = PSRPTransport()
    transport.logger = logger
    transport._psrp_host = 'remote_addr'


# Generated at 2022-06-13 12:18:03.695827
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass



# Generated at 2022-06-13 12:18:05.300322
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass


# Generated at 2022-06-13 12:18:16.558021
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext

    host = Host('dummy')
    pc = PlayContext()
    c = Connection(host, pc)

    # Test with present file
    out_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 12:18:24.907680
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Since this is a unit test for code within the Ansible 2.9 source code tree, we cannot use the actual
    # AnsibleModule class. The following code emulates it.
    def load_platform_subclass(cls, *args, **kwargs):
        return cls

    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            args[0]['ANSIBLE_MODULE_ARGS'] = args[2]
            self.params = args[0]

        def exit_json(self, **kwargs):
            pass

        def fail_json(self, **kwargs):
            pass

    def get_bin_path(*args, **kwargs):
        return  'powershell'


# Generated at 2022-06-13 12:18:26.220924
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = None
    try:
        assert True
    except Exception:
        pass



# Generated at 2022-06-13 12:18:30.878724
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:18:37.180713
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Arrange
    psrp_host = 'test_host'
    psrp_user = 'test_user'
    psrp_pass = 'test_pass'
    psrp_protocol = 'https'
    psrp_port = 5986
    psrp_path = 'test_path'
    psrp_auth = 'Kerberos'
    psrp_cert_validation = True
    psrp_connection_timeout = 10
    psrp_read_timeout = 20
    psrp_message_encryption = 'test_message_encryption'
    psrp_proxy = 'test_proxy'
    psrp_ignore_proxy = 'test_ignore_proxy'
    psrp_operation_timeout = 30
    psrp_max_envelope_size

# Generated at 2022-06-13 12:18:45.989722
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # TODO: Move this method in to a unit test library
    # Capture stdout and stderr to strings in order to confirm messages sent
    # to stdout and stderr.
    stdout = sys.stdout
    stderr = sys.stderr
    # Need to set these to strings for unit test to check for errors
    sys.stdout = stdout_string = StringIO()
    sys.stderr = stderr_string = StringIO()

    # Create connection and command objects
    psrp_connection = Connection(play_context='', new_stdin='', runner_queue='')

    file_spec = "c:\\temp\\test_file"
    dest = "c:\\temp\\test_file"

# Generated at 2022-06-13 12:18:49.471165
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    data = {
    "ansible_connection": "winrm",
    "ansible_host": "localhost"
   }
    c = Connection(data)
    c.exec_command('dir')

# Generated at 2022-06-13 12:21:18.893858
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection()
    filename = 'test_put.txt'
    test_file = open(filename,"w+")
    temp = "test"
    test_file.write(temp)
    test_file.close()
    file_attributes = 'attributes'
    
    # Put test file
    conn.put_file(filename,temp,file_attributes)
    rc, stdout, stderr = conn._exec_psrp_script('$content = Get-Content -Path test_put.txt',use_local_scope=False,arguments=[])
    assert(stdout == 'test')

    # Delete test file
    conn._exec_psrp_script('Remove-Item test_put.txt -Force',use_local_scope=False,arguments=[])

# Generated at 2022-06-13 12:21:25.823838
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Ensure Ansible aborts on exception
    def no_ansible_abort(x):
        raise OSError()

    fetch_file = Connection.fetch_file
    Connection.fetch_file = no_ansible_abort
    try:
        with pytest.raises(OSError):
            with patch.dict('sys.modules', {'pypsrp': mock.MagicMock(side_effect=ValueError)}):
                fetch_file('', '', '')
    finally:
        Connection.fetch_file = fetch_file

# Generated at 2022-06-13 12:21:33.656865
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    connection._build_kwargs = MagicMock()
    connection._exec_psrp_script = MagicMock(return_value=(0, '', ''))
    connection._copy_module_to_remote = MagicMock(return_value=('path/to/module'))
    connection._create_directory = MagicMock(return_value=None)
    connection._remove_file = MagicMock(return_value=None)
    connection._get_tmp_path = MagicMock(return_value='tmpdir')
    connection._write_to_file = MagicMock(return_value=None)
    connection._psrp_host = 'host'
    connection._psrp_user = 'user'
    in_path = '/path/to/file'
    out_path = '/tmp/file'

# Generated at 2022-06-13 12:21:36.623751
# Unit test for method reset of class Connection
def test_Connection_reset():
    with patch('ansible.parsing.dataloader.DataLoader') as dataloader_mock:
        with patch('ansible.inventory.Manager') as manager_mock:
            connection = windows_psrp_connection.Connection(play_context=dict(remote_addr='localhost', remote_user='Administrator'), new_stdin=None)
            connection.reset()



# Generated at 2022-06-13 12:21:40.635401
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    conn = mock.Mock()
    result = exec_command(conn, 'echo hello')
    print(result)
    assert result['rc'] == 0
    assert result['stdout'] == 'hello'

if __name__ == "__main__":
    test_Connection_exec_command()

# Generated at 2022-06-13 12:21:51.178230
# Unit test for method reset of class Connection
def test_Connection_reset():
    from ansible.runner import Runner
    from ansible.playbook import PlayBook
    from ansible.inventory import Inventory
    from ansible import callbacks
    from ansible import utils

    cb = callbacks.DefaultRunnerCallbacks()
    utils.VERBOSITY = 1
    cb.settings = utils
    inventory = Inventory(host_list='/home/nikunj/ansible/tests/inventory')


# Generated at 2022-06-13 12:21:56.554972
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    with patch(builtin_module_name + '.open'):
        with patch(builtin_module_name + '.Connection._exec_psrp_script'):
            c = Connection()
            with patch.object(c, '_exec_psrp_script') as mock_exec:
                mock_exec.side_effect = [
                    (1, '', 'error'),
                    (0, 'metadata', 'no error'),
                ]
                res = c.fetch_file('src', 'dest')
                assert res is None


# Generated at 2022-06-13 12:22:13.338233
# Unit test for method reset of class Connection

# Generated at 2022-06-13 12:22:22.413451
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    mock_loader = MagicMock()
    mock_inject = MagicMock()
    mock_display = MagicMock()
    mock_runner = MagicMock()
    mock_shell = MagicMock()
    mock_conn = MagicMock()

    with patch.multiple(PSRPClient,
                        _create_psrp_connection=DEFAULT,
                        _exec_psrp_script=DEFAULT,
                        _parse_pipeline_result=DEFAULT,
                        _build_kwargs=DEFAULT,
                        runspace=None):

        conn = PSRPClient(mock_runner, mock_shell, 'smart', 'winrm', mock_display)
        conn._build_kwargs()
        conn.runspace = Mock()
        conn.runspace.remote_host = "localhost"
        conn.runspace.remote
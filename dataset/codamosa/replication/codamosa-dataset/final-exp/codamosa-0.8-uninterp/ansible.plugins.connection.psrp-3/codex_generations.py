

# Generated at 2022-06-13 12:12:40.662972
# Unit test for method reset of class Connection
def test_Connection_reset():
  connection = Connection()
  connection.reset()
  assert connection.runspace is None
  assert connection._connected is False
  assert connection._last_pipeline is None


# Generated at 2022-06-13 12:12:47.397879
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    """
    Unit test of Connection.put_file
    """

    _test_Connection_put_file = '''test_Connection_put_file'''

    from tempfile import mkdtemp
    from shutil import rmtree
    from datetime import datetime

    b_temp_path = to_bytes(mkdtemp())
    b_temp_file = to_bytes(mkdtemp(dir=b_temp_path))
    b_temp_path = to_bytes(os.path.join(b_temp_path, b'foo'))
    b_temp_file_contents = b"hello world!\n"
    b_temp_file_contents_len = len(b_temp_file_contents)

    # create file to transfer

# Generated at 2022-06-13 12:12:50.250326
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = get_connection_mock()
    connection.reset()
    assert connection.last_pipeline is None
    if not isinstance(connection, MockConnection):
        assert connection.runspace is None
        assert not connection._connected



# Generated at 2022-06-13 12:12:59.208034
# Unit test for method fetch_file of class Connection

# Generated at 2022-06-13 12:13:02.582714
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():  # noqa: E302
    # set up and run the test
    conn = Connection()

    # jjb()
    # ensure the method returns None
    assert conn.fetch_file(None, None, None) == None



# Generated at 2022-06-13 12:13:12.492137
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    a = Connection(task_vars=dict())
    a._build_kwargs()
    a._psrp_conn_kwargs['ssl'] = False
    a._psrp_port = 5985
    a._psrp_path = '/wsman'
    a._psrp_user = 'vagrant'
    a._psrp_pass = 'vagrant'
    a._psrp_protocol = 'http'
    a._psrp_host = '192.168.33.10'
    a.connect()

    a.exec_command('echo HELLO')
    a.exec_command('echo HELLO2')
    a.exec_command('echo HELLO3')


# Generated at 2022-06-13 12:13:15.359394
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    """
    put_file() unit test
    """

    import pytest

    with pytest.raises(AnsibleError) as excinfo:
        print("test exception")
        c = Connection()
        c._exec_psrp_script("0001")
        c.put_file("", "")

# Generated at 2022-06-13 12:13:20.896175
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  # Setup test
  connection = Connection()
  connection._connected = True
  connection._psrp_protocol = 'https'
  connection._psrp_user = 'test'
  connection._psrp_pass = 'test'
  connection._psrp_port = 5986
  connection._psrp_connection_timeout = 10
  connection._psrp_operation_timeout = 10
  connection._psrp_max_envelope_size = 153600
  connection.host = RemoteHost('server')
  connection.host.transport = 'https'
  connection.host.ui = MockUI()
  connection.runspace = None

  cmd = 'ls'

  # Execute
  connection.exec_command(cmd)

  # Verify results
  pass

# Generated at 2022-06-13 12:13:29.250912
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Test module

    # Define a dict to pass
    argument_spec = dict(
        src=dict(type='str', required=True),
        dest=dict(type='str', required=True)
    )

    # Instantiate a connection
    conn = Connection(argument_spec=argument_spec, supports_check_mode=True)
    # Test it
    conn.put_file('./testfile.txt','./destfile.txt')
    assert Path('./destfile.txt').exists()
    os.remove('./destfile.txt')



# Generated at 2022-06-13 12:13:37.506133
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    temp_ps_script = os.path.join(C.DEFAULT_LOCAL_TMP, 'test.ps1')
    ps_script = """
    write-output $env:TEST_VAR
    """
    test_host = '127.0.0.1'
    with open(temp_ps_script, 'wt') as f:
        f.write(ps_script)
    result = {u'rc': 0, u'changed': False, u'stdout_lines': [u'hello'], u'stdout': u'hello\r\n', u'stderr': u''}
    monkeypatch.setenv(u'ANSIBLE_REMOTE_TEMP', C.DEFAULT_LOCAL_TMP)

# Generated at 2022-06-13 12:14:12.247013
# Unit test for constructor of class Connection
def test_Connection():
    conn = Connection(play_context=PlayContext())
    assert isinstance(conn, Connection)

# Generated at 2022-06-13 12:14:16.860652
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = create_connection()
    module_name = "path"
    module_args = "to/some/file.txt"
    timeout = 30
    executable = None

    result = connection.exec_command(module_name, module_args, timeout, executable)

    assert result is not None
    assert result == "Test script output message"


# Generated at 2022-06-13 12:14:17.830616
# Unit test for method close of class Connection
def test_Connection_close():
  c = psrp.Connection()



# Generated at 2022-06-13 12:14:20.364523
# Unit test for method reset of class Connection
def test_Connection_reset():
    '''
    Unit test for method reset of class Connection
    '''

    # Test with no parameters

    # Test with valid parameters

    # Test with invalid parameters



# Generated at 2022-06-13 12:14:22.482849
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    in_path = '' # TODO: Initialize
    out_path = '' # TODO: Initialize
    expect = None
    actual = connection.fetch_file(in_path, out_path)
    assert actual == expect


# Generated at 2022-06-13 12:14:23.382102
# Unit test for method close of class Connection
def test_Connection_close():
    conn = Connection()
    conn.close()


# Generated at 2022-06-13 12:14:31.350289
# Unit test for method reset of class Connection
def test_Connection_reset():
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 12:14:33.172931
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection(None)

    # Example call of method
    connection.reset()

# Generated at 2022-06-13 12:14:43.807369
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    class MockConnPsrp(ConnectionPsrp):

        def _exec_psrp_script(self, script, input_data=None, use_local_scope=None, arguments=None):
            return 0, 'Test stdout', 'Test stderr'
    with patch.dict(ansible_module_generated._PSRP_IMPLEMENTATION_AVAILABLE, {'pypsrp': True}):
        conn = MockConnPsrp(MagicMock())
        cmd = 'Test command string'
        cmd_result = conn.exec_command(cmd, False)
        assert cmd_result.rc == 0
        assert_equal(cmd_result._stdout.decode('utf-8'), 'Test stdout')

# Generated at 2022-06-13 12:14:49.927704
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Execute the command line specified in tmp_command and
    # compare the requested command with the actual command.

    # Create an instance of the class under test
    ansible = Connection()

    # Set the command line to be executed with the tmp_command file
    request_command = ansible._build_exec_command('findstr /M test /B foo.txt')
    with open('tmp_command', 'w') as f:
        f.write(request_command)

    # Execute the command line from the tmp_command file
    ansible._exec_command('tmp_command')

    # Compare the requested command with the actual command.
    assert ansible._command == request_command, "Requested and actual command are not equal."


# Generated at 2022-06-13 12:15:27.715406
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    connection._build_kwargs()
    connection.runspace = runspace()
    connection.runspace.state = RunspacePoolState.OPENED
    connection.close()

    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None

# Generated at 2022-06-13 12:15:28.589135
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    c = Connection()
    pass


# Generated at 2022-06-13 12:15:40.297203
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Test function exec_command of class Connection
    # Test that exec_command doesn't crash on an SSHException
    # set up a fake session and mock up the client.exec_command to raise an
    # exception.
    fake_session = FakeSession()
    fake_conn = FakeConnection(fake_session)

    fake_session.client.exec_command = Mock(side_effect=SSHException())

    try:
        fake_conn.exec_command('ls')
    except Exception as e:
        assert False, "exec_command crashed: %s" % str(e)



# Generated at 2022-06-13 12:15:42.551310
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    assert False, "Test if the method fetch_file of class Connection works."



# Generated at 2022-06-13 12:15:45.045949
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    con = Connection()
    con.exec_command('ls')



# Generated at 2022-06-13 12:15:47.853019
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    with pytest.raises(AnsibleError):
        conn = Connection(PlayContext())
        conn.put_file('src', '/dest')
        assert True

# Generated at 2022-06-13 12:15:59.074468
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    remote_addr = "test_put_file"
    remote_user = "test_put_file"
    remote_password = "test_put_file"
    protocol = "test_put_file"
    port = "test_put_file"
    path = "test_put_file"
    auth = "test_put_file"
    cert_validation = "test_put_file"
    connection_timeout = "test_put_file"
    read_timeout = "test_put_file"
    message_encryption = "test_put_file"
    proxy = "test_put_file"
    ignore_proxy = "test_put_file"
    operation_timeout = "test_put_file"
    max_envelope_size = "test_put_file"

# Generated at 2022-06-13 12:16:00.369474
# Unit test for method put_file of class Connection
def test_Connection_put_file():    
    connection = Connection()

# Generated at 2022-06-13 12:16:08.668515
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    session = Connection()
    session.runspace = None
    session._psrp_host = ''
    session.connect()
    with mock.patch("ansible_collections.notstdlib.moveitallout.plugins.connection.psrp.PSRPConnection.exec_psrp_script") as mock_exec_psrp_script:
        session.fetch_file(src="", dst="")
        mock_exec_psrp_script.assert_any_call(read_script % 0)
        session.fetch_file(src="", dst="", offset=0)
        mock_exec_psrp_script.assert_called()

# Generated at 2022-06-13 12:16:12.073180
# Unit test for method close of class Connection
def test_Connection_close():
    # Make an instance of class Connection
    connection = Connection()
    # Test if instance is of class Connection
    assert isinstance(connection, Connection)
    # Test close method
    assert connection.close() is None


# Generated at 2022-06-13 12:16:54.110798
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    fetch_file method of Connection class
    """
    # Remove if the target method is an instance method
    args = []
    # Establish a mock "builtins" module
    builtins_name = 'builtins'
    if builtins_name in sys.modules:
        builtins = sys.modules[builtins_name]
    else:
        builtins = types.ModuleType(builtins_name)
        sys.modules[builtins_name] = builtins
    # Set up the desired outputs
    builtins.open = MagicMock(name='open', side_effect=test_fetch_file_open)
    connection = Connection()
    result = connection.fetch_file(*args, **{})
    assert result == 'value'


# Generated at 2022-06-13 12:16:54.998455
# Unit test for method close of class Connection
def test_Connection_close():
    pass

# Generated at 2022-06-13 12:16:57.760553
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # FIXME: The test does nothing, it just checks if the method exists
    pass


# Generated at 2022-06-13 12:17:14.169337
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    host = '127.0.0.1'
    port = 5985
    user = 'ansible'
    password = 'password'
    configuration_name = None
    connection_timeout = 30
    read_timeout = None
    cert_validation = True
    message_encryption = 'auto'
    proxy = None
    ignore_proxy = False
    operation_timeout = None
    max_envelope_size = 153600
    reconnection_retries = 5
    reconnection_backoff = 5.0
    certificate_key_pem = None
    certificate_pem = None
    credssp_auth_mechanism = 'negotiate'
    credssp_disable_tlsv1_2 = False
    credssp_minimum_version = None
    negotiate_send_cbt = None
    negotiate

# Generated at 2022-06-13 12:17:28.601956
# Unit test for method reset of class Connection
def test_Connection_reset():
    from collections import namedtuple
    from ansible.parsing.plugin_docs import read_docstring


# Generated at 2022-06-13 12:17:39.242299
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    _connection = Connection()
    _connection._exec_psrp_script = MagicMock(return_value=(0,b"some data",b"some error"))
    _in_path = "some_input_file_path"
    _out_path = "some_output_file_path"
    _buffer_size = 5
    _connection.fetch_file(_in_path, _out_path, buffer_size=_buffer_size)
    _call_args_list = _connection._exec_psrp_script.call_args_list
    assert _call_args_list[0][0][0] == "$fs = new-Object IO.FileStream(\\\"%s\\\", [System.IO.FileMode]::Open);" % _in_path 

# Generated at 2022-06-13 12:17:47.414587
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    conn = Connection()
    assert conn.exec_command.__name__ == "exec_command"

    # Test with default args
    conn.protocol = "https"
    conn.host = "123.123.123.123"
    conn.username = "username"
    conn.password = "password"
    conn.port = 5986
    res = conn.exec_command(command="Get-Process")
    assert len(res) == 3
    for item in res:
        assert len(item) > 0

    # Test with default args and stdin
    conn.protocol = "http"
    conn.host = "123.123.123.123"
    conn.username = "username"
    conn.password = "password"
    conn.port = 5985

# Generated at 2022-06-13 12:17:54.130768
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    args = dict(
        host='localhost',
        port=5986,
        user='Administrator',
        password='Password123!',
    )

    # connection = psrp.Connection(**args)

    command = 'ipconfig /all'
    rc, stdout, stderr = connection.exec_command(command)

    print(rc)
    print(to_bytes(stdout))
    print(to_bytes(stderr))

# Generated at 2022-06-13 12:17:55.506488
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    connection.put_file("foo")



# Generated at 2022-06-13 12:17:56.197203
# Unit test for method close of class Connection
def test_Connection_close():
	pass

# Generated at 2022-06-13 12:19:03.053751
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection_reset()

# Generated at 2022-06-13 12:19:08.451578
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    psrp_host = 'winhost'
    psrp_port = 5986
    psrp_protocol = 'https'
    psrp_path = 'wsman'
    psrp_auth = 'CredSSP'
    psrp_cert_validation = True
    psrp_connection_timeout = 15
    psrp_read_timeout = 30
    psrp_message_encryption = 'Always'
    psrp_ignore_proxy = False
    psrp_operation_timeout = 0
    psrp_max_envelope_size = 153600
    psrp_credssp_auth_mechanism = 'Negotiate'
    psrp_credssp_disable_tlsv1_2 = False
    psrp_credssp

# Generated at 2022-06-13 12:19:18.096139
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    connection._connected = True
    connection._psrp_host = "192.168.1.1"
    connection._psrp_protocol = "http"
    connection._psrp_port = 5985
    connection._psrp_path = "/wsman"
    connection._psrp_user = "admin"
    connection._psrp_pass = "fakepass"

    from ansible.parsing.utils.addresses import parse_address
    connection._shell = None
    connection._play_context = PlayContext()
    display.verbosity = 4
    connection._play_context.port = 5985
    connection._play_context.remote_addr = parse_address("192.168.1.1", port=None)
    connection._connected = True


# Generated at 2022-06-13 12:19:28.917198
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
#        fetch_file(self, in_path, out_path, file_size, buffer_size=16384):
    write_file = "w+"
    read_file = "r"
    # Test with fetching a file that does not exist

# Generated at 2022-06-13 12:19:29.860328
# Unit test for method close of class Connection
def test_Connection_close():
    pass

# Generated at 2022-06-13 12:19:31.208672
# Unit test for method close of class Connection
def test_Connection_close():
    aa=Connection()
    print(aa)

# Generated at 2022-06-13 12:19:37.844942
# Unit test for method close of class Connection
def test_Connection_close():
    '''
    Unit test for method close of class Connection
    '''
    for case_name, case in TEST_CASES['close'].items():
        connection = Connection(None, case.get('connection', None))
        connection.close()
        expected_result = case.get('expected_result', {})
        assert connection.runspace is expected_result.get('runspace', None)
        assert connection._connected is expected_result.get('_connected', None)
        assert connection._last_pipeline is expected_result.get('_last_pipeline', None)


# Generated at 2022-06-13 12:19:40.793525
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Initializing the variables for: Connection.fetch_file
    connection_class_instance = Connection()
    source = "test_source"
    destination = "test_destination"
    flat = True
    connection_class_instance.fetch_file(source,destination,flat=flat)



# Generated at 2022-06-13 12:19:47.378974
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Create a dummy object
    # Use patch to mock object.method
    # Assert that method returns correct value
    # Assert that correct method is called on object
    # Assert that correct method is called on mock
    # Assert implementation
    obj = Connection()
    with pytest.raises(Exception) as excinfo:
        obj.exec_command("")
    assert 'Not implemented' in str(excinfo.value)
    with patch.object(Connection, 'exec_command', return_value='Hello') as mock_method:
        assert mock_method('arg') == 'Hello'
        assert Connection.exec_command.called
        assert mock_method.called
        assert mock_method.call_args == call('arg')
        assert Connection.exec_command.call_args == call('arg')

# Generated at 2022-06-13 12:19:53.435487
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file_src_args = [
        'ansible_connection: psrp',
        'ansible_psrp_server: "{{ ansible_psrp_server }}"',
        'ansible_user: "{{ ansible_user }}"',
        'ansible_password: "{{ ansible_password }}"',
        'delegate_to: 127.0.0.1',
        'vars:'
         ]

    fetch_file_src_args_yaml = ''.join(fetch_file_src_args)

    fetch_file_dest_args = ['src: C:\\Users\\fakeuser\\Documents\\fileoutput.txt',
                            'dest: /home/fakeuser/Documents/fileoutput.txt',
                            'mode: 0600']

    fetch_file_dest_args_y

# Generated at 2022-06-13 12:22:08.743733
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection=Connection()
    connection.host="127.0.0.1"
    connection.port=5985
    connection.user="Administrator"
    connection.password="Passw0rd!"

# Generated at 2022-06-13 12:22:11.554367
# Unit test for method reset of class Connection
def test_Connection_reset():
    mock_connection = _setup_mock_connection()
    mock_connection.reset()
    assert mock_connection._connected == False and mock_connection.runspace == None


# Generated at 2022-06-13 12:22:16.015984
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection('psrp')
    command = "pwd"
    rc, stdout, stderr = connection.exec_command(command)
    assert rc == 0
    assert stdout != ""
    assert stderr == ""


# Generated at 2022-06-13 12:22:20.419024
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection(None, None)
    connection._psrp_conn = None
    rc, stdout, stderr = connection.exec_command("dir c:")
    assert rc == 0
    assert stdout != None
    assert stderr != None
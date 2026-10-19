

# Generated at 2022-06-13 12:12:43.458748
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    con = Connection(play_context=play_context)
    con._connected = True
    con._build_kwargs()
    con.runspace = RunspacePool(con.psrp_client, host=con.host)
    con.runspace.open()
    con.protocol = 'psrp'
    rc, stdout, stderr = con.exec_command('echo hello')
    print(rc)
    print(stdout)
    print(stderr)

# Generated at 2022-06-13 12:12:44.272760
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    pass

# Generated at 2022-06-13 12:12:45.065297
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    pass

# Generated at 2022-06-13 12:12:46.650417
# Unit test for method reset of class Connection
def test_Connection_reset():
    # init a test obj
    c = Connection()
    # call the method
    c.reset()

# Generated at 2022-06-13 12:12:54.279728
# Unit test for method close of class Connection
def test_Connection_close():
    model = '''
{
  "__ansible_module__": "psrp",
  "__ansible_arguments__": "echo 'Hello World'",
  "__ansible_play_hosts__": "localhost",
  "ansible_connection": "psrp",
  "ansible_play_batch": "0",
  "ansible_play_hosts_all": [
    "localhost"
  ]
}
'''
    job = job_template.JobTemplate('localhost', json.loads(model))
    psrp = psrp_connection.Connection(job._play_context, job.extras)
    ret_value = psrp.close()
    assert ret_value is None



# Generated at 2022-06-13 12:13:01.120608
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Initializing mock for Connection
    mock_Connection = mock.MagicMock()
    mock_psrp_host = "mock_psrp_host"
    mock_in_path = "mock_in_path"
    mock_out_path = "mock_out_path"

    print(mock_in_path)
    print(mock_out_path)


    # Calling method with required args
    # Connection.put_file(in_path, out_path)

    mock_Connection.put_file(mock_in_path,mock_out_path)


# Generated at 2022-06-13 12:13:07.826497
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    import sys
    import inspect
    import os
    import shutil
    import imp
    import tempfile
    import ansible.utils.module_docs
    import ansible.modules.psrp
    imp.reload(ansible.modules.psrp)

    # Prepend current path to module_utils
    sys.path.insert(1, os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))


# Generated at 2022-06-13 12:13:15.390070
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    filename = None
    tmpdir = None
    tmpdir_name = None
    filename_name = None
    b_in_path = None
    connection = None
    display = None
    host = None
    b_out_path = None
    
    
    
    
    # validation for the parameters
    if not isinstance(filename, (str, unicode)):
        raise Exception('"filename" parameter must be a string or unicode')
    
    
    
    
    
    
    
    
    
    
    
    
    # validation for the parameters
    if not isinstance(tmpdir, (str, unicode)):
        raise Exception('"tmpdir" parameter must be a string or unicode')
    
    # validation for the parameters

# Generated at 2022-06-13 12:13:24.144274
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
#        module = importlib.import_module("ansible.plugins.connection.psrp")
#        conn = module.Connection()
        conn = Connection()
        conn._exec_psrp_script("$test = @{test=\"testValue\"}")
        conn._exec_psrp_script("$test.test")
        #print conn._exec_psrp_script("$test.test")

# Generated at 2022-06-13 12:13:26.346407
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    test_Connection = Connection()
    test_Connection.fetch_file()

# Generated at 2022-06-13 12:13:46.544813
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # arguments for method we are testing
    args = [b'echo "hello"']

    # the code from our method

# Generated at 2022-06-13 12:13:54.444000
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    import mock
    import pytest
    from ansible.module_utils.six import StringIO
    from pypsrp.exceptions import WinRMError, RunspacePoolState

    @mock.patch.object(Connection, 'runspace')
    @mock.patch.object(Connection, 'host')
    @mock.patch.object(Connection, '_exec_psrp_script')
    def test_exec_command(mock_script, mock_host, mock_runspace):

        # mocks
        mock_runspace.state = 'OPENED'
        mock_host.ui = mock.MagicMock()
        mock_host.ui.stdout = ['ansible stdout']
        mock_host.ui.stderr = ['ansible stderr']
        mock_host.rc = 0
        mock_

# Generated at 2022-06-13 12:14:04.022929
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    fake_shell_id = 'a1b2c3'
    fake_rc = 0
    fake_stdout = u'hi out\r\nhi again'
    fake_stderr = u'hi err\r\nhi again'
    psrp_host = 'testhost'
    psrp_user = 'testuser'
    psrp_pass = 'testpass'
    psrp_protocol = 'http'
    psrp_port = 5985
    psrp_path = '/wsman'
    psrp_auth = 'basic'
    psrp_connection_timeout = None  # Can be None as we will use the default value of 30s
    psrp_read_timeout = None  # Can be None as we will use the default value of 30s
    psrp_message

# Generated at 2022-06-13 12:14:08.084230
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Establish a connection to target device using psrp.
    conn = Connection(remote_addr='10.10.10.10', remote_port=80, remote_user='Administrator', remote_pass='P@ssw0rd')
    return_val = conn.fetch_file()

    # assert that the return value is not None.
    assert return_val is not None


# Generated at 2022-06-13 12:14:11.873487
# Unit test for method reset of class Connection
def test_Connection_reset():
    mock_runspace = MagicMock(spec=RunspacePool)
    mock_runspace.state = RunspacePoolState.OPENED

    conn = Connection(MagicMock(), MagicMock())
    conn.runspace = mock_runspace

    conn.reset()

    mock_runspace.close.assert_called_once_with()
    assert conn.runspace is None
    assert conn._connected is False


# Generated at 2022-06-13 12:14:21.605475
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    params = {}
    ansible_psrp_path = os.getenv('TEST_ANSIBLE_PSRP_PATH', '/windows/system32/WindowsPowerShell/v1.0/modules/pester/3.4.0/Pester.psd1')
    params['_ansible_verbosity'] = 4
    params['_ansible_debug'] = True
    params['_ansible_socket'] = None
    params['_ansible_check_mode'] = False
    params['ansible_module_name'] = 'win_copy'
    params['ansible_psrp_configuration_name'] = 'Microsoft.PowerShell'
    params['ansible_psrp_auth'] = 'basic'
    params['ansible_psrp_cert_validation'] = 'ignore'

# Generated at 2022-06-13 12:14:27.395144
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # create a connection
    connection = Connection(1)
    # parameters for the method
    b_in_path = IS_PY2 and b'/home/vagrant/testfile.txt' or '/home/vagrant/testfile.txt'
    in_path = IS_PY2 and unicode('/home/vagrant/testfile.txt') or str('/home/vagrant/testfile.txt')
    b_out_path = IS_PY2 and b'c:\\users\\vagrant\\testfile.txt' or 'c:\\users\\vagrant\\testfile.txt'
    out_path = IS_PY2 and unicode('c:\\users\\vagrant\\testfile.txt') or str('c:\\users\\vagrant\\testfile.txt')
    buffer_size = 65536
    # invoke the

# Generated at 2022-06-13 12:14:38.417366
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    class MockCommModule(object):
        def __init__(self, parameters):
            self.params = parameters

        def __enter__(self):
            self.rc = 0

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    class MockConnection(Connection):

        def __init__(self, module, play_context, new_stdin):
            self._psrp_host = None
            self._psrp_user = None
            self._psrp_pass = None
            self._psrp_protocol = None
            self._psrp_port = None
            self._psrp_path = None
            self._psrp_auth = None
            self._psrp_cert_validation = None

# Generated at 2022-06-13 12:14:47.230758
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    module_args = dict(
            a="b",
            c="d",
            e="f",
            g="h",
            i="j",
            k="l",
            m="n",
            o="p",
            q="r",
            s="t",
            u="v",
            w="x",
            y="z",
            A="B",
            C="D",
            E="F",
            G="H",
            I="J",
            K="L",
            M="N",
            O="P",
            Q="R",
            S="T",
            U="V",
            W="X",
            Y="Z")
    p = Connection(module_args)
    assert p.get_option('a') == 'b'
    assert p.get_option('c')

# Generated at 2022-06-13 12:14:50.732677
# Unit test for method reset of class Connection
def test_Connection_reset():
    """
    Test for reset for Connection class
    """
    connection = psrp_connection()
    assert connection.reset() is None, 'Unable to reset'


# Generated at 2022-06-13 12:15:08.465156
# Unit test for method reset of class Connection
def test_Connection_reset():
    assert True == True

# Generated at 2022-06-13 12:15:14.103296
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = get_connection()
    file_name = 'DummyTestFile.txt'
    dest_file = os.path.join(tempfile.gettempdir(), file_name)
    src_file = file_utils.find_needle('tests/sanity/psrp/files/' + file_name)
    os.remove(dest_file)
    assert not os.path.exists(dest_file)
    connection.fetch_file(src_file, dest_file)
    assert os.path.exists(dest_file)
    assert filecmp.cmp(dest_file, src_file)



# Generated at 2022-06-13 12:15:23.759783
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file_args = {} # type: ignore
    fetch_file_args['self'] = None
    fetch_file_args['in_path'] = None
    fetch_file_args['out_path'] = None
    fetch_file_args['use_module'] = None
    fetch_file_args['mime'] = None
    fetch_file_args['md5sum'] = None
    # No exception should be raised
    fetch_file(**fetch_file_args)


# Generated at 2022-06-13 12:15:32.378649
# Unit test for method close of class Connection
def test_Connection_close():
    mock_get_option = MagicMock(return_value='test')
    mock_get_option.side_effect = lambda x, default=None: default
    mock_close = MagicMock()
    mock_display_vvvvv = MagicMock()
    mock_display_warning = MagicMock()
    mock_AnsibleError = MagicMock(side_effect=AnsibleError('test'))
    mock_to_native = MagicMock(return_value='native_string')
    mock_to_bytes = MagicMock(return_value=b'byte_data')
    mock_to_text = MagicMock(return_value=u'text_data')
    mock_to_unicode = MagicMock(return_value=u'unicode_data')

# Generated at 2022-06-13 12:15:43.440776
# Unit test for method reset of class Connection
def test_Connection_reset():
    c = Connection('localhost')
    c.reset()

# Generated at 2022-06-13 12:15:49.954435
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection=Connection(play_context=PlayContext())
    connection._build_kwargs()
    connection.connect()
    result = connection.exec_command('ls -la', None)
    display.display(result)
    connection.close()
    return result


# Generated at 2022-06-13 12:16:00.909203
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    Test for Connection.fetch_file
    """
    """
    Test for Connection.fetch_file
    """
    conn = Connection(play_context=play_context, new_stdin=new_stdin)
    conn.open()
    assert isinstance(conn.runspace, RunspacePool)
    conn.get()
    conn.put()
    conn.close()
    conn = Connection(play_context=play_context, new_stdin=new_stdin)
    conn.open()
    assert isinstance(conn.runspace, RunspacePool)
    conn.get()
    conn.put()
    conn.close()
    conn = Connection(play_context=play_context, new_stdin=new_stdin)
    conn.open()

# Generated at 2022-06-13 12:16:02.036294
# Unit test for method close of class Connection
def test_Connection_close():
    assert True == False


# Generated at 2022-06-13 12:16:04.900336
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from ansible.module_utils.connection import Connection
    connection = Connection()
    assert connection is not None

    result = connection.put_file('local_path', 'remote_path')
    assert result == ''



# Generated at 2022-06-13 12:16:16.058536
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    mock_psrp_host = 'MOCK_PSRP_HOST'
    mock_psrp_user = 'MOCK_PSRP_USER'
    mock_psrp_pass = 'MOCK_PSRP_PASS'
    mock_psrp_protocol = 'http'
    mock_psrp_port = 5985
    mock_psrp_path = None
    mock_psrp_auth = 'basic'
    mock_psrp_cert_validation = True
    mock_psrp_connection_timeout = None
    mock_psrp_read_timeout = None
    mock_psrp_message_encryption = 'auto'
    mock_psrp_proxy = None
    mock_psrp_ignore_proxy = False

# Generated at 2022-06-13 12:16:36.815457
# Unit test for method reset of class Connection
def test_Connection_reset():
    """
    Connection.reset()
    """
    args = {"play_context": {"verbosity": 3}, "_play_context": {"verbosity": 3}, "new_stdin": False}
    curr_conn = Connection(args)
    curr_conn.reset()
    # Test the no exception case

# Generated at 2022-06-13 12:16:38.002352
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    assert False, "Test failed"

# Generated at 2022-06-13 12:16:42.909662
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file()
# =============== BUILT-IN FUNCTION ===============
# Evaluates a string and returns an object.
# https://docs.python.org/2/library/functions.html#eval

# Generated at 2022-06-13 12:16:53.490571
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection(None)
    connection._psrp_host = '192.168.10.20'
    connection.host_output_lines = ["[stdout]", "test-file1.txt", "test-file2.txt", "test-file3.txt"]
    connection.in_filename = 'test-file1.txt'
    connection.out_path = '.'
    connection.host_rc = 0
    connection.host_stdout = ''
    connection.host_stderr = ''
    connection.host_stdin = ''
    ret = connection.fetch_file()
    assert ret == True
    assert connection.host_in_path == 'test-file1.txt'
    assert connection.out_path == 'test-file1.txt'

# Generated at 2022-06-13 12:16:56.052485
# Unit test for method reset of class Connection
def test_Connection_reset():
  """Unit test for method reset of class Connection"""
  connection = Connection()
  connection.reset()


# Generated at 2022-06-13 12:17:00.706313
# Unit test for method reset of class Connection
def test_Connection_reset():
    c = Connection()
    c.reset()

    c.exec_command("ls -la")
    c.exec_command("ls -la")
    c.reset()
    c.close()

# Generated at 2022-06-13 12:17:15.390995
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    host = 'fake_hostname'
    psrp_conn = Connection(host=host)

    input_data = "test_input"
    result_data = "test_result"
    arguments = ["-Arg1", "Arg2"]
    command_data = "test_command"
    pipeline = MagicMock()
    pipeline.invoke.return_value = None
    pipeline.output = {result_data}
    pipeline.streams.error = {}
    pipeline.had_errors = 0
    psrp_conn.runspace = MagicMock()
    psrp_conn.runspace.state = RunspacePoolState.OPENED
    psrp_conn.powershell = MagicMock()
    psrp_conn.powershell.return_value = pipeline
    psrp_conn._parse_pipeline_

# Generated at 2022-06-13 12:17:29.410751
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    my_connection = Connection()
    my_connection.runspace = RunspacePool()
    my_connection.runspace.id = 123
    my_connection.host = Host()
    my_connection.host.ui = HostUi()
    file_data = """
[
    {
        "Key": "DEFAULT",
        "Value": {
            "Enabled": true,
            "Priority": "0"
        }
    }
]
"""
    my_connection._psrp_host = "test_host"
    my_connection._psrp_user = "test_user"
    my_connection._psrp_pass = "test_pass"
    my_connection._psrp_protocol = "test_protocol"
    my_connection._psrp_port = "test_port"
    my

# Generated at 2022-06-13 12:17:33.215993
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection(None)
    command = 'echo ansible-psrp'
    execution_results = connection.exec_command(*command)
    assert execution_results == ('ansible-psrp', '', 0)

# tests for method put_file of class Connection

# Generated at 2022-06-13 12:17:40.964555
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Test the method exec_command of class Connection
    """
    psrp_options = {
        'transport': 'psrp',
        'remote_addr': "localhost",
        'path': 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe',
        'password': '',
        'username': 'user'
    }
    connection = Connection(psrp_options)
    connection._build_kwargs()
    connection.connect()
    result = connection.exec_command('echo "Hello World!"')
    print(result)


# Generated at 2022-06-13 12:18:18.108792
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    # We test Connection by calling its method reset.
    connection.reset()



# Generated at 2022-06-13 12:18:25.838183
# Unit test for method reset of class Connection
def test_Connection_reset():
  conn = Connection()
  expected = dict()
  expected['_connected'] = False
  expected['_last_pipeline'] = None
  expected['_play_context'] = None
  expected['_play_context'] = None
  expected['_shell_type'] = None
  expected['_shell_id'] = None
  expected['_shell_standby_timeout'] = None
  expected['_delegate'] = None
  expected['_play_name'] = None
  expected['_loader'] = None
  expected['_shell_output_encoding'] = 'utf-16-le'
  expected['_shell_encoding'] = None
  expected['become'] = False
  expected['become_method'] = None
  expected['become_user'] = None
  expected['become_pass'] = None

# Generated at 2022-06-13 12:18:32.449617
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
	dest_dir = ".\\.test_data"
	# 1st test, in_path and out_path are all file path
	in_path = ".\\.test_data\\file1.txt"
	out_path = ".\\.test_data\\file1_test.txt"
	if os.path.exists(in_path):
		os.remove(in_path)
	if os.path.exists(out_path):
		os.remove(out_path)
	fout = open(in_path, "w")
	fout.write("This is line1.\n")
	fout.write("This is line2.\n")
	fout.write("This is line3.\n")
	fout.close()


# Generated at 2022-06-13 12:18:38.283786
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Test setup
    protocol = 'https'
    port = int(5986)
    server = '127.0.0.1'
    username = 'adamr'
    password = 'adamr'
    connection_timeout = int(30)
    read_timeout = int(30)
    psrp_path = ''
    psrp_cert_validation = False
    psrp_message_encryption = False
    psrp_proxy = None
    psrp_ignore_proxy = False
    psrp_operation_timeout = int(0)
    psrp_max_envelope_size = int(153600)
    psrp_auth = 'Negotiate'

# Generated at 2022-06-13 12:18:44.198911
# Unit test for method close of class Connection
def test_Connection_close():
    connection = pysrp.PSRP(None)
    if connection.runspace and connection.runspace.state == RunspacePoolState.OPENED:
        display.vvvvv("PSRP CLOSE RUNSPACE: %s" % (connection.runspace.id),
                  host=connection._psrp_host)
        connection.runspace.close()
    connection.runspace = None
    connection._connected = False
    connection._last_pipeline = None


# Generated at 2022-06-13 12:18:53.924665
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Parametrize the arguments of Connection.fetch_file()
    params = [
        # args, kwargs, expected_return
        # AnsibleError("src and dest are required")
        (None, None, None),
        # rc, stdout, stderr = self._exec_psrp_script("$fs.Close()")
        # if rc != 0:
        #     display.warning("failed to close remote file stream of file "
        #                     "'%s': %s" % (in_path, to_native(stderr)))
        (
            dict(), dict(), dict()
        )
    ]

    ansible_mock = Mock(
        spec=Connection
    )


# Generated at 2022-06-13 12:19:02.850731
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection_psrp = Connection(Formatter())
    connection_psrp._exec_psrp_script = mock.Mock()
    connection_psrp._exec_psrp_script.return_value = 0, u"foo\nbar", u""
    connection_psrp.host = mock.Mock()
    connection_psrp.host.rc = 0
    connection_psrp.host.ui.stdout = []
    connection_psrp.host.ui.stderr = []
    result = connection_psrp.exec_command(u"foo", in_data=u"bar")
    assert result.rc == 0
    assert result.stdout == u"foo\nbar"
    assert result.stderr == u""

# Generated at 2022-06-13 12:19:11.806495
# Unit test for method close of class Connection
def test_Connection_close():
    p = mock.patch('ansible.plugins.connection.psrp.Connection.runspace', new_callable=mock.PropertyMock)
    mock_runspace = p.start()
    mock_runspace.state = RunspacePoolState.OPENED
    c = Connection()
    c.close()
    assert c.runspace is None


# Generated at 2022-06-13 12:19:19.192567
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Script to return base64 encoded content of remote file
    read_script = '''
        $fs = $host.Name.GetType().Assembly.GetType("System.IO.FileStream")
        $fs.InvokeMember("ReadFully", [system.reflection.bindingflags]::InvokeMethod, $null, (New-Object IO.FileStream %s, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::Read), @($buffer, $offset, $buffer_size)) | out-null
        return [System.Convert]::ToBase64String($buffer)
    '''

    # import the module we are testing

    # Get the test context
    test_context = {}

    # Construct the object that we are testing
    # connection = Connection()

    #

# Generated at 2022-06-13 12:19:29.946837
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Initialize test values
    psrp_host = '127.0.0.1'
    psrp_user = 'vagrant'
    psrp_pass = 'vagrant'
    psrp_protocol = 'https'
    psrp_port = 5986

    psrp_path = '/wsman'
    psrp_auth = 'basic'
    psrp_cert_validation = 'ignore'
    psrp_connection_timeout = None
    psrp_read_timeout = None
    psrp_message_encryption = 'never'
    psrp_proxy = None
    psrp_ignore_proxy = False
    psrp_operation_timeout = None
    psrp_max_envelope_size = 153600
    psrp_configuration_

# Generated at 2022-06-13 12:20:38.703206
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection(ConnectionInfo())
    assert connection.put_file(None, None, None) == None


# Generated at 2022-06-13 12:20:49.319260
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """Test exec_command of Connection"""

# Generated at 2022-06-13 12:20:51.739697
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn=Connection()
    conn.put_file('test_file','test_file_path')
    # cleanup
    os.remove('test_file')

# Generated at 2022-06-13 12:20:52.896314
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    assert isinstance(connection, Connection)

# Generated at 2022-06-13 12:20:58.763985
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    """
    Tests fetch_file method of class Connection.
    """
    connection = Connection(play_context=PlayContext())
    connection.set_options(direct={'remote_addr':"remote_addr", 'remote_user':"remote_user", 'remote_password':"remote_password"})
    connection.set_options(direct={'protocol':"protocol", 'port':"port"})
    connection.set_options(direct={'path':"path", 'auth':"auth", 'cert_validation':"cert_validation", 'cert_trust_path':"cert_trust_path"})

# Generated at 2022-06-13 12:21:02.083131
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = init_psrp_connection()

    put_file(connection, 'test.txt', b'Hello world')

    assert os.path.isfile('test.txt')
    os.remove('test.txt')



# Generated at 2022-06-13 12:21:05.506120
# Unit test for method reset of class Connection
def test_Connection_reset():
    out = []
    for action in Connection.__dict__:
        if not action.startswith('_') and \
            type(getattr(Connection, action)).__name__ == 'function':
            out += [action]
    return out

# Generated at 2022-06-13 12:21:13.000058
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Unit tests for the method Connection.exec_command of the class Connection

    Raises
    ------
    AssertionError
        When one of the tests fails
    """

    # Save the current state of the module variables
    saved_ansible_module_creation_counter = builder._ANSIBLE_MODULE_CREATION_COUNTER
    saved_ansible_module_cache = builder._ANSIBLE_MODULE_CACHE

    # Reset the global variables before testing
    builder._ANSIBLE_MODULE_CREATION_COUNTER = 0
    builder._ANSIBLE_MODULE_CACHE = {}

    # GIVEN: A Connection object configured with the default settings
    host = Host('127.0.0.1')
    host.port = 5986
    connection = Connection(host, None, None, None)
    connection._

# Generated at 2022-06-13 12:21:13.682021
# Unit test for method reset of class Connection
def test_Connection_reset():
    assert True

# Generated at 2022-06-13 12:21:14.371186
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass
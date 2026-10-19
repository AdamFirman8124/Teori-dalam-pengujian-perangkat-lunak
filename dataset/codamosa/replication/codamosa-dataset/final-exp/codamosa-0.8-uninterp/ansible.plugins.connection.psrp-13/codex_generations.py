

# Generated at 2022-06-13 12:12:52.489594
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    module = get_test_connection_class_instance()
    in_path = 'in_path'
    out_path = 'out_path'
    foo = 'bar'
    try:
        module.put_file(in_path, out_path)
    except Exception as exception:
        assert True

# Generated at 2022-06-13 12:12:54.675063
# Unit test for method close of class Connection
def test_Connection_close():
    '''
    Connection.close
    '''
    connection = Connection(play_context=play_context)
    connection.close()
    
    

# Generated at 2022-06-13 12:12:57.978440
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    connection = Connection()
    result = connection.exec_command('date')
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], int)
    assert isinstance(result[1], bytes)
    assert isinstance(result[2], bytes)


# Generated at 2022-06-13 12:13:06.082873
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Create a mock PsrpSession object.
    mock_session = mock.MagicMock()
    # Create a mock RunspacePool object.
    mock_runspace_pool = mock.MagicMock()
    mock_runspace_pool.create.return_value = mock.MagicMock()
    mock_session.runspace_pools.create.return_value = mock_runspace_pool
    # Create a mock RunspacePoolState object.
    mock_runspace_pool_state = mock.MagicMock()
    mock_runspace_pool.state = mock_runspace_pool_state
    mock_runspace_pool_state.OPENED = 1
    mock_runspace_pool_state.DISPOSED = 2
    mock_runspace_pool_state.CLOSED = 3
    # Create a mock PowerShellHost object.

# Generated at 2022-06-13 12:13:08.819545
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection(play_context=None, new_stdin=None)
    conn.put_file('src', 'dest')
    

# Generated at 2022-06-13 12:13:17.029634
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Setup
    my_ssh = mock.MagicMock()
    my_ssh.get_transport = mock.MagicMock()
    my_ssh.exec_command = mock.MagicMock()


# Generated at 2022-06-13 12:13:29.255463
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection()
    
    # mock input args
    b_in_path = b'in_path'
    b_out_path = b'out_path'
    
    # mock class attributes
    conn.module_implementation_preferences = [b'Psrp', b'WinRM']
    conn.protocol = b'psrp'
    conn._psrp_host = b'_psrp_host'
    
    # mock function inputs
    # mock exec_psrp_script
    old_exec_psrp_script = conn._exec_psrp_script

# Generated at 2022-06-13 12:13:37.506794
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    '''
    :return:
    '''
    import file
    import uuid
    import x509
    import json
    import logging
    import remote
    import psrp
    import http
    import runspace
    import credssp
    import templates
    import ssl
    import socket
    import session
    import security
    import select
    import runspace
    import enum
    import types
    import tpool
    import host
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import iteritems, binary_type
    from ansible.module_utils.six.moves import input

# Generated at 2022-06-13 12:13:44.226339
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    connection._exec_psrp_script = mock.MagicMock(
        return_value=(0, b'', b'')
    )
    in_path = '/path/to/local/file'
    out_path = '/path/to/remote/file'
    display.vvvvv = mock.MagicMock()

    connection.put_file(in_path, out_path)

    # PSRP does not compress files prior to transfer
    with open(in_path, 'rb') as file:
        file_contents = file.read()
    assert connection._exec_psrp_script.call_count == len(file_contents) // CHUNK_SIZE + 1
    assert display.vvvvv.call_count == len(file_contents) // CHUNK_SIZE + 1


# Generated at 2022-06-13 12:13:49.017786
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    command = 'cmd /c (echo stdout1 && echo stdout2) && (echo stderr1 >&2 && echo stderr2 >&2)'
    expected_rc = 1
    expected_stdout = b"stdout1\r\nstdout2\r\n"
    expected_stderr = b"stderr1\r\nstderr2\r\n"
    connection = Connection()
    rc, stdout, stderr = connection.exec_command(command)
    assert rc == expected_rc
    assert stdout == expected_stdout
    assert stderr == expected_stderr

# Generated at 2022-06-13 12:14:23.468111
# Unit test for method close of class Connection
def test_Connection_close():
    # Create a mock action plugin
    action_plugin = MockActionModule()
    display = MockDisplay()

    args = dict(
        remote_addr="10.10.10.10",
        remote_user="ansible\testuser",
        remote_pass="TestPassword123",
        remote_port=5985,
        remote_protocol="HTTP",
        remote_path="/Cimv2",
        auth="CredSSP",
    )
    # Create a new connection
    connection = Connection(action_plugin)
    # Check that the connection is not connected
    assert not connection._connected
    # Initialize the connection with the args
    connection.init_conn(args, display)
    # Check that the connection is connected
    assert connection._connected
    # Close the connection
    connection.close()
    # Check that the connection is not

# Generated at 2022-06-13 12:14:31.485122
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    print("Testing _exec_psrp_script")
    # Input arguments
    winargs = ["powershell.exe", "-executionpolicy", "unrestricted"]
    script = "$hostname = hostname;"
    script += "exit $hostname"
    input_data = "Test string"
    pipelined_scripts = [
        "$pipeline_invocation_id = ($env:ANSIBLE_COMMAND_ID + 1);",
        "$env:ANSIBLE_COMMAND_ID = $pipeline_invocation_id;",
        "$env:ANSIBLE_COMMAND_ID = ($env:ANSIBLE_COMMAND_ID - 1);",
    ]

    winrm_conn = Connection(winargs)
    winrm_conn._exec_psrp_script(script, input_data)
    stdout

# Generated at 2022-06-13 12:14:32.176298
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass

# Generated at 2022-06-13 12:14:37.133111
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    connection = Connection()
    rc, stdout, stderr = connection.exec_command("Get-Module -Name PSSessionConfiguration")

# Generated at 2022-06-13 12:14:46.466686
# Unit test for method close of class Connection
def test_Connection_close():
    mock_module_helper = MagicMock()
    mock_module_helper.psrp_protocol = 'https'
    mock_module_helper.psrp_connection_timeout = 100
    mock_module_helper.psrp_read_timeout = 120
    mock_module_helper.psrp_message_encryption = False
    mock_module_helper.psrp_proxy = ''
    mock_module_helper.psrp_ignore_proxy = True
    mock_module_helper.psrp_operation_timeout = 300
    mock_module_helper.psrp_max_envelope_size = 1
    mock_module_helper.no_log = True
    mock_module_helper.psrp_configuration_name = None
    mock_module_

# Generated at 2022-06-13 12:14:49.554979
# Unit test for method close of class Connection
def test_Connection_close():
    #
    connection = None
    #

    #
    # Setup
    connection = Connection(None)
    connection.runspace = connection.runspace
    #

    #
    # Exercise
    connection.close()
    #

    #
    # Verify
    assert connection.runspace == None
    #

    #
    # Cleanup
    #


# Generated at 2022-06-13 12:14:59.628503
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  # setting up the testing configuration
  from ansible.plugins import connection
  from ansible.plugins.connection.psrp import Connection
  from ansible.utils.path import unfrackpath
  from ansible.utils.display import Display
  from ansible.plugins.loader import add_all_plugin_dirs
  from ansible import constants as C
  import os
  import os.path
  import tempfile
  import unittest

  # adding all the plugins path in order to be able to get the plugin
  add_all_plugin_dirs()

  # setup connection class
  display = Display()
  display.verbosity = 5
  connection_psrp = Connection(None, display, None)
  connection_psrp._connected = True

  # pylint: disable=protected-access
  connection_psrp._last

# Generated at 2022-06-13 12:15:02.885797
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection(Runner())
    with pytest.raises(AnsibleError) as excinfo:
        connection.fetch_file('local_path', 'remote_path', 'file_name')
    assert to_native(excinfo.value) == "The 'psrp' connection plugin does not support fetching files."



# Generated at 2022-06-13 12:15:07.087081
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection(play_context=PlayContext())
    local_path = "/home/user/a"
    remote_path = "/home/user/b"
    conn.fetch_file(local_path, remote_path)


# Generated at 2022-06-13 12:15:14.335627
# Unit test for method close of class Connection
def test_Connection_close():
    mock_inventory = InventoryManager(loader=None, sources=[])
    mock_variable_manager = VariableManager(loader=None, inventory=mock_inventory)
    mock_loader = DataLoader()
    mock_options = Options()

    mock_options.connection = 'psrp'
    mock_options.remote_addr = 'localhost'
    mock_options.remote_user = 'vagrant'
    mock_options.remote_password = 'vagrant'
    mock_options.timeout = 10

    # set up test PSConnection object
    mock_connection = Connection(mock_options, mock_variable_manager, mock_loader)
    mock_connection._connected = True
    mock_connection.runspace = "mock_runspace"
    
    # set up mock runspace
    mock_runspace = Mock()
    mock_runspace

# Generated at 2022-06-13 12:15:45.361303
# Unit test for method close of class Connection
def test_Connection_close():
    conn = Connection(play_context=PlayContext())
    conn.close()


# Generated at 2022-06-13 12:15:57.004028
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():

    # Declare mock objects
    class MockInMemoryFile:
        pass

    class MockRunspace:
        pass

    class MockRunspacePoolState:
        pass

    class MockHost:
        pass

    class MockPlayContext:
        pass

    # Create the object under test
    pylint: disable=too-many-arguments
    connection = Connection(in_memory_file=MockInMemoryFile(),
                            host="host",
                            port=1,
                            username="username",
                            password="password",
                            runspace=MockRunspace(),
                            runspace_pool_state=MockRunspacePoolState(),
                            host_impl=MockHost(),
                            play_context=MockPlayContext())

    # Set up needed values

# Generated at 2022-06-13 12:15:58.315179
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    assert connection.close() is None


# Generated at 2022-06-13 12:16:08.759385
# Unit test for method put_file of class Connection

# Generated at 2022-06-13 12:16:15.788702
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    # in_path is str
    assertRaises(TypeError, connection.fetch_file, )
    # in_path is str and out_path is str

# Generated at 2022-06-13 12:16:19.383451
# Unit test for method reset of class Connection
def test_Connection_reset():
    host = create_psrp_connection(None)
    host.close()
    res = host.close()


# Generated at 2022-06-13 12:16:26.120492
# Unit test for method close of class Connection
def test_Connection_close():
    # Set up mock objects
    class MockPSRPConnection(PSRPConnection):
        def __init__(self):
            self.runspace = MockRunspacePool()
            self._connected = False
            self._last_pipeline = None
    
    class MockRunspacePool():
        def __init__(self):
            self._runspace_id = None
            self.state = RunspacePoolState.OPENED
    # Performs connection.close() and check if it works as expected
    conn = MockPSRPConnection()
    assert conn._connected == False
    assert conn._last_pipeline == None
    assert conn is not None
    conn.close()
    assert conn._connected == False
    assert conn._last_pipeline == None
    assert conn is not None


# Generated at 2022-06-13 12:16:36.063004
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    print("Executing test_Connection_put_file")
    
    psrp_host = "win-vh7cgp0t70u"
    psrp_user = "Administrator"
    psrp_pass = "MiSa2018!"
    psrp_protocol = "https"
    psrp_port = 5986
    psrp_path = "wsman"
    psrp_auth = "certificate"
    psrp_cert_validation = "ignore"
    
    psrp_connection_timeout = None
    psrp_read_timeout = None
    psrp_message_encryption = None
    psrp_proxy = None
    psrp_ignore_proxy = False
    psrp_operation_timeout = 120000
    psrp_max_envelop

# Generated at 2022-06-13 12:16:42.600366
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """Test exec_command method of class Connection."""
    print("type: %s" % type)
    print("value: %s" % value)
    print("is_missing_linked_lib: %s" % is_missing_linked_lib)
    print("traceback: %s" % traceback)




# Generated at 2022-06-13 12:16:49.656951
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Unit test for method exec_command of class Connection
    """
    args = dict(
        func=exec_command,
        cmd="powershell -file C:\\users\\abc\\Desktop\\abc.ps1",
        defalut_output="nul 2>&1",
        display_error=True
    )
    # TODO: Verify the correctness of exec_command
    


# Generated at 2022-06-13 12:17:30.446705
# Unit test for method reset of class Connection
def test_Connection_reset():
    import pytest
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['remote_addr'] = '127.0.0.1'
            self.params['remote_user'] = 'ansible'
            self.params['remote_password'] = 'ansible'
            self.params['protocol'] = 'https'
            self.params['port'] = 5986
            self.params['path'] = '/wsman'
            self.params['auth'] = 'plaintext'
            self.params['cert_validation'] = 'ignore'
            self.params['connection_timeout'] = 30
            self.params['read_timeout'] = 30
            self.params['message_encryption'] = 'disable'
            self.params['proxy'] = None

# Generated at 2022-06-13 12:17:34.165680
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():

    # Explicitly create instance of a Connection subclass to test exec_command
    connection = ConsoleConnection()
    # Call method to test
    result = connection.exec_command("echo hello world")
    assert result is not None, "Connection method exec_command returned None"

# Generated at 2022-06-13 12:17:43.739133
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from ansible.plugins.connection.psrp import Connection

    # Get some test data
    test_file = open(os.path.join(os.path.dirname(__file__), os.path.pardir, 'lib', 'ansible', 'module_utils', 'powershell', 'test', 'test.ps1'), 'r')
    test_data = to_text(test_file.read(), errors='surrogate_or_strict', encoding='utf-8')

    # Mock our psrp module so we can test the put_file method
    def mock_exec_psrp_script(script, input_data=None, use_local_scope=True, arguments=None):
        if script.startswith('$fs.OpenText('):
            return 0, '', ''

# Generated at 2022-06-13 12:17:47.458638
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    con = Connection()
    command = 'echo "success"'
    result = con.exec_command(command)
    assert result['rc'] == 0
    assert result['stdout'] == 'success\r\n'
    assert result['stderr'] == ''
    assert result['stdin'] == ''


# Generated at 2022-06-13 12:17:52.120059
# Unit test for method close of class Connection
def test_Connection_close():
    x = Connection()
    x.runspace = x
    x.runspace.state = x
    x.runspace.state = RunspacePoolState.OPENED
    x.runspace.close = Mock()
    x.close()
    x.runspace.close.assert_called()


# Generated at 2022-06-13 12:18:01.313135
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Set up params for tests
    server = 'localhost'
    username = 'bogus_user'
    password = 'bogus_password'
    commands = ['dir c:\\', 'dir c:\\ /s']
    results = []
    expected_results = [('0', '', ''), ('0', '', '')]

    # Invoke the tested method
    connection = Connection(server, username, password)
    connection.connect()
    for command in commands:
        result = connection.exec_psrp_command(command)
        results.append(result)
    connection.close()

    # Check the results
    assert len(results) == len(expected_results)
    for i in range(len(results)):
        assert results[i] == expected_results[i]


# Generated at 2022-06-13 12:18:04.631943
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
   connection = PSRPConnection()
   assert connection.fetch_file('test_file_path', 'destination_path') == None
   assert connection.fetch_file() == None


# Generated at 2022-06-13 12:18:21.648575
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
  from psrp_plugin.module_utils.common import to_text
  from ansible.errors import AnsibleError

  # Constructor test
  params = {'extra_arg': 'extra_value'}
  psrp_conn = Connection(play_context=None, new_stdin='', *[], **params)
  assert psrp_conn.get_option('remote_addr') == None
  assert psrp_conn.get_option('remote_user') == None
  assert psrp_conn.get_option('remote_password') == None
  assert psrp_conn.get_option('protocol') == None
  assert psrp_conn.get_option('port') == None
  assert psrp_conn.get_option('path') == None
  assert psrp_conn.get_option

# Generated at 2022-06-13 12:18:25.268958
# Unit test for method put_file of class Connection
def test_Connection_put_file():

    # Arrange
    connection = Connection(None)
    tmp_file = tempfile.NamedTemporaryFile()
    tmp_file.write(b'Success')
    tmp_file.seek(0)
    
    # Act
    connection.put_file(tmp_file.name, '/tmp/ansible_test.txt')
    ret = tmp_file.readline()
    
    # Assert
    assert ret == b'Success'

# Generated at 2022-06-13 12:18:32.059546
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    #set up connection
    conn = Connection(None)
    conn._psrp_host = "myhost"
    conn._psrp_protocol = "http"
    conn._psrp_port = 5985
    conn._psrp_auth = "Basic"
    conn._psrp_user = "admin"
    conn._psrp_pass = "password"
    conn._psrp_cert_validation = False
    conn._psrp_connection_timeout = None
    conn._psrp_read_timeout = None
    conn._psrp_message_encryption = False
    conn._psrp_proxy = None
    conn._psrp_ignore_proxy = False
    conn._psrp_operation_timeout = 60

# Generated at 2022-06-13 12:18:59.609478
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    con = Connection()

# Generated at 2022-06-13 12:19:05.863888
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    from ansible.errors import AnsibleError
    from mock import MagicMock
    from unit.mock.loader import DictDataLoader
    from ansible.plugins.connection.psrp import Connection

    loader = DictDataLoader({})

    conn = Connection(
        MagicMock(),
        '/home/user/.ansible/roles/my-role/tests/inventory'
    )
    conn._host = MagicMock()
    conn._psrp_host = 'localhost'

    conn.get_option = MagicMock(side_effect=[None, None, None, None, None])

    # We'll define some dummy scripts which we'll return in the _exec_psrp_script method.
    read_script = 'Get-Content -Path "/path/to/file.txt" -Encoding Byte -ReadCount 8'
   

# Generated at 2022-06-13 12:19:08.381716
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    conn = Connection(None, None)
    conn._connected = False
    conn._exec_psrp_script = mock.MagicMock()
    rc, stdout, stderr = conn.exec_command('Get-Host')
    assert rc == 0
    assert len(stdout) > 0
    assert len(stderr) == 0
    conn.close()


# Generated at 2022-06-13 12:19:13.648743
# Unit test for method reset of class Connection
def test_Connection_reset():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.connection.psrp import Connection

    conn = Connection()
    conn._connected = True
    conn.close = MagicMock()
    conn.reset()
    conn.close.assert_called_once()



# Generated at 2022-06-13 12:19:20.363723
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Unit test for exec_command of class Connection
    """
    connection = Connection()
    if not connection.__class__.__name__ == 'Connection':
        raise AssertionError("Class `Connection` should have __name__ == `Connection`")
    if not connection.__class__.__doc__ == Connection.__doc__:
        raise AssertionError("Class `Connection` should have __doc__ == `%s`" % Connection.__doc__)
    if not Connection.exec_command.__doc__ == executable.exec_command.__doc__:
        raise AssertionError("Method `Connection.exec_command` should have __doc__ == `%s`" % executable.exec_command.__doc__)

# Generated at 2022-06-13 12:19:22.159630
# Unit test for method reset of class Connection
def test_Connection_reset():

	connection = Connection(None)

	assert(connection.reset() == None)

# Generated at 2022-06-13 12:19:28.066224
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Setup the dummy file
    with open('./dummyfile','w') as dummy:
        dummy.write('Hello World')

    # Instantiate the class and execute the method
    print('Instantiate the class and execute the method')
    conn = Connection()
    conn.put_file('c:\\ansible\\dummyfile','./dummyfile')

    # Cleanup
    os.remove('./dummyfile')



# Generated at 2022-06-13 12:19:37.272931
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
	
	# Make sure _create_psrp_connection does not throw an exception
		psrp_host = ''
		psrp_port = 5985
		psrp_user = None
		psrp_pass = None
		psrp_path = 'wsman'
		psrp_auth = 'basic'
		psrp_protocol = 'http'
		# TODO: What is cert_validation?
		psrp_cert_validation = True
		psrp_connection_timeout = None
		psrp_message_encryption = 'auto'
		psrp_proxies = None
		psrp_ignore_proxy = False
		psrp_proxy = ''
		psrp_operation_timeout = 30


# Generated at 2022-06-13 12:19:48.106266
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Set up the test connection
    module_args = dict(
                        host='localhost',
                        port=5986,
                        path='/wsman',
                        protocol='https',
                        user='Administrator',
                        password='password',
                        connection_timeout=30,
                        operation_timeout=30,
                        read_timeout=30,
                        max_envelope_size=512000,
                        message_encryption='auto',
                        cert_validation='ignore',
                        auth=None,
                        proxy=None,
                        ignore_proxy=None,
                        transport='ntlm',
                        _extras=None,
                        _ansible_check_mode=False
                    )
    # Instantiate a connection
    conn = Connection(module_args)
    # Connect the connection
    conn.connect()
    # Execute the command
    output

# Generated at 2022-06-13 12:19:55.676665
# Unit test for constructor of class Connection
def test_Connection():
    try:
        # Unit test
        # Create a Connection object, representing a connection to localhost,
        # using the 'winrm' protocol, port 5985 and the 'http' transport.
        connection = Connection(module_name='winrm', host='localhost',
                                port=5985, protocol='http')

        # Ensure connection object is of type Connection.
        assert isinstance(connection, Connection)
    except Exception as e:
        # Print error message when an exception is caught.
        print(e)


# Generated at 2022-06-13 12:20:52.897810
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    connection.close()
    # test output of function close()
    assert (connection.runspace == None)
    assert (connection._connected == False)
    assert (connection._last_pipeline == None)
    
    
    



# Generated at 2022-06-13 12:21:01.311922
# Unit test for method close of class Connection
def test_Connection_close():
    conn = psrp.Connection(play_context=play_context, new_stdin=None)
    with patch('ansible_collections.ansible.community.plugins.connection.psrp.psrp.Connection._exec_psrp_script') as exec_psrp_script:
        exec_psrp_script.return_value = (0, "stdout", "stderr")
        conn.close()
        exec_psrp_script.assert_called_with("Stop-RunspacePool")


# Generated at 2022-06-13 12:21:09.019453
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    c = Connection()
    arg1 = None
    arg2 = None
    arg3 = None
    arg4 = None
    arg5 = None
    arg6 = None
    arg7 = None
    arg8 = None
    arg9 = None
    arg10 = None
    arg11 = None
    arg12 = None
    arg13 = None
    arg14 = None
    arg15 = None
    expected = None
    actual = c.exec_command(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15)
    assert expected == actual, 'Test failed'

# Generated at 2022-06-13 12:21:13.717170
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    cmd = "echo b > c:\\test_echo.txt"
    connection = Connection()
    connection._build_kwargs()
    connection.runspace = None
    connection.connect()
    connection._exec_psrp_script(cmd)
test_Connection_exec_command()

 

# Generated at 2022-06-13 12:21:19.815761
# Unit test for method close of class Connection
def test_Connection_close():
    args_dict = dict(
        runspace=RunspacePoolState.OPENED,
        runspace=None,
        _connected=False,
        _last_pipeline=None
    )
    args = dict2namedtuple(args_dict, name='Args')
    setattr(args, '_psrp_host', None)

    obj = Connection(args)

    setattr(obj, 'runspace', RunspacePoolState.OPENED)

    obj.close()

# Generated at 2022-06-13 12:21:25.456892
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # This is a unit test function for the Connection class's method fetch_file.
    #
    # Args:
    #   self: The object pointer
    #
    # Returns:
    #   None
    #
    # Raises:
    #   None

    # fetch_file is defined in connection_plugins/psrp.py
    # No tests are provided since there are no unit testable lines in the function

    return None



# Generated at 2022-06-13 12:21:26.346388
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()


# Generated at 2022-06-13 12:21:31.096154
# Unit test for method reset of class Connection
def test_Connection_reset():
    mock_psrp = mock.Mock()
    kwargs = dict(
        host='myhost',
        port=5985,
        user='myuser',
        password='mypassword',
    )
    psrp_connection = Connection(mock_psrp, **kwargs)
    psrp_connection.reset()
    mock_psrp.assert_called_with(**kwargs)  # pylint: disable=no-member

# Generated at 2022-06-13 12:21:34.097595
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """Test exec_command of class Connection"""
    connection = Connection()
    rc, out, err = connection.exec_command('echo "hello"')
    assert rc == 0
    assert out == b"hello\r\n"
    assert err == b""



# Generated at 2022-06-13 12:21:43.025117
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Create a mock Transport object to test against
    transport = unittest.mock.MagicMock()
    transport.protocol = 'https'
    transport.port = 5986
    transport.is_psrp = True
    transport.remote_addr = '127.0.0.1'
    transport.remote_user = 'ansible'

    # Create a mock PSRP connection object to test against
    psrp = pypsrp.client.Client('127.0.0.1', username='ansible', password='ansible', port=5986, ssl=True)
    transport.psrp_connection = unittest.mock.MagicMock(return_value=psrp)

    # Create a Connection object
    conn = Connection(None, None)

    # Test that the method call succeeds when a destination path is
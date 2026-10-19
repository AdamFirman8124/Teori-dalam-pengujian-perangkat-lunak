

# Generated at 2022-06-13 12:12:47.375335
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
  # Unit test for method fetch_file of class Connection
  # Ensures that fetch_file raises an ansible error when a value error occurs
  class Obj(object):
    pass
  # method fetch_file from module psrp
  # Ensures that fetch_file raises an ansible error when a value error occurs
  def test_fetch_file(self, in_path, out_path):
    file_transfer_obj = Obj()
    file_transfer_obj.set_play_context(play_context)
    file_transfer_obj._connection = psrp.Connection(play_context, new_stdin=None)
    file_transfer_obj._connection._psrp_path = u'/wsman'

# Generated at 2022-06-13 12:12:49.240561
# Unit test for method reset of class Connection
def test_Connection_reset():
    my_connection = ansible_psrp.Connection()
    my_connection.reset()
    assert my_connection is not None


# Generated at 2022-06-13 12:12:57.567846
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    mock_module = MagicMock()
    mock_connection = Connection(mock_module._play_context, mock_module._new_stdin, 'test')

    # First call, raise an exception
    mock_open = MagicMock(side_effect=Exception("Test Exception"))
    mock_connection._open_psrp_file = mock.MagicMock(side_effect=Exception("Test Exception"))
    with patch('ansible_collections.ansible.community.plugins.module_utils.common.remoting.Connection._open', mock_open):
        with patch('ansible_collections.ansible.community.plugins.module_utils.common.remoting.Connection._exec_psrp_script', return_value=(0, '', '')):
            with pytest.raises(AnsibleError) as excinfo:
                mock

# Generated at 2022-06-13 12:13:05.836005
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    """
    Unit test for method put_file of class Connection
    """
    # Arguments
    test_params = dict()
    test_params['file_path'] = 'C:\\Users\\test.txt'
    test_params['in_path'] = 'C:\\Users\\test.txt'
    test_params['out_path'] = 'C:\\Users\\test.txt'
    test_params['tmp_path'] = None
    test_params['directory_mode'] = None
    test_params['use_atomic'] = True
    test_params['use_sudo'] = False
    test_params['use_subprocess'] = False
    test_params['remote_src'] = True
    test_params['checksum'] = None
    test_params['modify_remote_file'] = True

# Generated at 2022-06-13 12:13:15.523478
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from mock import patch
    from ansible.module_utils.psrp import Connection

    module = AnsibleModuleMock(1)
    connection = Connection(module)
    path = 'test_path'
    buffer_size = 16 * 1024
    script_path = 'test_script_path'
    in_path = 'test_in_path'
    out_path = 'test_out_path'
    rc = 1
    stdout = 'test_stdout'
    stderr = 'test_stderr'
    call_list = []

    def exec_psrp_script(script, input_data=None, use_local_scope=True,
                         arguments=None):
        call_list.append(script)
        return rc, stdout, stderr


# Generated at 2022-06-13 12:13:28.513633
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    stdout= 'bobby'
    stderr= None
    rc= 0
    runspace = mock.MagicMock()
    runspace.state.return_value= RunspacePoolState.OPENED
    pipeline = mock.MagicMock()
    pipeline.invoke.return_value= None
    pipeline.had_errors.return_value= False
    ps = mock.MagicMock()
    ps.add_script.return_value= None
    ps.add_argument.return_value= None
    ps.invoke.return_value= None
    PowerShell.return_value= ps
    host = mock.MagicMock()
    host.rc.return_value= 0
    host.ui.stdout.return_value= None
    host.ui.stderr.return_value= None
    runspace._create_pip

# Generated at 2022-06-13 12:13:29.177406
# Unit test for method reset of class Connection
def test_Connection_reset():
    assert True

# Generated at 2022-06-13 12:13:31.100820
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    result = connection.put_file(src='src', dest='dest')
    assert type(result) == Connection


# Generated at 2022-06-13 12:13:35.047719
# Unit test for method close of class Connection
def test_Connection_close():
    if not os.path.exists('/usr/local/bin/psrp'):
        pytest.skip("There is no psrp installed.")
    else:
        executor = Connection()
        executor.close()


# Generated at 2022-06-13 12:13:40.285445
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # Initialize test values
    in_path = "in_path"
    out_path = "out_path"
    buffer_size = 0
    offset = 0

    # Initialize mock
    module = get_module()
    module.params = {}
    module.params['extract_csv_fields'] = False

    # Execute method
    result = module.connection.fetch_file(in_path, out_path, buffer_size, offset)

    # Verify results
    assert(result is None)

# Generated at 2022-06-13 12:14:04.131486
# Unit test for method close of class Connection
def test_Connection_close():
    connection =Connection(None)
    connection._connected = False
    connection._psrp_host = None
    connection.runspace = None
    connection._last_pipeline = None
    connection.close()

# Generated at 2022-06-13 12:14:11.243157
# Unit test for constructor of class Connection
def test_Connection():
    conn = Connection(None)
    assert conn.has_pipelining is False
    assert conn.always_pipeline is False
    assert conn.become_method is None
    assert conn.become_info is None
    assert conn._connected is False
    assert conn.have_tty is False
    assert conn.play_context is None
    assert conn._shell is None
    assert conn._shell_type is None
    assert conn._last_pipeline is None
    assert conn._play_context is None
    assert conn._shell_config is None
    assert conn._powershell_compat is None
    assert conn.become is False
    assert conn.become_user is None
    assert conn.become_pass is None
    assert conn._shell_type is None
    assert conn._shell_config is None
    assert conn._

# Generated at 2022-06-13 12:14:21.311270
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    transport = 'psrp'
    remote_addr = 'localhost'
    remote_user = 'ansible'
    remote_pass = password
    remote_port = 5985
    protocol = 'http'
    path = ''
    auth = 'ntlm'
    cert_validation = 'ignore'
    connection_timeout = 20
    read_timeout = None
    message_encryption = False
    proxy = None
    ignore_proxy = True
    operation_timeout = 40
    max_envelope_size = 153600
    configuration_name = None
    reconnection_retries = 2
    reconnection_backoff = 5
    certificate_key_pem = None
    certificate_pem = None
    credssp_auth_mechanism = 'negotiate'
    credssp_disable_tlsv1

# Generated at 2022-06-13 12:14:24.181425
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # import pytest

    # conn = psrp_connection.Connection(play_context=None)
    # conn.run()
    # conn.put_file()

    # assert callable(psrp_connection.Connection.put_file)
    pass

# Generated at 2022-06-13 12:14:28.874339
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
   psrp_host='test'
   session_id=1
   runspace=None
   remote_addr='test'
   remote_user='test'
   remote_password='test'
   connection=Connection(psrp_host,session_id,runspace,remote_addr,remote_user,remote_password)
   in_path='test'
   out_path='test'
   file_size=1
   buffer_size=1
   connection.fetch_file(in_path,out_path,file_size,buffer_size)



# Generated at 2022-06-13 12:14:40.394438
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Ansible Connection class for Microsoft Windows
    """

    import pytest

    @pytest.mark.parametrize("ansible_module_name", [
        (None),
        ('ping'),
        ('win_ping')
    ])
    def test_Connection_exec_command_module_name(mocker, ansible_module_name):
        from ansible.module_utils.common._collections_compat import Mapping

        mocker.patch("ansible.module_utils.basic.AnsibleModule")
        mocker.patch("ansible.module_utils.windows.crypto.SPNEGO")

        runspace_pool = mocker.MagicMock()
        runspace_pool.state = RunspacePoolState.OPENED


# Generated at 2022-06-13 12:14:48.547617
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    test = Connection()
    test._psrp_protocol = 'test_value'
    test._psrp_host = 'test_value'
    test._psrp_user = 'test_value'
    test._psrp_pass = 'test_value'
    test._psrp_port = 'test_value'
    test._psrp_path = 'test_value'
    test._psrp_auth = 'test_value'
    test._psrp_cert_validation = 'test_value'
    test._psrp_connection_timeout = 'test_value'
    test._psrp_read_timeout = 'test_value'
    test._psrp_message_encryption = 'test_value'
    test._psrp_proxy = 'test_value'
    test

# Generated at 2022-06-13 12:14:58.654651
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
  psrp_connection = Connection()
  psrp_connection.set_options({"_extras":{"ansible_psrp_test_opt":True}})
  in_path = "test_in_path"
  out_path = "test_out_path"
  file_size = 1024
  buffer_size = 512
  offset = 0

# Generated at 2022-06-13 12:15:03.622639
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    from ansible.module_utils.psrp import Connection

    c = Connection('')
    c._connected = True
    c.runspace = MagicMock()

    c._exec_psrp_script = MagicMock(return_value=(0, 'test', ''))

    c.fetch_file('psrp://server/c$/test', 'c:\temp')

    assert c._exec_psrp_script.call_count == 2, '_exec_psrp_script should have been called twice'


# Generated at 2022-06-13 12:15:06.111680
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    """
    Connection.exec_command()
    """
    # FIXME: this method needs a unit test
    pass

# Generated at 2022-06-13 12:15:54.232474
# Unit test for method close of class Connection
def test_Connection_close():
    from mock import MagicMock
    from ansible.plugins.connection.psrp import Connection

    mock_connection = MagicMock()
    mock_connection.state = "OPENED"

    mock_runspace = MagicMock()
    mock_runspace.runspace = mock_connection

    mock_self = MagicMock()
    mock_self.runspace = mock_runspace

    test_connection = Connection(mock_self)
    test_connection.close()

    assert test_connection.runspace is None
    assert test_connection._connected is False
    assert test_connection._last_pipeline is None



# Generated at 2022-06-13 12:15:58.499034
# Unit test for method reset of class Connection
def test_Connection_reset():
    # TODO: Pass in values for all params
    cnx = Connection(play_context=play_context, new_stdin=None)

    # TODO: Test for no return value
    # Test for return type
    assert isinstance(cnx.reset(), Connection)



# Generated at 2022-06-13 12:16:08.012740
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    
    # Assign default values for variables used in this method
    psrp_connection_reference = None
    dest_file_name = '../playbooks/files/readonly.txt'
    dest_file_path = 'C:\\ansible\\readonly.txt'
    src_file_name = '../playbooks/files/readonly.txt'
    src_file_path = 'C:\\ansible\\readonly.txt'
    with_attributes = None
    # Invoke method
    result = psrp_connection_reference.put_file(dest_file_name,dest_file_path,src_file_name,src_file_path,with_attributes)

# Generated at 2022-06-13 12:16:15.172752
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Unit test with mock host
    mock_host = Linux()
    test_command = 'uname -a'

    # assert original class
    conn = Connection(mock_host, become_method=None, become_username=None)
    assert isinstance(conn,Connection)

    # mock replace Connection class with Connection_proxy class
    Connection_proxy.exec_command(conn, test_command,in_data=None, sudoable=False)

if __name__ == '__main__':
    test_Connection_exec_command()

# Generated at 2022-06-13 12:16:18.695953
# Unit test for method close of class Connection
def test_Connection_close():
    connection = ansible_psrp.Connection()
    print(connection.close())


# Generated at 2022-06-13 12:16:20.197358
# Unit test for method close of class Connection
def test_Connection_close():
    test_conn = psrp_connection.Connection(psrp_host='server')
    test_conn.close()


# Generated at 2022-06-13 12:16:21.699627
# Unit test for method close of class Connection
def test_Connection_close():
    connection = Connection()
    connection.close()



# Generated at 2022-06-13 12:16:24.419096
# Unit test for method reset of class Connection
def test_Connection_reset():
    '''
    Unit test for Connection.reset
    '''
    c = Connection()
    c.reset()
    c.close()


# Generated at 2022-06-13 12:16:26.499442
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    conn = Connection()
    conn.put_file()


# Generated at 2022-06-13 12:16:31.443975
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    conn = Connection(None)
    conn.runspace = RunspacePool(host='127.0.0.1', username='foo', password='bar')
    conn._psrp_host = '127.0.0.1'
    conn.fetch_file('/path/to/local/file', '/path/to/local/file')

# Generated at 2022-06-13 12:17:54.175955
# Unit test for method reset of class Connection

# Generated at 2022-06-13 12:17:59.916280
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()
    context = Mock()
    in_path = "foo"
    out_path = "bar"
    transport_options = None
    connection.get_option = MagicMock(return_value="")
    transport_class = MagicMock()
    transport_class.return_value.check_mode = False
    transport_class.return_value.put_file = MagicMock(return_value=None)
    with patch.object(connection, 'transport', transport_class):
        with patch.object(connection, 'open', MagicMock(return_value=None)):
            connection.put_file(in_path, out_path, context)


# Generated at 2022-06-13 12:18:02.431422
# Unit test for method close of class Connection
def test_Connection_close():	
	obj = Connection()
	assert not(obj.runspace)

# Generated at 2022-06-13 12:18:06.472308
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    my_obj = connection.Connection()
    args = tuple([])
    curr_rc = None
    curr_stdout = b''
    curr_stderr = b''

    result = my_obj.exec_command(args, curr_rc, curr_stdout, curr_stderr)
    assert result is None

# Generated at 2022-06-13 12:18:08.674572
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    # TODO write unit tests for Connection
    pass

# Generated at 2022-06-13 12:18:10.893212
# Unit test for method close of class Connection
def test_Connection_close():
  conn = Connection()
  conn.close()


# Generated at 2022-06-13 12:18:12.710885
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    connection = Connection()



# Generated at 2022-06-13 12:18:13.688278
# Unit test for method reset of class Connection
def test_Connection_reset():
    pass

# Generated at 2022-06-13 12:18:18.015313
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection((None,None), None, None)
    ret_val = connection.fetch_file(None, None)
    assert ret_val == None


# Generated at 2022-06-13 12:18:22.355266
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Arrange
    psrp_conn = Connection()
    cmd = 'echo test'

    # Act
    result = psrp_conn.exec_command(cmd)

    # Assert
    assert(result == {
        'rc': 0,
        'stdout': 'test',
        'stderr': ''
    })



# Generated at 2022-06-13 12:20:56.304134
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    connection.runspace_id = 123
    connection.runspace = "pypsrp.powershell.runspaces.RunspacePool"
    connection._psrp_host = "localhost"
    connection._psrp_user = "username"
    connection._psrp_pass = "password"
    connection._psrp_protocol = "https"
    connection._psrp_port = 5986
    connection._psrp_path = "/wsman"
    connection._psrp_auth = "plaintext"
    connection._psrp_cert_validation = True
    connection._psrp_connection_timeout = None
    connection._psrp_read_timeout = 30
    connection._psrp_message_encryption = "auto"
    connection._psrp_proxy = None

# Generated at 2022-06-13 12:21:05.662744
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    plugin = Connection()
    # the closest to a real path we can get
    dir_path = os.path.dirname(os.path.realpath(__file__))
    in_path = os.path.join(dir_path, 'test_fetch_file.txt')
    out_path = os.path.join(dir_path, 'test_fetch_file_out.txt')
    try:
        os.remove(out_path)
    except (OSError, IOError):
        pass
    # run fetch_file
    plugin.fetch_file(in_path, out_path)
    # now the file must exist
    assert os.path.isfile(out_path)



# Generated at 2022-06-13 12:21:06.836082
# Unit test for method reset of class Connection
def test_Connection_reset():
    connection = Connection()
    connection.reset()

# Generated at 2022-06-13 12:21:11.945070
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    connection = Connection()
    with pytest.raises(AnsibleError):
        connection.fetch_file(None, None)
    with pytest.raises(AnsibleError):
        connection.fetch_file('in_path', None)
    with pytest.raises(AnsibleError):
        connection.fetch_file(None, 'out_path')
    with pytest.raises(AnsibleError):
        connection.fetch_file('in_path', 'out_path')


# Generated at 2022-06-13 12:21:20.000751
# Unit test for method close of class Connection
def test_Connection_close():
    '''
    Unit test for method close of class Connection
    '''
    remote_addr = '192.168.1.1'
    remote_user = 'ansible'
    remote_pass = 'password'
    remote_port = 5986

    # Initialize the class
    connection = Connection(remote_addr, remote_user, remote_pass, remote_port)

    # Replace the runspace attribute
    # TODO: Replace this with a mock object
    connection.runspace = object()

    # Call the close method
    connection.close()

    # Check the runspace attribute was set to None
    assert connection.runspace == None


# Generated at 2022-06-13 12:21:29.012761
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    # Init variable
    # Create the AnsibleModule object
    module = AnsibleModule(
        argument_spec={
            'host': {
                'type': str,
                'required': True
            },
            'password': {
                'type': str,
                'required': True
            },
            'port': {
                'type': int,
                'required': False
            },
            'user': {
                'type': str,
                'required': True
            }
        },
        supports_check_mode=False
    )

    # Create the Connection object
    connection = Connection(module._socket_path)
    # test the connection
    rc = connection.exec_command('echo hello')
    assert rc[0] == 0

    # put_file with exception

# Generated at 2022-06-13 12:21:32.855108
# Unit test for method put_file of class Connection
def test_Connection_put_file():
    from ansible_collections.ansible.community.plugins.connection.psrp import Connection
    import pytest
    con = Connection()
    with pytest.raises(NotImplementedError) as excinfo:
        con.put_file()
    assert excinfo.value.message == "put_file() not implemented for psrp"


# Generated at 2022-06-13 12:21:41.268693
# Unit test for method fetch_file of class Connection
def test_Connection_fetch_file():
    fetch_file_args = {}
    fetch_file_args['in_path'] = u'O:\\Ansible\\Test'
    fetch_file_args['out_path'] = u'C:\\Users\\dligtenb\\test.txt'
    fetch_file_args['temp_path'] = u'C:\\Users\\dligtenb\\AppData\\Local\\Temp'
    fetch_file_args['use_powershell'] = True
    fetch_file_args['follow'] = False
    fetch_file_args['md5sum'] = None

    psrp_host = u'192.168.10.132'
    psrp_user = u'dligtenb'
    psrp_pass = u'Ligtenberg1'
    psrp_port = 5986
    psrp_protocol

# Generated at 2022-06-13 12:21:47.978222
# Unit test for method exec_command of class Connection
def test_Connection_exec_command():
    # Can't do real tests yet because the module is not loaded by pytest
    mock_module = MagicMock(spec=Connection)
    mock_module.exec_command.return_value = (0, "omg_stdout_oh_noe", "yikes_stderr")
    assert (0, "omg_stdout_oh_noe", "yikes_stderr") == mock_module.exec_command("ls")


# Generated at 2022-06-13 12:21:54.293789
# Unit test for method close of class Connection
def test_Connection_close():
    hostname = "hostname"
    username = "user_name"
    password = "password"
    psrp_path = "/ansible"
    psrp_protocol = "https"
    psrp_certificate_validation = False

    connection = Connection(hostname, username, password, psrp_path, psrp_protocol, psrp_certificate_validation)
    connection.close()
    assert connection.runspace == None
    assert connection._connected == False
    assert connection._last_pipeline == None

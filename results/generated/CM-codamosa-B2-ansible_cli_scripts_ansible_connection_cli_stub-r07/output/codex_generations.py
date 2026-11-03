

# Generated at 2026-11-01 22:23:29.521027
# Unit test for method start of class ConnectionProcess

# Generated at 2026-11-01 22:26:16.130176
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    from unittest.mock import MagicMock, patch

    fd = StringIO()
    socket_path = '/tmp/.ansible_test_ConnectionProcess_start.sock'
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = 'keys/test_id_rsa'

    process = ConnectionProcess(
        fd,
        play_context,
        socket_path,
        os.getcwd(),
        task_uuid='aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
        ansible_playbook_pid=os.getpid(),
    )

    mock_connection = MagicMock()
    mock_connection.pop_messages.return_value = []

    with patch.object(connection_loader, 'get', return_value=mock_connection) as mock_get, \
            patch('sys.stdout', new=StringIO()):
        process.start({'ansible_user': 'tester'})

    # relative private key path should have been joined onto original_path
    assert play_context.private_key_file == os.path.join(os.getcwd(), 'keys/test_id_rsa')

    mock_get.assert_called_once_with(
        'local',
        play_context,
        '/dev/null',
        task_uuid='aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
        ansible_playbook_pid=process._ansible_playbook_pid,
    )
    mock_connection.set_options.assert_called_once_with(var_options={'ansible_user': 'tester'})
    assert mock_connection._socket_path == socket_path
    assert process.connection is mock_connection

    # the unix domain socket should have been bound and set listening
    process.sock.bind.assert_called_once_with(socket_path)
    process.sock.listen.assert_called_once_with(1)

    # the result payload written to the file descriptor
    result = json.loads(fd.getvalue())
    assert 'error' not in result
    assert result['messages'][0] == ['vvvv', 'control socket path is %s' % socket_path]
    assert ['vvvv', 'local domain socket listeners started successfully'] in result['messages']

# Generated at 2026-11-01 22:28:22.600372
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-11-01 22:29:54.754394
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-11-01 22:31:05.004143
# Unit test for method shutdown of class ConnectionProcess
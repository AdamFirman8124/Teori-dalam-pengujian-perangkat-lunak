

# Generated at 2026-11-01 20:56:22.468727
# Unit test for function read_stream
def test_read_stream():
    from io import BytesIO

    # Successful read with matching checksum
    data = b'hello world'
    stream = BytesIO(b'%d\n' % len(data) + data + to_bytes(hashlib.sha1(data).hexdigest()) + b'\n')
    assert module_0.read_stream(stream) == data

    # Empty payload
    data = b''
    stream = BytesIO(b'%d\n' % len(data) + data + to_bytes(hashlib.sha1(data).hexdigest()) + b'\n')
    assert module_0.read_stream(stream) == data

    # Escaped \r sequences are restored to real carriage returns
    data = b'line1\\rline2\\r'
    stream = BytesIO(b'%d\n' % len(data) + data + to_bytes(hashlib.sha1(data).hexdigest()) + b'\n')
    assert module_0.read_stream(stream) == b'line1\rline2\r'

    # EOF before data is complete raises an exception
    stream = BytesIO(b'20\nshort')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'EOF found before data was complete' in to_text(e)
    else:
        raise AssertionError("Expected 'EOF found before data was complete' exception")

    # Checksum mismatch raises an exception
    data = b'hello world'
    stream = BytesIO(b'%d\n' % len(data) + data + b'0' * 40 + b'\n')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'but data did not match checksum' in to_text(e)
    else:
        raise AssertionError("Expected 'did not match checksum' exception")

# Generated at 2026-11-01 20:56:47.558051
# Unit test for function read_stream
def test_read_stream():from io import BytesIO


# Generated at 2026-11-01 20:57:58.090252
# Unit test for method start of class ConnectionProcess

# Generated at 2026-11-01 20:59:15.729441
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import tempfile
    from io import StringIO
    from unittest.mock import patch, MagicMock

    socket_dir = tempfile.mkdtemp()
    socket_path = os.path.join(socket_dir, 'pc.sock')
    fd = StringIO()

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = 'id_rsa'
    original_path = '/tmp/ansible-test-cwd'

    mock_connection = MagicMock()
    mock_connection.pop_messages.return_value = []
    variables = {'ansible_connection': 'local'}

    with patch.object(connection_loader, 'get', return_value=mock_connection) as mock_get, \
            patch('sys.stdout', new=StringIO()):
        process = ConnectionProcess(fd, play_context, socket_path, original_path,
                                    task_uuid='task-uuid-1', ansible_playbook_pid=4242)
        process.start(variables)

    result = json.loads(fd.getvalue())

    assert 'error' not in result
    assert result['messages'] == [
        ['vvvv', 'control socket path is %s' % socket_path],
        ['vvvv', 'local domain socket listeners started successfully'],
    ]
    assert play_context.private_key_file == os.path.join(original_path, 'id_rsa')
    mock_get.assert_called_once_with(
        'local', play_context, '/dev/null',
        task_uuid='task-uuid-1', ansible_playbook_pid=4242)
    mock_connection.set_options.assert_called_once_with(var_options=variables)
    assert process.connection is mock_connection
    assert process.connection._socket_path == socket_path
    assert os.path.exists(socket_path)

    process.sock.close()
    os.remove(socket_path)
    os.rmdir(socket_dir)

# Generated at 2026-11-01 20:59:24.423788
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():
    '''
    Test the constructor of ConnectionProcess
    '''
    play_context = PlayContext()
    fd = StringIO()
    socket_path = '/tmp/ansible-connection-socket'
    original_path = '/tmp'
    task_uuid = 'task-uuid-1234'
    ansible_playbook_pid = 12345

    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path,
                                           task_uuid=task_uuid,
                                           ansible_playbook_pid=ansible_playbook_pid)

    # Verify attributes set in constructor
    assert connection_process.play_context == play_context
    assert connection_process.socket_path == socket_path
    assert connection_process.original_path == original_path
    assert connection_process._task_uuid == task_uuid
    assert connection_process.fd == fd
    assert connection_process.exception is None
    assert connection_process.sock is None
    assert connection_process.connection is None
    assert connection_process._ansible_playbook_pid == ansible_playbook_pid
    assert isinstance(connection_process.srv, JsonRpcServer)

    # Verify constructor works with default optional arguments
    connection_process_default = ConnectionProcess(fd, play_context, socket_path, original_path)
    assert connection_process_default._task_uuid is None
    assert connection_process_default._ansible_playbook_pid is None
    assert connection_process_default.exception is None
    assert connection_process_default.sock is None
    assert connection_process_default.connection is None
    assert isinstance(connection_process_default.srv, JsonRpcServer)

# Generated at 2026-11-01 20:59:50.025020
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():from unittest.mock import MagicMock, patch


# Generated at 2026-11-01 21:00:35.612141
# Unit test for function file_lock
def test_file_lock():
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_file_lock_')
    lock_path = os.path.join(tmpdir, 'test.lock')

    try:
        with patch('os.open', wraps=os.open) as mock_open, \
                patch('fcntl.lockf', wraps=fcntl.lockf) as mock_lockf, \
                patch('os.close', wraps=os.close) as mock_close:

            with module_0.file_lock(lock_path):
                # lock file should exist while the lock is held
                assert os.path.exists(lock_path)

                # opened with O_RDWR | O_CREAT and mode 0o600
                mock_open.assert_called_once_with(lock_path, os.O_RDWR | os.O_CREAT, 0o600)

                fd = mock_open.return_value
                # exclusive lock acquired on entry
                mock_lockf.assert_called_once_with(fd, fcntl.LOCK_EX)

            fd = mock_open.return_value
            # lock released exactly once more, then fd closed
            assert mock_lockf.call_count == 2
            mock_lockf.assert_any_call(fd, fcntl.LOCK_UN)
            mock_close.assert_called_once_with(fd)

        # an exception inside the block must still release the lock
        raised = False
        try:
            with module_0.file_lock(lock_path):
                raise RuntimeError('boom')
        except RuntimeError:
            raised = True
        assert raised, 'exception inside file_lock block was swallowed'

        # the same lock can be re-acquired afterwards (proves it was unlocked)
        with module_0.file_lock(lock_path):
            pass

        # nested/sequential usage works too
        with module_0.file_lock(lock_path):
            with module_0.file_lock(os.path.join(tmpdir, 'other.lock')):
                pass
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == '__main__':
    test_file_lock()
    print('test_file_lock passed')

# Generated at 2026-11-01 21:01:57.728183
# Unit test for method start of class ConnectionProcess

# Generated at 2026-11-01 21:03:35.631495
# Unit test for method start of class ConnectionProcess

# Generated at 2026-11-01 21:05:26.700489
# Unit test for method start of class ConnectionProcess
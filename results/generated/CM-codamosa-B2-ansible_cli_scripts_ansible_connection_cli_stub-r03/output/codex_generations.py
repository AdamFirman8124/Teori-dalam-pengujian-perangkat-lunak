

# Generated at 2026-10-25 11:08:43.733029
# Unit test for function main

# Generated at 2026-10-25 11:08:46.465321
# Unit test for function main

# Generated at 2026-10-25 11:08:48.883513
# Unit test for function main

# Generated at 2026-10-25 11:08:51.299305
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 11:08:53.714827
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 11:08:56.133170
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 11:08:58.550710
# Unit test for function main

# Generated at 2026-10-25 11:09:00.973531
# Unit test for function main

# Generated at 2026-10-25 11:09:03.900173
# Unit test for function main

# Generated at 2026-10-25 11:09:12.681412
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():
    fd = StringIO()
    play_context = object()
    socket_path = '/tmp/ansible-connection.sock'
    original_path = '/working/directory'
    task_uuid = 'test-task-uuid'
    ansible_playbook_pid = 12345

    process = ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path=socket_path,
        original_path=original_path,
        task_uuid=task_uuid,
        ansible_playbook_pid=ansible_playbook_pid,
    )

    assert process.fd is fd
    assert process.play_context is play_context
    assert process.socket_path == socket_path
    assert process.original_path == original_path
    assert process._task_uuid == task_uuid
    assert process._ansible_playbook_pid == ansible_playbook_pid

    assert process.exception is None
    assert isinstance(process.srv, JsonRpcServer)
    assert process.sock is None
    assert process.connection is None

# Generated at 2026-10-25 11:09:20.982110
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():
    fd = StringIO()
    play_context = object()
    socket_path = '/tmp/ansible-connection.sock'
    original_path = '/original/path'
    task_uuid = 'test-task-uuid'
    ansible_playbook_pid = 12345

    process = ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path=socket_path,
        original_path=original_path,
        task_uuid=task_uuid,
        ansible_playbook_pid=ansible_playbook_pid,
    )

    assert process.fd is fd
    assert process.play_context is play_context
    assert process.socket_path == socket_path
    assert process.original_path == original_path
    assert process._task_uuid == task_uuid
    assert process._ansible_playbook_pid == ansible_playbook_pid

    assert process.exception is None
    assert isinstance(process.srv, JsonRpcServer)
    assert process.sock is None
    assert process.connection is None

# Generated at 2026-10-25 11:09:55.978280
# Unit test for function file_lock
def test_file_lock():
    lock_path = "/tmp/test-file.lock"
    lock_fd = 42

    with patch.object(os, "open", return_value=lock_fd) as mock_open, \
            patch.object(fcntl, "lockf") as mock_lockf, \
            patch.object(os, "close") as mock_close:

        with module_0.file_lock(lock_path):
            mock_open.assert_called_once_with(
                lock_path, os.O_RDWR | os.O_CREAT, 0o600
            )
            mock_lockf.assert_called_once_with(lock_fd, fcntl.LOCK_EX)
            mock_close.assert_not_called()

        assert mock_lockf.call_args_list == [
            call(lock_fd, fcntl.LOCK_EX),
            call(lock_fd, fcntl.LOCK_UN),
        ]
        mock_close.assert_called_once_with(lock_fd)

# Generated at 2026-10-25 11:10:30.019361
# Unit test for function read_stream
def test_read_stream():
    payload = b'hello\\rworld'
    checksum = hashlib.sha1(payload).hexdigest().encode('ascii')
    stream = BytesIO(
        str(len(payload)).encode('ascii') + b'\n' +
        payload +
        checksum + b'\n'
    )

    assert module_0.read_stream(stream) == b'hello\rworld'


def test_read_stream_rejects_incomplete_data():
    stream = BytesIO(b'10\nabc')

    with pytest.raises(Exception, match='EOF found before data was complete'):
        module_0.read_stream(stream)


def test_read_stream_rejects_invalid_checksum():
    payload = b'hello'
    stream = BytesIO(
        str(len(payload)).encode('ascii') + b'\n' +
        payload +
        (b'0' * 40) + b'\n'
    )

    with pytest.raises(Exception, match='data did not match checksum'):
        module_0.read_stream(stream)

# Generated at 2026-10-25 11:11:19.557530
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 11:12:04.484113
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 11:12:06.901066
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 11:12:09.315248
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 11:12:12.074461
# Unit test for function main

# Generated at 2026-10-25 11:12:15.149761
# Unit test for function main

# Generated at 2026-10-25 11:12:19.757760
# Unit test for function main

# Generated at 2026-10-25 11:12:34.395023
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import shutil
    import tempfile
    from unittest.mock import MagicMock

    tmpdir = tempfile.mkdtemp()
    try:
        # Normal shutdown: socket and lock exist, log messages enabled
        socket_path = os.path.join(tmpdir, "test_socket")
        lock_path = os.path.join(tmpdir, ".ansible_pc_lock_test_socket")
        open(socket_path, "w").close()
        open(lock_path, "w").close()

        proc = ConnectionProcess.__new__(ConnectionProcess)
        proc.socket_path = socket_path
        proc.sock = MagicMock()
        proc.connection = MagicMock()
        proc.connection.get_option.return_value = True
        proc.connection.pop_messages.return_value = [("vvvv", "hello")]
        proc.connection._socket_path = socket_path
        proc.connection._connected = True

        proc.shutdown()

        proc.sock.close.assert_called_once_with()
        proc.connection.close.assert_called_once_with()
        proc.connection.get_option.assert_called_with("persistent_log_messages")
        proc.connection.pop_messages.assert_called_once_with()
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)
        assert proc.connection._socket_path is None
        assert proc.connection._connected is False

        # No socket file: sock/connection not closed, lock still removed
        socket_path2 = os.path.join(tmpdir, "missing_socket")
        lock_path2 = os.path.join(tmpdir, ".ansible_pc_lock_missing_socket")
        open(lock_path2, "w").close()

        proc2 = ConnectionProcess.__new__(ConnectionProcess)
        proc2.socket_path = socket_path2
        proc2.sock = MagicMock()
        proc2.connection = MagicMock()

        proc2.shutdown()

        proc2.sock.close.assert_not_called()
        proc2.connection.close.assert_not_called()
        assert not os.path.exists(lock_path2)

        # Exception during close is swallowed and files are still removed
        socket_path3 = os.path.join(tmpdir, "err_socket")
        lock_path3 = os.path.join(tmpdir, ".ansible_pc_lock_err_socket")
        open(socket_path3, "w").close()
        open(lock_path3, "w").close()

        proc3 = ConnectionProcess.__new__(ConnectionProcess)
        proc3.socket_path = socket_path3
        proc3.sock = MagicMock()
        proc3.sock.close.side_effect = Exception("boom")
        proc3.connection = MagicMock()
        proc3.connection._socket_path = socket_path3

        proc3.shutdown()

        proc3.sock.close.assert_called_once_with()
        assert not os.path.exists(socket_path3)
        assert not os.path.exists(lock_path3)
        assert proc3.connection._socket_path is None
        assert proc3.connection._connected is False

        # No sock and no connection, socket file exists
        socket_path4 = os.path.join(tmpdir, "bare_socket")
        open(socket_path4, "w").close()

        proc4 = ConnectionProcess.__new__(ConnectionProcess)
        proc4.socket_path = socket_path4
        proc4.sock = None
        proc4.connection = None

        try:
            proc4.shutdown()
        except AttributeError:
            # setattr on None connection in finally block
            pass
        assert not os.path.exists(socket_path4)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

# Generated at 2026-10-25 11:13:11.880073
# Unit test for function read_stream

# Generated at 2026-10-25 11:13:32.887804
# Unit test for function read_stream
def test_read_stream():import hashlib

# Generated at 2026-10-25 11:13:35.751994
# Unit test for function main

# Generated at 2026-10-25 11:13:38.620769
# Unit test for function main

# Generated at 2026-10-25 11:13:58.905571
# Unit test for function main

# Generated at 2026-10-25 11:14:39.436386
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 11:15:13.881420
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from unittest import mock


# Generated at 2026-10-25 11:15:39.325537
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 11:15:42.430196
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 11:15:48.666675
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 11:16:09.150761
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import shutil
    import tempfile
    from unittest.mock import MagicMock

    tmpdir = tempfile.mkdtemp()
    try:
        # Normal shutdown: socket and lock exist, log messages enabled
        socket_path = os.path.join(tmpdir, "test_socket")
        lock_path = os.path.join(tmpdir, ".ansible_pc_lock_test_socket")
        open(socket_path, "w").close()
        open(lock_path, "w").close()

        proc = ConnectionProcess.__new__(ConnectionProcess)
        proc.socket_path = socket_path
        proc.sock = MagicMock()
        proc.connection = MagicMock()
        proc.connection.get_option.return_value = True
        proc.connection.pop_messages.return_value = [("vvvv", "hello")]
        proc.connection._socket_path = socket_path
        proc.connection._connected = True

        proc.shutdown()

        proc.sock.close.assert_called_once_with()
        proc.connection.close.assert_called_once_with()
        proc.connection.get_option.assert_called_with("persistent_log_messages")
        proc.connection.pop_messages.assert_called_once_with()
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)
        assert proc.connection._socket_path is None
        assert proc.connection._connected is False

        # No socket file: sock/connection not closed, lock still removed
        socket_path2 = os.path.join(tmpdir, "missing_socket")
        lock_path2 = os.path.join(tmpdir, ".ansible_pc_lock_missing_socket")
        open(lock_path2, "w").close()

        proc2 = ConnectionProcess.__new__(ConnectionProcess)
        proc2.socket_path = socket_path2
        proc2.sock = MagicMock()
        proc2.connection = MagicMock()

        proc2.shutdown()

        proc2.sock.close.assert_not_called()
        proc2.connection.close.assert_not_called()
        assert not os.path.exists(lock_path2)

        # Exception during close is swallowed and files are still removed
        socket_path3 = os.path.join(tmpdir, "err_socket")
        lock_path3 = os.path.join(tmpdir, ".ansible_pc_lock_err_socket")
        open(socket_path3, "w").close()
        open(lock_path3, "w").close()

        proc3 = ConnectionProcess.__new__(ConnectionProcess)
        proc3.socket_path = socket_path3
        proc3.sock = MagicMock()
        proc3.sock.close.side_effect = Exception("boom")
        proc3.connection = MagicMock()
        proc3.connection._socket_path = socket_path3

        proc3.shutdown()

        proc3.sock.close.assert_called_once_with()
        assert not os.path.exists(socket_path3)
        assert not os.path.exists(lock_path3)
        assert proc3.connection._socket_path is None
        assert proc3.connection._connected is False

        # No sock and no connection, socket file exists
        socket_path4 = os.path.join(tmpdir, "bare_socket")
        open(socket_path4, "w").close()

        proc4 = ConnectionProcess.__new__(ConnectionProcess)
        proc4.socket_path = socket_path4
        proc4.sock = None
        proc4.connection = None

        try:
            proc4.shutdown()
        except AttributeError:
            # setattr on None connection in finally block
            pass
        assert not os.path.exists(socket_path4)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

# Generated at 2026-10-25 11:17:12.027033
# Unit test for function read_stream
def test_read_stream():
    from io import BytesIO

    def create_stream(data):
        # mimic the writer: escape loose \r characters, then frame with
        # size, data, and sha1 checksum of the escaped payload
        data = data.replace(b'\r', b'\\r')
        return BytesIO(b'%d\n%s%s\n' % (len(data), data, hashlib.sha1(data).hexdigest()))

    # simple valid payload
    stream = create_stream(b'{"key": "value"}')
    assert module_0.read_stream(stream) == b'{"key": "value"}'

    # empty payload
    stream = create_stream(b'')
    assert module_0.read_stream(stream) == b''

    # payload containing embedded newlines is read by size, not by line
    stream = create_stream(b'line1\nline2\nline3')
    assert module_0.read_stream(stream) == b'line1\nline2\nline3'

    # loose \r characters are escaped on the wire and restored after read
    stream = create_stream(b'line1\r\nline2\nline3\rend')
    assert module_0.read_stream(stream) == b'line1\r\nline2\nline3\rend'

    # EOF before data was complete raises an Exception
    stream = BytesIO(b'10\nshort')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'EOF found before data was complete' in to_text(e)
    else:
        raise AssertionError('expected Exception for EOF before data was complete')

    # checksum mismatch raises an Exception
    stream = BytesIO(b'5\nhello\n0123456789012345678901234567890123456789\n')

# Generated at 2026-10-25 11:17:33.733949
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 11:18:53.411299
# Unit test for method run of class ConnectionProcess
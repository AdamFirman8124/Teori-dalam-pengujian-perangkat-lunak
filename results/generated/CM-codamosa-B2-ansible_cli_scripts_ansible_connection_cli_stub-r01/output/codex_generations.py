

# Generated at 2026-10-25 01:59:43.821726
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    fd = MagicMock()
    play_context = MagicMock()
    play_context.connection = "network_cli"
    play_context.private_key_file = "keys/id_rsa"

    connection = MagicMock()
    sock = MagicMock()
    stdout = StringIO()
    stdout.write("connection loader output\n")

    process = connection_stub.ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path="/tmp/ansible-connection.sock",
        original_path="/working/directory",
        task_uuid="task-uuid",
        ansible_playbook_pid=1234,
    )
    process.srv = MagicMock()

    variables = {"ansible_user": "admin"}

    with patch.object(
        connection_stub.connection_loader,
        "get",
        return_value=connection,
    ) as loader_get, patch.object(
        connection_stub.socket,
        "socket",
        return_value=sock,
    ) as socket_factory, patch.object(
        connection_stub.sys,
        "stdout",
        stdout,
    ):
        process.start(variables)

    assert play_context.private_key_file == (
        "/working/directory/keys/id_rsa"
    )

    loader_get.assert_called_once_with(
        "network_cli",
        play_context,
        "/dev/null",
        task_uuid="task-uuid",
        ansible_playbook_pid=1234,
    )
    connection.set_options.assert_called_once_with(var_options=variables)
    assert connection._socket_path == "/tmp/ansible-connection.sock"

    process.srv.register.assert_called_once_with(connection)

    socket_factory.assert_called_once_with(
        connection_stub.socket.AF_UNIX,
        connection_stub.socket.SOCK_STREAM,
    )
    sock.bind.assert_called_once_with("/tmp/ansible-connection.sock")
    sock.listen.assert_called_once_with(1)

    fd.write.assert_called_once()
    fd.close.assert_called_once_with()

    result = json.loads(fd.write.call_args[0][0])

    assert "error" not in result
    assert "exception" not in result

# Generated at 2026-10-25 02:00:05.637830
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():from unittest.mock import MagicMock, call


def test_ConnectionProcess_shutdown(tmp_path, monkeypatch):
    socket_path = tmp_path / "control.sock"
    lock_path = tmp_path / ".ansible_pc_lock_control.sock"

    socket_path.touch()
    lock_path.touch()

    process = ConnectionProcess.__new__(ConnectionProcess)
    process.socket_path = str(socket_path)
    process.sock = MagicMock()
    process.connection = MagicMock()
    process.connection.get_option.return_value = True
    process.connection.pop_messages.return_value = [
        ("debug", "persistent connection message")
    ]

    mock_display = MagicMock()
    monkeypatch.setitem(globals(), "display", mock_display)

    process.shutdown()

    process.sock.close.assert_called_once_with()
    process.connection.close.assert_called_once_with()
    process.connection.get_option.assert_called_once_with(
        "persistent_log_messages"
    )
    process.connection.pop_messages.assert_called_once_with()

    assert process.connection._socket_path is None
    assert process.connection._connected is False
    assert not socket_path.exists()
    assert not lock_path.exists()

    mock_display.display.assert_has_calls([
        call("persistent connection message", log_only=True),
        call("shutdown complete", log_only=True),
    ])

# Generated at 2026-10-25 02:00:32.136158
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:00:50.480286
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():import pytest


# Generated at 2026-10-25 02:01:01.642806
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():
    fd = object()
    play_context = object()
    socket_path = '/tmp/ansible-connection.sock'
    original_path = '/working/directory'
    task_uuid = 'task-uuid'
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
    assert process.sock is None
    assert process.connection is None
    assert isinstance(process.srv, JsonRpcServer)

# Generated at 2026-10-25 02:01:04.406181
# Unit test for function read_stream
def test_read_stream():
    class TestReadStream(unittest.TestCase):
        def _make_stream(self, data):
            """Build a byte stream in the format read_stream expects:
            <size>\n<data><sha1 hex>\n"""
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            return buf

        def test_valid_stream(self):
            data = b"hello world"
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_empty_payload(self):
            data = b""
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_binary_payload(self):
            data = bytes(range(256))
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_escaped_carriage_return_restored(self):
            # Loose \r characters are escaped as literal "\r" (two chars)
            # on write; read_stream must restore them.
            data = b"line1\rline2\nline3"
            escaped = data.replace(b"\r", b"\\r")
            buf = BytesIO()
            buf.write(b"%d\n" % len(escaped))
            buf.write(escaped)
            buf.write(hashlib.sha1(escaped).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertEqual(module_0.read_stream(buf), data)

        def test_truncated_data_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data[:5])  # fewer bytes than declared
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_checksum_mismatch_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(b"0" * 40 + b"\n")  # wrong checksum
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_bad_size_line_raises(self):
            buf = BytesIO()
            buf.write(b"not-a-number\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

    return TestReadStream

# Generated at 2026-10-25 02:01:07.276564
# Unit test for function file_lock

# Generated at 2026-10-25 02:01:21.710185
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 02:01:54.582672
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    timeout = 30
    expected_message = (
        "command timeout triggered, timeout value is 30 secs.\n"
        "See the timeout setting options in the Network Debug and "
        "Troubleshooting Guide."
    )

    class FakeConnection(object):
        def __init__(self):
            self.requested_options = []

        def get_option(self, option):
            self.requested_options.append(option)
            return timeout

    class FakeDisplay(object):
        def __init__(self):
            self.calls = []

        def display(self, message, **kwargs):
            self.calls.append((message, kwargs))

    process = object.__new__(ConnectionProcess)
    process.connection = FakeConnection()
    fake_display = FakeDisplay()

    module_globals = sys.modules[ConnectionProcess.__module__].__dict__
    missing = object()
    original_display = module_globals.get("display", missing)
    module_globals["display"] = fake_display

    try:
        try:
            process.command_timeout(signal.SIGALRM, None)
        except Exception as exc:
            assert str(exc) == expected_message
        else:
            raise AssertionError("command_timeout did not raise an exception")
    finally:
        if original_display is missing:
            module_globals.pop("display", None)
        else:
            module_globals["display"] = original_display

    assert process.connection.requested_options == [
        "persistent_command_timeout"
    ]
    assert fake_display.calls == [
        (expected_message, {"log_only": True})
    ]

# Generated at 2026-10-25 02:01:57.000327
# Unit test for function main

# Generated at 2026-10-25 02:01:59.414940
# Unit test for function main

# Generated at 2026-10-25 02:02:02.368132
# Unit test for function main

# Generated at 2026-10-25 02:02:05.069594
# Unit test for function read_stream
def test_read_stream():
    class TestReadStream(unittest.TestCase):
        def _make_stream(self, data):
            """Build a byte stream in the format read_stream expects:
            <size>\n<data><sha1 hex>\n"""
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            return buf

        def test_valid_stream(self):
            data = b"hello world"
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_empty_payload(self):
            data = b""
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_binary_payload(self):
            data = bytes(range(256))
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_escaped_carriage_return_restored(self):
            # Loose \r characters are escaped as literal "\r" (two chars)
            # on write; read_stream must restore them.
            data = b"line1\rline2\nline3"
            escaped = data.replace(b"\r", b"\\r")
            buf = BytesIO()
            buf.write(b"%d\n" % len(escaped))
            buf.write(escaped)
            buf.write(hashlib.sha1(escaped).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertEqual(module_0.read_stream(buf), data)

        def test_truncated_data_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data[:5])  # fewer bytes than declared
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_checksum_mismatch_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(b"0" * 40 + b"\n")  # wrong checksum
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_bad_size_line_raises(self):
            buf = BytesIO()
            buf.write(b"not-a-number\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

    return TestReadStream

# Generated at 2026-10-25 02:02:07.729886
# Unit test for function main

# Generated at 2026-10-25 02:02:10.563825
# Unit test for function main

# Generated at 2026-10-25 02:02:13.336152
# Unit test for function main

# Generated at 2026-10-25 02:02:36.453245
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:38.870903
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:41.288718
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:43.866150
# Unit test for function main

# Generated at 2026-10-25 02:02:46.297220
# Unit test for function main

# Generated at 2026-10-25 02:02:48.705673
# Unit test for function main

# Generated at 2026-10-25 02:02:51.119758
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:53.535335
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:55.961239
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:02:58.375965
# Unit test for function main

# Generated at 2026-10-25 02:03:00.790535
# Unit test for function main

# Generated at 2026-10-25 02:03:03.205871
# Unit test for function main

# Generated at 2026-10-25 02:03:19.782262
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:03:21.119577
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():import pytest


# Generated at 2026-10-25 02:03:29.886712
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 02:03:38.627852
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():import pytest

# Generated at 2026-10-25 02:03:41.385378
# Unit test for function file_lock

# Generated at 2026-10-25 02:03:43.801698
# Unit test for function file_lock

# Generated at 2026-10-25 02:03:46.223827
# Unit test for function file_lock

# Generated at 2026-10-25 02:03:48.733582
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:03:51.149751
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:03:53.664757
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:03:56.081165
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:03:58.497893
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:04:00.921201
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:04:03.328827
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:04:05.742751
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 02:04:07.155838
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():import pytest


# Generated at 2026-10-25 02:04:09.985678
# Unit test for function main

# Generated at 2026-10-25 02:04:12.730987
# Unit test for function main

# Generated at 2026-10-25 02:04:15.533718
# Unit test for function main

# Generated at 2026-10-25 02:04:26.442369
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    from unittest.mock import MagicMock

    process = ConnectionProcess(
        fd=None,
        play_context=None,
        socket_path=None,
        original_path=None,
    )

    mock_display = MagicMock()
    handler_globals = ConnectionProcess.handler.__globals__
    previous_display = handler_globals.get('display')
    handler_globals['display'] = mock_display

    try:
        signum = signal.SIGTERM
        expected = 'signal handler called with signal %s.' % signum

        try:
            process.handler(signum, None)
            assert False, 'Expected module_0.handler() to raise an exception'
        except Exception as exc:
            assert str(exc) == expected

        mock_display.display.assert_called_once_with(expected, log_only=True)
    finally:
        if previous_display is None:
            handler_globals.pop('display', None)
        else:
            handler_globals['display'] = previous_display

# Generated at 2026-10-25 02:04:29.206496
# Unit test for function file_lock

# Generated at 2026-10-25 02:04:47.005808
# Unit test for function file_lock

# Generated at 2026-10-25 02:04:49.419853
# Unit test for function file_lock

# Generated at 2026-10-25 02:04:51.834920
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:04:54.249829
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:04:56.665565
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:04:59.079505
# Unit test for function main

# Generated at 2026-10-25 02:05:01.505134
# Unit test for function main

# Generated at 2026-10-25 02:05:03.919683
# Unit test for function main

# Generated at 2026-10-25 02:05:06.332330
# Unit test for function file_lock

# Generated at 2026-10-25 02:05:08.745827
# Unit test for function file_lock

# Generated at 2026-10-25 02:05:32.496298
# Unit test for function file_lock
def test_file_lock():import tempfile


# Generated at 2026-10-25 02:05:35.254718
# Unit test for function file_lock

# Generated at 2026-10-25 02:05:58.398420
# Unit test for function file_lock
def test_file_lock():import tempfile


# Generated at 2026-10-25 02:06:24.122237
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 02:06:48.165126
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():import tempfile

# Generated at 2026-10-25 02:06:50.892712
# Unit test for function read_stream
def test_read_stream():
    class TestReadStream(unittest.TestCase):
        def _make_stream(self, data):
            """Build a byte stream in the format read_stream expects:
            <size>\n<data><sha1 hex>\n"""
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            return buf

        def test_valid_stream(self):
            data = b"hello world"
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_empty_payload(self):
            data = b""
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_binary_payload(self):
            data = bytes(range(256))
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_escaped_carriage_return_restored(self):
            # Loose \r characters are escaped as literal "\r" (two chars)
            # on write; read_stream must restore them.
            data = b"line1\rline2\nline3"
            escaped = data.replace(b"\r", b"\\r")
            buf = BytesIO()
            buf.write(b"%d\n" % len(escaped))
            buf.write(escaped)
            buf.write(hashlib.sha1(escaped).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertEqual(module_0.read_stream(buf), data)

        def test_truncated_data_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data[:5])  # fewer bytes than declared
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_checksum_mismatch_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(b"0" * 40 + b"\n")  # wrong checksum
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_bad_size_line_raises(self):
            buf = BytesIO()
            buf.write(b"not-a-number\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

    return TestReadStream

# Generated at 2026-10-25 02:07:12.740683
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 02:07:14.284789
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 02:07:17.246682
# Unit test for function read_stream
def test_read_stream():
    class TestReadStream(unittest.TestCase):
        def _make_stream(self, data):
            """Build a byte stream in the format read_stream expects:
            <size>\n<data><sha1 hex>\n"""
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            return buf

        def test_valid_stream(self):
            data = b"hello world"
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_empty_payload(self):
            data = b""
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_binary_payload(self):
            data = bytes(range(256))
            stream = self._make_stream(data)
            self.assertEqual(module_0.read_stream(stream), data)

        def test_escaped_carriage_return_restored(self):
            # Loose \r characters are escaped as literal "\r" (two chars)
            # on write; read_stream must restore them.
            data = b"line1\rline2\nline3"
            escaped = data.replace(b"\r", b"\\r")
            buf = BytesIO()
            buf.write(b"%d\n" % len(escaped))
            buf.write(escaped)
            buf.write(hashlib.sha1(escaped).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertEqual(module_0.read_stream(buf), data)

        def test_truncated_data_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data[:5])  # fewer bytes than declared
            buf.write(hashlib.sha1(data).hexdigest().encode() + b"\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_checksum_mismatch_raises(self):
            data = b"hello world"
            buf = BytesIO()
            buf.write(b"%d\n" % len(data))
            buf.write(data)
            buf.write(b"0" * 40 + b"\n")  # wrong checksum
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

        def test_bad_size_line_raises(self):
            buf = BytesIO()
            buf.write(b"not-a-number\n")
            buf.seek(0)
            self.assertRaises(Exception, read_stream, buf)

    return TestReadStream

# Generated at 2026-10-25 02:08:06.462583
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import shutil
    import tempfile
    from unittest import mock

    from ansible.persistent.connection import ConnectionProcess

    tmp_dir = tempfile.mkdtemp(prefix='ansible_pc_test_')
    try:
        socket_path = os.path.join(tmp_dir, 'test_socket')
        lock_path = os.path.join(tmp_dir, '.ansible_pc_lock_test_socket')

        # Create fake socket file and lock file on disk
        with open(socket_path, 'w'):
            pass
        with open(lock_path, 'w'):
            pass

        fd = mock.MagicMock()
        play_context = mock.MagicMock()
        original_path = tmp_dir

        process = ConnectionProcess(fd, play_context, socket_path, original_path)

        mock_connection = mock.MagicMock()
        mock_connection.get_option.return_value = False
        mock_connection.pop_messages.return_value = []
        mock_sock = mock.MagicMock()

        process.connection = mock_connection
        process.sock = mock_sock

        with mock.patch('ansible.persistent.connection.display') as mock_display:
            process.shutdown()

        # connection and socket must be closed
        mock_connection.close.assert_called_once_with()
        mock_sock.close.assert_called_once_with()

        # socket file removed, connection state reset
        assert not os.path.exists(socket_path)
        assert mock_connection._socket_path is None
        assert mock_connection._connected is False

        # lock file removed
        assert not os.path.exists(lock_path)

        # shutdown completion logged
        mock_display.display.assert_called_with('shutdown complete', log_only=True)

        # Scenario 2: missing socket path should not raise and should not close sock
        missing_socket_path = os.path.join(tmp_dir, 'missing_socket')
        missing_lock_path = os.path.join(tmp_dir, '.ansible_pc_lock_missing_socket')
        with open(missing_lock_path, 'w'):
            pass

        process2 = ConnectionProcess(fd, play_context, missing_socket_path, original_path)
        process2.connection = mock.MagicMock()
        process2.sock = mock.MagicMock()

        with mock.patch('ansible.persistent.connection.display'):
            process2.shutdown()

        process2.sock.close.assert_not_called()
        process2.connection.close.assert_not_called()
        assert not os.path.exists(missing_lock_path)
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

# Generated at 2026-10-25 02:08:25.782181
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import shutil
    import tempfile

    class FakeSocket(object):
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    class FakeConnection(object):
        def __init__(self):
            self.closed = False
            self._socket_path = 'old-socket-path'
            self._connected = True

        def close(self):
            self.closed = True

        def get_option(self, option):
            assert option == 'persistent_log_messages'
            return True

        def pop_messages(self):
            return [
                ('debug', 'first message'),
                ('vvvv', 'second message'),
            ]

    class FakeDisplay(object):
        def __init__(self):
            self.messages = []

        def display(self, message, **kwargs):
            self.messages.append((message, kwargs))

    temporary_directory = tempfile.mkdtemp()
    socket_path = os.path.join(temporary_directory, 'control.sock')
    lock_path = unfrackpath(
        "%s/.ansible_pc_lock_%s" % os.path.split(socket_path)
    )

    # Regular files are sufficient because shutdown only checks for their
    # existence and removes them.
    open(socket_path, 'wb').close()
    open(lock_path, 'wb').close()

    process = ConnectionProcess(
        fd=None,
        play_context=None,
        socket_path=socket_path,
        original_path=temporary_directory,
    )
    process.sock = FakeSocket()
    process.connection = FakeConnection()

    fake_display = FakeDisplay()
    namespace = ConnectionProcess.shutdown.__globals__
    missing = object()
    original_display = namespace.get('display', missing)
    namespace['display'] = fake_display

    try:
        process.shutdown()

        assert process.sock.closed is True
        assert process.connection.closed is True
        assert process.connection._socket_path is None
        assert process.connection._connected is False

        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        assert fake_display.messages == [
            ('first message', {'log_only': True}),
            ('second message', {'log_only': True}),
            ('shutdown complete', {'log_only': True}),
        ]
    finally:
        if original_display is missing:
            namespace.pop('display', None)
        else:
            namespace['display'] = original_display

        shutil.rmtree(temporary_directory, ignore_errors=True)

# Generated at 2026-10-25 02:08:28.621371
# Unit test for function file_lock

# Generated at 2026-10-25 02:08:40.786558
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 02:09:09.460927
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:09:11.876769
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:09:14.292711
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 02:09:17.035136
# Unit test for function file_lock

# Generated at 2026-10-25 02:09:19.450443
# Unit test for function file_lock

# Generated at 2026-10-25 02:09:28.315282
# Unit test for function file_lock
def test_file_lock():import tempfile

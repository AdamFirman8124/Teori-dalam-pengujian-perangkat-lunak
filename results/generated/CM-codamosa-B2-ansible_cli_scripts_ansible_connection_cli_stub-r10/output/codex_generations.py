

# Generated at 2026-10-25 01:49:11.438663
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:49:22.970000
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():import sys

# Generated at 2026-10-25 01:49:31.461612
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
    assert isinstance(process.srv, JsonRpcServer)
    assert process.sock is None
    assert process.connection is None

# Generated at 2026-10-25 01:49:49.997512
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
            self._socket_path = 'original_socket_path'
            self._connected = True
            self.messages_popped = False

        def close(self):
            self.closed = True

        def get_option(self, option):
            assert option == 'persistent_log_messages'
            return True

        def pop_messages(self):
            self.messages_popped = True
            return [('debug', 'connection log message')]

    class FakeDisplay(object):
        def __init__(self):
            self.messages = []

        def display(self, message, log_only=False):
            self.messages.append((message, log_only))

    temp_dir = tempfile.mkdtemp()
    socket_path = os.path.join(temp_dir, 'control.sock')
    lock_path = os.path.join(temp_dir, '.ansible_pc_lock_control.sock')

    # module_0.shutdown() only requires these paths to exist; they do not need to be
    # real socket or lock objects.
    open(socket_path, 'w').close()
    open(lock_path, 'w').close()

    fake_socket = FakeSocket()
    fake_connection = FakeConnection()
    fake_display = FakeDisplay()

    process = ConnectionProcess(
        fd=None,
        play_context=None,
        socket_path=socket_path,
        original_path=None,
    )
    process.sock = fake_socket
    process.connection = fake_connection

    namespace = globals()
    had_display = 'display' in namespace
    original_display = namespace.get('display')
    namespace['display'] = fake_display

    try:
        process.shutdown()

        assert fake_socket.closed is True
        assert fake_connection.closed is True
        assert fake_connection.messages_popped is True
        assert fake_connection._socket_path is None
        assert fake_connection._connected is False

        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        assert ('connection log message', True) in fake_display.messages
        assert ('shutdown complete', True) in fake_display.messages
    finally:
        if had_display:
            namespace['display'] = original_display
        else:
            namespace.pop('display', None)

        shutil.rmtree(temp_dir, ignore_errors=True)

# Generated at 2026-10-25 01:50:10.419344
# Unit test for function file_lock

# Generated at 2026-10-25 01:50:18.872370
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 01:50:42.631560
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    class RecordingFD(object):
        def __init__(self):
            self.data = ''
            self.closed = False

        def write(self, data):
            self.data += data

        def close(self):
            self.closed = True

    play_context = MagicMock()
    play_context.connection = 'network_cli'
    play_context.private_key_file = 'keys/id_rsa'

    fd = RecordingFD()
    connection = MagicMock()
    connection._socket_path = None

    rpc_server = MagicMock()
    unix_socket = MagicMock()
    fake_stdout = MagicMock()
    fake_stdout.getvalue.return_value = 'connection plugin initialized\n'

    process = ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path='/tmp/ansible-connection.sock',
        original_path='/working/directory',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    process.srv = rpc_server

    variables = {'ansible_user': 'admin'}

    with patch.object(
        connection_loader, 'get', return_value=connection
    ) as loader_get, patch.object(
        socket, 'socket', return_value=unix_socket
    ) as socket_factory, patch.object(
        sys, 'stdout', fake_stdout
    ):
        process.start(variables)

    loader_get.assert_called_once_with(
        'network_cli',
        play_context,
        '/dev/null',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    connection.set_options.assert_called_once_with(var_options=variables)

    assert play_context.private_key_file == \
        '/working/directory/keys/id_rsa'
    assert connection._socket_path == '/tmp/ansible-connection.sock'

    rpc_server.register.assert_called_once_with(connection)

    socket_factory.assert_called_once_with(
        socket.AF_UNIX,
        socket.SOCK_STREAM,
    )
    unix_socket.bind.assert_called_once_with(
        '/tmp/ansible-connection.sock'
    )

# Generated at 2026-10-25 01:51:04.229489
# Unit test for function main

# Generated at 2026-10-25 01:51:06.767762
# Unit test for function main

# Generated at 2026-10-25 01:51:09.182608
# Unit test for function main

# Generated at 2026-10-25 01:51:11.598001
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 01:51:14.014566
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 01:51:16.428997
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 01:52:08.441778
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:52:11.140147
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:52:13.555216
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:52:16.089126
# Unit test for function file_lock

# Generated at 2026-10-25 01:52:18.599133
# Unit test for function file_lock

# Generated at 2026-10-25 01:52:21.013245
# Unit test for function file_lock

# Generated at 2026-10-25 01:52:23.428654
# Unit test for function main

# Generated at 2026-10-25 01:52:57.501781
# Unit test for function main

# Generated at 2026-10-25 01:53:00.266775
# Unit test for function main

# Generated at 2026-10-25 01:53:26.278433
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:53:43.674743
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from types import SimpleNamespace
from unittest.mock import patch

events = []
sent = []

class FakeConnection:
    def __init__(self):
        self._conn_closed = False
        self.connected = True

    def get_option(self, name):
        return {
            'persistent_log_messages': False,
            'persistent_connect_timeout': 10,
            'persistent_command_timeout': 20,
        }[name]

class FakeClientSocket:
    def close(self):
        events.append('client_closed')

class FakeListeningSocket:
    def accept(self):
        events.append('accepted')
        return FakeClientSocket(), None

class FakeServer:
    def handle_request(self, data):
        events.append(('request', data))
        return '{"result": "ok"}'

connection = FakeConnection()
responses = iter([b'{"method": "ping"}', b''])

def fake_recv_data(sock):
    data = next(responses)
    if not data:
        connection._conn_closed = True
    return data

def fake_send_data(sock, data):
    sent.append(data)

process = ConnectionProcess.__new__(ConnectionProcess)
process.connection = connection
process.sock = FakeListeningSocket()
process.srv = FakeServer()
process.exception = None
process.shutdown = lambda: events.append('shutdown')

fake_signal = SimpleNamespace(
    SIGALRM=14,
    SIGTERM=15,
    signal=lambda signum, handler: events.append(('signal', signum)),
    alarm=lambda seconds: events.append(('alarm', seconds)),
)
fake_time = SimpleNamespace(sleep=lambda seconds: events.append(('sleep', seconds)))

with patch.dict(
    ConnectionProcess.run.__globals__,
    {
        'recv_data': fake_recv_data,
        'send_data': fake_send_data,
        'signal': fake_signal,
        'time': fake_time,
    },
):
    result = process.run()

assert result is None
assert process.exception is None
assert sent == [b'{"result": "ok"}']
assert ('request', b'{"method": "ping"}') in events
assert 'client_closed' in events
assert 'shutdown' in events

# Generated at 2026-10-25 01:53:46.540321
# Unit test for function file_lock

# Generated at 2026-10-25 01:54:14.575250
# Unit test for function file_lock
def test_file_lock():import subprocess

# Generated at 2026-10-25 01:54:17.458465
# Unit test for function main

# Generated at 2026-10-25 01:54:19.995521
# Unit test for function main

# Generated at 2026-10-25 01:54:22.407501
# Unit test for function main

# Generated at 2026-10-25 01:54:24.821066
# Unit test for function read_stream

# Generated at 2026-10-25 01:54:27.236964
# Unit test for function read_stream

# Generated at 2026-10-25 01:54:29.651082
# Unit test for function read_stream

# Generated at 2026-10-25 01:54:32.066151
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 01:54:34.480622
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 01:54:36.895710
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 01:54:39.310065
# Unit test for function file_lock

# Generated at 2026-10-25 01:54:46.141668
# Unit test for function file_lock
def test_file_lock():import tempfile


# Generated at 2026-10-25 01:55:05.084361
# Unit test for function main

# Generated at 2026-10-25 01:55:07.960512
# Unit test for function main

# Generated at 2026-10-25 01:55:10.718655
# Unit test for function main

# Generated at 2026-10-25 01:55:29.971993
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:55:54.542463
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():import json

# Generated at 2026-10-25 01:56:23.677648
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

# Generated at 2026-10-25 01:56:26.401877
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

# Generated at 2026-10-25 01:56:45.958076
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 01:57:03.150744
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():import sys

# Generated at 2026-10-25 01:57:06.020966
# Unit test for function main

# Generated at 2026-10-25 01:57:08.718874
# Unit test for function main

# Generated at 2026-10-25 01:57:11.656180
# Unit test for function main

# Generated at 2026-10-25 01:57:39.505635
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 01:57:41.922969
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 01:57:44.337716
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 01:57:46.752317
# Unit test for function read_stream

# Generated at 2026-10-25 01:57:52.506268
# Unit test for function read_stream
def test_read_stream():import io

# Generated at 2026-10-25 01:57:55.337040
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

# Generated at 2026-10-25 01:57:58.039734
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

# Generated at 2026-10-25 01:58:00.902641
# Unit test for function file_lock

# Generated at 2026-10-25 01:58:15.342315
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 01:58:18.114061
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

# Generated at 2026-10-25 01:58:43.094515
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    try:
        from unittest.mock import MagicMock, patch
    except ImportError:
        from mock import MagicMock, patch

    fd = MagicMock()

    play_context = MagicMock()
    play_context.connection = 'network_cli'
    play_context.private_key_file = 'keys/id_rsa'

    connection = MagicMock()
    sock = MagicMock()
    server = MagicMock()

    process = ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path='/tmp/ansible-connection.sock',
        original_path='/work/project',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    process.srv = server

    variables = {'ansible_user': 'admin'}

    with patch.object(
        connection_loader, 'get', return_value=connection
    ) as connection_get, patch.object(
        socket, 'socket', return_value=sock
    ) as socket_factory, patch.object(
        sys, 'stdout', StringIO('connection plugin output\n')
    ):
        process.start(variables)

    assert play_context.private_key_file == '/work/project/keys/id_rsa'

    connection_get.assert_called_once_with(
        'network_cli',
        play_context,
        '/dev/null',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    connection.set_options.assert_called_once_with(var_options=variables)
    assert connection._socket_path == '/tmp/ansible-connection.sock'

    server.register.assert_called_once_with(connection)

    socket_factory.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind.assert_called_once_with('/tmp/ansible-connection.sock')
    sock.listen.assert_called_once_with(1)

    fd.write.assert_called_once()
    fd.close.assert_called_once_with()

    result = json.loads(fd.write.call_args[0][0])

    assert 'error' not in result
    assert 'exception' not in result
    assert result['messages'] == [
        ['vvvv', 'control socket path is /tmp/ansible-connection.sock'],
        ['vvvv', 'connection plugin output'],
        ['vvvv', 'local domain socket listeners started successfully'],
    ]

# Generated at 2026-10-25 01:58:45.512201
# Unit test for function file_lock

# Generated at 2026-10-25 01:58:47.927181
# Unit test for function file_lock

# Generated at 2026-10-25 01:58:50.341879
# Unit test for function file_lock

# Generated at 2026-10-25 01:58:52.759038
# Unit test for function file_lock

# Generated at 2026-10-25 01:58:55.174538
# Unit test for function file_lock

# Generated at 2026-10-25 01:59:06.133864
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-25 01:59:23.542287
# Unit test for method shutdown of class ConnectionProcess
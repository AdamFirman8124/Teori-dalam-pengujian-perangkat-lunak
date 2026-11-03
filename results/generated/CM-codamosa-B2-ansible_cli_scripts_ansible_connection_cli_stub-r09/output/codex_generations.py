

# Generated at 2026-11-01 21:53:54.571476
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-11-01 21:55:34.612115
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import tempfile

    if 'display' not in globals():
        globals()['display'] = Display()

    class FakeConnection(object):
        def __init__(self):
            self.close_called = False
            self._socket_path = 'placeholder'
            self._connected = True

        def close(self):
            self.close_called = True

        def get_option(self, option):
            return False

    tmpdir = tempfile.mkdtemp()
    socket_path = os.path.join(tmpdir, 'test_persist_socket')

    process = ConnectionProcess(StringIO(), PlayContext(), socket_path, tmpdir)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(socket_path)
    process.sock = sock
    process.connection = FakeConnection()

    lock_path = unfrackpath('%s/.ansible_pc_lock_%s' % os.path.split(socket_path))
    open(lock_path, 'w').close()

    assert os.path.exists(socket_path)
    assert os.path.exists(lock_path)

    process.shutdown()

    assert process.connection.close_called is True
    assert os.path.exists(socket_path) is False
    assert os.path.exists(lock_path) is False
    assert process.connection._socket_path is None
    assert process.connection._connected is False

# Generated at 2026-11-01 21:56:51.659529
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    import os
    from io import StringIO
    from unittest.mock import MagicMock, patch

    import pytest

    from ansible.plugins.connection.persisted_connection import ConnectionProcess
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_text

    pc = PlayContext()
    fd = StringIO()
    socket_path = '/tmp/ansible_test_socket_path'
    original_path = os.getcwd()

    cp = ConnectionProcess(fd, pc, socket_path, original_path)
    cp.connection = MagicMock()
    cp.connection.get_option.return_value = 10

    expected_msg = ('command timeout triggered, timeout value is 10 secs.\n'
                    'See the timeout setting options in the Network Debug and Troubleshooting Guide.')

    with patch('ansible.plugins.connection.persisted_connection.display.display') as mock_display:
        with pytest.raises(Exception) as excinfo:
            cp.command_timeout('signum', 'frame')

    assert to_text(excinfo.value) == expected_msg
    cp.connection.get_option.assert_called_with('persistent_command_timeout')
    mock_display.assert_called_once_with(expected_msg, log_only=True)

# Generated at 2026-11-01 21:57:36.306252
# Unit test for function read_stream
def test_read_stream():
    """Ensure read_stream returns the original data when the checksum matches."""
    data = b'{"jsonrpc": "2.0", "result": "success"}'
    byte_stream = io.BytesIO(
        b'%d\n%s\n%s\n' % (len(data), data, hashlib.sha1(data).hexdigest().encode())
    )
    assert module_0.read_stream(byte_stream) == data


def test_read_stream_empty_data():
    data = b''

# Generated at 2026-11-01 21:59:20.856774
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-11-01 22:00:50.454698
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import tempfile
    from unittest import mock

    from ansible.playbook.play_context import PlayContext

# Generated at 2026-11-01 22:01:29.272542
# Unit test for function read_stream
def test_read_stream():
    import io

    # Valid stream with plain data
    data = b"hello world"
    stream = io.BytesIO(to_bytes("{0}\n".format(len(data))) + data + to_bytes(hashlib.sha1(data).hexdigest() + "\n"))
    assert module_0.read_stream(stream) == data

    # Valid stream with empty data
    data = b""
    stream = io.BytesIO(to_bytes("{0}\n".format(len(data))) + data + to_bytes(hashlib.sha1(data).hexdigest() + "\n"))
    assert module_0.read_stream(stream) == data

    # Valid stream containing newlines in the payload
    data = b"line1\nline2\n"
    stream = io.BytesIO(to_bytes("{0}\n".format(len(data))) + data + to_bytes(hashlib.sha1(data).hexdigest() + "\n"))
    assert module_0.read_stream(stream) == data

    # Escaped loose \r sequences are restored to real carriage returns
    data = b"line1\\rline2\\r"
    stream = io.BytesIO(to_bytes("{0}\n".format(len(data))) + data + to_bytes(hashlib.sha1(data).hexdigest() + "\n"))
    assert module_0.read_stream(stream) == b"line1\rline2\r"

    # EOF before data is complete raises an exception
    stream = io.BytesIO(b"100\nshort")
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert "EOF found before data was complete" in str(e)
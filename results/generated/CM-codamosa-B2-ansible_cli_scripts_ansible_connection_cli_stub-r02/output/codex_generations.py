

# Generated at 2026-11-02 17:47:48.262565
# Unit test for function main
def test_main():
    # Mock sys.stdin as a byte stream
    vars_data = cPickle.dumps({'ansible_connection': 'local'})
    init_data = cPickle.dumps(PlayContext().serialize())
    mock_stdin = StringIO()
    mock_stdin.buffer = mock_stdin

    with patch('sys.stdin', mock_stdin), \
         patch('ansible.module_utils.service.fork_process') as mock_fork, \
         patch('ansible.plugins.loader.connection_loader.get') as mock_conn_loader, \
         patch('ansible.utils.path.makedirs_safe'), \
         patch('ansible.utils.path.unfrackpath') as mock_unfrackpath, \
         patch('os.path.exists') as mock_exists, \
         patch('os.getcwd') as mock_getcwd, \
         patch('os.pipe') as mock_pipe, \
         patch('os.fdopen') as mock_fdopen, \
         patch('os.close'), \
         patch('sys.argv', ['ansible-connection', '12345', 'abc-123']), \
         patch('sys.exit') as mock_exit:

        mock_unfrackpath.side_effect = lambda p: p
        mock_getcwd.return_value = '/tmp'
        mock_exists.return_value = False

        # Setup mock connection class
        mock_ssh = MagicMock()
        mock_ssh._create_control_path.return_value = '%(directory)s/%(socket)s'
        mock_conn_loader.return_value = mock_ssh

        # Setup fork_process to return a child pid
        mock_fork.return_value = 12345

        # Setup pipe
        mock_pipe.return_value = (10, 11)
        mock_rfd = MagicMock()
        mock_rfd.read.return_value = json.dumps({
            'messages': [],
            'socket_path': '/tmp/socket'
        })
        mock_fdopen.return_value = mock_rfd

        # Set stdin data
        mock_stdin.write(read_stream(io.BytesIO(vars_data)) if False else '')
        mock_stdin.seek(0)

        # Mock read_stream to return pickled data
        with patch.object(sys.modules[__name__], 'read_stream') as mock_read_stream:
            mock_read_stream.side_effect = [vars_data, init_data]

            # Mock sys.stdout to capture output
            saved_stdout = sys.stdout
            sys.stdout = StringIO()

            try:
                module_0.main()
            except SystemExit:
                pass
            finally:
                sys.stdout = saved_stdout

        mock_exit.assert_called_once_with(0)

# Generated at 2026-11-02 17:49:17.550954
# Unit test for function file_lock
def test_file_lock():
    import tempfile
    from unittest.mock import patch, call

    lock_path = '/tmp/ansible_test_file_lock'
    fake_fd = 42

    # Normal operation: lock acquired on enter, released and fd closed on exit
    with patch('os.open', return_value=fake_fd) as mock_open, \
            patch('fcntl.lockf') as mock_lockf, \
            patch('os.close') as mock_close:
        with module_0.file_lock(lock_path):
            mock_open.assert_called_once_with(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
            mock_lockf.assert_called_once_with(fake_fd, fcntl.LOCK_EX)

        assert mock_lockf.call_args_list == [
            call(fake_fd, fcntl.LOCK_EX),
            call(fake_fd, fcntl.LOCK_UN),
        ]
        mock_close.assert_called_once_with(fake_fd)

    # Exception safety: lock still released and fd closed when body raises
    with patch('os.open', return_value=fake_fd), \
            patch('fcntl.lockf') as mock_lockf, \
            patch('os.close') as mock_close:
        try:
            with module_0.file_lock(lock_path):
                raise RuntimeError('boom')
        except RuntimeError:
            pass
        else:
            raise AssertionError('expected RuntimeError to propagate')

        assert mock_lockf.call_args_list == [
            call(fake_fd, fcntl.LOCK_EX),
            call(fake_fd, fcntl.LOCK_UN),
        ]
        mock_close.assert_called_once_with(fake_fd)

    # Integration check with a real lock file: it is created and cleaned up
    lock_dir = tempfile.mkdtemp()
    real_path = os.path.join(lock_dir, 'lockfile')
    try:
        with module_0.file_lock(real_path):
            assert os.path.exists(real_path)
        # Re-acquiring after release must succeed (no deadlock)
        with module_0.file_lock(real_path):
            assert os.path.exists(real_path)
    finally:
        if os.path.exists(real_path):
            os.remove(real_path)
        os.rmdir(lock_dir)

# Generated at 2026-11-02 17:51:43.372722
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():"""Test connect_timeout of ConnectionProcess"""

# Generated at 2026-11-02 17:54:22.419418
# Unit test for function main
def test_main():import json
import os
import sys
import hashlib
import errno
import signal
import time
import traceback
import fcntl
from io import StringIO
from unittest.mock import MagicMock, patch, mock_open, PropertyMock
from contextlib import contextmanager

import pytest

from ansible.module_utils.service import fork_process
from ansible.parsing.ajson import AnsibleJSONEncoder, AnsibleJSONDecoder
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import connection_loader
from ansible.utils.path import unfrackpath, makedirs_safe
from ansible.utils.display import Display
from ansible.utils.jsonrpc import JsonRpcServer


def _make_stream_data(vars_data, init_data):
    """Helper to create byte stream data with length prefix and hash."""
    def _encode(data):
        data_bytes = data if isinstance(data, bytes) else data.encode()
        size = len(data_bytes)
        data_hash = hashlib.sha1(data_bytes).hexdigest()
        return b"%d\n%s\n%s\n" % (size, data_bytes, to_bytes(data_hash))
    return _encode(vars_data) + _encode(init_data)


@patch('ansible.module_utils.persistent_connection.sys.exit')
@patch('ansible.module_utils.persistent_connection.sys.stdout', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.sys.stderr', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.os.getcwd')
@patch('ansible.module_utils.persistent_connection.fork_process')
@patch('ansible.module_utils.persistent_connection.os.pipe')
@patch('ansible.module_utils.persistent_connection.makedirs_safe')
@patch('ansible.module_utils.persistent_connection.unfrackpath')
@patch('ansible.module_utils.persistent_connection.connection_loader')
@patch('ansible.module_utils.persistent_connection.PlayContext')
@patch('ansible.module_utils.persistent_connection.file_lock')
@patch('ansible.module_utils.persistent_connection.os.path.exists')
def test_main(mock_exists, mock_file_lock, mock_play_context, mock_connection_loader,
              mock_unfrackpath, mock_makedirs_safe, mock_pipe, mock_fork_process,
              mock_getcwd, mock_stderr, mock_stdout, mock_exit):
    """Test that module_0.main() runs successfully in the parent process path."""
    # Setup mocks
    mock_exists.return_value = False
    mock_file_lock.return_value.__enter__ = MagicMock()
    mock_file_lock.return_value.__exit__ = MagicMock(return_value=False)

    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.remote_user = 'test'
    play_context.connection = 'ssh'
    play_context.verbosity = 0
    play_context.private_key_file = None
    mock_play_context.return_value = play_context

    mock_unfrackpath.side_effect = lambda path: path
    mock_getcwd.return_value = '/tmp'

    r_fd, w_fd = 10, 11
    mock_pipe.return_value = (r_fd, w_fd)
    mock_fork_process.return_value = 1  # simulate parent process

    mock_ssh = MagicMock()
    mock_ssh._create_control_path.return_value = '%(directory)s/.ansible_pc_%(user)s@%(host)s:%(port)s'
    mock_connection_loader.get.return_value = mock_ssh

    # Prepare stdin data
    vars_data = {'ANSIBLE_NET_USERNAME': 'test'}
    pc_data = play_context.serialize()
    stdin_data = _make_stream_data(cPickle.dumps(vars_data), cPickle.dumps(pc_data))

    mock_stdin = MagicMock()
    mock_stdin.buffer = MagicMock()
    mock_stdin.buffer.readline.side_effect = [
        to_bytes(str(len(cPickle.dumps(vars_data)))) + b'\n',
        to_bytes(str(len(cPickle.dumps(pc_data)))) + b'\n',
    ]
    mock_stdin.buffer.read.side_effect = [
        cPickle.dumps(vars_data),
        cPickle.dumps(pc_data),
    ]

    # Simulate parent reading from pipe
    parent_result = {'messages': [], 'socket_path': '/tmp/.ansible_pc_test@127.0.0.1:22'}

    with patch('ansible.module_utils.persistent_connection.sys.stdin', mock_stdin), \
         patch('ansible.module_utils.persistent_connection.os.fdopen') as mock_fdopen, \
         patch('ansible.module_utils.persistent_connection.os.close') as mock_close:

        mock_rfd = MagicMock()
        mock_rfd.read.return_value = json.dumps(parent_result, cls=AnsibleJSONEncoder)
        mock_wfd = MagicMock()
        mock_fdopen.side_effect = [mock_wfd, mock_rfd]

        # Call main
        import ansible.module_utils.persistent_connection as pc_module
        pc_module.main()

    # Verify exit was called
    mock_exit.assert_called_once()
    assert mock_exit.call_args[0][0] == 0


@patch('ansible.module_utils.persistent_connection.sys.exit')
@patch('ansible.module_utils.persistent_connection.sys.stdout', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.sys.stderr', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.os.getcwd')
@patch('ansible.module_utils.persistent_connection.fork_process')
@patch('ansible.module_utils.persistent_connection.os.pipe')
@patch('ansible.module_utils.persistent_connection.makedirs_safe')
@patch('ansible.module_utils.persistent_connection.unfrackpath')
@patch('ansible.module_utils.persistent_connection.connection_loader')
@patch('ansible.module_utils.persistent_connection.PlayContext')
@patch('ansible.module_utils.persistent_connection.file_lock')
@patch('ansible.module_utils.persistent_connection.os.path.exists')
def test_main_fork_child_process(mock_exists, mock_file_lock, mock_play_context, mock_connection_loader,
                                 mock_unfrackpath, mock_makedirs_safe, mock_pipe, mock_fork_process,
                                 mock_getcwd, mock_stderr, mock_stdout, mock_exit):
    """Test module_0.main() when running in the child process (pid == 0)."""
    mock_exists.return_value = False
    mock_file_lock.return_value.__enter__ = MagicMock()
    mock_file_lock.return_value.__exit__ = MagicMock(return_value=False)

    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.remote_user = 'test'
    play_context.connection = 'ssh'
    play_context.verbosity = 0
    play_context.private_key_file = None
    mock_play_context.return_value = play_context

    mock_unfrackpath.side_effect = lambda path: path
    mock_getcwd.return_value = '/tmp'

    r_fd, w_fd = 10, 11
    mock_pipe.return_value = (r_fd, w_fd)
    mock_fork_process.return_value = 0  # simulate child process

    mock_ssh = MagicMock()
    mock_ssh._create_control_path.return_value = '%(directory)s/.ansible_pc_%(user)s@%(host)s:%(port)s'
    mock_connection_loader.get.return_value = mock_ssh

    vars_data = {'ANSIBLE_NET_USERNAME': 'test'}
    pc_data = play_context.serialize()

    mock_stdin = MagicMock()
    mock_stdin.buffer = MagicMock()
    mock_stdin.buffer.readline.side_effect = [
        to_bytes(str(len(cPickle.dumps(vars_data)))) + b'\n',
        to_bytes(str(len(cPickle.dumps(pc_data)))) + b'\n',
    ]
    mock_stdin.buffer.read.side_effect = [
        cPickle.dumps(vars_data),
        cPickle.dumps(pc_data),
    ]

    with patch('ansible.module_utils.persistent_connection.sys.stdin', mock_stdin), \
         patch('ansible.module_utils.persistent_connection.os.fdopen') as mock_fdopen, \
         patch('ansible.module_utils.persistent_connection.os.close') as mock_close, \
         patch('ansible.module_utils.persistent_connection.ConnectionProcess') as mock_cp:

        mock_wfd = MagicMock()
        mock_fdopen.return_value = mock_wfd
        mock_process = MagicMock()
        mock_cp.return_value = mock_process

        import ansible.module_utils.persistent_connection as pc_module
        pc_module.main()

    # In child process, ConnectionProcess should be created and started
    mock_cp.assert_called_once()
    mock_process.start.assert_called_once_with(vars_data)
    mock_process.run.assert_called_once()
    mock_exit.assert_called_once()


@patch('ansible.module_utils.persistent_connection.sys.exit')
@patch('ansible.module_utils.persistent_connection.sys.stdout', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.sys.stderr', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.os.getcwd')
@patch('ansible.module_utils.persistent_connection.fork_process')
@patch('ansible.module_utils.persistent_connection.os.pipe')
@patch('ansible.module_utils.persistent_connection.makedirs_safe')
@patch('ansible.module_utils.persistent_connection.unfrackpath')
@patch('ansible.module_utils.persistent_connection.connection_loader')
@patch('ansible.module_utils.persistent_connection.PlayContext')
@patch('ansible.module_utils.persistent_connection.file_lock')
@patch('ansible.module_utils.persistent_connection.os.path.exists')
def test_main_existing_socket(mock_exists, mock_file_lock, mock_play_context, mock_connection_loader,
                              mock_unfrackpath, mock_makedirs_safe, mock_pipe, mock_fork_process,
                              mock_getcwd, mock_stderr, mock_stdout, mock_exit):
    """Test module_0.main() when an existing socket is found."""
    mock_exists.return_value = True
    mock_file_lock.return_value.__enter__ = MagicMock()
    mock_file_lock.return_value.__exit__ = MagicMock(return_value=False)

    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.remote_user = 'test'
    play_context.connection = 'ssh'
    play_context.verbosity = 0
    play_context.private_key_file = None
    mock_play_context.return_value = play_context

    mock_unfrackpath.side_effect = lambda path: path
    mock_getcwd.return_value = '/tmp'

    mock_ssh = MagicMock()
    mock_ssh._create_control_path.return_value = '%(directory)s/.ansible_pc_%(user)s@%(host)s:%(port)s'
    mock_connection_loader.get.return_value = mock_ssh

    vars_data = {'ANSIBLE_NET_USERNAME': 'test'}
    pc_data = play_context.serialize()

    mock_stdin = MagicMock()
    mock_stdin.buffer = MagicMock()
    mock_stdin.buffer.readline.side_effect = [
        to_bytes(str(len(cPickle.dumps(vars_data)))) + b'\n',
        to_bytes(str(len(cPickle.dumps(pc_data)))) + b'\n',
    ]
    mock_stdin.buffer.read.side_effect = [
        cPickle.dumps(vars_data),
        cPickle.dumps(pc_data),
    ]

    with patch('ansible.module_utils.persistent_connection.sys.stdin', mock_stdin), \
         patch('ansible.module_utils.persistent_connection.Connection') as mock_conn:

        mock_connection = MagicMock()
        mock_connection.pop_messages.return_value = []
        mock_conn.return_value = mock_connection

        import ansible.module_utils.persistent_connection as pc_module
        pc_module.main()

    # Verify Connection was instantiated with socket_path
    mock_conn.assert_called_once()
    mock_connection.set_options.assert_called_once()
    mock_connection.update_play_context.assert_called_once()
    mock_connection.set_check_prompt.assert_called_once()
    mock_exit.assert_called_once()


@patch('ansible.module_utils.persistent_connection.sys.exit')
@patch('ansible.module_utils.persistent_connection.sys.stdout', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.sys.stderr', new_callable=StringIO)
@patch('ansible.module_utils.persistent_connection.os.getcwd')
@patch('ansible.module_utils.persistent_connection.fork_process')
@patch('ansible.module_utils.persistent_connection.os.pipe')
@patch('ansible.module_utils.persistent_connection.makedirs_safe')
@patch('ansible.module_utils.persistent_connection.unfrackpath')
@patch('ansible.module_utils.persistent_connection.connection_loader')
@patch('ansible.module_utils.persistent_connection.PlayContext')
@patch('ansible.module_utils.persistent_connection.file_lock')
@patch('ansible.module_utils.persistent_connection.os.path.exists')
def test_main_existing_socket_update_play_context_error(mock_exists, mock_file_lock, mock_play_context,
                                                         mock_connection_loader, mock_unfrackpath,
                                                         mock_makedirs_safe, mock_pipe, mock_fork_process,
                                                         mock_getcwd, mock_stderr, mock_stdout, mock_exit):
    """Test module_0.main() with existing socket when update_play_context raises a non-ConnectionError."""
    mock_exists.return_value = True
    mock_file_lock.return_value.__enter__ = MagicMock()
    mock_file_lock.return_value.__exit__ = MagicMock(return_value=False)

    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 22
    play_context.remote_user = 'test'
    play_context.connection = 'ssh'
    play_context.verbosity = 0
    play_context.private_key_file = None
    mock_play_context.return_value = play_context

    mock_unfrackpath.side_effect = lambda path: path
    mock_getcwd.return_value = '/tmp'

    mock_ssh = MagicMock()
    mock_ssh._create_control_path.return_value = '%(directory)s/.ansible_pc_%(user)s@%(host)s:%(port)s'
    mock_connection_loader.get.return_value = mock_ssh

    vars_data = {'ANSIBLE_NET_USERNAME': 'test'}
    pc_data = play_context.serialize()

    mock_stdin = MagicMock()
    mock_stdin.buffer = MagicMock()
    mock_stdin.buffer.readline.side_effect = [
        to_bytes(str(len(cPickle.dumps(vars_data)))) + b'\n',
        to_bytes(str(len(cPickle.dumps(pc_data)))) + b'\n',
    ]
    mock_stdin.buffer.read.side_effect = [
        cPickle.dumps(vars_data),
        cPickle.dumps(pc_data),
    ]

    with patch('ansible.module_utils.persistent_connection.sys.stdin', mock_stdin), \
         patch('ansible.module_utils.persistent_connection.Connection') as mock_conn:

        mock_connection = MagicMock()
        mock_connection.pop_messages.return_value = []
        mock_connection.update_play_context.side_effect = Exception('some error')
        mock_conn.return_value = mock_connection

        import ansible.module_utils.persistent_connection as pc_module
        pc_module.main()

    # Exit should be called with rc=1 due to exception in result
    mock_exit.assert_called_once()
    assert mock_exit.call_args[0][0] == 1

# Generated at 2026-11-02 17:55:29.256444
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    """
    Test that ConnectionProcess.handler logs the signal message via display
    with log_only=True and raises an Exception containing the signal number.
    """
    from unittest.mock import MagicMock, patch
    import pytest

    # Arrange
    fd = MagicMock()
    play_context = PlayContext()
    socket_path = '/tmp/ansible_test_socket_path'
    original_path = '/tmp'
    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path)

    signum = 15
    frame = None
    expected_msg = 'signal handler called with signal %s.' % signum

    # Act / Assert
    with patch.object(sys.modules[__name__], 'display', create=True) as mock_display:
        with pytest.raises(Exception) as exc_info:
            connection_process.handler(signum, frame)

    mock_display.display.assert_called_once_with(expected_msg, log_only=True)
    assert str(exc_info.value) == expected_msg


# Unit test for method handler of class ConnectionProcess with SIGTERM
def test_ConnectionProcess_handler_sigterm():
    """
    Test handler with signal.SIGTERM to ensure the message contains the
    correct signal number and the exception propagates.
    """
    from unittest.mock import MagicMock, patch
    import pytest

    fd = MagicMock()
    play_context = PlayContext()
    socket_path = '/tmp/ansible_test_socket_path_sigterm'
    original_path = '/tmp'
    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path)

    signum = signal.SIGTERM
    expected_msg = 'signal handler called with signal %s.' % signum

    with patch.object(sys.modules[__name__], 'display', create=True) as mock_display:
        with pytest.raises(Exception, match='signal handler called with signal'):
            connection_process.handler(signum, None)

    mock_display.display.assert_called_once_with(expected_msg, log_only=True)


# Generated at 2026-10-24 07:36:58.239193
# Unit test for function file_lock
def test_file_lock():
    import stat
    import tempfile

    def can_lock_in_child(lock_path):
        pid = os.fork()
        if pid == 0:
            fd = os.open(lock_path, os.O_RDWR)
            try:
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os._exit(1)
            os._exit(0)
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status) == 0

    with tempfile.TemporaryDirectory() as tmpdir:
        lock_path = os.path.join(tmpdir, "test.lock")

        assert not os.path.exists(lock_path)

        with module_0.file_lock(lock_path):
            assert os.path.exists(lock_path)
            assert stat.S_IMODE(os.stat(lock_path).st_mode) == 0o600
            assert not can_lock_in_child(lock_path)

        assert can_lock_in_child(lock_path)

# Generated at 2026-10-24 07:37:00.656616
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 07:37:03.070335
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 07:37:05.632554
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 07:37:08.046068
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 07:37:10.462337
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 07:37:12.875318
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 07:37:15.292678
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:37:17.707403
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:37:20.122281
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:37:22.543346
# Unit test for function file_lock

# Generated at 2026-10-24 07:37:24.959259
# Unit test for function file_lock

# Generated at 2026-10-24 07:37:27.373742
# Unit test for function file_lock

# Generated at 2026-10-24 07:37:29.786122
# Unit test for function file_lock

# Generated at 2026-10-24 07:37:46.922331
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-24 07:37:48.250718
# Unit test for function file_lock
def test_file_lock():
    import stat
    import tempfile

    def can_lock_in_child(lock_path):
        pid = os.fork()
        if pid == 0:
            fd = os.open(lock_path, os.O_RDWR)
            try:
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os._exit(1)
            os._exit(0)
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status) == 0

    with tempfile.TemporaryDirectory() as tmpdir:
        lock_path = os.path.join(tmpdir, "test.lock")

        assert not os.path.exists(lock_path)

        with module_0.file_lock(lock_path):
            assert os.path.exists(lock_path)
            assert stat.S_IMODE(os.stat(lock_path).st_mode) == 0o600
            assert not can_lock_in_child(lock_path)

        assert can_lock_in_child(lock_path)

# Generated at 2026-10-24 07:37:49.552027
# Unit test for function file_lock
def test_file_lock():
    import stat
    import tempfile

    def can_lock_in_child(lock_path):
        pid = os.fork()
        if pid == 0:
            fd = os.open(lock_path, os.O_RDWR)
            try:
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os._exit(1)
            os._exit(0)
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status) == 0

    with tempfile.TemporaryDirectory() as tmpdir:
        lock_path = os.path.join(tmpdir, "test.lock")

        assert not os.path.exists(lock_path)

        with module_0.file_lock(lock_path):
            assert os.path.exists(lock_path)
            assert stat.S_IMODE(os.stat(lock_path).st_mode) == 0o600
            assert not can_lock_in_child(lock_path)

        assert can_lock_in_child(lock_path)

# Generated at 2026-10-24 07:38:11.135890
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:38:13.644557
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:38:16.060227
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:38:18.474928
# Unit test for function file_lock

# Generated at 2026-10-24 07:38:20.894520
# Unit test for function file_lock

# Generated at 2026-10-24 07:38:23.309641
# Unit test for function file_lock

# Generated at 2026-10-24 07:38:25.723271
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:38:28.137583
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:38:30.551868
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:38:32.964945
# Unit test for function read_stream

# Generated at 2026-10-24 07:38:35.385087
# Unit test for function read_stream

# Generated at 2026-10-24 07:38:37.797741
# Unit test for function read_stream

# Generated at 2026-10-24 07:38:40.213601
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 07:38:57.743344
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():import importlib

# Generated at 2026-10-24 07:39:14.126199
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 07:39:15.461061
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():import importlib

# Generated at 2026-10-24 07:39:39.501465
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:39:41.915778
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:39:44.333763
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:39:48.372280
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:39:50.785249
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:39:53.199315
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:39:55.613482
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:39:58.031149
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:40:00.445900
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:40:02.859519
# Unit test for function read_stream

# Generated at 2026-10-24 07:40:05.275456
# Unit test for function read_stream

# Generated at 2026-10-24 07:40:29.800956
# Unit test for function read_stream

# Generated at 2026-10-24 07:41:09.841244
# Unit test for function read_stream
def test_read_stream():
    import hashlib
    import io
    import pytest


# Generated at 2026-10-24 07:42:06.878905
# Unit test for function main

# Generated at 2026-10-24 07:43:04.245205
# Unit test for function main
def test_main():import hashlib

# Generated at 2026-10-24 07:43:32.688807
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import tempfile
    from io import StringIO
    from unittest import mock

    socket_path = os.path.join(tempfile.gettempdir(), 'ansible_pc_test_socket')
    original_path = os.getcwd()
    task_uuid = 'test-task-uuid'
    ansible_playbook_pid = 12345

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = 'test_private_key'

    variables = {'ansible_connection': 'local'}

    mock_connection = mock.MagicMock()
    mock_connection.pop_messages.return_value = []

    # use a pipe so we can read what module_0.start() writes even after fd.close()
    wr_fd, rd_fd = os.pipe()
    fd = os.fdopen(wr_fd, 'w')

    with mock.patch.object(connection_loader, 'get', return_value=mock_connection) as mock_loader_get, \
            mock.patch.object(sys, 'stdout', new=StringIO()), \
            mock.patch.object(socket, 'socket') as mock_socket:

        cp = ConnectionProcess(fd, play_context, socket_path, original_path,
                               task_uuid=task_uuid, ansible_playbook_pid=ansible_playbook_pid)
        cp.start(variables)

    # read the JSON result

# Generated at 2026-10-24 07:43:35.107079
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:43:37.673132
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:43:40.090943
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:43:42.511307
# Unit test for function read_stream

# Generated at 2026-10-24 07:43:44.927156
# Unit test for function read_stream

# Generated at 2026-10-24 07:44:00.640846
# Unit test for function read_stream
def test_read_stream():import io

# Generated at 2026-10-24 07:44:12.215960
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import tempfile
    from unittest.mock import MagicMock, patch

    import ansible.modules  # noqa: F401  (ensures ansible is importable)
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play_context import PlayContext

    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        # Create the socket file and lock file so module_0.shutdown() has cleanup work to do
        with open(socket_path, 'wb'):
            pass
        with open(lock_path, 'wb'):
            pass

        assert os.path.exists(socket_path)
        assert os.path.exists(lock_path)

        # Build the ConnectionProcess instance without running start()
        play_context = PlayContext()
        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = play_context
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = MagicMock()
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        with patch.object(connection_loader, 'get', return_value=process.connection):
            process.shutdown()

        # Socket object was closed
        process.sock.close.assert_called_once()

        # Connection was closed
        process.connection.close.assert_called_once()

        # Connection state was reset
        assert getattr(process.connection, '_socket_path', 'missing') is None
        assert getattr(process.connection, '_connected', 'missing') is False

        # Socket file and lock file were removed
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        # No exception captured during shutdown
        assert process.exception is None

    # Second scenario: shutdown when the socket file does not exist
    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn_missing.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = PlayContext()
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = None
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        process.shutdown()

        # Nothing was closed on the connection since socket file was absent
        process.connection.close.assert_not_called()

        # No exception raised even though paths never existed
        assert process.exception is None
        assert not os.path.exists(lock_path)

# Generated at 2026-10-24 07:44:13.535267
# Unit test for function file_lock
def test_file_lock():
    import stat
    import tempfile

    def can_lock_in_child(lock_path):
        pid = os.fork()
        if pid == 0:
            fd = os.open(lock_path, os.O_RDWR)
            try:
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os._exit(1)
            os._exit(0)
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status) == 0

    with tempfile.TemporaryDirectory() as tmpdir:
        lock_path = os.path.join(tmpdir, "test.lock")

        assert not os.path.exists(lock_path)

        with module_0.file_lock(lock_path):
            assert os.path.exists(lock_path)
            assert stat.S_IMODE(os.stat(lock_path).st_mode) == 0o600
            assert not can_lock_in_child(lock_path)

        assert can_lock_in_child(lock_path)

# Generated at 2026-10-24 07:44:27.680173
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:44:30.100441
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:44:32.523636
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:44:34.940674
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:44:37.356949
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:44:39.773446
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:44:42.186565
# Unit test for function read_stream

# Generated at 2026-10-24 07:44:44.600500
# Unit test for function read_stream

# Generated at 2026-10-24 07:44:47.018151
# Unit test for function read_stream

# Generated at 2026-10-24 07:44:49.447165
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 07:45:06.896819
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():import json

# Generated at 2026-10-24 07:45:24.676095
# Unit test for function read_stream
def test_read_stream():
    import hashlib
    import io
    import pytest


# Generated at 2026-10-24 07:45:27.371896
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import tempfile
    from unittest.mock import MagicMock, patch

    import ansible.modules  # noqa: F401  (ensures ansible is importable)
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play_context import PlayContext

    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        # Create the socket file and lock file so module_0.shutdown() has cleanup work to do
        with open(socket_path, 'wb'):
            pass
        with open(lock_path, 'wb'):
            pass

        assert os.path.exists(socket_path)
        assert os.path.exists(lock_path)

        # Build the ConnectionProcess instance without running start()
        play_context = PlayContext()
        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = play_context
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = MagicMock()
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        with patch.object(connection_loader, 'get', return_value=process.connection):
            process.shutdown()

        # Socket object was closed
        process.sock.close.assert_called_once()

        # Connection was closed
        process.connection.close.assert_called_once()

        # Connection state was reset
        assert getattr(process.connection, '_socket_path', 'missing') is None
        assert getattr(process.connection, '_connected', 'missing') is False

        # Socket file and lock file were removed
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        # No exception captured during shutdown
        assert process.exception is None

    # Second scenario: shutdown when the socket file does not exist
    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn_missing.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = PlayContext()
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = None
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        process.shutdown()

        # Nothing was closed on the connection since socket file was absent
        process.connection.close.assert_not_called()

        # No exception raised even though paths never existed
        assert process.exception is None
        assert not os.path.exists(lock_path)

# Generated at 2026-10-24 07:45:54.519776
# Unit test for function read_stream
def test_read_stream():from io import BytesIO


# Generated at 2026-10-24 07:45:57.277148
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import tempfile
    from unittest.mock import MagicMock, patch

    import ansible.modules  # noqa: F401  (ensures ansible is importable)
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play_context import PlayContext

    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        # Create the socket file and lock file so module_0.shutdown() has cleanup work to do
        with open(socket_path, 'wb'):
            pass
        with open(lock_path, 'wb'):
            pass

        assert os.path.exists(socket_path)
        assert os.path.exists(lock_path)

        # Build the ConnectionProcess instance without running start()
        play_context = PlayContext()
        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = play_context
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = MagicMock()
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        with patch.object(connection_loader, 'get', return_value=process.connection):
            process.shutdown()

        # Socket object was closed
        process.sock.close.assert_called_once()

        # Connection was closed
        process.connection.close.assert_called_once()

        # Connection state was reset
        assert getattr(process.connection, '_socket_path', 'missing') is None
        assert getattr(process.connection, '_connected', 'missing') is False

        # Socket file and lock file were removed
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        # No exception captured during shutdown
        assert process.exception is None

    # Second scenario: shutdown when the socket file does not exist
    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn_missing.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = PlayContext()
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = None
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        process.shutdown()

        # Nothing was closed on the connection since socket file was absent
        process.connection.close.assert_not_called()

        # No exception raised even though paths never existed
        assert process.exception is None
        assert not os.path.exists(lock_path)

# Generated at 2026-10-24 07:46:00.144420
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import tempfile
    from io import StringIO
    from unittest import mock

    socket_path = os.path.join(tempfile.gettempdir(), 'ansible_pc_test_socket')
    original_path = os.getcwd()
    task_uuid = 'test-task-uuid'
    ansible_playbook_pid = 12345

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = 'test_private_key'

    variables = {'ansible_connection': 'local'}

    mock_connection = mock.MagicMock()
    mock_connection.pop_messages.return_value = []

    # use a pipe so we can read what module_0.start() writes even after fd.close()
    wr_fd, rd_fd = os.pipe()
    fd = os.fdopen(wr_fd, 'w')

    with mock.patch.object(connection_loader, 'get', return_value=mock_connection) as mock_loader_get, \
            mock.patch.object(sys, 'stdout', new=StringIO()), \
            mock.patch.object(socket, 'socket') as mock_socket:

        cp = ConnectionProcess(fd, play_context, socket_path, original_path,
                               task_uuid=task_uuid, ansible_playbook_pid=ansible_playbook_pid)
        cp.start(variables)

    # read the JSON result

# Generated at 2026-10-24 07:46:02.897921
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import tempfile
    from unittest.mock import MagicMock, patch

    import ansible.modules  # noqa: F401  (ensures ansible is importable)
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play_context import PlayContext

    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        # Create the socket file and lock file so module_0.shutdown() has cleanup work to do
        with open(socket_path, 'wb'):
            pass
        with open(lock_path, 'wb'):
            pass

        assert os.path.exists(socket_path)
        assert os.path.exists(lock_path)

        # Build the ConnectionProcess instance without running start()
        play_context = PlayContext()
        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = play_context
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = MagicMock()
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        with patch.object(connection_loader, 'get', return_value=process.connection):
            process.shutdown()

        # Socket object was closed
        process.sock.close.assert_called_once()

        # Connection was closed
        process.connection.close.assert_called_once()

        # Connection state was reset
        assert getattr(process.connection, '_socket_path', 'missing') is None
        assert getattr(process.connection, '_connected', 'missing') is False

        # Socket file and lock file were removed
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        # No exception captured during shutdown
        assert process.exception is None

    # Second scenario: shutdown when the socket file does not exist
    with tempfile.TemporaryDirectory() as tmpdir:
        socket_path = os.path.join(tmpdir, 'ansible_conn_missing.sock')
        lock_path = os.path.join(
            tmpdir,
            '.ansible_pc_lock_%s' % os.path.basename(socket_path)
        )

        process = ConnectionProcess.__new__(ConnectionProcess)
        process.play_context = PlayContext()
        process.socket_path = socket_path
        process.original_path = tmpdir
        process._task_uuid = None
        process.fd = None
        process.exception = None
        process.srv = MagicMock()
        process.sock = None
        process.connection = MagicMock()
        process.connection.get_option.return_value = False
        process._ansible_playbook_pid = None

        process.shutdown()

        # Nothing was closed on the connection since socket file was absent
        process.connection.close.assert_not_called()

        # No exception raised even though paths never existed
        assert process.exception is None
        assert not os.path.exists(lock_path)

# Generated at 2026-10-24 07:46:07.139721
# Unit test for function main

# Generated at 2026-10-24 07:46:34.998268
# Unit test for function main
def test_main():import hashlib

# Generated at 2026-10-24 07:46:37.381298
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:46:39.796897
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:46:42.212100
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 07:46:44.635988
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:46:47.051085
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 07:46:49.467424
# Unit test for method shutdown of class ConnectionProcess
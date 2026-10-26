

# Generated at 2026-10-25 06:05:14.015246
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:05:15.477079
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:05:46.792032
# Unit test for method command_timeout of class ConnectionProcess
def test_ConnectionProcess_command_timeout():
    from unittest.mock import MagicMock

    timeout_value = 30

    # Build a ConnectionProcess instance without running __init__
    # (only `connection` is needed by command_timeout)
    process = ConnectionProcess.__new__(ConnectionProcess)
    process.connection = MagicMock()
    process.connection.get_option.return_value = timeout_value

    # Capture calls to the module-level display.display
    displayed = []
    original_display = display.display

    def fake_display(msg, log_only=False):
        displayed.append((msg, log_only))

    display.display = fake_display
    try:
        raised = None
        try:
            process.command_timeout(signal.SIGALRM, None)
        except Exception as e:
            raised = e
    finally:
        display.display = original_display

    # An exception must have been raised
    assert raised is not None, "command_timeout did not raise an exception"

    expected_msg = (
        'command timeout triggered, timeout value is %s secs.\n'
        'See the timeout setting options in the Network Debug and Troubleshooting Guide.'
        % timeout_value
    )

    # The exception message must contain the configured timeout value
    assert str(raised) == expected_msg, (
        "Unexpected exception message: %r (expected %r)" % (str(raised), expected_msg)
    )

    # The message must have been logged via display with log_only=True
    assert displayed == [(expected_msg, True)], (
        "display.display was not called correctly: %r" % (displayed,)
    )

    # The timeout value must be read from the persistent_command_timeout option
    process.connection.get_option.assert_called_once_with('persistent_command_timeout')

# Generated at 2026-10-25 06:05:49.555045
# Unit test for function read_stream
def test_read_stream():
    import io
    import hashlib
    def _make(transmitted, digest_override=None):
        digest = digest_override if digest_override is not None else hashlib.sha1(transmitted).hexdigest()
        return io.BytesIO(("%d\n" % len(transmitted)).encode("utf-8") + transmitted + digest.encode("utf-8") + b"\n")
    assert module_0.read_stream(_make(b"hello world")) == b"hello world"
    assert module_0.read_stream(_make(b"")) == b""
    assert module_0.read_stream(_make(b"line1\nline2\n")) == b"line1\nline2\n"

# Generated at 2026-10-25 06:05:51.155310
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:06:41.369628
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:06:57.956657
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:07:00.623699
# Unit test for function read_stream

# Generated at 2026-10-25 06:07:03.039198
# Unit test for function read_stream

# Generated at 2026-10-25 06:07:05.456752
# Unit test for function read_stream

# Generated at 2026-10-25 06:07:13.619949
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:07:16.035301
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:07:18.453115
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:07:20.869303
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:23.434652
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:25.990342
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:28.402922
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:30.821540
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:33.235236
# Unit test for function file_lock

# Generated at 2026-10-25 06:07:35.651690
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:07:38.068341
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:07:39.738401
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:07:57.932486
# Unit test for function main

# Generated at 2026-10-25 06:08:00.730641
# Unit test for function main

# Generated at 2026-10-25 06:08:03.264241
# Unit test for function main

# Generated at 2026-10-25 06:08:05.684695
# Unit test for function main

# Generated at 2026-10-25 06:08:08.099488
# Unit test for function main

# Generated at 2026-10-25 06:08:10.592007
# Unit test for function main

# Generated at 2026-10-25 06:08:13.170819
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:15.589449
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:18.170981
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:20.620646
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:23.137360
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:25.553164
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:08:27.966039
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:08:30.381339
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:08:32.829837
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:08:35.245676
# Unit test for function main

# Generated at 2026-10-25 06:08:37.659979
# Unit test for function main

# Generated at 2026-10-25 06:08:40.495338
# Unit test for function main

# Generated at 2026-10-25 06:08:43.233109
# Unit test for function read_stream
def test_read_stream():
    import io
    import hashlib
    def _make(transmitted, digest_override=None):
        digest = digest_override if digest_override is not None else hashlib.sha1(transmitted).hexdigest()
        return io.BytesIO(("%d\n" % len(transmitted)).encode("utf-8") + transmitted + digest.encode("utf-8") + b"\n")
    assert module_0.read_stream(_make(b"hello world")) == b"hello world"
    assert module_0.read_stream(_make(b"")) == b""
    assert module_0.read_stream(_make(b"line1\nline2\n")) == b"line1\nline2\n"

# Generated at 2026-10-25 06:09:01.053781
# Unit test for function main

# Generated at 2026-10-25 06:09:03.470119
# Unit test for function main

# Generated at 2026-10-25 06:09:06.035524
# Unit test for function main

# Generated at 2026-10-25 06:09:08.451625
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:10.868771
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:13.286870
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:15.706147
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:18.124697
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:20.540422
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:22.958765
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:25.374875
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:27.794561
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:09:30.207813
# Unit test for function read_stream

# Generated at 2026-10-25 06:09:32.619540
# Unit test for function read_stream

# Generated at 2026-10-25 06:09:35.034029
# Unit test for function read_stream

# Generated at 2026-10-25 06:09:37.448347
# Unit test for function file_lock

# Generated at 2026-10-25 06:09:39.864043
# Unit test for function file_lock

# Generated at 2026-10-25 06:09:42.278763
# Unit test for function file_lock

# Generated at 2026-10-25 06:09:44.693917
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:47.110123
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:49.527154
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:09:51.944000
# Unit test for function main

# Generated at 2026-10-25 06:09:54.359511
# Unit test for function main

# Generated at 2026-10-25 06:09:56.857422
# Unit test for function main

# Generated at 2026-10-25 06:09:59.474566
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

# Generated at 2026-10-25 06:10:03.202573
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:10:05.940132
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:10:08.649079
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:10:30.351765
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import shutil
    import tempfile
    from mock import MagicMock, patch

    socket_dir = tempfile.mkdtemp()
    socket_path = os.path.join(socket_dir, 'ansiballz_socket')
    fd = MagicMock()

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = None

    original_path = os.getcwd()
    cp = ConnectionProcess(fd, play_context, socket_path, original_path,
                           ansible_playbook_pid=os.getpid())

    fake_connection = MagicMock()
    fake_connection.pop_messages.return_value = []
    fake_connection.get_option.return_value = False

    variables = {'ansible_connection': 'local'}


# Generated at 2026-10-25 06:10:32.984266
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:35.397266
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:37.808294
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:40.230269
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:42.647294
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:45.065280
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:47.478267
# Unit test for function file_lock

# Generated at 2026-10-25 06:10:49.898411
# Unit test for function file_lock

# Generated at 2026-10-25 06:10:52.314851
# Unit test for function file_lock

# Generated at 2026-10-25 06:10:54.726290
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:57.144291
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:10:59.679282
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:11:02.017562
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:04.433642
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:06.851747
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:09.265113
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:11.681295
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:14.095573
# Unit test for function read_stream

# Generated at 2026-10-25 06:11:16.543383
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:11:18.958297
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:11:21.562388
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:11:24.296399
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import shutil
    import tempfile
    from mock import MagicMock, patch

    socket_dir = tempfile.mkdtemp()
    socket_path = os.path.join(socket_dir, 'ansiballz_socket')
    fd = MagicMock()

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = None

    original_path = os.getcwd()
    cp = ConnectionProcess(fd, play_context, socket_path, original_path,
                           ansible_playbook_pid=os.getpid())

    fake_connection = MagicMock()
    fake_connection.pop_messages.return_value = []
    fake_connection.get_option.return_value = False

    variables = {'ansible_connection': 'local'}


# Generated at 2026-10-25 06:11:46.122653
# Unit test for function file_lock
def test_file_lock():import fcntl
import os

import pytest


def test_file_lock(tmp_path):
    lock_path = str(tmp_path / "test.lock")

    # The lock file should not exist before the context is entered
    assert not os.path.exists(lock_path)

    with module_0.file_lock(lock_path):
        # Entering the context should create the lock file with 0600 perms
        assert os.path.exists(lock_path)
        assert (os.stat(lock_path).st_mode & 0o777) == 0o600

        # While held, a second non-blocking exclusive lock must fail
        fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        with pytest.raises(IOError):
            fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.close(fd)

    # After leaving the context, the lock must be released
    fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    fcntl.lockf(fd, fcntl.LOCK_UN)
    os.close(fd)

    # The context manager must not close or delete the lock file itself
    assert os.path.exists(lock_path)

# Generated at 2026-10-25 06:11:48.652327
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:11:51.065919
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:11:53.708374
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:11:56.124343
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:11:58.539954
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:12:01.171403
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:12:03.583191
# Unit test for function file_lock

# Generated at 2026-10-25 06:12:05.999226
# Unit test for function file_lock

# Generated at 2026-10-25 06:12:30.972703
# Unit test for function file_lock
def test_file_lock():import tempfile

# Generated at 2026-10-25 06:12:33.390231
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:36.048077
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:38.462891
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:40.875127
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:43.290988
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:45.992762
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:12:48.476243
# Unit test for function read_stream

# Generated at 2026-10-25 06:12:50.893562
# Unit test for function read_stream

# Generated at 2026-10-25 06:12:53.305770
# Unit test for function read_stream

# Generated at 2026-10-25 06:12:55.763465
# Unit test for function file_lock

# Generated at 2026-10-25 06:12:58.178387
# Unit test for function file_lock

# Generated at 2026-10-25 06:13:00.592417
# Unit test for function file_lock

# Generated at 2026-10-25 06:13:03.008292
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:05.425946
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:07.839483
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:10.256272
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:12.670049
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:15.085065
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:35.147170
# Unit test for function file_lock
def test_file_lock():import fcntl
import os

import pytest


def test_file_lock(tmp_path):
    lock_path = str(tmp_path / "test.lock")

    # The lock file should not exist before the context is entered
    assert not os.path.exists(lock_path)

    with module_0.file_lock(lock_path):
        # Entering the context should create the lock file with 0600 perms
        assert os.path.exists(lock_path)
        assert (os.stat(lock_path).st_mode & 0o777) == 0o600

        # While held, a second non-blocking exclusive lock must fail
        fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        with pytest.raises(IOError):
            fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.close(fd)

    # After leaving the context, the lock must be released
    fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    fcntl.lockf(fd, fcntl.LOCK_UN)
    os.close(fd)

    # The context manager must not close or delete the lock file itself
    assert os.path.exists(lock_path)

# Generated at 2026-10-25 06:13:37.822533
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:40.359839
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:42.774253
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:13:45.191566
# Unit test for function read_stream

# Generated at 2026-10-25 06:13:47.608147
# Unit test for function read_stream

# Generated at 2026-10-25 06:13:50.204717
# Unit test for function read_stream

# Generated at 2026-10-25 06:13:52.997342
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:13:55.415008
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:13:57.833119
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:14:00.247105
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:02.660622
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:05.075385
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:07.490255
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:14:09.905265
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:14:12.324500
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:14:14.733912
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:17.149139
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:19.564620
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:21.981092
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:24.396407
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:26.811247
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:29.225181
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:31.640283
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:34.056330
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:36.471735
# Unit test for function file_lock

# Generated at 2026-10-25 06:14:54.639238
# Unit test for function file_lock
def test_file_lock():import tempfile
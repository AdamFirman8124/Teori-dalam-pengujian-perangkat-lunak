

# Generated at 2026-10-25 06:57:40.844317
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:57:43.258404
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:57:45.673817
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:57:48.087632
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:57:50.504090
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:57:52.917478
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:57:55.335137
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:57:57.753372
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:58:00.173131
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:58:02.586423
# Unit test for function read_stream

# Generated at 2026-10-25 06:58:05.332293
# Unit test for function read_stream
def test_read_stream():import io

# Generated at 2026-10-25 06:58:33.370271
# Unit test for method handler of class ConnectionProcess
def test_ConnectionProcess_handler():
    process = ConnectionProcess.__new__(ConnectionProcess)
    signum = signal.SIGTERM
    frame = None

    expected_message = "signal handler called with signal %s." % signum

    with mock.patch.object(module.display, "display") as display_mock:
        with pytest.raises(Exception, match=r"signal handler called with signal .*"):
            process.handler(signum, frame)

    display_mock.assert_called_once_with(
        expected_message,
        log_only=True,
    )

# Generated at 2026-10-25 06:58:36.550004
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

# Generated at 2026-10-25 06:58:39.469260
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:41.006576
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:43.873404
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:46.631509
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


# Generated at 2026-10-25 06:58:49.172412
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:51.707479
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:54.123251
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:58:56.700637
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:58:59.120695
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:59:01.529298
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:59:03.943274
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:59:06.995948
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:59:09.695352
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:59:11.177893
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:59:27.629601
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:59:29.134285
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:59:30.566047
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:59:48.690081
# Unit test for function main

# Generated at 2026-10-25 06:59:51.662732
# Unit test for function main

# Generated at 2026-10-25 06:59:54.081316
# Unit test for function main

# Generated at 2026-10-25 06:59:56.494007
# Unit test for function read_stream

# Generated at 2026-10-25 06:59:59.345992
# Unit test for function read_stream

# Generated at 2026-10-25 07:00:01.761191
# Unit test for function read_stream

# Generated at 2026-10-25 07:00:04.545256
# Unit test for function file_lock

# Generated at 2026-10-25 07:00:22.687468
# Unit test for function file_lock
def test_file_lock():import tempfile

# Generated at 2026-10-25 07:00:25.563993
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


# Generated at 2026-10-25 07:00:28.346845
# Unit test for function main

# Generated at 2026-10-25 07:00:31.221291
# Unit test for function main

# Generated at 2026-10-25 07:00:34.128967
# Unit test for function main

# Generated at 2026-10-25 07:00:37.031289
# Unit test for function main

# Generated at 2026-10-25 07:00:39.443266
# Unit test for function main

# Generated at 2026-10-25 07:00:42.233424
# Unit test for function main

# Generated at 2026-10-25 07:00:44.645963
# Unit test for function file_lock

# Generated at 2026-10-25 07:00:47.253403
# Unit test for function file_lock

# Generated at 2026-10-25 07:00:49.858671
# Unit test for function file_lock

# Generated at 2026-10-25 07:00:52.271403
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:00:54.685245
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:00:57.103721
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:00:59.515439
# Unit test for function file_lock

# Generated at 2026-10-25 07:01:01.943962
# Unit test for function file_lock

# Generated at 2026-10-25 07:01:04.350017
# Unit test for function file_lock

# Generated at 2026-10-25 07:01:06.766619
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:01:09.182313
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:01:11.595257
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:01:14.010161
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:16.479995
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:18.895120
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:21.308816
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:23.742267
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:26.140338
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:28.552521
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:01:46.563479
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:02:03.152726
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 07:02:21.270779
# Unit test for function main

# Generated at 2026-10-25 07:02:23.688730
# Unit test for function main

# Generated at 2026-10-25 07:02:26.103523
# Unit test for function main

# Generated at 2026-10-25 07:02:28.519654
# Unit test for function read_stream

# Generated at 2026-10-25 07:02:31.162237
# Unit test for function read_stream
def test_read_stream():import io

# Generated at 2026-10-25 07:02:33.985130
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


# Generated at 2026-10-25 07:02:51.961426
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

# Generated at 2026-10-25 07:02:53.324911
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:11.120035
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:13.536255
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:15.952275
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:18.565937
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:20.985617
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:23.399120
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:25.819665
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:28.230784
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 07:03:30.658061
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:33.075461
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:35.491299
# Unit test for function file_lock

# Generated at 2026-10-25 07:03:37.911404
# Unit test for function main

# Generated at 2026-10-25 07:03:40.325872
# Unit test for function main

# Generated at 2026-10-25 07:03:42.742928
# Unit test for function main

# Generated at 2026-10-25 07:03:47.226088
# Unit test for function read_stream

# Generated at 2026-10-25 07:03:49.639478
# Unit test for function read_stream

# Generated at 2026-10-25 07:03:52.053381
# Unit test for function read_stream

# Generated at 2026-10-25 07:03:54.468099
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:03:56.885510
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:03:59.298391
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:04:01.759982
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:04.172517
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:06.590495
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:09.000108
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:11.416020
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:13.830424
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:16.244869
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:18.678351
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:21.098572
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:23.510266
# Unit test for function main

# Generated at 2026-10-25 07:04:25.924742
# Unit test for function main

# Generated at 2026-10-25 07:04:28.341454
# Unit test for function main

# Generated at 2026-10-25 07:04:30.756535
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:33.177330
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:35.590333
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:38.003150
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:40.417841
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:42.832647
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:45.248730
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:47.661153
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:50.083567
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 07:04:52.489509
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:54.903325
# Unit test for function file_lock

# Generated at 2026-10-25 07:04:57.316980
# Unit test for function file_lock

# Generated at 2026-10-25 07:05:03.936230
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:06.349835
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:08.763535
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:11.178165
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:13.591671
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:16.005146
# Unit test for function read_stream

# Generated at 2026-10-25 07:05:18.419951
# Unit test for function main

# Generated at 2026-10-25 07:05:20.837320
# Unit test for function main

# Generated at 2026-10-25 07:05:23.253605
# Unit test for function main

# Generated at 2026-10-25 07:05:25.664598
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:02.584751
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:05.310858
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:07.641466
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:10.055191
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:12.468480
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 07:06:15.025654
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:17.411698
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:19.825942
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:22.240443
# Unit test for function main

# Generated at 2026-10-25 07:06:24.654448
# Unit test for function main

# Generated at 2026-10-25 07:06:27.269926
# Unit test for function main

# Generated at 2026-10-25 07:06:29.684411
# Unit test for function main

# Generated at 2026-10-25 07:06:32.101987
# Unit test for function main

# Generated at 2026-10-25 07:06:34.514366
# Unit test for function main

# Generated at 2026-10-25 07:06:36.927987
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:39.343923
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:41.760034
# Unit test for function read_stream

# Generated at 2026-10-25 07:06:44.177144
# Unit test for function main

# Generated at 2026-10-25 07:06:46.584802
# Unit test for function main

# Generated at 2026-10-25 07:06:48.997668
# Unit test for function main

# Generated at 2026-10-25 07:07:15.746346
# Unit test for function main

# Generated at 2026-10-25 07:07:18.161296
# Unit test for function main

# Generated at 2026-10-25 07:07:20.574944
# Unit test for function main

# Generated at 2026-10-25 07:07:22.987796
# Unit test for function file_lock

# Generated at 2026-10-25 07:07:25.401511
# Unit test for function file_lock

# Generated at 2026-10-25 07:07:27.816279
# Unit test for function file_lock
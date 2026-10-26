

# Generated at 2026-10-25 06:41:58.524736
# Unit test for function main

# Generated at 2026-10-25 06:42:00.906789
# Unit test for function main

# Generated at 2026-10-25 06:42:03.322257
# Unit test for function main

# Generated at 2026-10-25 06:42:05.735938
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:42:08.151815
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:42:51.239588
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:42:53.807729
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:42:56.215041
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:42:58.632693
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 06:43:01.061599
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:43:03.474232
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:43:05.890843
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-25 06:43:08.340247
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:10.748900
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:13.168270
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:15.582121
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:17.997665
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:20.412166
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:22.854922
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:25.638791
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:28.513509
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:29.948414
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:43:46.358147
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import tempfile


# Generated at 2026-10-25 06:43:48.774880
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:51.190571
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:53.769725
# Unit test for function file_lock

# Generated at 2026-10-25 06:43:56.183616
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:43:58.601918
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:44:01.017496
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:44:03.435434
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:05.854270
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:08.470669
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:10.889956
# Unit test for function file_lock

# Generated at 2026-10-25 06:44:13.349602
# Unit test for function file_lock

# Generated at 2026-10-25 06:44:15.731581
# Unit test for function file_lock

# Generated at 2026-10-25 06:44:18.149006
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:20.638677
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:22.991856
# Unit test for function read_stream

# Generated at 2026-10-25 06:44:25.410647
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:27.959247
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:30.258668
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:32.675504
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:35.182866
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:37.519741
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:44:39.936462
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:44:42.424998
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:44:44.768283
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:44:47.185388
# Unit test for function main

# Generated at 2026-10-25 06:44:50.317870
# Unit test for function main

# Generated at 2026-10-25 06:44:53.235939
# Unit test for function main

# Generated at 2026-10-25 06:44:56.095241
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


# Generated at 2026-10-25 06:44:59.036077
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

# Generated at 2026-10-25 06:45:17.467132
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:45:20.186133
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:45:22.699765
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:45:25.116617
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:45:27.546692
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:45:29.968621
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:45:32.384611
# Unit test for function main

# Generated at 2026-10-25 06:45:34.800843
# Unit test for function main

# Generated at 2026-10-25 06:45:37.214220
# Unit test for function main

# Generated at 2026-10-25 06:45:39.631231
# Unit test for function file_lock

# Generated at 2026-10-25 06:45:42.043588
# Unit test for function file_lock

# Generated at 2026-10-25 06:45:44.461776
# Unit test for function file_lock

# Generated at 2026-10-25 06:45:46.878186
# Unit test for function read_stream

# Generated at 2026-10-25 06:45:49.414281
# Unit test for function read_stream

# Generated at 2026-10-25 06:45:51.768911
# Unit test for function read_stream

# Generated at 2026-10-25 06:45:54.186151
# Unit test for function read_stream

# Generated at 2026-10-25 06:46:10.268958
# Unit test for function read_stream
def test_read_stream():import io

# Generated at 2026-10-25 06:46:25.665942
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:46:28.844956
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:46:46.632639
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:46:49.050995
# Unit test for function file_lock

# Generated at 2026-10-25 06:46:51.781878
# Unit test for function file_lock

# Generated at 2026-10-25 06:46:54.195728
# Unit test for function file_lock

# Generated at 2026-10-25 06:46:56.670979
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:46:59.088662
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:47:27.110766
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import tempfile
    from io import StringIO
    from unittest.mock import MagicMock, patch

    tmpdir = tempfile.mkdtemp()
    socket_path = os.path.join(tmpdir, 'test_socket')

    fd = StringIO()
    fake_stdout = StringIO()

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = None

    mock_connection = MagicMock()
    mock_connection.pop_messages.return_value = []

    with patch('ansible.plugins.connection.connection_loader.get', return_value=mock_connection), \
            patch('ansible.plugins.connection.sys.stdout', fake_stdout):
        process = ConnectionProcess(fd, play_context, socket_path, tmpdir)
        process.start({})

    result = json.loads(fd.getvalue())

    assert 'error' not in result
    assert 'exception' not in result
    assert 'control socket path is %s' % socket_path in result['messages']
    assert 'local domain socket listeners started successfully' in result['messages']
    assert process.connection is mock_connection
    assert mock_connection._socket_path == socket_path
    assert os.path.exists(socket_path)

    process.sock.close()
    os.remove(socket_path)

# Generated at 2026-10-25 06:47:29.522477
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:31.942338
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:34.587080
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:37.008016
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:47:39.417252
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:47:41.840755
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:47:44.549276
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:46.965896
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:49.378419
# Unit test for function read_stream

# Generated at 2026-10-25 06:47:51.794382
# Unit test for function main

# Generated at 2026-10-25 06:47:54.209824
# Unit test for function main

# Generated at 2026-10-25 06:47:56.628600
# Unit test for function main

# Generated at 2026-10-25 06:47:59.046466
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:01.459047
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:03.904212
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:06.295929
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:08.709763
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:11.129295
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:13.544394
# Unit test for function file_lock

# Generated at 2026-10-25 06:48:15.959762
# Unit test for function file_lock

# Generated at 2026-10-25 06:48:18.380793
# Unit test for function file_lock

# Generated at 2026-10-25 06:48:23.021781
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:25.440641
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:27.856393
# Unit test for function read_stream

# Generated at 2026-10-25 06:48:30.286202
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:48:32.696159
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:48:35.113776
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:48:37.526000
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:48:39.943727
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:48:42.362736
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:48:44.863299
# Unit test for function main

# Generated at 2026-10-25 06:48:47.274878
# Unit test for function main

# Generated at 2026-10-25 06:48:49.689394
# Unit test for function main

# Generated at 2026-10-25 06:48:52.103333
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:54.517314
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:56.933627
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:48:59.346898
# Unit test for function read_stream

# Generated at 2026-10-25 06:49:01.764390
# Unit test for function read_stream

# Generated at 2026-10-25 06:49:04.181404
# Unit test for function read_stream

# Generated at 2026-10-25 06:49:06.594528
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:49:09.011012
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:49:11.427943
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:49:13.841778
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:49:16.259569
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:49:18.676641
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:49:21.090480
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:23.507844
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:25.924919
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:28.341179
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:49:30.756959
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:49:33.175294
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:49:40.115508
# Unit test for function main

# Generated at 2026-10-25 06:49:42.498526
# Unit test for function main

# Generated at 2026-10-25 06:49:44.915356
# Unit test for function main

# Generated at 2026-10-25 06:49:47.332589
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:49.746814
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:52.163853
# Unit test for function file_lock

# Generated at 2026-10-25 06:49:54.580767
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:49:56.996130
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:49:59.412333
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:01.829891
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:50:04.246281
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:50:06.682859
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 06:50:09.097567
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:11.523974
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:13.934104
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:16.350842
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:50:18.862689
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:50:21.197016
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:50:23.614587
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:26.025432
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:28.440156
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:50:30.854583
# Unit test for function main

# Generated at 2026-10-25 06:50:33.268708
# Unit test for function main

# Generated at 2026-10-25 06:50:35.791290
# Unit test for function main

# Generated at 2026-10-25 06:50:38.205176
# Unit test for function file_lock

# Generated at 2026-10-25 06:50:40.622661
# Unit test for function file_lock

# Generated at 2026-10-25 06:50:43.105497
# Unit test for function file_lock

# Generated at 2026-10-25 06:50:45.473711
# Unit test for function file_lock

# Generated at 2026-10-25 06:50:47.891468
# Unit test for function file_lock

# Generated at 2026-10-25 06:50:50.345635
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:06.085264
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:08.501845
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:10.916363
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:13.366871
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:15.751811
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:18.167454
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:20.604500
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:23.021440
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:25.436141
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:27.926230
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:30.342639
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:32.757296
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:35.171540
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:51:37.587483
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:51:40.002795
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 06:51:42.419807
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:44.837155
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:47.251480
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:49.669591
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:52.081027
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:54.495217
# Unit test for function file_lock

# Generated at 2026-10-25 06:51:56.909225
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:51:59.326872
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 06:52:00.825254
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    import tempfile
    from io import StringIO
    from unittest.mock import MagicMock, patch

    tmpdir = tempfile.mkdtemp()
    socket_path = os.path.join(tmpdir, 'test_socket')

    fd = StringIO()
    fake_stdout = StringIO()

    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.private_key_file = None

    mock_connection = MagicMock()
    mock_connection.pop_messages.return_value = []

    with patch('ansible.plugins.connection.connection_loader.get', return_value=mock_connection), \
            patch('ansible.plugins.connection.sys.stdout', fake_stdout):
        process = ConnectionProcess(fd, play_context, socket_path, tmpdir)
        process.start({})

    result = json.loads(fd.getvalue())

    assert 'error' not in result
    assert 'exception' not in result
    assert 'control socket path is %s' % socket_path in result['messages']
    assert 'local domain socket listeners started successfully' in result['messages']
    assert process.connection is mock_connection
    assert mock_connection._socket_path == socket_path
    assert os.path.exists(socket_path)

    process.sock.close()
    os.remove(socket_path)
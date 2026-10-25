

# Generated at 2026-10-25 05:27:53.301610
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:27:55.718409
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:27:58.139194
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:28:00.557741
# Unit test for function main

# Generated at 2026-10-25 05:28:02.976191
# Unit test for function main

# Generated at 2026-10-25 05:28:05.395541
# Unit test for function main

# Generated at 2026-10-25 05:28:08.005352
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 05:28:10.423393
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 05:28:12.840900
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-25 05:28:15.259458
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 05:28:17.678370
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 05:28:20.097893
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-25 05:28:22.517075
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:24.936695
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:27.355072
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:32.359342
# Unit test for function file_lock

# Generated at 2026-10-25 05:28:34.774965
# Unit test for function file_lock

# Generated at 2026-10-25 05:28:37.195925
# Unit test for function file_lock

# Generated at 2026-10-25 05:28:39.611913
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:42.029020
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:44.451053
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:28:46.871316
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:28:49.291427
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:28:51.709861
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:28:54.126905
# Unit test for function file_lock

# Generated at 2026-10-25 05:28:56.546055
# Unit test for function file_lock

# Generated at 2026-10-25 05:28:58.965851
# Unit test for function file_lock

# Generated at 2026-10-25 05:29:01.384068
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:03.802601
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:06.219829
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:08.638291
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:29:11.058477
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:29:13.477742
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:29:15.895795
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:18.313431
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:20.731803
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-25 05:29:23.151444
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:29:25.570094
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:29:43.716703
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-25 05:30:01.655083
# Unit test for function main

# Generated at 2026-10-25 05:30:44.825972
# Unit test for function main
def test_main():import io

# Generated at 2026-10-25 05:31:02.348935
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-25 05:31:19.201440
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import os

# Generated at 2026-10-25 05:31:38.089278
# Unit test for function main

# Generated at 2026-10-25 05:32:05.309908
# Unit test for function main
def test_main():import io

# Generated at 2026-10-25 05:32:28.138491
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import shutil
    import tempfile

    try:
        from unittest.mock import MagicMock, call
    except ImportError:
        from mock import MagicMock, call

    temp_dir = tempfile.mkdtemp()
    socket_path = os.path.join(temp_dir, 'pc.sock')
    lock_path = os.path.join(temp_dir, '.ansible_pc_lock_pc.sock')

    # module_0.shutdown() only checks for the paths, so regular files are sufficient.
    open(socket_path, 'wb').close()
    open(lock_path, 'wb').close()

    process = ConnectionProcess(
        fd=None,
        play_context=MagicMock(),
        socket_path=socket_path,
        original_path=temp_dir,
    )
    process.sock = MagicMock()
    process.connection = MagicMock()
    process.connection.get_option.return_value = True
    process.connection.pop_messages.return_value = [
        ('debug', 'persistent connection message'),
    ]

    display_mock = MagicMock()
    module = sys.modules[ConnectionProcess.__module__]
    missing = object()
    original_display = getattr(module, 'display', missing)
    module.display = display_mock

    try:
        process.shutdown()

        process.sock.close.assert_called_once_with()
        process.connection.close.assert_called_once_with()
        process.connection.get_option.assert_called_once_with(
            'persistent_log_messages'
        )
        process.connection.pop_messages.assert_called_once_with()

        assert process.connection._socket_path is None
        assert process.connection._connected is False
        assert not os.path.exists(socket_path)
        assert not os.path.exists(lock_path)

        assert display_mock.display.call_args_list == [
            call('persistent connection message', log_only=True),
            call('shutdown complete', log_only=True),
        ]
    finally:
        if original_display is missing:
            delattr(module, 'display')
        else:
            module.display = original_display
        shutil.rmtree(temp_dir, ignore_errors=True)

# Generated at 2026-10-25 05:32:51.190404
# Unit test for function file_lock
def test_file_lock():import shutil
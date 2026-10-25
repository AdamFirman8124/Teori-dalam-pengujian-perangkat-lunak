

# Generated at 2026-10-24 23:15:56.239941
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:16:21.522401
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:16:23.936290
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:16:26.355429
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:28.934586
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:31.350654
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:33.768180
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:36.187286
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:38.603613
# Unit test for function read_stream

# Generated at 2026-10-24 23:16:41.022135
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 23:16:43.438604
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 23:16:52.458890
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():import io


# Generated at 2026-10-24 23:17:18.674236
# Unit test for function main

# Generated at 2026-10-24 23:17:21.093249
# Unit test for function main

# Generated at 2026-10-24 23:17:23.636665
# Unit test for function main

# Generated at 2026-10-24 23:17:26.990944
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:29.409572
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:32.003949
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:34.419641
# Unit test for function read_stream

# Generated at 2026-10-24 23:17:36.839239
# Unit test for function read_stream

# Generated at 2026-10-24 23:17:39.258655
# Unit test for function read_stream

# Generated at 2026-10-24 23:17:41.676269
# Unit test for function file_lock

# Generated at 2026-10-24 23:17:44.095807
# Unit test for function file_lock

# Generated at 2026-10-24 23:17:46.511019
# Unit test for function file_lock

# Generated at 2026-10-24 23:17:48.928700
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:51.359817
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:53.768790
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:56.185948
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:17:58.600873
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:18:01.019927
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:18:03.438017
# Unit test for function file_lock

# Generated at 2026-10-24 23:18:33.526879
# Unit test for function file_lock
def test_file_lock():import tempfile

# Generated at 2026-10-24 23:18:35.946097
# Unit test for function main

# Generated at 2026-10-24 23:18:38.364937
# Unit test for function main

# Generated at 2026-10-24 23:18:40.901744
# Unit test for function main

# Generated at 2026-10-24 23:18:43.319408
# Unit test for function main

# Generated at 2026-10-24 23:18:45.738157
# Unit test for function main

# Generated at 2026-10-24 23:18:48.161388
# Unit test for function main

# Generated at 2026-10-24 23:18:50.578578
# Unit test for function main

# Generated at 2026-10-24 23:18:52.996525
# Unit test for function main

# Generated at 2026-10-24 23:18:55.415517
# Unit test for function main

# Generated at 2026-10-24 23:18:57.833770
# Unit test for function file_lock

# Generated at 2026-10-24 23:19:00.250267
# Unit test for function file_lock

# Generated at 2026-10-24 23:19:02.669360
# Unit test for function file_lock

# Generated at 2026-10-24 23:19:05.084634
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:19:07.501034
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:19:09.935899
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:19:12.350263
# Unit test for function read_stream

# Generated at 2026-10-24 23:19:14.768653
# Unit test for function read_stream

# Generated at 2026-10-24 23:19:17.189552
# Unit test for function read_stream

# Generated at 2026-10-24 23:19:19.605581
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:19:22.025119
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:19:24.444631
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:19:26.864112
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:19:29.285858
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:19:55.975410
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from unittest.mock import MagicMock, patch


# Generated at 2026-10-24 23:20:06.572191
# Unit test for function read_stream
def test_read_stream():
    from io import BytesIO

    encoded_data = b'hello\\rworld'
    checksum = hashlib.sha1(encoded_data).hexdigest().encode('ascii')
    stream = BytesIO(
        str(len(encoded_data)).encode('ascii')
        + b'\n'
        + encoded_data
        + checksum
        + b'\n'
    )

    assert module_0.read_stream(stream) == b'hello\rworld'

# Generated at 2026-10-24 23:20:09.258815
# Unit test for function file_lock

# Generated at 2026-10-24 23:20:11.908145
# Unit test for function file_lock

# Generated at 2026-10-24 23:20:14.328598
# Unit test for function file_lock

# Generated at 2026-10-24 23:20:16.886208
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:20:19.302207
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:20:21.719148
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:20:24.292829
# Unit test for function read_stream

# Generated at 2026-10-24 23:20:26.711370
# Unit test for function read_stream

# Generated at 2026-10-24 23:20:29.251415
# Unit test for function read_stream

# Generated at 2026-10-24 23:20:31.670203
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:20:34.089476
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:20:36.505364
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:21:18.597497
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 23:21:30.783586
# Unit test for function file_lock
def test_file_lock():
    from unittest.mock import call, patch

    lock_path = "/tmp/test-file.lock"
    lock_fd = 42

    with patch.object(os, "open", return_value=lock_fd) as mock_open, \
            patch.object(os, "close") as mock_close, \
            patch.object(fcntl, "lockf") as mock_lockf:

        # Normal exit
        with module_0.file_lock(lock_path):
            mock_lockf.assert_called_once_with(lock_fd, fcntl.LOCK_EX)

        mock_open.assert_called_once_with(
            lock_path, os.O_RDWR | os.O_CREAT, 0o600
        )
        assert mock_lockf.call_args_list == [
            call(lock_fd, fcntl.LOCK_EX),
            call(lock_fd, fcntl.LOCK_UN),
        ]
        mock_close.assert_called_once_with(lock_fd)

        # Exceptional exit must also unlock and close.
        mock_open.reset_mock()
        mock_lockf.reset_mock()
        mock_close.reset_mock()

        try:
            with module_0.file_lock(lock_path):
                raise RuntimeError("test error")
        except RuntimeError:
            pass

        assert mock_lockf.call_args_list == [
            call(lock_fd, fcntl.LOCK_EX),
            call(lock_fd, fcntl.LOCK_UN),
        ]
        mock_close.assert_called_once_with(lock_fd)

# Generated at 2026-10-24 23:21:33.206910
# Unit test for function file_lock

# Generated at 2026-10-24 23:21:35.622482
# Unit test for function file_lock

# Generated at 2026-10-24 23:21:38.041918
# Unit test for function file_lock

# Generated at 2026-10-24 23:21:40.458523
# Unit test for function file_lock

# Generated at 2026-10-24 23:21:42.875977
# Unit test for function file_lock

# Generated at 2026-10-24 23:21:45.676243
# Unit test for function file_lock
def test_file_lock():import tempfile

# Generated at 2026-10-24 23:22:10.506153
# Unit test for function main
def test_main():import json
from contextlib import nullcontext
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

import persistent_connection as module_under_test


def test_main_reuses_existing_socket(monkeypatch, capsys):
    socket_path = "/tmp/ansible-pc/control.sock"
    vars_data = b"serialized variables"
    init_data = b"serialized play context"

    variables = {"ansible_connection": "network_cli"}
    serialized_play_context = {"remote_addr": "router.example.com"}

    class FakePlayContext:
        def __init__(self):
            self.verbosity = 3
            self.remote_addr = "router.example.com"
            self.port = 22
            self.remote_user = "admin"
            self.connection = "network_cli"
            self.deserialized_data = None

        def deserialize(self, data):
            self.deserialized_data = data

    play_context = FakePlayContext()

    class FakeSSH:
        @staticmethod
        def _create_control_path(
            remote_addr,
            port,
            remote_user,
            connection,
            ansible_playbook_pid,
        ):
            assert remote_addr == "router.example.com"
            assert port == 22
            assert remote_user == "admin"
            assert connection == "network_cli"
            assert ansible_playbook_pid == "1234"
            return "%(directory)s/control.sock"

    connections = []

    class FakeConnection:
        def __init__(self, path):
            assert path == socket_path
            self.path = path
            self.options = None
            self.updated_play_context = None
            self.task_uuid = None
            connections.append(self)

        def set_options(self, var_options):
            self.options = var_options

        def update_play_context(self, data):
            self.updated_play_context = data

        def set_check_prompt(self, task_uuid):
            self.task_uuid = task_uuid

        def pop_messages(self):
            return [("debug", "queued connection message")]

    pickle_loads = Mock(
        side_effect=[serialized_play_context, variables]
    )
    makedirs_safe = Mock()

    monkeypatch.setattr(module_under_test, "PY3", False)
    monkeypatch.setattr(
        module_under_test.sys,
        "argv",
        ["persistent_connection", "1234", "task-uuid"],
    )
    monkeypatch.setattr(
        module_under_test,
        "read_stream",
        Mock(side_effect=[vars_data, init_data]),
    )
    monkeypatch.setattr(module_under_test.cPickle, "loads", pickle_loads)
    monkeypatch.setattr(
        module_under_test,
        "PlayContext",
        Mock(return_value=play_context),
    )
    monkeypatch.setattr(
        module_under_test.connection_loader,
        "get",
        Mock(return_value=FakeSSH),
    )
    monkeypatch.setattr(
        module_under_test,
        "C",
        SimpleNamespace(PERSISTENT_CONTROL_PATH_DIR="/tmp/ansible-pc"),
    )
    monkeypatch.setattr(module_under_test, "unfrackpath", lambda path: path)
    monkeypatch.setattr(module_under_test, "makedirs_safe", makedirs_safe)
    monkeypatch.setattr(
        module_under_test,
        "file_lock",
        lambda _path: nullcontext(),
    )
    monkeypatch.setattr(
        module_under_test.os.path,
        "exists",
        lambda path: path == socket_path,
    )
    monkeypatch.setattr(module_under_test, "Connection", FakeConnection)
    monkeypatch.setattr(
        module_under_test,
        "display",
        SimpleNamespace(verbosity=0),
    )

    with pytest.raises(SystemExit) as exc_info:
        module_under_test.main()

    assert exc_info.value.code == 0

    output = json.loads(capsys.readouterr().out)
    assert output["socket_path"] == socket_path
    assert "exception" not in output
    assert ["vvvv", "found existing local domain socket, using it!"] in output[
        "messages"
    ]

    # The first connection updates the existing persistent process.
    assert connections[0].options == variables
    assert connections[0].task_uuid == "task-uuid"
    assert connections[0].updated_play_context is not None

    # The second connection is created to retrieve queued messages.
    assert len(connections) == 2

    play_context.deserialize.assert_not_called() if isinstance(
        play_context.deserialize, Mock
    ) else None
    assert play_context.deserialized_data == serialized_play_context
    makedirs_safe.assert_called_once_with("/tmp/ansible-pc")

# Generated at 2026-10-24 23:22:35.927803
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    from unittest.mock import MagicMock, call, patch

    # Resolve the module containing ConnectionProcess so imported functions
    # such as recv_data/send_data are patched where they are used.
    module = sys.modules[ConnectionProcess.__module__]

    process = ConnectionProcess(
        fd=MagicMock(),
        play_context=MagicMock(),
        socket_path='/tmp/ansible-test-socket',
        original_path='/tmp',
    )

    process.connection = MagicMock()
    process.connection._conn_closed = False
    process.connection.connected = False

    options = {
        'persistent_log_messages': False,
        'persistent_connect_timeout': 30,
        'persistent_command_timeout': 60,
    }
    process.connection.get_option.side_effect = options.__getitem__

    client_socket = MagicMock()
    process.sock = MagicMock()
    process.sock.accept.return_value = (client_socket, None)

    # Closing the accepted socket ends the outer connection loop.
    def close_client_socket():
        process.connection._conn_closed = True

    client_socket.close.side_effect = close_client_socket

    process.srv = MagicMock()
    response = '{"jsonrpc": "2.0", "result": "ok", "id": 1}'
    process.srv.handle_request.return_value = response
    process.shutdown = MagicMock()

    request = (
        b'{"jsonrpc": "2.0", "method": "exec_command", '
        b'"params": [], "id": 1}'
    )

    with patch.object(
        module, 'recv_data', side_effect=[request, b'']
    ) as recv_data_mock, patch.object(
        module, 'send_data'
    ) as send_data_mock, patch.object(
        module.signal, 'signal'
    ) as signal_mock, patch.object(
        module.signal, 'alarm'
    ) as alarm_mock, patch.object(
        module.time, 'sleep'
    ) as sleep_mock:
        process.run()

    process.sock.accept.assert_called_once_with()
    recv_data_mock.assert_has_calls([
        call(client_socket),
        call(client_socket),
    ])

    # exec_command must establish the underlying connection when disconnected.
    process.connection._connect.assert_called_once_with()

    process.srv.handle_request.assert_called_once_with(request)

# Generated at 2026-10-24 23:22:38.469553
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:22:41.034717
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:22:43.561535
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:22:54.668592
# Unit test for function read_stream
def test_read_stream():
    from io import BytesIO

    # The checksum is calculated from the transmitted data before escaped
    # carriage returns are restored.
    transmitted_data = b'hello\\rworld'
    expected_data = b'hello\rworld'
    checksum = hashlib.sha1(transmitted_data).hexdigest().encode('ascii')

    stream = BytesIO(
        str(len(transmitted_data)).encode('ascii')
        + b'\n'
        + transmitted_data
        + checksum
        + b'\n'
    )

    assert module_0.read_stream(stream) == expected_data

# Generated at 2026-10-24 23:23:17.588258
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:23:29.587438
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import os

# Generated at 2026-10-24 23:23:32.116707
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:34.537421
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:36.952650
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:39.541247
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:42.070756
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:44.489084
# Unit test for function read_stream

# Generated at 2026-10-24 23:23:50.150954
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:23:52.569003
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:23:54.989263
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:24:23.008508
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 23:24:44.318974
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():import sys

# Generated at 2026-10-24 23:24:47.185451
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:25:04.009917
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():import io

# Generated at 2026-10-24 23:25:06.856112
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 23:25:28.251897
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():from io import StringIO

# Generated at 2026-10-24 23:25:29.644472
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 23:25:39.717857
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import os
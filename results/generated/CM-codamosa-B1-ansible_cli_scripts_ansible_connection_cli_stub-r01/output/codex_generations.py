

# Generated at 2026-10-24 12:34:23.206490
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import os

# Generated at 2026-10-24 12:34:25.624725
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:34:38.276817
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():
    import os
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp()
    socket_path = os.path.join(tmpdir, 'sock')
    lock_path = os.path.join(tmpdir, '.ansible_pc_lock_sock')

    # Create the socket file and lock file so module_0.shutdown() takes the cleanup path
    with open(socket_path, 'w') as f:
        f.write('')
    with open(lock_path, 'w') as f:
        f.write('')

    class FakeConnection:
        def __init__(self):
            self.closed = False
            self.close_called = False

        def close(self):
            self.close_called = True

        def get_option(self, name):
            return False

        def pop_messages(self):
            return []

    fake_conn = FakeConnection()

    cp = ConnectionProcess(None, None, socket_path, None)
    cp.connection = fake_conn
    cp.sock = None  # module_0.shutdown() skips sock.close() when falsy

    cp.shutdown()

    # socket file was removed
    assert not os.path.exists(socket_path)
    # lock file was removed
    assert not os.path.exists(lock_path)
    # connection.close() was called
    assert fake_conn.close_called is True
    # connection state was reset
    assert getattr(fake_conn, '_socket_path') is None
    assert getattr(fake_conn, '_connected') is False

    shutil.rmtree(tmpdir, ignore_errors=True)

# Generated at 2026-10-24 12:34:39.631529
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.connected = True
    conn.get_option.side_effect = lambda name: (
        False if name == 'persistent_log_messages' else 30
    )

    srv = mock.MagicMock()
    srv.handle_request.return_value = '{"jsonrpc": "2.0", "result": "ok"}'

    sock = mock.MagicMock()
    client_sock = mock.MagicMock()

    request = json.dumps({'jsonrpc': '2.0', 'method': 'exec_command', 'params': []}).encode('utf-8')
    resp = to_bytes = ('{"jsonrpc": "2.0", "result": "ok"}').encode('utf-8')

    # End the outer loop after the first accept() returns.
    def accept_side_effect():
        conn._conn_closed = True
        return (client_sock, None)

    sock.accept.side_effect = accept_side_effect

    with mock.patch.object(persistent, 'recv_data', side_effect=[request, b'']), \
         mock.patch.object(persistent, 'send_data') as mock_send, \
         mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    # Assertions
    srv.handle_request.assert_called_once_with(request)
    mock_send.assert_called_once_with(client_sock, resp)
    client_sock.close.assert_called_once()
    proc.shutdown.assert_called_once()
    assert proc.exception is None
    # connected was True, so _connect must NOT have been called
    conn._connect.assert_not_called()


def test_ConnectionProcess_run_connects_on_exec_command():
    """exec_command on a disconnected connection must trigger _connect()."""
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.connected = False
    conn.get_option.side_effect = lambda name: (
        False if name == 'persistent_log_messages' else 30
    )

    srv = mock.MagicMock()
    srv.handle_request.return_value = '{}'

    sock = mock.MagicMock()
    client_sock = mock.MagicMock()

    request = json.dumps({'jsonrpc': '2.0', 'method': 'exec_command', 'params': []}).encode('utf-8')

    def accept_side_effect():
        conn._conn_closed = True
        return (client_sock, None)

    sock.accept.side_effect = accept_side_effect

    with mock.patch.object(persistent, 'recv_data', side_effect=[request, b'']), \
         mock.patch.object(persistent, 'send_data'), \
         mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    conn._connect.assert_called_once()
    assert proc.exception is None


def test_ConnectionProcess_run_records_exception():
    """A non-EINTR error from accept() must be captured in proc.exception."""
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.get_option.return_value = 30

    srv = mock.MagicMock()
    sock = mock.MagicMock()
    err = OSError(13, 'Permission denied')  # errno 13, not EINTR
    sock.accept.side_effect = err

    with mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    assert proc.exception is not None
    assert 'Permission denied' in proc.exception
    proc.shutdown.assert_called_once()

# Generated at 2026-10-24 12:34:48.656248
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 12:34:51.073292
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 12:34:53.492321
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 12:34:55.904645
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 12:34:58.414643
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 12:35:00.826446
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 12:35:03.238415
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:35:05.651776
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:35:08.065940
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:35:10.480441
# Unit test for function main

# Generated at 2026-10-24 12:35:12.892806
# Unit test for function main

# Generated at 2026-10-24 12:35:15.313026
# Unit test for function main

# Generated at 2026-10-24 12:35:17.724610
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:20.142163
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:22.554644
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:24.979693
# Unit test for function file_lock

# Generated at 2026-10-24 12:35:27.401977
# Unit test for function file_lock

# Generated at 2026-10-24 12:35:29.814358
# Unit test for function file_lock

# Generated at 2026-10-24 12:35:32.225747
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:34.639733
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:37.053163
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:35:39.465829
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:41.878802
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:44.293432
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:46.716377
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:49.130013
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:51.545131
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:35:53.962773
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:35:56.377059
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:35:58.789269
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:36:01.203046
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:03.617092
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:06.029783
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:08.442840
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:36:10.855877
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:36:13.269022
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:36:16.830988
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:19.244253
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:21.658151
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:24.071577
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:26.488099
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:28.905033
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:36:31.319196
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:33.732064
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:36.144976
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:38.558077
# Unit test for function file_lock

# Generated at 2026-10-24 12:36:40.971704
# Unit test for function file_lock

# Generated at 2026-10-24 12:36:43.382864
# Unit test for function file_lock

# Generated at 2026-10-24 12:36:45.796108
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:48.210544
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:50.623370
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:36:53.036537
# Unit test for function file_lock

# Generated at 2026-10-24 12:36:55.449630
# Unit test for function file_lock

# Generated at 2026-10-24 12:36:57.864012
# Unit test for function file_lock

# Generated at 2026-10-24 12:37:00.279980
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:02.696379
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:05.110181
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:07.522896
# Unit test for function file_lock

# Generated at 2026-10-24 12:37:09.935810
# Unit test for function file_lock

# Generated at 2026-10-24 12:37:12.349881
# Unit test for function file_lock

# Generated at 2026-10-24 12:37:14.762712
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:17.175738
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:19.588263
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:22.000574
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:24.413969
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:26.826930
# Unit test for function read_stream

# Generated at 2026-10-24 12:37:32.042576
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:34.455558
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:36.867396
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:37:39.285718
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:37:41.697576
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:37:44.109023
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:37:46.523562
# Unit test for function main

# Generated at 2026-10-24 12:37:48.936392
# Unit test for function main

# Generated at 2026-10-24 12:37:51.348347
# Unit test for function main

# Generated at 2026-10-24 12:37:53.760970
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:37:56.173490
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:37:58.587623
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:01.001510
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:03.412913
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:05.826686
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:08.241185
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:10.654340
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:13.069544
# Unit test for function read_stream

# Generated at 2026-10-24 12:38:15.486722
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:17.901098
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:20.313231
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:22.725432
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:25.141375
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:27.553004
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:29.965882
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:38:32.378399
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:38:34.791253
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:38:37.204945
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:39.622401
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:42.031294
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:50.653026
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:53.064255
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:55.476877
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:38:57.888053
# Unit test for function file_lock

# Generated at 2026-10-24 12:39:00.300765
# Unit test for function file_lock

# Generated at 2026-10-24 12:39:02.713302
# Unit test for function file_lock

# Generated at 2026-10-24 12:39:05.123901
# Unit test for function read_stream

# Generated at 2026-10-24 12:39:07.535023
# Unit test for function read_stream

# Generated at 2026-10-24 12:39:09.946358
# Unit test for function read_stream

# Generated at 2026-10-24 12:39:12.358867
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:39:14.771186
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:39:17.183982
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 12:39:19.595765
# Unit test for function main

# Generated at 2026-10-24 12:39:22.011465
# Unit test for function main

# Generated at 2026-10-24 12:39:24.423904
# Unit test for function main

# Generated at 2026-10-24 12:39:26.837852
# Unit test for function main

# Generated at 2026-10-24 12:39:29.248404
# Unit test for function main

# Generated at 2026-10-24 12:39:31.660640
# Unit test for function main

# Generated at 2026-10-24 12:39:34.072240
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:39:36.483992
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:39:38.896294
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 12:40:14.926813
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import shutil

# Generated at 2026-10-24 12:40:17.342855
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:40:19.849175
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:40:22.261599
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 12:40:24.675367
# Unit test for function main

# Generated at 2026-10-24 12:40:27.089432
# Unit test for function main

# Generated at 2026-10-24 12:40:29.502576
# Unit test for function main

# Generated at 2026-10-24 12:41:31.027610
# Unit test for function main
def test_main():import io

# Generated at 2026-10-24 12:41:33.632005
# Unit test for function main

# Generated at 2026-10-24 12:41:36.053381
# Unit test for function main

# Generated at 2026-10-24 12:41:38.562984
# Unit test for function main

# Generated at 2026-10-24 12:41:41.332598
# Unit test for function main

# Generated at 2026-10-24 12:41:43.756060
# Unit test for function main

# Generated at 2026-10-24 12:41:46.174722
# Unit test for function main

# Generated at 2026-10-24 12:42:25.058869
# Unit test for function read_stream
def test_read_stream():
    import io

    # valid payload round-trips
    payload = b'hello world'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == payload

    # escaped literal \r sequences are restored to real carriage returns
    payload = b'a\\rb'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == b'a\rb'

    # checksum mismatch raises
    payload = b'data'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        b'0' * 40 + b'\n'
    )
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'did not match checksum' in str(e)
    else:
        raise AssertionError('expected checksum mismatch error')

    # truncated payload raises EOF error
    stream = io.BytesIO(b'10\nshort\n')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'EOF found before data was complete' in str(e)
    else:
        raise AssertionError('expected EOF error')

# Generated at 2026-10-24 12:43:08.322596
# Unit test for method start of class ConnectionProcess
def test_ConnectionProcess_start():
    try:
        from unittest.mock import MagicMock, patch
    except ImportError:
        from mock import MagicMock, patch

    play_context = MagicMock()
    play_context.connection = 'network_cli'
    play_context.private_key_file = 'keys/id_rsa'

    fd = MagicMock()
    connection = MagicMock()
    connection.pop_messages.return_value = []
    control_socket = MagicMock()
    stdout = StringIO()
    stdout.write('connection initialized\n')

    process = ConnectionProcess(
        fd=fd,
        play_context=play_context,
        socket_path='/tmp/ansible-control.sock',
        original_path='/original',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    process.srv = MagicMock()

    variables = {'ansible_user': 'admin'}

    with patch.object(connection_loader, 'get', return_value=connection) as get_connection:
        with patch.object(socket, 'socket', return_value=control_socket) as socket_factory:
            with patch.object(sys, 'stdout', stdout):
                process.start(variables)

    get_connection.assert_called_once_with(
        'network_cli',
        play_context,
        '/dev/null',
        task_uuid='task-uuid',
        ansible_playbook_pid=1234,
    )
    connection.set_options.assert_called_once_with(var_options=variables)
    assert play_context.private_key_file == '/original/keys/id_rsa'
    assert connection._socket_path == '/tmp/ansible-control.sock'
    process.srv.register.assert_called_once_with(connection)

    socket_factory.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    control_socket.bind.assert_called_once_with('/tmp/ansible-control.sock')
    control_socket.listen.assert_called_once_with(1)
    assert process.sock is control_socket

    fd.write.assert_called_once()
    result = json.loads(fd.write.call_args[0][0])
    assert 'error' not in result
    assert result['messages'] == [
        ['vvvv', 'control socket path is /tmp/ansible-control.sock'],
        ['vvvv', 'connection initialized'],
        ['vvvv', 'local domain socket listeners started successfully'],
    ]
    fd.close.assert_called_once_with()

# Generated at 2026-10-24 12:43:09.688074
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.connected = True
    conn.get_option.side_effect = lambda name: (
        False if name == 'persistent_log_messages' else 30
    )

    srv = mock.MagicMock()
    srv.handle_request.return_value = '{"jsonrpc": "2.0", "result": "ok"}'

    sock = mock.MagicMock()
    client_sock = mock.MagicMock()

    request = json.dumps({'jsonrpc': '2.0', 'method': 'exec_command', 'params': []}).encode('utf-8')
    resp = to_bytes = ('{"jsonrpc": "2.0", "result": "ok"}').encode('utf-8')

    # End the outer loop after the first accept() returns.
    def accept_side_effect():
        conn._conn_closed = True
        return (client_sock, None)

    sock.accept.side_effect = accept_side_effect

    with mock.patch.object(persistent, 'recv_data', side_effect=[request, b'']), \
         mock.patch.object(persistent, 'send_data') as mock_send, \
         mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    # Assertions
    srv.handle_request.assert_called_once_with(request)
    mock_send.assert_called_once_with(client_sock, resp)
    client_sock.close.assert_called_once()
    proc.shutdown.assert_called_once()
    assert proc.exception is None
    # connected was True, so _connect must NOT have been called
    conn._connect.assert_not_called()


def test_ConnectionProcess_run_connects_on_exec_command():
    """exec_command on a disconnected connection must trigger _connect()."""
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.connected = False
    conn.get_option.side_effect = lambda name: (
        False if name == 'persistent_log_messages' else 30
    )

    srv = mock.MagicMock()
    srv.handle_request.return_value = '{}'

    sock = mock.MagicMock()
    client_sock = mock.MagicMock()

    request = json.dumps({'jsonrpc': '2.0', 'method': 'exec_command', 'params': []}).encode('utf-8')

    def accept_side_effect():
        conn._conn_closed = True
        return (client_sock, None)

    sock.accept.side_effect = accept_side_effect

    with mock.patch.object(persistent, 'recv_data', side_effect=[request, b'']), \
         mock.patch.object(persistent, 'send_data'), \
         mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    conn._connect.assert_called_once()
    assert proc.exception is None


def test_ConnectionProcess_run_records_exception():
    """A non-EINTR error from accept() must be captured in proc.exception."""
    conn = mock.MagicMock()
    conn._conn_closed = False
    conn.get_option.return_value = 30

    srv = mock.MagicMock()
    sock = mock.MagicMock()
    err = OSError(13, 'Permission denied')  # errno 13, not EINTR
    sock.accept.side_effect = err

    with mock.patch.object(persistent, 'signal'), \
         mock.patch.object(persistent.display, 'display'), \
         mock.patch.object(persistent.time, 'sleep'):

        proc = _make_process(conn, sock, srv)
        proc.run()

    assert proc.exception is not None
    assert 'Permission denied' in proc.exception
    proc.shutdown.assert_called_once()

# Generated at 2026-10-24 12:43:35.426120
# Unit test for function read_stream
def test_read_stream():from ansible.module_utils.six import BytesIO, PY3
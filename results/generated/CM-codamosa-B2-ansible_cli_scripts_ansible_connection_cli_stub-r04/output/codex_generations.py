

# Generated at 2026-11-02 22:13:19.311062
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():
    from unittest.mock import MagicMock, patch
    import pytest

    fd = MagicMock()
    play_context = MagicMock()
    socket_path = '/tmp/ansible_connection_socket'
    original_path = '/tmp'

    connection_process = ConnectionProcess(fd, play_context, socket_path, original_path)

    connection_process.connection = MagicMock()
    connection_process.connection.get_option.return_value = 30

    expected_msg = ('persistent connection idle timeout triggered, timeout value is 30 secs.\n'
                    'See the timeout setting options in the Network Debug and Troubleshooting Guide.')

    module = sys.modules[__name__]
    with patch.object(module, 'display', create=True) as mock_display:
        with pytest.raises(Exception) as exc_info:
            connection_process.connect_timeout(signal.SIGALRM, None)

    assert str(exc_info.value) == expected_msg
    mock_display.display.assert_called_once_with(expected_msg, log_only=True)

# Generated at 2026-11-02 22:18:09.459448
# Unit test for method command_timeout of class ConnectionProcess
# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import pytest
from unittest import mock

from youtube_dl.socks import sockssocket, InvalidVersionError


@pytest.fixture
def fake_socks_socket():
    """A sockssocket whose real socket machinery is stubbed out."""
    with mock.patch('socket.socket.__init__', return_value=None), \
         mock.patch('socket.socket.close') as mock_close:
        sock = sockssocket()
        yield sock, mock_close


def test_check_response_version_mismatch_raises(fake_socks_socket):
    sock, mock_close = fake_socks_socket

    with pytest.raises(InvalidVersionError) as exc_info:
        sock._check_response_version(0x04, 0x00)

    # close() must have been called exactly once before raising
    mock_close.assert_called_once_with()

    # Verify the error message contents
    msg = str(exc_info.value)
    assert 'Invalid response version from server' in msg
    assert 'Expected 04' in msg
    assert 'got 00' in msg


def test_check_response_version_match_does_nothing(fake_socks_socket):
    sock, mock_close = fake_socks_socket

    # Matching version: no exception, no close
    result = sock._check_response_version(0x05, 0x05)

    assert result is None
    mock_close.assert_not_called()

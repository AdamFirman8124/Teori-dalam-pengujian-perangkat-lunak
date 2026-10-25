# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_message_and_args():
    err = InvalidVersionError(5, 4)

    expected_msg = (
        'Invalid response version from server. Expected 05 got 04'
    )
    assert isinstance(err, InvalidVersionError)
    assert isinstance(err, ProxyError)
    assert isinstance(err, socket.error)
    assert err.args == (0, expected_msg)
    assert err.errno == 0
    assert err.strerror == expected_msg
    assert expected_msg in str(err)


@pytest.mark.parametrize(
    'expected_version,got_version,expected_hex,got_hex',
    [
        (0, 0, '00', '00'),
        (5, 4, '05', '04'),
        (4, 5, '04', '05'),
        (0xAB, 0xCD, 'ab', 'cd'),
        (0xFF, 0x10, 'ff', '10'),
        (0x100, 0x0A, '100', '0a'),
    ],
)
def test_invalid_version_error_hex_formatting(
    expected_version, got_version, expected_hex, got_hex
):
    err = InvalidVersionError(expected_version, got_version)

    expected_msg = (
        'Invalid response version from server. Expected {0} got {1}'.format(
            expected_hex, got_hex
        )
    )
    assert err.args == (0, expected_msg)
    assert err.errno == 0
    assert err.strerror == expected_msg


def test_invalid_version_error_can_be_raised_and_caught():
    with pytest.raises(InvalidVersionError) as exc_info:
        raise InvalidVersionError(5, 0)

    err = exc_info.value
    expected_msg = (
        'Invalid response version from server. Expected 05 got 00'
    )
    assert isinstance(err, ProxyError)
    assert err.args == (0, expected_msg)
    assert err.errno == 0
    assert err.strerror == expected_msg

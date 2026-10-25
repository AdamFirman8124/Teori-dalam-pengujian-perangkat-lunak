# file: project/youtube_dl/socks.py:134-136
# asked: {"lines": [136], "branches": []}
# gained: {"lines": [136], "branches": []}

import pytest

from youtube_dl.socks import sockssocket


@pytest.mark.parametrize(
    'data, expected',
    [
        (b'', b'\x00'),
        (b'A', b'\x01A'),
        (b'hello', b'\x05hello'),
        (b'\x00\x01\x02', b'\x03\x00\x01\x02'),
        (b'x' * 255, b'\xff' + b'x' * 255),
    ],
)
def test_len_and_data(data, expected):
    result = sockssocket._len_and_data(data)
    assert result == expected
    # First byte is the big-endian unsigned length prefix
    assert result[0] == len(data)
    assert result[1:] == data
    assert isinstance(result, bytes)

# file: project/youtube_dl/socks.py:134-136
# asked: {"lines": [136], "branches": []}
# gained: {"lines": [136], "branches": []}

import pytest

from youtube_dl.socks import sockssocket


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", b"\x00"),
        (b"abc", b"\x03abc"),
        (b"\x00\xff", b"\x02\x00\xff"),
    ],
)
def test_len_and_data_prefixes_payload_with_length(data, expected):
    assert sockssocket._len_and_data(data) == expected

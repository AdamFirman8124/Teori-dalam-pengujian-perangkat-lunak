# file: project/youtube_dl/socks.py:134-136
# asked: {"lines": [136], "branches": []}
# gained: {"lines": [136], "branches": []}

from youtube_dl.socks import sockssocket


def test_len_and_data_prefixes_payload_with_its_length():
    payload = b"abc"

    result = sockssocket._len_and_data(payload)

    assert result == b"\x03abc"
    assert result[0] == len(payload)
    assert result[1:] == payload

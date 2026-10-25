# file: project/youtube_dl/socks.py:134-136
# asked: {"lines": [136], "branches": []}
# gained: {"lines": [136], "branches": []}

from youtube_dl.socks import sockssocket


def test_len_and_data_prefixes_payload_with_one_byte_length():
    data = b"test payload"

    result = sockssocket._len_and_data(data)

    assert result == bytes((len(data),)) + data
    assert result[0] == len(data)
    assert result[1:] == data

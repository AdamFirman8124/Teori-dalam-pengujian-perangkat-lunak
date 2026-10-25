# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper.utils import truncate


def test_truncate_returns_original_when_max_length_is_none():
    string = "abcdefghij"

    result = truncate(string, None)

    assert result == string
    assert result is string


def test_truncate_returns_original_when_string_fits():
    string = "abcdefghij"

    result = truncate(string, len(string))

    assert result == string
    assert result is string


def test_truncate_long_string_with_even_max_length():
    result = truncate("abcdefghij", 8)

    assert result == "ab...hij"
    assert len(result) == 8


def test_truncate_long_string_with_odd_max_length():
    result = truncate("abcdefghij", 9)

    assert result == "abc...hij"
    assert len(result) == 9

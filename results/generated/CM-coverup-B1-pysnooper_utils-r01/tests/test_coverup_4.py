# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper.utils import truncate


def test_truncate_with_no_max_length_returns_original_string():
    string = "abcdefghij"

    assert truncate(string, None) == string


def test_truncate_returns_string_within_max_length():
    string = "abc"

    assert truncate(string, 3) == string


def test_truncate_shortens_string_exceeding_max_length():
    assert truncate("abcdefghijkl", 9) == "abc...jkl"

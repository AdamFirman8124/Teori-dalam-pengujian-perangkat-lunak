# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper.utils import truncate


def test_truncate_none_max_length_returns_original():
    s = "0123456789ABCDEF"
    result = truncate(s, None)
    assert result == s
    assert result is s
    assert truncate("", None) == ""


def test_truncate_shorter_than_max_returns_original():
    assert truncate("hi", 10) == "hi"
    assert truncate("", 5) == ""
    assert truncate("abc", 100) == "abc"


def test_truncate_equal_length_returns_original():
    s = "hello"
    result = truncate(s, 5)
    assert result == s
    assert result is s
    assert truncate(s, len(s)) == s


def test_truncate_long_string_even_budget():
    s = "0123456789ABCDEF"  # len 16
    max_length = 10
    # left = (10 - 3) // 2 = 3, right = 10 - 3 - 3 = 4
    expected = "012...CDEF"
    result = truncate(s, max_length)
    assert result == expected
    assert result == "{}...{}".format(s[:3], s[-4:])
    assert len(result) == max_length
    assert "..." in result


def test_truncate_long_string_odd_budget():
    s = "abcdefghijklmnopqrstuvwxyz"
    max_length = 7
    # left = (7 - 3) // 2 = 2, right = 7 - 3 - 2 = 2
    expected = "ab...yz"
    result = truncate(s, max_length)
    assert result == expected
    assert result == "{}...{}".format(s[:2], s[-2:])
    assert len(result) == max_length


def test_truncate_long_string_uneven_split():
    s = "0123456789ABCDEF"
    max_length = 8
    # left = (8 - 3) // 2 = 2, right = 8 - 3 - 2 = 3
    expected = "01...DEF"
    result = truncate(s, max_length)
    assert result == expected
    assert len(result) == max_length

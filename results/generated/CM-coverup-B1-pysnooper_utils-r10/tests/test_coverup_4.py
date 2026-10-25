# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper.utils import truncate


def test_truncate_max_length_none_returns_string_unchanged():
    s = "hello world"
    result = truncate(s, None)
    assert result == s
    assert result == "hello world"


def test_truncate_short_string_returns_string_unchanged():
    s = "hi"
    result = truncate(s, 10)
    assert result == s
    assert result == "hi"


def test_truncate_exact_length_returns_string_unchanged():
    s = "hello"
    result = truncate(s, 5)
    assert result == s
    assert len(result) == 5


def test_truncate_long_string_even_max_length():
    s = "abcdefghijklmnopqrstuvwxyz"
    result = truncate(s, 10)
    # left = (10 - 3) // 2 = 3, right = 10 - 3 - 3 = 4
    assert result == "abc...wxyz"
    assert result == u'{}...{}'.format(s[:3], s[-4:])
    assert len(result) == 10


def test_truncate_long_string_odd_max_length():
    s = "abcdefghijklmnopqrstuvwxyz"
    result = truncate(s, 11)
    # left = (11 - 3) // 2 = 4, right = 11 - 3 - 4 = 4
    assert result == "abcd...wxyz"
    assert len(result) == 11


def test_truncate_long_string_asymmetric_split():
    s = "abcdefghijklmnopqrstuvwxyz"
    result = truncate(s, 12)
    # left = (12 - 3) // 2 = 4, right = 12 - 3 - 4 = 5
    assert result == "abcd...vwxyz"
    assert result == u'{}...{}'.format(s[:4], s[-5:])
    assert len(result) == 12

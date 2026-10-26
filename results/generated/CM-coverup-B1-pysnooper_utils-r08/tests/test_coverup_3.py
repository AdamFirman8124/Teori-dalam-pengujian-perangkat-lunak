# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

from pysnooper.utils import truncate


def test_truncate_max_length_none_returns_string():
    assert truncate('hello world', None) == 'hello world'


def test_truncate_shorter_than_max_length_returns_string():
    assert truncate('hello', 10) == 'hello'


def test_truncate_equal_to_max_length_returns_string():
    assert truncate('hello', 5) == 'hello'


def test_truncate_longer_than_max_length_even_split():
    # left = (8 - 3) // 2 = 2, right = 8 - 3 - 2 = 3
    result = truncate('hello world', 8)
    assert result == 'he...rld'
    assert len(result) == 8


def test_truncate_longer_than_max_length_odd_split():
    # left = (7 - 3) // 2 = 2, right = 7 - 3 - 2 = 2
    result = truncate('hello world', 7)
    assert result == 'he...ld'
    assert len(result) == 7


def test_truncate_with_max_length_three():
    # left = 0, right = 0, and string[-0:] == string[0:] == full string
    result = truncate('hello', 3)
    assert result == '...hello'
    assert result == '{}...{}'.format('hello'[:0], 'hello'[-0:])


def test_truncate_with_max_length_four():
    # left = 0, right = 1
    result = truncate('hello', 4)
    assert result == '...o'
    assert len(result) == 4

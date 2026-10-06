# file: script_12.py:4-20
# asked: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 0], [18, 19], [19, 18], [19, 20]]}
# gained: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 19], [19, 18], [19, 20]]}

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


def test_longest_empty_list():
    """Test that empty list returns None - covers lines 14-15"""
    from script_12 import longest
    result = longest([])
    assert result is None


def test_longest_single_string():
    """Test with a single string - covers lines 17-20"""
    from script_12 import longest
    result = longest(['hello'])
    assert result == 'hello'


def test_longest_multiple_strings_different_lengths():
    """Test with multiple strings of different lengths - covers lines 17-20"""
    from script_12 import longest
    result = longest(['a', 'bb', 'ccc'])
    assert result == 'ccc'


def test_longest_multiple_strings_same_length():
    """Test that first string is returned when multiple have same length - covers lines 17-20"""
    from script_12 import longest
    result = longest(['aa', 'bb', 'cc'])
    assert result == 'aa'


def test_longest_with_empty_string():
    """Test with empty string among other strings - covers lines 17-20"""
    from script_12 import longest
    result = longest(['', 'a', 'bb'])
    assert result == 'bb'


def test_longest_all_empty_strings():
    """Test with all empty strings - covers lines 17-20"""
    from script_12 import longest
    result = longest(['', '', ''])
    assert result == ''

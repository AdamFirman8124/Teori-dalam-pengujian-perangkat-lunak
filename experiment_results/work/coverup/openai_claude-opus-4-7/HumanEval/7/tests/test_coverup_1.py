# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [x for x in strings if substring in x]


def test_filter_by_substring_returns_matching_strings():
    strings = ['abc', 'bacd', 'cde', 'array']
    result = filter_by_substring(strings, 'a')
    assert result == ['abc', 'bacd', 'array']
    assert all('a' in x for x in result)
    assert 'cde' not in result


def test_filter_by_substring_empty_list():
    result = filter_by_substring([], 'a')
    assert result == []
    assert isinstance(result, list)


def test_filter_by_substring_no_matches():
    strings = ['xyz', 'uvw']
    result = filter_by_substring(strings, 'a')
    assert result == []
    assert all('a' not in x for x in strings)


def test_filter_by_substring_all_match():
    strings = ['apple', 'banana', 'avocado']
    result = filter_by_substring(strings, 'a')
    assert result == ['apple', 'banana', 'avocado']
    assert len(result) == len(strings)


def test_filter_by_substring_empty_substring_matches_everything():
    strings = ['', 'a', 'bb']
    result = filter_by_substring(strings, '')
    assert result == ['', 'a', 'bb']
    assert result is not strings


def test_filter_by_substring_does_not_mutate_input():
    strings = ['abc', 'cde', 'array']
    original = list(strings)
    result = filter_by_substring(strings, 'a')
    assert strings == original
    assert result is not strings


def test_filter_by_substring_line_11_executes():
    # Directly exercise the return statement on line 11 with a non-empty match.
    strings = ['hello', 'world', 'yellow']
    substring = 'ell'
    result = filter_by_substring(strings, substring)
    assert result == ['hello', 'yellow']
    assert all(substring in x for x in result)
    assert 'world' not in result


def test_filter_by_substring_called_via_module_attribute():
    # Ensure the function body (line 11) is executed through the module namespace.
    import script_7
    result = script_7.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    assert result == ['abc', 'bacd', 'array']

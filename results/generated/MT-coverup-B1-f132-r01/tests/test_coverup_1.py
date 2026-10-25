# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

from f132 import is_nested


def test_is_nested_with_two_nested_pairs():
    assert is_nested("[[]]") is True


def test_is_nested_with_one_pair():
    assert is_nested("[]") is False


def test_is_nested_with_no_closing_brackets():
    assert is_nested("[[") is False


def test_is_nested_with_closing_bracket_before_opening_bracket():
    assert is_nested("][") is False


def test_is_nested_with_empty_string():
    assert is_nested("") is False

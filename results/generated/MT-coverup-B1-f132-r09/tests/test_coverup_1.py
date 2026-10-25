# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

from f132 import is_nested


def test_is_nested_returns_true_for_nested_brackets():
    assert is_nested("[[]]") is True


def test_is_nested_returns_false_without_closing_brackets():
    assert is_nested("[[") is False


def test_is_nested_returns_false_when_closing_bracket_precedes_opening():
    assert is_nested("][") is False


def test_is_nested_returns_false_for_empty_string():
    assert is_nested("") is False

# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

from f132 import is_nested


def test_nested_brackets_returns_true():
    assert is_nested("[[]]") is True


def test_single_pair_returns_false():
    assert is_nested("[]") is False


def test_closing_bracket_before_opening_returns_false():
    assert is_nested("][") is False


def test_opening_brackets_without_closing_brackets_returns_false():
    assert is_nested("[[") is False

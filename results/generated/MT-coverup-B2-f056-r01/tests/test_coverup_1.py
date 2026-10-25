# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f056 import correct_bracketing


def test_empty_string_balanced():
    assert correct_bracketing("") is True


def test_simple_balanced_pair():
    assert correct_bracketing("<>") is True


def test_nested_balanced():
    assert correct_bracketing("<<>>") is True


def test_early_closing_returns_false():
    assert correct_bracketing(">") is False


def test_closing_before_opening_returns_false():
    assert correct_bracketing("><") is False


def test_unclosed_opening_returns_false():
    assert correct_bracketing("<") is False


def test_extra_closing_after_balanced_returns_false():
    assert correct_bracketing("<>>") is False

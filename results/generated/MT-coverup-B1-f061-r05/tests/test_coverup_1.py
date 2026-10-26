# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f061 import correct_bracketing


def test_empty_string_is_balanced():
    assert correct_bracketing("") is True


def test_single_balanced_pair():
    assert correct_bracketing("()") is True


def test_nested_balanced():
    assert correct_bracketing("(())") is True
    assert correct_bracketing("(()())") is True


def test_early_closing_returns_false():
    assert correct_bracketing(")") is False
    assert correct_bracketing(")()") is False
    assert correct_bracketing("())") is False


def test_unbalanced_open_returns_false():
    assert correct_bracketing("(") is False
    assert correct_bracketing("((") is False
    assert correct_bracketing("(()") is False
    assert correct_bracketing("()(") is False

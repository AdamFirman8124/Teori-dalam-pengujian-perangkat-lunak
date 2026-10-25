# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f061 import correct_bracketing


def test_empty_string_is_balanced():
    assert correct_bracketing("") is True
    assert correct_bracketing("") == (0 == 0)


def test_simple_balanced_pair():
    assert correct_bracketing("()") is True


def test_nested_balanced():
    assert correct_bracketing("(())") is True
    assert correct_bracketing("()()") is True
    assert correct_bracketing("(()())") is True


def test_early_closing_returns_false():
    # covers else branch (depth -= 1) and depth < 0 -> return False
    assert correct_bracketing(")") is False
    assert correct_bracketing(")(") is False
    assert correct_bracketing("())(()") is False


def test_unclosed_opening_returns_false():
    # covers if b == "(" branch and final return depth == 0 -> False
    assert correct_bracketing("(") is False
    assert correct_bracketing("(()") is False
    assert correct_bracketing("((())") is False


def test_mixed_unbalanced():
    assert correct_bracketing("((()))()") is True
    assert correct_bracketing("((()))(()") is False
    assert correct_bracketing("(()))(") is False

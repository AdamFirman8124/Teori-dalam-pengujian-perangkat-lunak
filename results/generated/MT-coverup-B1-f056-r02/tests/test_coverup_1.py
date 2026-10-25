# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f056 import correct_bracketing


def test_correct_bracketing_accepts_balanced_brackets():
    assert correct_bracketing("<>") is True


def test_correct_bracketing_rejects_unbalanced_opening_brackets():
    assert correct_bracketing("<<") is False


def test_correct_bracketing_rejects_closing_bracket_at_zero_depth():
    assert correct_bracketing(">") is False

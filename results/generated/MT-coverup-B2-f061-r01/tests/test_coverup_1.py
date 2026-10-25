# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f061 import correct_bracketing


def test_all_open_increments_depth():
    # Lines 3-6: depth starts at 0, '(' increments it
    assert correct_bracketing("(((") is False  # depth > 0 at end -> line 11 False


def test_close_decrements_and_negative_returns_false():
    # Lines 8-10: ')' decrements; depth < 0 returns False early
    assert correct_bracketing(")(") is False


def test_balanced_returns_true():
    # Lines 3-11 all execute; final depth == 0 -> True
    assert correct_bracketing("(()())") is True


def test_empty_string_returns_true():
    # Line 3 and 11 only: loop body never runs, depth stays 0
    assert correct_bracketing("") is True


def test_unbalanced_open_returns_false():
    # Loop completes but depth != 0 -> line 11 returns False
    assert correct_bracketing("(()") is False

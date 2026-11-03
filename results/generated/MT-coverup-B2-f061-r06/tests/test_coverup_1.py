# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f061 import correct_bracketing


def test_correct_bracketing_balanced():
    # Covers: depth init, loop, '(' branch (depth += 1), ')' branch (depth -= 1),
    # and final return with depth == 0 (True)
    assert correct_bracketing("()") is True
    assert correct_bracketing("(())") is True
    assert correct_bracketing("()()") is True
    assert correct_bracketing("(()())") is True


def test_correct_bracketing_empty_string():
    # Covers: depth init, loop skipped, final return True
    assert correct_bracketing("") is True


def test_correct_bracketing_early_false_on_negative_depth():
    # Covers: ')' branch making depth negative and early return False (line 10)
    assert correct_bracketing(")(") is False
    assert correct_bracketing("())") is False
    assert correct_bracketing("(()") is False


def test_correct_bracketing_final_false_on_positive_depth():
    # Covers: final return with depth > 0 (line 11 evaluating to False)
    assert correct_bracketing("((") is False
    assert correct_bracketing("(()") is False
    assert correct_bracketing("()(") is False

# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

from f061 import correct_bracketing


def test_empty_string_is_correct():
    assert correct_bracketing("") is True


def test_balanced_pairs_are_correct():
    assert correct_bracketing("()") is True
    assert correct_bracketing("(())") is True
    assert correct_bracketing("()()") is True


def test_unclosed_open_bracket_is_incorrect():
    assert correct_bracketing("(") is False
    assert correct_bracketing("(()") is False


def test_early_negative_depth_returns_false():
    assert correct_bracketing(")") is False
    assert correct_bracketing(")(") is False
    assert correct_bracketing("())(") is False


def test_negative_depth_short_circuits_before_end():
    # ")" at index 0 drives depth to -1 and must return immediately,
    # even though the remaining characters would balance out.
    assert correct_bracketing(")(") is False
    assert correct_bracketing(")()(") is False

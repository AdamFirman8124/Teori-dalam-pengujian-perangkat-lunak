# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


def test_empty_string_skips_loop():
    """Covers the false branch of the while condition (line 6) and the return."""
    assert fix_spaces("") == ""


def test_no_spaces_covers_plain_append():
    """Covers the else branch at line 9 and the end - start == 0 case (line 15)."""
    assert fix_spaces("abc") == "abc"


def test_single_space_becomes_underscore():
    """Covers the space branch (lines 7-8) and end - start > 0 (lines 12-13)."""
    assert fix_spaces("a b") == "a_b"


def test_two_spaces_become_two_underscores():
    """Covers end - start == 2 inside the loop (line 13 with repetition)."""
    assert fix_spaces("a  b") == "a__b"


def test_three_spaces_become_dash():
    """Covers end - start > 2 inside the loop (lines 10-11)."""
    assert fix_spaces("a   b") == "a-b"


def test_many_spaces_become_single_dash():
    """Covers end - start > 4 inside the loop (still lines 10-11)."""
    assert fix_spaces("a     b") == "a-b"


def test_trailing_three_spaces_become_dash():
    """Covers the post-loop end - start > 2 branch (lines 18-19)."""
    assert fix_spaces("a   ") == "a-"


def test_trailing_two_spaces_become_underscore():
    """Covers the post-loop end - start > 0 branch (lines 20-21)."""
    assert fix_spaces("a  ") == "a_"


def test_trailing_single_space_becomes_underscore():
    """Covers the post-loop end - start == 1 case (line 21)."""
    assert fix_spaces("a ") == "a_"


def test_leading_spaces_become_underscores():
    """Covers spaces at the very start (start == 0 baseline)."""
    assert fix_spaces("  a") == "__a"


def test_mixed_patterns():
    """Exercises every branch in a single input."""
    assert fix_spaces("a b   c  d") == "a_b-c__d"


def test_no_trailing_spaces_post_loop_both_false():
    """Covers the false branches of both post-loop conditions (lines 18, 20)."""
    assert fix_spaces("a b") == "a_b"

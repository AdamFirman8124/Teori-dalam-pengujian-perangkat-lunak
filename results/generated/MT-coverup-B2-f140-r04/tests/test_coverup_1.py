# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

"""Tests for f140.fix_spaces covering all lines and branches (lines 3-22).

fix_spaces is a pure function (no I/O, no globals, no side effects),
so no monkeypatching or cleanup is required; each test is fully isolated.
"""

from f140 import fix_spaces


def test_empty_string():
    """Covers: while-loop false branch (line 6), line 18 false, line 20 false."""
    assert fix_spaces("") == ""


def test_no_spaces():
    """Covers: line 7 false, line 10 false, line 12 false, line 15, line 18/20 false."""
    assert fix_spaces("abc") == "abc"


def test_single_inner_space_becomes_underscore():
    """Covers: line 7 true, line 10 false, line 12 true (end-start == 1), line 13."""
    assert fix_spaces("a b") == "a_b"


def test_two_inner_spaces_become_two_underscores():
    """Covers: line 12 true with end-start == 2 (underscore repetition)."""
    assert fix_spaces("a  b") == "a__b"


def test_three_inner_spaces_become_dash():
    """Covers: line 10 true (end-start > 2), line 11."""
    assert fix_spaces("a   b") == "a-b"


def test_leading_space_becomes_underscore():
    """Covers: space at index 0 handled via line 12/13 (start == end == 0)."""
    assert fix_spaces(" a") == "_a"


def test_trailing_single_space_becomes_underscore():
    """Covers: line 18 false, line 20 true (end-start == 1), line 21."""
    assert fix_spaces("a ") == "a_"


def test_trailing_two_spaces_become_underscore():
    """Covers: line 18 false, line 20 true (end-start == 2), line 21."""
    assert fix_spaces("a  ") == "a_"


def test_trailing_three_spaces_become_dash():
    """Covers: line 18 true (end-start > 2), line 19."""
    assert fix_spaces("a   ") == "a-"


def test_mixed_runs_and_trailing_space():
    """Covers dash run, underscore run, and trailing-space branch in one input."""
    assert fix_spaces("a   b c ") == "a-b_c_"


def test_long_space_run_replaced_by_single_dash():
    """Covers line 11 with end-start well above 2 (only one dash, not repeated)."""
    assert fix_spaces("a     b") == "a-b"


def test_only_spaces():
    """Covers: every iteration takes the space branch, then line 18/19."""
    assert fix_spaces("   ") == "-"

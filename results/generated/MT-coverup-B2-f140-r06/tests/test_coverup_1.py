# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

"""Tests for f140.fix_spaces covering all missing lines (3-22) and branches.

fix_spaces is a pure function (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required; each test leaves no
state behind.
"""

from f140 import fix_spaces


def test_empty_string_skips_loop_and_final_branches():
    # Executes lines 3-5, skips the while body, and takes neither final
    # branch (end - start == 0), returning the empty string.
    assert fix_spaces("") == ""


def test_no_spaces_takes_inner_else_branch():
    # Covers line 15 (end - start == 0 for every char) and the final
    # no-op path (line 22 reached with no append).
    assert fix_spaces("abc") == "abc"


def test_single_space_becomes_underscore():
    # Covers line 13 with end - start == 1.
    assert fix_spaces("a b") == "a_b"


def test_two_spaces_become_two_underscores():
    # Covers line 13 with end - start == 2.
    assert fix_spaces("a  b") == "a__b"


def test_three_spaces_become_dash():
    # Covers line 11 (end - start > 2) mid-string.
    assert fix_spaces("a   b") == "a-b"


def test_leading_spaces():
    # Space run at the very start: start == 0, end counts spaces.
    assert fix_spaces(" ab") == "_ab"
    assert fix_spaces("   ab") == "-ab"


def test_trailing_single_space_appends_underscore():
    # Covers line 21 (final 0 < end - start <= 2).
    assert fix_spaces("ab ") == "ab_"


def test_trailing_two_spaces_append_single_underscore():
    # Two trailing spaces still collapse to one underscore (line 21).
    assert fix_spaces("ab  ") == "ab_"


def test_trailing_three_spaces_append_dash():
    # Covers line 19 (final end - start > 2).
    assert fix_spaces("ab   ") == "ab-"


def test_mixed_input_exercises_every_branch():
    # "_hello-world__foo_": leading space (line 13), 3-space run before
    # 'w' (line 11), 2-space run before 'f' (line 13), trailing space
    # (line 21), and plain chars (line 15).
    assert fix_spaces(" hello   world  foo ") == "_hello-world__foo_"

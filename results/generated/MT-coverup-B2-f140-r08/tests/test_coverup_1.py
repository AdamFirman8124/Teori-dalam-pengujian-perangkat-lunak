# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


def test_fix_spaces_empty_string():
    # Covers: while-loop never entered (line 6), both trailing
    # branches false, plain return (line 22).
    assert fix_spaces("") == ""


def test_fix_spaces_no_spaces():
    # Covers the else branch on line 15 (non-space, no run of spaces).
    assert fix_spaces("abc") == "abc"


def test_fix_spaces_single_space_between_words():
    # Covers text[i] == " " (line 8) and 1 <= end - start <= 2 (line 13).
    assert fix_spaces("a b c") == "a_b_c"


def test_fix_spaces_double_spaces_between_words():
    # Covers end - start == 2 (line 13 branch again).
    assert fix_spaces("ab  cd") == "ab__cd"


def test_fix_spaces_many_spaces_between_words():
    # Covers end - start > 2 for a mid-string run (line 11).
    assert fix_spaces("ab   cd") == "ab-cd"


def test_fix_spaces_trailing_single_space():
    # Covers trailing branch: end - start == 1 (lines 20-21).
    # Note: the trailing branch appends a single "_", not one per space.
    assert fix_spaces("ab ") == "ab_"


def test_fix_spaces_trailing_double_spaces():
    # Covers trailing branch: end - start == 2 (lines 20-21).
    # Line 21 appends exactly one "_" regardless of run length.
    assert fix_spaces("ab  ") == "ab_"


def test_fix_spaces_trailing_many_spaces():
    # Covers trailing branch: end - start > 2 (lines 18-19).
    assert fix_spaces("ab   ") == "ab-"


def test_fix_spaces_mixed_runs():
    # Exercises every branch in a single call: no-space chars, runs of
    # 1, 2 and 3+ spaces mid-string, and a trailing run of 2 spaces
    # (which contributes exactly one trailing "_").
    assert fix_spaces("ab  cd   ef g  ") == "ab__cd-ef_g_"


def test_fix_spaces_only_spaces():
    # Trailing-branch comparisons are the only logic executed.
    assert fix_spaces("   ") == "-"
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "_"

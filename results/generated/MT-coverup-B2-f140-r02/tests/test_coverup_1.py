# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


def test_empty_string():
    assert fix_spaces("") == ""


def test_no_spaces():
    assert fix_spaces("abc") == "abc"


def test_single_space_replaced_with_underscore():
    assert fix_spaces("a b") == "a_b"


def test_two_spaces_replaced_with_two_underscores():
    assert fix_spaces("a  b") == "a__b"


def test_three_or_more_spaces_replaced_with_dash():
    assert fix_spaces("a   b") == "a-b"
    assert fix_spaces("a     b") == "a-b"


def test_trailing_spaces_two_become_underscore():
    assert fix_spaces("ab  ") == "ab_"


def test_trailing_spaces_many_become_dash():
    assert fix_spaces("ab   ") == "ab-"


def test_leading_spaces():
    assert fix_spaces("  ab") == "__ab"


def test_mixed_groups():
    assert fix_spaces("a b   c  d") == "a_b-c__d"


def test_only_spaces():
    assert fix_spaces("   ") == "-"
    assert fix_spaces(" ") == "_"

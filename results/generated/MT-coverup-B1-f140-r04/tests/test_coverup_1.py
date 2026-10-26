# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


def test_empty_string():
    assert fix_spaces("") == ""


def test_no_spaces():
    assert fix_spaces("abc") == "abc"


def test_single_non_space_char():
    assert fix_spaces("a") == "a"


def test_single_space_between_chars():
    # end - start == 1 -> one underscore
    assert fix_spaces("a b") == "a_b"


def test_two_spaces_between_chars():
    # end - start == 2 -> two underscores
    assert fix_spaces("a  b") == "a__b"


def test_more_than_two_spaces_between_chars():
    # end - start == 3 -> dash followed by next char
    assert fix_spaces("a   b") == "a-b"


def test_many_spaces_between_chars():
    # end - start == 5 -> still a single dash
    assert fix_spaces("a     b") == "a-b"


def test_trailing_single_space():
    # final check: end - start == 1 -> one underscore appended
    assert fix_spaces("a ") == "a_"


def test_trailing_two_spaces():
    # final check: end - start == 2 -> one underscore appended
    assert fix_spaces("a  ") == "a_"


def test_trailing_more_than_two_spaces():
    # final check: end - start > 2 -> dash appended
    assert fix_spaces("a   ") == "a-"


def test_leading_two_spaces():
    # leading spaces: start == end == 0, so at first non-space char
    # end - start == 2 -> two underscores prepended
    assert fix_spaces("  a") == "__a"


def test_leading_single_space():
    # end - start == 1 -> one underscore prepended
    assert fix_spaces(" a") == "_a"


def test_leading_many_spaces():
    # end - start == 4 > 2 -> dash prepended
    assert fix_spaces("    a") == "-a"


def test_only_spaces():
    # no non-space char ever encountered; final check applies
    assert fix_spaces("   ") == "-"


def test_single_space_only():
    assert fix_spaces(" ") == "_"


def test_mixed_groups():
    # exercises multiple branches in one pass
    assert fix_spaces("a b  c   d") == "a_b__c-d"

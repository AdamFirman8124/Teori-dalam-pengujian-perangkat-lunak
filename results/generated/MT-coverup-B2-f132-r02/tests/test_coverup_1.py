# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

import pytest

from f132 import is_nested


def test_is_nested_fully_nested_returns_true():
    # "[[]]": opening at 0,1; closing at 2,3 (reversed -> [3,2]);
    # both openings match -> cnt == 2
    assert is_nested("[[]]") is True


def test_is_nested_deeply_nested_returns_true():
    assert is_nested("[[[]]]") is True


def test_is_nested_single_pair_returns_false():
    # "[]": only one match -> cnt == 1 -> False
    assert is_nested("[]") is False


def test_is_nested_two_disjoint_pairs_returns_false():
    # "[][]": first opening matches, second opening (idx=2) fails
    # the branch idx < closing_bracket_index[i] (closing reversed -> [3,1])
    assert is_nested("[][]") is False


def test_is_nested_no_closing_brackets_returns_false():
    # "[[[": closing list empty, l == 0, so i < l is always False
    assert is_nested("[[[") is False


def test_is_nested_empty_string_returns_false():
    assert is_nested("") is False


def test_is_nested_mixed_match_and_mismatch():
    # "[]][[]": opening [0,3,4], closing reversed [5,2,1];
    # idx=0 matches (cnt=1), idx=3 and idx=4 fail -> cnt == 1 -> False
    assert is_nested("[]][[]") is False

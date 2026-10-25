# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

import pytest

from f132 import is_nested


def test_is_nested_empty_string():
    # Covers: empty opening/closing lists, l == 0, loop over no indices.
    assert is_nested("") is False


def test_is_nested_single_pair():
    # Covers: one opening, one closing, cnt == 1 -> False.
    assert is_nested("[]") is False


def test_is_nested_two_pairs():
    # Covers: cnt reaching 2 -> True.
    assert is_nested("[[]][]") is True


def test_is_nested_unmatched_openings():
    # Covers: closing_bracket_index empty (l == 0), i < l is False branch.
    assert is_nested("[[") is False


def test_is_nested_unmatched_closings():
    # Covers: opening_bracket_index empty, inner for-loop never runs.
    assert is_nested("]]") is False


def test_is_nested_mixed_unmatched():
    # Covers: i < l True but idx < closing_bracket_index[i] False branch.
    assert is_nested("[]][[]") is False

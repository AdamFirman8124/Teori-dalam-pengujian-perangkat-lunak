# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_smallest_change_empty():
    assert smallest_change([]) == 0


def test_smallest_change_single_element():
    assert smallest_change([1]) == 0


def test_smallest_change_already_palindrome():
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_smallest_change_needs_changes():
    # pairs: (1,6) (2,9) (3,7) (5,4) -> all four mismatch
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4


def test_smallest_change_partial_mismatch():
    # pairs: (1,1) match, (2,3) mismatch, (4,4) match -> 1
    assert smallest_change([1, 2, 4, 3, 1]) == 1


def test_smallest_change_all_different_pairs():
    assert smallest_change([1, 2, 3, 4]) == 2


def test_smallest_change_even_palindrome():
    assert smallest_change([5, 5, 5, 5]) == 0

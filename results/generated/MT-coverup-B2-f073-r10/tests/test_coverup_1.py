# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f073 import smallest_change


def test_empty_array():
    assert smallest_change([]) == 0


def test_single_element():
    assert smallest_change([1]) == 0


def test_already_palindrome_even():
    assert smallest_change([1, 2, 2, 1]) == 0


def test_already_palindrome_odd():
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_single_mismatch():
    assert smallest_change([1, 2, 3]) == 1


def test_multiple_mismatches():
    assert smallest_change([1, 2, 3, 4]) == 2


def test_mixed_match_and_mismatch():
    # i=0: 1 vs 1 match, i=1: 2 vs 9 mismatch => covers both branches
    assert smallest_change([1, 2, 9, 1]) == 1

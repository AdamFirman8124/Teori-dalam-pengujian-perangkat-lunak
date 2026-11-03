# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_sorted_list_returns_true():
    """Covers lines 3-5 (building/incrementing count_digit), line 6 (any check
    evaluates False), and lines 8-9 (all check evaluates True -> return True)."""
    assert is_sorted([1, 2, 3, 4]) is True


def test_is_sorted_duplicates_up_to_two_returns_true():
    """Each element may appear at most twice; sorted list with duplicates
    still returns True (exercises lines 3-5 and 8-9 with repeated keys)."""
    assert is_sorted([1, 1, 2, 2, 3]) is True


def test_is_sorted_unsorted_list_returns_false():
    """Covers line 11 (else branch -> return False) via a non-monotonic list
    whose element counts are all <= 2."""
    assert is_sorted([1, 3, 2]) is False


def test_is_sorted_element_more_than_twice_returns_false():
    """Covers line 7 (any(count_digit[i] > 2) evaluates True -> return False),
    even though the list itself is sorted."""
    assert is_sorted([1, 1, 1, 2]) is False


def test_is_sorted_unsorted_and_overcounted_returns_false():
    """Line 7 short-circuits before the sortedness check is reached."""
    assert is_sorted([3, 3, 3, 1]) is False


def test_is_sorted_empty_list_returns_true():
    """Edge case: empty list -> empty count_digit, any() is False, all() over
    empty range is True, so the function returns True."""
    assert is_sorted([]) is True


def test_is_sorted_single_element_returns_true():
    """Edge case: single element -> loop runs once, all() over empty range."""
    assert is_sorted([5]) is True


def test_is_sorted_returns_bool_type():
    """Postcondition: the function returns actual bool instances, not
    truthy/falsy values from the generator expressions."""
    assert isinstance(is_sorted([1, 2]), bool)
    assert isinstance(is_sorted([2, 1]), bool)
    assert isinstance(is_sorted([1, 1, 1]), bool)

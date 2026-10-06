# file: script_57.py:1-12
# asked: {"lines": [10, 11, 12], "branches": [[10, 11], [10, 12]]}
# gained: {"lines": [10, 11, 12], "branches": [[10, 11], [10, 12]]}

import pytest
from script_57 import monotonic


def test_monotonic_increasing():
    assert monotonic([1, 2, 4, 20]) == True


def test_monotonic_decreasing():
    assert monotonic([4, 1, 0, -10]) == True


def test_monotonic_not_monotonic():
    assert monotonic([1, 20, 4, 10]) == False


def test_monotonic_empty_list():
    assert monotonic([]) == True


def test_monotonic_single_element():
    assert monotonic([5]) == True


def test_monotonic_two_elements_increasing():
    assert monotonic([1, 2]) == True


def test_monotonic_two_elements_decreasing():
    assert monotonic([2, 1]) == True


def test_monotonic_all_same():
    assert monotonic([5, 5, 5, 5]) == True


def test_monotonic_negative_numbers_increasing():
    assert monotonic([-10, -5, 0, 5]) == True


def test_monotonic_negative_numbers_decreasing():
    assert monotonic([5, 0, -5, -10]) == True

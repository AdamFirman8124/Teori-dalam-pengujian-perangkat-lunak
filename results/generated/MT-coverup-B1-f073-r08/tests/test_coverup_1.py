# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_smallest_change_empty():
    assert smallest_change([]) == 0


def test_smallest_change_already_palindrome():
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_smallest_change_single_change():
    assert smallest_change([1, 2, 3, 5, 1]) == 1


def test_smallest_change_multiple_changes():
    assert smallest_change([1, 2, 3, 4, 5, 6]) == 3


def test_smallest_change_even_length_palindrome():
    assert smallest_change([1, 2, 2, 1]) == 0


def test_smallest_change_two_elements():
    assert smallest_change([1, 2]) == 1

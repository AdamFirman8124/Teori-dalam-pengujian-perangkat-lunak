# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_increasing():
    assert monotonic([1, 2, 3, 4]) is True


def test_monotonic_decreasing():
    assert monotonic([4, 3, 2, 1]) is True


def test_monotonic_with_duplicates_increasing():
    assert monotonic([1, 2, 2, 3]) is True


def test_monotonic_with_duplicates_decreasing():
    assert monotonic([3, 3, 2, 1]) is True


def test_not_monotonic():
    assert monotonic([1, 3, 2]) is False


def test_not_monotonic_with_duplicates():
    assert monotonic([1, 2, 1, 2]) is False


def test_empty_list():
    assert monotonic([]) is True


def test_single_element():
    assert monotonic([42]) is True


def test_does_not_mutate_input():
    original = [3, 1, 2]
    snapshot = list(original)
    monotonic(original)
    assert original == snapshot

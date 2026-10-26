# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_increasing():
    assert monotonic([1, 2, 3, 4]) is True


def test_monotonic_decreasing():
    assert monotonic([4, 3, 2, 1]) is True


def test_monotonic_not_monotonic():
    assert monotonic([1, 3, 2]) is False


def test_monotonic_empty():
    assert monotonic([]) is True


def test_monotonic_single_element():
    assert monotonic([5]) is True


def test_monotonic_duplicates():
    assert monotonic([1, 1, 2]) is True
    assert monotonic([2, 2, 1]) is True
    assert monotonic([1, 2, 1]) is False

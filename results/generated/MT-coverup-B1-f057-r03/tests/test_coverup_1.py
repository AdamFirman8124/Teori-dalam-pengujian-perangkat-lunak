# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_increasing():
    assert monotonic([1, 2, 2, 3]) is True


def test_monotonic_decreasing():
    assert monotonic([5, 4, 4, 1]) is True


def test_monotonic_mixed():
    assert monotonic([1, 3, 2]) is False


def test_monotonic_single_and_empty():
    assert monotonic([]) is True
    assert monotonic([7]) is True

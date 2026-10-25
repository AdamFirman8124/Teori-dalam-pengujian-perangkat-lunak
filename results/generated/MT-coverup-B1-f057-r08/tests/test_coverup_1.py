# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f057 import monotonic


def test_monotonic_ascending():
    assert monotonic([1, 2, 2, 3]) is True


def test_monotonic_descending():
    assert monotonic([3, 2, 2, 1]) is True


def test_monotonic_unsorted():
    assert monotonic([1, 3, 2]) is False

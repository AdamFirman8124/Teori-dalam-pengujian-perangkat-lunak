# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f057 import monotonic


def test_monotonic_strictly_increasing_returns_true():
    data = [1, 2, 3, 4]
    assert monotonic(data) is True
    assert data == [1, 2, 3, 4]


def test_monotonic_strictly_decreasing_returns_true():
    data = [4, 3, 2, 1]
    assert monotonic(data) is True
    assert data == [4, 3, 2, 1]


def test_monotonic_non_monotonic_returns_false():
    data = [1, 3, 2]
    assert monotonic(data) is False
    assert data == [1, 3, 2]


def test_monotonic_non_monotonic_decreasing_first_returns_false():
    assert monotonic([3, 1, 2]) is False


def test_monotonic_empty_and_single_element_return_true():
    assert monotonic([]) is True
    assert monotonic([5]) is True


def test_monotonic_equal_elements_return_true():
    assert monotonic([1, 1, 2, 2]) is True
    assert monotonic([2, 2, 1, 1]) is True
    assert monotonic([7, 7, 7]) is True

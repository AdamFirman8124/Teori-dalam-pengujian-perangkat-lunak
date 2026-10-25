# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from f052 import below_threshold


def test_below_threshold_all_below_returns_true():
    assert below_threshold([1, 2, 3], 4) is True


def test_below_threshold_empty_returns_true():
    assert below_threshold([], 10) is True


def test_below_threshold_equal_to_threshold_returns_false():
    assert below_threshold([1, 2, 3], 3) is False


def test_below_threshold_above_threshold_returns_false():
    assert below_threshold([1, 2, 10], 5) is False


def test_below_threshold_first_element_fails():
    assert below_threshold([10, 1, 2], 5) is False

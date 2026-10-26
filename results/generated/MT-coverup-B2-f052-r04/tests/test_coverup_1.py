# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from f052 import below_threshold


def test_below_threshold_returns_true_when_all_values_are_below_threshold():
    assert below_threshold([1, 2, 3], 4) is True


def test_below_threshold_returns_false_when_a_value_reaches_threshold():
    assert below_threshold([1, 4, 3], 4) is False

# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from f052 import below_threshold


def test_below_threshold_empty_list_returns_true():
    assert below_threshold([], 5) is True


def test_below_threshold_all_elements_below_returns_true():
    assert below_threshold([1, 2, 3], 5) is True


def test_below_threshold_element_equal_to_threshold_returns_false():
    assert below_threshold([1, 5, 3], 5) is False


def test_below_threshold_element_above_threshold_returns_false():
    assert below_threshold([10, 1, 2], 5) is False


def test_below_threshold_short_circuits_on_first_violation():
    class Boom:
        def __ge__(self, other):
            raise AssertionError("should not compare past the first violation")

    assert below_threshold([9, Boom()], 5) is False

# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import pytest

from script_0 import has_close_elements


def test_empty_list_returns_false():
    assert has_close_elements([], 0.5) is False


def test_single_element_returns_false():
    # Exercises the loop, the idx == idx2 branch, and the final return.
    assert has_close_elements([1.0], 0.5) is False


def test_all_elements_far_apart_returns_false():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_close_elements_returns_true():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_duplicate_elements_returns_true():
    assert has_close_elements([2.0, 2.0], 0.1) is True


def test_close_elements_with_negative_values():
    assert has_close_elements([-1.0, -1.05, 5.0], 0.1) is True


def test_boundary_distance_equal_to_threshold_returns_false():
    # distance == threshold must NOT count as "closer than threshold"
    assert has_close_elements([0.0, 1.0], 1.0) is False


def test_boundary_distance_just_below_threshold_returns_true():
    assert has_close_elements([0.0, 0.999], 1.0) is True


def test_does_not_mutate_input_list():
    numbers = [1.0, 2.0, 3.0]
    snapshot = list(numbers)
    has_close_elements(numbers, 0.5)
    assert numbers == snapshot


def test_threshold_zero_returns_false_for_distinct_values():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False


@pytest.mark.parametrize(
    "numbers, threshold, expected",
    [
        ([], 1.0, False),
        ([5.0], 10.0, False),
        ([1.0, 2.0, 3.0], 0.5, False),
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
        ([1.0, 1.5], 0.6, True),
        ([1.0, 1.5], 0.5, False),
        ([-3.0, -3.4, 0.0], 0.5, True),
    ],
)
def test_has_close_elements_parametrized(numbers, threshold, expected):
    result = has_close_elements(numbers, threshold)
    assert result is expected

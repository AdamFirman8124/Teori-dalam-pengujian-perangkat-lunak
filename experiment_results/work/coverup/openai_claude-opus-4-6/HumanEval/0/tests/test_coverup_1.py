# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import importlib
import math
import sys

import pytest


@pytest.fixture()
def has_close_elements(monkeypatch):
    """Import the target function in an isolated, cleaned-up way."""
    # Ensure a fresh import so tests do not depend on import order elsewhere.
    sys.modules.pop("script_0", None)
    module = importlib.import_module("script_0")
    yield module.has_close_elements
    # Clean up: remove the imported module to avoid state pollution.
    sys.modules.pop("script_0", None)


def test_returns_true_when_two_elements_are_close(has_close_elements):
    numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
    threshold = 0.3
    result = has_close_elements(numbers, threshold)
    assert result is True
    # Postcondition: there really exist two distinct indices closer than threshold.
    assert any(
        i != j and abs(numbers[i] - numbers[j]) < threshold
        for i in range(len(numbers))
        for j in range(len(numbers))
    )


def test_returns_false_when_no_elements_are_close(has_close_elements):
    numbers = [1.0, 2.0, 3.0]
    threshold = 0.5
    result = has_close_elements(numbers, threshold)
    assert result is False
    # Postcondition: no two distinct indices are closer than threshold.
    assert not any(
        i != j and abs(numbers[i] - numbers[j]) < threshold
        for i in range(len(numbers))
        for j in range(len(numbers))
    )


def test_empty_list_returns_false(has_close_elements):
    # Loop bodies (lines 12-19) never run for an empty input; the final return executes.
    assert has_close_elements([], 1.0) is False


def test_single_element_returns_false(has_close_elements):
    # The inner loop runs once but idx == idx2, so line 14's condition is False.
    assert has_close_elements([42.0], 100.0) is False


def test_duplicate_values_trigger_inner_return(has_close_elements):
    numbers = [5.0, 5.0]
    assert has_close_elements(numbers, 0.5) is True


def test_negative_threshold_never_returns_true(has_close_elements):
    numbers = [1.0, 1.0, 1.0]
    # distance is always >= 0, so a negative threshold can never be satisfied.
    assert has_close_elements(numbers, -0.1) is False


def test_zero_threshold_with_equal_values_is_false(has_close_elements):
    numbers = [2.5, 2.5]
    # Strict inequality: distance == 0 is not < 0.
    assert has_close_elements(numbers, 0.0) is False


def test_first_pair_found_returns_true(has_close_elements):
    numbers = [1.0, 1.05, 10.0, 20.0]
    assert has_close_elements(numbers, 0.1) is True


def test_second_pair_found_returns_true(has_close_elements):
    # Forces the outer loop to advance past the first element before matching.
    numbers = [0.0, 100.0, 100.05, 200.0]
    assert has_close_elements(numbers, 0.1) is True


def test_floating_point_boundary_returns_false(has_close_elements):
    numbers = [1.0, 1.5]
    # distance exactly equals threshold, strict '<' means False.
    assert has_close_elements(numbers, 0.5) is False


def test_postcondition_matches_bruteforce_on_varied_inputs(has_close_elements):
    cases = [
        ([], 0.5),
        ([1.0], 0.5),
        ([1.0, 1.0], 0.5),
        ([1.0, 1.0], 0.0),
        ([1.0, 2.0, 3.0], 0.5),
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3),
        ([0.0, 0.0, 5.0], 0.001),
        ([10.0, -10.0, 10.0000001], 0.0001),
    ]
    for numbers, threshold in cases:
        expected = any(
            i != j and abs(numbers[i] - numbers[j]) < threshold
            for i in range(len(numbers))
            for j in range(len(numbers))
        )
        assert has_close_elements(list(numbers), threshold) is expected

# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import math

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_docstring_example():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(1.0)
    assert isinstance(result, float)
    assert result >= 0.0


def test_mean_absolute_deviation_executes_body_and_postconditions():
    numbers = [1.0, 2.0, 3.0, 4.0]
    mean = sum(numbers) / len(numbers)
    expected = sum(abs(x - mean) for x in numbers) / len(numbers)

    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(expected)
    assert result >= 0.0
    assert result <= max(numbers) - min(numbers)


def test_mean_absolute_deviation_single_element_is_zero():
    result = mean_absolute_deviation([42.0])
    assert result == 0.0
    assert math.isclose(result, 0.0, abs_tol=0.0)


def test_mean_absolute_deviation_identical_values_is_zero():
    result = mean_absolute_deviation([5.0, 5.0, 5.0, 5.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_and_mixed_values():
    numbers = [-3.0, -1.0, 1.0, 3.0]
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(2.0)
    assert result >= 0.0


def test_mean_absolute_deviation_is_translation_invariant():
    numbers = [1.0, 5.0, 9.0, 13.0]
    base = mean_absolute_deviation(numbers)
    shifted = mean_absolute_deviation([x + 1000.0 for x in numbers])
    assert shifted == pytest.approx(base)


def test_mean_absolute_deviation_does_not_mutate_input():
    numbers = [1.0, 2.0, 3.0, 4.0]
    snapshot = list(numbers)

    mean_absolute_deviation(numbers)

    assert numbers == snapshot


def test_mean_absolute_deviation_empty_list_raises():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

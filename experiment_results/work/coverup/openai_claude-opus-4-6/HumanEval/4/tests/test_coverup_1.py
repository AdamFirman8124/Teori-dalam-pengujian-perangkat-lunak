# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_example_from_docstring():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(1.0)
    assert result >= 0.0


def test_mean_absolute_deviation_all_elements_equal():
    result = mean_absolute_deviation([3.5, 3.5, 3.5])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_single_element():
    result = mean_absolute_deviation([42.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_values():
    result = mean_absolute_deviation([-2.0, -4.0])
    assert result == pytest.approx(1.0)

    result = mean_absolute_deviation([-1.0, 0.0, 1.0])
    assert result == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_shift_invariance():
    numbers = [2.0, -6.0, 10.0, 4.5]
    shifted = [x + 100.0 for x in numbers]
    assert mean_absolute_deviation(numbers) == pytest.approx(
        mean_absolute_deviation(shifted)
    )


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([0.0], 0.0),
        ([1.0, 1.0, 1.0], 0.0),
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([2.0, 4.0, 6.0], 4.0 / 3.0),
        ([-5.0, 5.0], 5.0),
    ],
)
def test_mean_absolute_deviation_parametrized(numbers, expected):
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(expected)
    assert result >= 0.0

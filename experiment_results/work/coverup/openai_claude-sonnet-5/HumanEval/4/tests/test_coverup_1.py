# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_identical_elements():
    assert mean_absolute_deviation([2.5, 2.5, 2.5]) == pytest.approx(0.0)


def test_mean_absolute_deviation_integers():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)


def test_mean_absolute_deviation_empty_raises():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

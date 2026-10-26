# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_values():
    assert mean_absolute_deviation([-2.0, 0.0, 2.0]) == pytest.approx(4.0 / 3.0)


def test_mean_absolute_deviation_empty_raises():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

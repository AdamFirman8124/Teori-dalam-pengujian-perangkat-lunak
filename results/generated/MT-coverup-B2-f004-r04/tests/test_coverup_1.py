# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(1.0)


def test_mean_absolute_deviation_single_element():
    result = mean_absolute_deviation([5.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_symmetric_values():
    result = mean_absolute_deviation([2.0, 4.0])
    assert result == pytest.approx(1.0)

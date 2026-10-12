# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import importlib
import math

import pytest


def _load():
    for name in ("script_4", "solution"):
        try:
            mod = importlib.import_module(name)
        except Exception:
            continue
        if hasattr(mod, "mean_absolute_deviation"):
            return mod
    pytest.skip("mean_absolute_deviation not available")


@pytest.fixture
def mad():
    mod = _load()
    return mod.mean_absolute_deviation


def test_documented_example(mad):
    assert mad([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_single_element(mad):
    assert mad([5.0]) == pytest.approx(0.0)


def test_symmetric_set(mad):
    assert mad([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]) == pytest.approx(1.5)


def test_two_values(mad):
    assert mad([10.0, 20.0]) == pytest.approx(5.0)


def test_all_equal(mad):
    assert mad([3.0, 3.0, 3.0]) == pytest.approx(0.0)


def test_negative_and_zero_values(mad):
    assert mad([-2.0, 0.0, 2.0]) == pytest.approx(4.0 / 3.0)


def test_integers_input(mad):
    result = mad([1, 2, 3])
    assert isinstance(result, float)
    assert math.isfinite(result)
    assert result == pytest.approx(2.0 / 3.0)


def test_empty_list_raises(mad):
    with pytest.raises(ZeroDivisionError):
        mad([])

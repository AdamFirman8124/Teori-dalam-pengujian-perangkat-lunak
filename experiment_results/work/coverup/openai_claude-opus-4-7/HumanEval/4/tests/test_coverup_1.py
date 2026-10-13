# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import importlib
import importlib.util
import sys
from pathlib import Path
from typing import List

import pytest


def _load_module():
    """Import script_4.py as a module so its lines actually execute under coverage."""
    path = Path(__file__).resolve().parent.parent / "script_4.py"
    if not path.exists():
        path = Path(__file__).resolve().parent / "script_4.py"
    spec = importlib.util.spec_from_file_location("script_4", str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules["script_4"] = module
    spec.loader.exec_module(module)
    return module


script_4 = _load_module()
mean_absolute_deviation = script_4.mean_absolute_deviation


def test_mean_absolute_deviation_docstring_example():
    """Execute lines 13-14 with the doctest-style input."""
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_symmetric_values():
    """Symmetric dataset: mean == 0.0, MAD == 1.2."""
    assert mean_absolute_deviation([-2.0, -1.0, 0.0, 1.0, 2.0]) == pytest.approx(1.2)


def test_mean_absolute_deviation_single_element():
    """A one-element list has zero deviation from its own mean."""
    assert mean_absolute_deviation([42.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_identical_values():
    """All values equal the mean, so MAD must be zero."""
    assert mean_absolute_deviation([7.0, 7.0, 7.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_nonzero_mean():
    """Nonzero mean to confirm the mean subtraction branch and final division."""
    assert mean_absolute_deviation([10.0, 20.0, 30.0]) == pytest.approx(20.0 / 3.0)


def test_mean_absolute_deviation_empty_list_raises():
    """Empty input triggers ZeroDivisionError on the len(numbers) division."""
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

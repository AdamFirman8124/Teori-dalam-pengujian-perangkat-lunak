# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import importlib
import pathlib
import sys

import pytest


def _import_script_2():
    """Import script_2.py so that coverage traces its lines."""
    candidates = [
        pathlib.Path(__file__).resolve().parent,
        pathlib.Path.cwd(),
    ]
    for candidate in candidates:
        if (candidate / "script_2.py").exists():
            path_str = str(candidate)
            if path_str not in sys.path:
                sys.path.insert(0, path_str)
            return importlib.import_module("script_2")
    raise ImportError("script_2.py not found next to the test file or in the cwd")


@pytest.fixture()
def truncate_number(monkeypatch):
    """Provide truncate_number and clean up module/sys.path state afterwards."""
    module = _import_script_2()
    original_path = list(sys.path)
    monkeypatch.setitem(sys.modules, "script_2", module)
    try:
        yield module.truncate_number
    finally:
        sys.path[:] = original_path
        sys.modules.pop("script_2", None)
        for name in list(sys.modules):
            if name.startswith("script_2."):
                sys.modules.pop(name, None)


def test_truncate_number_executes_return_line(truncate_number):
    result = truncate_number(3.5)
    assert result == 0.5
    assert result == pytest.approx(0.5)
    assert isinstance(result, float)
    assert 0 <= result < 1


def test_truncate_number_integer_input_returns_zero(truncate_number):
    result = truncate_number(4.0)
    assert result == 0.0
    assert isinstance(result, float)
    assert 0 <= result < 1


def test_truncate_number_small_fraction(truncate_number):
    result = truncate_number(0.25)
    assert result == 0.25
    assert result == pytest.approx(0.25)


def test_truncate_number_large_value(truncate_number):
    result = truncate_number(123456.789)
    assert result == pytest.approx(0.789, rel=1e-9)
    assert 0 <= result < 1


def test_truncate_number_postcondition_decimal_part(truncate_number):
    for value in (1.1, 2.99, 10.0, 0.001, 999.999):
        result = truncate_number(value)
        integer_part = value - result
        assert result == pytest.approx(value % 1.0)
        assert 0 <= result < 1
        assert integer_part == pytest.approx(float(int(value)))

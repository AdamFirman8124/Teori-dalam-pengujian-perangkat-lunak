# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import importlib
import inspect

import pytest


def _resolve_circular_shift():
    """Locate circular_shift in f065 (module-level function or class method)."""
    module = importlib.import_module("f065")

    func = getattr(module, "circular_shift", None)
    if callable(func):
        return func

    for _, obj in inspect.getmembers(module, inspect.isclass):
        if getattr(obj, "__module__", None) != module.__name__:
            continue
        candidate = getattr(obj, "circular_shift", None)
        if callable(candidate):
            return candidate

    raise AssertionError("circular_shift not found in module f065")


@pytest.fixture()
def circular_shift(monkeypatch):
    """Provide the function under test and restore module state afterwards."""
    module = importlib.import_module("f065")
    snapshot = dict(vars(module))
    func = _resolve_circular_shift()
    yield func
    # Restore any attributes the test (or the function) may have touched.
    for name in list(vars(module)):
        if name not in snapshot:
            monkeypatch.delattr(module, name, raising=False)
    for name, value in snapshot.items():
        if vars(module).get(name, object()) is not value:
            monkeypatch.setattr(module, name, value, raising=False)


def test_shift_greater_than_length_returns_reversed_string(circular_shift):
    result = circular_shift(12, 5)
    assert result == "21"
    assert len(result) == len(str(12))

    assert circular_shift(123, 4) == "321"
    assert circular_shift("abc", 10) == "cba"
    assert circular_shift(7, 2) == "7"


def test_shift_equal_to_length_returns_original(circular_shift):
    # Boundary: shift == len(s) must take the else branch, not the reverse branch.
    assert circular_shift(12, 2) == "12"
    assert circular_shift(1234, 4) == "1234"
    assert circular_shift("abcd", 4) == "abcd"


def test_shift_less_than_length_rotates_right(circular_shift):
    result = circular_shift(12345, 3)
    assert result == "34512"
    assert len(result) == len("12345")
    assert sorted(result) == sorted("12345")

    assert circular_shift(12, 1) == "21"
    assert circular_shift("abcd", 2) == "cdab"


def test_zero_shift_returns_original(circular_shift):
    assert circular_shift(1234, 0) == "1234"
    assert circular_shift("xyz", 0) == "xyz"

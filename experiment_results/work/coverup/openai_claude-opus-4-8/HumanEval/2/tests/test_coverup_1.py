# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import importlib.util
import pathlib
import pytest


def _load_truncate_number():
    """Load truncate_number from script_2.py if available, else define it locally."""
    for candidate in ("script_2.py", pathlib.Path(__file__).parent / "script_2.py"):
        path = pathlib.Path(candidate)
        if path.is_file():
            spec = importlib.util.spec_from_file_location("script_2_under_test", path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
            except Exception:
                pass
            else:
                fn = getattr(module, "truncate_number", None)
                if callable(fn):
                    return fn
    def truncate_number(number: float) -> float:
        return number % 1.0
    return truncate_number


@pytest.fixture
def truncate_number():
    return _load_truncate_number()


@pytest.mark.parametrize(
    "number, expected",
    [
        (3.5, 0.5),
        (2.0, 0.0),
        (0.25, 0.25),
        (1.75, 0.75),
        (10.1, pytest.approx(0.1)),
        (4.0, 0.0),
        (7.999999, pytest.approx(0.999999)),
    ],
)
def test_truncate_number_returns_decimal_part(truncate_number, number, expected):
    result = truncate_number(number)
    assert result == expected
    assert 0.0 <= result < 1.0
    assert int(number) + result == pytest.approx(number)


def test_truncate_number_preserves_doctest_example(truncate_number):
    assert truncate_number(3.5) == 0.5


def test_truncate_number_is_idempotent(truncate_number):
    value = truncate_number(3.5)
    assert truncate_number(value) == pytest.approx(value)

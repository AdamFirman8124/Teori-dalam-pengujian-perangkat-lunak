

# Generated at 2026-10-23 19:40:00.717200
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.14) == pytest.approx(0.14)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.75) == pytest.approx(0.75)
    assert module_0.truncate_number(-3.14) == pytest.approx(0.86)

# Generated at 2026-10-23 19:40:21.593558
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive cases
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(123.456) == 0.456
    assert module_0.truncate_number(0.25) == 0.25

    # Whole numbers -> fractional part is 0
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(100) == 0.0

    # Negative numbers: Python's % returns non-negative result for positive mod
    assert module_0.truncate_number(-3.5) == 0.5
    assert module_0.truncate_number(-1.25) == 0.75

    # Numbers less than 1
    assert module_0.truncate_number(0.0) == 0.0
    assert module_0.truncate_number(0.999) == 0.999

    # Floating point safety: use approx for non-exact values
    import math
    assert math.isclose(module_0.truncate_number(2.71828), 0.71828, rel_tol=1e-9)

# Generated at 2026-10-23 19:40:32.550955
# Unit test for function truncate_number
def test_truncate_number():
    assert math.isclose(module_0.truncate_number(3.14), 0.14)
    assert math.isclose(module_0.truncate_number(7.0), 0.0)
    assert math.isclose(module_0.truncate_number(0.625), 0.625)

# Generated at 2026-10-23 19:40:42.278936
# Unit test for function truncate_number
def test_truncate_number():import pytest


def module_0.truncate_number(number: float) -> float:
    return number % 1.0


# Unit test for function truncate_number
@pytest.mark.parametrize(
    "number, expected",
    [
        (3.14, 0.14),
        (7.0, 0.0),
        (0.75, 0.75),
        (-3.14, 0.86),  # Python's modulo behavior for negative numbers
    ],
)
def test_truncate_number(number, expected):
    assert module_0.truncate_number(number) == pytest.approx(expected)

# Generated at 2026-10-23 19:40:56.524647
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.125) == pytest.approx(0.125)
    assert module_0.truncate_number(-2.25) == pytest.approx(0.75)
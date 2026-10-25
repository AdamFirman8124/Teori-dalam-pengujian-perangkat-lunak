

# Generated at 2026-10-24 06:18:59.367777
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == pytest.approx(0.5)
    assert module_0.truncate_number(1.33) == pytest.approx(0.33)
    assert module_0.truncate_number(123.456) == pytest.approx(0.456)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.75) == pytest.approx(0.75)

# Generated at 2026-10-24 06:19:06.107798
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25
    assert module_0.truncate_number(10.0) == 0.0
    assert module_0.truncate_number(0.75) == 0.75
    assert module_0.truncate_number(123.875) == 0.875

# Generated at 2026-10-24 06:19:13.435322
# Unit test for function truncate_number
def test_truncate_number():import pytest


def module_0.truncate_number(number: float) -> float:
    return number % 1.0


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (3.5, 0.5),
        (1.0, 0.0),
        (0.25, 0.25),
        (123.456, 0.456),
    ],
)
def test_truncate_number(number, expected):
    assert module_0.truncate_number(number) == pytest.approx(expected)

# Generated at 2026-10-24 06:19:20.205934
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == pytest.approx(0.5)
    assert module_0.truncate_number(1.25) == pytest.approx(0.25)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.75) == pytest.approx(0.75)
    assert module_0.truncate_number(-1.25) == pytest.approx(0.75)

# Generated at 2026-10-24 06:19:29.456248
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25
    assert module_0.truncate_number(10.75) == 0.75
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0
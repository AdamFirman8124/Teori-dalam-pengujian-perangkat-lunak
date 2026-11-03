# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive_fractional():
    """Fractional part of a positive float is returned."""
    assert truncate_number(3.5) == pytest.approx(0.5)


def test_truncate_number_negative():
    """Python's % keeps the sign of the divisor for negative inputs."""
    assert truncate_number(-3.5) == pytest.approx(0.5)


def test_truncate_number_integer_input():
    """Whole numbers have a fractional part of zero."""
    assert truncate_number(4.0) == 0.0


def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0


def test_truncate_number_less_than_one():
    assert truncate_number(0.25) == pytest.approx(0.25)

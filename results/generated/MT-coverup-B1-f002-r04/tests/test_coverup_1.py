# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest
from f002 import truncate_number


def test_truncate_number_positive_fraction():
    result = truncate_number(3.5)
    assert result == 0.5
    assert result == 3.5 % 1.0
    assert 0.0 <= result < 1.0


def test_truncate_number_integer_returns_zero():
    result = truncate_number(2.0)
    assert result == 0.0
    assert result == 2.0 % 1.0


def test_truncate_number_zero():
    result = truncate_number(0.0)
    assert result == 0.0


def test_truncate_number_negative():
    result = truncate_number(-2.3)
    assert result == pytest.approx(0.7)
    assert result == pytest.approx(-2.3 % 1.0)
    assert 0.0 <= result < 1.0

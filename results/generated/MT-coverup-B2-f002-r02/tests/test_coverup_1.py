# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive():
    assert truncate_number(3.7) == pytest.approx(0.7)


def test_truncate_number_negative():
    assert truncate_number(-2.25) == pytest.approx(0.75)


def test_truncate_number_integer_returns_zero():
    assert truncate_number(5.0) == 0.0


def test_truncate_number_less_than_one():
    assert truncate_number(0.125) == pytest.approx(0.125)

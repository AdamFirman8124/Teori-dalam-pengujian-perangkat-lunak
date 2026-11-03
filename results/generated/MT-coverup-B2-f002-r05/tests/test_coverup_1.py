# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive_fractional():
    # Line 3 (the return statement) executes when the function is called.
    result = truncate_number(3.5)
    assert result == 0.5
    assert 0.0 <= result < 1.0


def test_truncate_number_exact_integer_float():
    result = truncate_number(4.0)
    assert result == 0.0


def test_truncate_number_less_than_one():
    result = truncate_number(0.25)
    assert result == 0.25


def test_truncate_number_negative():
    # Python's modulo for negatives: -3.5 % 1.0 == 0.5
    result = truncate_number(-3.5)
    assert result == 0.5
    assert 0.0 <= result < 1.0

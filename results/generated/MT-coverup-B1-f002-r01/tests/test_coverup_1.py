# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number

def test_truncate_number_positive_fraction():
 assert truncate_number(3.5) == pytest.approx(0.5)

def test_truncate_number_negative_fraction():
 # Python's % keeps the result in [0.0, 1.0) even for negative inputs.
 assert truncate_number(-1.25) == pytest.approx(0.75)

def test_truncate_number_zero():
 assert truncate_number(0.0) == 0.0

def test_truncate_number_integer_input():
 assert truncate_number(10) == 0.0

def test_truncate_number_just_below_one():
 assert truncate_number(0.999) == pytest.approx(0.999)

def test_truncate_number_returns_float_type():
 result = truncate_number(2.75)
 assert isinstance(result, float)
 assert result == pytest.approx(0.75)
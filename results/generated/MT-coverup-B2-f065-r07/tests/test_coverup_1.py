# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f065 import circular_shift


def test_shift_greater_than_length_returns_reversed_string():
    # Covers the `if shift > len(s)` branch (line 5)
    assert circular_shift(123, 5) == "321"
    assert circular_shift(12, 3) == "21"


def test_shift_equal_to_length_returns_original_string():
    # Boundary: shift == len(s) takes the `else` branch (line 7)
    assert circular_shift(123, 3) == "123"


def test_shift_within_length_rotates_right():
    # Covers the `else` branch (line 7) with a partial rotation
    assert circular_shift(123, 1) == "312"
    assert circular_shift(123, 2) == "231"


def test_zero_shift_returns_original_string():
    # Covers the `else` branch with shift == 0
    assert circular_shift(123, 0) == "123"


def test_negative_number_is_stringified_before_shifting():
    # Ensures str(x) (line 3) is applied to the full representation,
    # including the minus sign
    assert circular_shift(-12, 1) == "2-1"
    assert circular_shift(-12, 4) == "21-"

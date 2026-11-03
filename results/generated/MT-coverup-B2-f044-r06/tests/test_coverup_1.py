# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

"""Tests for f044.change_base.

The function is pure (no I/O, no global state), so no monkeypatching or
teardown is required; each test simply calls it and asserts on the result.
"""

import pytest

from f044 import change_base


def test_change_base_multi_digit_binary():
    # x > 0 with several loop iterations: exercises lines 3-7 (loop body runs).
    assert change_base(10, 2) == "1010"


def test_change_base_base_greater_than_ten():
    # Digits are emitted via str(x % base), i.e. as plain decimal numbers,
    # so base 16 yields "1515" for 255 (15 then 15), not "ff".
    assert change_base(255, 16) == "1515"


def test_change_base_single_iteration():
    # x < base: exactly one pass through the loop body.
    assert change_base(5, 8) == "5"


def test_change_base_decimal():
    assert change_base(1234, 10) == "1234"


def test_change_base_zero_skips_loop():
    # x == 0: loop body never runs, empty string returned (lines 3, 4, 7 only).
    assert change_base(0, 2) == ""


def test_change_base_negative_skips_loop():
    # x < 0: loop condition false immediately, empty string returned.
    assert change_base(-7, 10) == ""


def test_change_base_base_two_exact_powers():
    assert change_base(8, 2) == "1000"
    assert change_base(1, 2) == "1"


def test_change_base_result_round_trips():
    # Postcondition: for bases <= 10 every digit is a single decimal
    # character, so int(result, base) reconstructs the original value.
    for x, base in [(0, 2), (1, 2), (42, 2), (999, 8), (777, 8), (1234, 10)]:
        result = change_base(x, base)
        assert isinstance(result, str)
        if x > 0:
            assert int(result, base) == x
        else:
            assert result == ""

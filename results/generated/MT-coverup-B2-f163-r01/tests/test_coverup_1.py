# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

"""Tests for f163.generate_integers.

The function is pure (no I/O, no global state, no monkeypatching targets),
so no cleanup is required; each test is self-contained and leaves no state
behind.

Coverage plan:
- line 3 (lower = max(2, min(a, b))): both branches of max exercised
  (min(a, b) >= 2 and min(a, b) < 2).
- line 4 (upper = min(8, max(a, b))): both branches of min exercised
  (max(a, b) <= 8 and max(a, b) > 8).
- line 6 (list comprehension): both branches of the `i % 2 == 0` filter
  exercised, plus empty and non-empty ranges.
"""

from f163 import generate_integers


def test_basic_range_in_order():
    # lower = max(2, 2) = 2 (min(a, b) branch of max wins)
    # upper = min(8, 8) = 8 (max(a, b) branch of min wins)
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_arguments_reversed():
    # Swapping the arguments must not change the result.
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_lower_clamped_to_two():
    # min(a, b) == 1 < 2, so the constant 2 wins in max(2, ...).
    assert generate_integers(1, 5) == [2, 4]


def test_upper_clamped_to_eight_empty_result():
    # max(a, b) == 20 > 8, so the constant 8 wins in min(8, ...);
    # lower (10) > upper (8) yields an empty range.
    assert generate_integers(10, 20) == []


def test_odd_values_filtered_out():
    # range(3, 5) contains 3 (odd, filtered) and 4 (even, kept),
    # exercising the False branch of `i % 2 == 0`.
    assert generate_integers(3, 4) == [4]


def test_single_odd_value():
    # range(7, 8) contains only the odd value 7 -> empty result.
    assert generate_integers(7, 7) == []


def test_negative_values_both_clamps_active():
    # min(a, b) = -5 < 2 -> lower = 2; max(a, b) = -3 < 8 -> upper = -3;
    # empty range.
    assert generate_integers(-5, -3) == []

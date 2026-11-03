# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

"""Tests for f036.fizz_buzz.

fizz_buzz(n) returns the number of times the digit '7' appears in the
concatenation of the decimal representations of all integers i in
[0, n) that are divisible by 11 or by 13.

The function under test is pure (no I/O, no module-level state, no
side effects), so no monkeypatching or teardown is required; the tests
leave no state behind.
"""

from f036 import fizz_buzz


def test_n_zero_never_enters_either_loop():
    # Covers the function body with both `for` loops skipped:
    # `range(0)` is empty and the resulting string is empty.
    assert fizz_buzz(0) == 0


def test_only_multiple_is_zero():
    # n == 1: the loop body runs once with i == 0, which satisfies the
    # first operand `i % 11 == 0` of the `or`, so 0 is appended.  The
    # character loop then runs over "0" without finding a '7'.
    assert fizz_buzz(1) == 0


def test_condition_false_branch():
    # i == 1 satisfies neither `i % 11 == 0` nor `i % 13 == 0`,
    # exercising the False branch of the divisibility condition.
    assert fizz_buzz(2) == 0


def test_divisible_by_11_only_short_circuits_or():
    # i == 11: first operand of the `or` is True, so the second
    # operand is never evaluated (short-circuit branch).
    assert fizz_buzz(12) == 0  # "011" contains no '7'


def test_divisible_by_13_only():
    # i == 13: first operand False, second operand True.
    assert fizz_buzz(14) == 0  # "013" contains no '7'


def test_counts_sevens_up_to_78():
    # Multiples of 11 or 13 below 78 concatenate to
    # "01113223339445255656677", which contains exactly two '7's
    # (both digits of 77).  Exercises the True branch of `c == '7'`.
    assert fizz_buzz(78) == 2


def test_counts_sevens_including_78():
    # 78 is divisible by 13 and contributes one more '7' -> 3 total.
    assert fizz_buzz(79) == 3


def test_reference_values():
    # Reference values for larger inputs (verified independently by
    # positional digit counting).
    assert fizz_buzz(50) == 0
    assert fizz_buzz(100) == 3
    assert fizz_buzz(200) == 6
    assert fizz_buzz(4000) == 192
    assert fizz_buzz(10000) == 639


def test_return_type_is_int():
    # Postcondition: the accumulated count is a plain int, not a bool.
    result = fizz_buzz(78)
    assert isinstance(result, int) and not isinstance(result, bool)

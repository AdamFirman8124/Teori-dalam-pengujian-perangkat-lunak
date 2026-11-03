# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

"""Tests for f036.fizz_buzz (counts digit '7' occurrences in integers < n
that are divisible by 11 or 13).

Covers every line (3-11) and every branch:
  * line 4 loop: entered (n > 0) and skipped (n == 0)
  * line 5 condition: i % 11 == 0 True (short-circuit), i % 11 != 0 but
    i % 13 == 0, and both False
  * line 6: append executed
  * line 9 loop: entered (non-empty string) and skipped (empty string)
  * line 10: c == '7' evaluating to True and to False
"""

from f036 import fizz_buzz


def test_fizz_buzz_zero_skips_both_loops():
    """n = 0: the range loop and the string loop are both never entered."""
    assert fizz_buzz(0) == 0


def test_fizz_buzz_single_zero():
    """n = 1: only i = 0 is seen (0 % 11 == 0 short-circuits the 'or');
    the resulting string '0' contains no '7', so c == '7' is False."""
    assert fizz_buzz(1) == 0


def test_fizz_buzz_thirteen_branch():
    """n = 14: i = 13 makes i % 11 != 0 but i % 13 == 0 (second arm of the
    'or'); ns == [0, 13] -> '013' has no '7'."""
    assert fizz_buzz(14) == 0


def test_fizz_buzz_no_sevens_below_50():
    """Multiples of 11 or 13 below 50 (0, 11, 13, 22, 26, 33, 39, 44)
    contain no digit 7; both False-branch of the condition and the
    False outcome of c == '7' are exercised."""
    assert fizz_buzz(50) == 0


def test_fizz_buzz_counts_sevens():
    """Below 78 the only 7s come from 77 (two of them); 78 (divisible by
    13) adds one more, so c == '7' evaluates True as well."""
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3


def test_fizz_buzz_result_type():
    """The result is always an int, even when nothing is counted."""
    result = fizz_buzz(12)  # multiples: 0, 11 -> '011' -> no '7'
    assert isinstance(result, int)
    assert result == 0

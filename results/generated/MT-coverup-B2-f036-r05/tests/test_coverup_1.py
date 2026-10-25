# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

import pytest

from f036 import fizz_buzz


def test_fizz_buzz_empty_ranges():
    # n <= 0 -> range is empty, no numbers collected, empty string
    assert fizz_buzz(0) == 0
    assert fizz_buzz(-5) == 0


def test_fizz_buzz_small_n_no_sevens():
    # range(1) -> [0]; range(11) -> [0]; range(12) -> [0, 11]; range(14) -> [0, 11, 13]
    assert fizz_buzz(1) == 0
    assert fizz_buzz(11) == 0
    assert fizz_buzz(12) == 0
    assert fizz_buzz(14) == 0


def test_fizz_buzz_multiple_of_11_branch():
    # 11 is divisible by 11 (first half of the `or` short-circuits)
    assert fizz_buzz(12) == 0
    # 22, 33, 44, 55, 66 are all multiples of 11 and contain no '7'
    assert fizz_buzz(67) == 0


def test_fizz_buzz_multiple_of_13_branch():
    # 13 is divisible by 13 only (second half of the `or` is evaluated)
    assert fizz_buzz(14) == 0
    # 13, 26, 39, 52, 65 contain no '7'
    assert fizz_buzz(66) == 0


def test_fizz_buzz_counts_sevens():
    # 77 is the first collected number containing a '7' (77 % 11 == 0) -> two sevens
    assert fizz_buzz(78) == 2
    # 77 excluded at n=77
    assert fizz_buzz(77) == 0
    # n=100 adds 78, 88, 91, 99; only 91 contains a '7' -> 2 + 1
    assert fizz_buzz(100) == 3


def test_fizz_buzz_return_type_and_purity():
    result = fizz_buzz(100)
    assert isinstance(result, int)
    assert not isinstance(result, bool)
    # calling twice must give the same answer (no hidden state)
    assert fizz_buzz(100) == result

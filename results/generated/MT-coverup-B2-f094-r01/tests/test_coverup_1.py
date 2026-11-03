# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

"""Tests for skjkasdkd in f094/__init__.py.

skjkasdkd(lst) returns the sum of the digits of the largest prime in lst
(note: the nested isPrime treats 0 and 1 as "prime" because its loop body
never runs for them). The function is pure and touches no global state,
so no monkeypatching/cleanup is needed; each test only calls it with
fresh literal lists, avoiding any state pollution.
"""

from f094 import skjkasdkd


def test_mixed_list_covers_prime_and_composite_paths():
    # 0 fails `lst[i] > maxx` (0 > 0), so isPrime is skipped for it.
    # 1, 2, 3: isPrime's loop body never runs -> returns True (line 8).
    # 4, 6, 8: divisor found on first check -> returns False (line 6).
    # 9: 9 % 2 != 0 but 9 % 3 == 0 -> False after several iterations.
    # 5 and 7 survive the loop -> True and update maxx (line 13).
    # Largest prime is 7, so the digit sum is 7.
    assert skjkasdkd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7


def test_no_primes_leaves_maxx_at_zero():
    # Every element is composite, so maxx never leaves 0 and the digit
    # sum of str(0) is 0. 25 forces several isPrime loop iterations
    # (25 % 2, 3, 4 all nonzero, then 25 % 5 == 0).
    assert skjkasdkd([4, 6, 8, 9, 10, 25]) == 0


def test_multi_digit_prime_digit_sum():
    # Largest prime is 13 -> 1 + 3 == 4. Also exercises isPrime on
    # multi-digit composites (10, 12, 14, 15) and primes (11, 13).
    assert skjkasdkd([10, 11, 12, 13, 14, 15]) == 4


def test_empty_list_skips_while_loop():
    # With an empty list the while-loop body never runs; maxx stays 0.
    assert skjkasdkd([]) == 0


def test_elements_not_greater_than_maxx_short_circuit():
    # After maxx becomes 7, every later element fails `lst[i] > maxx`,
    # so isPrime is never called for them (short-circuit branch of the
    # `and` on line 12).
    assert skjkasdkd([7, 5, 4, 3]) == 7


def test_larger_composite_after_max_prime():
    # 25 > 23 makes `lst[i] > maxx` True while isPrime(25) is False,
    # so maxx stays 23 and the result is 2 + 3 == 5.
    assert skjkasdkd([23, 25]) == 5

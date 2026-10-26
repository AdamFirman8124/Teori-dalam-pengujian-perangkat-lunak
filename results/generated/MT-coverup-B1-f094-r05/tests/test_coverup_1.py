# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

from f094 import skjkasdkd


def test_empty_list():
    assert skjkasdkd([]) == 0


def test_single_small_prime_empty_loop_range():
    # 2 and 3 exercise isPrime with empty range -> return True
    assert skjkasdkd([2]) == 2
    assert skjkasdkd([3]) == 3


def test_composites_only_return_false_branch():
    # 4 exercises isPrime inner if True -> return False on first iteration
    assert skjkasdkd([4]) == 0
    # 9 exercises inner if False then True (multiple loop iterations)
    assert skjkasdkd([9]) == 0
    # all composites, maxx stays 0
    assert skjkasdkd([4, 6, 8, 9, 15]) == 0


def test_primes_requiring_loop_iterations():
    # 5, 7 exercise inner if False for all iterations -> return True
    assert skjkasdkd([5]) == 5
    assert skjkasdkd([7]) == 7
    # 11 exercises loop with multiple False checks -> True
    assert skjkasdkd([11]) == 2
    # max prime tracking and digit sum
    assert skjkasdkd([2, 3, 5, 7]) == 7
    assert skjkasdkd([19]) == 10
    assert skjkasdkd([97]) == 16
    assert skjkasdkd([101]) == 2


def test_mixed_max_tracking_and_short_circuit():
    # covers lst[i] > maxx True + isPrime True -> update,
    # True + False -> no update, and False (<= maxx) short-circuit
    assert skjkasdkd([2, 4, 9, 11, 15]) == 2
    assert skjkasdkd([11, 5, 4]) == 2
    assert skjkasdkd([7, 7, 3, 2]) == 7
    assert skjkasdkd([0, 1, 2]) == 2


def test_descending_and_multi_digit_sum():
    assert skjkasdkd([2, 4, 9, 11, 15, 101]) == 2
    assert skjkasdkd([19, 5]) == 10

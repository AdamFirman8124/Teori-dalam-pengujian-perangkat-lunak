# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

from f075 import is_multiply_prime


def test_true_product_of_three_distinct_primes():
    """30 = 2 * 3 * 5, found immediately by the triple loop."""
    assert is_multiply_prime(30) is True


def test_true_product_with_repeated_prime():
    """8 = 2 * 2 * 2 exercises repetition of the same prime factor."""
    assert is_multiply_prime(8) is True


def test_true_requires_skipping_composite_candidates():
    """125 = 5 * 5 * 5.

    Reaching i == 5 forces the i-loop to step over the composite value 4
    (line 13 `continue`); reaching j == 5 forces the j-loop to step over
    composite j == 4 (line 15 `continue`); the k-loop steps over composite
    k values such as 4 (line 17 `continue`).
    """
    assert is_multiply_prime(125) is True


def test_true_first_factor_greater_than_two():
    """105 = 3 * 5 * 7.

    The i == 2 slice can never produce 105 (105 / 2 is not an integer),
    so the j- and k-loops are fully exhausted for i == 2 before the
    answer is found at i == 3.
    """
    assert is_multiply_prime(105) is True


def test_true_largest_representable_product():
    """97 is the largest prime below 100, so 97**3 = 912673 is the largest
    input that can still yield True; every smaller leading prime index is
    exhausted first."""
    assert is_multiply_prime(97 ** 3) is True


def test_false_below_smallest_possible_product():
    """The smallest product of three primes (each >= 2) is 2*2*2 = 8,
    so 2 can never match; the loops run to completion and line 19 executes."""
    assert is_multiply_prime(2) is False


def test_false_with_only_two_prime_factors():
    """10 = 2 * 5 has only two prime factors, so it is not a 'multiply prime'."""
    assert is_multiply_prime(10) is False


def test_false_full_loop_exhaustion():
    """10**6 exceeds the largest reachable product (97**3) and is not a
    product of three primes, so every loop is exhausted and `return False`
    on line 19 executes."""
    assert is_multiply_prime(10 ** 6) is False

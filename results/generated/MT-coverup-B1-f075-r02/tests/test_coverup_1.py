# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

from f075 import is_multiply_prime


def test_is_multiply_prime_returns_true_for_three_prime_factors():
    assert is_multiply_prime(2 * 3 * 5) is True


def test_is_multiply_prime_returns_false_when_no_prime_product_matches():
    assert is_multiply_prime(1) is False

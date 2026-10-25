# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

from f075 import is_multiply_prime


def test_is_multiply_prime_smallest_triple_product():
    assert is_multiply_prime(8) is True


def test_is_multiply_prime_repeated_prime():
    assert is_multiply_prime(27) is True


def test_is_multiply_prime_distinct_primes():
    assert is_multiply_prime(30) is True


def test_is_multiply_prime_mixed_repeated_and_distinct():
    assert is_multiply_prime(12) is True


def test_is_multiply_prime_not_triple_product():
    assert is_multiply_prime(1) is False


def test_is_multiply_prime_prime_number_is_false():
    assert is_multiply_prime(7) is False


def test_is_multiply_prime_product_of_two_primes_is_false():
    assert is_multiply_prime(6) is False

# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

from f075 import is_multiply_prime


def test_is_multiply_prime_basic_true():
    assert is_multiply_prime(30) is True


def test_is_multiply_prime_repeated_prime_true():
    assert is_multiply_prime(8) is True
    assert is_multiply_prime(12) is True
    assert is_multiply_prime(27) is True


def test_is_multiply_prime_larger_true():
    assert is_multiply_prime(2 * 3 * 97) is True
    assert is_multiply_prime(5 * 5 * 5) is True


def test_is_multiply_prime_false_small():
    assert is_multiply_prime(4) is False
    assert is_multiply_prime(6) is False
    assert is_multiply_prime(1) is False


def test_is_multiply_prime_false_prime_and_other():
    assert is_multiply_prime(7) is False
    assert is_multiply_prime(13) is False
    assert is_multiply_prime(2 * 3 * 5 + 1) is False


def test_is_multiply_prime_false_requires_full_search():
    assert is_multiply_prime(0) is False
    assert is_multiply_prime(999983) is False

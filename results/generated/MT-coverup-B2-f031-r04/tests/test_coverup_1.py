# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

from f031 import is_prime


def test_is_prime_rejects_numbers_below_two():
    assert is_prime(1) is False


def test_is_prime_rejects_composite_numbers():
    assert is_prime(4) is False


def test_is_prime_accepts_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(5) is True

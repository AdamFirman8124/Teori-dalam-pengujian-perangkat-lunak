# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

from f025 import factorize


def test_factorize_one_returns_empty():
    assert factorize(1) == []


def test_factorize_two_returns_two():
    assert factorize(2) == [2]


def test_factorize_prime():
    assert factorize(13) == [13]


def test_factorize_composite_with_repeated_factors():
    assert factorize(12) == [2, 2, 3]


def test_factorize_power_of_two_leaves_no_remainder():
    # ends with n == 1, so covers `if n > 1` False branch
    assert factorize(4) == [2, 2]


def test_factorize_square_of_odd_prime():
    assert factorize(49) == [7, 7]


def test_factorize_product_of_distinct_primes():
    assert factorize(60) == [2, 2, 3, 5]

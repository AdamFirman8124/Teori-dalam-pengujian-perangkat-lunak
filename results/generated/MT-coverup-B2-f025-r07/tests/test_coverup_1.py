# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

from f025 import factorize


def test_factorize_one_returns_empty():
    assert factorize(1) == []


def test_factorize_small_prime_two():
    assert factorize(2) == [2]


def test_factorize_prime():
    result = factorize(13)
    assert result == [13]


def test_factorize_composite_with_repeated_factors():
    result = factorize(12)
    assert result == [2, 2, 3]
    # postcondition: product of factors equals input
    prod = 1
    for f in result:
        prod *= f
    assert prod == 12


def test_factorize_composite_distinct_factors():
    result = factorize(60)
    assert result == [2, 2, 3, 5]
    prod = 1
    for f in result:
        prod *= f
    assert prod == 60

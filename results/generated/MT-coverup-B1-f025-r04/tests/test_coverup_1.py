# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

from f025 import factorize


def test_factorize_composite_with_repeated_factors():
    assert factorize(12) == [2, 2, 3]


def test_factorize_prime():
    assert factorize(13) == [13]


def test_factorize_small_composite_reduced_to_one():
    assert factorize(4) == [2, 2]


def test_factorize_one_returns_empty():
    assert factorize(1) == []


def test_factorize_zero_skips_loop():
    assert factorize(0) == []

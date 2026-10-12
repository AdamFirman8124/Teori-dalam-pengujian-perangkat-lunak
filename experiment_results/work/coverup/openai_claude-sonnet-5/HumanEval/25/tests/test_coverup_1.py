# file: script_25.py:4-27
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27], "branches": [[18, 19], [18, 25], [19, 20], [19, 23], [25, 26], [25, 27]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27], "branches": [[18, 19], [18, 25], [19, 20], [19, 23], [25, 26], [25, 27]]}

import pytest
from script_25 import factorize


def test_factorize_8():
    assert factorize(8) == [2, 2, 2]


def test_factorize_25():
    assert factorize(25) == [5, 5]


def test_factorize_70():
    assert factorize(2 * 5 * 7) == [2, 5, 7]


def test_factorize_prime_number():
    assert factorize(13) == [13]
    assert factorize(17) == [17]


def test_factorize_2():
    assert factorize(2) == [2]


def test_factorize_3():
    assert factorize(3) == [3]


def test_factorize_large_prime():
    assert factorize(97) == [97]


def test_factorize_composite_with_large_prime_factor():
    assert factorize(2 * 97) == [2, 97]
    assert factorize(6 * 97) == [2, 3, 97]


def test_factorize_product_equals_input():
    n = 100
    factors = factorize(n)
    product = 1
    for f in factors:
        product *= f
    assert product == n

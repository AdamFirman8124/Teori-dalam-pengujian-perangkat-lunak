# file: script_24.py:1-8
# asked: {"lines": [6, 7, 8], "branches": [[6, 0], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [6, 7, 8], "branches": [[6, 7], [7, 6], [7, 8]]}

import pytest
from script_24 import largest_divisor


def test_largest_divisor_15():
    assert largest_divisor(15) == 5


def test_largest_divisor_prime():
    assert largest_divisor(7) == 1


def test_largest_divisor_even():
    assert largest_divisor(10) == 5


def test_largest_divisor_large_prime():
    assert largest_divisor(13) == 1


def test_largest_divisor_composite():
    assert largest_divisor(20) == 10


def test_largest_divisor_perfect_square():
    assert largest_divisor(16) == 8

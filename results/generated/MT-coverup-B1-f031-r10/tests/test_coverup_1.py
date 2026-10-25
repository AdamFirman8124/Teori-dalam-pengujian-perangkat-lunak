# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


@pytest.mark.parametrize("n", [-10, -1, 0, 1])
def test_is_prime_below_two_returns_false(n):
    result = is_prime(n)
    assert result is False


@pytest.mark.parametrize("n", [4, 6, 9, 15, 25, 49, 100])
def test_is_prime_composite_returns_false(n):
    result = is_prime(n)
    assert result is False


@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 97])
def test_is_prime_prime_returns_true(n):
    result = is_prime(n)
    assert result is True


def test_is_prime_returns_bool_type():
    assert isinstance(is_prime(7), bool)
    assert isinstance(is_prime(8), bool)
    assert isinstance(is_prime(1), bool)

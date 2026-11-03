# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


@pytest.mark.parametrize("n", [0, 1, -1, -17])
def test_is_prime_numbers_below_two_are_not_prime(n):
    """Covers lines 3-4: the 'n < 2' branch and its early return."""
    assert is_prime(n) is False


@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 97])
def test_is_prime_prime_numbers_are_prime(n):
    """Covers lines 5 and 8: loop entry (including empty ranges for 2 and 3)
    and the final 'return True'."""
    assert is_prime(n) is True


@pytest.mark.parametrize("n", [4, 6, 9, 15, 25, 100])
def test_is_prime_composite_numbers_are_not_prime(n):
    """Covers lines 5-7: loop body, the divisibility check, and 'return False'."""
    assert is_prime(n) is False

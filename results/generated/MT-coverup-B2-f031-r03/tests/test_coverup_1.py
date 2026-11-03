# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


@pytest.mark.parametrize("n", [-100, -7, -1, 0, 1])
def test_is_prime_returns_false_for_n_below_two(n):
    # Covers lines 3-4: the `n < 2` branch taken.
    assert is_prime(n) is False


@pytest.mark.parametrize("n", [4, 6, 8, 9, 15, 21, 25, 100])
def test_is_prime_returns_false_for_composites(n):
    # Covers lines 5-7: loop entered and a divisor found (early return False).
    assert is_prime(n) is False


@pytest.mark.parametrize("n", [2, 3])
def test_is_prime_returns_true_when_loop_body_never_runs(n):
    # Covers line 8 via the branch where range(2, n - 1) is empty.
    assert is_prime(n) is True


@pytest.mark.parametrize("n", [5, 7, 11, 13, 17, 19, 23, 97])
def test_is_prime_returns_true_when_loop_completes(n):
    # Covers line 8 via the branch where the loop runs to exhaustion
    # without finding a divisor.
    assert is_prime(n) is True

# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins
import f059


def test_largest_prime_factor_small_prime():
    assert f059.largest_prime_factor(2) == 2


def test_largest_prime_factor_composite_divisor():
    # j=2 prime -> True/True, j=3 non-divisor -> False (short-circuit),
    # j=4 divisor but composite -> True/False covering is_prime False path
    assert f059.largest_prime_factor(4) == 2


def test_largest_prime_factor_with_looped_prime_check():
    # is_prime(5) iterates with k % i != 0 covering inner-if False branch
    # divisors 3 and 5 are prime, 15 is composite
    assert f059.largest_prime_factor(15) == 5
    assert f059.largest_prime_factor(5) == 5


def test_largest_prime_factor_no_iteration():
    # range(2, n+1) empty so outer loop body never runs
    assert f059.largest_prime_factor(1) == 1
    assert f059.largest_prime_factor(0) == 1
    assert f059.largest_prime_factor(-5) == 1


def test_largest_prime_factor_k_less_than_two(monkeypatch):
    orig_range = builtins.range

    def fake_range(*args, **kwargs):
        # Only remap the outer loop range(2, 6) to include j=1,
        # leaving inner is_prime ranges untouched.
        if tuple(args) == (2, 6) and not kwargs:
            return orig_range(1, 6)
        return orig_range(*args, **kwargs)

    monkeypatch.setattr(builtins, "range", fake_range)
    # j=1 gives n % j == 0 True then is_prime(1) covers k < 2 -> return False;
    # remaining j values behave normally so result is unchanged.
    assert f059.largest_prime_factor(5) == 5

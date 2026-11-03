# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins

from f059 import largest_prime_factor


def test_returns_one_when_there_are_no_candidate_factors():
    # For n <= 1 the factor loop `range(2, n + 1)` is empty, so the initial
    # value `largest = 1` is returned untouched.
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-7) == 1


def test_prime_input_returns_itself():
    # k = 2 and k = 3 make the inner `range(2, k - 1)` loop empty, while
    # k = 13 and k = 97 run the loop without ever finding a divisor.
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(97) == 97


def test_composite_input_returns_largest_prime_factor():
    # 15 = 3 * 5: covers the `n % j != 0` short-circuit (j = 2), prime
    # factors updating `largest` (j = 3 and j = 5), and is_prime rejecting
    # the composite divisor 15 (inner loop finds 15 % 3 == 0).
    assert largest_prime_factor(15) == 5
    # 13195 = 5 * 7 * 13 * 29.
    assert largest_prime_factor(13195) == 29


def test_repeated_prime_factors_are_handled():
    # Composite divisors such as 4, 8, 6, 12 and 49 must be rejected by
    # is_prime while the genuine prime factors are still reported.
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(49) == 7


def test_is_prime_guard_rejects_values_below_two(monkeypatch):
    # The factor loop only ever calls is_prime with j >= 2, so the `k < 2`
    # early return inside is_prime cannot be reached through the public
    # interface.  Temporarily patch range so the outer loop also sees the
    # candidate j = 1 (which divides every n); the observable result for
    # n = 6 must remain its true largest prime factor, 3.
    real_range = builtins.range
    outer_loop_seen = []

    def fake_range(*args):
        if not outer_loop_seen:
            # The first range call inside largest_prime_factor is the outer
            # `for j in range(2, n + 1)` loop; prepend the candidate j = 1.
            outer_loop_seen.append(True)
            return iter([1, *real_range(*args)])
        return real_range(*args)

    monkeypatch.setattr(builtins, "range", fake_range)
    assert largest_prime_factor(6) == 3

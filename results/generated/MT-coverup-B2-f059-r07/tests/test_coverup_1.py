# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins

from f059 import largest_prime_factor


def test_prime_input_returns_itself():
    # Exercises the nested def, is_prime(13) scanning every candidate divisor
    # without finding one (inner loop + `return True`), the outer loop and
    # the final return statement.
    assert largest_prime_factor(13) == 13


def test_composite_inputs():
    # Exercises the outer loop over several js, the `n % j == 0 and ...`
    # short-circuit (False for non-divisors such as j=6), primality of
    # divisors, and the `largest = max(largest, j)` update.
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(13195) == 29


def test_power_of_two():
    # 8 -> only prime factor is 2. is_prime(4) and is_prime(8) hit the
    # "divisor found" early `return False` inside is_prime.
    assert largest_prime_factor(8) == 2


def test_smallest_prime():
    # is_prime(2): range(2, 1) is empty, so the inner loop body never runs
    # and `return True` is reached immediately.
    assert largest_prime_factor(2) == 2


def test_no_candidate_factors():
    # n <= 1: range(2, n + 1) is empty, the loop body never executes and
    # the initial `largest = 1` is returned.
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1


def test_is_prime_lower_bound_branch(monkeypatch):
    # `is_prime` is only ever invoked with j >= 2 by the outer loop, so the
    # `k < 2` early return is unreachable through the public API. Temporarily
    # patch builtins.range (the function resolves `range` via builtins at
    # call time) so the very first range call -- the outer loop's
    # range(2, n + 1) -- also yields 1. Then 15 % 1 == 0 makes the function
    # call is_prime(1), which takes the `k < 2` branch. Every later range
    # call (including is_prime's inner loop) is delegated unchanged to the
    # real range, and monkeypatch restores builtins.range afterwards.
    real_range = builtins.range
    state = {"outer_patched": False}

    def fake_range(*args, **kwargs):
        if not state["outer_patched"] and len(args) == 2:
            state["outer_patched"] = True
            return real_range(1, args[1])
        return real_range(*args, **kwargs)

    monkeypatch.setattr(builtins, "range", fake_range)

    # j=1: 15 % 1 == 0 -> is_prime(1) -> k < 2 -> False (branch taken);
    # the remaining candidates are evaluated exactly as before, so the
    # observable result is unchanged.
    assert largest_prime_factor(15) == 5

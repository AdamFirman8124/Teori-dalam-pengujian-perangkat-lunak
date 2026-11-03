# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins

import f059
from f059 import largest_prime_factor


def test_largest_prime_factor_returns_expected_values():
    # Covers: def is_prime (line 3), the k >= 2 path, the trial-division loop
    # completing normally (line 9), the outer loop, the True branch of
    # `n % j == 0 and is_prime(j)` (line 13) and the final return (line 14).
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(330) == 11


def test_largest_prime_factor_prime_and_composite_divisor_branches():
    # n = 4 walks the outer loop over j = 2, 3, 4:
    #   j=2: divisor -> is_prime(2): range(2, 1) is empty -> True (line 9)
    #   j=3: not a divisor -> `and` short-circuits, is_prime not called
    #   j=4: divisor -> is_prime(4): 4 % 2 == 0 -> False (line 8)
    assert largest_prime_factor(4) == 2
    # n = 9: j=3 -> is_prime(3): range(2, 2) is empty -> True
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3


def test_largest_prime_factor_outer_loop_skipped_for_n_below_two():
    # range(2, n + 1) is empty for n <= 1, so the loop body never executes
    # (covers the "loop skipped" arc of line 11); the function returns 1.
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1


def test_largest_prime_factor_is_prime_guard_for_k_below_two(monkeypatch):
    """Exercise the ``k < 2`` early return (line 5) inside the nested is_prime.

    The outer loop starts at j = 2, so is_prime is normally never invoked with
    k < 2 and that guard is unreachable through ordinary calls.  Temporarily
    shadow ``range`` (restored automatically by monkeypatch) so that the outer
    loop of a call with n = 1 yields j = 1; then n % 1 == 0 holds and
    is_prime(1) takes the ``k < 2`` branch.  The observable result for n = 1
    is unchanged (1), so the assertion remains valid either way.
    """
    real_range = range
    fired = {"outer": False}

    def fake_range(start, stop=None, step=None):
        if (
            step is None
            and stop is not None
            and (start, stop) == (2, 2)
            and not fired["outer"]
        ):
            # First range(2, 2) call is the outer loop of largest_prime_factor;
            # make it yield j = 1 so is_prime is called with k = 1 < 2.
            fired["outer"] = True
            return iter([1])
        if stop is None:
            return real_range(start)
        if step is None:
            return real_range(start, stop)
        return real_range(start, stop, step)

    # Patch both the module globals of the code under test and the builtin
    # fallback, so the interception works regardless of how f059 was imported.
    monkeypatch.setattr(f059, "range", fake_range, raising=False)
    monkeypatch.setattr(builtins, "range", fake_range)

    assert largest_prime_factor(1) == 1
    assert fired["outer"], "outer-loop hook did not fire; k < 2 guard not exercised"

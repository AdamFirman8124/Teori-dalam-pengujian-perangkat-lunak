# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059


def test_largest_prime_factor_basic_composite():
    # 13195 = 5 * 7 * 13 * 29
    assert f059.largest_prime_factor(13195) == 29
    assert f059.largest_prime_factor(15) == 5
    assert f059.largest_prime_factor(21) == 7


def test_largest_prime_factor_prime_inputs():
    # For prime n most j values do not divide n, exercising the
    # short-circuit of `n % j == 0 and is_prime(j)`; j == n is prime.
    assert f059.largest_prime_factor(2) == 2
    assert f059.largest_prime_factor(3) == 3
    assert f059.largest_prime_factor(11) == 11


def test_largest_prime_factor_composite_divisor_rejected():
    # Composite divisors of n make is_prime's inner loop hit its
    # early `return False` (e.g. is_prime(4), is_prime(6), is_prime(100)).
    assert f059.largest_prime_factor(4) == 2
    assert f059.largest_prime_factor(12) == 3
    assert f059.largest_prime_factor(100) == 5


def test_largest_prime_factor_loop_never_runs():
    # For n < 2 the for-loop body never executes and 1 is returned.
    assert f059.largest_prime_factor(1) == 1
    assert f059.largest_prime_factor(0) == 1
    assert f059.largest_prime_factor(-7) == 1


def test_is_prime_guard_k_below_two(monkeypatch):
    # is_prime is only ever fed j >= 2 by the public API, so its `k < 2`
    # guard is unreachable through normal calls.  Shadow `range` in the
    # module's namespace for this single call so the loop also sees
    # j = 1 (the monkeypatch fixture restores the module afterwards).
    real_range = range
    n = 6

    def fake_range(start, stop=None, step=None):
        if step is not None:
            return real_range(start, stop, step)
        if stop is None:
            return real_range(start)
        if start == 2 and stop == n + 1:
            # Prepend 1 so the loop also evaluates is_prime(1).
            return [1, *real_range(start, stop)]
        return real_range(start, stop)

    monkeypatch.setattr(f059, "range", fake_range, raising=False)
    # j = 1 divides 6 but is_prime(1) is False; largest prime factor is 3.
    assert f059.largest_prime_factor(n) == 3

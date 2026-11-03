# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f122.add_elements.

The function under test is pure (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; each test works only on local data, which
guarantees no state pollution between tests.

Coverage goals:
  * Execute line 3 (the function body) by calling add_elements.
  * Cover both branches of the generator's ``if len(str(elem)) <= 2``
    condition (elements kept and elements filtered out).
  * Cover the generator loop entering, yielding, and exhausting.
  * Cover edge cases: empty array, k == 0, k > len(arr), all elements
    filtered out, and negative numbers.
"""

import pytest

from f122 import add_elements


def test_add_elements_mixed_lengths_covers_both_if_branches():
    # Elements with len(str(elem)) <= 2 are summed; longer ones are skipped.
    # This exercises both the True and False branches of the filter, the
    # generator's yield, and normal loop exhaustion.
    arr = [1, 22, 333, 4, 5555, 6]
    assert add_elements(arr, len(arr)) == 1 + 22 + 4 + 6


def test_add_elements_k_limits_slice():
    # Only the first k elements are considered; the element at index k
    # (which would pass the filter) must be excluded.
    arr = [1, 22, 333, 4]
    assert add_elements(arr, 2) == 1 + 22


def test_add_elements_all_elements_filtered_out():
    # Every element fails the filter, so the generator yields nothing and
    # sum() returns 0 (covers loop exit with zero yields).
    assert add_elements([100, 2000, 30000], 3) == 0


def test_add_elements_empty_array():
    # arr[:k] is empty: the generator loop exits immediately.
    assert add_elements([], 5) == 0


def test_add_elements_k_zero():
    # k == 0 produces an empty slice regardless of contents.
    assert add_elements([1, 22, 333], 0) == 0


def test_add_elements_k_larger_than_array():
    # Slicing beyond the end of arr is safe and uses the whole array.
    assert add_elements([7, 88], 10) == 7 + 88


def test_add_elements_negative_numbers():
    # str(-5) has length 2 (kept); str(-100) has length 4 (filtered).
    assert add_elements([-5, -100, -7], 3) == -5 + -7


def test_add_elements_returns_int_sum():
    # Postcondition: the result is the integer sum of the kept elements.
    result = add_elements([10, 20, 300], 3)
    assert isinstance(result, int)
    assert result == 30


if __name__ == "__main__":  # pragma: no cover - never executed by pytest
    raise SystemExit(pytest.main([__file__]))

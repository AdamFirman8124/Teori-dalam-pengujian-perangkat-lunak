# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


def test_fib4_base_cases():
    """Covers lines 3-5: initialization and the n < 4 early-return branch."""
    # fib4 is a pure function (no global state, no I/O), so no cleanup is needed.
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_recursive_cases():
    """Covers lines 7-11: the loop branch and the final return."""
    # Each term is the sum of the previous four terms.
    # Sequence: 0, 0, 2, 0, 2, 4, 8, 14, ...
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    # Cross-check a larger value computed independently:
    # fib4(8) = 14 + 8 + 4 + 2 = 28
    assert fib4(8) == 28


def test_fib4_matches_quadruple_fibonacci_recurrence():
    """Property check: fib4(n) equals the sum of the four preceding terms."""
    values = [fib4(i) for i in range(4, 12)]
    for i in range(4, len(values)):
        assert values[i] == values[i - 1] + values[i - 2] + values[i - 3] + values[i - 4]

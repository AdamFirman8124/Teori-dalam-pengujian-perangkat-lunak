# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

"""Tests for f106.f — covering lines 3-13 (both loop branches).

f(n) builds a list where, for each i in 1..n:
  - even i  -> factorial(i)      (lines 5-8, the `if` branch)
  - odd  i  -> sum(1..i)         (lines 10-12, the `else` branch)

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required to avoid state pollution.
"""

from f106 import f


def test_f_zero_executes_loop_setup_and_return():
    """n=0: covers lines 3 (ret = []), 4 (loop header) and 13 (return)."""
    assert f(0) == []


def test_f_odd_branch():
    """Odd i exercises the else branch (lines 10-12): triangular numbers."""
    assert f(1) == [1]          # 1
    assert f(3) == [1, 2, 6]    # 1, 2!, 1+2+3


def test_f_even_branch():
    """Even i exercises the if branch (lines 5-8): factorials."""
    assert f(2) == [1, 2]       # 1, 2!
    assert f(4) == [1, 2, 6, 24]  # 1, 2!, 3, 4!


def test_f_mixed_branches_full_coverage():
    """A single call with both parities covers every line 3-13."""
    result = f(5)
    assert result == [1, 2, 6, 24, 15]
    # Postconditions: correct length and per-element parity semantics.
    assert len(result) == 5
    assert result[1] == 2 and result[3] == 24          # even -> factorial
    assert result[0] == 1 and result[2] == 6 and result[4] == 15  # odd -> sum

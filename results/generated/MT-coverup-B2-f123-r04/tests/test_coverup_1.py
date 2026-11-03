# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

"""Tests for f123.get_odd_collatz covering all previously unexecuted lines (3-16)
and both branches of every conditional.

Branch coverage map:
  - line 3 True  (even n)  -> test_get_odd_collatz_even_input
  - line 3 False (odd n)   -> test_get_odd_collatz_odd_input, test_get_odd_collatz_one
  - line 4                 -> test_get_odd_collatz_even_input
  - line 6                 -> test_get_odd_collatz_odd_input, test_get_odd_collatz_one
  - line 7 True            -> test_get_odd_collatz_even_input, test_get_odd_collatz_odd_input
  - line 7 False (n == 1)  -> test_get_odd_collatz_one
  - line 8 True  (even n)  -> test_get_odd_collatz_even_input
  - line 8 False (odd n)   -> test_get_odd_collatz_odd_input
  - line 9                 -> test_get_odd_collatz_even_input
  - line 11                -> test_get_odd_collatz_odd_input
  - line 13 True           -> test_get_odd_collatz_even_input, test_get_odd_collatz_odd_input
  - line 13 False          -> test_get_odd_collatz_even_input, test_get_odd_collatz_odd_input
  - line 14                -> test_get_odd_collatz_even_input, test_get_odd_collatz_odd_input
  - line 16                -> all tests
"""

from f123 import get_odd_collatz


def test_get_odd_collatz_odd_input():
    """Odd starting value: seeds the list with n, applies the 3n+1 step (line 11),
    skips appending even intermediate values (line 13 False), appends odd ones
    (line 14), and returns the sorted odd numbers."""
    # Collatz sequence for 5: 5, 16, 8, 4, 2, 1 -> odd values {5, 1}
    result = get_odd_collatz(5)
    assert result == [1, 5]
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)


def test_get_odd_collatz_even_input():
    """Even starting value: starts with an empty list (line 4), halves n (line 9),
    appends odd intermediate values (lines 13-14), and returns them sorted."""
    # Collatz sequence for 6: 6, 3, 10, 5, 16, 8, 4, 2, 1 -> odd values {3, 5, 1}
    result = get_odd_collatz(6)
    assert result == [1, 3, 5]
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    # The even starting value itself must never appear in the result.
    assert 6 not in result


def test_get_odd_collatz_one():
    """n == 1 takes the odd branch (line 6) but never enters the while loop
    (line 7 False), so the result is just [1]."""
    assert get_odd_collatz(1) == [1]

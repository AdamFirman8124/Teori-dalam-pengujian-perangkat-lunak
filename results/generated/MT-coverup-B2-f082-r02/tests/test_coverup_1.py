# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    """Length 0 is not prime: covers lines 3-5 via the l == 0 branch."""
    assert prime_length("") is False


def test_prime_length_single_char():
    """Length 1 is not prime: covers lines 3-5 via the l == 1 branch."""
    assert prime_length("a") is False


def test_prime_length_composite():
    """Composite lengths enter the loop and return early: covers lines 6-8."""
    # length 4: range(2, 4) yields i=2, 4 % 2 == 0 -> return False
    assert prime_length("abcd") is False
    # length 6: range(2, 6) yields i=2, 6 % 2 == 0 -> return False
    assert prime_length("abcdef") is False
    # length 9: 9 % 2 != 0 but 9 % 3 == 0 -> return False (exercises loop continuation)
    assert prime_length("abcdefghi") is False


def test_prime_length_prime():
    """Prime lengths skip the early returns and reach the final return: covers line 9."""
    # length 2: range(2, 2) is empty, loop body never runs
    assert prime_length("ab") is True
    # length 3: i=2, 3 % 2 != 0, loop ends
    assert prime_length("abc") is True
    # length 5: i=2,3,4 all fail the divisibility check
    assert prime_length("abcde") is True
    # length 7: i=2..6 all fail the divisibility check
    assert prime_length("abcdefg") is True

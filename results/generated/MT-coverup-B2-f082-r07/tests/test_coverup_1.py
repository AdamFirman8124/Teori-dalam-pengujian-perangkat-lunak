# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string_returns_false():
    """Covers lines 3-5 with l == 0 (first branch of the condition)."""
    assert prime_length("") is False


def test_prime_length_single_char_returns_false():
    """Covers lines 3-5 with l == 1 (second branch of the condition)."""
    assert prime_length("a") is False


def test_prime_length_two_is_prime():
    """Covers lines 3, 4 (False branch), 6 and 9; loop body never runs for l == 2."""
    assert prime_length("ab") is True


def test_prime_length_three_is_prime():
    """Covers lines 3, 4 (False branch), 6, 7 (False branch) and 9."""
    assert prime_length("abc") is True


def test_prime_length_seven_is_prime():
    """Covers lines 3, 4 (False branch), 6, 7 (False branch) and 9 with a longer prime length."""
    assert prime_length("abcdefg") is True


def test_prime_length_four_is_composite():
    """Covers lines 3, 4 (False branch), 6, 7 (True branch) and 8."""
    assert prime_length("abcd") is False


def test_prime_length_nine_is_composite():
    """Covers lines 3, 4 (False branch), 6, 7 (True branch) and 8 for a larger composite length."""
    assert prime_length("a" * 9) is False


def test_prime_length_six_is_composite():
    """Covers lines 3, 4 (False branch), 6, 7 (True branch) and 8 for another composite length."""
    assert prime_length("abcdef") is False

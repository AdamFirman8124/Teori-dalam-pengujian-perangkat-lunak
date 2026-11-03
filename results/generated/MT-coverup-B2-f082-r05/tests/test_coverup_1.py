# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

"""Tests for f082.prime_length.

Covers all previously uncovered lines (3-9) and every branch:

- line 3: executed by every test (len computation)
- line 4: both sides of ``l == 0 or l == 1``
    * ``l == 0`` True  -> empty string
    * ``l == 1`` True  -> single-character string
    * both False       -> longer strings
- line 5: early ``return False`` for lengths 0 and 1
- line 6: loop entered (length >= 3) and loop skipped entirely
          (length 2 -> ``range(2, 2)`` is empty)
- line 7: both outcomes of ``l % i == 0``
    * True  -> composite lengths (4, 6, 9)
    * False -> prime lengths (3, 5, 7)
- line 8: ``return False`` from inside the loop
- line 9: ``return True`` after the loop finishes

prime_length is a pure function (no I/O, no globals, no mutable state),
so no monkeypatching or teardown is required; there is no state to
pollute.
"""

import pytest

from f082 import prime_length


def test_prime_length_empty_string_returns_false():
    """Length 0 hits the ``l == 0`` short-circuit and returns False."""
    assert prime_length("") is False


def test_prime_length_single_character_returns_false():
    """Length 1 hits the ``l == 1`` operand and returns False."""
    assert prime_length("x") is False


def test_prime_length_two_characters_returns_true():
    """Length 2: the for-loop range is empty, so line 9 is reached."""
    assert prime_length("ab") is True


@pytest.mark.parametrize("s", ["abc", "abcde", "abcdefg"])
def test_prime_length_prime_lengths_return_true(s):
    """Lengths 3, 5, 7: loop runs, no divisor found, returns True."""
    assert prime_length(s) is True


@pytest.mark.parametrize(
    "s", ["abcd", "abcdef", "a" * 9, "a" * 12]
)
def test_prime_length_composite_lengths_return_false(s):
    """Lengths 4, 6, 9, 12: a divisor is found and False is returned."""
    assert prime_length(s) is False

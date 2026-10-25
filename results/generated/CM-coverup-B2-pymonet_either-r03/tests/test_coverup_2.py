# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

import pytest

from pymonet.either import Either, Left, Right


def test_eq_same_right_values():
    """Lines 18-20: equal Rights compare equal."""
    assert Right(42) == Right(42)


def test_eq_same_left_values():
    """Lines 18-20: equal Lefts compare equal."""
    assert Left("err") == Left("err")


def test_eq_not_an_either():
    """Line 18 short-circuits: non-Either operand is not equal."""
    assert Right(42) != 42
    assert Left("err") != "err"
    assert Right(42) != None  # noqa: E711


def test_eq_different_values():
    """Line 19 short-circuits: same side, different values are not equal."""
    assert Right(42) != Right(43)
    assert Left("err") != Left("other")


def test_eq_different_sides_same_value():
    """Line 20: same value but different sides are not equal."""
    assert Right(42) != Left(42)


def test_eq_against_subclass_instance():
    """Line 18: any Either subclass instance passes the isinstance check."""
    class CustomEither(Either):
        def is_right(self):
            return True

    assert Right(1) == CustomEither(1)
    assert CustomEither(1) == Right(1)

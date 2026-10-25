# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

import pytest

from pymonet.either import Either, Left, Right


def test_eq_non_either_returns_false():
    """Line 18 short-circuits to False when other is not an Either."""
    left = Left(1)
    assert (left == 1) is False
    assert (left == "not an either") is False
    assert (left is not None) is True


def test_eq_different_values_returns_false():
    """Line 19 short-circuits to False when values differ."""
    left1 = Left(1)
    left2 = Left(2)
    right1 = Right(1)
    right2 = Right(2)

    assert (left1 == left2) is False
    assert (right1 == right2) is False
    assert (left1 == right2) is False


def test_eq_same_value_different_sides_returns_false():
    """Line 20 short-circuits to False when is_right() differs."""
    left = Left(1)
    right = Right(1)

    assert (left == right) is False
    assert (right == left) is False


def test_eq_same_value_same_side_returns_true():
    """All three lines execute and evaluate to True."""
    left1 = Left(1)
    left2 = Left(1)
    right1 = Right(1)
    right2 = Right(1)

    assert (left1 == left2) is True
    assert (right1 == right2) is True


def test_eq_is_symmetric():
    """__eq__ is symmetric for both matching and non-matching eithers."""
    assert (Left(5) == Left(5)) == (Left(5) == Left(5))
    assert (Left(5) == Right(5)) == (Right(5) == Left(5))
    assert (Right(5) == Right(5)) == (Right(5) == Right(5))

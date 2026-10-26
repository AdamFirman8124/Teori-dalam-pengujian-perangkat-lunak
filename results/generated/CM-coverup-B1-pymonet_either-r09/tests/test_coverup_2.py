# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_eq_with_non_either_returns_false():
    """Line 18: isinstance check fails, short-circuits to False."""
    left = Left(42)
    assert (left == 42) is False
    assert (left == "not an either") is False
    assert (Right(42) == None) is False


def test_eq_with_equal_values_and_same_side():
    """Lines 18-20 all execute and evaluate to True."""
    assert (Left(42) == Left(42)) is True
    assert (Right(42) == Right(42)) is True


def test_eq_with_different_values():
    """Lines 18-19-20: value comparison fails on line 19."""
    assert (Left(1) == Left(2)) is False
    assert (Right(1) == Right(2)) is False


def test_eq_with_same_value_but_different_side():
    """Lines 18-19-20: is_right comparison fails on line 20."""
    assert (Left(42) == Right(42)) is False
    assert (Right(42) == Left(42)) is False


def test_eq_is_symmetric():
    """__eq__ works from both operands' perspectives."""
    assert (Left(7) == Left(7)) is True
    assert (Left(7) == Right(7)) is False
    assert (Right(7) == Left(7)) is False
    assert (Right(7) == Right(7)) is True

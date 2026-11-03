# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

import pytest

from pymonet.either import Either, Left, Right


def test_eq_left_with_equal_left_is_true():
    """Left(1) == Left(1): isinstance, value and is_right all match -> True.

    Exercises the full True path through lines 18-20.
    """
    result = Left(1).__eq__(Left(1))
    assert result is True
    assert Left(1) == Left(1)


def test_eq_left_with_non_either_is_false():
    """Left(1) == <non-Either>: isinstance check fails -> False.

    Exercises the False branch of the isinstance check on line 18.
    """
    assert Left(1).__eq__(1) is False
    assert Left(1).__eq__(None) is False
    assert (Left(1) == 1) is False


def test_eq_left_with_left_of_different_value_is_false():
    """Left(1) == Left(2): values differ -> False.

    Exercises the False branch of the value comparison on line 19.
    """
    assert Left(1).__eq__(Left(2)) is False
    assert (Left(1) == Left(2)) is False


def test_eq_left_with_right_of_same_value_is_false():
    """Left(1) == Right(1): values equal but is_right differs -> False.

    Exercises the False branch of the is_right comparison on line 20.
    """
    assert Left(1).__eq__(Right(1)) is False
    assert (Left(1) == Right(1)) is False


def test_eq_right_with_equal_right_is_true():
    """Right(1) == Right(1): all conditions hold -> True.

    Exercises the full True path through lines 18-20 for the Right subclass.
    """
    result = Right(1).__eq__(Right(1))
    assert result is True
    assert Right(1) == Right(1)


def test_eq_right_with_right_of_different_value_is_false():
    """Right(1) == Right(2): values differ -> False."""
    assert Right(1).__eq__(Right(2)) is False
    assert (Right(1) == Right(2)) is False


def test_eq_right_with_left_of_same_value_is_false():
    """Right(1) == Left(1): values equal but is_right differs -> False."""
    assert Right(1).__eq__(Left(1)) is False
    assert (Right(1) == Left(1)) is False


def test_eq_right_with_non_either_is_false():
    """Right(1) == <non-Either>: isinstance check fails -> False."""
    assert Right(1).__eq__('not an either') is False
    assert (Right(1) == 'not an either') is False

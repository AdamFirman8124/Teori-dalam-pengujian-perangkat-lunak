# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

from pymonet.either import Left, Right


def test_either_is_not_equal_to_unrelated_object():
    assert not (Right(1) == object())


def test_eithers_with_different_values_are_not_equal():
    assert not (Right(1) == Right(2))


def test_left_and_right_with_same_value_are_not_equal():
    assert not (Left(1) == Right(1))
    assert not (Right(1) == Left(1))


def test_eithers_with_same_value_and_side_are_equal():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)

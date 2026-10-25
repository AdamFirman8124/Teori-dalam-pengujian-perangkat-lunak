# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

from pymonet.either import Left, Right


def test_either_equality_with_non_either() -> None:
    assert (Right(1) == object()) is False


def test_either_equality_with_different_values() -> None:
    assert (Right(1) == Right(2)) is False


def test_either_equality_with_same_value_but_different_sides() -> None:
    assert (Right(1) == Left(1)) is False
    assert (Left(1) == Right(1)) is False


def test_either_equality_with_same_value_and_side() -> None:
    assert (Right(1) == Right(1)) is True
    assert (Left(1) == Left(1)) is True

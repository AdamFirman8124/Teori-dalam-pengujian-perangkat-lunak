# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

from pymonet.either import Left, Right


def test_either_equality_rejects_non_either():
    assert Left(1).__eq__(object()) is False


def test_either_equality_rejects_different_values():
    assert Left(1).__eq__(Left(2)) is False


def test_either_equality_rejects_different_sides():
    assert Left(1).__eq__(Right(1)) is False


def test_either_equality_accepts_same_value_and_side():
    assert Left(1).__eq__(Left(1)) is True
    assert Right(1).__eq__(Right(1)) is True

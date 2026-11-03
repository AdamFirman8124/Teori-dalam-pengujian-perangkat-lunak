# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

"""Tests for pymonet.either.Either.__eq__ (lines 18-20).

These tests are pure (no global state is created or mutated), so no
monkeypatching/teardown is required; each test only constructs local
Either/Left/Right instances and asserts on the boolean result of __eq__.
"""

from pymonet.either import Either, Left, Right


def test_eq_same_lefts_is_true():
    """Left(1) == Left(1): isinstance ok, values equal, is_right() equal
    (lines 18-20 all execute and every condition is True)."""
    assert Left(1) == Left(1)
    assert Left(1).__eq__(Left(1)) is True


def test_eq_same_rights_is_true():
    """Right(1) == Right(1): isinstance ok, values equal, is_right() equal
    (lines 18-20 all execute and every condition is True)."""
    assert Right(1) == Right(1)
    assert Right(1).__eq__(Right(1)) is True


def test_eq_against_non_either_is_false():
    """__eq__ short-circuits on the isinstance check when other is not an
    Either instance (line 18, False branch)."""
    assert (Left(1) == 1) is False
    assert (Right("a") == "a") is False
    assert Left(1).__eq__(object()) is False
    assert Left(1).__eq__(None) is False


def test_eq_different_values_is_false():
    """__eq__ returns False when both are Eithers but values differ
    (line 19, False branch)."""
    assert (Left(1) == Left(2)) is False
    assert (Right(1) == Right(2)) is False


def test_eq_same_value_opposite_sides_is_false():
    """__eq__ returns False for a Left and a Right holding equal values,
    because is_right() differs (line 20, False branch)."""
    assert (Left(1) == Right(1)) is False
    assert (Right(1) == Left(1)) is False


def test_eq_base_either_instances():
    """Plain Either instances compare by value and is_right() result."""
    assert Either(1) == Either(1)
    assert (Either(1) == Either(2)) is False
    assert (Either(1) == 1) is False

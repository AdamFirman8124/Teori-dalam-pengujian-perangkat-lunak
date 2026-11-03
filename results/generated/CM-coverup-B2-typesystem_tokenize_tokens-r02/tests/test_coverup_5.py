# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

import typing

import pytest

from typesystem.tokenize.tokens import ScalarToken, Token


def test_eq_against_non_token_is_false():
    """
    Covers line 67: the isinstance(other, Token) guard short-circuits
    to False when comparing a Token against a non-Token object.
    """
    token = ScalarToken("a", 0, 1)

    assert (token == "a") is False
    assert (token == 42) is False
    assert (token == None) is False
    assert (token == object()) is False
    # Python 3 derives __ne__ from __eq__, so it must be the inverse.
    assert (token != "a") is True


def test_eq_against_equal_token_is_true():
    """
    Covers lines 67-70 with a True outcome: same value, same start
    index and same end index.
    """
    token_a = ScalarToken("a", 0, 1)
    token_b = ScalarToken("a", 0, 1)

    assert (token_a == token_b) is True
    assert (token_b == token_a) is True  # symmetric
    assert (token_a == token_a) is True  # reflexive
    assert (token_a != token_b) is False


def test_eq_with_different_value_is_false():
    """
    Covers lines 67-69: the value comparison fails, so the start/end
    index comparisons are short-circuited.
    """
    token_a = ScalarToken("a", 0, 1)
    token_b = ScalarToken("b", 0, 1)

    assert (token_a == token_b) is False
    assert (token_a != token_b) is True


def test_eq_with_different_start_index_is_false():
    """
    Covers lines 67-70: the values match but the start index differs,
    so the end index comparison is short-circuited.
    """
    token_a = ScalarToken("a", 0, 1)
    token_b = ScalarToken("a", 5, 1)

    assert (token_a == token_b) is False


def test_eq_with_different_end_index_is_false():
    """
    Covers lines 67-70: value and start index match but the end index
    differs, exercising the final comparison on line 70.
    """
    token_a = ScalarToken("a", 0, 1)
    token_b = ScalarToken("a", 0, 9)

    assert (token_a == token_b) is False


def test_eq_with_other_token_subclass():
    """
    A plain Token subclass (not ScalarToken) still goes through the
    same __eq__ path, covering the isinstance branch of line 67 for a
    different concrete class, including cross-subclass equality.
    """

    class _ValueToken(Token):
        def _get_value(self) -> typing.Any:
            return self._value

    token_a = _ValueToken("x", 1, 2)
    token_b = _ValueToken("x", 1, 2)
    scalar = ScalarToken("x", 1, 2)

    assert (token_a == token_b) is True
    assert (token_a == scalar) is True
    assert (token_a == "x") is False

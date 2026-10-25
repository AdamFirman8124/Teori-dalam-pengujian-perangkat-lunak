# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


@pytest.fixture
def token_factory():
    class ConcreteToken(Token):
        def _get_value(self):
            return self._value

    return ConcreteToken


def test_token_eq_same_value_and_indices(token_factory):
    token = token_factory("hello", 0, 5)
    other = token_factory("hello", 0, 5)

    assert (token == other) is True
    assert (token != other) is False
    assert (token == token) is True


def test_token_eq_non_token(token_factory):
    token = token_factory("hello", 0, 5)

    assert (token == "hello") is False
    assert (token == 123) is False
    assert (token == None) is False  # noqa: E711
    assert (token == object()) is False
    assert (token != "hello") is True


def test_token_eq_non_token_does_not_call_get_value():
    # Token._get_value raises NotImplementedError; returning False
    # proves the isinstance check short-circuits before calling it.
    token = Token("hello", 0, 5)

    assert (token == "hello") is False
    assert (token == object()) is False


def test_token_eq_different_value(token_factory):
    token = token_factory("hello", 0, 5)
    other = token_factory("world", 0, 5)

    assert (token == other) is False
    assert (token != other) is True


def test_token_eq_different_start_index(token_factory):
    token = token_factory("hello", 0, 5)
    other = token_factory("hello", 1, 5)

    assert (token == other) is False
    assert (token != other) is True


def test_token_eq_different_end_index(token_factory):
    token = token_factory("hello", 0, 5)
    other = token_factory("hello", 0, 6)

    assert (token == other) is False
    assert (token != other) is True


def test_token_eq_other_is_token_subclass(token_factory):
    class OtherToken(Token):
        def _get_value(self):
            return self._value

    token = token_factory("hello", 0, 5)
    other = OtherToken("hello", 0, 5)

    assert (token == other) is True
    assert (other == token) is True

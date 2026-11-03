# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

import pytest

from typesystem.tokenize.tokens import ScalarToken


def test_token_init_explicit_content():
    """Instantiate a concrete Token with all arguments provided
    (covers lines 10-13 of Token.__init__)."""
    token = ScalarToken(value="hello", start_index=0, end_index=5, content="hello")

    # Postconditions: the constructor stored every argument.
    assert token._value == "hello"
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == "hello"

    # Public accessor reflects the stored state.
    assert token.value == "hello"


def test_token_init_default_content():
    """Instantiate a concrete Token without 'content' (covers lines 10-13
    and the default-argument branch of the 'content' parameter)."""
    token = ScalarToken(value=42, start_index=3, end_index=7)

    # Postconditions: the constructor stored every argument,
    # with 'content' falling back to its default value.
    assert token._value == 42
    assert token._start_index == 3
    assert token._end_index == 7
    assert token._content == ""

    # Public accessor reflects the stored state.
    assert token.value == 42


def test_token_init_isolated_instances():
    """Two independently constructed tokens do not share state,
    confirming the constructor assigns per-instance attributes."""
    first = ScalarToken(value="a", start_index=1, end_index=2, content="a")
    second = ScalarToken(value="b", start_index=3, end_index=4, content="b")

    assert first._value == "a"
    assert second._value == "b"
    assert first._start_index == 1
    assert second._start_index == 3
    assert first._end_index == 2
    assert second._end_index == 4
    assert first._content == "a"
    assert second._content == "b"

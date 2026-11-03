# file: project/typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [10, 11, 12, 13], "branches": []}
# gained: {"lines": [10, 11, 12, 13], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_init_sets_all_attributes():
    """Instantiating Token with explicit content must execute lines 10-13
    and store all four arguments on the instance."""
    value = {"key": [1, 2, 3]}
    token = Token(value=value, start_index=5, end_index=42, content="some content")

    assert token._value == {"key": [1, 2, 3]}
    assert token._start_index == 5
    assert token._end_index == 42
    assert token._content == "some content"


def test_token_init_default_content():
    """Instantiating Token without content must still execute lines 10-13,
    with the default empty string used for _content."""
    token = Token(value="scalar", start_index=0, end_index=6)

    assert token._value == "scalar"
    assert token._start_index == 0
    assert token._end_index == 6
    assert token._content == ""


def test_token_init_accepts_arbitrary_value_types():
    """Token must accept any value type (typing.Any) and store it as-is."""
    for value in (None, 0, 3.14, "text", b"bytes", [1, 2], {"a": 1}, (1, 2)):
        token = Token(value, 1, 2, "c")
        assert token._value is value
        assert token._start_index == 1
        assert token._end_index == 2
        assert token._content == "c"


def test_token_init_does_not_mutate_inputs():
    """The constructor must not mutate or share mutable state unexpectedly."""
    value = [1, 2, 3]
    token = Token(value, 0, 3, "abc")
    assert token._value == [1, 2, 3]
    # The stored value is the same object passed in (no copying), so mutating
    # the original is reflected; this documents the actual behavior.
    value.append(4)
    assert token._value == [1, 2, 3, 4]

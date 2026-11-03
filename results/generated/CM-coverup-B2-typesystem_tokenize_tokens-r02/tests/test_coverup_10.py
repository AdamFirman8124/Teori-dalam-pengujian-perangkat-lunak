# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token, ScalarToken


def test_base_token_value_property_calls_get_value():
    """
    Covers line 30 (`return self._get_value()`) via the abstract base class,
    whose `_get_value` implementation raises NotImplementedError.
    """
    token = Token(value="anything", start_index=0, end_index=5)

    # Accessing .value must dispatch to _get_value(), executing line 30.
    with pytest.raises(NotImplementedError):
        _ = token.value


def test_scalar_token_value_property_returns_underlying_value():
    """
    Covers line 30 (`return self._get_value()`) via ScalarToken, whose
    `_get_value` override returns the wrapped value.
    """
    token = ScalarToken(value=42, start_index=3, end_index=7)

    assert token.value == 42


def test_scalar_token_value_property_with_string_content():
    """
    Additional coverage of line 30 with a different value type and
    non-default content argument.

    `Token.string` slices the source content with
    `content[start_index:end_index + 1]`, so indices must match the
    content for the assertion to hold.
    """
    token = ScalarToken(
        value="hello", start_index=0, end_index=6, content='"hello"'
    )

    assert token.value == "hello"
    assert token.string == '"hello"'

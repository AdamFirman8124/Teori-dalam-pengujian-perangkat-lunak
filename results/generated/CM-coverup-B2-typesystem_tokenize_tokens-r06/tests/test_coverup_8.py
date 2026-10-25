# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from unittest.mock import Mock

from typesystem.tokenize.tokens import ListToken, Token


def test_list_token_value_returns_values_from_child_tokens():
    first = Mock(spec=Token)
    second = Mock(spec=Token)
    first._get_value.return_value = "first"
    second._get_value.return_value = 42
    token = ListToken([first, second], 0, 2)

    assert token.value == ["first", 42]
    first._get_value.assert_called_once_with()
    second._get_value.assert_called_once_with()


def test_list_token_lookup_returns_child_at_index():
    first = Mock(spec=Token)
    second = Mock(spec=Token)
    token = ListToken([first, second], 0, 2)

    assert token.lookup([1]) is second

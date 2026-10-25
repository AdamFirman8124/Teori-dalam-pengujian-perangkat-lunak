# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from unittest.mock import Mock

from typesystem.tokenize.tokens import ListToken


def test_list_token_get_value_returns_child_values():
    first = Mock()
    first._get_value.return_value = "first"
    second = Mock()
    second._get_value.return_value = 2
    token = ListToken([first, second], 0, 0)

    assert token._get_value() == ["first", 2]
    first._get_value.assert_called_once_with()
    second._get_value.assert_called_once_with()


def test_list_token_get_child_token_returns_indexed_token():
    first = Mock()
    second = Mock()
    token = ListToken([first, second], 0, 0)

    assert token._get_child_token(1) is second

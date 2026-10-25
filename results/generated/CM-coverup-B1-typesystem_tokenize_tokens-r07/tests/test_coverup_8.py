# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from unittest.mock import Mock

from typesystem.tokenize.tokens import ListToken, Token


def test_list_token_gets_values_and_child_tokens():
    first_child = Mock(spec=Token)
    first_child._get_value.return_value = "first"

    second_child = Mock(spec=Token)
    second_child._get_value.return_value = {"second": 2}

    token = ListToken([first_child, second_child], 0, 1)

    assert token.value == ["first", {"second": 2}]
    assert token.lookup([0]) is first_child
    assert token.lookup([1]) is second_child

    first_child._get_value.assert_called_once_with()
    second_child._get_value.assert_called_once_with()

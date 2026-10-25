# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_value_returns_child_values():
    children = [
        ScalarToken("first", 0, 5),
        ScalarToken(2, 6, 7),
    ]
    token = ListToken(children, 0, 7)

    assert token.value == ["first", 2]
    assert token.value is not token._value


def test_empty_list_token_value_returns_empty_list():
    token = ListToken([], 0, 0)

    assert token.value == []
    assert token.value is not token._value


def test_list_token_lookup_returns_requested_child():
    children = [
        ScalarToken("first", 0, 5),
        ScalarToken("second", 6, 12),
    ]
    token = ListToken(children, 0, 12)

    assert token.lookup([0]) is children[0]
    assert token.lookup([1]) is children[1]

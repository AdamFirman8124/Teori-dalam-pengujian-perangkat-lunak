# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_get_value():
    children = [
        ScalarToken("first", 0, 5, "first"),
        ScalarToken(2, 7, 7, "2"),
    ]
    token = ListToken(children, 0, 7, "[first, 2]")

    assert token._get_value() == ["first", 2]
    assert token._value == children


def test_list_token_get_child_token():
    children = [
        ScalarToken("first", 0, 5, "first"),
        ScalarToken("second", 7, 12, "second"),
    ]
    token = ListToken(children, 0, 12, "[first, second]")

    assert token._get_child_token(1) is children[1]
    assert token._value == children

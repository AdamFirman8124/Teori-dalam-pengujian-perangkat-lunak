# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_get_value_returns_child_values():
    children = [
        ScalarToken("alpha", 0, 5, "alpha"),
        ScalarToken(42, 6, 8, "42"),
    ]
    token = ListToken(children, 0, 8, "alpha 42")

    assert token._get_value() == ["alpha", 42]


def test_list_token_get_child_token_returns_indexed_child():
    children = [
        ScalarToken("first", 0, 5, "first"),
        ScalarToken("second", 6, 12, "second"),
    ]
    token = ListToken(children, 0, 12, "first second")

    assert token._get_child_token(1) is children[1]

# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

from typesystem.tokenize.tokens import ListToken, ScalarToken


def test_list_token_value_and_child_lookup():
    first = ScalarToken("first", 0, 5, "first")
    second = ScalarToken(42, 6, 8, "42")
    token = ListToken([first, second], 0, 8, "[first, 42]")

    assert token.value == ["first", 42]
    assert token.lookup([0]) is first
    assert token.lookup([1]) is second

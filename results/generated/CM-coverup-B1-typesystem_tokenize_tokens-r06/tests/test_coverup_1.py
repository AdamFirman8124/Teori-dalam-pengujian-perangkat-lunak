# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_value_and_child_lookups():
    key_token = ScalarToken("answer", 1, 7, '"answer"')
    value_token = ScalarToken(42, 9, 11, "42")
    token = DictToken({key_token: value_token}, 0, 12, '{"answer": 42}')

    assert token.value == {"answer": 42}
    assert token.lookup(["answer"]) is value_token
    assert token.lookup_key(["answer"]) is key_token

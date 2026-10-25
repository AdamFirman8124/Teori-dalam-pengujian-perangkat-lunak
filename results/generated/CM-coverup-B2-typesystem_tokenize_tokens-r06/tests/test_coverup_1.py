# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

from typesystem.tokenize.tokens import DictToken, Token


def test_dict_token_builds_child_mappings_and_returns_decoded_value():
    class DummyToken(Token):
        __hash__ = object.__hash__

        def _get_value(self):
            return self._value

    first_key = DummyToken("name", 1, 7, '"name"')
    first_value = DummyToken("Ada", 9, 14, '"Ada"')
    second_key = DummyToken("active", 16, 24, '"active"')
    second_value = DummyToken(True, 26, 30, "true")

    token = DictToken(
        {
            first_key: first_value,
            second_key: second_value,
        },
        0,
        31,
        '{"name": "Ada", "active": true}',
    )

    assert token._get_value() == {"name": "Ada", "active": True}
    assert token._get_child_token("name") is first_value
    assert token._get_child_token("active") is second_value
    assert token._get_key_token("name") is first_key
    assert token._get_key_token("active") is second_key

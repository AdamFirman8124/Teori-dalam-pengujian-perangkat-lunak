# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_equality_covers_all_conditions():
    class ConcreteToken(Token):
        def _get_value(self):
            return self._value

    token = ConcreteToken("value", 1, 5)

    assert token == ConcreteToken("value", 1, 5)
    assert not (token == object())
    assert not (token == ConcreteToken("other", 1, 5))
    assert not (token == ConcreteToken("value", 2, 5))
    assert not (token == ConcreteToken("value", 1, 6))

# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_value_delegates_to_get_value():
    expected = object()
    calls = []

    class ConcreteToken(Token):
        def _get_value(self):
            calls.append(self)
            return expected

    token = ConcreteToken("raw", 0, 3, "raw")

    assert token.value is expected
    assert calls == [token]

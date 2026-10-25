# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_value_calls_get_value():
    expected = object()

    class ConcreteToken(Token):
        def _get_value(self):
            self.get_value_called = True
            return expected

    token = ConcreteToken("raw", 0, 3, "raw")
    token.get_value_called = False

    assert token.value is expected
    assert token.get_value_called is True

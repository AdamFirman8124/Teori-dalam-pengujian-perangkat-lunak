# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_value_calls_get_value():
    sentinel = object()
    calls = []

    class TestToken(Token):
        def _get_value(self):
            calls.append(True)
            return sentinel

    token = TestToken(value=None, start_index=0, end_index=0)

    assert token.value is sentinel
    assert calls == [True]

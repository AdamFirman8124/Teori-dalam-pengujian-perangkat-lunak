# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_token_value_delegates_to_get_value():
    class FakeToken(Token):
        def _get_value(self):
            return "fake-value"

    token = FakeToken("ignored", 0, 5)
    assert token.value == "fake-value"


def test_token_value_base_class_raises_not_implemented():
    token = Token("raw", 0, 5)
    with pytest.raises(NotImplementedError):
        token.value

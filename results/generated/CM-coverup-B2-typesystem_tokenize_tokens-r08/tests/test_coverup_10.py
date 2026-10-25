# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


def test_value_property_returns_get_value_result():
    calls = []

    class _ConcreteToken(Token):
        def _get_value(self):
            calls.append(1)
            return "sentinel-value"

    token = _ConcreteToken("raw", 0, 3, content="raw")

    assert token.value == "sentinel-value"
    assert calls == [1]
    assert token.value == "sentinel-value"
    assert calls == [1, 1]


def test_value_property_base_class_raises_not_implemented():
    token = Token("raw", 0, 3)

    with pytest.raises(NotImplementedError):
        token.value

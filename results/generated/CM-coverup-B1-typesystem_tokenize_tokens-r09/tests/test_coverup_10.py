# file: project/typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [30], "branches": []}
# gained: {"lines": [30], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token


def test_token_value_delegates_to_get_value(monkeypatch):
    token = Token(value="raw", start_index=0, end_index=3, content="raw")
    monkeypatch.setattr(token, "_get_value", lambda: "mocked-value")
    assert token.value == "mocked-value"


def test_token_value_returns_exact_object_identity(monkeypatch):
    sentinel = object()
    token = Token(value=sentinel, start_index=0, end_index=1, content="")
    monkeypatch.setattr(token, "_get_value", lambda: sentinel)
    assert token.value is sentinel


def test_token_value_base_implementation_executes_and_raises():
    token = Token(value=123, start_index=0, end_index=1, content="123")
    with pytest.raises(NotImplementedError):
        _ = token.value

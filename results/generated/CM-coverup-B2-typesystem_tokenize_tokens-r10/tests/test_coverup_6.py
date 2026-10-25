# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from unittest.mock import Mock

from typesystem.tokenize.tokens import Token


def test_lookup_key_returns_key_token(monkeypatch):
    root_token = Token(value=None, start_index=0, end_index=0)
    container_token = Token(value={}, start_index=0, end_index=0)
    expected_token = Token(value="value", start_index=1, end_index=2)

    lookup = Mock(return_value=container_token)
    get_key_token = Mock(return_value=expected_token)

    monkeypatch.setattr(root_token, "lookup", lookup)
    monkeypatch.setattr(container_token, "_get_key_token", get_key_token)

    result = root_token.lookup_key(["parent", "key"])

    assert result is expected_token
    lookup.assert_called_once_with(["parent"])
    get_key_token.assert_called_once_with("key")

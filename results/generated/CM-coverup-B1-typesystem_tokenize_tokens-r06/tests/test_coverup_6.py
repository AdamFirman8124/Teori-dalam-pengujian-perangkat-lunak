# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from unittest.mock import Mock, sentinel

from typesystem.tokenize.tokens import Token


def test_lookup_key_uses_parent_token_and_returns_key_token(monkeypatch):
    root = Token(value=None, start_index=0, end_index=0)
    parent_token = Mock()
    parent_token._get_key_token.return_value = sentinel.key_token
    lookup = Mock(return_value=parent_token)
    monkeypatch.setattr(root, "lookup", lookup)

    result = root.lookup_key(["parent", "key"])

    assert result is sentinel.key_token
    lookup.assert_called_once_with(["parent"])
    parent_token._get_key_token.assert_called_once_with("key")

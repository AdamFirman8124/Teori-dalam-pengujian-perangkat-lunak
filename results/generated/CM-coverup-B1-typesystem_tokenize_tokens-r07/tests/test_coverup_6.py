# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from unittest.mock import Mock, sentinel

from typesystem.tokenize.tokens import Token


def test_lookup_key_uses_parent_token_and_final_key():
    root = Mock(spec=Token)
    parent = Mock(spec=Token)
    root.lookup.return_value = parent
    parent._get_key_token.return_value = sentinel.key_token

    result = Token.lookup_key(root, ["outer", "inner", "target"])

    assert result is sentinel.key_token
    root.lookup.assert_called_once_with(["outer", "inner"])
    parent._get_key_token.assert_called_once_with("target")

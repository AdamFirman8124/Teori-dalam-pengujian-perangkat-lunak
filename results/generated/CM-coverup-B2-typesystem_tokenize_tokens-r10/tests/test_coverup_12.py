# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from unittest.mock import Mock

from typesystem.tokenize.tokens import Token


def test_token_end_returns_position_at_end_index(monkeypatch):
    token = Token(value=None, start_index=2, end_index=7, content="example")
    expected_position = object()
    get_position = Mock(return_value=expected_position)
    monkeypatch.setattr(token, "_get_position", get_position)

    assert token.end is expected_position
    get_position.assert_called_once_with(7)

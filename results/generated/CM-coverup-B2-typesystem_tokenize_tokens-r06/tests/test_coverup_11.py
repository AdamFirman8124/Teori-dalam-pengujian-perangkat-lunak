# file: project/typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_start_uses_start_index(monkeypatch):
    expected_position = object()
    received_indexes = []

    def fake_get_position(self, index):
        received_indexes.append(index)
        return expected_position

    monkeypatch.setattr(Token, "_get_position", fake_get_position)

    token = Token(value="value", start_index=7, end_index=12, content="content")

    assert token.start is expected_position
    assert received_indexes == [7]

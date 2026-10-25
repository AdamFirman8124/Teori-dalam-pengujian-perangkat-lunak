# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.tokenize.tokens import Token


def test_end_returns_position_for_end_index(monkeypatch):
    token = Token(value=None, start_index=2, end_index=7, content="example")
    expected_position = object()
    observed_indices = []

    def fake_get_position(index):
        observed_indices.append(index)
        return expected_position

    monkeypatch.setattr(token, "_get_position", fake_get_position)

    assert token.end is expected_position
    assert observed_indices == [7]

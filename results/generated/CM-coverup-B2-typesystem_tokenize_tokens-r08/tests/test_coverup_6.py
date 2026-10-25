# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from typesystem.tokenize.tokens import Token


def test_lookup_key_returns_key_token_from_parent(monkeypatch):
    root = Token(value={}, start_index=0, end_index=0)
    parent = Token(value={}, start_index=0, end_index=0)
    key_token = Token(value="key", start_index=0, end_index=3)

    lookup_calls = []
    key_calls = []

    def fake_lookup(index):
        lookup_calls.append(index)
        return parent

    def fake_get_key_token(key):
        key_calls.append(key)
        return key_token

    monkeypatch.setattr(root, "lookup", fake_lookup)
    monkeypatch.setattr(parent, "_get_key_token", fake_get_key_token)

    result = root.lookup_key(["parent", "key"])

    assert result is key_token
    assert lookup_calls == [["parent"]]
    assert key_calls == ["key"]

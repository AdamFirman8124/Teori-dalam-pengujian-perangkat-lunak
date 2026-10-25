# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_empty_index_returns_self():
    token = Token(value="abc", start_index=0, end_index=3, content="abc")
    result = token.lookup([])
    assert result is token


def test_lookup_single_key(monkeypatch):
    parent = Token(value={"a": 1}, start_index=0, end_index=8, content='{"a": 1}')
    child = Token(value=1, start_index=6, end_index=7, content='{"a": 1}')
    calls = []

    def fake_get_child(key):
        calls.append(key)
        assert key == "a"
        return child

    monkeypatch.setattr(parent, "_get_child_token", fake_get_child)
    result = parent.lookup(["a"])
    assert result is child
    assert calls == ["a"]


def test_lookup_chained_keys(monkeypatch):
    root = Token(value={"a": {"b": 2}}, start_index=0, end_index=14, content='{"a": {"b": 2}}')
    mid = Token(value={"b": 2}, start_index=6, end_index=13, content='{"a": {"b": 2}}')
    leaf = Token(value=2, start_index=11, end_index=12, content='{"a": {"b": 2}}')
    root_calls = []
    mid_calls = []

    def fake_root_get_child(key):
        root_calls.append(key)
        assert key == "a"
        return mid

    def fake_mid_get_child(key):
        mid_calls.append(key)
        assert key == "b"
        return leaf

    monkeypatch.setattr(root, "_get_child_token", fake_root_get_child)
    monkeypatch.setattr(mid, "_get_child_token", fake_mid_get_child)
    result = root.lookup(["a", "b"])
    assert result is leaf
    assert root_calls == ["a"]
    assert mid_calls == ["b"]

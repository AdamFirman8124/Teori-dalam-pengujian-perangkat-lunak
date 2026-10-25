# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_with_empty_index_returns_same_token():
    token = Token(value=None, start_index=0, end_index=0)

    result = token.lookup([])

    assert result is token


def test_lookup_traverses_each_key(monkeypatch):
    root = Token(value=None, start_index=0, end_index=0)
    child = Token(value=None, start_index=0, end_index=0)
    leaf = Token(value="result", start_index=0, end_index=0)
    calls = []

    def get_root_child(key):
        calls.append(("root", key))
        return child

    def get_child_child(key):
        calls.append(("child", key))
        return leaf

    monkeypatch.setattr(root, "_get_child_token", get_root_child)
    monkeypatch.setattr(child, "_get_child_token", get_child_child)

    result = root.lookup(["outer", "inner"])

    assert result is leaf
    assert calls == [("root", "outer"), ("child", "inner")]

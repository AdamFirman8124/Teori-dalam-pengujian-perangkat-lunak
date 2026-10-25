# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_returns_self_for_empty_index(monkeypatch):
    token = Token(None, 0, 0)

    def unexpected_lookup(key):
        raise AssertionError("_get_child_token should not be called")

    monkeypatch.setattr(token, "_get_child_token", unexpected_lookup)

    assert token.lookup([]) is token


def test_lookup_traverses_each_index_key(monkeypatch):
    root = Token(None, 0, 0)
    child = Token(None, 0, 0)
    grandchild = Token(None, 0, 0)
    calls = []

    def get_root_child(key):
        calls.append((root, key))
        assert key == "child"
        return child

    def get_child_child(key):
        calls.append((child, key))
        assert key == 1
        return grandchild

    monkeypatch.setattr(root, "_get_child_token", get_root_child)
    monkeypatch.setattr(child, "_get_child_token", get_child_child)

    result = root.lookup(["child", 1])

    assert result is grandchild
    assert calls == [(root, "child"), (child, 1)]

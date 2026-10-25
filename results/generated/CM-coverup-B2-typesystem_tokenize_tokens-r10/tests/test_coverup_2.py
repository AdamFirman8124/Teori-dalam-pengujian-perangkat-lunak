# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_with_empty_index_returns_same_token():
    token = Token(value="root", start_index=0, end_index=4, content="root")

    result = token.lookup([])

    assert result is token


def test_lookup_traverses_each_child_token(monkeypatch):
    root = Token(value="root", start_index=0, end_index=4, content="root")
    child = Token(value="child", start_index=5, end_index=10, content="child")
    grandchild = Token(
        value="grandchild",
        start_index=11,
        end_index=21,
        content="grandchild",
    )
    calls = []
    children = {
        (id(root), "first"): child,
        (id(child), "second"): grandchild,
    }

    def fake_get_child_token(self, key):
        calls.append((self, key))
        return children[(id(self), key)]

    monkeypatch.setattr(Token, "_get_child_token", fake_get_child_token)

    result = root.lookup(["first", "second"])

    assert result is grandchild
    assert calls == [(root, "first"), (child, "second")]

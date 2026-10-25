# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_with_empty_index_returns_same_token(monkeypatch):
    token = Token(value=None, start_index=0, end_index=0)

    def unexpected_child_lookup(self, key):
        raise AssertionError("_get_child_token must not be called for an empty index")

    monkeypatch.setattr(Token, "_get_child_token", unexpected_child_lookup)

    assert token.lookup([]) is token


def test_lookup_traverses_each_key_in_order(monkeypatch):
    root = Token(value="root", start_index=0, end_index=10)
    child = Token(value="child", start_index=1, end_index=9)
    grandchild = Token(value="grandchild", start_index=2, end_index=8)
    calls = []

    def get_child_token(self, key):
        calls.append((self, key))
        if self is root and key == "first":
            return child
        if self is child and key == "second":
            return grandchild
        raise AssertionError(f"Unexpected lookup: {self!r}, {key!r}")

    monkeypatch.setattr(Token, "_get_child_token", get_child_token)

    assert root.lookup(["first", "second"]) is grandchild
    assert calls == [(root, "first"), (child, "second")]

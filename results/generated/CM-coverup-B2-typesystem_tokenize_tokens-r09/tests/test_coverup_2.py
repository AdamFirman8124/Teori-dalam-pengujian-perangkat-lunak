# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_with_empty_index_returns_same_token(monkeypatch):
    token = Token(None, 0, 0)

    def unexpected_get_child_token(self, key):
        raise AssertionError("_get_child_token must not be called for an empty index")

    monkeypatch.setattr(Token, "_get_child_token", unexpected_get_child_token)

    assert token.lookup([]) is token


def test_lookup_traverses_each_index_key(monkeypatch):
    root = Token(None, 0, 0)
    child = Token(None, 0, 0)
    target = Token(None, 0, 0)
    calls = []

    def get_child_token(self, key):
        calls.append((self, key))
        if self is root and key == "child":
            return child
        if self is child and key == 1:
            return target
        raise AssertionError(f"Unexpected lookup: {key!r}")

    monkeypatch.setattr(Token, "_get_child_token", get_child_token)

    result = root.lookup(["child", 1])

    assert result is target
    assert len(calls) == 2
    assert calls[0][0] is root
    assert calls[0][1] == "child"
    assert calls[1][0] is child
    assert calls[1][1] == 1

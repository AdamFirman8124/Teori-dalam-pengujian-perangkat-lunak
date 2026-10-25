# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


def test_lookup_empty_index_returns_self(monkeypatch):
    token = Token({"a": 1}, 0, 8, content='{"a": 1}')

    def _fail(self, key):
        raise AssertionError("_get_child_token should not be called for empty index")

    monkeypatch.setattr(Token, "_get_child_token", _fail)

    result = token.lookup([])

    assert result is token


def test_lookup_single_key(monkeypatch):
    token = Token({"a": 1}, 0, 8, content='{"a": 1}')
    expected_child = Token(1, 5, 6, content='{"a": 1}')
    calls = []

    def _fake_get_child(self, key):
        calls.append((self, key))
        return expected_child

    monkeypatch.setattr(Token, "_get_child_token", _fake_get_child)

    result = token.lookup(["a"])

    assert result is expected_child
    assert calls == [(token, "a")]


def test_lookup_chained_keys(monkeypatch):
    root = Token({"a": {"b": 2}}, 0, 14, content='{"a": {"b": 2}}')
    mid = Token({"b": 2}, 5, 13, content='{"a": {"b": 2}}')
    leaf = Token(2, 11, 12, content='{"a": {"b": 2}}')
    calls = []

    def _fake_get_child(self, key):
        calls.append((self, key))
        if self is root and key == "a":
            return mid
        if self is mid and key == "b":
            return leaf
        raise AssertionError(f"unexpected lookup: {self!r} [{key!r}]")

    monkeypatch.setattr(Token, "_get_child_token", _fake_get_child)

    result = root.lookup(["a", "b"])

    assert result is leaf
    assert calls == [(root, "a"), (mid, "b")]

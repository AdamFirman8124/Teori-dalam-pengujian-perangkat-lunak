# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import Token


class FakeToken(Token):
    """Minimal Token subclass with a dict of children, for lookup() tests."""

    def __init__(self, children=None, name="root"):
        super().__init__(value=None, start_index=0, end_index=0)
        self.children = children if children is not None else {}
        self.name = name
        self.requested_keys = []

    def _get_child_token(self, key):
        self.requested_keys.append(key)
        return self.children[key]


def test_lookup_empty_index_returns_self():
    token = FakeToken()
    result = token.lookup([])
    assert result is token
    assert token.requested_keys == []


def test_lookup_single_key_returns_child():
    child = FakeToken(name="child")
    token = FakeToken(children={"a": child})
    result = token.lookup(["a"])
    assert result is child
    assert token.requested_keys == ["a"]


def test_lookup_multiple_keys_walks_chain():
    leaf = FakeToken(name="leaf")
    mid = FakeToken(children={"b": leaf}, name="mid")
    root = FakeToken(children={"a": mid}, name="root")

    result = root.lookup(["a", "b"])

    assert result is leaf
    assert root.requested_keys == ["a"]
    assert mid.requested_keys == ["b"]
    assert leaf.requested_keys == []


def test_lookup_does_not_mutate_self():
    child = FakeToken(name="child")
    token = FakeToken(children={"a": child})
    token.lookup(["a"])
    assert token.children == {"a": child}
    assert token.name == "root"


def test_lookup_missing_key_propagates_error():
    token = FakeToken(children={})
    with pytest.raises(KeyError):
        token.lookup(["missing"])
    assert token.requested_keys == ["missing"]


def test_lookup_uses_get_child_token_via_monkeypatch(monkeypatch):
    """Exercise lookup() on a plain Token by patching the abstract hook."""
    calls = []
    child = Token(value="child", start_index=1, end_index=2)

    def fake_get_child_token(self, key):
        calls.append(key)
        return child

    monkeypatch.setattr(Token, "_get_child_token", fake_get_child_token)

    token = Token(value="root", start_index=0, end_index=4)

    assert token.lookup([]) is token
    assert calls == []

    assert token.lookup(["x"]) is child
    assert calls == ["x"]

    assert token.lookup(["x", "y"]) is child
    assert calls == ["x", "x", "y"]

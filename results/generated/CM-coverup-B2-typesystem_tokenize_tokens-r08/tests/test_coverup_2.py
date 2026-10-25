# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import Token


def test_lookup_with_empty_index_returns_same_token(monkeypatch):
    token = Token(value="root", start_index=0, end_index=4, content="root")

    def unexpected_child_lookup(self, key):
        pytest.fail("_get_child_token must not be called for an empty index")

    monkeypatch.setattr(Token, "_get_child_token", unexpected_child_lookup)

    assert token.lookup([]) is token


def test_lookup_traverses_each_key_in_order(monkeypatch):
    root = Token(value="root", start_index=0, end_index=10, content="root")
    child = Token(value="child", start_index=1, end_index=5, content="child")
    leaf = Token(value="leaf", start_index=2, end_index=4, content="leaf")

    calls = []
    transitions = {
        (id(root), "child"): child,
        (id(child), 0): leaf,
    }

    def get_child_token(self, key):
        calls.append((self, key))
        return transitions[(id(self), key)]

    monkeypatch.setattr(Token, "_get_child_token", get_child_token)

    result = root.lookup(["child", 0])

    assert result is leaf
    assert calls == [(root, "child"), (child, 0)]

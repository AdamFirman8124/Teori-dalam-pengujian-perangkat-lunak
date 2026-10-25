# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import Token


def _make_token(children=None):
    token = object.__new__(Token)
    token._children = dict(children) if children else {}
    token._get_child_token = lambda key: token._children[key]
    return token


def test_lookup_empty_index_returns_self():
    token = _make_token()

    result = token.lookup([])

    assert result is token


def test_lookup_single_key_returns_child():
    child = _make_token()
    parent = _make_token({"a": child})

    result = parent.lookup(["a"])

    assert result is child


def test_lookup_multiple_keys_traverses_nested_tokens():
    leaf = _make_token()
    middle = _make_token({"c": leaf})
    root = _make_token({"b": middle})

    result = root.lookup(["b", "c"])

    assert result is middle._children["c"]
    assert result is leaf


def test_lookup_list_index_traverses_in_order():
    leaf = _make_token()
    first = _make_token({0: leaf})
    root = _make_token({0: first})

    assert root.lookup([0]) is first
    assert root.lookup([0, 0]) is leaf
    assert root.lookup([]) is root


def test_lookup_calls_get_child_token_for_each_key(monkeypatch):
    calls = []
    child = object.__new__(Token)
    leaf = object.__new__(Token)
    root = object.__new__(Token)
    mapping = {(id(root), "a"): child, (id(child), "b"): leaf}

    def fake_get_child_token(self, key):
        calls.append((self, key))
        return mapping[(id(self), key)]

    monkeypatch.setattr(Token, "_get_child_token", fake_get_child_token)

    result = root.lookup(["a", "b"])

    assert result is leaf
    assert calls == [(root, "a"), (child, "b")]


def test_lookup_propagates_missing_key_error():
    child = _make_token()
    parent = _make_token({"a": child})

    with pytest.raises(KeyError):
        parent.lookup(["missing"])

    with pytest.raises(KeyError):
        parent.lookup(["a", "missing"])

# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import Token


class _StubToken(Token):
    """Token whose children are supplied explicitly, recording lookups."""

    def __init__(self, value, children=None):
        super().__init__(value, 0, 0)
        self._children = children if children is not None else {}
        self.requested_keys = []

    def _get_child_token(self, key):
        self.requested_keys.append(key)
        return self._children[key]


def test_lookup_empty_index_returns_self():
    token = _StubToken("root")
    result = token.lookup([])
    assert result is token
    assert token.requested_keys == []


def test_lookup_single_key_returns_child():
    child = _StubToken("child")
    root = _StubToken("root", {"a": child})

    result = root.lookup(["a"])

    assert result is child
    assert root.requested_keys == ["a"]
    assert child.requested_keys == []


def test_lookup_multiple_keys_walks_chain_in_order():
    leaf = _StubToken("leaf")
    mid = _StubToken("mid", {"b": leaf})
    root = _StubToken("root", {"a": mid})

    result = root.lookup(["a", "b"])

    assert result is leaf
    assert root.requested_keys == ["a"]
    assert mid.requested_keys == ["b"]
    assert leaf.requested_keys == []


def test_lookup_does_not_mutate_self():
    child = _StubToken("child")
    root = _StubToken("root", {"a": child})
    before = (root._value, root._start_index, root._end_index, root._content)

    root.lookup(["a"])

    assert (root._value, root._start_index, root._end_index, root._content) == before


def test_lookup_propagates_missing_key_error():
    root = _StubToken("root", {})

    with pytest.raises(KeyError):
        root.lookup(["missing"])

    assert root.requested_keys == ["missing"]


def test_base_token_get_child_token_not_implemented():
    token = Token("root", 0, 0)

    with pytest.raises(NotImplementedError):
        token.lookup(["a"])

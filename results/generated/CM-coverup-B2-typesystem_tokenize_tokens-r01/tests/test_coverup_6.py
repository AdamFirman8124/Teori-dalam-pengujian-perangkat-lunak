# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


class _ChildToken(Token):
    """Stub token that records the key it receives and returns a fixed token."""

    def __init__(self, key_token):
        self.key_token = key_token
        self.received_key = None

    def _get_key_token(self, key):
        self.received_key = key
        return self.key_token


class _ParentToken(Token):
    """Stub token that returns a fixed child for any lookup key."""

    def __init__(self, child):
        self.child = child
        self.received_keys = []

    def _get_child_token(self, key):
        self.received_keys.append(key)
        return self.child


class _SelfKeyToken(Token):
    """Stub token that can serve as its own key token (for single-element index)."""

    def __init__(self):
        self.received_key = None

    def _get_key_token(self, key):
        self.received_key = key
        return self


def test_lookup_key_traverses_to_child_and_returns_key_token():
    key_token = Token.__new__(Token)  # sentinel result token
    child = _ChildToken(key_token)
    parent = _ParentToken(child)

    result = parent.lookup_key(["a", "b"])

    # lookup(index[:-1]) must have traversed with "a" ...
    assert parent.received_keys == ["a"]
    # ... and _get_key_token must have been called with the last element "b"
    assert child.received_key == "b"
    # the returned token is the one produced by the child's _get_key_token
    assert result is key_token


def test_lookup_key_with_single_element_index_uses_self():
    token = _SelfKeyToken()

    result = token.lookup_key(["only"])

    # lookup([]) returns self, so _get_key_token is called on the token itself
    assert token.received_key == "only"
    assert result is token

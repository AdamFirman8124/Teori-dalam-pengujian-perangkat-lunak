# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest

from typesystem.tokenize.tokens import Token


@pytest.fixture()
def fake_token_cls():
    """
    A minimal concrete ``Token`` subclass with programmable child/key
    mappings, used to drive ``Token.lookup_key`` deterministically.

    The class is created fresh for every test (function-scoped fixture)
    and nothing outside the test module is mutated, so no state can
    leak between tests.
    """

    class FakeToken(Token):
        def __init__(self, value, start_index, end_index, content=""):
            super().__init__(value, start_index, end_index, content)
            self.children = {}    # key -> child token (used by lookup)
            self.key_tokens = {}  # key -> key token (used by lookup_key)
            self.child_calls = []
            self.key_calls = []

        def _get_child_token(self, key):
            self.child_calls.append(key)
            return self.children[key]

        def _get_key_token(self, key):
            self.key_calls.append(key)
            return self.key_tokens[key]

    return FakeToken


def test_lookup_key_single_level(fake_token_cls):
    # index[:-1] == [] -> lookup([]) returns self, no traversal happens;
    # index[-1] is then resolved via _get_key_token on self.
    root = fake_token_cls({}, 0, 0)
    key_token = fake_token_cls("name", 0, 6)
    root.key_tokens["name"] = key_token

    result = root.lookup_key(["name"])

    assert result is key_token
    assert root.child_calls == []          # lookup(index[:-1]) did not traverse
    assert root.key_calls == ["name"]      # _get_key_token called with index[-1]


def test_lookup_key_nested(fake_token_cls):
    # index[:-1] == ["outer"] -> lookup traverses via _get_child_token,
    # then _get_key_token is called on the resolved child token.
    root = fake_token_cls({}, 0, 0)
    child = fake_token_cls({}, 5, 10)
    grandchild_key = fake_token_cls("inner", 12, 19)
    root.children["outer"] = child
    child.key_tokens["inner"] = grandchild_key

    result = root.lookup_key(["outer", "inner"])

    assert result is grandchild_key
    assert root.child_calls == ["outer"]   # root resolved the "outer" child
    assert root.key_calls == []            # key lookup happened on the child...
    assert child.key_calls == ["inner"]    # ...not on the root


def test_lookup_key_returns_key_token_not_value_token(fake_token_cls):
    # lookup_key must return the token for the *key*, unlike lookup()
    # which returns the token for the *value*.
    root = fake_token_cls({}, 0, 0)
    key_token = fake_token_cls("name", 0, 6)
    value_token = fake_token_cls("alice", 8, 15)
    root.key_tokens["name"] = key_token
    root.children["name"] = value_token

    assert root.lookup_key(["name"]) is key_token
    assert root.lookup(["name"]) is value_token


def test_lookup_key_with_non_string_key(fake_token_cls):
    # index[-1] may be any hashable key (e.g. a list index), not just a str.
    root = fake_token_cls([], 0, 0)
    key_token = fake_token_cls(0, 0, 1)
    root.key_tokens[0] = key_token

    assert root.lookup_key([0]) is key_token
    assert root.key_calls == [0]


def test_lookup_key_with_real_dict_token():
    try:
        from typesystem.tokenize.tokens import DictToken, ScalarToken
    except ImportError:
        pytest.skip("DictToken/ScalarToken not available in this version")

    key = ScalarToken("name", 1, 7)
    value = ScalarToken("alice", 9, 16)
    try:
        root = DictToken({key: value}, 0, 17, '{"name": "alice"}')
    except TypeError:
        pytest.skip("Token instances are not hashable in this version")

    # Exercises lines 53-54 through the real DictToken implementation:
    # lookup([]) -> root, then root._get_key_token("name") -> key token.
    assert root.lookup_key(["name"]) is key

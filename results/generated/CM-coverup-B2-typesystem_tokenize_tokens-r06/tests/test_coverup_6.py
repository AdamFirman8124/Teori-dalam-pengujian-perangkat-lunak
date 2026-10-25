# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_lookup_key_top_level():
    # {"name": "alice"}
    key_token = ScalarToken("name", 0, 5)
    value_token = ScalarToken("alice", 7, 12)
    dict_token = DictToken({key_token: value_token}, 0, 14)

    result = dict_token.lookup_key(["name"])

    # lookup([]) returns self, then _get_key_token returns the key token
    assert result is key_token
    assert result._value == "name"


def test_lookup_key_nested():
    # {"a": {"b": 1}}
    inner_key = ScalarToken("b", 4, 6)
    inner_value = ScalarToken(1, 8, 9)
    inner = DictToken({inner_key: inner_value}, 4, 9)

    outer_key = ScalarToken("a", 0, 3)
    outer = DictToken({outer_key: inner}, 0, 10)

    result = outer.lookup_key(["a", "b"])

    # lookup(["a"]) returns the inner dict token, then its key token for "b"
    assert result is inner_key
    assert result._value == "b"

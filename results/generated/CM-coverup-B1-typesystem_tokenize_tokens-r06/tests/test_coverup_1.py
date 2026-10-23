# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest
from typesystem.tokenize.tokens import DictToken, ScalarToken


def test_dict_token_covers_missing_lines():
    key_a = ScalarToken("a", 0, 1)
    key_b = ScalarToken("b", 2, 3)
    val_a = ScalarToken("1", 4, 5)
    val_b = ScalarToken("2", 6, 7)

    source = {key_a: val_a, key_b: val_b}
    token = DictToken(source, 0, 7)

    # __init__ body: lines 84-86
    assert token._value is source
    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_tokens == {"a": val_a, "b": val_b}

    # _get_value body: lines 89-91
    assert token._get_value() == {"a": "1", "b": "2"}

    # _get_child_token body: line 95
    assert token._get_child_token("a") is val_a
    assert token._get_child_token("b") is val_b

    # _get_key_token body: line 98
    assert token._get_key_token("a") is key_a
    assert token._get_key_token("b") is key_b

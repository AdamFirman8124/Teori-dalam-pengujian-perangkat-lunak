# file: project/typesystem/tokenize/tokens.py:82-98
# asked: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}
# gained: {"lines": [84, 85, 86, 89, 90, 91, 95, 98], "branches": []}

import pytest

from typesystem.tokenize.tokenize_json import tokenize_json
from typesystem.tokenize.tokens import DictToken


def test_dict_token_value_and_child_token_access():
    token = tokenize_json('{"answer": 42, "enabled": true}')

    assert isinstance(token, DictToken)
    assert token._get_value() == {"answer": 42, "enabled": True}

    answer_token = token._get_child_token("answer")
    answer_key_token = token._get_key_token("answer")
    enabled_token = token._get_child_token("enabled")
    enabled_key_token = token._get_key_token("enabled")

    assert answer_token._get_value() == 42
    assert answer_key_token._get_value() == "answer"
    assert enabled_token._get_value() is True
    assert enabled_key_token._get_value() == "enabled"

    # Child token lookups are consistent with the dict's own value mapping.
    assert set(token._child_tokens) == {"answer", "enabled"}
    assert set(token._child_keys) == {"answer", "enabled"}


def test_dict_token_unknown_key_raises_keyerror():
    token = tokenize_json('{"answer": 42}')

    with pytest.raises(KeyError):
        token._get_child_token("missing")

    with pytest.raises(KeyError):
        token._get_key_token("missing")

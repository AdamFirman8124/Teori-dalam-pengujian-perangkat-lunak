# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest

from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken


def test_lookup_key_navigates_through_list_to_dict():
    """
    Covers lines 53-54 of Token.lookup_key:
        token = self.lookup(index[:-1])
        return token._get_key_token(index[-1])

    The index navigates through a ListToken into a DictToken, so
    lookup(index[:-1]) resolves to the DictToken and _get_key_token
    returns the key token for the final index element.
    """
    key_b = ScalarToken("b", 5, 6)
    value_one = ScalarToken(1, 9, 10)
    inner_dict = DictToken({key_b: value_one}, 4, 11)
    root = ListToken([inner_dict], 0, 12)

    result = root.lookup_key([0, "b"])

    # The returned token must be the key token held by the dict,
    # not the value token.
    assert result is key_b
    assert result.value == "b"
    assert result._start_index == 5
    assert result._end_index == 6


def test_lookup_key_with_dict_root_and_empty_prefix():
    """
    Also covers lines 53-54, exercising two variants:
      - index[:-1] non-empty (navigates into a nested DictToken)
      - index[:-1] empty (lookup returns the token itself, which must
        then provide _get_key_token)
    """
    key_a = ScalarToken("a", 1, 2)
    key_b = ScalarToken("b", 5, 6)
    value_one = ScalarToken(1, 9, 10)
    inner_dict = DictToken({key_b: value_one}, 4, 11)
    root = DictToken({key_a: inner_dict}, 0, 12)

    # Non-empty prefix: lookup(["a"]) -> inner_dict, then key token "b".
    result_nested = root.lookup_key(["a", "b"])
    assert result_nested is key_b
    assert result_nested.value == "b"
    assert result_nested._start_index == 5
    assert result_nested._end_index == 6

    # Empty prefix: lookup([]) -> root itself, then key token "a".
    result_self = root.lookup_key(["a"])
    assert result_self is key_a
    assert result_self.value == "a"
    assert result_self._start_index == 1
    assert result_self._end_index == 2

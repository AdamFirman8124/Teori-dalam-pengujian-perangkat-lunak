# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

import pytest

from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token


def _build_nested_token():
    """
    Build the token tree corresponding to the document:

        {"data": {"list": [42]}}

    Note: keys/values inside a DictToken's value must themselves be Token
    instances, because DictToken.__init__ reads ``k._value`` from each key.
    All objects are purely local, so the tests leave no global state behind
    (nothing to monkeypatch or tear down).
    """
    scalar = ScalarToken(42, 21, 23, content="42")
    list_token = ListToken([scalar], 20, 24, content="[42]")
    inner_dict = DictToken(
        {ScalarToken("list", 13, 19, content='"list"'): list_token},
        12,
        25,
        content='{"list": [42]}',
    )
    outer = DictToken(
        {ScalarToken("data", 1, 7, content='"data"'): inner_dict},
        0,
        26,
        content='{"data": {"list": [42]}}',
    )
    return outer, inner_dict, list_token, scalar


def test_lookup_empty_index_returns_self():
    """
    Covers line 44 (token = self) and line 47 (return token) with the
    for-loop on line 45 never entering its body (empty index branch).
    """
    outer, *_ = _build_nested_token()

    result = outer.lookup([])

    assert result is outer


def test_lookup_traverses_nested_children():
    """
    Covers line 46 (token = token._get_child_token(key)) repeatedly,
    exercising DictToken._get_child_token (str keys) and
    ListToken._get_child_token (int key) along the way.
    """
    outer, inner_dict, list_token, scalar = _build_nested_token()

    assert outer.lookup(["data"]) is inner_dict
    assert outer.lookup(["data", "list"]) is list_token

    result = outer.lookup(["data", "list", 0])

    assert result is scalar
    assert result.value == 42


def test_lookup_through_base_token_raises_not_implemented():
    """
    The loop body dispatches to _get_child_token; on the base Token class
    that raises NotImplementedError, which must propagate out of lookup().
    """
    base = Token(value=None, start_index=0, end_index=0)

    with pytest.raises(NotImplementedError):
        base.lookup(["any"])


def test_lookup_missing_key_propagates_keyerror():
    """
    A key absent from the structure surfaces the underlying KeyError
    raised by DictToken._get_child_token.
    """
    outer, *_ = _build_nested_token()

    with pytest.raises(KeyError):
        outer.lookup(["nope"])

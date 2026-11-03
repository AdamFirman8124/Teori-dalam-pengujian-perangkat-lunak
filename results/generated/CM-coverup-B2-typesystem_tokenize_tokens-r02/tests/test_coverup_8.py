# file: project/typesystem/tokenize/tokens.py:101-106
# asked: {"lines": [103, 106], "branches": []}
# gained: {"lines": [103, 106], "branches": []}

import pytest

from typesystem.tokenize.tokens import ListToken, Token


class _ScalarToken(Token):
    """Minimal concrete Token subclass whose value is the wrapped scalar."""

    def _get_value(self):
        return self._value


def test_list_token_get_value_returns_child_values():
    # Covers line 103: the list comprehension in ListToken._get_value.
    children = [
        _ScalarToken(1, 0, 1, "1"),
        _ScalarToken("two", 2, 7, '"two"'),
    ]
    token = ListToken(children, 0, 7, '[1, "two"]')

    assert token.value == [1, "two"]
    # The underlying child-token list must be used as-is (not copied/mutated).
    assert token._value is children
    assert [child.value for child in token._value] == [1, "two"]


def test_list_token_get_value_empty_list():
    # Covers line 103 with an empty child list (comprehension runs zero times).
    token = ListToken([], 0, 2, "[]")

    assert token.value == []


def test_list_token_get_child_token_by_index():
    # Covers line 106: ListToken._get_child_token.
    child_a = _ScalarToken("a", 1, 4, '"a"')
    child_b = _ScalarToken("b", 7, 10, '"b"')
    token = ListToken([child_a, child_b], 0, 11, '["a", "b"]')

    assert token._get_child_token(0) is child_a
    assert token._get_child_token(1) is child_b
    # Negative indices index from the end of the child list.
    assert token._get_child_token(-1) is child_b
    assert token._get_child_token(-2) is child_a

    with pytest.raises(IndexError):
        token._get_child_token(2)


def test_list_token_lookup_drives_get_child_token():
    # Exercise line 106 through the public lookup() API, which repeatedly
    # calls _get_child_token for each key in the index path.
    inner = _ScalarToken(42, 5, 7, "42")
    middle = ListToken([inner], 4, 8, "[42]")
    outer = ListToken([middle], 0, 9, "[[42]]")

    assert outer.lookup([0]) is middle
    assert outer.lookup([0, 0]) is inner
    # Also re-exercises line 103 via the value property on the nested list.
    assert outer.lookup([0]).value == [42]
    assert outer.value == [[42]]

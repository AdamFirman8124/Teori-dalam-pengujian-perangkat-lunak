# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_init_attributes():
    err = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)
    assert err.kind is list
    assert err.expected_kind is tuple
    assert isinstance(err, ISortError)
    assert isinstance(err, Exception)


def test_literal_sort_type_mismatch_message():
    err = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)
    expected = (
        f"isort was told to sort a literal of type {tuple} but was given "
        f"a literal of type {list}."
    )
    assert str(err) == expected
    assert err.args[0] == expected


def test_literal_sort_type_mismatch_raise_and_catch():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(kind=dict, expected_kind=set)
    err = exc_info.value
    assert err.kind is dict
    assert err.expected_kind is set
    assert "isort was told to sort a literal" in str(err)
    assert str(dict) in str(err)
    assert str(set) in str(err)

# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_message_and_attributes():
    exc = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert str(exc) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )
    assert exc.args == (str(exc),)
    assert exc.kind is list
    assert exc.expected_kind is dict


def test_literal_sort_type_mismatch_is_isort_error_and_raisable():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(kind=tuple, expected_kind=set)

    caught = excinfo.value
    assert isinstance(caught, ISortError)
    assert isinstance(caught, Exception)
    assert caught.kind is tuple
    assert caught.expected_kind is set
    assert "tuple" in str(caught)
    assert "set" in str(caught)

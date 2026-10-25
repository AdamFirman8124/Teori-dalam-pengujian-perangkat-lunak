# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_message_and_attributes():
    kind = list
    expected_kind = dict

    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    error = exc_info.value
    # Verify the exception message covers lines 114-117.
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )
    # Verify attributes are set (lines 118-119).
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    # Verify it is an ISortError (and therefore an Exception).
    assert isinstance(error, ISortError)

# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_message_and_attributes():
    kind = str
    expected_kind = list
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Verify the exception is an ISortError (and thus an Exception).
    assert isinstance(error, Exception)

    # Verify the formatted message produced by super().__init__ (lines 114-117).
    assert str(error) == (
        "isort was told to sort a literal of type <class 'list'> but was given "
        "a literal of type <class 'str'>."
    )

    # Verify the attributes assigned in __init__ (lines 118-119).
    assert error.kind is kind
    assert error.expected_kind is expected_kind


def test_literal_sort_type_mismatch_reversed_types():
    kind = dict
    expected_kind = tuple
    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'dict'>."
    )
    assert error.kind is dict
    assert error.expected_kind is tuple

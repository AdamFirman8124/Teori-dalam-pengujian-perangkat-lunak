# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_message_and_attributes():
    """Directly exercising LiteralSortTypeMismatch.__init__ (lines 114-119)."""
    kind = int
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    expected_message = (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )
    assert str(error) == expected_message
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    # Postcondition: it must remain a proper isort exception.
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_sort_type_mismatch_raised_and_caught():
    """Ensure the exception behaves correctly when raised and caught."""
    kind = str
    expected_kind = tuple

    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    error = exc_info.value
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )

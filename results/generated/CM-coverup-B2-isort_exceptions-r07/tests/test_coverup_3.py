# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_initialization():
    """Executing LiteralSortTypeMismatch.__init__ (lines 114-119) sets the
    message and stores both the actual and expected kinds."""
    kind = int
    expected_kind = str

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # The exception is properly initialized within the isort exception hierarchy.
    assert isinstance(error, LiteralSortTypeMismatch)
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Lines 114-117: the message built via super().__init__ is correct.
    assert str(error) == (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )

    # Lines 118-119: the attributes are stored on the instance.
    assert error.kind is kind
    assert error.expected_kind is expected_kind


def test_literal_sort_type_mismatch_raised_and_caught():
    """The exception can be raised and carries its data through pytest.raises."""
    kind = list
    expected_kind = dict

    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert excinfo.value.kind is kind
    assert excinfo.value.expected_kind is expected_kind
    assert str(excinfo.value) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

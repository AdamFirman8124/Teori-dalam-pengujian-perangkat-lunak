# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_message_and_attributes():
    kind = int
    expected_kind = list

    exc = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # The super().__init__ call (lines 114-117) must have stored the formatted message.
    expected_message = (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )
    assert str(exc) == expected_message
    assert exc.args == (expected_message,)

    # Lines 118-119: the attributes must be set on the instance.
    assert exc.kind is kind
    assert exc.expected_kind is expected_kind

    # Postcondition: it remains a proper isort/Exception subclass.
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_literal_sort_type_mismatch_raised_and_caught():
    kind = str
    expected_kind = dict

    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert excinfo.value.kind is kind
    assert excinfo.value.expected_kind is expected_kind
    assert str(excinfo.value) == (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )

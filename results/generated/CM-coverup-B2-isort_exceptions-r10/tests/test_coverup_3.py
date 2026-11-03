# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_initializes_message_and_attributes():
    kind = int
    expected_kind = str

    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(kind, expected_kind)

    error = excinfo.value

    # Attributes passed to the constructor are stored on the instance.
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # The exception is a subclass of the isort base error (and therefore Exception).
    assert isinstance(error, LiteralSortTypeMismatch)

    # The message was built by super().__init__ with both kinds interpolated.
    assert str(error) == (
        "isort was told to sort a literal of type <class 'str'> but was given "
        "a literal of type <class 'int'>."
    )

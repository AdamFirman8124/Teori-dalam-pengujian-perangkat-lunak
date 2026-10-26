# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_initializes_message_and_attributes():
    error = LiteralSortTypeMismatch(tuple, list)

    assert isinstance(error, LiteralSortTypeMismatch)
    assert str(error) == (
        "isort was told to sort a literal of type <class 'list'> but was given "
        "a literal of type <class 'tuple'>."
    )
    assert error.kind is tuple
    assert error.expected_kind is list

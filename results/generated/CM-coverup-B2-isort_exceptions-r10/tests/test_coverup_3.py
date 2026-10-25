# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_initializes_message_and_attributes():
    error = LiteralSortTypeMismatch(list, tuple)

    assert isinstance(error, ISortError)
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> "
        "but was given a literal of type <class 'list'>."
    )
    assert error.args == (str(error),)
    assert error.kind is list
    assert error.expected_kind is tuple

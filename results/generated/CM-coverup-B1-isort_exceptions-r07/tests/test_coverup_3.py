# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_initialization() -> None:
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind, expected_kind)

    expected_message = (
        "isort was told to sort a literal of type "
        "<class 'list'> but was given a literal of type <class 'dict'>."
    )
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.kind is kind
    assert error.expected_kind is expected_kind

# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_attributes_and_message():
    exc = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

    assert exc.kind is dict
    assert exc.expected_kind is list
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert str(exc) == (
        "isort was told to sort a literal of type <class 'list'> "
        "but was given a literal of type <class 'dict'>."
    )
    assert exc.args == (str(exc),)


def test_literal_sort_type_mismatch_raised_and_caught():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(list, dict)

    exc = exc_info.value
    assert exc.kind is list
    assert exc.expected_kind is dict
    assert str(exc) == (
        "isort was told to sort a literal of type <class 'dict'> "
        "but was given a literal of type <class 'list'>."
    )
    assert exc.args == (str(exc),)


@pytest.mark.parametrize(
    "kind,expected_kind",
    [
        (dict, list),
        (list, tuple),
        (set, dict),
        (str, list),
        (int, set),
    ],
)
def test_literal_sort_type_mismatch_parametrized(kind, expected_kind):
    exc = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert exc.kind is kind
    assert exc.expected_kind is expected_kind
    assert str(exc) == (
        f"isort was told to sort a literal of type {expected_kind} "
        f"but was given a literal of type {kind}."
    )
    assert exc.args == (str(exc),)

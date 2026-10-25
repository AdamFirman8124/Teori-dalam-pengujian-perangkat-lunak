# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

import pytest

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch():
    kind = list
    expected_kind = dict

    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    exception = exc_info.value
    assert exception.kind is kind
    assert exception.expected_kind is expected_kind
    assert str(exception) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

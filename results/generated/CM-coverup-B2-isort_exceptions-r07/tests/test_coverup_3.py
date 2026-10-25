# file: project/isort/exceptions.py:108-119
# asked: {"lines": [114, 115, 116, 118, 119], "branches": []}
# gained: {"lines": [114, 115, 116, 118, 119], "branches": []}

from isort.exceptions import ISortError, LiteralSortTypeMismatch


def test_literal_sort_type_mismatch_init_attributes():
    kind = list
    expected_kind = tuple
    exc = LiteralSortTypeMismatch(kind, expected_kind)
    assert exc.kind is list
    assert exc.expected_kind is tuple
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_literal_sort_type_mismatch_message():
    kind = list
    expected_kind = tuple
    exc = LiteralSortTypeMismatch(kind, expected_kind)
    expected_message = (
        f"isort was told to sort a literal of type {expected_kind} "
        f"but was given a literal of type {kind}."
    )
    assert str(exc) == expected_message
    assert exc.args == (expected_message,)


def test_literal_sort_type_mismatch_raised():
    try:
        raise LiteralSortTypeMismatch(dict, list)
    except LiteralSortTypeMismatch as exc:
        assert exc.kind is dict
        assert exc.expected_kind is list
        assert "dict" in str(exc)
        assert "list" in str(exc)
    else:
        raise AssertionError("LiteralSortTypeMismatch was not raised")


def test_literal_sort_type_mismatch_caught_as_isort_error():
    try:
        raise LiteralSortTypeMismatch(str, set)
    except ISortError as exc:
        assert isinstance(exc, LiteralSortTypeMismatch)
        assert exc.kind is str
        assert exc.expected_kind is set
    else:
        raise AssertionError("Expected ISortError was not raised")

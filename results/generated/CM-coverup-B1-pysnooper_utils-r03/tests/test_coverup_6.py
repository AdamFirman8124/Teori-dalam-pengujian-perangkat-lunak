# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_converts_non_string_iterable_to_tuple():
    assert ensure_tuple([1, 2, 3]) == (1, 2, 3)


def test_ensure_tuple_wraps_string_without_splitting_it():
    assert ensure_tuple("abc") == ("abc",)


def test_ensure_tuple_wraps_non_iterable():
    value = object()

    result = ensure_tuple(value)

    assert result == (value,)
    assert result[0] is value

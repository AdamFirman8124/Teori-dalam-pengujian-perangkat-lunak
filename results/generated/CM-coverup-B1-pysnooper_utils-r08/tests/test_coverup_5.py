# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_with_list_returns_tuple():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_tuple_returns_same_tuple():
    result = ensure_tuple((4, 5))
    assert result == (4, 5)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_string_wraps_in_tuple():
    result = ensure_tuple("hello")
    assert result == ("hello",)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_non_iterable_wraps_in_tuple():
    assert ensure_tuple(42) == (42,)
    assert ensure_tuple(None) == (None,)
    obj = object()
    result = ensure_tuple(obj)
    assert result == (obj,)
    assert isinstance(result, tuple)

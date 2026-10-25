# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_with_list_returns_tuple():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_tuple_returns_same_tuple():
    result = ensure_tuple((1, 2))
    assert result == (1, 2)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_generator_returns_tuple():
    result = ensure_tuple(x for x in [1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_string_returns_singleton():
    result = ensure_tuple("hello")
    assert result == ("hello",)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_non_iterable_int_returns_singleton():
    result = ensure_tuple(42)
    assert result == (42,)
    assert isinstance(result, tuple)


def test_ensure_tuple_with_none_returns_singleton():
    result = ensure_tuple(None)
    assert result == (None,)
    assert isinstance(result, tuple)

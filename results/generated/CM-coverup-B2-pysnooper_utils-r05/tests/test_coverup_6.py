# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_converts_non_string_iterable():
    value = [1, 2, 3]

    result = ensure_tuple(value)

    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_wraps_string():
    value = "abc"

    result = ensure_tuple(value)

    assert result == ("abc",)


def test_ensure_tuple_wraps_non_iterable():
    value = 42

    result = ensure_tuple(value)

    assert result == (42,)

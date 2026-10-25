# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

from pymonet.either import Left, Right


def test_left_ap_returns_left_with_same_value():
    left = Left("error")
    result = left.ap(Right(lambda x: x))
    assert isinstance(result, Left)
    assert result.value == "error"
    assert result == Left("error")


def test_left_ap_returns_copy_not_same_instance():
    left = Left("error")
    result = left.ap(Right(lambda x: x + 1))
    assert result is not left
    assert result.value == left.value
    assert left.value == "error"


def test_left_ap_ignores_left_argument():
    left = Left("original")
    other = Left("other")
    result = left.ap(other)
    assert isinstance(result, Left)
    assert result.value == "original"
    assert result == Left("original")


def test_left_ap_preserves_various_values():
    for value in [None, 0, 42, "", {"a": 1}, [1, 2, 3]]:
        left = Left(value)
        result = left.ap(Right(lambda x: x))
        assert isinstance(result, Left)
        assert result.value == value
        assert result == Left(value)
        assert result is not left

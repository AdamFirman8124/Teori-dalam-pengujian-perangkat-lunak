# file: project/pymonet/either.py:182-187
# asked: {"lines": [187], "branches": []}
# gained: {"lines": [187], "branches": []}

from pymonet.either import Left, Right


def test_right_is_left_returns_false():
    assert Right(42).is_left() is False


def test_right_is_left_returns_bool_false():
    result = Right(42).is_left()
    assert result == False
    assert isinstance(result, bool)


def test_right_is_left_with_various_values():
    assert Right(None).is_left() is False
    assert Right("hello").is_left() is False
    assert Right([1, 2, 3]).is_left() is False
    assert Right({"key": "value"}).is_left() is False


def test_right_is_left_consistent_with_is_right():
    right = Right(10)
    assert right.is_left() is False
    assert right.is_right() is True
    assert not right.is_left()


def test_right_is_left_does_not_mutate_value():
    right = Right(99)
    assert right.is_left() is False
    assert right.value == 99
    assert right.is_left() is False

# file: project/pymonet/either.py:81-82
# asked: {"lines": [82], "branches": []}
# gained: {"lines": [82], "branches": []}

from pymonet.either import Either


def test_either_is_right_executes():
    instance = Either(42)
    result = instance.is_right()
    assert result is None
    assert instance.value == 42


def test_either_is_right_executes_with_different_value():
    instance = Either("hello")
    assert instance.is_right() is None
    assert instance.value == "hello"

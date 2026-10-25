# file: project/pymonet/either.py:153-162
# asked: {"lines": [162], "branches": []}
# gained: {"lines": [162], "branches": []}

from pymonet.either import Right


def test_right_map_applies_mapper_and_returns_new_right():
    original = Right(21)

    result = original.map(lambda value: value * 2)

    assert isinstance(result, Right)
    assert result.value == 42
    assert result is not original
    assert original.value == 21

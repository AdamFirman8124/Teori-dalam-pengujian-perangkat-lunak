# file: project/pymonet/either.py:153-162
# asked: {"lines": [162], "branches": []}
# gained: {"lines": [162], "branches": []}

from pymonet.either import Right


def test_right_map_executes_line_162_basic():
    result = Right(1).map(lambda x: x + 1)
    assert isinstance(result, Right)
    assert result.value == 2
    assert result.is_right() is True
    assert result.is_left() is False


def test_right_map_applies_mapper_to_value():
    seen = []

    def mapper(x):
        seen.append(x)
        return x * 10

    result = Right(5).map(mapper)
    assert seen == [5]
    assert isinstance(result, Right)
    assert result.value == 50


def test_right_map_returns_new_right_with_mapped_type():
    original = Right("hello")
    result = original.map(str.upper)
    assert result.value == "HELLO"
    assert isinstance(result, Right)
    # original is unchanged
    assert original.value == "hello"
    assert result is not original

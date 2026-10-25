# file: project/pymonet/either.py:153-162
# asked: {"lines": [162], "branches": []}
# gained: {"lines": [162], "branches": []}

from pymonet.either import Right


def test_right_map_returns_new_right_with_mapped_value():
    right = Right(2)

    result = right.map(lambda x: x * 3)

    assert isinstance(result, Right)
    assert result is not right
    assert result.value == 6
    assert right.value == 2


def test_right_map_with_identity_preserves_value():
    right = Right('abc')

    result = right.map(lambda x: x)

    assert isinstance(result, Right)
    assert result.value == 'abc'


def test_right_map_changes_type():
    right = Right(5)

    result = right.map(str)

    assert isinstance(result, Right)
    assert result.value == '5'

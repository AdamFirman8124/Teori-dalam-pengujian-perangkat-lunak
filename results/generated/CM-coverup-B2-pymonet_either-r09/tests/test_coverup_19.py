# file: project/pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

from pymonet.either import Right, Left


def test_right_bind_calls_mapper_with_value():
    right = Right(42)
    result = right.bind(lambda value: value + 1)
    assert result == 43


def test_right_bind_returns_mapper_result_object():
    right = Right('abc')
    result = right.bind(lambda value: Right(value.upper()))
    assert isinstance(result, Right)
    assert result.value == 'ABC'


def test_right_bind_mapper_receives_exact_value():
    right = Right([1, 2, 3])
    captured = []

    def mapper(value):
        captured.append(value)
        return len(value)

    result = right.bind(mapper)
    assert result == 3
    assert captured == [[1, 2, 3]]


def test_right_bind_does_not_mutate_right(monkeypatch):
    right = Right(7)
    result = right.bind(lambda value: value * 2)
    assert result == 14
    assert right.value == 7


def test_right_bind_with_left_mapper_result():
    right = Right(0)
    result = right.bind(lambda value: Left('error'))
    assert isinstance(result, Left)
    assert result.value == 'error'

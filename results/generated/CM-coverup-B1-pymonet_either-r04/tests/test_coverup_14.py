# file: project/pymonet/either.py:97-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from pymonet.either import Left


def test_left_bind_returns_self():
    left = Left(42)

    result = left.bind(lambda x: x + 1)

    assert result is left
    assert isinstance(result, Left)
    assert result.value == 42


def test_left_bind_ignores_mapper():
    calls = []

    def mapper(value):
        calls.append(value)
        return value

    left = Left('error')

    result = left.bind(mapper)

    assert result is left
    assert result.value == 'error'
    assert calls == []

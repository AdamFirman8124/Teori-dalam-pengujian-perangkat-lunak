# file: project/pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

from pymonet.either import Right


def test_right_bind_calls_mapper_with_value_and_returns_result():
    value = object()
    expected = object()
    received = []

    def mapper(argument):
        received.append(argument)
        return expected

    result = Right(value).bind(mapper)

    assert result is expected
    assert received == [value]

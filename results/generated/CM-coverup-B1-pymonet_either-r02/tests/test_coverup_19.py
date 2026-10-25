# file: project/pymonet/either.py:164-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

import pytest

from pymonet.either import Right


def test_right_bind_applies_mapper_to_value():
    """Right.bind should call mapper with the wrapped value and return its result."""
    right = Right(42)

    result = right.bind(lambda value: value + 1)

    assert result == 43


def test_right_bind_returns_mapper_result_unchanged():
    """Right.bind should return exactly what mapper returns, even a non-Either value."""
    right = Right("abc")

    sentinel = object()
    result = right.bind(lambda value: sentinel)

    assert result is sentinel


def test_right_bind_receives_wrapped_value():
    """Right.bind should pass the wrapped value itself to the mapper."""
    right = Right((1, 2))
    received = {}

    def mapper(value):
        received["value"] = value
        return value[0] + value[1]

    result = right.bind(mapper)

    assert received["value"] == (1, 2)
    assert result == 3

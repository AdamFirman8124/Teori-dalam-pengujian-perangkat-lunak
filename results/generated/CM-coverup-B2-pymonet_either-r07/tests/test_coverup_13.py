# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

import pytest

from pymonet.either import Left


def test_left_map_returns_new_left_with_same_value():
    """Left.map must return a new Left instance holding the same value,
    ignoring the mapper function entirely (covers line 95)."""
    left = Left("error")
    mapper_calls = []

    def mapper(value):
        mapper_calls.append(value)
        return "transformed"

    result = left.map(mapper)

    # Postconditions: new Left instance, same value, mapper not invoked.
    assert isinstance(result, Left)
    assert result is not left
    assert result.value == "error"
    assert mapper_calls == []

# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

from unittest.mock import Mock

from pymonet.either import Left


def test_left_map_returns_new_left_without_calling_mapper():
    value = object()
    mapper = Mock(side_effect=AssertionError("mapper must not be called"))
    left = Left(value)

    result = left.map(mapper)

    assert isinstance(result, Left)
    assert result is not left
    assert result.value is value
    assert left.value is value
    mapper.assert_not_called()

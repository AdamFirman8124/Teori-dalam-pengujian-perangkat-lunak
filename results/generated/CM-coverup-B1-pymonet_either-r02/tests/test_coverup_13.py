# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

from pymonet.either import Left


def test_left_map_returns_new_left_with_same_value_without_calling_mapper():
    value = object()
    left = Left(value)

    def mapper(_):
        raise AssertionError("Left.map must not call the mapper")

    result = left.map(mapper)

    assert isinstance(result, Left)
    assert result is not left
    assert result.value is value

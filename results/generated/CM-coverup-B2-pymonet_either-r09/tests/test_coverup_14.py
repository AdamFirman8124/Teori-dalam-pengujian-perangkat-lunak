# file: project/pymonet/either.py:97-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from pymonet.either import Left


def test_left_bind_returns_self_and_ignores_mapper():
    """Left.bind must execute line 104: return self, ignoring the mapper."""
    left = Left("error value")

    def mapper(value):
        raise AssertionError("mapper should never be called on Left.bind")

    result = left.bind(mapper)

    # Postcondition: bind returns the very same instance (line 104)
    assert result is left
    # Postcondition: stored value is unchanged
    assert result.value == "error value"
    # Postcondition: still a Left
    assert isinstance(result, Left)
    assert result.is_left() is True
    assert result.is_right() is False

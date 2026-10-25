# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

from pymonet.either import Left


def test_left_map_returns_new_left_with_same_value():
    original = Left("error")
    result = original.map(lambda x: "transformed")

    assert isinstance(result, Left)
    assert result.value == "error"
    assert result == Left("error")
    assert result is not original
    assert result.is_left() is True
    assert result.is_right() is False


def test_left_map_does_not_invoke_mapper():
    calls = []

    def mapper(x):
        calls.append(x)
        return "should not be used"

    original = Left(42)
    result = original.map(mapper)

    assert calls == []
    assert isinstance(result, Left)
    assert result.value == 42
    assert result == Left(42)
    assert result is not original

# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

from pymonet.either import Left


def test_left_map_returns_new_left_without_calling_mapper():
    value = object()
    calls = []

    def mapper(item):
        calls.append(item)
        raise AssertionError("Left.map must not call the mapper")

    original = Left(value)
    result = original.map(mapper)

    assert isinstance(result, Left)
    assert result is not original
    assert result.value is value
    assert calls == []

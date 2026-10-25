# file: project/pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

from pymonet.either import Left


def test_left_map_returns_new_left_without_calling_mapper():
    original = Left("error")
    mapper_calls = []

    def mapper(value):
        mapper_calls.append(value)
        return "mapped"

    result = original.map(mapper)

    assert isinstance(result, Left)
    assert result is not original
    assert result.value == "error"
    assert original.value == "error"
    assert mapper_calls == []

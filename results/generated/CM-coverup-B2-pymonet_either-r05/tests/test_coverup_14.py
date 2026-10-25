# file: project/pymonet/either.py:97-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from pymonet.either import Left


def test_left_bind_returns_same_instance_without_calling_mapper():
    left = Left("error")

    def mapper(_):
        raise AssertionError("Left.bind must not call the mapper")

    result = left.bind(mapper)

    assert result is left
    assert result.value == "error"

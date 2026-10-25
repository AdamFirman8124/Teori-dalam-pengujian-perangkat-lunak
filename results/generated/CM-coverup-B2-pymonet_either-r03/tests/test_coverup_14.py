# file: project/pymonet/either.py:97-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from pymonet.either import Left


def test_left_bind_returns_same_instance():
    left = Left("error")

    result = left.bind(lambda value: value)

    assert result is left
    assert result.value == "error"

# file: project/pymonet/either.py:153-162
# asked: {"lines": [162], "branches": []}
# gained: {"lines": [162], "branches": []}

from pymonet.either import Right


def test_right_map_executes_line_162():
    """Right.map should apply the mapper to its value and return a new Right."""
    right = Right(10)

    result = right.map(lambda x: x * 2)

    assert isinstance(result, Right)
    assert result is not right
    assert result.value == 20

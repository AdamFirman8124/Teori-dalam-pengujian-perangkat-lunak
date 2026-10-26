# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.5, 1.0]
    # verify input not mutated (no state pollution)
    assert numbers == [1.0, 2.0, 3.0]


def test_rescale_to_unit_negative_and_float():
    numbers = [-1.0, 0.0, 1.0, 2.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0]
    assert min(result) == 0.0
    assert max(result) == 1.0

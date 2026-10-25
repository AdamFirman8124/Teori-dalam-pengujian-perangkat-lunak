# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f021 import rescale_to_unit


def test_rescale_to_unit_scales_values_without_mutating_input():
    numbers = [2.0, 4.0, 6.0]

    result = rescale_to_unit(numbers)

    assert result == [0.0, 0.5, 1.0]
    assert numbers == [2.0, 4.0, 6.0]

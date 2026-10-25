# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f021 import rescale_to_unit


def test_rescale_to_unit_scales_values_without_mutating_input():
    numbers = [10.0, -10.0, 0.0, 5.0]
    original = numbers.copy()

    result = rescale_to_unit(numbers)

    assert result == [1.0, 0.0, 0.5, 0.75]
    assert numbers == original
    assert min(result) == 0.0
    assert max(result) == 1.0

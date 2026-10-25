# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_scales_values_and_preserves_input():
    numbers = [-5.0, 0.0, 5.0]
    original = numbers.copy()

    result = rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 0.5, 1.0])
    assert numbers == original

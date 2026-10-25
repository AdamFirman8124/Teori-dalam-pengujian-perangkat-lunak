# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest
from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    assert result == pytest.approx([0.0, 0.5, 1.0])
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)
    # verify original input is unchanged (no state pollution)
    assert numbers == [1.0, 2.0, 3.0]


def test_rescale_to_unit_negative_range():
    result = rescale_to_unit([-10.0, 0.0, 10.0])
    assert result == pytest.approx([0.0, 0.5, 1.0])

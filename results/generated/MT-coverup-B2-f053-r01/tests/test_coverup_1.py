# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (1, 2, 3),
        (-5, 5, 0),
        (0, 0, 0),
        (100, 250, 350),
    ],
)
def test_add_returns_sum_of_operands(x, y, expected):
    """Calling add must execute its body (line 3) and return x + y."""
    result = add(x, y)

    # Postcondition: the returned value equals the sum of the operands.
    assert result == expected
    assert isinstance(result, int)


def test_add_with_float_inputs():
    """Exercise add with non-int numeric inputs to hit line 3 again."""
    result = add(1.5, 2.5)

    # Postcondition: floats are summed correctly.
    assert result == 4.0
    assert isinstance(result, float)

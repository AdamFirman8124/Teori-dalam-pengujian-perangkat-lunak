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

    assert result == expected
    # Postcondition: result equals the sum of both operands.
    assert result == x + y

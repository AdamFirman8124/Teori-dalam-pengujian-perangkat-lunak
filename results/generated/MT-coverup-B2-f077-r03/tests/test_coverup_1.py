# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, True),        # zero cube: 0 ** (1/3) -> 0, 0**3 == 0
        (1, True),        # smallest positive cube
        (8, True),        # 2**3
        (27, True),       # 3**3
        (64, True),       # 4**3 (rounding of 3.9999... must still work)
        (-1, True),       # abs() on line 3 handles negatives
        (-27, True),      # negative perfect cube
        (2, False),       # not a cube
        (9, False),       # not a cube
        (-2, False),      # negative non-cube (abs then compare)
        (-9, False),      # negative non-cube
    ],
)
def test_iscube_executes_body_and_branches(value, expected):
    """Calling iscube executes lines 3-4 for both cube and non-cube inputs."""
    result = iscube(value)
    assert result is expected
    # Postcondition: result is a genuine boolean comparison outcome
    assert isinstance(result, bool)
    # Postcondition: a value is a cube iff its absolute value is a perfect cube
    root = int(round(abs(value) ** (1.0 / 3)))
    assert result == (root ** 3 == abs(value))

# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        # Zero and positive perfect cubes -> True
        (0, True),
        (1, True),
        (8, True),
        (27, True),
        # 64 ** (1/3) evaluates to ~3.9999999999999996, exercising the
        # rounding branch before cubing.
        (64, True),
        (125, True),
        # Negative perfect cubes -> True (exercises the abs() conversion).
        (-1, True),
        (-8, True),
        (-27, True),
        (-64, True),
        # Non-cubes -> False
        (2, False),
        (-2, False),
        (9, False),
        (63, False),
        (100, False),
    ],
)
def test_iscube_integers(value, expected):
    """Execute lines 3-4 for integer inputs and verify the postcondition."""
    result = iscube(value)

    # Postcondition: result is a proper boolean matching the expectation,
    # i.e. value is a perfect cube iff int(round(cbrt(|value|)))**3 == |value|.
    assert isinstance(result, bool)
    assert result is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (8.0, True),
        (-8.0, True),
        (27.0, True),
        (2.5, False),
        (-3.3, False),
    ],
)
def test_iscube_floats(value, expected):
    """Execute lines 3-4 for float inputs and verify the postcondition."""
    result = iscube(value)

    assert isinstance(result, bool)
    assert result is expected

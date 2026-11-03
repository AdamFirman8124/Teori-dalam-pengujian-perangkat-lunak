# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


@pytest.mark.parametrize(
    "value, expected",
    [
        # Perfect cubes, including zero and negatives (exercises abs() on line 3
        # and the True outcome of the comparison on line 4)
        (0, True),
        (1, True),
        (8, True),
        (27, True),
        (64, True),
        (125, True),
        (-1, True),
        (-8, True),
        (-27, True),
        # Non-cubes (exercises the False outcome of the comparison on line 4)
        (2, False),
        (3, False),
        (7, False),
        (9, False),
        (26, False),
        (-2, False),
        (-9, False),
    ],
)
def test_iscube(value, expected):
    result = iscube(value)
    assert isinstance(result, bool)
    assert result is expected

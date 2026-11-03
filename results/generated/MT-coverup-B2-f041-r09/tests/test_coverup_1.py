# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 4),
        (5, 25),
        (-3, 9),
        (10, 100),
    ],
)
def test_car_race_collision_returns_square(n, expected):
    """car_race_collision must return n squared (line 3 executes on call)."""
    result = car_race_collision(n)
    assert result == expected
    assert result == n ** 2


def test_car_race_collision_large_value():
    """Verify correctness for a larger input as well."""
    n = 1234
    assert car_race_collision(n) == n * n

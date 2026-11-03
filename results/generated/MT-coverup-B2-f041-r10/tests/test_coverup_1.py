# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


def test_car_race_collision_executes_return_line():
    """Calling the function ensures line 3 (`return n**2`) executes."""
    # Positive integer
    assert car_race_collision(3) == 9
    # Zero
    assert car_race_collision(0) == 0
    # Negative integer (squared is positive)
    assert car_race_collision(-4) == 16
    # Large value sanity check
    assert car_race_collision(10) == 100

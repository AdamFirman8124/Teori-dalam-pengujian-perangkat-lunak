# file: script_41.py:1-13
# asked: {"lines": [13], "branches": []}
# gained: {"lines": [13], "branches": []}

import pytest
from script_41 import car_race_collision


def test_car_race_collision_zero():
    """Test with zero cars - no collisions possible."""
    assert car_race_collision(0) == 0


def test_car_race_collision_one():
    """Test with one car in each direction - exactly one collision."""
    assert car_race_collision(1) == 1


def test_car_race_collision_multiple():
    """Test with multiple cars - each left-to-right car collides with each right-to-left car."""
    assert car_race_collision(2) == 4
    assert car_race_collision(3) == 9
    assert car_race_collision(5) == 25
    assert car_race_collision(10) == 100

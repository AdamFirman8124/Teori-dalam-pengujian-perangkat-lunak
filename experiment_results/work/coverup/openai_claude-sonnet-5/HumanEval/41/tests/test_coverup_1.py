# file: script_41.py:1-13
# asked: {"lines": [13], "branches": []}
# gained: {"lines": [13], "branches": []}

import pytest
from script_41 import car_race_collision


def test_car_race_collision_zero_cars():
    """Test with zero cars - should return 0 collisions."""
    assert car_race_collision(0) == 0


def test_car_race_collision_one_car():
    """Test with one car in each direction - should return 1 collision."""
    assert car_race_collision(1) == 1


def test_car_race_collision_two_cars():
    """Test with two cars in each direction - should return 4 collisions."""
    assert car_race_collision(2) == 4


def test_car_race_collision_five_cars():
    """Test with five cars in each direction - should return 25 collisions."""
    assert car_race_collision(5) == 25


def test_car_race_collision_ten_cars():
    """Test with ten cars in each direction - should return 100 collisions."""
    assert car_race_collision(10) == 100


def test_car_race_collision_large_number():
    """Test with a larger number of cars."""
    assert car_race_collision(100) == 10000

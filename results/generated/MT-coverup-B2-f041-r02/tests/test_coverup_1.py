# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


def test_car_race_collision_positive():
    """Calling with a positive integer executes line 3 (return n ** 2)."""
    result = car_race_collision(5)
    assert result == 25


def test_car_race_collision_zero():
    """Zero input still executes the return statement."""
    result = car_race_collision(0)
    assert result == 0


def test_car_race_collision_negative():
    """Negative input also exercises the return statement."""
    result = car_race_collision(-3)
    assert result == 9


def test_car_race_collision_large():
    """Large input verifies the squaring behavior on line 3."""
    result = car_race_collision(10**6)
    assert result == 10**12


def test_car_race_collision_returns_int():
    """The return value is an int, confirming line 3 executed."""
    result = car_race_collision(7)
    assert isinstance(result, int)
    assert result == 49

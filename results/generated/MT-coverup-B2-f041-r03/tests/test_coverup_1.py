# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


def test_car_race_collision_positive():
    """Calling the function executes line 3 (return n**2) for a positive n."""
    result = car_race_collision(3)
    assert result == 9


def test_car_race_collision_zero():
    """Edge case: n == 0 still executes the return statement."""
    result = car_race_collision(0)
    assert result == 0


def test_car_race_collision_negative():
    """Negative n also exercises the return statement (squaring makes it positive)."""
    result = car_race_collision(-4)
    assert result == 16


def test_car_race_collision_large():
    """Large input verifies the squaring behavior without overflow issues."""
    result = car_race_collision(10**6)
    assert result == 10**12

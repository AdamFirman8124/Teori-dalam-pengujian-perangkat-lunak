# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


def test_car_race_collision_returns_square():
    assert car_race_collision(3) == 9
    assert car_race_collision(0) == 0
    assert car_race_collision(-2) == 4

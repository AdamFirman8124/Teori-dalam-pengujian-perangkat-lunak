# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


def test_car_race_collision_executes_return():
    # Exercise line 3 (the return statement) with several inputs and
    # verify the postcondition: the result is n squared.
    assert car_race_collision(3) == 9
    assert car_race_collision(0) == 0
    assert car_race_collision(1) == 1
    assert car_race_collision(-2) == 4
    assert car_race_collision(10) == 100

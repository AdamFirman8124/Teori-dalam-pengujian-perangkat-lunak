# file: project/f041/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f041 import car_race_collision


@pytest.mark.parametrize("n", [0, 1, 2, 3, 10, 1000])
def test_car_race_collision_returns_square(n):
    result = car_race_collision(n)
    assert result == n ** 2
    assert isinstance(result, int)
    assert result >= 0


def test_car_race_collision_zero():
    assert car_race_collision(0) == 0


def test_car_race_collision_negative():
    # Postcondition: squaring makes any integer input non-negative.
    result = car_race_collision(-7)
    assert result == 49
    assert result >= 0


def test_car_race_collision_is_pure_and_repeatable():
    first = car_race_collision(12)
    second = car_race_collision(12)
    assert first == second == 144


def test_car_race_collision_large_value():
    n = 10 ** 6
    assert car_race_collision(n) == 10 ** 12

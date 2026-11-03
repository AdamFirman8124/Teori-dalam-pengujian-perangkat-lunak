

# Generated at 2026-11-01 23:51:01.563945
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic positive integer cases
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000

    # Larger values
    assert module_0.car_race_collision(1000) == 1000000

    # Negative inputs (n cars in each direction, magnitude squared)
    assert module_0.car_race_collision(-1) == 1
    assert module_0.car_race_collision(-5) == 25

    # Verify return type is int
    assert isinstance(module_0.car_race_collision(4), int)

    # Verify result equals n raised to power 2 for a range of values
    for n in range(-20, 21):
        assert module_0.car_race_collision(n) == n ** 2

    print("All tests passed!")

# Generated at 2026-11-01 23:52:09.762167
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic cases
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9

    # Larger values
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000

    # Each pair of cars (one from each direction) collides exactly once,
    # so total collisions should always be n squared.
    for n in range(0, 50):
        assert module_0.car_race_collision(n) == n * n

# Generated at 2026-11-01 23:53:48.271392
# Unit test for function car_race_collision
def test_car_race_collision():
    # Edge case: no cars means no collisions
    assert module_0.car_race_collision(0) == 0

    # One car from each direction results in exactly one collision
    assert module_0.car_race_collision(1) == 1

    # Small inputs
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(5) == 25

    # Larger inputs
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000

    # Property check: result equals n squared over a range of inputs
    for n in range(50):
        assert module_0.car_race_collision(n) == n ** 2

# Generated at 2026-11-01 23:55:45.396187
# Unit test for function car_race_collision
def test_car_race_collision():import unittest


class TestCarRaceCollision(unittest.TestCase):
    def test_car_race_collision(self):
        self.assertEqual(module_0.car_race_collision(0), 0)
        self.assertEqual(module_0.car_race_collision(1), 1)
        self.assertEqual(module_0.car_race_collision(2), 4)
        self.assertEqual(module_0.car_race_collision(3), 9)
        self.assertEqual(module_0.car_race_collision(10), 100)
        self.assertEqual(module_0.car_race_collision(100), 10000)
        self.assertEqual(module_0.car_race_collision(-3), 9)
        self.assertTrue(isinstance(module_0.car_race_collision(5), int))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 23:56:53.309987
# Unit test for function car_race_collision
def test_car_race_collision():
    # Each of the n cars moving left collides with each of the n cars moving right,
    # so the total number of collisions is n squared.
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(5) == 25
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000
    # Large input check
    assert module_0.car_race_collision(1000) == 1000000
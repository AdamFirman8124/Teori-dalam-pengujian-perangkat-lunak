

# Generated at 2026-11-02 18:08:32.666528
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic positive cases
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(10) == 100

    # Larger values
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Symmetry: negative input behaves like positive (squared)
    assert module_0.car_race_collision(-3) == 9
    assert module_0.car_race_collision(-10) == 100

    # Result is always non-negative and a perfect square
    for n in range(0, 50):
        result = module_0.car_race_collision(n)
        assert result == n * n
        assert result >= 0
        assert int(result ** 0.5) ** 2 == result

    # Type check: returns an int for int input
    assert isinstance(module_0.car_race_collision(5), int)

    print("All tests passed!")

# Generated at 2026-11-02 18:09:51.653931
# Unit test for function car_race_collision
def test_car_race_collision():
    # Test with zero cars
    assert module_0.car_race_collision(0) == 0

    # Test with one car
    assert module_0.car_race_collision(1) == 1

    # Test with small positive numbers
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(5) == 25
    assert module_0.car_race_collision(10) == 100

    # Test with larger numbers
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Test with very large number
    assert module_0.car_race_collision(10**6) == 10**12

    # Test that result is always non-negative for non-negative input
    for n in range(0, 50):
        assert module_0.car_race_collision(n) >= 0

    # Test result equals n squared property
    for n in range(0, 100):
        assert module_0.car_race_collision(n) == n * n

# Generated at 2026-11-02 18:10:36.329758
# Unit test for function car_race_collision
def test_car_race_collision():
    # Edge case: no cars means no collisions
    assert module_0.car_race_collision(0) == 0

    # Single pair of cars
    assert module_0.car_race_collision(1) == 1

    # Small values
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(4) == 16
    assert module_0.car_race_collision(5) == 25

    # Larger values
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Property check: result equals n * n for a range of inputs
    for n in range(0, 50):
        assert module_0.car_race_collision(n) == n * n

    # Property check: monotonic growth
    prev = module_0.car_race_collision(0)
    for n in range(1, 100):
        current = module_0.car_race_collision(n)
        assert current > prev
        prev = current

# Generated at 2026-11-02 18:11:34.644497
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic positive cases
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(10) == 100

    # Larger values
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Negative values (squared, so positive result)
    assert module_0.car_race_collision(-1) == 1
    assert module_0.car_race_collision(-5) == 25

    # Large number sanity check
    assert module_0.car_race_collision(10**6) == 10**12


def test_car_race_collision_returns_int():
    result = module_0.car_race_collision(7)
    assert isinstance(result, int)


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (5, 25),
    (-3, 9),
    (12, 144),
])
def test_car_race_collision_parametrized(n, expected):
    assert module_0.car_race_collision(n) == expected

# Generated at 2026-11-02 18:12:21.739205
# Unit test for function car_race_collision
def test_car_race_collision():
    # Base cases
    assert module_0.car_race_collision(0) == 0
    assert module_0.car_race_collision(1) == 1

    # Typical cases
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(5) == 25
    assert module_0.car_race_collision(10) == 100

    # Larger values
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Negative input still squares to a positive result
    assert module_0.car_race_collision(-3) == 9
    assert module_0.car_race_collision(-5) == 25

    print("All tests passed!")


if __name__ == "__main__":
    test_car_race_collision()
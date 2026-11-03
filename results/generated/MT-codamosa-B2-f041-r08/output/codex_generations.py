

# Generated at 2026-11-02 22:04:52.262790
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic positive cases
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(10) == 100

    # Zero case
    assert module_0.car_race_collision(0) == 0

    # Larger values
    assert module_0.car_race_collision(100) == 10000
    assert module_0.car_race_collision(1000) == 1000000

    # Negative inputs (squared result is positive)
    assert module_0.car_race_collision(-1) == 1
    assert module_0.car_race_collision(-5) == 25

    # Property check: result equals n * n for a range of values
    for n in range(0, 50):
        assert module_0.car_race_collision(n) == n * n

    # Property check: result is always non-negative
    for n in range(-10, 10):
        assert module_0.car_race_collision(n) >= 0

    print("All test_car_race_collision tests passed!")


if __name__ == "__main__":
    test_car_race_collision()

# Generated at 2026-11-02 22:08:17.396564
# Unit test for function car_race_collision
def test_car_race_collision():
    # Zero cars means zero collisions
    assert module_0.car_race_collision(0) == 0

    # Single car from each direction -> one collision
    assert module_0.car_race_collision(1) == 1

    # Two cars from each direction -> four collisions
    assert module_0.car_race_collision(2) == 4

    # Three cars from each direction -> nine collisions
    assert module_0.car_race_collision(3) == 9

    # Larger input
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000

    # Very large input to check for overflow-free integer math
    assert module_0.car_race_collision(1000000) == 1000000000000

    # Result must always be a perfect square of the input
    for n in range(1, 20):
        result = module_0.car_race_collision(n)
        assert result == n * n
        assert int(result ** 0.5) == n

# Generated at 2026-11-02 22:10:13.905207
# Unit test for function car_race_collision
def test_car_race_collision():
    # Single pair of cars -> exactly 1 collision
    assert module_0.car_race_collision(1) == 1

    # Two cars in each direction -> 4 collisions
    assert module_0.car_race_collision(2) == 4

    # Three cars in each direction -> 9 collisions
    assert module_0.car_race_collision(3) == 9

    # No cars -> no collisions
    assert module_0.car_race_collision(0) == 0

    # Larger input
    assert module_0.car_race_collision(10) == 100
    assert module_0.car_race_collision(100) == 10000

    # Verify result is always a perfect square of n
    for n in range(0, 50):
        assert module_0.car_race_collision(n) == n * n

    # Result type check
    assert isinstance(module_0.car_race_collision(5), int)

    print("All tests passed!")


if __name__ == "__main__":
    test_car_race_collision()

# Generated at 2026-11-02 22:12:26.471773
# Unit test for function car_race_collision
def test_car_race_collision():
    # Basic positive cases
    assert module_0.car_race_collision(1) == 1
    assert module_0.car_race_collision(2) == 4
    assert module_0.car_race_collision(3) == 9
    assert module_0.car_race_collision(10) == 100

    # Zero cars on each side -> zero collisions
    assert module_0.car_race_collision(0) == 0

    # Large input
    assert module_0.car_race_collision(1000) == 1_000_000

    # Negative input still yields a positive square
    assert module_0.car_race_collision(-3) == 9
    assert module_0.car_race_collision(-10) == 100

    # Property check: result equals n squared for a range of inputs
    for n in range(0, 50):
        assert module_0.car_race_collision(n) == n ** 2

    # Symmetry: collisions(n) == collisions(-n)
    for n in range(1, 20):
        assert module_0.car_race_collision(n) == module_0.car_race_collision(-n)

    # Result is always non-negative
    for n in range(-100, 101):
        assert module_0.car_race_collision(n) >= 0
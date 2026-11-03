

# Generated at 2026-11-02 22:45:38.619207
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Test with a simple list of numbers
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]) - 2.0 / 3.0) < 1e-9

    # Test with a list where MAD is a whole number
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-9

    # Test with a single element list (deviation is zero)
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Test with all identical elements (deviation is zero)
    assert module_0.mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0

    # Test with negative numbers
    assert abs(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) - 2.0 / 3.0) < 1e-9

    # Test with mixed positive and negative numbers
    assert abs(module_0.mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]) - 1.5) < 1e-9

    # Test with floating point values
    assert abs(module_0.mean_absolute_deviation([0.5, 1.5, 2.5, 3.5]) - 1.0) < 1e-9

    # Test with a list of many elements
    numbers = [float(i) for i in range(100)]
    expected = sum(abs(x - 49.5) for x in numbers) / 100
    assert abs(module_0.mean_absolute_deviation(numbers) - expected) < 1e-9

    # Verify result is always non-negative
    assert module_0.mean_absolute_deviation([3.7, -8.2, 1.1, 9.9]) >= 0.0


if __name__ == "__main__":
    test_mean_absolute_deviation()
    print("All tests passed!")

# Generated at 2026-11-02 22:47:40.737383
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]) - 2.0 / 3.0) < 1e-9

    # Even-length list
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-9

    # Single element -> zero deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Identical elements -> zero deviation
    assert module_0.mean_absolute_deviation([7.0, 7.0, 7.0]) == 0.0

    # Negative numbers
    assert abs(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) - 2.0 / 3.0) < 1e-9

    # Symmetric around zero
    assert abs(module_0.mean_absolute_deviation([-1.0, 1.0]) - 1.0) < 1e-9

    # Zeros
    assert module_0.mean_absolute_deviation([0.0, 0.0]) == 0.0

    # Floats with decimals
    assert abs(module_0.mean_absolute_deviation([1.5, 2.5]) - 0.5) < 1e-9

    # Result is always non-negative
    assert module_0.mean_absolute_deviation([3.0, -3.0, 10.0]) >= 0.0

    print("All tests passed!")


if __name__ == "__main__":
    test_mean_absolute_deviation()

# Generated at 2026-11-02 22:48:53.271467
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case with even distribution
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)

    # All identical values -> deviation is zero
    assert module_0.mean_absolute_deviation([1.0, 1.0, 1.0]) == pytest.approx(0.0)

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0]) == pytest.approx(0.0)

    # Values with negative numbers
    assert module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) == pytest.approx(2.0 / 3.0)

    # Symmetric values around zero
    assert module_0.mean_absolute_deviation([-2.0, 2.0]) == pytest.approx(2.0)

    # Non-uniform spread
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx(1.2)

    # Result must be non-negative for arbitrary data
    assert module_0.mean_absolute_deviation([3.7, -2.1, 9.4, 0.5]) >= 0.0

# Generated at 2026-11-02 22:50:18.640988
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: evenly spaced numbers
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)

    # Two elements
    assert module_0.mean_absolute_deviation([1.0, 2.0]) == pytest.approx(0.5)

    # All identical values -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == pytest.approx(0.0)

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([42.0]) == pytest.approx(0.0)

    # All zeros
    assert module_0.mean_absolute_deviation([0.0, 0.0, 0.0]) == pytest.approx(0.0)

    # Negative numbers
    assert module_0.mean_absolute_deviation([-1.0, -2.0, -3.0]) == pytest.approx(2.0 / 3.0)

    # Mixed positive and negative values
    assert module_0.mean_absolute_deviation([-2.0, 2.0]) == pytest.approx(2.0)

    # Fractional values
    assert module_0.mean_absolute_deviation([1.5, 2.5, 3.5]) == pytest.approx(2.0 / 3.0)

    # Verify symmetry: deviation is invariant under adding a constant
    base = module_0.mean_absolute_deviation([1.0, 2.0, 3.0])
    shifted = module_0.mean_absolute_deviation([11.0, 12.0, 13.0])
    assert base == pytest.approx(shifted)

# Generated at 2026-11-02 22:51:58.874424
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: evenly spaced numbers
    result = module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert math.isclose(result, 1.0), f"Expected 1.0, got {result}"

    # Symmetric values around zero
    result = module_0.mean_absolute_deviation([-1.0, 0.0, 1.0])
    assert math.isclose(result, 2.0 / 3.0), f"Expected {2.0/3.0}, got {result}"

    # Single element: deviation must be zero
    result = module_0.mean_absolute_deviation([5.0])
    assert math.isclose(result, 0.0), f"Expected 0.0, got {result}"

    # All identical values: deviation must be zero
    result = module_0.mean_absolute_deviation([7.5, 7.5, 7.5, 7.5])
    assert math.isclose(result, 0.0), f"Expected 0.0, got {result}"

    # Two elements
    result = module_0.mean_absolute_deviation([0.5, 1.5])
    assert math.isclose(result, 0.5), f"Expected 0.5, got {result}"

    # All negative numbers
    result = module_0.mean_absolute_deviation([-2.0, -4.0, -6.0])
    # mean = -4.0, deviations = [2.0, 0.0, 2.0], MAD = 4/3
    assert math.isclose(result, 4.0 / 3.0), f"Expected {4.0/3.0}, got {result}"

    # Mixed values with decimals
    result = module_0.mean_absolute_deviation([1.5, 2.5, 3.5, 4.5])
    assert math.isclose(result, 1.0), f"Expected 1.0, got {result}"

    # Large list sanity check against manual computation
    data = [float(i) for i in range(1, 101)]  # 1.0 .. 100.0
    result = module_0.mean_absolute_deviation(data)
    assert math.isclose(result, 25.0), f"Expected 25.0, got {result}"

    # Result is always non-negative
    result = module_0.mean_absolute_deviation([3.0, -3.0, 3.0, -3.0])
    assert result >= 0.0
    assert math.isclose(result, 3.0), f"Expected 3.0, got {result}"


if __name__ == "__main__":
    test_mean_absolute_deviation()
    print("All tests passed!")
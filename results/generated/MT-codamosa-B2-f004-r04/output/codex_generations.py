

# Generated at 2026-11-01 21:40:17.753210
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Simple evenly spaced list
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # All identical values -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0, 5.0, 5.0]) == 0.0

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([42.0]) == 0.0

    # Symmetric values around zero
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Values with a fractional mean
    # mean = 2.5, deviations = 1.5, 0.5, 0.5, 2.5 -> MAD = 1.25
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 5.0]), 1.25)

    # Negative numbers
    # mean = -2.0, deviations = 1, 1, 3 -> MAD = 5/3
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, -3.0, -2.0]), 5.0 / 3.0)

    # Zeros
    assert module_0.mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0

    # Result is always non-negative
    assert module_0.mean_absolute_deviation([3.0, -7.0, 2.5]) >= 0.0


def test_mean_absolute_deviation_matches_manual_computation():
    numbers = [4.0, 1.0, 8.0, 7.0]
    mean = sum(numbers) / len(numbers)
    expected = sum(abs(x - mean) for x in numbers) / len(numbers)
    assert math.isclose(module_0.mean_absolute_deviation(numbers), expected)

# Generated at 2026-11-01 21:40:40.869943
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: [1, 2, 3] -> mean = 2, MAD = (1 + 0 + 1) / 3 = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]), 2.0 / 3.0)

    # Even-length list: [1, 2, 3, 4] -> mean = 2.5, MAD = (1.5 + 0.5 + 0.5 + 1.5) / 4 = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Single element: deviation is always zero
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # All identical values: deviation is zero
    assert module_0.mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0

    # Symmetric around mean with negative values
    # [-2, -1, 1, 2] -> mean = 0, MAD = (2 + 1 + 1 + 2) / 4 = 1.5
    assert math.isclose(module_0.mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]), 1.5)

    # Float precision check
    result = module_0.mean_absolute_deviation([1.0, 2.0, 3.0])
    assert abs(result - 0.6666666666666666) < 1e-9

# Generated at 2026-11-01 21:41:05.578806
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: mean is one of the elements
    result = module_0.mean_absolute_deviation([1.0, 2.0, 3.0])
    assert math.isclose(result, (abs(1.0 - 2.0) + abs(2.0 - 2.0) + abs(3.0 - 2.0)) / 3.0)

    # Case where mean falls between elements
    result = module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert math.isclose(result, 1.0)

    # Single element has zero deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Identical elements have zero deviation
    assert module_0.mean_absolute_deviation([2.0, 2.0, 2.0]) == 0.0

    # Negative numbers
    result = module_0.mean_absolute_deviation([-1.0, 0.0, 1.0])
    assert math.isclose(result, 2.0 / 3.0)

    # Non-trivial floats
    result = module_0.mean_absolute_deviation([1.5, 2.5, 3.5, 4.5])
    assert math.isclose(result, 1.0)

    # Result is symmetric under translation
    original = module_0.mean_absolute_deviation([10.0, 20.0, 30.0])
    shifted = module_0.mean_absolute_deviation([110.0, 120.0, 130.0])
    assert math.isclose(original, shifted)

# Generated at 2026-11-01 21:41:54.626090
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: [1, 2, 3, 4] -> mean = 2.5, deviations = [1.5, 0.5, 0.5, 1.5]
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Simple case: [1, 2, 3] -> mean = 2.0, deviations = [1.0, 0.0, 1.0]
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]), 2.0 / 3.0)

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # All identical values -> zero deviation
    assert module_0.mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0

    # Negative and positive values
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 1.0]), 1.0)

    # Symmetric around zero
    assert math.isclose(module_0.mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]), 1.5)

    # Floats with fractional values
    result = module_0.mean_absolute_deviation([1.5, 2.5, 3.5])
    assert math.isclose(result, 2.0 / 3.0)

    # Verify result is non-negative for arbitrary input
    assert module_0.mean_absolute_deviation([3.0, -7.0, 0.5, 12.1]) >= 0.0

    # Verify against manual computation
    data = [4.0, 8.0, 6.0, 5.0]
    expected = sum(abs(x - 5.75) for x in data) / 4.0
    assert math.isclose(module_0.mean_absolute_deviation(data), expected)

# Generated at 2026-11-01 21:42:17.971476
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: mean is 2.5, deviations are [1.5, 0.5, 0.5, 1.5], MAD = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Single element: deviation is 0
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # All identical elements: deviation is 0
    assert module_0.mean_absolute_deviation([3.0, 3.0, 3.0]) == 0.0

    # Symmetric values around mean
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]), 2.0 / 3.0)

    # Mixed positive and negative values
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Floating point values
    assert math.isclose(module_0.mean_absolute_deviation([0.5, 1.5, 2.5, 3.5]), 1.0)
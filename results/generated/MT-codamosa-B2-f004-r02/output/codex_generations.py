

# Generated at 2026-11-03 02:27:44.784359
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Simple list of numbers
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Single element list
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # All identical elements
    assert module_0.mean_absolute_deviation([3.0, 3.0, 3.0]) == 0.0

    # Negative numbers
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Floating point values
    assert math.isclose(module_0.mean_absolute_deviation([1.5, 2.5, 3.5]), 2.0 / 3.0)

    # Unsorted list
    assert math.isclose(module_0.mean_absolute_deviation([4.0, 1.0, 3.0, 2.0]), 1.0)

    # Larger set with known result
    # mean of [0, 10] is 5, deviations are 5 and 5 -> MAD = 5
    assert math.isclose(module_0.mean_absolute_deviation([0.0, 10.0]), 5.0)

# Generated at 2026-11-03 02:29:50.818322
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Typical case: symmetric distribution
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-9

    # Another known case: [4, 1, 8, 3] -> mean=4, deviations=[0,3,4,1], MAD=2.0
    assert abs(module_0.mean_absolute_deviation([4.0, 1.0, 8.0, 3.0]) - 2.0) < 1e-9

    # All identical values -> zero deviation
    assert module_0.mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == 0.0

    # Single element -> zero deviation
    assert module_0.mean_absolute_deviation([42.0]) == 0.0

    # Two elements symmetric around their mean
    assert abs(module_0.mean_absolute_deviation([1.0, 3.0]) - 1.0) < 1e-9

    # Negative numbers: [-1, 0, 1] -> mean=0, MAD=2/3
    assert abs(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) - 2.0 / 3.0) < 1e-9

    # All negative numbers: [-2, -4, -6] -> mean=-4, deviations=[2,0,2], MAD=4/3
    assert abs(module_0.mean_absolute_deviation([-2.0, -4.0, -6.0]) - 4.0 / 3.0) < 1e-9

    # Result is always non-negative
    assert module_0.mean_absolute_deviation([3.0, 7.0, 1.0, 9.0]) >= 0.0

    # Float precision case
    assert abs(module_0.mean_absolute_deviation([0.1, 0.2, 0.3]) - 0.06666666666666667) < 1e-9

    print("All tests passed!")


if __name__ == "__main__":
    test_mean_absolute_deviation()

# Generated at 2026-11-03 02:31:03.501306
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Test with a simple list of numbers
    assert abs(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-9

    # Test with a single element (deviation should be zero)
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Test with identical elements (deviation should be zero)
    assert module_0.mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0

    # Test with negative numbers
    # mean = -1.0, deviations = [2.0, 1.0, 0.0, 1.0, 2.0] -> MAD = 1.2
    assert abs(module_0.mean_absolute_deviation([-3.0, -2.0, -1.0, 0.0, 1.0]) - 1.2) < 1e-9

    # Test with floats and known result
    # mean = 4.0, deviations = [2.0, 0.0, 2.0] -> MAD = 4/3
    assert abs(module_0.mean_absolute_deviation([2.0, 4.0, 6.0]) - (4.0 / 3.0)) < 1e-9

    # Test that result is always non-negative
    assert module_0.mean_absolute_deviation([3.0, -7.0, 2.5, 9.1]) >= 0.0

    print("All tests passed!")


if __name__ == "__main__":
    test_mean_absolute_deviation()

# Generated at 2026-11-03 02:32:41.519929
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: [1, 2, 3] -> mean = 2, MAD = (1 + 0 + 1) / 3 = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]), 2.0 / 3.0)

    # Even-length list: [1, 2, 3, 4] -> mean = 2.5, MAD = (1.5 + 0.5 + 0.5 + 1.5) / 4 = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Single element: deviation is zero
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # All identical values: deviation is zero
    assert module_0.mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]) == 0.0

    # Negative numbers: [-1, 0, 1] -> mean = 0, MAD = (1 + 0 + 1) / 3 = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Mixed positive/negative floats: [0.5, -0.5, 1.5, -1.5] -> mean = 0, MAD = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([0.5, -0.5, 1.5, -1.5]), 1.0)

    # Larger values: [10, 20, 30] -> mean = 20, MAD = (10 + 0 + 10) / 3 = 20/3
    assert math.isclose(module_0.mean_absolute_deviation([10.0, 20.0, 30.0]), 20.0 / 3.0)

    # Float precision values: [1.5, 2.5] -> mean = 2.0, MAD = 0.5
    assert math.isclose(module_0.mean_absolute_deviation([1.5, 2.5]), 0.5)

# Generated at 2026-11-03 02:34:18.294287
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic odd-length list: [1, 2, 3] -> mean = 2, MAD = (1 + 0 + 1) / 3 = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0]), 2.0 / 3.0)

    # Even-length list: [1, 2, 3, 4] -> mean = 2.5, MAD = (1.5+0.5+0.5+1.5)/4 = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # All identical values -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == 0.0

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([42.0]) == 0.0

    # Symmetric around zero: [-1, 0, 1] -> mean = 0, MAD = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Non-integer floats: [1.5, 2.5, 3.5] -> mean = 2.5, MAD = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.5, 2.5, 3.5]), 1.0)

    # Order of elements should not matter
    assert math.isclose(
        module_0.mean_absolute_deviation([3.0, 1.0, 4.0, 2.0]),
        module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]),
    )

    # Larger varied list: compare against independently computed expectation
    data = [10.0, 2.0, 38.0, 23.0, 38.0, 23.0, 21.0]
    m = sum(data) / len(data)
    expected = sum(abs(x - m) for x in data) / len(data)
    assert math.isclose(module_0.mean_absolute_deviation(data), expected)

    # Result must be a non-negative float
    result = module_0.mean_absolute_deviation([1.0, 7.0, 3.0])
    assert isinstance(result, float)
    assert result >= 0.0
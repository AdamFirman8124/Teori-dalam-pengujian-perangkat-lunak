

# Generated at 2026-11-03 06:05:08.523178
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: [1, 2, 3, 4] -> mean = 2.5, MAD = (1.5+0.5+0.5+1.5)/4 = 1.0
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)

    # Single element: deviation is always 0
    assert module_0.mean_absolute_deviation([5.0]) == pytest.approx(0.0)

    # Identical elements: mean equals each element, deviation is 0
    assert module_0.mean_absolute_deviation([7.0, 7.0, 7.0]) == pytest.approx(0.0)

    # Negative and positive values: [1, -2, 3] -> mean = 2/3, MAD = (5/3 + 8/3 + 7/3)/3 = 20/9
    assert module_0.mean_absolute_deviation([1.0, -2.0, 3.0]) == pytest.approx(20.0 / 9.0)

    # Symmetric values around zero: [−1, 0, 1] -> mean = 0, MAD = 2/3
    assert module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) == pytest.approx(2.0 / 3.0)

    # Float precision check
    assert module_0.mean_absolute_deviation([0.1, 0.2, 0.3]) == pytest.approx(0.06666666666666667)

    # Result is non-negative for arbitrary data
    assert module_0.mean_absolute_deviation([3.5, -7.2, 1.1, 9.9]) >= 0.0

# Generated at 2026-11-03 06:06:42.431806
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)

    # Non-integer result
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0]) == pytest.approx(2.0 / 3.0)

    # All identical values -> zero deviation
    assert module_0.mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == pytest.approx(0.0)

    # All zeros
    assert module_0.mean_absolute_deviation([0.0, 0.0, 0.0]) == pytest.approx(0.0)

    # Five elements: mean=3, deviations 2,1,0,1,2 -> 6/5 = 1.2
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx(1.2)

    # Negative and positive values
    assert module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]) == pytest.approx(2.0 / 3.0)

    # Symmetric spread around mean
    assert module_0.mean_absolute_deviation([10.0, 20.0]) == pytest.approx(5.0)

# Generated at 2026-11-03 06:08:02.298474
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Standard case: mean = 2.5, deviations = [1.5, 0.5, 0.5, 1.5], MAD = 1.0
    assert module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)

    # Unsorted values: mean = 3.75, MAD = (0.25 + 2.75 + 4.25 + 1.75) / 4 = 2.25
    assert module_0.mean_absolute_deviation([4.0, 1.0, 8.0, 2.0]) == pytest.approx(2.25)

    # Single element: deviation from mean is zero
    assert module_0.mean_absolute_deviation([5.0]) == pytest.approx(0.0)

    # Identical elements: no deviation
    assert module_0.mean_absolute_deviation([3.0, 3.0, 3.0]) == pytest.approx(0.0)

    # Negative and positive values: mean = -1.0, MAD = (2 + 1 + 0 + 1 + 2) / 5 = 1.2
    assert module_0.mean_absolute_deviation([1.0, 0.0, -1.0, -2.0, -3.0]) == pytest.approx(1.2)

    # Floating point precision check
    assert module_0.mean_absolute_deviation([0.1, 0.2, 0.3]) == pytest.approx(0.06666666666666667)

# Generated at 2026-11-03 06:09:46.075604
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # Basic case: evenly spaced numbers
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # All identical values -> deviation is zero
    assert module_0.mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0

    # Single element -> deviation is zero
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Symmetric values around zero
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 1.0]), 1.0)
    assert math.isclose(module_0.mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]), 1.5)

    # Negative numbers only
    # mean = -4.0, deviations = [1.0, 0.0, 2.0, 1.0] -> 1.0
    assert math.isclose(module_0.mean_absolute_deviation([-3.0, -4.0, -6.0, -3.0]), 1.0)

    # Mixed floats
    # mean = 0.5, deviations = [0.5, 0.0, 0.5] -> 1.0/3
    assert math.isclose(module_0.mean_absolute_deviation([0.0, 0.5, 1.0]), 1.0 / 3.0)

    # Two elements
    assert math.isclose(module_0.mean_absolute_deviation([0.0, 10.0]), 5.0)

    # Result is never negative
    assert module_0.mean_absolute_deviation([3.7, 2.1, -4.5]) >= 0.0

    # Manual verification against explicit computation
    data = [1.5, 2.5, 3.5, 4.5, 10.0]
    expected_mean = sum(data) / len(data)
    expected = sum(abs(x - expected_mean) for x in data) / len(data)
    assert math.isclose(module_0.mean_absolute_deviation(data), expected)

# Generated at 2026-11-03 06:11:36.418325
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # nonce:2720d2e9
    # Classic example: mean = 2.5, deviations = [1.5, 0.5, 0.5, 1.5] -> MAD = 1.0
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    # Two elements: mean = 1.5, deviations = [0.5, 0.5] -> MAD = 0.5
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0]), 0.5)

    # Single element has zero deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # Identical elements have zero deviation
    assert module_0.mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]) == 0.0

    # Five elements: mean = 3.0, deviations = [2, 1, 0, 1, 2] -> MAD = 1.2
    assert math.isclose(module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.2)

    # Negative numbers: mean = 0.0, deviations = [1, 0, 1] -> MAD = 2/3
    assert math.isclose(module_0.mean_absolute_deviation([-1.0, 0.0, 1.0]), 2.0 / 3.0)

    # Skewed values: mean = 2.5, deviations = [2.5, 2.5, 2.5, 7.5] -> MAD = 3.75
    assert math.isclose(module_0.mean_absolute_deviation([0.0, 0.0, 0.0, 10.0]), 3.75)

    # Fractional floats: mean = 1.0, deviations = [0.5, 0.0, 0.5] -> MAD = 1/3
    assert math.isclose(module_0.mean_absolute_deviation([0.5, 1.0, 1.5]), 1.0 / 3.0)

    # All-negative input: result is still non-negative
    assert module_0.mean_absolute_deviation([-10.0, -20.0, -30.0]) >= 0.0

    # Order independence: shuffling inputs doesn't change the MAD
    assert math.isclose(
        module_0.mean_absolute_deviation([4.0, 1.0, 3.0, 2.0]),
        module_0.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]),
    )
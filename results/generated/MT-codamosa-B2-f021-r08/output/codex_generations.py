

# Generated at 2026-11-01 23:57:51.730064
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic increasing sequence
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

    # Longer sequence
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Negative and positive values
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Two-element list spans full range
    assert module_0.rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]

    # Unsorted input should still map min->0, max->1 correctly
    result = module_0.rescale_to_unit([12.13, 7.84, 3.41])
    assert abs(result[0] - 1.0) < 1e-9
    assert abs(result[2] - 0.0) < 1e-9

    # All outputs must lie within [0, 1]
    values = module_0.rescale_to_unit([3.5, -2.1, 9.9, 0.0])
    assert all(0.0 <= v <= 1.0 for v in values)

    # Min value maps to 0, max value maps to 1 regardless of position
    vals = module_0.rescale_to_unit([100.0, 50.0, 0.0])
    assert vals[0] == 1.0
    assert vals[2] == 0.0

# Generated at 2026-11-01 23:58:14.182145
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: linear spread maps to [0, 1]
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Min maps to 0.0, max maps to 1.0
    result = module_0.rescale_to_unit([2.0, 4.0, 6.0])
    assert math.isclose(result[0], 0.0)
    assert math.isclose(result[-1], 1.0)

    # Negative numbers
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]

    # Unsorted input: order is preserved
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Fractional values
    result = module_0.rescale_to_unit([0.5, 1.5])
    assert math.isclose(result[0], 0.0)
    assert math.isclose(result[1], 1.0)

    # All identical values -> min == max -> division by zero
    try:
        module_0.rescale_to_unit([3.0, 3.0, 3.0])
        assert False, "Expected ZeroDivisionError for identical values"
    except ZeroDivisionError:
        pass

    # Empty list -> min/max raise ValueError
    try:
        module_0.rescale_to_unit([])
        assert False, "Expected ValueError for empty input"
    except ValueError:
        pass

    # All results lie within [0, 1]
    numbers = [10.0, -2.5, 3.3, 7.7, 0.0]
    assert all(0.0 <= x <= 1.0 for x in module_0.rescale_to_unit(numbers))

    # Output length matches input length
    assert len(module_0.rescale_to_unit(numbers)) == len(numbers)

# Generated at 2026-11-01 23:58:29.977456
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: evenly spaced values
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Evenly spaced with larger step
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([1.0, 2.0]) == [0.0, 1.0]

    # Negative and positive values
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # All negative values
    assert module_0.rescale_to_unit([-5.0, -3.0, -1.0]) == [0.0, 0.5, 1.0]

    # Unsorted input with floating point tolerance
    result = module_0.rescale_to_unit([3.5, 1.2, 7.8, 2.2])
    expected = [(x - 1.2) / (7.8 - 1.2) for x in [3.5, 1.2, 7.8, 2.2]]
    assert all(abs(a - b) < 1e-9 for a, b in zip(result, expected))

    # Min maps to 0.0 and max maps to 1.0
    scaled = module_0.rescale_to_unit([10.0, 20.0, 30.0])
    assert min(scaled) == 0.0
    assert max(scaled) == 1.0

    # Result length matches input length
    assert len(module_0.rescale_to_unit([1.0, 2.0, 3.0])) == 3

    # Duplicated min/max values
    assert module_0.rescale_to_unit([3.0, 3.0, 7.0, 7.0]) == [0.0, 0.0, 1.0, 1.0]

# Generated at 2026-11-01 23:58:48.614982
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear mapping to [0, 1]
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Min and max map exactly to 0 and 1
    assert module_0.rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]

    # Descending order still works
    assert module_0.rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]

    # Negative values
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Non-evenly spaced values are proportionally scaled
    result = module_0.rescale_to_unit([5.0, 10.0, 15.0, 20.0])
    expected = [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0]
    assert all(abs(r - e) < 1e-9 for r, e in zip(result, expected))

    # All outputs lie within [0, 1]
    assert all(0.0 <= v <= 1.0 for v in result)

    # Degenerate case: all equal values cause division by zero
    try:
        module_0.rescale_to_unit([3.0, 3.0, 3.0])
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

# Generated at 2026-11-01 23:58:57.321484
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: evenly spaced numbers rescale to [0, 1]
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements: min maps to 0, max maps to 1
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Unsorted input still yields correct min/max scaling
    result = module_0.rescale_to_unit([5.0, 1.0, 3.0])
    assert result == [1.0, 0.0, 0.5]

    # Negative values are handled correctly
    assert module_0.rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

    # All values between 0 and 1 (exclusive of bounds check via range)
    result = module_0.rescale_to_unit([10.0, 20.0, 30.0])
    assert all(0.0 <= x <= 1.0 for x in result)
    assert result[0] == 0.0 and result[-1] == 1.0
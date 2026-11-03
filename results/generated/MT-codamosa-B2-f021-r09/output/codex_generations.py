

# Generated at 2026-11-01 21:55:41.719698
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # nonce:a8c264a6
    # Basic case: evenly spaced values rescale linearly
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e)

    # Smallest value maps to 0.0, largest maps to 1.0
    assert result[0] == 0.0
    assert result[-1] == 1.0

    # Two-element list
    result = module_0.rescale_to_unit([2.0, 6.0])
    assert result[0] == 0.0
    assert result[1] == 1.0

    # Unsorted input
    result = module_0.rescale_to_unit([5.0, 3.0, 1.0])
    assert math.isclose(result[0], 1.0)
    assert math.isclose(result[1], 0.5)
    assert math.isclose(result[2], 0.0)

    # Negative numbers
    result = module_0.rescale_to_unit([-2.0, 0.0, 2.0])
    assert math.isclose(result[0], 0.0)
    assert math.isclose(result[1], 0.5)
    assert math.isclose(result[2], 1.0)

    # General properties: results stay within [0, 1]
    numbers = [3.7, 1.2, 9.4, 0.5, 7.1]
    result = module_0.rescale_to_unit(numbers)
    assert all(0.0 <= x <= 1.0 for x in result)
    assert math.isclose(result[numbers.index(min(numbers))], 0.0)
    assert math.isclose(result[numbers.index(max(numbers))], 1.0)

# Generated at 2026-11-01 21:56:24.112089
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: evenly spaced values
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0]) == [0.0, 0.5, 1.0]

    # Already in unit range
    assert module_0.rescale_to_unit([0.0, 0.5, 1.0]) == [0.0, 0.5, 1.0]

    # Unsorted input: min maps to 0, max maps to 1
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Arbitrary values: length preserved, values within [0, 1]
    numbers = [3.5, 7.2, 1.1, 9.9]
    result = module_0.rescale_to_unit(numbers)
    assert len(result) == len(numbers)
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)
    assert result[0] == pytest.approx((3.5 - 1.1) / (9.9 - 1.1))
    assert all(0.0 <= x <= 1.0 for x in result)

    # All identical values cause division by zero
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([2.0, 2.0, 2.0])

# Generated at 2026-11-01 21:57:01.699875
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic two-element list
    assert module_0.rescale_to_unit([1.0, 2.0]) == [0.0, 1.0]

    # Evenly spaced values map to evenly spaced unit interval
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Negative numbers are handled correctly
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0, 1.0, 2.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Unordered input: relative order preserved, min -> 0.0, max -> 1.0
    assert module_0.rescale_to_unit([10.0, 1.0, 5.5]) == [1.0, 0.0, 0.5]

    # Duplicate min/max values
    assert module_0.rescale_to_unit([3.0, 3.0, 7.0, 7.0]) == [0.0, 0.0, 1.0, 1.0]

    # All outputs lie within [0, 1]; min and max of result are exactly 0 and 1
    result = module_0.rescale_to_unit([3.5, 1.2, 4.8, 2.1])
    assert all(0.0 <= x <= 1.0 for x in result)
    assert min(result) == 0.0
    assert max(result) == 1.0

    # Approximate check for values not exactly representable in binary floats
    result = module_0.rescale_to_unit([0.0, 0.1, 0.3])
    assert abs(result[1] - 0.1 / 0.3) < 1e-9
    assert result[0] == 0.0
    assert result[2] == 1.0

    # Output length matches input length
    numbers = [5.0, 1.0, 9.0, 2.0, 7.0]
    assert len(module_0.rescale_to_unit(numbers)) == len(numbers)

# Generated at 2026-11-01 21:57:48.181836
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear scaling: min -> 0, max -> 1
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Min/max at different positions preserved order-wise
    assert module_0.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

    # Negative numbers handled correctly
    assert module_0.rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

    # All negative values
    assert module_0.rescale_to_unit([-5.0, -3.0, -1.0]) == [0.0, 0.5, 1.0]

    # Two-element list maps exactly to endpoints
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Range smaller than [0, 1] is stretched to full [0, 1]
    assert module_0.rescale_to_unit([0.2, 0.6]) == [0.0, 1.0]

    # Floating-point robustness using approx comparison
    result = module_0.rescale_to_unit([1.0, 2.0, 7.0])
    assert result == pytest.approx([0.0, 1.0 / 6.0, 1.0])

    # Output bounds are always 0 and 1
    data = [3.5, -1.2, 9.8, 0.0, 4.44]
    scaled = module_0.rescale_to_unit(data)
    assert min(scaled) == pytest.approx(0.0)
    assert max(scaled) == pytest.approx(1.0)
    assert len(scaled) == len(data)


def test_rescale_to_unit_empty_raises():
    # Empty input has no min/max
    with pytest.raises(ValueError):
        module_0.rescale_to_unit([])


def test_rescale_to_unit_single_element_raises():
    # Single element => division by zero (max - min == 0)
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([42.0])


def test_rescale_to_unit_identical_values_raises():
    # Identical values => division by zero
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([7.0, 7.0, 7.0])

# Generated at 2026-11-01 21:58:38.362067
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear rescaling: min -> 0, max -> 1, evenly spaced in between
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Proportional values with different scale map identically
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Two-element list
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Reversed order: max -> 1 first, min -> 0 last
    assert module_0.rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]) == [1.0, 0.75, 0.5, 0.25, 0.0]

    # Negative numbers are handled correctly
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

    # All-negative inputs
    result = module_0.rescale_to_unit([-10.0, -5.0, -15.0])
    assert abs(result[0] - (5.0 / 10.0)) < 1e-9   # (-10 - (-15)) / 10
    assert abs(result[1] - (10.0 / 10.0)) < 1e-9  # (-5 - (-15)) / 10
    assert abs(result[2] - (0.0 / 10.0)) < 1e-9   # (-15 - (-15)) / 10

    # Unsorted input preserves original ordering
    result = module_0.rescale_to_unit([3.0, 1.0, 2.0])
    assert result == [1.0, 0.0, 0.5]

    # Output values always fall within [0, 1]
    data = [17.5, -3.2, 8.8, 0.001, -100.7]
    scaled = module_0.rescale_to_unit(data)
    for v in scaled:
        assert 0.0 <= v <= 1.0

    # Length of output matches length of input
    assert len(scaled) == len(data)


def test_rescale_to_unit_constant_list_raises():
    # Identical values produce division by zero (max - min == 0)
    try:
        module_0.rescale_to_unit([3.0, 3.0, 3.0])
        raised = False
    except ZeroDivisionError:
        raised = True
    assert raised, "Expected ZeroDivisionError for constant input list"
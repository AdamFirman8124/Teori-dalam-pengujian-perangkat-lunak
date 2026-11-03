

# Generated at 2026-11-02 12:49:58.151794
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: min maps to 0, max maps to 1, evenly spaced in between
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

    # All negative numbers
    assert module_0.rescale_to_unit([-10.0, -5.0, 0.0]) == [0.0, 0.5, 1.0]

    # Unsorted input: order is preserved
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Fractional values
    result = module_0.rescale_to_unit([0.0, 0.5, 1.0])
    assert abs(result[1] - 0.5) < 1e-9

    # Output bounds and length for arbitrary input
    numbers = [10.0, 20.0, 15.0, 30.0]
    result = module_0.rescale_to_unit(numbers)
    assert len(result) == len(numbers)
    assert min(result) == 0.0
    assert max(result) == 1.0

    # Identical values cause division by zero (max - min == 0)
    try:
        module_0.rescale_to_unit([3.0, 3.0, 3.0])
        assert False, "Expected ZeroDivisionError for identical values"
    except ZeroDivisionError:
        pass

    # Single element also triggers division by zero
    try:
        module_0.rescale_to_unit([7.0])
        assert False, "Expected ZeroDivisionError for single element"
    except ZeroDivisionError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_rescale_to_unit()

# Generated at 2026-11-02 12:51:21.455297
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear sequence: min -> 0, max -> 1, evenly spaced in between
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements map exactly to the endpoints
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Negative numbers are handled correctly
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]

    # Already normalized input is unchanged
    assert module_0.rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]

    # Unsorted input: original order is preserved
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Non evenly-spaced values: use approximate comparison
    result = module_0.rescale_to_unit([1.0, 2.0, 4.0])
    assert result == pytest.approx([0.0, 1.0 / 3.0, 1.0])

    # Values strictly between min and max stay strictly within (0, 1)
    result = module_0.rescale_to_unit([10.0, 20.0, 15.0, 12.5])
    assert result[0] == 1.0
    assert result[1] == 0.0
    assert 0.0 < result[2] < 1.0
    assert 0.0 < result[3] < 1.0

    # Fractional inputs
    result = module_0.rescale_to_unit([0.5, 1.5, 2.5])
    assert result == [0.0, 0.5, 1.0]

    # Repeated extreme values
    assert module_0.rescale_to_unit([3.0, 3.0, 7.0, 7.0]) == [0.0, 0.0, 1.0, 1.0]

# Generated at 2026-11-02 12:52:28.873186
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: values spread across the unit interval
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Two elements: min maps to 0, max maps to 1
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0]) == [0.0, 0.5, 1.0]

    # Unsorted input still rescales correctly relative to min/max
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Floating point input
    result = module_0.rescale_to_unit([0.5, 1.5])
    assert abs(result[0] - 0.0) < 1e-9
    assert abs(result[1] - 1.0) < 1e-9

    # All values in range [0, 1]
    result = module_0.rescale_to_unit([3.0, 7.0, 5.0])
    assert all(0.0 <= x <= 1.0 for x in result)

    # Single element raises ZeroDivisionError (max == min)
    try:
        module_0.rescale_to_unit([42.0])
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

    # Empty list raises ValueError from min()
    try:
        module_0.rescale_to_unit([])
        assert False, "Expected ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    test_rescale_to_unit()
    print("All tests passed!")

# Generated at 2026-11-02 12:53:46.182714
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear rescaling
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Unsorted input rescales the same way
    assert module_0.rescale_to_unit([5.0, 3.0, 1.0, 2.0]) == [1.0, 0.5, 0.0, 0.25]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Two elements map to the boundaries
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Single min/max boundary checks with arbitrary values
    result = module_0.rescale_to_unit([2.5, 7.3, 4.1])
    assert math.isclose(result[0], 0.0)
    assert math.isclose(max(result), 1.0)
    assert math.isclose(result[2], (4.1 - 2.5) / (7.3 - 2.5))

    # Length is preserved
    input_list = [3.5, 1.2, 9.8, 4.4, 0.0]
    result = module_0.rescale_to_unit(input_list)
    assert len(result) == len(input_list)

    # All output values fall within [0, 1]
    for v in result:
        assert 0.0 <= v <= 1.0

    # Input list is not mutated
    original = [1.0, 2.0, 3.0]
    snapshot = list(original)
    module_0.rescale_to_unit(original)
    assert original == snapshot

    # Floating point precision check
    result = module_0.rescale_to_unit([0.0, 1.0, 3.0])
    assert math.isclose(result[1], 1.0 / 3.0)

# Generated at 2026-11-02 12:54:44.198269
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: linear scaling from min to max
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_rescale_to_unit_two_elements():
    # Two elements map to endpoints of the unit interval
    assert module_0.rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]


def test_rescale_to_unit_negative_numbers():
    # Negative values are handled correctly
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]


def test_rescale_to_unit_unsorted_input():
    # Order of input is preserved (not sorted)
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]


def test_rescale_to_unit_with_duplicates():
    # Duplicates of the minimum map to 0.0
    assert module_0.rescale_to_unit([1.0, 1.0, 3.0]) == [0.0, 0.0, 1.0]


def test_rescale_to_unit_min_max_repeated():
    # Mix of min/max values rescales to 0 and 1
    assert module_0.rescale_to_unit([0.0, 10.0, 0.0, 10.0]) == [0.0, 1.0, 0.0, 1.0]


def test_rescale_to_unit_fractional_values():
    # Fractional inputs rescale correctly
    result = module_0.rescale_to_unit([0.5, 1.0, 1.5])
    assert result == pytest.approx([0.0, 0.5, 1.0])


def test_rescale_to_unit_all_within_unit_interval():
    # All outputs must lie within [0, 1]
    numbers = [3.7, 12.5, -4.2, 0.0, 8.1]
    result = module_0.rescale_to_unit(numbers)
    assert all(0.0 <= x <= 1.0 for x in result)
    assert result[0] == 0.0  # smallest value
    assert result[2] == 1.0  # largest value
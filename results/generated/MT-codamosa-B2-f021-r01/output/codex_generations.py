

# Generated at 2026-11-02 17:01:36.163257
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Test basic case: min maps to 0, max maps to 1, middle values scale linearly
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

    # Test with negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Test with two elements
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Test with already normalized values
    assert module_0.rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]

    # Test with duplicates: all min values map to 0
    assert module_0.rescale_to_unit([5.0, 5.0, 10.0]) == [0.0, 0.0, 1.0]

    # Test order and length preservation with arbitrary floats
    numbers = [10.0, 2.5, 7.25, 0.0, 3.75]
    result = module_0.rescale_to_unit(numbers)
    assert len(result) == len(numbers)
    assert result[0] == 1.0          # max element
    assert result[3] == 0.0          # min element
    assert abs(result[1] - (2.5 - 0.0) / 10.0) < 1e-9
    assert abs(result[2] - 7.25 / 10.0) < 1e-9
    assert abs(result[4] - 3.75 / 10.0) < 1e-9

    # Test floating point precision
    result = module_0.rescale_to_unit([1.0, 2.0, 4.0])
    assert abs(result[0] - 0.0) < 1e-9
    assert abs(result[1] - (1.0 / 3.0)) < 1e-9
    assert abs(result[2] - 1.0) < 1e-9

    # Test edge case: all identical values raise ZeroDivisionError
    try:
        module_0.rescale_to_unit([5.0, 5.0, 5.0])
        assert False, "Expected ZeroDivisionError for constant list"
    except ZeroDivisionError:
        pass


# Run the test
if __name__ == "__main__":
    test_rescale_to_unit()
    print("All tests passed!")

# Generated at 2026-11-02 17:03:33.178878
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    import math

    # Basic case: linear sequence of numbers
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert all(math.isclose(r, e) for r, e in zip(result, expected)), \
        f"Expected {expected}, got {result}"

    # Case with negative numbers
    result = module_0.rescale_to_unit([-2.0, 0.0, 2.0])
    expected = [0.0, 0.5, 1.0]
    assert all(math.isclose(r, e) for r, e in zip(result, expected)), \
        f"Expected {expected}, got {result}"

    # Case with only two elements
    result = module_0.rescale_to_unit([10.0, 20.0])
    expected = [0.0, 1.0]
    assert all(math.isclose(r, e) for r, e in zip(result, expected)), \
        f"Expected {expected}, got {result}"

    # Case with unsorted input
    result = module_0.rescale_to_unit([5.0, 1.0, 3.0])
    expected = [1.0, 0.0, 0.5]
    assert all(math.isclose(r, e) for r, e in zip(result, expected)), \
        f"Expected {expected}, got {result}"

    # Case with float values
    result = module_0.rescale_to_unit([0.5, 1.5])
    expected = [0.0, 1.0]
    assert all(math.isclose(r, e) for r, e in zip(result, expected)), \
        f"Expected {expected}, got {result}"

    # Result should always be within [0, 1]
    result = module_0.rescale_to_unit([3.7, 1.2, 9.9, 4.4])
    assert all(0.0 <= x <= 1.0 for x in result), \
        f"All values should be in [0, 1], got {result}"

    # Minimum maps to 0.0 and maximum maps to 1.0
    assert math.isclose(min(result), 0.0), "Minimum should map to 0.0"
    assert math.isclose(max(result), 1.0), "Maximum should map to 1.0"

    # Output length should match input length
    assert len(result) == 4, "Output length should match input length"

# Generated at 2026-11-02 17:04:38.184830
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

    result = module_0.rescale_to_unit([0.0, 1.0])
    assert result == [0.0, 1.0]

    result = module_0.rescale_to_unit([3.0, 1.0, 2.0])
    assert result == [1.0, 0.0, 0.5]

    result = module_0.rescale_to_unit([-2.0, 0.0, 2.0])
    assert result == [0.0, 0.5, 1.0]

    result = module_0.rescale_to_unit([1.0, 3.0, 5.5, 7.0])
    assert result[0] == 0.0
    assert abs(result[1] - (2.0 / 6.0)) < 1e-9
    assert result[2] == 0.75
    assert result[3] == 1.0

# Generated at 2026-11-02 17:05:37.989376
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: evenly spaced values
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements: smallest maps to 0.0, largest maps to 1.0
    assert module_0.rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]

    # Descending order: largest first
    assert module_0.rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]

    # Unsorted input
    assert module_0.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

    # Another unsorted input
    assert module_0.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

    # Negative values
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Values not starting at zero
    assert module_0.rescale_to_unit([10.0, 20.0, 30.0]) == [0.0, 0.5, 1.0]


if __name__ == "__main__":
    test_rescale_to_unit()
    print("All tests passed!")

# Generated at 2026-11-02 17:06:34.438834
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Test with a simple list of positive numbers
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Test with negative and positive numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Test with evenly spaced values
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Test min maps to 0.0 and max maps to 1.0
    numbers = [3.5, 7.2, 1.1, 9.9]
    result = module_0.rescale_to_unit(numbers)
    assert result[2] == 0.0
    assert result[3] == 1.0

    # Test all values are within the unit interval
    assert all(0.0 <= x <= 1.0 for x in result)

    # Test that order of input is preserved
    assert result == sorted(result)

    # Test with exactly two elements
    assert module_0.rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]

    # Test with an all-negative range (descending order)
    assert module_0.rescale_to_unit([-5.0, -10.0]) == [1.0, 0.0]

    # Test with unsorted input
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

# Generated at 2026-11-02 17:07:14.817204
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: smallest -> 0, largest -> 1, others scaled in between
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([1.0, 2.0]) == [0.0, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

    # All negative numbers
    result = module_0.rescale_to_unit([-5.0, -3.0, -1.0])
    assert result == [0.0, 0.5, 1.0]

    # Unsorted input preserves order
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Floating point precision
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Single range check: all outputs within [0, 1]
    numbers = [3.5, -1.2, 7.8, 0.0, 2.2]
    result = module_0.rescale_to_unit(numbers)
    assert all(0.0 <= x <= 1.0 for x in result)
    assert min(result) == 0.0
    assert max(result) == 1.0

    # Result length matches input length
    assert len(result) == len(numbers)


# Generated at 2026-11-02 19:50:35.707174
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Test with a simple list of positive numbers
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

    # Test with two elements
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Test with negative numbers
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0, 1.0]) == [0.0, 1/3, 2/3, 1.0]

    # Test with unsorted input
    assert module_0.rescale_to_unit([3.0, 1.0, 2.0]) == [1.0, 0.0, 0.5]

    # Test with duplicate values
    assert module_0.rescale_to_unit([1.0, 1.0, 2.0]) == [0.0, 0.0, 1.0]

    # Test with float precision
    result = module_0.rescale_to_unit([0.0, 10.0, 5.0])
    assert result == [0.0, 1.0, 0.5]

    # Test that min maps to 0 and max maps to 1 for arbitrary input
    numbers = [17.3, -4.2, 8.8, 0.5, 23.1]
    result = module_0.rescale_to_unit(numbers)
    assert min(result) == 0.0
    assert max(result) == 1.0
    assert all(0.0 <= x <= 1.0 for x in result)

    # Test length preservation
    assert len(result) == len(numbers)

    # Test relative ordering is preserved
    scaled = module_0.rescale_to_unit([5.0, 1.0, 3.0])
    assert scaled[1] < scaled[2] < scaled[0]

    # Test division by zero when all elements are equal raises an error
    import pytest
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([4.0, 4.0, 4.0])


if __name__ == "__main__":
    test_rescale_to_unit()
    print("All tests passed!")

# Generated at 2026-11-02 19:52:24.745499
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: evenly spaced values map linearly to [0, 1]
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Smallest maps to 0, largest maps to 1
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]

    # Unsorted input still maps correctly
    assert module_0.rescale_to_unit([5.0, 3.0, 1.0]) == [1.0, 0.5, 0.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # All results lie within [0, 1]
    result = module_0.rescale_to_unit([3.7, 1.2, 9.4, 5.6])
    assert all(0.0 <= x <= 1.0 for x in result)

    # Min and max elements are mapped exactly to 0 and 1
    numbers = [3.7, 1.2, 9.4, 5.6]
    result = module_0.rescale_to_unit(numbers)
    assert result[numbers.index(min(numbers))] == 0.0
    assert result[numbers.index(max(numbers))] == 1.0

    # Floating point tolerance check
    result = module_0.rescale_to_unit([1.0, 2.0])
    assert abs(result[0] - 0.0) < 1e-9
    assert abs(result[1] - 1.0) < 1e-9

# Generated at 2026-11-02 19:54:29.588507
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear rescaling
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two elements: min -> 0, max -> 1
    assert module_0.rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]
    assert module_0.rescale_to_unit([4.0, 2.0]) == [1.0, 0.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-2.0, -1.0, 0.0]) == [0.0, 0.5, 1.0]

    # Unordered input still rescales correctly
    assert module_0.rescale_to_unit([5.0, 3.0, 1.0]) == [1.0, 0.5, 0.0]

    # Duplicated values
    assert module_0.rescale_to_unit([1.0, 1.0, 2.0]) == [0.0, 0.0, 1.0]

    # Non-exact values, compared with tolerance
    result = module_0.rescale_to_unit([10.0, 15.0, 13.0])
    expected = [0.0, 1.0, 0.6]
    assert all(abs(r - e) < 1e-9 for r, e in zip(result, expected))

    # Minimum becomes 0, maximum becomes 1, all values within [0, 1]
    numbers = [3.5, -2.1, 7.8, 0.0, 4.4]
    rescaled = module_0.rescale_to_unit(numbers)
    assert rescaled[1] == 0.0  # -2.1 is the minimum
    assert rescaled[2] == 1.0  # 7.8 is the maximum
    assert all(0.0 <= v <= 1.0 for v in rescaled)

    # All elements equal -> division by zero
    try:
        module_0.rescale_to_unit([3.0, 3.0, 3.0])
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

    # Empty list -> ValueError from min()
    try:
        module_0.rescale_to_unit([])
        assert False, "Expected ValueError"
    except ValueError:
        pass

# Generated at 2026-11-02 19:56:40.590806
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: linearly spaced values
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Values with a different range
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Unsorted input
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Two elements
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]

    # Floating point precision check
    result = module_0.rescale_to_unit([0.0, 1.0, 2.0, 3.0])
    assert result == pytest.approx([0.0, 1 / 3, 2 / 3, 1.0])

    # Output bounds: min maps to 0, max maps to 1
    numbers = [3.5, 7.2, 1.8, 9.9]
    result = module_0.rescale_to_unit(numbers)
    assert min(result) == 0.0
    assert max(result) == 1.0
    assert len(result) == len(numbers)

# Generated at 2026-11-02 19:58:05.901053
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: min maps to 0.0, max maps to 1.0, evenly spaced in between
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])

    # Middle value maps to 0.5
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == pytest.approx([0.0, 0.5, 1.0])

    # Negative numbers are handled correctly
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == pytest.approx([0.0, 0.5, 1.0])

    # Unsorted input still yields correct mapping per element
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == pytest.approx([1.0, 0.0, 0.5])

    # Two-element list
    assert module_0.rescale_to_unit([10.0, 20.0]) == pytest.approx([0.0, 1.0])

    # Non-uniform spacing
    assert module_0.rescale_to_unit([0.0, 1.0, 10.0]) == pytest.approx([0.0, 0.1, 1.0])

    # Result bounds hold for arbitrary input: min -> 0, max -> 1, all in [0, 1]
    numbers = [3.5, 7.2, 1.1, 9.9, -2.4]
    result = module_0.rescale_to_unit(numbers)
    assert result[3] == pytest.approx(1.0)
    assert result[4] == pytest.approx(0.0)
    assert all(0.0 <= x <= 1.0 for x in result)

    # Length of output matches length of input
    assert len(module_0.rescale_to_unit(numbers)) == len(numbers)
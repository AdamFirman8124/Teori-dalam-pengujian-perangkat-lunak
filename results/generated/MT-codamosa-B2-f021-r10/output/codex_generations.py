

# Generated at 2026-11-02 10:40:23.706573
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic linear sequence
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Smaller list
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

    # Unsorted input: min maps to 0.0, max maps to 1.0
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]

    # Two elements
    assert module_0.rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]

    # Boundaries and length preservation on arbitrary floats
    numbers = [3.5, 7.2, 1.1, 9.9]
    result = module_0.rescale_to_unit(numbers)
    assert len(result) == len(numbers)
    assert abs(min(result)) < 1e-9
    assert abs(max(result) - 1.0) < 1e-9
    assert all(0.0 <= x <= 1.0 for x in result)

# Generated at 2026-11-02 10:41:25.249105
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: values spread evenly
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    # Simple case
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]
    # Descending order
    assert module_0.rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]
    # Two elements
    assert module_0.rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]
    # Negative numbers
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]
    # Duplicates of min/max values
    assert module_0.rescale_to_unit([1.0, 1.0, 5.0]) == [0.0, 0.0, 1.0]
    # All values preserved in order (length check)
    assert len(module_0.rescale_to_unit([3.0, 7.0, 1.5, 9.2])) == 4

# Generated at 2026-11-02 10:43:23.624994
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic case: values spread between min and max
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    # Min value maps to 0, max value maps to 1
    result = module_0.rescale_to_unit([2.0, 4.0, 6.0])
    assert result[0] == 0.0
    assert result[-1] == 1.0
    assert abs(result[1] - 0.5) < 1e-9
    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-5.0, -3.0]) == [0.0, 1.0]
    # Two elements
    assert module_0.rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]
    # Unsorted input preserves order
    assert module_0.rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]
    # Values already within [0, 1]
    assert module_0.rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]
    assert module_0.rescale_to_unit([0.2, 0.4, 0.8]) == [0.0, 0.3333333333333333, 1.0]
    # Duplicated min/max values
    assert module_0.rescale_to_unit([3.0, 3.0, 7.0, 7.0]) == [0.0, 0.0, 1.0, 1.0]
    # Floating point precision check
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0])
    assert all(0.0 <= x <= 1.0 for x in result)
    assert abs(sum(result) - 1.5) < 1e-9
    # Result length matches input length
    assert len(module_0.rescale_to_unit([1.5, 2.5, 3.5, 4.5])) == 4
    print("All tests passed!")


if __name__ == "__main__":
    test_rescale_to_unit()

# Generated at 2026-11-02 10:45:07.461900
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic ascending case
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Two-element list
    assert module_0.rescale_to_unit([2.0, 49.9]) == [0.0, 1.0]

    # Descending order
    assert module_0.rescale_to_unit([100.0, 49.9]) == [1.0, 0.0]

    # Unsorted input
    assert module_0.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

    # Different offset, same spacing
    assert module_0.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

    # Mixed positive/negative values (approximate comparison)
    result = module_0.rescale_to_unit([2.0, -9.0, 1.0, 3.0, -4.0, 5.0])
    expected = [11.0 / 14.0, 0.0, 10.0 / 14.0, 12.0 / 14.0, 5.0 / 14.0, 1.0]
    assert all(abs(r - e) < 1e-9 for r, e in zip(result, expected))

    # Min maps to 0.0, max maps to 1.0, everything within [0, 1]
    for data in ([3.0, -1.5, 7.2, 0.0], [-5.0, -2.0, -10.0]):
        result = module_0.rescale_to_unit(data)
        assert min(result) == 0.0
        assert max(result) == 1.0
        assert all(0.0 <= x <= 1.0 for x in result)

    # Degenerate case: constant list -> division by zero
    try:
        module_0.rescale_to_unit([4.0, 4.0, 4.0])
        assert False, "Expected ZeroDivisionError for constant input"
    except ZeroDivisionError:
        pass

    print("test_rescale_to_unit passed")


if __name__ == "__main__":
    test_rescale_to_unit()

# Generated at 2026-11-02 10:47:09.113690
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # Basic increasing sequence
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

    # Negative numbers
    assert module_0.rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

    # Two elements
    assert module_0.rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]
    assert module_0.rescale_to_unit([10.0, 0.0]) == [1.0, 0.0]

    # Decreasing sequence
    assert module_0.rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]) == [1.0, 0.75, 0.5, 0.25, 0.0]

    # Unsorted input
    assert module_0.rescale_to_unit([3.0, 1.0, 2.0]) == [1.0, 0.0, 0.5]

    # Fractional values with tolerance
    result = module_0.rescale_to_unit([2.5, 3.5, 4.5])
    assert abs(result[0] - 0.0) < 1e-9
    assert abs(result[1] - 0.5) < 1e-9
    assert abs(result[2] - 1.0) < 1e-9

    # All identical values -> division by zero
    import pytest
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([3.0, 3.0, 3.0])

    # Single element -> division by zero
    with pytest.raises(ZeroDivisionError):
        module_0.rescale_to_unit([42.0])

    # Output bounds check for arbitrary input
    data = [7.13, -2.4, 0.0, 15.9, 3.3]
    res = module_0.rescale_to_unit(data)
    assert min(res) == 0.0
    assert max(res) == 1.0
    assert all(0.0 <= v <= 1.0 for v in res)
# nonce:503643f0
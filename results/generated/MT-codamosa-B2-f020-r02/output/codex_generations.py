

# Generated at 2026-11-02 21:57:58.692375
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair at the start
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Longer list, closest pair at the start
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Unsorted input, result should still be sorted tuple
    assert module_0.find_closest_elements([3.0, 1.0, 2.0]) == (1.0, 2.0)

    # Two elements only
    assert module_0.find_closest_elements([5.0, 3.0]) == (3.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -5.0, -2.0]) == (-2.0, -1.0)

    # Duplicated value yields zero distance pair
    assert module_0.find_closest_elements([1.0, 5.0, 1.0]) == (1.0, 1.0)

    # Closest pair in the middle of the list
    assert module_0.find_closest_elements([10.0, 20.0, 30.0, 30.5, 40.0]) == (30.0, 30.5)

    # Floating point precision
    assert module_0.find_closest_elements([0.1, 0.11, 0.5]) == (0.1, 0.11)

    # Result is a tuple of floats
    result = module_0.find_closest_elements([1.0, 2.0, 3.0])
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] <= result[1]

    print("All tests passed!")


test_find_closest_elements()

# Generated at 2026-11-02 21:59:01.645427
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case with distinct closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Case with duplicate values being the closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Only two elements
    assert module_0.find_closest_elements([1.1, 2.2]) == (1.1, 2.2)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0, 5.0]) == (-2.0, -1.0)

    # Closest pair with small fractional difference
    assert module_0.find_closest_elements([10.0, 10.1, 20.0]) == (10.0, 10.1)

    # Unsorted input; result must be ordered (smaller, larger)
    result = module_0.find_closest_elements([3.5, 1.2, 4.0, 1.0])
    assert result == (1.0, 1.2)
    assert result[0] <= result[1]

    # All identical elements
    assert module_0.find_closest_elements([7.0, 7.0, 7.0]) == (7.0, 7.0)

    # Closest pair straddling zero
    assert module_0.find_closest_elements([-0.5, 0.5, 5.0]) == (-0.5, 0.5)

    # Single element: no valid pair exists
    assert module_0.find_closest_elements([5.0]) is None

    print("All tests passed!")


test_find_closest_elements()

# Generated at 2026-11-02 22:00:44.832837
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Test with a simple sorted list
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Test with an unsorted list
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # Test where closest pair is at the end of the list
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0)

    # Test with duplicate elements (zero distance)
    assert module_0.find_closest_elements([1.0, 1.0, 2.0]) == (1.0, 1.0)

    # Test with all negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -1.0)

    # Test with mixed positive and negative numbers
    assert module_0.find_closest_elements([-1.0, 1.0, 0.5]) == (0.5, 1.0)

    # Test with exactly two elements
    assert module_0.find_closest_elements([5.0, 10.0]) == (5.0, 10.0)

    # Test with unsorted two elements (result must be sorted tuple)
    assert module_0.find_closest_elements([10.0, 5.0]) == (5.0, 10.0)

    # Test that the result is a sorted tuple
    result = module_0.find_closest_elements([3.0, 1.0, 2.0])
    assert result == (1.0, 2.0)
    assert isinstance(result, tuple)
    assert result[0] <= result[1]

    # Test with floats having very close values
    assert module_0.find_closest_elements([1.0, 1.001, 5.0]) == (1.0, 1.001)

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-11-02 22:04:03.945685
# Unit test for function find_closest_elements
def test_find_closest_elements():from pytest import approx

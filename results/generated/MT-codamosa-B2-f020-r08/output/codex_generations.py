

# Generated at 2026-11-02 08:18:59.910347
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from math import isclose

    # Basic case: closest pair among distinct values
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert isclose(result[0], 2.0) and isclose(result[1], 2.2)

    # Duplicates: distance zero
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert isclose(result[0], 2.0) and isclose(result[1], 2.0)

    # Exactly two elements
    result = module_0.find_closest_elements([1.0, 1.0])
    assert isclose(result[0], 1.0) and isclose(result[1], 1.0)

    # Closest pair not at the start
    result = module_0.find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1])
    assert isclose(result[0], 2.2) and isclose(result[1], 3.1)

    # Unsorted input
    result = module_0.find_closest_elements([10.0, 3.0, 7.5, 8.0, 1.0])
    assert isclose(result[0], 7.5) and isclose(result[1], 8.0)

    # Negative numbers
    result = module_0.find_closest_elements([-1.0, -1.5, 2.0, 5.0])
    assert isclose(result[0], -1.5) and isclose(result[1], -1.0)

    # Result is always sorted ascending
    result = module_0.find_closest_elements([5.0, 1.0, 4.9])
    assert result == tuple(sorted(result))

# Generated at 2026-11-02 08:19:59.738760
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.1, 2.2]) == (1.1, 2.2)
    assert module_0.find_closest_elements([5.0, 3.0, 1.0]) == (3.0, 5.0)
    assert module_0.find_closest_elements([1.0, 1.1, 10.0, 20.0]) == (1.0, 1.1)
    assert module_0.find_closest_elements([-5.0, -4.0, 100.0]) == (-5.0, -4.0)
    assert module_0.find_closest_elements([2.0, 2.0]) == (2.0, 2.0)

# Generated at 2026-11-02 08:20:31.232854
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Test with a simple list
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1.0, 2.0)
    # Test with unsorted list
    assert module_0.find_closest_elements([4.0, 1.0, 3.0, 2.0]) == (1.0, 2.0)
    # Test with negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -3.0)
    # Test with mixed positive and negative numbers
    assert module_0.find_closest_elements([1.0, -1.0, 5.0]) == (-1.0, 1.0)
    # Test with two elements
    assert module_0.find_closest_elements([10.0, 20.0]) == (10.0, 20.0)
    # Test with duplicates
    assert module_0.find_closest_elements([1.0, 1.0, 2.0]) == (1.0, 1.0)
    # Test with floating point values
    assert module_0.find_closest_elements([1.5, 2.5, 3.75]) == (1.5, 2.5)
    # Test result is sorted tuple
    result = module_0.find_closest_elements([5.0, 1.0, 0.9])
    assert result == (0.9, 1.0)
    assert result[0] <= result[1]
    # Test with larger list
    assert module_0.find_closest_elements([100.0, 1.0, 50.0, 1.5]) == (1.0, 1.5)

# Generated at 2026-11-02 08:21:45.787623
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]) == (3.0, 3.0)

# Generated at 2026-11-02 08:22:05.952259
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2, 3.3]) == (3.9, 4.0)
    assert module_0.find_closest_elements([1.0, 2.0, 5.3, 4.0, 5.0]) == (2.0, 1.0) or module_0.find_closest_elements([1.0, 2.0, 5.3, 4.0, 5.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0) or module_0.find_closest_elements([1.0, 2.0, 3.0]) == (2.0, 3.0)

    # Two elements
    assert module_0.find_closest_elements([5.0, 3.0]) == (3.0, 5.0)
    assert module_0.find_closest_elements([7.5, 7.6]) == (7.5, 7.6)

    # Duplicates (distance zero)
    assert module_0.find_closest_elements([1.0, 1.0, 2.0]) == (1.0, 1.0)
    assert module_0.find_closest_elements([4.0, 4.0, 4.0]) == (4.0, 4.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 2.0]) == (-1.0, -1.5)
    assert module_0.find_closest_elements([-5.0, -3.0, -2.9]) == (-3.0, -2.9)

    # Mixed positive/negative
    result = module_0.find_closest_elements([-0.5, 0.5, 10.0])
    assert result == (-0.5, 0.5)

    # Result should always be sorted and a tuple of two floats
    result = module_0.find_closest_elements([100.0, 0.1, 0.2])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (0.1, 0.2)


test_find_closest_elements()
print("All tests passed!")
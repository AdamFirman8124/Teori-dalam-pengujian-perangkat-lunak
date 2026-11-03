

# Generated at 2026-11-03 05:11:21.277171
# Unit test for function find_closest_elements
def test_find_closest_elements():
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)
    assert module_0.find_closest_elements([1.0, 1.0, 5.0]) == (1.0, 1.0)
    assert module_0.find_closest_elements([10.0, 10.0, 10.0]) == (10.0, 10.0)
    assert module_0.find_closest_elements([-1.0, -1.5, 5.0]) == (-1.5, -1.0)
    assert module_0.find_closest_elements([0.5, 3.5, 2.4, 1.5]) == (1.5, 2.4)
    assert module_0.find_closest_elements([1.1, 1.15]) == (1.1, 1.15)
    assert module_0.find_closest_elements([3.5, -2.5, 7.0, -2.6]) == (-2.6, -2.5)
    assert module_0.find_closest_elements([100.0, 0.0, 50.0, 50.5]) == (50.0, 50.5)

# Generated at 2026-11-03 05:13:21.139804
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Two elements, already sorted
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # Two elements, unsorted input — result must be sorted
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # Multiple elements, closest pair in the middle
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate elements form the closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # All identical elements
    assert module_0.find_closest_elements([4.0, 4.0, 4.0]) == (4.0, 4.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 5.0]) == (-1.1, -1.0)

    # Mixed positive and negative numbers
    assert module_0.find_closest_elements([-10.0, 10.0, 0.1, -0.1]) == (-0.1, 0.1)

    # Closest pair at the extremes of the list
    assert module_0.find_closest_elements([100.0, 0.0, 50.0, 100.5]) == (100.0, 100.5)

    # Result is always a sorted tuple
    result = module_0.find_closest_elements([3.0, 1.0, 2.9])
    assert result == (2.9, 3.0)
    assert result[0] <= result[1]

    # Floating point closeness
    assert module_0.find_closest_elements([0.1, 0.10000001, 100.0]) == (0.1, 0.10000001)

    # Single element list has no pair — returns None
    assert module_0.find_closest_elements([1.0]) is None

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()
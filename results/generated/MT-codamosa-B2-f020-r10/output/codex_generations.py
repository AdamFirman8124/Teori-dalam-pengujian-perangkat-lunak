

# Generated at 2026-10-25 08:34:52.612906
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:34:55.028092
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:34:57.446211
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:34:59.870666
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:35:02.281909
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:35:04.698359
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:35:07.118483
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:35:09.542621
# Unit test for function find_closest_elements

# Generated at 2026-10-25 08:35:16.056225
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: two closest values out of order
    result = module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2), f"Expected (2.0, 2.2), got {result}"

    # Closest pair with duplicates
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2), f"Expected (2.0, 2.2), got {result}"

    # Minimal list of two elements
    result = module_0.find_closest_elements([3.5, 1.2])
    assert result == (1.2, 3.5), f"Expected (1.2, 3.5), got {result}"

    # Exact duplicates are the closest pair
    result = module_0.find_closest_elements([5.0, 5.0, 10.0])
    assert result == (5.0, 5.0), f"Expected (5.0, 5.0), got {result}"

    # Negative numbers
    result = module_0.find_closest_elements([-1.0, -1.1, 5.0])
    assert result == (-1.1, -1.0), f"Expected (-1.1, -1.0), got {result}"

    # Result must be sorted regardless of input order
    result = module_0.find_closest_elements([10.0, 8.0, 8.5])
    assert result == (8.0, 8.5), f"Expected (8.0, 8.5), got {result}"

    # Returned value is a tuple of floats
    result = module_0.find_closest_elements([1.0, 1.5])
    assert isinstance(result, tuple) and len(result) == 2
    assert result == (1.0, 1.5), f"Expected (1.0, 1.5), got {result}"

# Generated at 2026-10-25 08:35:17.457175
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-10-25 08:35:18.964130
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic cases
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)

    # Two elements â the only pair
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicates â zero distance
    assert module_0.find_closest_elements([5.0, 5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 10.0]) == (-1.1, -1.0)

    # Unsorted input, closest pair not at the start
    assert module_0.find_closest_elements([100.0, 0.0, 50.1, 50.0]) == (50.0, 50.1)

    # Result must always be sorted
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (3.0, 7.0) and result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()
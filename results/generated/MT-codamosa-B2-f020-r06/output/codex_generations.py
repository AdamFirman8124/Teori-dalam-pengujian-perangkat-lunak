

# Generated at 2026-11-01 22:04:42.169350
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # nonce:1600ceef
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 3.1]) == (3.0, 3.1)
    assert module_0.find_closest_elements([10.0, 10.0]) == (10.0, 10.0)
    assert module_0.find_closest_elements([5.0, 1.0, 3.0]) == (1.0, 3.0)
    assert module_0.find_closest_elements([-1.0, 1.0, 0.5]) == (0.5, 1.0)
    assert module_0.find_closest_elements([100.0, -100.0, 99.5]) == (99.5, 100.0)
    assert module_0.find_closest_elements([0.1, 0.2, 0.3, 0.11]) == (0.1, 0.11)

# Generated at 2026-11-01 22:05:21.820555
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: consecutive numbers
    result = module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (3.9, 4.0), f"Expected (3.9, 4.0), got {result}"

    # Duplicated minimum distance handled correctly
    result = module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0])
    assert result == (4.0, 5.0), f"Expected (4.0, 5.0), got {result}"

    # Closest pair not at the beginning
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2), f"Expected (2.0, 2.2), got {result}"

    # Negative numbers
    result = module_0.find_closest_elements([-1.0, -2.0, -3.0])
    assert result == (-2.0, -1.0), f"Expected (-2.0, -1.0), got {result}"

    # Two element list
    result = module_0.find_closest_elements([10.5, 7.5])
    assert result == (7.5, 10.5), f"Expected (7.5, 10.5), got {result}"

    # Result should always be sorted ascending
    result = module_0.find_closest_elements([5.0, 1.0, 4.5])
    assert result == (4.5, 5.0), f"Expected (4.5, 5.0), got {result}"
    assert result[0] <= result[1], "Pair must be sorted"

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-11-01 22:06:10.061198
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # nonce:93577c0f
    # Exactly two elements
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

    # Closest pair in the middle of the list
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate values form the closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # All identical values
    assert module_0.find_closest_elements([3.0, 3.0, 3.0]) == (3.0, 3.0)

    # Negative numbers
    assert module_0.find_closest_elements([-10.0, -9.0, -20.0, -30.0]) == (-10.0, -9.0)

    # Mixed positive and negative numbers
    assert module_0.find_closest_elements([5.0, -5.0, 4.9, -4.9]) == (4.9, 5.0)

    # Small fractional difference
    assert module_0.find_closest_elements([1.1, 1.15, 5.5]) == (1.1, 1.15)

    # Result must be a sorted tuple regardless of input order
    result = module_0.find_closest_elements([10.0, 8.0, 12.0])
    assert isinstance(result, tuple)
    assert result == (8.0, 10.0)
    assert result[0] <= result[1]

    # Unsorted input list
    assert module_0.find_closest_elements([7.0, 3.0, 1.0, 9.0, 2.5]) == (1.0, 2.5)

# Generated at 2026-11-01 22:06:38.515807
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair in the middle
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Closest pair at the end
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0)

    # Larger list with close pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate values yield equal pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Only two elements
    assert module_0.find_closest_elements([1.1, 2.2]) == (1.1, 2.2)

    # Identical elements only
    assert module_0.find_closest_elements([5.0, 5.0]) == (5.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 3.0]) == (-1.5, -1.0)

    # Unsorted input still returns sorted tuple
    result = module_0.find_closest_elements([10.0, 1.0, 1.5, 20.0])
    assert result == (1.0, 1.5)
    assert result[0] <= result[1]

    # Result is always a tuple of two floats
    result = module_0.find_closest_elements([3.0, 7.0, 3.5])
    assert isinstance(result, tuple) and len(result) == 2
    assert all(isinstance(x, float) for x in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-11-01 22:07:00.801505
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair among several distinct values
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # Two elements only
    assert module_0.find_closest_elements([10.0, 20.0]) == (10.0, 20.0)

    # Result must be sorted in ascending order regardless of input order
    assert module_0.find_closest_elements([4.0, 3.9]) == (3.9, 4.0)
    assert module_0.find_closest_elements([20.0, 10.0]) == (10.0, 20.0)

    # Duplicate values yield zero-distance pair
    assert module_0.find_closest_elements([1.0, 1.0, 5.0]) == (1.0, 1.0)
    assert module_0.find_closest_elements([2.0, 2.0, 2.0]) == (2.0, 2.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0, -2.5]) == (-2.5, -2.0)

    # Mixed positive/negative numbers
    assert module_0.find_closest_elements([-5.0, 5.0, 5.5, -100.0]) == (5.0, 5.5)

    # Very close fractional values
    assert module_0.find_closest_elements([0.1, 0.10000001, 50.0]) == (0.1, 0.10000001)
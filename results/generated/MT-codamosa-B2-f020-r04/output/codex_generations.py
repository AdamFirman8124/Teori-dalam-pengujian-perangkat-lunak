

# Generated at 2026-11-02 21:48:00.739701
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case with multiple elements
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    # Another basic case
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0)
    # List with exactly two identical elements
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)
    # Two distinct elements
    assert module_0.find_closest_elements([3.0, 7.0]) == (3.0, 7.0)
    # Closest pair at the start of the list
    assert module_0.find_closest_elements([1.0, 1.1, 10.0, 20.0]) == (1.0, 1.1)
    # Closest pair at the end of the list
    assert module_0.find_closest_elements([1.0, 5.0, 8.0, 8.1]) == (8.0, 8.1)
    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 3.0, 10.0]) == (-1.5, -1.0)
    # Mixed negative and positive numbers
    assert module_0.find_closest_elements([-2.0, 2.0, -1.9, 5.0]) == (-2.0, -1.9)
    # Duplicate values that are closest
    assert module_0.find_closest_elements([4.0, 4.0, 10.0, 20.0]) == (4.0, 4.0)
    # Unsorted input list
    assert module_0.find_closest_elements([10.0, 2.0, 7.5, 2.3]) == (2.0, 2.3)
    # Result is always sorted tuple
    result = module_0.find_closest_elements([5.5, 1.0, 5.2])
    assert result == (5.2, 5.5)
    assert result[0] <= result[1]
    # Floats with small differences
    assert module_0.find_closest_elements([0.1, 0.10001, 5.0]) == (0.1, 0.10001)

# Generated at 2026-11-02 21:49:16.941889
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair among several numbers
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2)

    # Duplicates: identical closest elements
    result = module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert result == (2.0, 2.0)

    # Two elements only
    result = module_0.find_closest_elements([10.0, 20.0])
    assert result == (10.0, 20.0)

    # Negative numbers
    result = module_0.find_closest_elements([-1.0, -2.0, -3.0])
    assert result == (-2.0, -1.0)

    # Very close floats
    result = module_0.find_closest_elements([1.0, 1.1, 5.0])
    assert result == (1.0, 1.1)

    # Unsorted input: result must be sorted ascending
    result = module_0.find_closest_elements([3.0, 1.0, 2.0])
    assert result == (2.0, 3.0)
    assert result[0] <= result[1]

    # Result is a tuple of floats
    assert isinstance(result, tuple)
    assert len(result) == 2

# Generated at 2026-11-02 21:50:48.989851
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair among distinct values
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    # Duplicate values form the closest pair (distance zero)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    # Closest pair not adjacent in list order
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    # Result is sorted regardless of input order
    assert module_0.find_closest_elements([5.9, 4.0, 1.0, 2.0, 5.0]) == (5.0, 5.9)
    # Multiple close pairs, smallest distance wins
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2, 3.1]) == (3.0, 3.1)
    # Two-element list
    assert module_0.find_closest_elements([10.5, 3.2]) == (3.2, 10.5)
    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 5.0]) == (-1.1, -1.0)

# Generated at 2026-11-02 21:52:14.126125
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic cases with a unique closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # Duplicate values yield distance zero
    assert module_0.find_closest_elements([1.0, 1.0, 2.0]) == (1.0, 1.0)
    assert module_0.find_closest_elements([2.0, 2.0, 2.0]) == (2.0, 2.0)

    # Two-element list (minimum valid input)
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)
    assert module_0.find_closest_elements([5.0, 4.0]) == (4.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 5.0]) == (-1.5, -1.0)
    assert module_0.find_closest_elements([-10.0, -9.9, -20.0]) == (-10.0, -9.9)

    # Small fractional differences
    assert module_0.find_closest_elements([10.0, 10.05, 20.0]) == (10.0, 10.05)

    # Return type and ordering guarantees
    result = module_0.find_closest_elements([7.0, 3.0, 3.1])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (3.0, 3.1)

# Generated at 2026-11-02 21:53:18.393541
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case with distinct floats
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Pair spanning a larger gap elsewhere
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-10.0, -9.0, 0.0, 5.0]) == (-10.0, -9.0)

    # Duplicate values (distance zero)
    assert module_0.find_closest_elements([3.0, 1.0, 3.0, 7.0]) == (3.0, 3.0)

    # Only two elements
    assert module_0.find_closest_elements([2.5, 1.5]) == (1.5, 2.5)

    # Result pair is always sorted (smaller first)
    result = module_0.find_closest_elements([10.0, 3.0, 3.1, 100.0])
    assert result == (3.0, 3.1)
    assert result[0] <= result[1]

    # Floats with fractional precision
    assert module_0.find_closest_elements([0.1, 0.11, 0.5]) == (0.1, 0.11)

    # Mixed positive/negative around zero
    assert module_0.find_closest_elements([-1.0, 0.5, 1.0]) == (0.5, 1.0)

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()
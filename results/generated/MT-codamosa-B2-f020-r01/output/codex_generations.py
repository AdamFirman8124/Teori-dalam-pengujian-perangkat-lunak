

# Generated at 2026-11-02 09:17:48.242618
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair in a simple list
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    # Duplicate values yield a pair of equal elements (distance 0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    # Exactly two elements
    assert module_0.find_closest_elements([1.1, 2.2]) == (1.1, 2.2)
    # Result is sorted regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)
    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.1, 5.0]) == (-1.1, -1.0)
    # Mixed positives and negatives
    assert module_0.find_closest_elements([3.5, -2.0, 1.0, 1.5]) == (1.0, 1.5)
    # Ties: first pair encountered in iteration order is kept
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1.0, 2.0)
    # Duplicate not at the start of the list
    assert module_0.find_closest_elements([0.5, 3.0, 0.5]) == (0.5, 0.5)
    # Single element cannot form a pair
    assert module_0.find_closest_elements([1.0]) is None

# Generated at 2026-11-02 09:18:05.826761
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case with distinct closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate elements -> closest pair is the duplicates
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # All elements distinct, evenly spaced -> first minimal pair encountered
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == (1.0, 2.0)

    # Three elements
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Two identical elements
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # Two different elements
    assert module_0.find_closest_elements([3.5, 1.2]) == (1.2, 3.5)

    # Unsorted input, closest pair near the end
    assert module_0.find_closest_elements([10.0, 1.0, 5.0, 5.1]) == (5.0, 5.1)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -1.5, 2.0, 3.0]) == (-1.5, -1.0)

    # Single element -> no pair exists, returns None
    assert module_0.find_closest_elements([1.0]) is None

    # Empty list -> returns None
    assert module_0.find_closest_elements([]) is None

    # Zero-distance pair among many
    assert module_0.find_closest_elements([0.5, 0.5, 9.9, 100.0]) == (0.5, 0.5)

    # Floats with small differences
    assert module_0.find_closest_elements([1.0001, 1.0002, 5.0]) == (1.0001, 1.0002)

# Generated at 2026-11-02 09:18:50.168854
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: consecutive integers, closest pair is (1.0, 2.0)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1.0, 2.0)

    # Unsorted input, unique minimum distance
    assert module_0.find_closest_elements([1.0, 5.0, 10.0]) == (1.0, 5.0)

    # Pair should be returned in sorted order regardless of input order
    assert module_0.find_closest_elements([10.0, 1.0, 2.0]) == (1.0, 2.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -5.0]) == (-2.0, -1.0)

    # Mixed positive and negative numbers
    assert module_0.find_closest_elements([-10.0, 10.0, 9.0]) == (9.0, 10.0)

    # Only two elements: must return them sorted
    assert module_0.find_closest_elements([3.0, 1.0]) == (1.0, 3.0)

    # Duplicate values: distance zero pair wins
    assert module_0.find_closest_elements([2.0, 7.0, 2.0]) == (2.0, 2.0)

    # Floats with small differences
    assert module_0.find_closest_elements([1.5, 1.6, 100.0]) == (1.5, 1.6)

    # Duplicates among larger list
    assert module_0.find_closest_elements([5.0, 1.0, 1.0, 8.0]) == (1.0, 1.0)

    # Result should be a tuple of two floats in ascending order
    result = module_0.find_closest_elements([4.0, 2.0, 9.0, 2.5])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]
    assert result == (2.0, 2.5)

# Generated at 2026-11-02 09:19:26.416991
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # nonce:fc3c98b0
    # Basic increasing list
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Duplicates close together
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -1.0)

    # Unsorted input
    assert module_0.find_closest_elements([5.0, 1.0, 3.0]) == (3.0, 5.0)

    # Two elements only
    assert module_0.find_closest_elements([10.0, 4.0]) == (4.0, 10.0)

    # Equal elements -> zero distance
    assert module_0.find_closest_elements([2.0, 2.0]) == (2.0, 2.0)

    # Mixed positives and negatives
    assert module_0.find_closest_elements([-5.0, 0.0, 5.0, -4.8]) == (-5.0, -4.8)

    # Result is always a sorted tuple
    result = module_0.find_closest_elements([3.0, 1.0, 2.5])
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-11-02 09:21:24.701427
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair among ascending numbers
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate values should be the closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Two-element list
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)
    assert module_0.find_closest_elements([10.0, 5.0]) == (5.0, 10.0)

    # Unsorted input, result should be sorted pair
    assert module_0.find_closest_elements([5.0, 1.0, 3.0]) == (1.0, 3.0)
    assert module_0.find_closest_elements([2.0, 4.0, 1.0, 3.0]) == (1.0, 2.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, 0.0]) == (-2.0, -1.0)
    assert module_0.find_closest_elements([-5.0, -1.0, -3.0]) == (-3.0, -1.0)

    # Mixed positive and negative
    assert module_0.find_closest_elements([3.0, -3.0, 1.0]) == (1.0, 3.0)

    # Floats with fractional parts
    assert module_0.find_closest_elements([0.5, 0.6, 10.0]) == (0.5, 0.6)

    # Result must always be a sorted tuple of two elements
    result = module_0.find_closest_elements([7.0, 3.0, 9.0])
    assert result == tuple(sorted(result))
    assert len(result) == 2


# Generated at 2026-11-03 00:57:54.420589
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case with a clearly closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicate values yield a pair with zero distance
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Two elements only
    assert module_0.find_closest_elements([1.0, 5.0]) == (1.0, 5.0)

    # Result must be sorted regardless of input order
    assert module_0.find_closest_elements([5.0, 1.0]) == (1.0, 5.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -1.0)

    # Mixed signs
    assert module_0.find_closest_elements([-1.0, 1.0, 0.5]) == (0.5, 1.0)

    # Floats with small differences
    assert module_0.find_closest_elements([1.5, 1.6, 3.0]) == (1.5, 1.6)

    # All identical elements
    assert module_0.find_closest_elements([7.0, 7.0, 7.0]) == (7.0, 7.0)

    # Unsorted input with negatives and positives
    assert module_0.find_closest_elements([3.0, -1.0, 2.0, 5.0]) == (2.0, 3.0)

    # Return type check
    result = module_0.find_closest_elements([10.0, 9.9, 1.0])
    assert isinstance(result, tuple)
    assert result == (9.9, 10.0)

    print("All tests passed!")


test_find_closest_elements()

# Generated at 2026-11-03 00:58:33.500394
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Simple case with three elements
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Case where closest pair is in the middle
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # Case where closest pair is near the end
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # Case with a non-obvious closest pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Two-element list
    assert module_0.find_closest_elements([1.1, 2.2]) == (1.1, 2.2)

    # Duplicate values
    assert module_0.find_closest_elements([1.0, 1.0]) == (1.0, 1.0)

    # Duplicate values in a longer list
    assert module_0.find_closest_elements([5.0, 3.0, 3.0, 8.0]) == (3.0, 3.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, 0.5]) == (-1.0, 0.5)

    # Result should be sorted regardless of input order
    assert module_0.find_closest_elements([10.0, 9.5, 1.0]) == (9.5, 10.0)

    # Unsorted input
    assert module_0.find_closest_elements([4.0, 1.0, 3.0, 2.0]) == (1.0, 2.0)

    # Result is a tuple of two floats
    result = module_0.find_closest_elements([1.0, 2.0, 3.0])
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("test_find_closest_elements passed!")


if __name__ == "__main__":
    test_find_closest_elements()

# Generated at 2026-11-03 00:59:00.756219
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair in ascending order
    assert module_0.find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)

    # Duplicated closest elements
    assert module_0.find_closest_elements([1.0, 2.0, 3.4, 5.4, 2.0]) == (2.0, 2.0)

    # Unsorted input
    assert module_0.find_closest_elements([3.0, 1.0, 2.0]) == (1.0, 2.0)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -1.0)

    # Mixed positive and negative
    assert module_0.find_closest_elements([-5.0, 5.0, 4.9]) == (4.9, 5.0)

    # Two elements only
    assert module_0.find_closest_elements([10.0, 3.0]) == (3.0, 10.0)

    # Zero distance pair wins over others
    assert module_0.find_closest_elements([1.5, 1.5, 100.0]) == (1.5, 1.5)

    # Fractional values
    assert module_0.find_closest_elements([0.1, 0.11, 0.5]) == (0.1, 0.11)

    # Closest pair is in the middle of the list
    assert module_0.find_closest_elements([100.0, 50.0, 50.5, 0.0]) == (50.0, 50.5)

    # Result is always sorted (smaller, larger)
    result = module_0.find_closest_elements([7.0, 3.0, 8.0])
    assert result == (7.0, 8.0)
    assert result[0] <= result[1]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()
# nonce:6d6e48bd

# Generated at 2026-11-03 00:59:53.267590
# Unit test for function find_closest_elements
def test_find_closest_elements():
    # Basic case: closest pair in a sorted list
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Duplicates yield a zero-distance pair
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Unsorted input
    assert module_0.find_closest_elements([1.0, 2.0, 5.0, 4.0, 3.0, 2.2]) == (2.0, 2.2)

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-3.0, -2.0)

    # Only two elements — returned in sorted order
    assert module_0.find_closest_elements([10.0, 3.5]) == (3.5, 10.0)

    # Closest pair straddles far-apart values
    assert module_0.find_closest_elements([0.0, 100.0, 100.5]) == (100.0, 100.5)

    # Result is always a sorted tuple
    result = module_0.find_closest_elements([5.0, 1.0, 4.5])
    assert result[0] <= result[1]

    # Verify the returned pair truly has the minimal distance
    a, b = module_0.find_closest_elements([3.1, 7.5, 2.9, 100.0])
    assert abs(a - b) == pytest.approx(0.2)

    # Mixed positive/negative numbers
    assert module_0.find_closest_elements([-5.0, 5.0, 4.8, 0.1]) == (4.8, 5.0)

# Generated at 2026-11-03 01:00:17.118232
# Unit test for function find_closest_elements
def test_find_closest_elements():
    from typing import List, Tuple

    # Basic case: closest pair in a simple list
    assert module_0.find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # Closest pair appears earlier in the list
    assert module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (1.8, 2.0) or \
           module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.9, 5.0) or \
           module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9) or \
           module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (4.0, 5.0) or \
           module_0.find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (2.0, 1.0)

    # Duplicate values: distance zero
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert module_0.find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Exact duplicates anywhere in the list
    assert module_0.find_closest_elements([5.0, 5.0]) == (5.0, 5.0)
    assert module_0.find_closest_elements([3.5, 1.2, 3.5, 7.8]) == (3.5, 3.5)

    # Two-element list
    assert module_0.find_closest_elements([1.0, 2.0]) == (1.0, 2.0)
    assert module_0.find_closest_elements([2.0, 1.0]) == (1.0, 2.0)  # result is sorted

    # Negative numbers
    assert module_0.find_closest_elements([-1.0, -2.0, -3.0]) == (-2.0, -1.0)
    assert module_0.find_closest_elements([-5.5, -5.6, 10.0]) == (-5.6, -5.5)

    # Mixed positive and negative numbers
    assert module_0.find_closest_elements([-1.0, 1.0, 0.5]) == (0.5, 1.0)

    # Floating point precision
    assert module_0.find_closest_elements([0.1, 0.2, 0.3000001]) == (0.2, 0.3000001)

    # Closest pair at the end of the list
    assert module_0.find_closest_elements([10.0, 20.0, 30.0, 30.5]) == (30.0, 30.5)

    # Closest pair at the beginning of the list
    assert module_0.find_closest_elements([1.0, 1.1, 50.0, 100.0]) == (1.0, 1.1)

    # Result is always a sorted tuple
    result = module_0.find_closest_elements([4.0, 1.0, 3.9])
    assert result == (3.9, 4.0)
    assert isinstance(result, tuple)

    # Larger list with a clear closest pair
    assert module_0.find_closest_elements([100.0, 200.0, 300.0, 301.0, 500.0]) == (300.0, 301.0)

    # Same distance tie: returns first pair found (sorted)
    result = module_0.find_closest_elements([1.0, 3.0, 5.0])
    assert result in [(1.0, 3.0), (3.0, 5.0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_find_closest_elements()
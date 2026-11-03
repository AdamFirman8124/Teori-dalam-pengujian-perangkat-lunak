

# Generated at 2026-11-02 22:00:55.587448
# Unit test for function maximum
def test_maximum():
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Basic case: k largest elements in ascending order
    assert module_0.maximum([1, 2, 3], 2) == [2, 3]
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # k equals length of array: returns all elements sorted ascending
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # Duplicates are preserved
    assert module_0.maximum([4, -4, 4], 2) == [4, 4]

    # Single largest element
    assert module_0.maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

    # Negative numbers
    assert module_0.maximum([-10, -5, -1], 2) == [-5, -1]

    # Single element array
    assert module_0.maximum([7], 1) == [7]

    # k larger than array length: returns all elements sorted
    assert module_0.maximum([2, 1], 5) == [1, 2]

    # Empty array with k > 0
    assert module_0.maximum([], 3) == []

    # Array with mixed positive/negative and unsorted input
    assert module_0.maximum([5, -2, 9, 0, 3], 2) == [5, 9]

    # Floats
    assert module_0.maximum([1.5, 2.5, 0.5], 2) == [1.5, 2.5]

    print("All tests passed!")

# Generated at 2026-11-02 22:04:14.989035
# Unit test for function maximum
def test_maximum():
    # Test k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Test basic case: k largest elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # Test k equals array length (returns all sorted)
    assert module_0.maximum([5, 1, 3], 3) == [1, 3, 5]

    # Test k larger than array length (returns sorted whole array)
    assert module_0.maximum([2, 1], 5) == [1, 2]

    # Test with negative numbers
    assert module_0.maximum([-1, -5, -3, 2], 2) == [-3, 2]

    # Test with duplicates
    assert module_0.maximum([4, -4, 4], 2) == [4, 4]

    # Test single element array with k == 1
    assert module_0.maximum([7], 1) == [7]

    # Test unsorted input with negative and positive values
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # Test k == 1 returns the single maximum
    assert module_0.maximum([10, -10, 0], 1) == [10]

    print("All tests passed!")


test_maximum()

# Generated at 2026-11-02 22:08:04.058824
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic case: k largest elements
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert module_0.maximum([5, 1, 3, 2, 4], 2) == [4, 5]

    # unsorted input
    assert module_0.maximum([10, -2, 7, 3], 2) == [7, 10]

    # k equals array length
    assert module_0.maximum([4, -4, 0], 3) == [-4, 0, 4]

    # single element array
    assert module_0.maximum([42], 1) == [42]

    # negative numbers
    assert module_0.maximum([-1, -5, -3], 2) == [-3, -1]

    # duplicates
    assert module_0.maximum([2, 2, 2, 2], 2) == [2, 2]
    assert module_0.maximum([1, 3, 3, 2], 3) == [2, 3, 3]

    # k larger than array length returns all sorted elements
    assert module_0.maximum([3, 1], 5) == [1, 3]

    # k == 1 returns the maximum element
    assert module_0.maximum([9, 7, 8], 1) == [9]

    # empty array with k == 0
    assert module_0.maximum([], 0) == []

    # mixed positive/negative/zero
    assert module_0.maximum([0, -10, 10, 5, -5], 4) == [-5, 0, 5, 10]

    # floats
    assert module_0.maximum([1.5, 2.5, 0.5], 2) == [1.5, 2.5]

    print("All tests passed!")


test_maximum()
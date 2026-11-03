

# Generated at 2026-11-02 13:55:32.795202
# Unit test for function next_smallest
def test_next_smallest():
    # Test with a typical list of distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Test with unsorted list
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Test with duplicates - duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([5, 5, 5, 1, 1]) is None
    # Test with negative numbers
    assert module_0.next_smallest([-1, -2, -3, -4]) == -3
    # Test with mixed positive and negative
    assert module_0.next_smallest([0, -5, 3, 1]) == -5
    # Test with two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 10
    # Test with single element list - should return None
    assert module_0.next_smallest([7]) is None
    # Test with empty list - should return None
    assert module_0.next_smallest([]) is None
    # Test with all identical elements - should return None
    assert module_0.next_smallest([3, 3, 3, 3]) is None
    # Test with floats
    assert module_0.next_smallest([1.5, 2.5, 3.5]) == 2.5
    # Test with large numbers
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000
    # Test with strings (sorted lexicographically)
    assert module_0.next_smallest(["banana", "apple", "cherry"]) == "banana"
    print("All tests passed!")


test_next_smallest()

# Generated at 2026-11-02 13:58:17.752179
# Unit test for function next_smallest
def test_next_smallest():
    # Basic cases with distinct values
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([3, 1, 4, 1, 5, 9, 2, 6]) == 2

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([7, 7, 7, 1, 1]) == 7

    # Too few unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([5, 5, 5]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20
    assert module_0.next_smallest([3, 3, 8]) == 8

    # Negative numbers and mixed values
    assert module_0.next_smallest([-1, -5, -3]) == -3
    assert module_0.next_smallest([-2, 0, 5, -2]) == 0
    assert module_0.next_smallest([0, -1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Unsorted input with mixed duplicates
    assert module_0.next_smallest([9, 3, 9, 3, 5]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 14:00:06.057654
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Unsorted input with duplicates
    assert module_0.next_smallest([4, 1, 3, 1, 2, 2]) == 2
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2

    # Negative numbers
    assert module_0.next_smallest([-5, -2, -10]) == -2
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([1, 1]) is None
    assert module_0.next_smallest([3, 3, 3, 3]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([100, 50, 50, 100]) == 100

    # Floats
    assert module_0.next_smallest([1.5, 2.5, 0.5]) == 1.5

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 14:02:07.193761
# Unit test for function next_smallest
def test_next_smallest():
    # Normal case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([3, 1, 4, 2]) == 2

    # List with duplicates
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([5, 5, 5, 1, 1]) == 5
    assert module_0.next_smallest([2, 2, 2, 1]) == 2

    # Unsorted list with negatives
    assert module_0.next_smallest([-5, -1, -3, 0]) == -3
    assert module_0.next_smallest([-10, 10, 0]) == 0

    # Floats and mixed values
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    assert module_0.next_smallest([3, 1.2, 7]) == 1.2

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([7, 7, 7, 7]) is None

    # Two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    print("All tests passed!")


test_next_smallest()
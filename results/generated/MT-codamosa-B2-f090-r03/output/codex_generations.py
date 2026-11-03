

# Generated at 2026-11-02 12:57:24.077537
# Unit test for function next_smallest
def test_next_smallest():
    # Standard cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([3, 1, 4, 1, 5, 9, 2, 6]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates should be ignored (unique values only)
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([2, 2, 2, 2]) is None
    assert module_0.next_smallest([7, 7, 8, 8, 9]) == 8

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Mixed values
    assert module_0.next_smallest([1.5, 2.5, 0.5]) == 1.5
    assert module_0.next_smallest([True, False, 2]) is not None  # True == 1, False == 0

    # Unsorted input with two unique values
    assert module_0.next_smallest([100, 1]) == 100
    assert module_0.next_smallest([1, 100]) == 100

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-11-02 12:58:22.342566
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1]) == 3

    # Unsorted input with negatives and floats
    assert module_0.next_smallest([-5, -1, -3, 0]) == -3
    assert module_0.next_smallest([2.5, 1.5, 3.5]) == 2.5

    # Fewer than two unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([4, 4, 4]) is None

    # Two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    # Mixed types (ints and floats compare numerically)
    assert module_0.next_smallest([1, 1.5, 2]) == 1.5

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 12:59:46.445801
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case: distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Unsorted input
    assert module_0.next_smallest([10, 3, 7, 1]) == 3

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([2, 2, 2, 2]) is None
    assert module_0.next_smallest([3, 3, 1, 1, 2]) == 2

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-1, 0, 1]) == 0

    # Mixed positive and negative
    assert module_0.next_smallest([4, -2, 0, 9]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Edge cases: empty and single-element lists
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None

    # Two elements
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([1, 1]) is None

    # Large list
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 13:01:35.899891
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct values
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Unsorted input
    assert module_0.next_smallest([10, 3, 7, 1, 9]) == 3

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([4, 4, 4, 1, 1, 5]) == 4
    assert module_0.next_smallest([2, 2, 2, 1]) == 2

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-1, 0, 1]) == 0
    assert module_0.next_smallest([-2, -2, -1]) == -1

    # Exactly two unique elements
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([7, 3]) == 7

    # Fewer than two unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None
    assert module_0.next_smallest([0, 0]) is None

    # Mixed positives and negatives with duplicates
    assert module_0.next_smallest([0, -1, 1, -1, 0]) == 0
    assert module_0.next_smallest([100, -100, 50, 50]) == -100

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    assert module_0.next_smallest([2.2, 2.2, 1.1]) == 2.2

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 13:04:20.285281
# Unit test for function next_smallest
def test_next_smallest():
    # Test with a typical list of distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Test with unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Test with duplicate values
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    # Test with only duplicates of one value (should return None)
    assert module_0.next_smallest([1, 1]) is None
    # Test with a single element (should return None)
    assert module_0.next_smallest([1]) is None
    # Test with an empty list (should return None)
    assert module_0.next_smallest([]) is None
    # Test with exactly two distinct elements
    assert module_0.next_smallest([3, 7]) == 7
    assert module_0.next_smallest([7, 3]) == 7
    # Test with negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    # Test with mixed negative and positive numbers
    assert module_0.next_smallest([-10, 0, 10, 5]) == 0
    # Test with floats
    assert module_0.next_smallest([2.5, 1.5, 3.5]) == 2.5
    # Test with all identical elements (should return None)
    assert module_0.next_smallest([4, 4, 4, 4]) is None
    # Test with a large range of values
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2
    # Test with strings (lexicographic ordering)
    assert module_0.next_smallest(["banana", "apple", "cherry"]) == "banana"
    # Test with tuples
    assert module_0.next_smallest([(3, 1), (1, 2), (2, 3)]) == (2, 3)

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()
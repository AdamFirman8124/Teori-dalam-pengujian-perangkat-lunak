

# Generated at 2026-11-02 10:28:30.689951
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates should be ignored (unique values only)
    assert module_0.next_smallest([1, 1, 4, 2, 1, 3]) == 2
    assert module_0.next_smallest([2, 2, 3, 3]) == 3
    # Empty list
    assert module_0.next_smallest([]) is None
    # Single element
    assert module_0.next_smallest([7]) is None
    # All identical elements
    assert module_0.next_smallest([4, 4, 4]) is None
    # Exactly two unique elements
    assert module_0.next_smallest([3, 1]) == 3
    assert module_0.next_smallest([1, 3]) == 3
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, 0]) == -3
    # Floats mixed with ints
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000

# Generated at 2026-11-02 10:29:50.457577
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1]) is None

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 2]) == 2

    # Fewer than 2 unique elements
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([4, 4, 4]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20
    assert module_0.next_smallest([10, 20, 10, 20]) == 20

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3]) == -3
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Mixed positive/negative with duplicates
    assert module_0.next_smallest([-2, 2, -2, 0, 2]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    print("All tests passed!")

# Generated at 2026-11-02 10:31:06.033858
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case: distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 2]) == 2

    # Unsorted input with negatives
    assert module_0.next_smallest([-5, -1, -3, 0, 2]) == -3

    # Only one distinct element -> None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([42]) is None

    # Empty list -> None
    assert module_0.next_smallest([]) is None

    # Exactly two distinct elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    # Floats mixed with ints
    assert module_0.next_smallest([2.5, 1, 3]) == 2.5

    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 10:32:10.523112
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 3, 4, 1, 2]) == 2

    # Unsorted input
    assert module_0.next_smallest([10, 5, 8, 3]) == 5

    # Duplicates should be ignored (unique values only)
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([5, 5, 5, 1, 1, 3]) == 3
    assert module_0.next_smallest([2, 2, 2]) is None

    # Fewer than 2 unique elements returns None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([7, 7, 7, 7]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([3, 1]) == 3
    assert module_0.next_smallest([1, 3]) == 3

    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3]) == -2
    assert module_0.next_smallest([-5, 0, 5]) == 0
    assert module_0.next_smallest([-1, -1, 0]) == 0

    # Mixed ints and floats
    assert module_0.next_smallest([1.5, 1, 2]) == 1.5
    assert module_0.next_smallest([2, 1.5, 3]) == 2

    # Non-integer numeric values
    assert module_0.next_smallest([0.1, 0.2, 0.3]) == 0.2

    # Large values
    assert module_0.next_smallest([10**9, 10**8, 10**7]) == 10**8

    # Order of unique elements after sorting
    assert module_0.next_smallest([100, 1, 50, 1, 100]) == 50

# Generated at 2026-11-02 10:33:21.918883
# Unit test for function next_smallest
def test_next_smallest():
    # Basic sorted and unsorted lists
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Lists with duplicates
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1]) == 3
    assert module_0.next_smallest([2, 2, 1, 1]) == 2

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([7, 7, 7]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-1, 0, 1]) == 0
    assert module_0.next_smallest([-2, -2, -1]) == -1

    # Floats and mixed numeric types
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    assert module_0.next_smallest([2, 2.0, 1, 1.0]) == 2  # 2 and 2.0 dedupe in set

    # Larger values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000

    # Original list must not be mutated in a way that breaks results
    lst = [3, 1, 2]
    assert module_0.next_smallest(lst) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()
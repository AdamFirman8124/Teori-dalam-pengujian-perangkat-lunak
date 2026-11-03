

# Generated at 2026-11-02 19:55:34.720689
# Unit test for function next_smallest
def test_next_smallest():
    # Basic cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([3, 1, 4, 1, 5, 9, 2, 6]) == 2

    # Duplicates in the list
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([2, 2, 2, 2]) is None
    assert module_0.next_smallest([1, 1, 1, 2]) == 2

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([7, 7, 7]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -3, 0]) == -3
    assert module_0.next_smallest([-10, 0, 10, -10]) == 0

    # Floats and mixed ints/floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    assert module_0.next_smallest([2, 1.5, 3]) == 2

    # Two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 10

    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-11-02 19:57:14.174108
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case: sorted list
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2

    # Unsorted list
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # List with duplicates
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2

    # Duplicated smallest, unique second smallest
    assert module_0.next_smallest([1, 1, 1, 2, 3]) == 2

    # Empty list -> None
    assert module_0.next_smallest([]) is None

    # Single element -> None
    assert module_0.next_smallest([7]) is None

    # All identical elements -> None
    assert module_0.next_smallest([4, 4, 4, 4]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([3, 1]) == 3
    assert module_0.next_smallest([10, 2]) == 10

    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3]) == -3
    assert module_0.next_smallest([-1, -1, -2]) == -1

    # Mixed negative and positive
    assert module_0.next_smallest([0, -2, 5, 3]) == 0

    # Floats mixed with ints
    assert module_0.next_smallest([1.5, 1, 2]) == 1.5

    # Second smallest is a duplicate of nothing but close values
    assert module_0.next_smallest([2, 2, 3, 3]) == 3

    # Larger list
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2

    print("All test_next_smallest tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 19:58:39.284951
# Unit test for function next_smallest
def test_next_smallest():
    # Basic cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([1, 1]) is None
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20
    assert module_0.next_smallest([5, 5, 5, 5]) is None  # duplicates, only one unique value
    assert module_0.next_smallest([3, 3, 1, 1, 2, 2]) == 2  # duplicates with multiple unique values
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([1]) is None  # single element
    assert module_0.next_smallest([-5, -3, -1]) == -3  # negative numbers
    assert module_0.next_smallest([0, -1, 1]) == 0
    assert module_0.next_smallest([1.5, 2.5, 3.5]) == 2.5  # floats

    print("All tests passed!")

test_next_smallest()

# Generated at 2026-11-02 20:00:42.679330
# Unit test for function next_smallest
def test_next_smallest():
    # Standard case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # List with duplicates
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 4]) == 3
    # Duplicates of the smallest value
    assert module_0.next_smallest([1, 1, 1, 2]) == 2
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, 0]) == -3
    assert module_0.next_smallest([-10, -20, -30]) == -20
    # Two elements
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([7, 7]) is None
    # All identical elements -> None
    assert module_0.next_smallest([4, 4, 4]) is None
    # Single element -> None
    assert module_0.next_smallest([42]) is None
    # Empty list -> None
    assert module_0.next_smallest([]) is None
    # Mixed positive/negative with duplicates
    assert module_0.next_smallest([0, -1, 0, 1, -1]) == 0
    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 20:03:27.284039
# Unit test for function next_smallest
def test_next_smallest():
# nonce:92925c32
    # Typical case: distinct sorted elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates of the smallest value
    assert module_0.next_smallest([1, 1, 2, 3]) == 2
    # Duplicates throughout, second unique smallest
    assert module_0.next_smallest([2, 2, 1, 1, 3]) == 2
    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3, 0]) == -2
    assert module_0.next_smallest([-5, -5, -10]) == -5
    # Only one unique element -> None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([3, 3, 3]) is None
    # All identical duplicates
    assert module_0.next_smallest([7, 7, 7, 7]) is None
    # Empty list -> None
    assert module_0.next_smallest([]) is None
    # Two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20
    # Mixed positives, negatives, and duplicates
    assert module_0.next_smallest([0, -3, 5, -3, 2]) == -3
    # Floats included
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()
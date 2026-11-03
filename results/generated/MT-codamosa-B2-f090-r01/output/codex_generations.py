

# Generated at 2026-11-02 09:32:11.404541
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2

    # Unsorted list
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2

    # List with duplicates
    assert module_0.next_smallest([5, 1, 4, 3, 2, 1, 2]) == 2

    # Duplicates of the smallest value
    assert module_0.next_smallest([1, 1, 1, 2]) == 2

    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3, -4]) == -3

    # Mixed negative and positive numbers
    assert module_0.next_smallest([0, -5, 3, -2]) == -2

    # Two elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    # Two elements with duplicates
    assert module_0.next_smallest([7, 7, 8]) == 8

    # Empty list returns None
    assert module_0.next_smallest([]) is None

    # Single element returns None
    assert module_0.next_smallest([42]) is None

    # All identical elements returns None
    assert module_0.next_smallest([3, 3, 3, 3]) is None

    # Floats
    assert module_0.next_smallest([2.5, 1.5, 3.5]) == 2.5

    # Floats and ints mixed
    assert module_0.next_smallest([2, 1.5, 3]) == 2

    # Large list
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 09:36:18.258773
# Unit test for function next_smallest
def test_next_smallest():
    # nonce:35ff7701
    # Standard case with distinct values
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2
    # List with duplicates
    assert module_0.next_smallest([5, 1, 4, 3, 2, 1, 2]) == 2
    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3, -4]) == -3
    # Exactly two elements
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([1, 2]) == 2
    # Empty list
    assert module_0.next_smallest([]) is None
    # Single element
    assert module_0.next_smallest([7]) is None
    # All identical elements (only one unique value)
    assert module_0.next_smallest([3, 3, 3, 3]) is None
    # Duplicates leaving exactly two unique values
    assert module_0.next_smallest([1, 1, 1, 2]) == 2
    # Mixed floats and ints
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    # Large values
    assert module_0.next_smallest([10**9, 10**8, 10**10]) == 10**9
    # Strings (lexicographic ordering)
    assert module_0.next_smallest(["banana", "apple", "cherry"]) == "banana"
    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 09:38:50.318394
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2

    # Unsorted input
    assert module_0.next_smallest([10, 5, 8, 3, 9]) == 5

    # Duplicates should be ignored (set semantics)
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([4, 4, 4, 1, 1]) == 4

    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Empty list -> None
    assert module_0.next_smallest([]) is None

    # Exactly two unique elements
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([9, 9, 1, 1]) == 9

    # Negative numbers
    assert module_0.next_smallest([-1, -5, -3, 0]) == -3
    assert module_0.next_smallest([-2, -2, -7]) == -2

    # Mixed positive and negative
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()
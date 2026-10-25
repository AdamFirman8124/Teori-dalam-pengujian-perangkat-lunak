

# Generated at 2026-10-24 07:20:10.266538
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates must be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([7, 7, 7, 1]) is None  # only one unique value

    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -10]) == -5
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Original list must not be mutated
    data = [3, 1, 2]
    module_0.next_smallest(data)
    assert data == [3, 1, 2]

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-10-24 07:20:11.568528
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates must be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([7, 7, 7, 1]) is None  # only one unique value

    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -10]) == -5
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Original list must not be mutated
    data = [3, 1, 2]
    module_0.next_smallest(data)
    assert data == [3, 1, 2]

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-10-24 07:20:12.878743
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates must be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([7, 7, 7, 1]) is None  # only one unique value

    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -10]) == -5
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Original list must not be mutated
    data = [3, 1, 2]
    module_0.next_smallest(data)
    assert data == [3, 1, 2]

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-10-24 07:20:14.190508
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates must be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([7, 7, 7, 1]) is None  # only one unique value

    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -10]) == -5
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Original list must not be mutated
    data = [3, 1, 2]
    module_0.next_smallest(data)
    assert data == [3, 1, 2]

    print("All tests passed!")


test_next_smallest()

# Generated at 2026-10-24 07:20:15.513133
# Unit test for function next_smallest
def test_next_smallest():
    # Typical cases
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([10, 20, 30]) == 20

    # Duplicates must be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([7, 7, 7, 1]) is None  # only one unique value

    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([3, 3, 3]) is None

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -10]) == -5
    assert module_0.next_smallest([0, -1, 1]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Original list must not be mutated
    data = [3, 1, 2]
    module_0.next_smallest(data)
    assert data == [3, 1, 2]

    print("All tests passed!")


test_next_smallest()
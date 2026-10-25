

# Generated at 2026-10-24 04:47:38.072314
# Unit test for function next_smallest

# Generated at 2026-10-24 04:47:40.487071
# Unit test for function next_smallest

# Generated at 2026-10-24 04:47:57.174561
# Unit test for function next_smallest
def test_next_smallest():assert module_0.next_smallest([1, 2, 3]) == 2

# Generated at 2026-10-24 04:48:02.273367
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

# Generated at 2026-10-24 04:48:03.627982
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

# Generated at 2026-10-24 04:48:04.945610
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

# Generated at 2026-10-24 04:48:06.278555
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


# Generated at 2026-11-02 13:09:48.716291
# Unit test for function unique
def test_unique():
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert module_0.unique([]) == []
    assert module_0.unique([1]) == [1]
    assert module_0.unique([2, 2, 2, 2]) == [2]
    assert module_0.unique([3, 1, 2, 1, 3]) == [1, 2, 3]
    assert module_0.unique([-1, -5, -1, 0]) == [-5, -1, 0]
    assert module_0.unique(['b', 'a', 'c', 'a']) == ['a', 'b', 'c']
    assert module_0.unique([1.5, 1.5, 2.0]) == [1.5, 2.0]

# Generated at 2026-11-02 13:11:02.452797
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Already unique and sorted
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Negative numbers
    assert module_0.unique([-1, 1, -1, 0, 1]) == [-1, 0, 1]

    # Unsorted input
    assert module_0.unique([10, 2, 8, 2, 10, 1]) == [1, 2, 8, 10]

    # Strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Mixed floats and ints
    assert module_0.unique([1.0, 1, 2.5, 2]) == [1, 2.5]

    # Result length check
    assert len(module_0.unique([3, 1, 3, 2, 1])) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_unique()

# Generated at 2026-11-02 13:12:07.021659
# Unit test for function unique
def test_unique():
    # Basic case with duplicates and unsorted input
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    # Empty list
    assert module_0.unique([]) == []
    # Single element
    assert module_0.unique([1]) == [1]
    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]
    # Negative numbers
    assert module_0.unique([-1, 1, 0, -1, 0]) == [-1, 0, 1]
    # Strings
    assert module_0.unique(['b', 'a', 'b', 'c', 'a']) == ['a', 'b', 'c']
    # Floats
    assert module_0.unique([2.5, 1.5, 2.5, 0.5]) == [0.5, 1.5, 2.5]
    # Result should be a sorted list
    result = module_0.unique([10, 5, 8, 5, 10, 1])
    assert isinstance(result, list)
    assert result == sorted(result)
    # Mixed int/float (1 == 1.0 in a set)
    assert module_0.unique([1, 1.0, 2]) == [1, 2]

# Generated at 2026-11-02 13:13:52.234481
# Unit test for function unique
def test_unique():
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert module_0.unique([]) == []
    assert module_0.unique([1]) == [1]
    assert module_0.unique([2, 2, 2]) == [2]
    assert module_0.unique([3, 1, 2]) == [1, 2, 3]
    assert module_0.unique([-1, -5, -1, 0]) == [-5, -1, 0]
    assert module_0.unique(['b', 'a', 'b', 'c']) == ['a', 'b', 'c']
    assert module_0.unique([1.5, 1.5, 2.5]) == [1.5, 2.5]

# Generated at 2026-11-02 13:15:36.083962
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    # Empty list
    assert module_0.unique([]) == []
    # Already sorted unique elements
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]
    # Single element
    assert module_0.unique([42]) == [42]
    # Negative numbers
    assert module_0.unique([-1, 1, -1, 0, 1]) == [-1, 0, 1]
    # Unsorted with negatives and duplicates
    assert module_0.unique([3, -2, 3, -2, 0]) == [-2, 0, 3]
    # Result is a list
    assert isinstance(module_0.unique([1, 1, 2]), list)
    print("All tests passed!")


if __name__ == "__main__":
    test_unique()
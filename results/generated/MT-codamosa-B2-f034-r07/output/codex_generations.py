

# Generated at 2026-11-03 05:53:53.338944
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    # Empty list
    assert module_0.unique([]) == []
    # Single element
    assert module_0.unique([1]) == [1]
    # All duplicates
    assert module_0.unique([1, 1, 1]) == [1]
    # Already sorted input
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]
    # Reverse sorted input
    assert module_0.unique([3, 2, 1]) == [1, 2, 3]
    # Negative numbers
    assert module_0.unique([-1, -5, 0, -5, -1]) == [-5, -1, 0]
    # Mixed positive and negative
    assert module_0.unique([10, -10, 0, 10, -10]) == [-10, 0, 10]
    # Strings
    assert module_0.unique(['b', 'a', 'b', 'c']) == ['a', 'b', 'c']
    # Floats
    assert module_0.unique([2.5, 1.5, 2.5, 0.5]) == [0.5, 1.5, 2.5]
    # Boolean and int mix (True == 1 in Python)
    assert module_0.unique([True, 1, 2]) == [1, 2]
    # Result is a list
    assert isinstance(module_0.unique([3, 1, 2]), list)
    # No duplicates in result
    result = module_0.unique([1, 2, 2, 3, 3, 3])
    assert len(result) == len(set(result))

# Generated at 2026-11-03 05:54:26.777115
# Unit test for function unique
def test_unique():
    # Basic list with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Already unique, already sorted
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Negative numbers
    assert module_0.unique([-3, 1, -3, 0, 1, -1]) == [-3, -1, 0, 1]

    # Strings
    assert module_0.unique(["banana", "apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

    # Mixed floats and ints (equal values dedupe)
    assert module_0.unique([1, 1.0, 2, 2.0]) == [1, 2]

    # Unsorted input with duplicates
    assert module_0.unique([10, 2, 10, 2, 1]) == [1, 2, 10]

    # Result type is a list
    assert isinstance(module_0.unique([3, 1, 2]), list)

    # Original list is not modified
    original = [3, 1, 3, 2]
    module_0.unique(original)
    assert original == [3, 1, 3, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_unique()

# Generated at 2026-11-03 05:55:32.237810
# Unit test for function unique
def test_unique():
    # Test with a list of integers containing duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Test with an empty list
    assert module_0.unique([]) == []

    # Test with a list of strings containing duplicates
    assert module_0.unique(["apple", "banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

    # Test with a single element
    assert module_0.unique([42]) == [42]

    # Test with already unique elements
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]

    # Test with negative numbers
    assert module_0.unique([-1, -1, 0, -5, 3]) == [-5, -1, 0, 3]

    # Test that result is sorted regardless of input order
    assert module_0.unique([10, 1, 10, 2, 1]) == [1, 2, 10]

    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_unique()

# Generated at 2026-11-03 05:56:03.752554
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All identical elements
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Already sorted list
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted list
    assert module_0.unique([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Negative numbers
    assert module_0.unique([-1, 1, -1, 2, 0, 2]) == [-1, 0, 1, 2]

    # Negative duplicates
    assert module_0.unique([-3, -3, -1, -1, 0]) == [-3, -1, 0]

    # String elements
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Int and float with equal value dedupe together
    assert module_0.unique([1, 1.0, 2]) == [1, 2]

    # Large list with many duplicates
    assert module_0.unique(list(range(100, 0, -1)) * 3) == list(range(1, 101))

    # Result contains no duplicates
    result = module_0.unique([3, 1, 3, 2, 1])
    assert len(result) == len(set(result))

    # Result is sorted
    assert result == sorted(result)

# Generated at 2026-11-03 05:56:42.844752
# Unit test for function unique
def test_unique():
    # Basic case with duplicates (canonical example)
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([1]) == [1]

    # All elements identical
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Already sorted unique elements
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted input with duplicates
    assert module_0.unique([5, 4, 3, 2, 1, 1, 2, 3]) == [1, 2, 3, 4, 5]

    # Negative numbers and zero
    assert module_0.unique([-1, 1, -1, 0, 1, -5]) == [-5, -1, 0, 1]

    # Floating point numbers
    assert module_0.unique([2.5, 1.5, 2.5, 0.5]) == [0.5, 1.5, 2.5]

    # Strings
    assert module_0.unique(['b', 'a', 'b', 'c', 'a']) == ['a', 'b', 'c']

    # Verify output is sorted for unsorted input
    result = module_0.unique([10, 2, 33, 2, 10, -4])
    assert result == sorted(result)
    assert result == [-4, 2, 10, 33]

    # Verify duplicates are removed (length check)
    assert len(module_0.unique([1, 1, 1, 2, 2, 3])) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_unique()


# Generated at 2026-11-03 03:48:14.916561
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert module_0.common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with duplicates in inputs (result should be unique)
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3]) == [2, 3]

    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []

    # Test with identical lists
    assert module_0.common([7, 8, 9], [7, 8, 9]) == [7, 8, 9]

    # Test with unsorted inputs (result should be sorted)
    assert module_0.common([9, 5, 1], [1, 9, 5]) == [1, 5, 9]

    # Test with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "date"]) == ["banana"]

    # Test with negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]

    # Test with single elements
    assert module_0.common([1], [1]) == [1]
    assert module_0.common([1], [2]) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_common()

# Generated at 2026-11-03 03:50:08.384059
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    # Test with empty first list
    assert module_0.common([], [1, 2, 3]) == []
    # Test with empty second list
    assert module_0.common([1, 2, 3], []) == []
    # Test with both lists empty
    assert module_0.common([], []) == []
    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]
    # Test with strings
    assert module_0.common(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]
    # Test with unsorted results (output should be sorted)
    assert module_0.common([5, 1, 3], [3, 5, 1]) == [1, 3, 5]
    # Test with mixed types (int and float equality)
    assert module_0.common([1, 2.0, 3], [2, 3.0, 4]) == [2, 3]
    # Test with identical lists
    assert module_0.common([7, 8, 9], [7, 8, 9]) == [7, 8, 9]
    # Test with negative numbers
    assert module_0.common([-1, -2, 0], [-2, 0, 1]) == [-2, 0]
    # Test with booleans and integers (True == 1 in Python)
    assert module_0.common([True, 2], [1, 2]) == [1, 2]

# nonce:84c64618

# Generated at 2026-11-03 03:51:56.305825
# Unit test for function common
def test_common():
    # Test with common elements present
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []

    # Test with duplicates in input lists
    assert module_0.common([1, 1, 2, 3], [1, 3, 3]) == [1, 3]

    # Test with identical lists
    assert module_0.common([5, 1, 3], [3, 1, 5]) == [1, 3, 5]

    # Test result is sorted even when inputs are unsorted
    assert module_0.common([9, 7, 5, 1], [1, 5, 9]) == [1, 5, 9]

    # Test with strings
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]

    # Test with mixed types (ints and strings do not match)
    assert module_0.common([1, "1"], ["1", 1]) == [1, "1"]

    # Test with negative numbers and floats
    assert module_0.common([-1, -2, 3.5], [3.5, -2, 10]) == [-2, 3.5]

    # Test with boolean values
    assert module_0.common([True, 1], [1, False]) == [1]

    print("All tests passed!")

# Generated at 2026-11-03 03:54:30.122296
# Unit test for function common
def test_common():
    # Basic intersection
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # No common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    # Empty list cases
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    # Duplicates should not produce duplicates in result
    assert module_0.common([1, 1, 2, 2], [1, 2, 2]) == [1, 2]
    # Result should be sorted even if inputs are unsorted
    assert module_0.common([5, 3, 2, 8], [8, 3, 2]) == [2, 3, 8]
    # Works with strings
    assert module_0.common(['a', 'b', 'c'], ['b', 'd', 'a']) == ['a', 'b']
    # Works with negative numbers
    assert module_0.common([-1, 0, 1], [0, 1, 2]) == [0, 1]
    # Single common element
    assert module_0.common([7], [7]) == [7]

# Generated at 2026-11-03 03:56:02.385100
# Unit test for function common
def test_common():
    # Test with basic common elements
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    
    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 3], [1, 3, 3, 5]) == [1, 3]
    
    # Test with empty first list
    assert module_0.common([], [1, 2, 3]) == []
    
    # Test with empty second list
    assert module_0.common([1, 2, 3], []) == []
    
    # Test with both lists empty
    assert module_0.common([], []) == []
    
    # Test with identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    
    # Test with unsorted input and ensure sorted output
    assert module_0.common([5, 3, 1], [1, 5, 2]) == [1, 5]
    
    # Test with negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]
    
    # Test with strings
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]
    
    # Test with mixed types
    assert module_0.common([1, "a", 2.5], ["a", 2.5, "b"]) == [1 == 1 and 2.5, "a"] if False else module_0.common([1, "a", 2.5], ["a", 2.5, "b"]) == [2.5, "a"]
    
    # Test with single common element
    assert module_0.common([7], [7]) == [7]
    
    # Test with repeated common elements across lists
    assert module_0.common([1, 2, 2, 3, 3, 3], [3, 3, 2, 2, 1]) == [1, 2, 3]
    
    print("All test_common tests passed!")


if __name__ == "__main__":
    test_common()
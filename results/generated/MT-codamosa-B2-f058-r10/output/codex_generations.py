

# Generated at 2026-11-02 10:35:53.470872
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    
    # Test with no common elements
    assert module_0.common([1, 2], [3, 4]) == []
    
    # Test with empty lists
    assert module_0.common([], []) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], [1, 2]) == []
    
    # Test with duplicates in inputs (result should be unique)
    assert module_0.common([1, 1, 2, 3], [1, 3, 3, 4]) == [1, 3]
    assert module_0.common([2, 2, 2], [2, 2]) == [2]
    
    # Test with identical lists
    assert module_0.common([5, 1, 3], [3, 1, 5]) == [1, 3, 5]
    
    # Test with strings
    assert module_0.common(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]
    
    # Test result is sorted regardless of input order
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]
    
    # Test with negative numbers
    assert module_0.common([-3, -1, 0], [-1, 0, 1]) == [-1, 0]
    
    # Test with mixed types (int and float equality)
    assert module_0.common([1, 2.0, 3], [2, 3.0, 4]) == [2, 3]

# Generated at 2026-11-02 10:37:17.131982
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []

    # Test with duplicates in input lists
    assert module_0.common([1, 2, 2, 3, 3], [2, 3, 3, 4]) == [2, 3]

    # Test with identical lists
    assert module_0.common([5, 1, 3], [3, 5, 1]) == [1, 3, 5]

    # Test result is sorted
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]

    # Test with strings
    assert module_0.common(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]

    # Test with single element lists
    assert module_0.common([1], [1]) == [1]
    assert module_0.common([1], [2]) == []

    # Test with negative numbers
    assert module_0.common([-1, -2, 0], [-2, 0, 2]) == [-2, 0]

    print("All tests passed!")


test_common()

# Generated at 2026-11-02 10:38:42.537906
# Unit test for function common
def test_common():
# nonce:34ac75fb
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    
    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Test with duplicates in both lists (result should have unique elements)
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]
    
    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    
    # Test with identical lists
    assert module_0.common([5, 3, 1], [5, 3, 1]) == [1, 3, 5]
    
    # Test with single elements
    assert module_0.common([7], [7]) == [7]
    assert module_0.common([7], [8]) == []
    
    # Test with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "cherry", "date"]) == ["banana", "cherry"]
    
    # Test with negative numbers
    assert module_0.common([-1, -2, 0, 1], [-2, 0, 2]) == [-2, 0]
    
    # Test with unsorted input to verify sorted output
    assert module_0.common([9, 1, 5], [5, 9, 2]) == [5, 9]
    
    # Test with mixed types (int and float equality)
    assert module_0.common([1, 2.0, 3], [2.0, 3, 4]) == [2.0, 3]
    
    # Test with subset
    assert module_0.common([1, 2, 3, 4, 5], [2, 4]) == [2, 4]
    
    # Test with large lists
    assert module_0.common(list(range(100)), list(range(50, 150))) == list(range(50, 100))
    
    # Test with repeated elements in l1 only
    assert module_0.common([1, 1, 1], [1]) == [1]
    
    # Test with tuples as elements
    assert module_0.common([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_common()

# Generated at 2026-11-02 10:40:34.252960
# Unit test for function common
def test_common():
    # Test with common elements present
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]

    # Test with empty first list
    assert module_0.common([], [1, 2, 3]) == []

    # Test with empty second list
    assert module_0.common([1, 2, 3], []) == []

    # Test with both lists empty
    assert module_0.common([], []) == []

    # Test with identical lists
    assert module_0.common([5, 3, 1], [1, 3, 5]) == [1, 3, 5]

    # Test result is sorted regardless of input order
    assert module_0.common([9, 7, 5, 3], [3, 5, 7, 9]) == [3, 5, 7, 9]

    # Test with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "cherry", "date"]) == ["banana", "cherry"]

    # Test with mixed types
    assert module_0.common([1, "a", 2.5], ["a", 2.5, 3]) == [2.5, "a"]

    # Test with single common element
    assert module_0.common([1, 2], [2, 3]) == [2]

    # Test with negative numbers
    assert module_0.common([-1, -2, 0], [-2, 0, 2]) == [-2, 0]

    # Test result type is a list
    assert isinstance(module_0.common([1, 2], [2, 3]), list)

# Generated at 2026-11-02 10:41:43.885133
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []

    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]

    # Test with identical lists
    assert module_0.common([5, 3, 1], [1, 3, 5]) == [1, 3, 5]

    # Test result is sorted even when inputs are unsorted
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]

    # Test with strings
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]

    # Test with negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]

    # Test with single common element
    assert module_0.common([10], [10]) == [10]

    print("All tests passed!")


test_common()
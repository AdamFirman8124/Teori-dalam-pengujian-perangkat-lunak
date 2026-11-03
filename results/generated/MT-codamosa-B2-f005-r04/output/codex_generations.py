

# Generated at 2026-11-02 14:49:33.727059
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 4) == []

    # Test single element
    assert module_0.intersperse([5], 4) == [5]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test two elements
    assert module_0.intersperse([1, 2], 9) == [1, 9, 2]

    # Test negative numbers and delimiter
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test delimiter of zero
    assert module_0.intersperse([7, 8], 0) == [7, 0, 8]

    # Test larger list
    assert module_0.intersperse([10, 20, 30, 40], 5) == [10, 5, 20, 5, 30, 5, 40]

    # Test with duplicates
    assert module_0.intersperse([1, 1, 1], 2) == [1, 2, 1, 2, 1]

    print("All tests passed!")


test_intersperse()

# Generated at 2026-11-02 14:51:26.511750
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []
    
    # Test with single element
    assert module_0.intersperse([5], 4) == [5]
    
    # Test with two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]
    
    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    
    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]
    
    # Test with delimiter 0
    assert module_0.intersperse([7, 8, 9], 0) == [7, 0, 8, 0, 9]
    
    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    
    # Test with duplicate values
    assert module_0.intersperse([5, 5, 5], 1) == [5, 1, 5, 1, 5]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-02 14:53:15.375904
# Unit test for function intersperse
def test_intersperse():
    # Empty list returns empty list
    assert module_0.intersperse([], 4) == []

    # Single element has no delimiter
    assert module_0.intersperse([5], 4) == [5]

    # Two elements get one delimiter between them
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Delimiter of 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -9) == [-1, -9, -2, -9, -3]

    # Duplicate values
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]

    # Delimiter equal to an element value
    assert module_0.intersperse([2, 2], 2) == [2, 2, 2]

# Generated at 2026-11-02 14:54:45.677903
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []

    # Test with single element
    assert module_0.intersperse([1], 4) == [1]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with two elements
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]

    # Test with negative delimiter
    assert module_0.intersperse([5, 6, 7], -1) == [5, -1, 6, -1, 7]

    # Test with duplicate values
    assert module_0.intersperse([2, 2, 2], 9) == [2, 9, 2, 9, 2]

    # Test with zero delimiter
    assert module_0.intersperse([3, 4], 0) == [3, 0, 4]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-02 14:55:40.748898
# Unit test for function intersperse
def test_intersperse():
    # Empty list returns empty list
    assert module_0.intersperse([], 7) == []

    # Single element: no delimiter added
    assert module_0.intersperse([5], 7) == [5]

    # Two elements: one delimiter between them
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Multiple elements: delimiter between every adjacent pair
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Delimiter of zero
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -9) == [-1, -9, -2, -9, -3]

    # Delimiter equal to the elements themselves
    assert module_0.intersperse([3, 3, 3], 3) == [3, 3, 3, 3, 3]

    # Larger list
    assert module_0.intersperse([10, 20, 30, 40, 50], 99) == [10, 99, 20, 99, 30, 99, 40, 99, 50]

    # Input list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 9)
    assert original == [1, 2, 3]
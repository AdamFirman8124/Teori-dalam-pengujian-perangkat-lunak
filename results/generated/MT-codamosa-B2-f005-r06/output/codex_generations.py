

# Generated at 2026-11-03 04:31:39.693370
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []

    # Test with single element list
    assert module_0.intersperse([5], 4) == [5]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with two elements
    assert module_0.intersperse([1, 2], 9) == [1, 9, 2]

    # Test with delimiter 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]

    # Test that original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 4)
    assert original == [1, 2, 3]

    # Test result type
    result = module_0.intersperse([1, 2], 3)
    assert isinstance(result, list)

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 04:34:48.620144
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
    
    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    
    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 0) == [7, 0, 7, 0, 7]
    
    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]
    
    # Test that original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 9)
    assert original == [1, 2, 3]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 04:38:15.730588
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 4) == []

    # Test single element list
    assert module_0.intersperse([5], 4) == [5]

    # Test two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]

    # Test delimiter of zero
    assert module_0.intersperse([10, 20], 0) == [10, 0, 20]

    # Test negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test longer list
    assert module_0.intersperse([1, 2, 3, 4, 5], 9) == [1, 9, 2, 9, 3, 9, 4, 9, 5]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()
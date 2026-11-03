

# Generated at 2026-11-03 03:08:38.505261
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []

    # Test with single element (no delimiter needed)
    assert module_0.intersperse([5], 4) == [5]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with delimiter equal to an element value
    assert module_0.intersperse([1, 1, 1], 1) == [1, 1, 1, 1, 1]

    # Test with zero delimiter
    assert module_0.intersperse([10, 20, 30], 0) == [10, 0, 20, 0, 30]

    # Test with larger list
    assert module_0.intersperse([1, 2, 3, 4, 5], 9) == [1, 9, 2, 9, 3, 9, 4, 9, 5]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 03:10:44.717447
# Unit test for function intersperse
def test_intersperse():
    # Empty list returns empty list
    assert module_0.intersperse([], 4) == []

    # Single element: no delimiter added
    assert module_0.intersperse([5], 4) == [5]
    assert module_0.intersperse([10], 100) == [10]

    # Multiple elements: delimiter between each pair
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert module_0.intersperse([1, 2], 9) == [1, 9, 2]
    assert module_0.intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]

    # Negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Delimiter equal to element values
    assert module_0.intersperse([7, 7], 7) == [7, 7, 7]
    assert module_0.intersperse([3, 3, 3], 0) == [3, 0, 3, 0, 3]

    # Negative delimiter
    assert module_0.intersperse([1, 2], -5) == [1, -5, 2]

    # Input list is not modified
    nums = [1, 2, 3]
    module_0.intersperse(nums, 9)
    assert nums == [1, 2, 3]

    print("All intersperse tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 03:12:40.474721
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []

    # Test with single element (no delimiter needed)
    assert module_0.intersperse([5], 4) == [5]

    # Test with two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with delimiter of zero
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 9) == [7, 9, 7, 9, 7]

    # Test result length is correct: 2*n - 1 for n elements
    result = module_0.intersperse([1, 2, 3, 4, 5], 8)
    assert len(result) == 2 * 5 - 1

    # Test original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 4)
    assert original == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 03:13:21.485152
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []
    
    # Test with single element
    assert module_0.intersperse([1], 4) == [1]
    
    # Test with two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]
    
    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    
    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]
    
    # Test with delimiter 0
    assert module_0.intersperse([5, 6, 7], 0) == [5, 0, 6, 0, 7]
    
    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    
    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 03:14:23.281387
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

    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate elements
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]

    # Test with zero delimiter
    assert module_0.intersperse([10, 20], 0) == [10, 0, 20]

    # Test with larger list
    assert module_0.intersperse([1, 2, 3, 4, 5], 9) == [1, 9, 2, 9, 3, 9, 4, 9, 5]

    # Test result length is correct (2n - 1 for n elements)
    numbers = [1, 2, 3, 4]
    result = module_0.intersperse(numbers, 0)
    assert len(result) == 2 * len(numbers) - 1

    # Test original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 5)
    assert original == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()
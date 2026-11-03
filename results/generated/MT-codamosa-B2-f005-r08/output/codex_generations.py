

# Generated at 2026-11-03 05:53:47.749792
# Unit test for function intersperse
def test_intersperse():
    # Test with an empty list
    assert module_0.intersperse([], 4) == []

    # Test with a single element (no delimiter should be added)
    assert module_0.intersperse([5], 4) == [5]

    # Test with two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with delimiter equal to an element value
    assert module_0.intersperse([7, 7, 7], 7) == [7, 7, 7, 7, 7]

    # Test with zero delimiter
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test result length: 2n - 1 for n elements
    assert len(module_0.intersperse([1, 2, 3, 4, 5], 9)) == 9

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 05:54:17.152265
# Unit test for function intersperse
def test_intersperse():
    # Test with an empty list
    assert module_0.intersperse([], 7) == []

    # Test with a single element
    assert module_0.intersperse([5], 7) == [5]

    # Test with two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with delimiter 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -4) == [-1, -4, -2, -4, -3]

    # Test with duplicate elements
    assert module_0.intersperse([2, 2, 2], 9) == [2, 9, 2, 9, 2]

    print("All tests passed!")


test_intersperse()

# Generated at 2026-11-03 05:55:27.703818
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

    # Test with delimiter 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate values
    assert module_0.intersperse([7, 7, 7], 9) == [7, 9, 7, 9, 7]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 05:55:57.201717
# Unit test for function intersperse
def test_intersperse():
    # Empty list should return empty list
    assert module_0.intersperse([], 4) == []

    # Single element: no delimiter inserted
    assert module_0.intersperse([5], 4) == [5]

    # Two elements: one delimiter between them
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Multiple elements: delimiter between each pair, none trailing
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert module_0.intersperse([1, 2, 3, 4, 5], 8) == [1, 8, 2, 8, 3, 8, 4, 8, 5]

    # Delimiter of zero
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Duplicate values in input
    assert module_0.intersperse([7, 7, 7], 0) == [7, 0, 7, 0, 7]

    # Original list is not modified
    nums = [1, 2, 3]
    module_0.intersperse(nums, 9)
    assert nums == [1, 2, 3]

    print("All intersperse tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 05:56:27.508979
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 7) == [], "Expected empty list for empty input"

    # Test with single element list
    assert module_0.intersperse([5], 7) == [5], "Expected [5] for single element input"

    # Test with two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2], "Expected [1, 7, 2] for two elements"

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3], "Expected [1, 4, 2, 4, 3]"

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3], "Expected [-1, 0, -2, 0, -3]"

    # Test with delimiter equal to an element value
    assert module_0.intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2], "Expected [2, 2, 2, 2, 2]"

    # Test with duplicate elements
    assert module_0.intersperse([1, 1, 1, 1], 9) == [1, 9, 1, 9, 1, 9, 1], "Expected [1, 9, 1, 9, 1, 9, 1]"

    # Test that original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 0)
    assert original == [1, 2, 3], "Original list should not be modified"

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()
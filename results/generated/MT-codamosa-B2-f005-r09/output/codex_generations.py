

# Generated at 2026-11-02 11:59:43.045912
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

    # Test with a delimiter of 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with a negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with duplicate values
    assert module_0.intersperse([5, 5, 5], 9) == [5, 9, 5, 9, 5]

    # Test with negative numbers in the list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with a longer list
    assert module_0.intersperse([10, 20, 30, 40, 50], 99) == [10, 99, 20, 99, 30, 99, 40, 99, 50]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-02 12:02:22.095290
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 4) == []

    # Test with single element (no delimiter should be added)
    assert module_0.intersperse([5], 4) == [5]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate values
    assert module_0.intersperse([5, 5, 5], 1) == [5, 1, 5, 1, 5]

    # Test with delimiter equal to an element value
    assert module_0.intersperse([1, 2], 2) == [1, 2, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-02 12:04:27.005136
# Unit test for function intersperse
def test_intersperse():
    # Test with empty list
    assert module_0.intersperse([], 7) == []

    # Test with single element
    assert module_0.intersperse([5], 7) == [5]

    # Test with two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Test with multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate elements
    assert module_0.intersperse([3, 3, 3], 1) == [3, 1, 3, 1, 3]

    # Test with zero delimiter
    assert module_0.intersperse([10, 20, 30], 0) == [10, 0, 20, 0, 30]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -5) == [1, -5, 2, -5, 3]

    # Test that original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 9)
    assert original == [1, 2, 3]

    # Test with large list
    assert module_0.intersperse(list(range(100)), -1) == [x for i in range(100) for x in ([i, -1] if i < 99 else [i])]

    print("All tests passed!")

# Generated at 2026-11-02 12:05:50.630500
# Unit test for function intersperse

# Generated at 2026-11-02 12:06:18.932926
# Unit test for function intersperse

# Generated at 2026-11-02 12:07:00.891234
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 4) == []
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert module_0.intersperse([5], 3) == [5]
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]
    assert module_0.intersperse([0, -1, -2], 100) == [0, 100, -1, 100, -2]

# Generated at 2026-11-02 12:07:20.919842
# Unit test for function intersperse
def test_intersperse():
    # Empty list should return an empty list
    assert module_0.intersperse([], 4) == []

    # Single element should return the same list
    assert module_0.intersperse([1], 4) == [1]

    # Multiple elements with delimiter between them
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -4) == [-1, -4, -2, -4, -3]

    # Two elements
    assert module_0.intersperse([5, 6], 0) == [5, 0, 6]

    # Delimiter value same as element value
    assert module_0.intersperse([7, 7, 7], 7) == [7, 7, 7, 7, 7]

    # Zero delimiter
    assert module_0.intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()
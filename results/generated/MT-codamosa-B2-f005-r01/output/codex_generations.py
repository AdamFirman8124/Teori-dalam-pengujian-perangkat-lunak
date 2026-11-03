

# Generated at 2026-11-03 04:51:57.338134
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 4) == []

    # Test single element
    assert module_0.intersperse([1], 4) == [1]

    # Test two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative numbers
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test delimiter equal to element values
    assert module_0.intersperse([5, 5, 5], 5) == [5, 5, 5, 5, 5]

    # Test original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 4)
    assert original == [1, 2, 3]

    print("All tests passed!")


test_intersperse()

# Generated at 2026-11-03 04:54:33.194528
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 4) == []

    # Test single element (no delimiter needed)
    assert module_0.intersperse([5], 4) == [5]

    # Test two elements
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with zero delimiter
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -9) == [-1, -9, -2, -9, -3]

    # Test delimiter equal to elements
    assert module_0.intersperse([7, 7, 7], 7) == [7, 7, 7, 7, 7]

    # Test original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 4)
    assert original == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 04:56:28.190627
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

    # Test with zero delimiter
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test with negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -9) == [-1, -9, -2, -9, -3]

    # Test that original list is not modified
    original = [1, 2, 3]
    module_0.intersperse(original, 9)
    assert original == [1, 2, 3]

    # Test with duplicate values
    assert module_0.intersperse([7, 7, 7], 1) == [7, 1, 7, 1, 7]

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 04:59:05.478047
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 7) == []

    # Test single element list
    assert module_0.intersperse([5], 7) == [5]

    # Test two elements
    assert module_0.intersperse([1, 2], 3) == [1, 3, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test with negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test with negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test with duplicate values
    assert module_0.intersperse([5, 5, 5], 1) == [5, 1, 5, 1, 5]

    # Test delimiter same as element values
    assert module_0.intersperse([2, 2], 2) == [2, 2, 2]

    # Test longer list
    assert module_0.intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]

    # Verify result length for n elements is 2n - 1
    result = module_0.intersperse([1, 2, 3, 4], 9)
    assert len(result) == 2 * 4 - 1

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()
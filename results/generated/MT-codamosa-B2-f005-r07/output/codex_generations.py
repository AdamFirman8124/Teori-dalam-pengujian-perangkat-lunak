

# Generated at 2026-11-03 00:27:57.554396
# Unit test for function intersperse
def test_intersperse():
    # Empty list should return an empty list
    assert module_0.intersperse([], 4) == []

    # Single element: no delimiter needed
    assert module_0.intersperse([5], 4) == [5]

    # Two elements: one delimiter between them
    assert module_0.intersperse([1, 2], 4) == [1, 4, 2]

    # Multiple elements: delimiter between each pair
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Delimiter can be any integer, including negative
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Delimiter of zero works too
    assert module_0.intersperse([7, 8], 0) == [7, 0, 8]

    # Input list is not modified
    nums = [1, 2, 3]
    module_0.intersperse(nums, 9)
    assert nums == [1, 2, 3]

    # Larger list
    assert module_0.intersperse(list(range(5)), 100) == [0, 100, 1, 100, 2, 100, 3, 100, 4]


if __name__ == "__main__":
    test_intersperse()
    print("All tests passed!")

# Generated at 2026-11-03 00:29:04.318644
# Unit test for function intersperse
def test_intersperse():
    # Empty list returns empty list
    assert module_0.intersperse([], 7) == []

    # Single element: no delimiter added
    assert module_0.intersperse([5], 7) == [5]

    # Multiple elements: delimiter inserted between them
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Delimiter of 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Negative delimiter
    assert module_0.intersperse([10, 20, 30], -1) == [10, -1, 20, -1, 30]

    # Repeated elements
    assert module_0.intersperse([1, 1, 1], 2) == [1, 2, 1, 2, 1]

    # Two elements
    assert module_0.intersperse([3, 9], 5) == [3, 5, 9]

    # Delimiter larger than elements
    assert module_0.intersperse([1, 2], 100) == [1, 100, 2]

# Generated at 2026-11-03 00:30:07.290662
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 7) == []

    # Test single element list
    assert module_0.intersperse([5], 7) == [5]

    # Test two elements
    assert module_0.intersperse([1, 2], 7) == [1, 7, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test delimiter of 0
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

    # Test negative delimiter
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

    # Test negative numbers in list
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]

    # Test duplicate values
    assert module_0.intersperse([5, 5, 5], 1) == [5, 1, 5, 1, 5]

    # Test larger list
    assert module_0.intersperse([10, 20, 30, 40, 50], 99) == [10, 99, 20, 99, 30, 99, 40, 99, 50]

    # Test result type
    assert isinstance(module_0.intersperse([1, 2], 3), list)

    print("All tests passed!")


if __name__ == "__main__":
    test_intersperse()

# Generated at 2026-11-03 00:30:59.214699
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 7) == []
    assert module_0.intersperse([5], 7) == [5]
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]
    assert module_0.intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]
    assert module_0.intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]
    assert module_0.intersperse([10, 20], 10) == [10, 10, 20]

# Generated at 2026-11-03 00:32:33.315114
# Unit test for function intersperse
def test_intersperse():
    # Test empty list
    assert module_0.intersperse([], 4) == []

    # Test single element list
    assert module_0.intersperse([5], 4) == [5]

    # Test two element list
    assert module_0.intersperse([1, 2], 3) == [1, 3, 2]

    # Test multiple elements
    assert module_0.intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

    # Test delimiter of 0
    assert module_0.intersperse([7, 8, 9], 0) == [7, 0, 8, 0, 9]

    # Test negative numbers and negative delimiter
    assert module_0.intersperse([-1, -2, -3], -5) == [-1, -5, -2, -5, -3]

    # Test delimiter same as elements
    assert module_0.intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2]

    # Test result length is correct: 2*n - 1 for n > 0
    assert len(module_0.intersperse([1, 2, 3, 4, 5], 0)) == 9

    print("All tests passed!")


test_intersperse()
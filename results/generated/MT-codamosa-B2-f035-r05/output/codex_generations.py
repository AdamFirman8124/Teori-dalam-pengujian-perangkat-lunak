

# Generated at 2026-11-02 16:31:24.495430
# Unit test for function max_element
def test_max_element():
    # Basic case: positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    # List where max is not the last element
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    # All negative numbers
    assert module_0.max_element([-5, -3, -1, -10]) == -1
    # Single element list
    assert module_0.max_element([42]) == 42
    # Duplicates of the maximum
    assert module_0.max_element([7, 7, 7, 7]) == 7
    # Mixed positive and negative
    assert module_0.max_element([-10, 0, 10]) == 10
    # Max at the beginning
    assert module_0.max_element([100, 2, 3, 4]) == 100
    # Max in the middle
    assert module_0.max_element([1, 50, 2]) == 50
    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    # Two elements
    assert module_0.max_element([3, 1]) == 3
    assert module_0.max_element([1, 3]) == 3

# Generated at 2026-11-02 16:32:16.322073
# Unit test for function max_element
def test_max_element():
    # Basic case with positive integers
    assert module_0.max_element([1, 2, 3]) == 3
    # Max element not at the end
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    # Negative numbers only
    assert module_0.max_element([-10, -20, -3]) == -3
    # Single element list
    assert module_0.max_element([42]) == 42
    # All elements equal
    assert module_0.max_element([7, 7, 7]) == 7
    # Duplicates of the max value
    assert module_0.max_element([1, 9, 2, 9]) == 9
    # List with mixed positive and negative values
    assert module_0.max_element([-1, 0, 1]) == 1
    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    # Max element at the beginning
    assert module_0.max_element([100, 4, 2, 8]) == 100
    # Unsorted list with zeros
    assert module_0.max_element([0, -1, 0, -2]) == 0

# Generated at 2026-11-02 16:33:31.850636
# Unit test for function max_element
def test_max_element():
    # Basic case with positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

    # Max element at the beginning
    assert module_0.max_element([100, 2, 3, 4, 5]) == 100

    # Max element in the middle
    assert module_0.max_element([1, 2, 50, 3, 4]) == 50

    # Max element at the end
    assert module_0.max_element([1, 2, 3, 4, 99]) == 99

    # All negative numbers
    assert module_0.max_element([-1, -5, -3, -2]) == -1
    assert module_0.max_element([-10]) == -10

    # Single element list
    assert module_0.max_element([42]) == 42

    # List with duplicates
    assert module_0.max_element([7, 7, 7, 7]) == 7
    assert module_0.max_element([3, 3, 9, 9, 1]) == 9

    # Floating point numbers
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Mixed integers and floats
    assert module_0.max_element([1, 2.5, 2, 1.9]) == 2.5

    # Zeros and small numbers
    assert module_0.max_element([0, 0, 0]) == 0
    assert module_0.max_element([0, -1, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_max_element()

# Generated at 2026-11-02 16:34:46.237519
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, -124]) == 9

    # Single element list
    assert module_0.max_element([7]) == 7
    assert module_0.max_element([-7]) == -7

    # All negative numbers
    assert module_0.max_element([-10, -20, -3, -50]) == -3

    # Duplicates of the maximum
    assert module_0.max_element([4, 4, 4]) == 4
    assert module_0.max_element([1, 5, 5, 2]) == 5

    # Max at various positions
    assert module_0.max_element([10, 1, 2, 3]) == 10   # max at start
    assert module_0.max_element([1, 2, 3, 10]) == 10   # max at end
    assert module_0.max_element([1, 10, 2, 3]) == 10   # max in middle

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # Two elements
    assert module_0.max_element([1, 2]) == 2
    assert module_0.max_element([2, 1]) == 2

    # Booleans mixed with ints (True == 1, False == 0)
    assert module_0.max_element([False, True]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_max_element()

# Generated at 2026-11-02 16:36:03.368101
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # All negative numbers
    assert module_0.max_element([-1, -5, -3]) == -1
    assert module_0.max_element([-10, -20, -30]) == -10

    # Mixed positive and negative
    assert module_0.max_element([-5, 0, 5]) == 5
    assert module_0.max_element([0, -1, -2]) == 0

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([1, 3, 3, 2]) == 3

    # Max at various positions
    assert module_0.max_element([10, 1, 2, 3]) == 10   # max first
    assert module_0.max_element([1, 2, 3, 10]) == 10   # max last
    assert module_0.max_element([1, 10, 2, 3]) == 10   # max middle

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Large numbers
    assert module_0.max_element([10**9, 10**18]) == 10**18

    # Empty list should raise IndexError
    try:
        module_0.max_element([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass

    print("All tests passed!")
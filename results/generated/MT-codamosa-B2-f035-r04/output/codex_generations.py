

# Generated at 2026-11-03 06:11:19.325248
# Unit test for function max_element
def test_max_element():
    # Test with basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Test with all negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -3, -5, -2, -3, -3, -9, -124]) == -2

    # Test with mixed positive and negative numbers
    assert module_0.max_element([-10, 0, 10]) == 10
    assert module_0.max_element([0, -1, 1]) == 1

    # Test with single element list
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Test with duplicate elements
    assert module_0.max_element([3, 3, 3]) == 3
    assert module_0.max_element([1, 1, 2, 2, 2]) == 2

    # Test with max element at various positions
    assert module_0.max_element([10, 1, 2, 3]) == 10   # max at beginning
    assert module_0.max_element([1, 2, 3, 10]) == 10   # max at end
    assert module_0.max_element([1, 10, 2, 3]) == 10   # max in middle

    # Test with floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Test with zeros
    assert module_0.max_element([0, 0, 0]) == 0

    # Test with large numbers
    assert module_0.max_element([10**9, 10**8, 10**10]) == 10**10

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_max_element()

# Generated at 2026-11-03 06:12:47.076801
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # All negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -3, -10]) == -3

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Duplicates
    assert module_0.max_element([2, 2, 2, 2]) == 2
    assert module_0.max_element([1, 1, 5, 5, 3]) == 5

    # Max at various positions
    assert module_0.max_element([10, 1, 2, 3]) == 10   # max first
    assert module_0.max_element([1, 2, 3, 10]) == 10   # max last
    assert module_0.max_element([1, 10, 2, 3]) == 10   # max middle

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # Zero included
    assert module_0.max_element([0, -1, -2]) == 0
    assert module_0.max_element([-1, 0, -2]) == 0

# Generated at 2026-11-03 06:14:09.915842
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Negative numbers only
    assert module_0.max_element([-1, -5, -3]) == -1
    assert module_0.max_element([-10, -20, -30]) == -10

    # Single element list
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Duplicates of max element
    assert module_0.max_element([4, 4, 4]) == 4
    assert module_0.max_element([1, 9, 9, 2]) == 9

    # Max at various positions
    assert module_0.max_element([10, 2, 3]) == 10       # max at start
    assert module_0.max_element([1, 2, 10]) == 10       # max at end
    assert module_0.max_element([1, 10, 2]) == 10       # max in middle

    # Mixed positive and negative
    assert module_0.max_element([0, -1, 1]) == 1
    assert module_0.max_element([-100, 0, 100]) == 100

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Unsorted larger list
    assert module_0.max_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 9

    # Zero and near-zero cases
    assert module_0.max_element([0, 0, 0]) == 0

# Generated at 2026-11-03 06:15:26.000016
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([3, 2, 1]) == 3
    assert module_0.max_element([5, 5, 5]) == 5

    # Single element
    assert module_0.max_element([42]) == 42

    # Negative numbers
    assert module_0.max_element([-1, -5, -3]) == -1
    assert module_0.max_element([-10]) == -10

    # Mixed positive and negative
    assert module_0.max_element([-7, 0, 3, -2]) == 3

    # Duplicates of max value
    assert module_0.max_element([2, 9, 9, 4]) == 9

    # Floats
    assert module_0.max_element([1.5, 2.7, 2.6]) == 2.7

    # Max at various positions
    assert module_0.max_element([9, 1, 2]) == 9
    assert module_0.max_element([1, 9, 2]) == 9
    assert module_0.max_element([1, 2, 9]) == 9

# Generated at 2026-11-03 06:17:06.880489
# Unit test for function max_element
def test_max_element():
    # Test with basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Test with negative numbers only
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -3, -8, -1]) == -1

    # Test with mixed positive and negative numbers
    assert module_0.max_element([-10, 0, 10]) == 10
    assert module_0.max_element([0, -3, 2, -1]) == 2

    # Test with single element list
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Test with duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([1, 3, 3, 2]) == 3

    # Test with floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Test with unsorted list where max is at the beginning
    assert module_0.max_element([100, 4, 2, 8]) == 100

    # Test with max at the end
    assert module_0.max_element([1, 4, 2, 800]) == 800

    # Test with max in the middle
    assert module_0.max_element([1, 4, 50, 2, 8]) == 50
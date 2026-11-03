

# Generated at 2026-11-02 15:27:42.773968
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Negative numbers only
    assert module_0.max_element([-1, -5, -3]) == -1
    assert module_0.max_element([-10]) == -10

    # Single element
    assert module_0.max_element([42]) == 42

    # Max at beginning
    assert module_0.max_element([100, 2, 3, 4]) == 100

    # Max in middle
    assert module_0.max_element([1, 99, 3]) == 99

    # Duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([1, 7, 3, 7]) == 7

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7

    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # All equal elements
    assert module_0.max_element([0, 0, 0]) == 0

    print("All tests passed!")


test_max_element()

# Generated at 2026-11-02 15:29:13.862387
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

    # Max at the beginning
    assert module_0.max_element([10, 3, 5, 1]) == 10

    # Max at the end
    assert module_0.max_element([1, 2, 3, 4, 5]) == 5

    # Negative numbers only
    assert module_0.max_element([-5, -3, -1, -10]) == -1

    # Single element
    assert module_0.max_element([42]) == 42

    # Duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([3, 7, 3, 7]) == 7

    # Mixed positive and negative
    assert module_0.max_element([-100, 0, 100]) == 100

    # Floats
    assert module_0.max_element([1.5, 2.5, 0.5]) == 2.5

    # Two elements
    assert module_0.max_element([2, 1]) == 2
    assert module_0.max_element([1, 2]) == 2

    print("All tests passed!")


test_max_element()

# Generated at 2026-11-02 15:30:20.978795
# Unit test for function max_element
def test_max_element():
    # Basic cases
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([10]) == 10
    assert module_0.max_element([1, 2, 3, 4, 5]) == 5
    assert module_0.max_element([5, 4, 3, 2, 1]) == 1
    assert module_0.max_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 9
    assert module_0.max_element([0, 0, 0]) == 0
    assert module_0.max_element([-10, -20, -5, -1]) == -1
    assert module_0.max_element([2.5, 3.7, 1.1]) == 3.7
    assert module_0.max_element([7, 7, 7, 7]) == 7
    assert module_0.max_element([100, 100, 99]) == 100

    # Max element at various positions
    assert module_0.max_element([9, 1, 2]) == 9       # at start
    assert module_0.max_element([1, 9, 2]) == 9       # in middle
    assert module_0.max_element([1, 2, 9]) == 9       # at end

    # Large values
    assert module_0.max_element([10**6, 10**9, 10**3]) == 10**9

# Generated at 2026-11-02 15:31:20.499015
# Unit test for function max_element
def test_max_element():
    # Test with a list of positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    # Test with a list where max is not the last element
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    # Test with negative numbers only
    assert module_0.max_element([-1, -2, -3]) == -1
    # Test with a single element list
    assert module_0.max_element([42]) == 42
    # Test with duplicate maximum values
    assert module_0.max_element([7, 7, 7]) == 7
    # Test with mixed positive and negative numbers
    assert module_0.max_element([-10, 0, 10]) == 10
    # Test with float values
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    # Test with two elements
    assert module_0.max_element([1, 2]) == 2
    assert module_0.max_element([2, 1]) == 2

# Generated at 2026-11-02 15:32:28.656729
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

    # Negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -10, -3]) == -3

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([0]) == 0

    # Duplicates
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([3, 3, 1, 3]) == 3

    # Max at different positions
    assert module_0.max_element([9, 1, 2]) == 9      # max first
    assert module_0.max_element([1, 9, 2]) == 9      # max middle
    assert module_0.max_element([1, 2, 9]) == 9      # max last

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Mixed ints and floats
    assert module_0.max_element([1, 2.5, 2]) == 2.5

    # All elements equal to first (m initialized to l[0])
    assert module_0.max_element([4, 1, 1, 0]) == 4

    # Booleans (True == 1)
    assert module_0.max_element([False, True, False]) is True
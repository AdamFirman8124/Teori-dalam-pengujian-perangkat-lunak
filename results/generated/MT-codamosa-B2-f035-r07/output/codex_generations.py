

# Generated at 2026-11-02 12:42:49.240855
# Unit test for function max_element
def test_max_element():
    # Basic case: positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

    # Max at the beginning
    assert module_0.max_element([100, 2, 3, 4]) == 100

    # Max at the end
    assert module_0.max_element([1, 2, 3, 100]) == 100

    # All negative numbers
    assert module_0.max_element([-1, -5, -3]) == -1
    assert module_0.max_element([-10, -20, -30]) == -10

    # Single element list
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Duplicates of the max value
    assert module_0.max_element([5, 5, 5]) == 5
    assert module_0.max_element([1, 7, 7, 3]) == 7

    # Mixed positive and negative numbers
    assert module_0.max_element([-100, 0, 100]) == 100
    assert module_0.max_element([0, -1, -2]) == 0

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.1, -2.2, -0.5]) == -0.5

    # Max appears multiple times
    assert module_0.max_element([3, 9, 1, 9, 2]) == 9

    # Zeros and mixed values
    assert module_0.max_element([0, 0, -1]) == 0

# Generated at 2026-11-02 12:46:14.077180
# Unit test for function max_element
def test_max_element():
    # Basic case: max is at the end
    assert module_0.max_element([1, 2, 3]) == 3
    # Max is at the beginning
    assert module_0.max_element([5, 3, 1]) == 5
    # Max is in the middle
    assert module_0.max_element([1, 9, 2]) == 9
    # All negative numbers
    assert module_0.max_element([-5, -2, -10]) == -2
    # Mixed positive and negative
    assert module_0.max_element([-1, 0, 1]) == 1
    # Single element list
    assert module_0.max_element([42]) == 42
    # Duplicates of max
    assert module_0.max_element([7, 7, 7]) == 7
    # Duplicated max among others
    assert module_0.max_element([3, 8, 8, 2]) == 8
    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    # Two elements
    assert module_0.max_element([2, 1]) == 2


def test_max_element_negative_only():
    assert module_0.max_element([-10, -3, -7]) == -3


def test_max_element_single_element():
    assert module_0.max_element([0]) == 0


def test_max_element_empty_list_raises():
    # Accessing l[0] on an empty list raises IndexError
    with pytest.raises(IndexError):
        module_0.max_element([])

# Generated at 2026-11-02 12:49:02.263768
# Unit test for function max_element
def test_max_element():
    # Basic positive numbers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # All negative numbers
    assert module_0.max_element([-1, -2, -3]) == -1
    assert module_0.max_element([-5, -10, -3]) == -3

    # Single element
    assert module_0.max_element([42]) == 42
    assert module_0.max_element([-7]) == -7

    # Duplicates of the max value
    assert module_0.max_element([7, 7, 7]) == 7
    assert module_0.max_element([3, 9, 9, 2]) == 9

    # Mixed with zero
    assert module_0.max_element([-1, 0, -5]) == 0

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7

    # Max at various positions
    assert module_0.max_element([10, 1, 2, 3]) == 10   # first
    assert module_0.max_element([1, 2, 3, 10]) == 10   # last
    assert module_0.max_element([1, 10, 2, 3]) == 10   # middle

# Generated at 2026-11-02 12:50:20.725927
# Unit test for function max_element
def test_max_element():
    # Basic positive integers
    assert module_0.max_element([1, 2, 3]) == 3
    assert module_0.max_element([5, 3, -5, 2, -3, 3, 9, 0, 124]) == 124

    # Max at the beginning
    assert module_0.max_element([10, 2, 8, 1]) == 10

    # Max at the end
    assert module_0.max_element([1, 2, 10]) == 10

    # All negative numbers
    assert module_0.max_element([-5, -3, -1, -10]) == -1

    # Single element
    assert module_0.max_element([42]) == 42

    # Duplicates of the max
    assert module_0.max_element([7, 7, 7, 7]) == 7

    # Mixed positives and negatives
    assert module_0.max_element([-1, -2, -3, 0]) == 0

    # Floats
    assert module_0.max_element([1.5, 2.7, 0.3]) == 2.7
    assert module_0.max_element([-1.5, -2.7, -0.3]) == -0.3

    # Unsorted with repeated values
    assert module_0.max_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 9

    # Empty list should raise IndexError
    try:
        module_0.max_element([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass
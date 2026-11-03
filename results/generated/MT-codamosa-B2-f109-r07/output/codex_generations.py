

# Generated at 2026-11-02 19:25:16.378493
# Unit test for function move_one_ball
def test_move_one_ball():
    # nonce:ffd1735a
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element array
    assert module_0.move_one_ball([1]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Arrays that are rotations of a sorted array (one right shift away)
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Two elements, swapped order
    assert module_0.move_one_ball([2, 1]) == True

    # Arrays that cannot be sorted by a single rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 1, 3, 4]) == False

    # Arrays with duplicate values
    assert module_0.move_one_ball([2, 2, 3, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1, 2]) == True

    # Arrays containing negative numbers
    assert module_0.move_one_ball([2, -3, -1]) == True
    assert module_0.move_one_ball([-1, -3, 2]) == False

# Generated at 2026-11-02 19:25:41.666898
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element arrays are trivially sorted
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([7]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([1, 1, 2, 2]) == True

    # Arrays sortable by right shift rotation
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([2, 2, 1]) == True

    # Arrays not sortable by any rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([1, 2, 3, 3, 2]) == False

    # Works with negative numbers
    assert module_0.move_one_ball([-1, 0, -3]) == True   # rotates to [-3, -1, 0]
    assert module_0.move_one_ball([-5, -3, -4]) == False

    # Original array must not be modified
    arr = [3, 4, 5, 1, 2]
    module_0.move_one_ball(arr)
    assert arr == [3, 4, 5, 1, 2]

# Generated at 2026-11-02 19:27:21.645819
# Unit test for function move_one_ball
def test_move_one_ball():
    # Already sorted arrays
    assert module_0.move_one_ball([]) == True
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([1, 2, 3]) == True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Valid right rotations of sorted arrays
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([3, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([2, 2, 3, 1]) == True  # duplicates

    # Arrays that cannot be fixed by right shifts
    assert module_0.move_one_ball([7, 4, 3, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False  # reversed
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 3]) == False
    assert module_0.move_one_ball([3, 4, 5, 2, 1]) == False

# Generated at 2026-11-02 19:27:58.010733
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is considered sorted
    assert module_0.move_one_ball([]) == True
    # Single element
    assert module_0.move_one_ball([1]) == True
    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    # Can be sorted with one rotation
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([2, 1]) == True
    # Cannot be sorted with one rotation
    assert module_0.move_one_ball([4, 3, 1, 2]) == False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    # Array with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([3, 1, 1, 2]) == False
    # Negative numbers
    assert module_0.move_one_ball([-2, -1, -3]) == True
    assert module_0.move_one_ball([-3, -1, -2]) == False
    print("All test cases passed!")

# Generated at 2026-11-02 19:28:41.753048
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element
    assert module_0.move_one_ball([1]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([-3, -1, 0, 2, 7]) == True

    # Arrays sortable by right-shift rotations
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True

    # Arrays not sortable by right-shift rotations
    assert module_0.move_one_ball([2, 1, 3, 4]) == False
    assert module_0.move_one_ball([4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 3, 1, 2]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([3, 1, 2, 2, 1]) == False

    # Negative numbers
    assert module_0.move_one_ball([-2, -1, -5, -4, -3]) == True
    assert module_0.move_one_ball([-1, -5, -3, -2, -4]) == False

    print("All tests passed!")


test_move_one_ball()
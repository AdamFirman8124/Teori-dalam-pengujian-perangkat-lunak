

# Generated at 2026-11-03 01:03:06.315148
# Unit test for function move_one_ball
def test_move_one_ball():
    # Test with empty array
    assert module_0.move_one_ball([]) == True

    # Test with single element
    assert module_0.move_one_ball([1]) == True

    # Test with already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Test with array that can be sorted by one rotation
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Test with array that can be sorted by rotation
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Test with array that cannot be sorted by rotation
    assert module_0.move_one_ball([2, 1, 3, 5, 4]) == False

    # Test with array containing duplicates
    assert module_0.move_one_ball([3, 3, 1, 2]) == True

    # Test with array with duplicates that can't be rotated to sorted
    assert module_0.move_one_ball([3, 1, 3, 2]) == False

    # Test with two elements
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # Test with negative numbers
    assert module_0.move_one_ball([-3, -2, -1]) == True
    assert module_0.move_one_ball([-1, -3, -2]) == True
    assert module_0.move_one_ball([-2, -1, -3]) == True

    # Test with mixed positive and negative
    assert module_0.move_one_ball([-1, 0, 1]) == True
    assert module_0.move_one_ball([1, -1, 0]) == True
    assert module_0.move_one_ball([0, 1, -1]) == True

    # Test with larger array that cannot be sorted
    assert module_0.move_one_ball([7, 4, 2, 9, 1]) == False

    # Test with array where min appears multiple times
    assert module_0.move_one_ball([1, 2, 1, 2]) == False

    # Test reverse sorted array
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Test with all same elements
    assert module_0.move_one_ball([2, 2, 2, 2]) == True

    # Test with a rotation of sorted array with duplicates
    assert module_0.move_one_ball([2, 3, 1, 1]) == True

    print("All tests passed!")


test_move_one_ball()

# Generated at 2026-11-03 01:04:35.587890
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element array should return True
    assert module_0.move_one_ball([1]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Array that can be sorted by one right rotation
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Array that can be sorted by right rotations
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True

    # Array that cannot be sorted by any rotation
    assert module_0.move_one_ball([4, 3, 1, 2]) == False

    # Another array that cannot be sorted by rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False

    # Two elements swapped (not a rotation of sorted order)
    assert module_0.move_one_ball([2, 1]) == False

    # Two elements in sorted order
    assert module_0.move_one_ball([1, 2]) == True

    # Reverse sorted array cannot be fixed by rotation
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Large rotation case
    assert module_0.move_one_ball([7, 8, 9, 1, 2, 3, 4, 5, 6]) == True

    # Unsorted with multiple disorder points
    assert module_0.move_one_ball([2, 3, 1, 5, 4]) == False

    # Negative numbers, rotatable
    assert module_0.move_one_ball([-3, -2, -1, -5, -4]) == True

    # Negative numbers, not rotatable
    assert module_0.move_one_ball([-1, -3, -2, -5, -4]) == False

    # Duplicates that form a valid rotation
    assert module_0.move_one_ball([2, 2, 3, 1, 2]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_move_one_ball()

# Generated at 2026-11-03 01:06:45.633900
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element
    assert module_0.move_one_ball([5]) == True

    # Two elements in sorted order
    assert module_0.move_one_ball([1, 2]) == True

    # Two elements needing one rotation
    assert module_0.move_one_ball([2, 1]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Rotated sorted array (one right rotation of sorted)
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Rotation of sorted array with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([3, 1, 2]) == True

    # Array that cannot be sorted by a single rotation
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([1, 2, 4, 3]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 3, 1, 4]) == False

    # Array with negative numbers
    assert module_0.move_one_ball([-3, -2, -5, -4]) == True  # rotation of sorted
    assert module_0.move_one_ball([-1, -3, -2, -4]) == False

    # Larger rotated array
    assert module_0.move_one_ball([7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == True
    assert module_0.move_one_ball([7, 8, 9, 10, 2, 1, 3, 4, 5, 6]) == False

# Generated at 2026-11-03 01:10:11.769271
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is trivially sortable
    assert module_0.move_one_ball([]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([1, 2, 3]) == True
    assert module_0.move_one_ball([1, 2, 4, 5, 6]) == True

    # Arrays that are rotations of their sorted version
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([4, 5, 6, 1, 2, 3]) == True

    # Arrays that cannot be sorted by right shifts
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == False
    assert module_0.move_one_ball([2, 1, 3]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([7, 8, 3, 5, 6, 1, 2]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 2]) == True
    assert module_0.move_one_ball([3, 1, 2, 2, 3]) == False
    assert module_0.move_one_ball([2, 3, 1, 2]) == True
    assert module_0.move_one_ball([1, 1, 2, 1]) == True

    # Negative numbers
    assert module_0.move_one_ball([-1, -2, -3]) == False
    assert module_0.move_one_ball([-3, -2, -1]) == True
    assert module_0.move_one_ball([-2, -1, -3]) == True

    # Mixed positive and negative
    assert module_0.move_one_ball([-1, 0, 1]) == True
    assert module_0.move_one_ball([1, -1, 0]) == False
    assert module_0.move_one_ball([0, 1, -1]) == True

    print("All tests passed!")


test_move_one_ball()

# Generated at 2026-11-03 01:12:06.156914
# Unit test for function move_one_ball
def test_move_one_ball():
    # nonce:5a93755a
    # Test with empty array
    assert module_0.move_one_ball([]) == True

    # Test with single element
    assert module_0.move_one_ball([7]) == True

    # Test with already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Test with array sortable by one or more right shifts
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Test with two elements swapped (rotatable)
    assert module_0.move_one_ball([2, 1]) == True

    # Test with two elements in order
    assert module_0.move_one_ball([1, 2]) == True

    # Test with array not sortable by rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False

    # Test with reverse sorted array (length > 2, not rotatable)
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Test with duplicates, sortable by rotation
    assert module_0.move_one_ball([2, 3, 1, 2]) == True

    # Test with duplicates, not sortable by rotation
    assert module_0.move_one_ball([2, 1, 3, 2]) == False

    # Test with negative numbers
    assert module_0.move_one_ball([-1, -3, -2]) == True
    assert module_0.move_one_ball([-2, -1, -3]) == True
    assert module_0.move_one_ball([-2, -3, -1]) == False

    # Test with all identical elements
    assert module_0.move_one_ball([4, 4, 4, 4]) == True

    print("All tests passed!")


# Generated at 2026-11-01 22:39:00.343808
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element
    assert module_0.move_one_ball([1]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Can be sorted via right shift rotations
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True

    # Cannot be sorted via right shift rotations
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([7, 4, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 2, 4, 3]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 1, 2]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([2, 1, 1]) == True

    # Negative numbers
    assert module_0.move_one_ball([-1, 0, -3]) == True
    assert module_0.move_one_ball([-3, -2, -5]) == False

# Generated at 2026-11-01 22:39:41.426634
# Unit test for function move_one_ball
def test_move_one_ball():
# nonce:138c4676
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element arrays
    assert module_0.move_one_ball([7]) == True
    assert module_0.move_one_ball([0]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # Arrays sortable by rotation (right shift)
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([4, 1, 2, 3]) == True
    assert module_0.move_one_ball([2, 3, 4, 1]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([3, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True

    # Arrays not sortable by rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 3]) == False
    assert module_0.move_one_ball([1, 2, 4, 3]) == False
    assert module_0.move_one_ball([1, 2, 1]) == False

    # Arrays with duplicate values
    assert module_0.move_one_ball([1, 1]) == True
    assert module_0.move_one_ball([2, 2, 2, 2]) == True
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([3, 1, 2, 3]) == True

    # Arrays with negative numbers
    assert module_0.move_one_ball([-3, -2, -1]) == True
    assert module_0.move_one_ball([-2, -1, -3]) == True
    assert module_0.move_one_ball([-1, -5, 0]) == False
    assert module_0.move_one_ball([5, -1, 2, 3]) == True

# Generated at 2026-11-01 22:40:23.189405
# Unit test for function move_one_ball
def test_move_one_ball():# Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element array should return True
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([7]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # Arrays sortable with one right shift should return True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([1000000, 1, 2]) == True

    # Arrays not sortable with one right shift should return False
    assert module_0.move_one_ball([4, 3, 1, 2]) == False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 1, 3, 3]) == False

    # Arrays with duplicate elements
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([3, 3, 1, 2]) == True
    assert module_0.move_one_ball([2, 1, 2, 2]) == False

    # Arrays with negative numbers
    assert module_0.move_one_ball([-2, -1, -3]) == True
    assert module_0.move_one_ball([-3, -2, -1]) == True
    assert module_0.move_one_ball([-1, -2, -3]) == False
    assert module_0.move_one_ball([-1, 0, 1]) == True
    assert module_0.move_one_ball([0, -1, 1]) == False

    # Mixed positive/negative with rotation
    assert module_0.move_one_ball([1, -2, -3]) == True
    assert module_0.move_one_ball([-3, 1, -2]) == False

# Generated at 2026-11-01 22:40:58.719867
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element array should return True
    assert module_0.move_one_ball([7]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Array that can be sorted via rotations should return True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True

    # Array that cannot be sorted via rotations should return False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 3]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([7, 5, 3, 1]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 3, 1, 2]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([3, 1, 2, 2]) == False

    # Two element arrays
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([1, 2]) == True
    assert module_0.move_one_ball([2, 2]) == True

    print("All tests passed!")

test_move_one_ball()

# Generated at 2026-11-01 22:41:39.902550
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should always return True
    assert module_0.move_one_ball([]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Can be sorted with one right shift (rotation)
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Another valid rotation case
    assert module_0.move_one_ball([7, 1, 2, 3, 4, 5, 6]) == True

    # Cannot be sorted with one rotation
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False

    # Unsorted, not a rotation of sorted array
    assert module_0.move_one_ball([2, 1, 4, 3]) == False

    # Single element array
    assert module_0.move_one_ball([42]) == True

    # Two elements, swappable via rotation
    assert module_0.move_one_ball([2, 1]) == True

    # Two elements already sorted
    assert module_0.move_one_ball([1, 2]) == True

    # Duplicates with rotation possible
    assert module_0.move_one_ball([2, 3, 3, 5, 5, 1]) == True

    # Duplicates but not sortable by one rotation
    assert module_0.move_one_ball([1, 3, 2, 2]) == False

    # Negative numbers, valid rotation
    assert module_0.move_one_ball([-2, -1, -5, -4, -3]) == True

    # Negative numbers, invalid
    assert module_0.move_one_ball([-1, -5, -3, -2, -4]) == False
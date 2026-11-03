

# Generated at 2026-11-02 00:17:28.064483
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element array should return True
    assert module_0.move_one_ball([7]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Array sortable by rotation should return True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([3, 1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True

    # Array not sortable by rotation should return False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([2, 3, 1, 5, 4]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False

    # Negative numbers
    assert module_0.move_one_ball([-2, -1, -3]) == True
    assert module_0.move_one_ball([-1, -3, -2]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([1, 2, 2, 1]) == False
    assert module_0.move_one_ball([5, 5, 5]) == True

    # Larger mixed array
    assert module_0.move_one_ball([7, 8, 9, 1, 2, 3, 4, 5, 6]) == True
    assert module_0.move_one_ball([7, 8, 9, 3, 2, 1, 4, 5, 6]) == False

    print("All tests passed!")


test_move_one_ball()

# Generated at 2026-11-02 00:18:08.921704
# Unit test for function move_one_ball
def test_move_one_ball():
    # Test empty array
    assert module_0.move_one_ball([]) == True
    
    # Test single element
    assert module_0.move_one_ball([1]) == True
    
    # Test already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    
    # Test array that can be sorted by right shift
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    
    # Test array that can be sorted by right shift
    assert module_0.move_one_ball([2, 3, 4, 1]) == True
    
    # Test array that cannot be sorted by right shift
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    
    # Test array that cannot be sorted by right shift
    assert module_0.move_one_ball([1, 3, 2]) == False
    
    # Test two elements
    assert module_0.move_one_ball([7, 4]) == True
    assert module_0.move_one_ball([4, 7]) == True
    
    # Test array with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([3, 1, 2, 1]) == False
    
    # Test larger array
    assert module_0.move_one_ball([10, 20, 30, 5, 7]) == True
    assert module_0.move_one_ball([10, 20, 30, 7, 5]) == False
    
    # Test negative numbers
    assert module_0.move_one_ball([-3, -2, -1, -5, -4]) == True
    assert module_0.move_one_ball([-1, -3, -2]) == False
    
    print("All tests passed!")

test_move_one_ball()

# Generated at 2026-11-02 00:23:00.457166
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True
    
    # Single element should return True
    assert module_0.move_one_ball([1]) == True
    
    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    
    # Array that is a rotation of sorted array should return True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    
    # Array that cannot be sorted with one rotation should return False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([2, 1, 3, 4, 5]) == False
    
    # Two elements swapped via rotation
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([7, 3]) == False
    
    # Array with duplicates that works
    assert module_0.move_one_ball([2, 2, 3, 1, 2]) == True
    
    # Array with all identical elements
    assert module_0.move_one_ball([5, 5, 5, 5]) == True
    
    # Reverse sorted array with more than needed disorder
    assert module_0.move_one_ball([4, 3, 2, 1]) == False
    
    print("All tests passed!")

test_move_one_ball()

# Generated at 2026-11-02 00:23:41.417867
# Unit test for function move_one_ball
def test_move_one_ball():
    # nonce:cafe540d
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([42]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # Arrays that are rotations of their sorted version
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([3, 5, 10, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([2, 1]) == True

    # Arrays that cannot be sorted by rotation
    assert module_0.move_one_ball([7, 4, 2, 1]) == False
    assert module_0.move_one_ball([2, 3, 4, 1, 5]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 3, 5, 4]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([-2, -3, -1]) == False
    assert module_0.move_one_ball([0, -1, 1]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([2, 1, 2, 2]) == True
    assert module_0.move_one_ball([3, 1, 2, 2]) == True
    assert module_0.move_one_ball([1, 2, 1, 2]) == False

    # Arrays with negative numbers
    assert module_0.move_one_ball([-2, -1, 0, -3]) == True
    assert module_0.move_one_ball([-5, -4, -3, -6]) == True
    assert module_0.move_one_ball([-1, 0, -2]) == False

    print("All test cases passed!")


test_move_one_ball()

# Generated at 2026-11-02 00:25:07.125813
# Unit test for function move_one_ball
def test_move_one_ball():
    # Test empty array
    assert module_0.move_one_ball([]) == True

    # Test single element array
    assert module_0.move_one_ball([5]) == True

    # Test already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Test array sortable by rotations
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Test another sortable case
    assert module_0.move_one_ball([2, 3, 1]) == True

    # Test array not sortable by rotations
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False

    # Test unsorted array that cannot be fixed
    assert module_0.move_one_ball([7, 4, 3, 2]) == False

    # Test array with duplicates (sortable)
    assert module_0.move_one_ball([2, 2, 1]) == True

    # Test array with all identical elements
    assert module_0.move_one_ball([1, 1, 1, 1]) == True

    # Test two-element arrays
    assert module_0.move_one_ball([1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True

    # Test negative numbers
    assert module_0.move_one_ball([-3, -2, -5, -4]) == False
    assert module_0.move_one_ball([-5, -4, -3, -2]) == True

    # Test mixed positive/negative
    assert module_0.move_one_ball([-1, 0, 3, -2]) == False

    # Test larger sortable array
    assert module_0.move_one_ball([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == True

    # Test larger non-sortable array
    assert module_0.move_one_ball([6, 7, 9, 8, 10, 1, 2, 3, 4, 5]) == False
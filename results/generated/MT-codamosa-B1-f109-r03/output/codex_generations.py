

# Generated at 2026-10-25 02:10:33.614677
# Unit test for function move_one_ball

# Generated at 2026-10-25 02:10:36.031168
# Unit test for function move_one_ball

# Generated at 2026-10-25 02:10:38.445488
# Unit test for function move_one_ball

# Generated at 2026-10-25 02:11:03.940088
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty, single-element, and already sorted arrays
    assert module_0.move_one_ball([]) is True
    assert module_0.move_one_ball([1]) is True
    assert module_0.move_one_ball([1, 2, 3, 4]) is True

    # Valid rotations of a sorted array
    assert module_0.move_one_ball([3, 4, 1, 2]) is True
    assert module_0.move_one_ball([4, 1, 2, 3]) is True
    assert module_0.move_one_ball([2, 3, 4, 1]) is True

    # Arrays that cannot be sorted by rotation
    assert module_0.move_one_ball([2, 1, 3, 4]) is False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) is False
    assert module_0.move_one_ball([4, 2, 3, 1]) is False

# Generated at 2026-10-25 02:11:36.095646
# Unit test for function move_one_ball
def test_move_one_ball():
    # True cases
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True
    assert module_0.move_one_ball([1, 2, 3]) == True          # already sorted
    assert module_0.move_one_ball([7]) == True                # single element
    assert module_0.move_one_ball([]) == True                 # empty
    assert module_0.move_one_ball([1, 2, 1]) == True          # duplicates across rotation point

    # False cases
    assert module_0.move_one_ball([3, 5, 1, 2, 4]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 4, 3]) == False

    print("All tests passed.")

test_move_one_ball()

# Generated at 2026-10-25 02:11:53.422583
# Unit test for function move_one_ball
def test_move_one_ball():
    # True cases
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True
    assert module_0.move_one_ball([1, 2, 3]) == True          # already sorted
    assert module_0.move_one_ball([7]) == True                # single element
    assert module_0.move_one_ball([]) == True                 # empty
    assert module_0.move_one_ball([1, 2, 1]) == True          # duplicates across rotation point

    # False cases
    assert module_0.move_one_ball([3, 5, 1, 2, 4]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 4, 3]) == False

    print("All tests passed.")

test_move_one_ball()

# Generated at 2026-10-25 02:12:19.309802
# Unit test for function move_one_ball
def test_move_one_ball():
    assert module_0.move_one_ball([]) is True
    assert module_0.move_one_ball([1]) is True
    assert module_0.move_one_ball([1, 2, 3, 4]) is True
    assert module_0.move_one_ball([3, 4, 1, 2]) is True
    assert module_0.move_one_ball([4, 5, 1, 2, 3]) is True

    assert module_0.move_one_ball([4, 3, 2, 1]) is False
    assert module_0.move_one_ball([2, 1, 3]) is False
    assert module_0.move_one_ball([3, 1, 4, 2]) is False
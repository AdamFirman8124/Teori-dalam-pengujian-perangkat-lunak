

# Generated at 2026-10-24 14:51:35.222934
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:37.633466
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:40.049268
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:42.459843
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:44.871527
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:47.285006
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:49.697877
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:52.111307
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:51:54.523506
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:52:10.988236
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:52:12.432745
# Unit test for function move_one_ball
def test_move_one_ball():
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 1, 3, 4]) == False
    assert module_0.move_one_ball([1, 2, 4, 3]) == False
    assert module_0.move_one_ball([]) == True
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True

# Generated at 2026-10-24 14:52:13.861511
# Unit test for function move_one_ball
def test_move_one_ball():
    # empty and single element
    assert module_0.move_one_ball([]) == True
    assert module_0.move_one_ball([1]) == True

    # already sorted
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # sortable by rotation
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([4, 5, 1, 2, 3]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([2, 2, 1, 2]) == True
    assert module_0.move_one_ball([2, 1, 2]) == True

    # not sortable by rotation
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([3, 2, 1]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 3, 1, 4]) == False
    assert module_0.move_one_ball([1, 2, 1]) == False
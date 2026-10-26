

# Generated at 2026-10-25 06:46:33.142373
# Unit test for function move_one_ball
def test_move_one_ball():
    # empty and single element
    assert module_0.move_one_ball([]) == True
    assert module_0.move_one_ball([1]) == True
    assert module_0.move_one_ball([5]) == True

    # already sorted
    assert module_0.move_one_ball([1, 2, 3, 4]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True

    # sortable by rotation
    assert module_0.move_one_ball([4, 1, 2, 3]) == True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([2, 1, 2]) == True

    # not sortable by rotation
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([3, 2, 1]) == False
    assert module_0.move_one_ball([4, 3, 2, 1]) == False
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False

# Generated at 2026-10-25 06:46:35.787199
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:38.202043
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:40.918024
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:43.323376
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:45.855591
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:48.397292
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:50.819414
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:53.231805
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:55.643772
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:46:58.058453
# Unit test for function move_one_ball

# Generated at 2026-10-25 06:47:13.370350
# Unit test for function move_one_ball
def test_move_one_ball():assert module_0.move_one_ball([]) == True
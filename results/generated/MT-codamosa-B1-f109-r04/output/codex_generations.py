

# Generated at 2026-10-24 14:15:47.611682
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:15:49.043506
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

# Generated at 2026-10-24 14:15:50.477468
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:15:51.910700
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

# Generated at 2026-10-24 14:15:53.315570
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:15:54.671674
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

# Generated at 2026-10-24 14:16:08.806452
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

# Generated at 2026-10-24 14:16:25.613255
# Unit test for function move_one_ball

# Generated at 2026-10-24 14:16:27.034277
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
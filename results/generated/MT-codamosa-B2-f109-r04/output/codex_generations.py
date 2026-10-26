

# Generated at 2026-10-25 07:12:40.488179
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

# Generated at 2026-10-25 07:12:42.024008
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

# Generated at 2026-10-25 07:12:43.449812
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

# Generated at 2026-10-25 07:12:44.858571
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

# Generated at 2026-10-25 07:12:46.225400
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
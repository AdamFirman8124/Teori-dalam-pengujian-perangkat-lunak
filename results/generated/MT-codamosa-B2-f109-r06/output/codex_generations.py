

# Generated at 2026-10-24 15:37:35.023340
# Unit test for function move_one_ball

# Generated at 2026-10-24 15:37:37.437365
# Unit test for function move_one_ball

# Generated at 2026-10-24 15:37:39.968542
# Unit test for function move_one_ball

# Generated at 2026-10-24 15:38:02.601498
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

# Generated at 2026-10-24 15:38:04.021015
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

# Generated at 2026-10-24 15:38:05.467637
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

# Generated at 2026-10-24 15:38:06.901348
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
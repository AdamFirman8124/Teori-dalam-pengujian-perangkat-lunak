

# Generated at 2026-10-25 00:09:51.586176
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:09:54.000520
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:09:56.415943
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:09:58.831141
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:01.245533
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:03.660447
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:06.077195
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:08.492251
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:10.911321
# Unit test for function move_one_ball

# Generated at 2026-10-25 00:10:21.496052
# Unit test for function move_one_ball
def test_move_one_ball():
    assert module_0.move_one_ball([]) is True
    assert module_0.move_one_ball([1]) is True
    assert module_0.move_one_ball([1, 2, 3, 4]) is True

    # Arrays that become sorted after a circular rotation
    assert module_0.move_one_ball([3, 4, 1, 2]) is True
    assert module_0.move_one_ball([4, 1, 2, 3]) is True
    assert module_0.move_one_ball([0, 1, -2, -1]) is True

    # Arrays that cannot become sorted by a circular rotation
    assert module_0.move_one_ball([1, 3, 2, 4]) is False
    assert module_0.move_one_ball([4, 3, 2, 1]) is False
    assert module_0.move_one_ball([2, 1, 3, 4]) is False

# Generated at 2026-10-25 00:10:28.037298
# Unit test for function move_one_ball
def test_move_one_ball():
    assert module_0.move_one_ball([]) is True
    assert module_0.move_one_ball([1]) is True
    assert module_0.move_one_ball([1, 2, 3, 4]) is True
    assert module_0.move_one_ball([3, 4, 1, 2]) is True
    assert module_0.move_one_ball([4, 1, 2, 3]) is True

    assert module_0.move_one_ball([1, 3, 2]) is False
    assert module_0.move_one_ball([2, 1, 3]) is False
    assert module_0.move_one_ball([4, 2, 3, 1]) is False
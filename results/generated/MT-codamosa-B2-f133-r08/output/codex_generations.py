

# Generated at 2026-10-25 00:19:54.207412
# Unit test for function sum_squares
def test_sum_squares():
    # integers stay the same: 1**2 + 2**2 + 3**2 = 14
    assert module_0.sum_squares([1, 2, 3]) == 14

    # floats are ceiled first: ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0
    # 2**2 + 5**2 + 0**2 = 4 + 25 + 0 = 29
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29

    # negatives: ceil(-2.4)=-2, ceil(-1.0)=-1, ceil(2.1)=3
    # 4 + 1 + 9 = 14
    assert module_0.sum_squares([-2.4, -1.0, 2.1]) == 14

    # empty list
    assert module_0.sum_squares([]) == 0

    # whole-number floats
    assert module_0.sum_squares([1.0, 2.0]) == 5

# Generated at 2026-10-25 00:19:55.567059
# Unit test for function sum_squares
def test_sum_squares():
    # integers stay the same: 1**2 + 2**2 + 3**2 = 14
    assert module_0.sum_squares([1, 2, 3]) == 14

    # floats are ceiled first: ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0
    # 2**2 + 5**2 + 0**2 = 4 + 25 + 0 = 29
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29

    # negatives: ceil(-2.4)=-2, ceil(-1.0)=-1, ceil(2.1)=3
    # 4 + 1 + 9 = 14
    assert module_0.sum_squares([-2.4, -1.0, 2.1]) == 14

    # empty list
    assert module_0.sum_squares([]) == 0

    # whole-number floats
    assert module_0.sum_squares([1.0, 2.0]) == 5

# Generated at 2026-10-25 00:19:56.971639
# Unit test for function sum_squares
def test_sum_squares():
    # integers stay the same: 1**2 + 2**2 + 3**2 = 14
    assert module_0.sum_squares([1, 2, 3]) == 14

    # floats are ceiled first: ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0
    # 2**2 + 5**2 + 0**2 = 4 + 25 + 0 = 29
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29

    # negatives: ceil(-2.4)=-2, ceil(-1.0)=-1, ceil(2.1)=3
    # 4 + 1 + 9 = 14
    assert module_0.sum_squares([-2.4, -1.0, 2.1]) == 14

    # empty list
    assert module_0.sum_squares([]) == 0

    # whole-number floats
    assert module_0.sum_squares([1.0, 2.0]) == 5

# Generated at 2026-10-25 00:19:58.326135
# Unit test for function sum_squares
def test_sum_squares():
    # integers stay the same: 1**2 + 2**2 + 3**2 = 14
    assert module_0.sum_squares([1, 2, 3]) == 14

    # floats are ceiled first: ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0
    # 2**2 + 5**2 + 0**2 = 4 + 25 + 0 = 29
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29

    # negatives: ceil(-2.4)=-2, ceil(-1.0)=-1, ceil(2.1)=3
    # 4 + 1 + 9 = 14
    assert module_0.sum_squares([-2.4, -1.0, 2.1]) == 14

    # empty list
    assert module_0.sum_squares([]) == 0

    # whole-number floats
    assert module_0.sum_squares([1.0, 2.0]) == 5

# Generated at 2026-10-25 00:19:59.736160
# Unit test for function sum_squares
def test_sum_squares():
    # integers stay the same: 1**2 + 2**2 + 3**2 = 14
    assert module_0.sum_squares([1, 2, 3]) == 14

    # floats are ceiled first: ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0
    # 2**2 + 5**2 + 0**2 = 4 + 25 + 0 = 29
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29

    # negatives: ceil(-2.4)=-2, ceil(-1.0)=-1, ceil(2.1)=3
    # 4 + 1 + 9 = 14
    assert module_0.sum_squares([-2.4, -1.0, 2.1]) == 14

    # empty list
    assert module_0.sum_squares([]) == 0

    # whole-number floats
    assert module_0.sum_squares([1.0, 2.0]) == 5


# Generated at 2026-10-24 14:46:13.551126
# Unit test for function sum_squares

# Generated at 2026-10-24 14:46:15.964387
# Unit test for function sum_squares

# Generated at 2026-10-24 14:46:17.360212
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:46:43.619746
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

# Generated at 2026-10-24 14:46:52.983731
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.8, 3.0]) == 29  # 4 + 9 + 16
    assert module_0.sum_squares([-1.2, -2.8]) == 5        # (-1)^2 + (-2)^2
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:47:02.362505
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.1, 2.5, -1.2]) == 14
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:47:04.807638
# Unit test for function sum_squares

# Generated at 2026-10-24 14:47:07.189486
# Unit test for function sum_squares

# Generated at 2026-10-24 14:47:09.697511
# Unit test for function sum_squares


# Generated at 2026-10-24 12:54:27.823856
# Unit test for function any_int
def test_any_int():
    # True: one number equals sum of other two
    assert module_0.any_int(5, 2, 7) == True  # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True  # different order
    assert module_0.any_int(2, 5, 7) == True
    assert module_0.any_int(3, 2, 1) == True  # 2 + 1 == 3
    assert module_0.any_int(0, 0, 0) == True  # 0 + 0 == 0
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-1, -2, -3) == True  # -1 + -2 == -3

    # False: integers but no number is sum of other two
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 1, 2) == False
    assert module_0.any_int(10, 5, 4) == False

    # False: not all inputs are ints
    assert module_0.any_int(3.6, -2.2, 1.4) == False
    assert module_0.any_int(5.0, 2, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([5], 2, 7) == False

# Generated at 2026-10-24 12:54:29.252572
# Unit test for function any_int
def test_any_int():
    # True: one number equals sum of other two
    assert module_0.any_int(5, 2, 7) == True  # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True  # different order
    assert module_0.any_int(2, 5, 7) == True
    assert module_0.any_int(3, 2, 1) == True  # 2 + 1 == 3
    assert module_0.any_int(0, 0, 0) == True  # 0 + 0 == 0
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-1, -2, -3) == True  # -1 + -2 == -3

    # False: integers but no number is sum of other two
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 1, 2) == False
    assert module_0.any_int(10, 5, 4) == False

    # False: not all inputs are ints
    assert module_0.any_int(3.6, -2.2, 1.4) == False
    assert module_0.any_int(5.0, 2, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([5], 2, 7) == False

# Generated at 2026-10-24 12:54:30.693634
# Unit test for function any_int
def test_any_int():
    # True: one number equals sum of other two
    assert module_0.any_int(5, 2, 7) == True  # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True  # different order
    assert module_0.any_int(2, 5, 7) == True
    assert module_0.any_int(3, 2, 1) == True  # 2 + 1 == 3
    assert module_0.any_int(0, 0, 0) == True  # 0 + 0 == 0
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-1, -2, -3) == True  # -1 + -2 == -3

    # False: integers but no number is sum of other two
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 1, 2) == False
    assert module_0.any_int(10, 5, 4) == False

    # False: not all inputs are ints
    assert module_0.any_int(3.6, -2.2, 1.4) == False
    assert module_0.any_int(5.0, 2, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([5], 2, 7) == False

# Generated at 2026-10-24 12:54:32.124755
# Unit test for function any_int
def test_any_int():
    # True: one number equals sum of other two
    assert module_0.any_int(5, 2, 7) == True  # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True  # different order
    assert module_0.any_int(2, 5, 7) == True
    assert module_0.any_int(3, 2, 1) == True  # 2 + 1 == 3
    assert module_0.any_int(0, 0, 0) == True  # 0 + 0 == 0
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-1, -2, -3) == True  # -1 + -2 == -3

    # False: integers but no number is sum of other two
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 1, 2) == False
    assert module_0.any_int(10, 5, 4) == False

    # False: not all inputs are ints
    assert module_0.any_int(3.6, -2.2, 1.4) == False
    assert module_0.any_int(5.0, 2, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([5], 2, 7) == False

# Generated at 2026-10-24 12:54:33.555998
# Unit test for function any_int
def test_any_int():
    # True: one number equals sum of other two
    assert module_0.any_int(5, 2, 7) == True  # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True  # different order
    assert module_0.any_int(2, 5, 7) == True
    assert module_0.any_int(3, 2, 1) == True  # 2 + 1 == 3
    assert module_0.any_int(0, 0, 0) == True  # 0 + 0 == 0
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-1, -2, -3) == True  # -1 + -2 == -3

    # False: integers but no number is sum of other two
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 1, 2) == False
    assert module_0.any_int(10, 5, 4) == False

    # False: not all inputs are ints
    assert module_0.any_int(3.6, -2.2, 1.4) == False
    assert module_0.any_int(5.0, 2, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([5], 2, 7) == False
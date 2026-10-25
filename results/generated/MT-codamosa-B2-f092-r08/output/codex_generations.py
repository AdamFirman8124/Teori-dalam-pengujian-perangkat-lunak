

# Generated at 2026-10-24 13:23:57.138697
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

# Generated at 2026-10-24 13:23:58.536502
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

# Generated at 2026-10-24 13:23:59.962233
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

# Generated at 2026-10-24 13:24:01.395203
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

# Generated at 2026-10-24 13:24:02.829936
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

# Generated at 2026-10-24 13:24:05.353120
# Unit test for function any_int

# Generated at 2026-10-24 13:24:07.933176
# Unit test for function any_int

# Generated at 2026-10-24 13:24:10.349206
# Unit test for function any_int

# Generated at 2026-10-24 13:24:12.973586
# Unit test for function any_int

# Generated at 2026-10-24 13:24:15.613674
# Unit test for function any_int

# Generated at 2026-10-24 13:24:18.403305
# Unit test for function any_int

# Generated at 2026-10-24 13:24:21.043090
# Unit test for function any_int

# Generated at 2026-10-24 13:24:53.701749
# Unit test for function any_int
def test_any_int():assert module_0.any_int(5, 2, 7) == True

# Generated at 2026-10-24 13:24:55.150689
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

# Generated at 2026-10-24 13:24:56.590378
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

# Generated at 2026-10-24 13:24:58.061176
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

# Generated at 2026-10-24 13:24:59.457107
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

# Generated at 2026-10-24 13:25:00.805454
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

# Generated at 2026-10-24 13:25:02.323739
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

# Generated at 2026-10-24 13:25:04.844006
# Unit test for function any_int

# Generated at 2026-10-24 13:25:07.262128
# Unit test for function any_int

# Generated at 2026-10-24 13:25:09.803253
# Unit test for function any_int
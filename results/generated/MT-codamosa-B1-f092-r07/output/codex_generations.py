

# Generated at 2026-10-25 11:52:41.921127
# Unit test for function any_int

# Generated at 2026-10-25 11:52:44.333975
# Unit test for function any_int

# Generated at 2026-10-25 11:52:46.748139
# Unit test for function any_int

# Generated at 2026-10-25 11:52:49.161820
# Unit test for function any_int

# Generated at 2026-10-25 11:52:51.576139
# Unit test for function any_int

# Generated at 2026-10-25 11:52:53.990173
# Unit test for function any_int

# Generated at 2026-10-25 11:52:56.404213
# Unit test for function any_int

# Generated at 2026-10-25 11:52:58.816444
# Unit test for function any_int

# Generated at 2026-10-25 11:53:01.229811
# Unit test for function any_int

# Generated at 2026-10-25 11:53:03.644437
# Unit test for function any_int

# Generated at 2026-10-25 11:53:06.101705
# Unit test for function any_int

# Generated at 2026-10-25 11:53:08.497687
# Unit test for function any_int

# Generated at 2026-10-25 11:53:10.911890
# Unit test for function any_int

# Generated at 2026-10-25 11:53:13.327302
# Unit test for function any_int

# Generated at 2026-10-25 11:53:15.739912
# Unit test for function any_int

# Generated at 2026-10-25 11:53:18.154155
# Unit test for function any_int

# Generated at 2026-10-25 11:53:20.609553
# Unit test for function any_int

# Generated at 2026-10-25 11:53:23.258382
# Unit test for function any_int
def test_any_int():assert module_0.any_int(5, 2, 7) is True      # 5 + 2 == 7

# Generated at 2026-10-25 11:53:31.348034
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:32.855609
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:34.217107
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:35.552464
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:36.961317
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:38.341271
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:39.802271
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:41.354691
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:42.701049
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:44.442398
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:45.822709
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:47.263121
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False   # no combination sums
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(-3, -2, -5) == True # -3 + (-2) == -5
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Non-integer inputs must return False even if sums match
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int("3", 3, 6) == False
    assert module_0.any_int(None, 1, 1) == False
    assert module_0.any_int(True, 1, 2) == False  # bool is technically int subclass

    print("All tests passed!")

test_any_int()

# Generated at 2026-10-25 11:53:50.017891
# Unit test for function any_int

# Generated at 2026-10-25 11:53:52.433350
# Unit test for function any_int

# Generated at 2026-10-25 11:53:55.070245
# Unit test for function any_int

# Generated at 2026-10-25 11:53:57.486713
# Unit test for function any_int

# Generated at 2026-10-25 11:53:59.905041
# Unit test for function any_int

# Generated at 2026-10-25 11:54:02.316401
# Unit test for function any_int

# Generated at 2026-10-25 11:54:04.736665
# Unit test for function any_int

# Generated at 2026-10-25 11:54:07.152073
# Unit test for function any_int

# Generated at 2026-10-25 11:54:09.567094
# Unit test for function any_int

# Generated at 2026-10-25 11:54:11.983878
# Unit test for function any_int

# Generated at 2026-10-25 11:54:15.658888
# Unit test for function any_int

# Generated at 2026-10-25 11:54:18.070293
# Unit test for function any_int

# Generated at 2026-10-25 11:54:20.484399
# Unit test for function any_int

# Generated at 2026-10-25 11:54:22.962850
# Unit test for function any_int

# Generated at 2026-10-25 11:54:25.377712
# Unit test for function any_int

# Generated at 2026-10-25 11:54:27.794855
# Unit test for function any_int

# Generated at 2026-10-25 11:54:30.209293
# Unit test for function any_int

# Generated at 2026-10-25 11:54:32.624405
# Unit test for function any_int

# Generated at 2026-10-25 11:54:35.038646
# Unit test for function any_int

# Generated at 2026-10-25 11:54:37.451280
# Unit test for function any_int

# Generated at 2026-10-25 11:54:39.871896
# Unit test for function any_int
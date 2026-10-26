

# Generated at 2026-10-25 12:42:51.107825
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(1, 1, 2) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(0, 0, 0) is True
    assert module_0.any_int(-1, 1, 0) is True
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int("1", 2, 3) is False
    assert module_0.any_int(None, 2, 3) is False
    print("all tests passed")


test_any_int()

# Generated at 2026-10-25 12:42:53.153958
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

# Generated at 2026-10-25 12:42:54.587013
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

# Generated at 2026-10-25 12:42:56.021414
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

# Generated at 2026-10-25 12:42:57.521088
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

# Generated at 2026-10-25 12:42:58.890051
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

# Generated at 2026-10-25 12:43:00.334278
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

# Generated at 2026-10-25 12:43:03.211870
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

# Generated at 2026-10-25 12:43:04.830798
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

# Generated at 2026-10-25 12:43:12.715355
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

# Generated at 2026-10-25 12:43:14.251570
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

# Generated at 2026-10-25 12:43:16.092752
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

# Generated at 2026-10-25 12:43:18.510213
# Unit test for function any_int

# Generated at 2026-10-25 12:43:20.923968
# Unit test for function any_int

# Generated at 2026-10-25 12:43:23.727004
# Unit test for function any_int

# Generated at 2026-10-25 12:43:26.140911
# Unit test for function any_int

# Generated at 2026-10-25 12:43:28.896933
# Unit test for function any_int

# Generated at 2026-10-25 12:43:31.313755
# Unit test for function any_int

# Generated at 2026-10-25 12:43:33.726811
# Unit test for function any_int

# Generated at 2026-10-25 12:43:36.139188
# Unit test for function any_int

# Generated at 2026-10-25 12:43:38.553690
# Unit test for function any_int

# Generated at 2026-10-25 12:43:40.968540
# Unit test for function any_int

# Generated at 2026-10-25 12:43:43.384661
# Unit test for function any_int

# Generated at 2026-10-25 12:43:46.047638
# Unit test for function any_int
def test_any_int():assert module_0.any_int(5, 2, 7) is True      # 5 + 2 == 7

# Generated at 2026-10-25 12:43:47.429101
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

# Generated at 2026-10-25 12:43:48.804766
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

# Generated at 2026-10-25 12:44:03.610241
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

# Generated at 2026-10-25 12:44:05.245937
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

# Generated at 2026-10-25 12:44:06.681558
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

# Generated at 2026-10-25 12:44:08.113544
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

# Generated at 2026-10-25 12:44:09.685896
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

# Generated at 2026-10-25 12:44:12.082432
# Unit test for function any_int

# Generated at 2026-10-25 12:44:14.496121
# Unit test for function any_int

# Generated at 2026-10-25 12:44:16.910089
# Unit test for function any_int

# Generated at 2026-10-25 12:44:19.585963
# Unit test for function any_int

# Generated at 2026-10-25 12:44:22.005126
# Unit test for function any_int

# Generated at 2026-10-25 12:44:24.420350
# Unit test for function any_int
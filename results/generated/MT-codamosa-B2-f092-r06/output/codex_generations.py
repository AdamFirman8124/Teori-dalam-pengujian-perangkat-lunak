

# Generated at 2026-10-25 06:52:52.291746
# Unit test for function any_int

# Generated at 2026-10-25 06:52:54.704909
# Unit test for function any_int

# Generated at 2026-10-25 06:52:57.122817
# Unit test for function any_int

# Generated at 2026-10-25 06:52:59.539879
# Unit test for function any_int

# Generated at 2026-10-25 06:53:19.876501
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 3, 2) is True
    assert module_0.any_int(1, 1, 2) is True
    assert module_0.any_int(0, 0, 0) is True
    assert module_0.any_int(-1, 1, 0) is True
    assert module_0.any_int(2, 3, 6) is False
    assert module_0.any_int(10, 1, 1) is False
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int(2, 3.0, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(None, 3, 5) is False

# Generated at 2026-10-25 06:53:21.310112
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

# Generated at 2026-10-25 06:53:22.644749
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

# Generated at 2026-10-25 06:53:25.060330
# Unit test for function any_int

# Generated at 2026-10-25 06:53:27.476206
# Unit test for function any_int

# Generated at 2026-10-25 06:53:30.200081
# Unit test for function any_int
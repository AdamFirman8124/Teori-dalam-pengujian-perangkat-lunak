

# Generated at 2026-10-24 11:38:00.907138
# Unit test for function any_int

# Generated at 2026-10-24 11:38:03.325410
# Unit test for function any_int

# Generated at 2026-10-24 11:38:05.745635
# Unit test for function any_int

# Generated at 2026-10-24 11:38:20.492409
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(1, 3, 2) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(5, 3, 2) is True
    assert module_0.any_int(0, 0, 0) is True
    assert module_0.any_int(0, 5, 5) is True
    assert module_0.any_int(5, 0, 5) is True
    assert module_0.any_int(5, 5, 0) is True
    assert module_0.any_int(-1, 1, 0) is True
    assert module_0.any_int(-5, -3, -8) is True
    assert module_0.any_int(-8, -5, -3) is True
    assert module_0.any_int(10, -3, 7) is True
    assert module_0.any_int(1000000, 2000000, 3000000) is True
    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(1, 1, 1) is False
    assert module_0.any_int(2, 2, 3) is False
    assert module_0.any_int(0, 0, 1) is False
    assert module_0.any_int(0, 1, 2) is False
    assert module_0.any_int(-1, -1, 0) is False
    assert module_0.any_int(5, 5, 9) is False
    assert module_0.any_int(10, 5, 4) is False
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int(1, 2.0, 3) is False
    assert module_0.any_int(1, 2, 3.0) is False
    assert module_0.any_int(1.5, 1.5, 3) is False
    assert module_0.any_int("1", 2, 3) is False
    assert module_0.any_int(1, "2", 3) is False
    assert module_0.any_int(1, 2, "3") is False
    assert module_0.any_int(None, 2, 3) is False
    assert module_0.any_int(1, None, 3) is False
    assert module_0.any_int(1, 2, None) is False
    assert module_0.any_int([1], 2, 3) is False
    assert module_0.any_int(1, [2], 3) is False
    assert module_0.any_int(1, 2, [3]) is False

# Generated at 2026-10-24 11:38:26.983745
# Unit test for function any_int
def test_any_int():
    # True cases: one number is the sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 = 7
    assert module_0.any_int(3, 1, 2) == True    # 1 + 2 = 3
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 = 0
    assert module_0.any_int(-1, 1, 0) == True   # works with negatives: -1 + 1 = 0
    assert module_0.any_int(10, -5, 5) == True  # 10 + (-5) = 5

    # False cases: no number is the sum of the other two
    assert module_0.any_int(3, 4, 5) == False
    assert module_0.any_int(1, 2, 4) == False

    # False cases: non-integer inputs
    assert module_0.any_int(3.5, 2, 5) == False    # float
    assert module_0.any_int(3, 2.5, 5) == False    # float
    assert module_0.any_int("3", 2, 5) == False    # string
    assert module_0.any_int(True, 2, 3) == False   # bool is not a valid int here

    print("All tests passed!")


test_any_int()

# Generated at 2026-10-24 11:38:28.448492
# Unit test for function any_int
def test_any_int():
    # True cases: one number is the sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 = 7
    assert module_0.any_int(3, 1, 2) == True    # 1 + 2 = 3
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 = 0
    assert module_0.any_int(-1, 1, 0) == True   # works with negatives: -1 + 1 = 0
    assert module_0.any_int(10, -5, 5) == True  # 10 + (-5) = 5

    # False cases: no number is the sum of the other two
    assert module_0.any_int(3, 4, 5) == False
    assert module_0.any_int(1, 2, 4) == False

    # False cases: non-integer inputs
    assert module_0.any_int(3.5, 2, 5) == False    # float
    assert module_0.any_int(3, 2.5, 5) == False    # float
    assert module_0.any_int("3", 2, 5) == False    # string
    assert module_0.any_int(True, 2, 3) == False   # bool is not a valid int here

    print("All tests passed!")


test_any_int()

# Generated at 2026-10-24 11:38:29.870674
# Unit test for function any_int
def test_any_int():
    # True cases: one number is the sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 = 7
    assert module_0.any_int(3, 1, 2) == True    # 1 + 2 = 3
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 = 0
    assert module_0.any_int(-1, 1, 0) == True   # works with negatives: -1 + 1 = 0
    assert module_0.any_int(10, -5, 5) == True  # 10 + (-5) = 5

    # False cases: no number is the sum of the other two
    assert module_0.any_int(3, 4, 5) == False
    assert module_0.any_int(1, 2, 4) == False

    # False cases: non-integer inputs
    assert module_0.any_int(3.5, 2, 5) == False    # float
    assert module_0.any_int(3, 2.5, 5) == False    # float
    assert module_0.any_int("3", 2, 5) == False    # string
    assert module_0.any_int(True, 2, 3) == False   # bool is not a valid int here

    print("All tests passed!")


test_any_int()
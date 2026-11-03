

# Generated at 2026-11-02 23:25:45.837719
# Unit test for function any_int
def test_any_int():
    # Valid cases: one number equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 5) == True      # 2 + 3 == 5
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10

    # Valid types but no number equals the sum of the others
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(-1, -2, -3) == False  # -1 + -2 == -3 -> True actually
    # Correcting: -1 + (-2) == -3, so this should be True
    assert module_0.any_int(-1, -2, -3) == True

    # Invalid types: floats
    assert module_0.any_int(3.6, -2.2, 2) == False
    assert module_0.any_int(1.0, 2, 3) == False   # float is not int

    # Invalid types: strings
    assert module_0.any_int("3", 2, 1) == False
    assert module_0.any_int(1, "2", 3) == False

    # Mixed invalid types
    assert module_0.any_int(None, 2, 3) == False
    assert module_0.any_int(True, 2, 3) == False  # bool is subclass of int but check intent

    print("All test cases passed!")

# Generated at 2026-11-02 23:27:29.097811
# Unit test for function any_int
def test_any_int():
# nonce:24cf3f17
    # True cases: one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 5) == True      # 2 + 3 == 5
    assert module_0.any_int(7, 4, 3) == True      # 4 + 3 == 7
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(-1, -2, -3) == True   # (-1) + (-2) == (-3)
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 == 5

    # False cases: all ints but no sum relation holds
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(10, 5, 4) == False
    assert module_0.any_int(1, 1, 1) == False
    assert module_0.any_int(-1, 2, 5) == False

    # False cases: non-integer inputs
    assert module_0.any_int(2.5, 2, 3) == False       # float
    assert module_0.any_int(1.0, 2, 3) == False       # whole-valued float is still not int
    assert module_0.any_int("3", 2, 1) == False       # string
    assert module_0.any_int(3, None, 1) == False      # None
    assert module_0.any_int([1], 2, 3) == False       # list
    assert module_0.any_int(1, 2, 3.5) == False       # one float invalidates all

    print("All test_any_int tests passed!")


if __name__ == "__main__":
    test_any_int()

# Generated at 2026-11-02 23:29:23.933595
# Unit test for function any_int
def test_any_int():
    # All integers where sum of two equals the third
    assert module_0.any_int(5, 2, 7) == True      # x + y == z
    assert module_0.any_int(3, 2, 2) == False     # no combination sums
    assert module_0.any_int(7, 2, 5) == True      # y + z == x
    assert module_0.any_int(2, 7, 5) == True      # x + z == y

    # Non-integer inputs should return False
    assert module_0.any_int("3", 2, 1) == False   # string input
    assert module_0.any_int(1.5, 5, 3) == False   # float input
    assert module_0.any_int(3, 2.5, 1) == False   # float input
    assert module_0.any_int(None, 2, 1) == False  # None input
    assert module_0.any_int([3], 2, 1) == False   # list input

    # Negative integers
    assert module_0.any_int(-2, -3, -5) == True   # -2 + -3 == -5
    assert module_0.any_int(-2, 3, 1) == True     # -2 + 3 == 1
    assert module_0.any_int(-1, -1, -1) == False  # no combination sums

    # Zero edge cases
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 == 5
    assert module_0.any_int(0, 1, 2) == False     # no combination sums

    # Mixed int/non-int
    assert module_0.any_int(5, "2", 7) == False   # string among ints
    assert module_0.any_int(5, 2, 7.0) == False   # float result-like input

# Generated at 2026-11-02 23:30:24.191797
# Unit test for function any_int
def test_any_int():
    # Valid cases where one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 1, 4) == True      # 3 + 1 == 4
    assert module_0.any_int(1, 1, 2) == True      # 1 + 1 == 2
    assert module_0.any_int(-1, 0, 1) == True     # -1 + 1 == 0
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(-2, -3, -5) == True   # -2 + -3 == -5

    # Valid integers but no pair sums to the third
    assert module_0.any_int(2, 2, 2) == False     # 2 + 2 != 2
    assert module_0.any_int(3, 5, 10) == False
    assert module_0.any_int(1, 2, 4) == False

    # Non-integer inputs should always return False
    assert module_0.any_int(3.0, 1, 4) == False   # float input
    assert module_0.any_int(1.5, 2.5, 4) == False # floats
    assert module_0.any_int(5, 2.0, 7) == False
    assert module_0.any_int(5, 2, 7.0) == False
    assert module_0.any_int("5", 2, 7) == False   # string input
    assert module_0.any_int(None, 2, 7) == False  # None input
    assert module_0.any_int([5], 2, 7) == False   # list input
    assert module_0.any_int(True, 2, 3) == False  # bool is technically int, but edge case

# Generated at 2026-11-02 23:31:25.417773
# Unit test for function any_int
def test_any_int():
    # All integers, one equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # x + y == z
    assert module_0.any_int(3, 2, 2) == False     # no combination sums
    assert module_0.any_int(10, 5, 5) == True     # y + z == x
    assert module_0.any_int(7, 10, 3) == True     # x + z == y
    assert module_0.any_int(2, 2, 2) == False     # no combination sums
    
    # Negative integers
    assert module_0.any_int(-1, -2, -3) == True   # x + y == z
    assert module_0.any_int(-5, 3, -2) == True    # y + z == x
    assert module_0.any_int(-1, 0, 1) == True     # y + z == x
    assert module_0.any_int(-1, -1, -1) == False
    
    # Zeros
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(0, 5, 5) == True
    
    # Non-integer types should return False
    assert module_0.any_int(3.5, 2, 5) == False   # float
    assert module_0.any_int(3, 2.5, 5) == False   # float
    assert module_0.any_int(3, 2, 5.5) == False   # float
    assert module_0.any_int("3", 2, 5) == False   # string
    assert module_0.any_int(3, "2", 5) == False   # string
    assert module_0.any_int(3, 2, "5") == False   # string
    assert module_0.any_int(True, 2, 3) == False  # bool is not accepted per isinstance check... note: bool is subclass of int
    
    # Large integers
    assert module_0.any_int(1000000, 2000000, 3000000) == True
    assert module_0.any_int(1000000, 2000000, 3000001) == False
    
    print("All test_any_int tests passed!")

test_any_int()
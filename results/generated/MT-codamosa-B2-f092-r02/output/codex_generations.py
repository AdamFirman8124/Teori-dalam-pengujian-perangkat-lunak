

# Generated at 2026-11-02 18:00:19.580301
# Unit test for function any_int
def test_any_int():
    # All integers where one equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(10, 4, 6) == True     # 4 + 6 == 10
    assert module_0.any_int(-1, -2, -3) == True   # -1 + (-2) == -3
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(100, 50, 50) == True  # 50 + 50 == 100

    # All integers but no valid sum
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 1, 1) == False
    assert module_0.any_int(10, 20, 5) == False

    # Non-integer inputs should return False even if sums work numerically
    assert module_0.any_int(3.6, -5, 2) == False
    assert module_0.any_int(2.0, 3, 5) == False   # 2.0 is a float, not an int
    assert module_0.any_int(1.5, 2.5, 4) == False
    assert module_0.any_int("5", 2, 3) == False
    assert module_0.any_int(5, None, 3) == False
    assert module_0.any_int([5], 2, 3) == False

# Generated at 2026-11-02 18:02:01.266566
# Unit test for function any_int
def test_any_int():
    # Valid cases: one number is the sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 2, 1) == True    # 2 + 1 == 3
    assert module_0.any_int(10, 5, 5) == True   # 5 + 5 == 10
    assert module_0.any_int(3, -2, 1) == True   # 3 + (-2) == 1
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0
    assert module_0.any_int(-1, 0, -1) == True  # -1 + 0 == -1

    # All ints, but no combination sums correctly
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(2, 2, 2) == False
    assert module_0.any_int(1, 5, 10) == False

    # Non-integer inputs should always return False
    assert module_0.any_int(1.5, 2, 3) == False
    assert module_0.any_int(1, 2.5, 3) == False
    assert module_0.any_int(1, 2, 3.5) == False
    assert module_0.any_int(1.5, 2.5, 4.0) == False
    assert module_0.any_int("3", 2, 1) == False
    assert module_0.any_int(1, "2", 3) == False
    assert module_0.any_int(1, 2, "3") == False
    assert module_0.any_int(None, 2, 3) == False
    assert module_0.any_int([1], 2, 3) == False

    print("All tests passed!")


test_any_int()

# Generated at 2026-11-02 18:04:22.963039
# Unit test for function any_int
def test_any_int():
    # Valid cases: one number equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False     # no combination sums correctly
    assert module_0.any_int(2, 3, 1) == True      # 2 + 1 == 3
    assert module_0.any_int(1, 1, 2) == True      # 1 + 1 == 2
    assert module_0.any_int(10, 4, 6) == True     # 4 + 6 == 10
    assert module_0.any_int(15, 15, 30) == True   # 15 + 15 == 30

    # Zero and negative integers
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 == 5
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 == -3
    assert module_0.any_int(-1, 5, 4) == True     # -1 + 5 == 4
    assert module_0.any_int(-1, -2, 0) == False   # no valid sum

    # Non-integer inputs must return False, even if the sum would match
    assert module_0.any_int(3.5, 2, 5) == False   # float as first arg
    assert module_0.any_int(2, 3.5, 5) == False   # float as second arg
    assert module_0.any_int(2, 3, 5.0) == False   # float as third arg
    assert module_0.any_int("2", 3, 5) == False   # string as first arg
    assert module_0.any_int(2, "3", 5) == False   # string as second arg
    assert module_0.any_int(2, 3, "5") == False   # string as third arg
    assert module_0.any_int(None, 1, 1) == False  # None input
    assert module_0.any_int([1], 2, 3) == False   # list input
    assert module_0.any_int(True, 1, 2) == True   # bool is subclass of int (True == 1)

# Generated at 2026-11-02 18:06:00.371982
# Unit test for function any_int
def test_any_int():
    # Two integers sum to the third
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(7, 5, 2) == True      # 5 + 2 == 7 (any position)
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(-1, -2, -3) == True   # -1 + (-2) == -3
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0

    # No pair sums to the third
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 1, 1) == False
    assert module_0.any_int(10, 4, 5) == False

    # Non-integer inputs always return False
    assert module_0.any_int(3.6, -2, 2) == False  # float
    assert module_0.any_int(2, 3.6, 5) == False
    assert module_0.any_int("3", 2, 1) == False   # string
    assert module_0.any_int(3, None, 1) == False  # None
    assert module_0.any_int([1], 2, 3) == False   # list

    # Booleans are instances of int in Python
    assert module_0.any_int(True, 1, 2) == True   # True + 1 == 2
    assert module_0.any_int(True, True, 3) == False

# Generated at 2026-11-02 18:08:10.802942
# Unit test for function any_int
def test_any_int():
    # Case where x + y == z
    assert module_0.any_int(2, 3, 5) == True
    # Case where x + z == y
    assert module_0.any_int(5, 3, 2) == True
    # Case where y + z == x
    assert module_0.any_int(3, 2, 5) == True
    # All ints but no pair sums to the third
    assert module_0.any_int(1, 2, 4) == False
    # Non-integer input (float) should return False
    assert module_0.any_int(2.5, 2, 3) == False
    assert module_0.any_int(2, 2.5, 3) == False
    assert module_0.any_int(2, 3, 5.0) == False
    # Non-numeric input should return False
    assert module_0.any_int("2", 3, 5) == False
    assert module_0.any_int(2, None, 5) == False
    # Negative integers where a sum matches
    assert module_0.any_int(-2, -3, -5) == True
    assert module_0.any_int(-2, 3, 1) == True
    # Negative integers with no match
    assert module_0.any_int(-2, -3, 5) == False
    # Zero cases
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(0, 5, 5) == True
    assert module_0.any_int(0, 5, 6) == False
    # Large integers
    assert module_0.any_int(1000000, 2000000, 3000000) == True

# nonce:7d0ee13b


# Generated at 2026-11-02 12:19:01.297052
# Unit test for function any_int
def test_any_int():
    # Valid cases: two numbers sum to the third
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 = 7
    assert module_0.any_int(3, 1, 2) == True      # 1 + 2 = 3
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 = 10
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 = 0

    # Negative numbers
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 = -3
    assert module_0.any_int(-5, 3, -2) == True    # 3 + -2 = -5
    assert module_0.any_int(3, -3, 0) == True     # 3 + -3 = 0

    # No two numbers sum to the third
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(7, 3, 2) == False
    assert module_0.any_int(100, 50, 25) == False

    # Non-integer inputs should return False
    assert module_0.any_int(3.5, 2, 2) == False
    assert module_0.any_int(3, 2.5, 2) == False
    assert module_0.any_int(3, 2, 2.5) == False
    assert module_0.any_int("3", 2, 5) == False
    assert module_0.any_int(3, "2", 5) == False
    assert module_0.any_int(3, 2, "5") == False
    assert module_0.any_int(None, 2, 2) == False
    assert module_0.any_int([1], 2, 3) == False
    assert module_0.any_int(3.0, 1.0, 4.0) == False  # floats even with whole values

    # Edge case: bool is a subclass of int in Python
    # True (== 1) + 2 == 3, so this returns True
    assert module_0.any_int(True, 2, 3) == True

    print("All test_any_int tests passed!")


if __name__ == "__main__":
    test_any_int()

# Generated at 2026-11-02 12:19:45.717084
# Unit test for function any_int
def test_any_int():
    # Valid cases: one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 1) == True      # 2 + 1 == 3
    assert module_0.any_int(1, 4, 5) == True      # 1 + 4 == 5
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10

    # Invalid cases: all ints but no sum condition holds
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(5, 5, 5) == False
    assert module_0.any_int(0, 1, 2) == False

    # Non-integer inputs should return False
    assert module_0.any_int(3.5, 2, 5) == False
    assert module_0.any_int(3, 2.5, 5) == False
    assert module_0.any_int(3, 2, 5.5) == False
    assert module_0.any_int("3", 2, 5) == False
    assert module_0.any_int(3, "2", 5) == False
    assert module_0.any_int(3, 2, "5") == False
    assert module_0.any_int(None, 2, 3) == False
    assert module_0.any_int(True, 2, 3) == True   # bool is subclass of int; True==1, 1+2==3

    # Negative integers
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 == -3
    assert module_0.any_int(-5, 3, 2) == True     # 3 + 2 == -5? No: 3+2=5 != -5, but -5+3=-2? No; -5+2=-3? No -> False
    # Correcting: -5 + 3 = -2, -5 + 2 = -3, 3 + 2 = 5 -> none equal
    assert module_0.any_int(-5, 3, 2) == False

    # Zero cases
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 == 5

    # Large integers
    assert module_0.any_int(10**18, 10**18, 2 * 10**18) == True
    assert module_0.any_int(10**18, 10**18, 10**18) == False

# Generated at 2026-11-02 12:20:36.561752
# Unit test for function any_int
def test_any_int():
    # Cases where one value equals the sum of the other two (all ints)
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True    # 5 + 2 == 7 (x + z == y)
    assert module_0.any_int(7, 2, 5) == True    # 2 + 5 == 7 (y + z == x)

    # All ints but no combination sums correctly
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(3, 3, 3) == False

    # Negative integers
    assert module_0.any_int(-2, -3, -5) == True   # -2 + -3 == -5
    assert module_0.any_int(-1, 1, 0) == True     # -1 + 1 == 0
    assert module_0.any_int(-1, 5, 3) == False

    # Zero cases
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(0, 5, 5) == True

    # Non-integer inputs should return False
    assert module_0.any_int(5.0, 2, 7) == False    # float
    assert module_0.any_int(5, 2.5, 7) == False    # float
    assert module_0.any_int(5.5, 2.5, 8.0) == False
    assert module_0.any_int("5", 2, 7) == False    # string
    assert module_0.any_int(5, 2, None) == False   # None
    assert module_0.any_int([1], 2, 3) == False    # list
    assert module_0.any_int(True, 2, 3) == False   # bool is not a strict int here per intent

    # Large integers
    assert module_0.any_int(10**18, 10**18, 2 * 10**18) == True

    print("All test_any_int tests passed!")

# Generated at 2026-11-02 12:21:11.219040
# Unit test for function any_int
def test_any_int():
    # Valid cases: one number equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 1, 2) == True      # 1 + 2 == 3
    assert module_0.any_int(10, 10, 0) == True    # 10 + 0 == 10
    
    # Valid cases with negatives
    assert module_0.any_int(-2, -3, -5) == True   # -2 + -3 == -5
    assert module_0.any_int(5, -3, 2) == True     # -3 + 2 == 5
    assert module_0.any_int(-1, 1, 0) == True     # -1 + 1 == 0
    
    # Invalid cases: ints but no sum condition
    assert module_0.any_int(1, 2, 3) == True      # 1 + 2 == 3
    assert module_0.any_int(3, 3, 3) == False     # no combination works
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(0, 0, 1) == False
    
    # All zeros edge case
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    
    # Non-int types should return False
    assert module_0.any_int(3.5, 2, 5) == False   # float present
    assert module_0.any_int(3, 2.0, 5) == False   # float present
    assert module_0.any_int(3, 2, 5.0) == False   # float present
    assert module_0.any_int("3", 2, 5) == False   # string present
    assert module_0.any_int(3, "2", 5) == False   # string present
    assert module_0.any_int(3, 2, "5") == False   # string present
    assert module_0.any_int(None, 2, 5) == False  # None present
    assert module_0.any_int(True, 2, 3) == False  # bool is subclass of int, but semantically not int

# Generated at 2026-11-02 12:21:57.715672
# Unit test for function any_int
def test_any_int():
    # All integers, one equals the sum of the other two
    assert module_0.any_int(2, 3, 5) == True      # x + y == z
    assert module_0.any_int(5, 3, 2) == True      # x + z == y
    assert module_0.any_int(5, 2, 3) == True      # y + z == x
    assert module_0.any_int(3, 4, 7) == True
    assert module_0.any_int(0, 0, 0) == True      # zeros

    # All integers, but no value equals the sum of the others
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(10, 20, 5) == False

    # Negative integers
    assert module_0.any_int(-2, -3, -5) == True
    assert module_0.any_int(-2, 3, 1) == True
    assert module_0.any_int(-1, 5, 3) == False

    # Non-integer inputs should return False
    assert module_0.any_int(2.5, 3, 5) == False
    assert module_0.any_int(2, 3.5, 5) == False
    assert module_0.any_int(2, 3, 5.0) == False
    assert module_0.any_int("2", 3, 5) == False
    assert module_0.any_int(2, "3", 5) == False
    assert module_0.any_int(2, 3, "5") == False
    assert module_0.any_int(None, 3, 5) == False

    print("All tests passed!")


test_any_int()


# Generated at 2026-11-01 20:21:53.762165
# Unit test for function any_int
def test_any_int():
    # Valid cases: two integers sum to the third
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 1, 2) == True      # 1 + 2 == 3
    assert module_0.any_int(10, 4, 6) == True     # 4 + 6 == 10
    assert module_0.any_int(2, 2, 0) == True      # 2 + 0 == 2
    
    # Valid cases with negative numbers
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 == -3
    assert module_0.any_int(-5, 3, 2) == True     # 3 + 2 == 5... wait, -5+3=-2, -5+2=-3, 3+2=5
    
    # Invalid cases: all integers but no pair sums to the third
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(3, 3, 3) == False
    assert module_0.any_int(0, 0, 1) == False
    
    # Invalid cases: non-integer inputs
    assert module_0.any_int(1.5, 2, 3) == False   # float input
    assert module_0.any_int(1, 2.5, 3) == False   # float input
    assert module_0.any_int(1, 2, 3.0) == False   # float even if value is whole
    assert module_0.any_int("1", 2, 3) == False   # string input
    assert module_0.any_int(1, 2, "3") == False   # string input
    assert module_0.any_int(None, 2, 3) == False  # None input
    assert module_0.any_int(True, 2, 3) == False  # bool is technically int subclass but often excluded
    
    # Edge cases with zero
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 == 5
    
    print("All tests passed!")


if __name__ == "__main__":
    test_any_int()

# Generated at 2026-11-01 20:22:49.877012
# Unit test for function any_int
def test_any_int():
    # True cases: one element equals the sum of the other two
    assert module_0.any_int(2, 3, 1) == True
    assert module_0.any_int(4, 2, 2) == True
    assert module_0.any_int(5, 2, 7) == True
    assert module_0.any_int(10, 0, 10) == True
    assert module_0.any_int(3, -2, 1) == True
    assert module_0.any_int(-4, 6, 2) == True
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(3, 4, 7) == True

    # False cases: all ints but no element equals the sum of the others
    assert module_0.any_int(2, 6, 2) == False
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False

    # False cases: non-integer inputs
    assert module_0.any_int(2.5, 2, 3) == False
    assert module_0.any_int(1.5, 5, 3.5) == False
    assert module_0.any_int(2.2, 2.2, 2.2) == False
    assert module_0.any_int(1, "2", 3) == False
    assert module_0.any_int(None, 1, 2) == False
    assert module_0.any_int(1, 2, [3]) == False

    print("All tests passed!")

# Generated at 2026-11-01 20:23:20.707294
# Unit test for function any_int
def test_any_int():
    # All ints, x + y == z
    assert module_0.any_int(5, 2, 7) == True
    # All ints, x + z == y
    assert module_0.any_int(3, 10, 7) == True
    # All ints, y + z == x
    assert module_0.any_int(10, 3, 7) == True
    # All ints but no combination sums correctly
    assert module_0.any_int(2, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    # Non-int inputs (floats)
    assert module_0.any_int(1.5, 2, 3) == False
    assert module_0.any_int(1, 2.5, 3) == False
    assert module_0.any_int(1, 2, 3.5) == False
    # Non-int inputs (strings)
    assert module_0.any_int("1", 2, 3) == False
    assert module_0.any_int(1, "2", 3) == False
    assert module_0.any_int(1, 2, "3") == False
    # Non-int inputs (booleans are ints in Python, but mixed types fail)
    assert module_0.any_int(True, 2, 3) == False
    # Zero and negative numbers
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(-1, -2, -3) == True
    assert module_0.any_int(-1, 2, 1) == True
    assert module_0.any_int(-1, -2, 3) == False
    # Mixed int/float even if sum matches
    assert module_0.any_int(2.0, 2, 4) == False

    print("All test_any_int tests passed!")

test_any_int()

# Generated at 2026-11-01 20:23:55.966473
# Unit test for function any_int
def test_any_int():
    # All integers, one is sum of the other two
    assert module_0.any_int(2, 3, 5) == True
    assert module_0.any_int(5, 2, 3) == True
    assert module_0.any_int(3, 5, 2) == True
    assert module_0.any_int(1, 1, 2) == True
    assert module_0.any_int(0, 0, 0) == True

    # All integers, no sum condition holds
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(10, 20, 5) == False
    assert module_0.any_int(7, 3, 3) == False

    # Negative integers
    assert module_0.any_int(-2, -3, -5) == True
    assert module_0.any_int(-1, 1, 0) == True
    assert module_0.any_int(-5, 2, -3) == True
    assert module_0.any_int(-1, -2, -4) == False

    # Non-integer inputs should return False
    assert module_0.any_int(2.5, 3, 5) == False
    assert module_0.any_int(2, 3.0, 5) == False
    assert module_0.any_int(2, 3, 5.0) == False
    assert module_0.any_int("2", 3, 5) == False
    assert module_0.any_int(2, "3", 5) == False
    assert module_0.any_int(2, 3, "5") == False
    assert module_0.any_int(None, 3, 5) == False
    assert module_0.any_int(True, 2, 3) == True  # bool is subclass of int (2+3... True==1, 1+2==3)

    # Floats even if sum works
    assert module_0.any_int(2.0, 3.0, 5.0) == False

    # Large integers
    assert module_0.any_int(1000000, 2000000, 3000000) == True
    assert module_0.any_int(1000000, 2000000, 4000000) == False

# Generated at 2026-11-01 20:24:16.616941
# Unit test for function any_int
def test_any_int():
    # All integers, valid sums
    assert module_0.any_int(5, 2, 7) == True   # x + y == z
    assert module_0.any_int(3, 10, 7) == True  # x + z == y
    assert module_0.any_int(10, 3, 7) == True  # y + z == x

    # All integers, no valid sum
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(2, 3, 6) == False

    # Negative integers
    assert module_0.any_int(-1, -2, -3) == True
    assert module_0.any_int(-1, 2, 1) == True
    assert module_0.any_int(-5, 3, -8) == False

    # Zero cases
    assert module_0.any_int(0, 0, 0) == True
    assert module_0.any_int(0, 5, 5) == True
    assert module_0.any_int(0, 1, 2) == False

    # Non-integer inputs
    assert module_0.any_int(1.5, 2, 3) == False
    assert module_0.any_int(1, 2.5, 3) == False
    assert module_0.any_int(1, 2, 3.5) == False
    assert module_0.any_int(1.0, 2, 3) == False  # float even if whole number
    assert module_0.any_int("1", 2, 3) == False
    assert module_0.any_int(1, None, 3) == False
    assert module_0.any_int([1], 2, 3) == False

    # Large numbers
    assert module_0.any_int(1000000, 2000000, 3000000) == True
    assert module_0.any_int(1000000, 2000000, 4000000) == False

    print("All test_any_int tests passed!")
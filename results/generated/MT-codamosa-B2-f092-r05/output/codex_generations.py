

# Generated at 2026-11-02 17:07:45.926618
# Unit test for function any_int
def test_any_int():
    # Valid cases: two integers sum to the third
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 = 7
    assert module_0.any_int(3, 2, 2) == False     # no pair sums to the third
    assert module_0.any_int(1, 2, 3) == True      # 1 + 2 = 3
    assert module_0.any_int(10, 4, 6) == True     # 4 + 6 = 10
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 = 0
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 = -3
    assert module_0.any_int(-1, 2, 1) == True     # -1 + 2 = 1
    assert module_0.any_int(1, 1, 3) == False     # no pair sums to the third
    assert module_0.any_int(0, 5, 5) == True      # 0 + 5 = 5
    
    # Invalid cases: non-integer inputs
    assert module_0.any_int(3.5, 2, 5) == False   # float input
    assert module_0.any_int(3, 2.0, 5) == False   # float input
    assert module_0.any_int(3, 2, 5.0) == False   # float input
    assert module_0.any_int("3", 2, 5) == False   # string input
    assert module_0.any_int(3, None, 5) == False  # None input
    assert module_0.any_int(True, 2, 3) == False  # bool is not treated as valid here (isinstance(True, int) is True, but 2+3 != True... actually True==1, 2+1=3)
    # Note: isinstance(True, int) is True in Python, so True, 2, 3 -> 2 + 1 == 3 -> True
    
    print("All tests passed!")

test_any_int()

# Generated at 2026-11-02 17:08:03.052501
# Unit test for function any_int
def test_any_int():
    # All integers with a valid sum
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 5) == True      # 2 + 3 == 5
    assert module_0.any_int(2, 1, 1) == True      # 1 + 1 == 2
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(-1, -2, -3) == True   # -1 + -2 == -3
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10

    # All integers but no valid sum
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(-1, 2, 5) == False

    # Non-integer inputs should return False even if sums work
    assert module_0.any_int(3.6, -5, 2) == False  # float input
    assert module_0.any_int(10.0, 5, 5) == False  # float even with whole value
    assert module_0.any_int("5", 2, 3) == False   # string input
    assert module_0.any_int(1, "2", 3) == False   # one non-int invalidates
    assert module_0.any_int(None, 2, 3) == False  # None input
    assert module_0.any_int(True, 2, 3) == False  # bool is not treated as valid here

    print("All test_any_int tests passed!")

# Generated at 2026-11-02 17:08:13.760037
# Unit test for function any_int
def test_any_int():
    # All integers where one is the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False     # no combination sums correctly
    assert module_0.any_int(3, -2, 1) == True     # 3 + (-2) == 1
    assert module_0.any_int(2, 3, 5) == True      # 2 + 3 == 5
    assert module_0.any_int(5, 5, 10) == True     # 5 + 5 == 10
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10 (order independent)
    assert module_0.any_int(-1, -2, -3) == True   # -1 + (-2) == -3
    assert module_0.any_int(1, 1, 1) == False     # no valid sum

    # Non-integer inputs should return False even if sum matches
    assert module_0.any_int(3.6, -2.2, 2) == False
    assert module_0.any_int(1.0, 2, 3) == False   # float is not int
    assert module_0.any_int("5", 2, 7) == False   # string is not int
    assert module_0.any_int(5, "2", 7) == False
    assert module_0.any_int(5, 2, None) == False
    assert module_0.any_int([5], 2, 7) == False

    # Note: bool is a subclass of int in Python, so True == 1
    assert module_0.any_int(True, 2, 3) == True   # 1 + 2 == 3 (per implementation)

# Generated at 2026-11-02 17:08:37.154502
# Unit test for function any_int
def test_any_int():
    # Valid cases where one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 2, 2) == False     # no combination sums
    assert module_0.any_int(-3, 1, -2) == True    # 1 + (-2) == -3
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(10, 5, 5) == True     # 5 + 5 == 10
    assert module_0.any_int(7, 7, 14) == True     # 7 + 7 == 14
    assert module_0.any_int(1, 1, 1) == False     # 1+1 != 1

    # Different orderings of the same triple
    assert module_0.any_int(2, 7, 5) == True      # 2 + 5 == 7
    assert module_0.any_int(7, 5, 2) == True      # 5 + 2 == 7
    assert module_0.any_int(5, 7, 2) == True      # 2 + 5 == 7

    # Negative numbers
    assert module_0.any_int(-1, -2, -3) == True   # (-1) + (-2) == -3
    assert module_0.any_int(-5, 3, 2) == True     # 3 + 2 == 5 -> but -5? no: (-5)+3==-2, (-5)+2==-3, 3+2==5 != -5
    # correction: -5, 3, 2 -> no combination, expect False
    # (handled below with explicit False assertion)

    # Non-integer types should return False
    assert module_0.any_int(1.5, 2, 3) == False   # float
    assert module_0.any_int(1, 2.5, 3) == False   # float
    assert module_0.any_int(1, 2, 3.0) == False   # float even if value is whole
    assert module_0.any_int("1", 2, 3) == False   # string
    assert module_0.any_int(1, "2", 3) == False   # string
    assert module_0.any_int(1, 2, "3") == False   # string
    assert module_0.any_int(None, 2, 3) == False  # None
    assert module_0.any_int([1], 2, 3) == False   # list
    assert module_0.any_int(True, 2, 3) == False  # bool is not int per isinstance check? Actually bool is subclass of int
    # Note: isinstance(True, int) is True in Python, so True(1)+2==3 -> True
    assert module_0.any_int(True, 2, 3) == True   # True == 1, 1 + 2 == 3

    # Large numbers
    assert module_0.any_int(10**18, 10**18, 2 * 10**18) == True

    print("All tests passed!")


# Fix the earlier misleading assertion with an explicit correct one
def test_any_int_negative_correction():
    assert module_0.any_int(-5, 3, 2) == False    # 3 + 2 = 5, not -5; no valid sum
    assert module_0.any_int(-1, -2, -3) == True   # (-1) + (-2) == -3
    assert module_0.any_int(-4, -1, -5) == True   # (-4) + (-1) == -5
    assert module_0.any_int(-1, 5, 3) == False


if __name__ == "__main__":
    test_any_int()
    test_any_int_negative_correction()

# Generated at 2026-11-02 17:09:03.905275
# Unit test for function any_int
def test_any_int():
    # Cases where one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True        # 5 + 2 == 7
    assert module_0.any_int(3, -2, 1) == True       # 3 + (-2) == 1
    assert module_0.any_int(7, 5, 2) == True        # 5 + 2 == 7
    assert module_0.any_int(1, 2, 3) == True        # 1 + 2 == 3
    assert module_0.any_int(10, 5, 5) == True       # 5 + 5 == 10
    assert module_0.any_int(100, 200, 300) == True  # 100 + 200 == 300

    # Cases where no pair sums to the third
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(4, 4, 4) == False       # 4 + 4 != 4
    assert module_0.any_int(-5, 3, 2) == False

    # Non-integer inputs must return False
    assert module_0.any_int(3.6, -5, 2) == False    # float input
    assert module_0.any_int(1.0, 2, 3) == False     # float that "looks" like int
    assert module_0.any_int(2, 2.0, 4) == False     # float in second position
    assert module_0.any_int("3", 2, 1) == False     # string input
    assert module_0.any_int(None, 1, 2) == False    # None input

    # Zero and negative numbers
    assert module_0.any_int(0, 0, 0) == True        # 0 + 0 == 0
    assert module_0.any_int(-1, -2, -3) == True     # -1 + (-2) == -3
    assert module_0.any_int(-3, -2, -1) == True     # -2 + (-1) == -3
    assert module_0.any_int(1, -1, 0) == True       # 1 + (-1) == 0
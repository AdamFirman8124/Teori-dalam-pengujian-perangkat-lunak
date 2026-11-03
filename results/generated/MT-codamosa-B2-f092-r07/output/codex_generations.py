

# Generated at 2026-11-02 11:36:41.149837
# Unit test for function any_int
def test_any_int():
    # Cases where one value equals the sum of the other two (all ints)
    assert module_0.any_int(5, 2, 7) == True      # 5 + 2 == 7
    assert module_0.any_int(3, 1, 2) == True      # 1 + 2 == 3
    assert module_0.any_int(7, 10, 3) == True     # 7 + 3 == 10
    assert module_0.any_int(2, 2, 2) == False     # no combination sums
    assert module_0.any_int(-1, 0, 1) == True     # -1 + 1 == 0
    assert module_0.any_int(0, 0, 0) == True      # 0 + 0 == 0
    assert module_0.any_int(-3, -4, -7) == True   # -3 + -4 == -7
    assert module_0.any_int(1, -1, 0) == True     # 1 + -1 == 0

    # Non-integer inputs should return False
    assert module_0.any_int(3.5, 2, 5) == False   # float input
    assert module_0.any_int(3, 2.0, 5) == False   # float input
    assert module_0.any_int(3, 2, 5.0) == False   # float input
    assert module_0.any_int("3", 2, 5) == False   # string input
    assert module_0.any_int(3, "2", 5) == False   # string input
    assert module_0.any_int(None, 2, 5) == False  # None input
    assert module_0.any_int([3], 2, 5) == False   # list input
    assert module_0.any_int(True, 2, 3) == True   # bool is subclass of int (True == 1)
    assert module_0.any_int(True, False, 1) == True  # 1 + 0 == 1

    # Large numbers
    assert module_0.any_int(10**18, 10**18, 2 * 10**18) == True
    assert module_0.any_int(10**18, 10**18, 10**18) == False

    print("All tests passed!")


test_any_int()

# Generated at 2026-11-02 11:40:23.818520
# Unit test for function any_int
def test_any_int():
    # Valid: all ints, one value equals sum of the other two
    assert module_0.any_int(5, 2, 7) == True    # 5 + 2 == 7
    assert module_0.any_int(3, 10, 7) == True   # 3 + 7 == 10
    assert module_0.any_int(10, 3, 7) == True   # 3 + 7 == 10
    assert module_0.any_int(-1, -2, -3) == True # -1 + -2 == -3
    assert module_0.any_int(0, 0, 0) == True    # 0 + 0 == 0

    # Invalid: all ints but no pair sums to the third
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(-1, 2, 5) == False

    # Invalid: non-integer inputs, even if sums would match
    assert module_0.any_int(1.5, 2, 3) == False
    assert module_0.any_int(1, 2, 3.0) == False
    assert module_0.any_int(2.5, 2.5, 5) == False
    assert module_0.any_int("5", 2, 7) == False
    assert module_0.any_int(None, 2, 3) == False

    print("All tests passed!")

test_any_int()

# Generated at 2026-11-02 11:42:47.397588
# Unit test for function any_int
def test_any_int():
    # Valid cases where one value equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True, "5 + 2 == 7 should return True"
    assert module_0.any_int(3, 2, 2) == False, "No pair sums to the third value"
    assert module_0.any_int(10, 5, 5) == True, "5 + 5 == 10 should return True"
    assert module_0.any_int(2, 2, 4) == True, "2 + 2 == 4 should return True"

    # Order permutations should not matter
    assert module_0.any_int(7, 5, 2) == True, "2 + 5 == 7 in different order"
    assert module_0.any_int(2, 7, 5) == True, "2 + 5 == 7 in different order"

    # Negative integers
    assert module_0.any_int(-2, -3, -5) == True, "-2 + -3 == -5 should return True"
    assert module_0.any_int(-1, 1, 0) == True, "-1 + 1 == 0 should return True"
    assert module_0.any_int(-2, 3, 1) == False, "No pair sums to the third value"

    # Zero cases
    assert module_0.any_int(0, 0, 0) == True, "0 + 0 == 0 should return True"
    assert module_0.any_int(0, 1, 1) == True, "0 + 1 == 1 should return True"
    assert module_0.any_int(0, 1, 2) == False, "No pair sums to the third value"

    # Non-integer types should return False
    assert module_0.any_int(1.5, 2, 3) == False, "Float input should return False"
    assert module_0.any_int(1, 2.5, 3) == False, "Float input should return False"
    assert module_0.any_int(1, 2, 3.5) == False, "Float input should return False"
    assert module_0.any_int("1", 2, 3) == False, "String input should return False"
    assert module_0.any_int(1, "2", 3) == False, "String input should return False"
    assert module_0.any_int(1, 2, "3") == False, "String input should return False"
    assert module_0.any_int(None, 2, 3) == False, "None input should return False"
    assert module_0.any_int(True, 2, 3) == False, "Boolean input should return False"

    # Large integers
    assert module_0.any_int(1000000, 2000000, 3000000) == True, "Large int sum should return True"
    assert module_0.any_int(1000000, 2000000, 4000000) == False, "Large int non-sum should return False"

    print("All test_any_int tests passed!")


# Run the tests
if __name__ == "__main__":
    test_any_int()

# Generated at 2026-11-02 11:44:17.482989
# Unit test for function any_int
def test_any_int():
    # Valid: all ints and one equals the sum of the other two
    assert module_0.any_int(5, 2, 7) == True       # 5 + 2 == 7
    assert module_0.any_int(3, 12, 15) == True     # 3 + 12 == 15
    assert module_0.any_int(10, 3, 7) == True      # 3 + 7 == 10
    assert module_0.any_int(0, 0, 0) == True       # 0 + 0 == 0
    assert module_0.any_int(3, -2, 1) == True      # 3 + (-2) == 1
    assert module_0.any_int(-1, -2, -3) == True    # -1 + (-2) == -3
    assert module_0.any_int(7, 7, 14) == True      # 7 + 7 == 14

    # Invalid: all ints, but no combination sums correctly
    assert module_0.any_int(3, 2, 2) == False
    assert module_0.any_int(1, 2, 4) == False
    assert module_0.any_int(100, 1, 2) == False
    assert module_0.any_int(-1, -2, -4) == False

    # Invalid: non-integer inputs should always return False
    assert module_0.any_int(2.5, 2, 3) == False    # float in first position
    assert module_0.any_int(1, 2.5, 3) == False    # float in second position
    assert module_0.any_int(1, 2, 3.0) == False    # float even if sum holds
    assert module_0.any_int("3", 2, 1) == False    # string
    assert module_0.any_int(None, 2, 3) == False   # None
    assert module_0.any_int([1], 2, 3) == False    # list
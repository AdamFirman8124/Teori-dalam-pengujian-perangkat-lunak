

# Generated at 2026-11-02 21:01:06.164028
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases
    assert module_0.is_simple_power(1, 4) == True      # 4^0 = 1
    assert module_0.is_simple_power(2, 2) == True      # 2^1 = 2
    assert module_0.is_simple_power(8, 2) == True      # 2^3 = 8
    assert module_0.is_simple_power(16, 2) == True     # 2^4 = 16
    assert module_0.is_simple_power(4096, 8) == True   # 8^4 = 4096
    assert module_0.is_simple_power(143214132, 97) == True  # 97^4

    # Basic false cases
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(16, 12) == False

    # Edge case: n == 1
    assert module_0.is_simple_power(1, 1) == True      # x must be 1
    assert module_0.is_simple_power(3, 1) == False

    # Edge case: x == 0 (power starts at 1, never equals 0)
    assert module_0.is_simple_power(0, 2) == False

    # Large numbers
    assert module_0.is_simple_power(1024, 4) == True   # 4^5 = 1024
    assert module_0.is_simple_power(1000, 10) == True  # 10^3 = 1000
    assert module_0.is_simple_power(999, 10) == False

    # x equal to n itself
    assert module_0.is_simple_power(7, 7) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_simple_power()

# Generated at 2026-11-02 21:01:39.023254
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a valid power of n
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(125, 5) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(143214, 132) == False

    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(2, 1) == False

# Generated at 2026-11-02 21:02:03.734012
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(125, 5) == True

    # Basic false cases
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(7, 4) == False

    # Edge cases
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(6, 6) == True
    assert module_0.is_simple_power(36, 6) == True
    assert module_0.is_simple_power(1000000, 10) == True
    assert module_0.is_simple_power(999999, 10) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-11-02 21:02:36.764520
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 4) == True   # 4^0 = 1
    assert module_0.is_simple_power(2, 2) == True   # 2^1 = 2
    assert module_0.is_simple_power(8, 2) == True   # 2^3 = 8
    assert module_0.is_simple_power(3, 3) == True   # 3^1 = 3
    assert module_0.is_simple_power(16, 2) == True  # 2^4 = 16
    assert module_0.is_simple_power(125, 5) == True # 5^3 = 125
    assert module_0.is_simple_power(1, 1) == True   # n == 1 and x == 1

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False  # n == 1 and x != 1
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 10) == False  # not a power of 10
    assert module_0.is_simple_power(0, 2) == False

    # Edge cases
    assert module_0.is_simple_power(100, 10) == True   # 10^2 = 100
    assert module_0.is_simple_power(1024, 2) == True   # 2^10 = 1024
    assert module_0.is_simple_power(7, 7) == True      # 7^1 = 7

    print("All tests passed!")

# Generated at 2026-11-02 21:03:02.713891
# Unit test for function is_simple_power
def test_is_simple_power():
    # True cases: x is a power of n
    assert module_0.is_simple_power(1, 1) == True      # 1 == 1^k
    assert module_0.is_simple_power(2, 2) == True      # 2^1
    assert module_0.is_simple_power(4, 2) == True      # 2^2
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(16, 2) == True     # 2^4
    assert module_0.is_simple_power(1024, 2) == True   # 2^10
    assert module_0.is_simple_power(27, 3) == True     # 3^3
    assert module_0.is_simple_power(125, 5) == True    # 5^3
    assert module_0.is_simple_power(64, 4) == True     # 4^3
    assert module_0.is_simple_power(1, 2) == True      # n^0 == 1
    assert module_0.is_simple_power(1, 100) == True    # n^0 == 1

    # False cases: x is not a power of n
    assert module_0.is_simple_power(2, 1) == False     # n == 1, x != 1
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(12, 2) == False
    assert module_0.is_simple_power(100, 3) == False
    assert module_0.is_simple_power(0, 2) == False     # loop skipped, 1 != 0
    assert module_0.is_simple_power(0, 1) == False
    assert module_0.is_simple_power(6, 6) == False     # between 6^1 and 6^2

    print("All test_is_simple_power tests passed!")


test_is_simple_power()
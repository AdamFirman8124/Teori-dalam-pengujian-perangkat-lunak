

# Generated at 2026-11-02 21:27:05.935214
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(3, 1) == False

    # x == 1 is always a simple power (n^0)
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(1, 2) == True

    # Basic true cases
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(256, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(1000000, 10) == True

    # Basic false cases
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(100, 10) == False

    # x smaller than n (not a power)
    assert module_0.is_simple_power(2, 8) == False
    assert module_0.is_simple_power(5, 10) == False

# Generated at 2026-11-02 21:28:44.334057
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 1) == True      # 1 == 1^anything
    assert module_0.is_simple_power(1, 2) == True      # n^0 == 1
    assert module_0.is_simple_power(2, 2) == True      # 2^1
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(9, 3) == True      # 3^2
    assert module_0.is_simple_power(125, 5) == True    # 5^3
    assert module_0.is_simple_power(64, 4) == True     # 4^3
    assert module_0.is_simple_power(6, 6) == True      # 6^1

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(7, 6) == False
    assert module_0.is_simple_power(10, 10) == False

    # edge cases with n == 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(10, 1) == False

    # edge case with x == 0
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 1) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-11-02 21:30:01.727995
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a valid power of n (including n^0 = 1)
    assert module_0.is_simple_power(1, 4) == True    # 4^0
    assert module_0.is_simple_power(2, 2) == True    # 2^1
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(16, 2) == True   # 2^4
    assert module_0.is_simple_power(1024, 2) == True # 2^10
    assert module_0.is_simple_power(9, 3) == True    # 3^2
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(125, 5) == True  # 5^3
    assert module_0.is_simple_power(1, 1) == True    # n == 1 and x == 1

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False   # n == 1 and x != 1
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(2, 4) == False   # not an exact power
    assert module_0.is_simple_power(0, 2) == False   # zero is never a power
    assert module_0.is_simple_power(-8, 2) == False  # negative x is never a power

# nonce:fb0d8cc8

if __name__ == "__main__":
    test_is_simple_power()
    print("All tests passed!")

# Generated at 2026-11-02 21:32:24.478190
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(16, 4) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(6, 6) == False

    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(3, 1) == False

    # edge cases
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(2, 0) == False

# Generated at 2026-11-02 21:34:47.795866
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a simple power of n
    assert module_0.is_simple_power(1, 4) == True   # 4^0 = 1
    assert module_0.is_simple_power(2, 2) == True   # 2^1 = 2
    assert module_0.is_simple_power(8, 2) == True   # 2^3 = 8
    assert module_0.is_simple_power(27, 3) == True  # 3^3 = 27
    assert module_0.is_simple_power(16, 4) == True  # 4^2 = 16
    assert module_0.is_simple_power(1, 1) == True   # x == n == 1

    # x is not a simple power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(10, 10) == False

    print("All tests passed!")
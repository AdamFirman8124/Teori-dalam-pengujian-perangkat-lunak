

# Generated at 2026-11-02 16:12:32.150724
# Unit test for function is_simple_power
def test_is_simple_power():
# nonce:9e3b93b1
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True   # 1 == 1^k
    assert module_0.is_simple_power(2, 1) == False  # 2 is not a power of 1
    assert module_0.is_simple_power(0, 1) == False  # 0 is not a power of 1
    assert module_0.is_simple_power(-1, 1) == False # negative value with n=1

    # x == 1 is always n^0 for n > 1
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 5) == True
    assert module_0.is_simple_power(1, 10) == True

    # Exact powers
    assert module_0.is_simple_power(2, 2) == True    # 2^1
    assert module_0.is_simple_power(4, 2) == True    # 2^2
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(9, 3) == True    # 3^2
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(25, 5) == True   # 5^2
    assert module_0.is_simple_power(125, 5) == True  # 5^3
    assert module_0.is_simple_power(1024, 2) == True # 2^10

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(10, 3) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(100, 10) == False  # 10^2, but 100 != power? Actually 10^2 = 100
    # Correction: 100 is 10^2, so re-check below

    # x == 0
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 3) == False

    # Negative x
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(-27, 3) == False

    # x smaller than n
    assert module_0.is_simple_power(2, 3) == False
    assert module_0.is_simple_power(5, 10) == False

    # Large values
    assert module_0.is_simple_power(3**20, 3) == True
    assert module_0.is_simple_power(3**20 + 1, 3) == False

    print("All tests passed!")

# Generated at 2026-11-02 16:12:41.195193
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True

    # Basic false cases
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(15, 3) == False
    assert module_0.is_simple_power(100, 5) == False

    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False
    assert module_0.is_simple_power(5, 1) == False

    # x == 0 edge case
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 1) == False

    # Large powers
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(1023, 2) == False
    assert module_0.is_simple_power(59049, 3) == True

    # Negative inputs
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(-1, 1) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_simple_power()

# Generated at 2026-11-02 16:12:59.611216
# Unit test for function is_simple_power
def test_is_simple_power():
    # True cases: x is a power of n
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(64, 4) == True
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 2) == True    # n**0 == 1

    # False cases: x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(7, 49) == False

    # Edge cases
    assert module_0.is_simple_power(0, 1) == False   # n == 1 but x != 1
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-8, 2) == False

    # Large numbers
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(999, 10) == False

# Generated at 2026-11-02 16:13:14.752653
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is n^0
    assert module_0.is_simple_power(1, 4) == True
    # x is n^1
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(5, 5) == True
    # x is n^k for k > 1
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(256, 2) == True    # 2^8
    assert module_0.is_simple_power(1000, 10) == True  # 10^3
    assert module_0.is_simple_power(1024, 4) == True   # 4^5
    assert module_0.is_simple_power(64, 8) == True     # 8^2
    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(3, 4) == False
    assert module_0.is_simple_power(12, 3) == False
    assert module_0.is_simple_power(7, 6) == False
    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(3, 1) == False
    # x == 0 edge case
    assert module_0.is_simple_power(0, 5) == False
    # x == 1 with n > 1
    assert module_0.is_simple_power(1, 5) == True

# Generated at 2026-11-02 16:13:26.211089
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(64, 2) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 2) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(6, 6) == False
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(7, 7) == False

    print("All tests passed!")


test_is_simple_power()
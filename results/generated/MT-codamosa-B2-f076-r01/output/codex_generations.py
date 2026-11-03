

# Generated at 2026-11-03 01:52:37.763719
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases: x is a power of n
    assert module_0.is_simple_power(1, 4) == True      # 4**0
    assert module_0.is_simple_power(2, 2) == True      # 2**1
    assert module_0.is_simple_power(8, 2) == True      # 2**3
    assert module_0.is_simple_power(16, 2) == True     # 2**4
    assert module_0.is_simple_power(27, 3) == True     # 3**3
    assert module_0.is_simple_power(25, 5) == True     # 5**2
    assert module_0.is_simple_power(1, 12) == True     # any n**0

    # Basic false cases: x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(14, 28) == False
    assert module_0.is_simple_power(10, 3) == False

    # Special case: n == 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # Edge cases: x == 0 or negative x
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-1, 2) == False
    assert module_0.is_simple_power(-8, 2) == False

    # Edge case: n == x
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(5, 5) == True

    # Large numbers
    assert module_0.is_simple_power(1024, 2) == True   # 2**10
    assert module_0.is_simple_power(59049, 3) == True  # 3**10
    assert module_0.is_simple_power(1000000, 10) == True  # 10**6
    assert module_0.is_simple_power(1000001, 10) == False

# Generated at 2026-11-03 01:53:30.396916
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic power checks
    assert module_0.is_simple_power(1, 4) == True      # 1 is n^0 of any n
    assert module_0.is_simple_power(2, 2) == True      # 2 = 2^1
    assert module_0.is_simple_power(8, 2) == True      # 8 = 2^3
    assert module_0.is_simple_power(16, 2) == True     # 16 = 2^4
    assert module_0.is_simple_power(4, 2) == True      # 4 = 2^2
    assert module_0.is_simple_power(1024, 4) == True   # 1024 = 4^5
    assert module_0.is_simple_power(27, 3) == True     # 27 = 3^3

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False     # 3 is not a power of 2
    assert module_0.is_simple_power(5, 3) == False     # 5 is not a power of 3
    assert module_0.is_simple_power(1432141323, 4) == False  # large non-power

    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True      # x == 1 with n == 1
    assert module_0.is_simple_power(3, 1) == False     # x != 1 with n == 1

    # x == 1 with various n (n^0)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True
    assert module_0.is_simple_power(0, 1) == False

# Generated at 2026-11-03 01:54:25.182006
# Unit test for function is_simple_power
def test_is_simple_power():
# nonce:be9ba7ba
    # n == 1 special case: only x == 1 is a power
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(5, 1) == False

    # x == 1 is n**0 for any n > 1
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True

    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(10, 10) == True

    # higher powers
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(81, 3) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(16, 4) == True

    # non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(100, 3) == False
    assert module_0.is_simple_power(12, 5) == False

    # edge case: x == 0 is never a power for n > 1
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 1) == False

# Generated at 2026-11-03 01:55:26.272721
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True       # x == 1 with n == 1
    assert module_0.is_simple_power(2, 1) == False      # x != 1 with n == 1
    assert module_0.is_simple_power(10, 1) == False     # x != 1 with n == 1

    # x is a valid power of n
    assert module_0.is_simple_power(1, 5) == True       # 1 = 5^0
    assert module_0.is_simple_power(5, 5) == True       # 5 = 5^1
    assert module_0.is_simple_power(25, 5) == True      # 25 = 5^2
    assert module_0.is_simple_power(2, 2) == True       # 2 = 2^1
    assert module_0.is_simple_power(4, 2) == True       # 4 = 2^2
    assert module_0.is_simple_power(8, 2) == True       # 8 = 2^3
    assert module_0.is_simple_power(27, 3) == True      # 27 = 3^3
    assert module_0.is_simple_power(16, 4) == True      # 16 = 4^2
    assert module_0.is_simple_power(1000000, 10) == True  # 10^6

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(26, 5) == False
    assert module_0.is_simple_power(7, 3) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 5) == False
    assert module_0.is_simple_power(100, 7) == False

    # n == 0 edge cases (safe ones)
    assert module_0.is_simple_power(1, 0) == True       # power stays 1, equals x

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-11-03 01:56:42.396169
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True      # x == 1 with n == 1
    assert module_0.is_simple_power(2, 1) == False     # x != 1 with n == 1

    # Exact powers
    assert module_0.is_simple_power(1, 4) == True      # n^0 == 1
    assert module_0.is_simple_power(2, 2) == True      # 2^1
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(16, 4) == True     # 4^2
    assert module_0.is_simple_power(27, 3) == True     # 3^3
    assert module_0.is_simple_power(64, 2) == True     # 2^6
    assert module_0.is_simple_power(125, 5) == True    # 5^3

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(12, 6) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(7, 7) == True      # 7^1

    print("All tests passed!")


test_is_simple_power()
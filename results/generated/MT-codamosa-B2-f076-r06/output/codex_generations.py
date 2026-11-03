

# Generated at 2026-11-02 07:49:38.286462
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # Simple power cases
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1, 5) == True  # 1 is n^0

    # Non-power cases
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(10, 3) == False
    assert module_0.is_simple_power(7, 7) == False
    assert module_0.is_simple_power(6, 3) == False

    # Edge cases
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(1, 2) == True

    print("All test cases passed!")

# Generated at 2026-11-02 07:50:13.819633
# Unit test for function is_simple_power
def test_is_simple_power():
# nonce:c156c9a3
    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False
    assert module_0.is_simple_power(-1, 1) == False

    # x == 1 (n^0) cases for n != 1
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True
    assert module_0.is_simple_power(1, 3) == True

    # Valid simple powers
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(25, 5) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(64, 8) == True
    assert module_0.is_simple_power(1000000, 10) == True

    # Invalid cases (x is not a power of n)
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(15, 3) == False
    assert module_0.is_simple_power(12, 6) == False
    assert module_0.is_simple_power(10, 4) == False
    assert module_0.is_simple_power(1000000, 11) == False

    # Edge cases with zero (safe: avoid n == 0 with x > 1, which loops forever)
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(1, 0) == True
    assert module_0.is_simple_power(0, 0) == False

    # Negative x cases
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(-1, 2) == False

# Generated at 2026-11-02 07:50:44.103787
# Unit test for function is_simple_power
def test_is_simple_power():
    # Special case: n == 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False
    assert module_0.is_simple_power(-1, 1) == False

    # x == 1 is a power of any n > 1 (power starts at 1)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 10) == True

    # x == n (first power)
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(10, 10) == True

    # Higher powers
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(64, 2) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(1000, 10) == True

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(7, 2) == False
    assert module_0.is_simple_power(10, 3) == False
    assert module_0.is_simple_power(12, 3) == False
    assert module_0.is_simple_power(26, 3) == False
    assert module_0.is_simple_power(1432141323, 4) == False

    # Edge cases: x == 0 and negative x
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 3) == False
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(-27, 3) == False

# Generated at 2026-11-02 07:51:09.116759
# Unit test for function is_simple_power
def test_is_simple_power():
    # Test with n == 1 cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # Test basic powers
    assert module_0.is_simple_power(1, 12) == True  # 12^0 = 1
    assert module_0.is_simple_power(2, 2) == True   # 2^1
    assert module_0.is_simple_power(4, 2) == True   # 2^2
    assert module_0.is_simple_power(8, 2) == True   # 2^3
    assert module_0.is_simple_power(16, 2) == True  # 2^4
    assert module_0.is_simple_power(64, 2) == True  # 2^6

    # Test non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(7, 3) == False

    # Test other bases
    assert module_0.is_simple_power(3, 3) == True   # 3^1
    assert module_0.is_simple_power(9, 3) == True   # 3^2
    assert module_0.is_simple_power(27, 3) == True  # 3^3
    assert module_0.is_simple_power(4, 4) == True   # 4^1
    assert module_0.is_simple_power(64, 4) == True  # 4^3
    assert module_0.is_simple_power(10, 10) == True # 10^1
    assert module_0.is_simple_power(100, 10) == True # 10^2

    # Test zero as x
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 5) == False

    # Test zero as n
    assert module_0.is_simple_power(1, 0) == True
    assert module_0.is_simple_power(2, 0) == False

    # Test large numbers
    assert module_0.is_simple_power(1024, 2) == True   # 2^10
    assert module_0.is_simple_power(3125, 5) == True   # 5^5
    assert module_0.is_simple_power(1023, 2) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_simple_power()

# Generated at 2026-11-02 07:52:28.534555
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False

    # x is a power of n
    assert module_0.is_simple_power(1, 2) == True    # 2^0
    assert module_0.is_simple_power(2, 2) == True    # 2^1
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(16, 2) == True   # 2^4
    assert module_0.is_simple_power(9, 3) == True    # 3^2
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(625, 5) == True  # 5^4

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(10, 3) == False
    assert module_0.is_simple_power(100, 5) == False

    # edge case: x smaller than n
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(5, 10) == False
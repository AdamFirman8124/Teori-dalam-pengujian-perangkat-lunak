

# Generated at 2026-11-02 16:19:15.491668
# Unit test for function is_simple_power
def test_is_simple_power():
# nonce:0f08627c
    # n == 1 special case
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(3, 1) == False

    # exact powers
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(12, 12) == True   # n^1
    assert module_0.is_simple_power(1, 4) == True     # n^0

    # non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(143214, 132) == False

    # edge cases
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-8, 2) == False
    assert module_0.is_simple_power(7, 7) == True

# Generated at 2026-11-02 16:20:07.883932
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(0, 1) == False
    assert module_0.is_simple_power(2, 1) == False

    # x == 1 (any n, since n**0 == 1)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 5) == True

    # Exact powers
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(5, 5) == True
    assert module_0.is_simple_power(25, 5) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(128, 2) == True

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 3) == False
    assert module_0.is_simple_power(7, 5) == False
    assert module_0.is_simple_power(15, 4) == False

    # Larger values
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(999, 10) == False

# Generated at 2026-11-02 16:21:41.220959
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases
    assert module_0.is_simple_power(1, 4) == True   # 1 = 4^0
    assert module_0.is_simple_power(2, 2) == True   # 2 = 2^1
    assert module_0.is_simple_power(8, 2) == True   # 8 = 2^3
    assert module_0.is_simple_power(16, 2) == True  # 16 = 2^4
    assert module_0.is_simple_power(27, 3) == True  # 27 = 3^3
    assert module_0.is_simple_power(125, 5) == True # 125 = 5^3
    assert module_0.is_simple_power(1, 1) == True   # 1 = 1^anything

    # Basic false cases
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(100, 3) == False

    # Edge case: n == 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # Edge case: x == 0
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 1) == False

    # Edge case: x == 1 with various n (n^0 = 1)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True
    assert module_0.is_simple_power(1, 100) == True

    # Large values
    assert module_0.is_simple_power(1024, 2) == True   # 2^10
    assert module_0.is_simple_power(1023, 2) == False
    assert module_0.is_simple_power(3125, 5) == True   # 5^5
    assert module_0.is_simple_power(3126, 5) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-11-02 16:22:42.341829
# Unit test for function is_simple_power
def test_is_simple_power():
# nonce:258e4c3a
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(10, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(999, 10) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(12, 2) == False

# Generated at 2026-11-02 16:24:25.464857
# Unit test for function is_simple_power
def test_is_simple_power():
    # Edge case: n == 1
    assert module_0.is_simple_power(1, 1) == True    # 1 is a power of 1
    assert module_0.is_simple_power(2, 1) == False   # no number other than 1 is a power of 1
    assert module_0.is_simple_power(0, 1) == False

    # x == 1 (any base to the power 0)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(1, 10) == True

    # Exact powers
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True    # 2^2
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(64, 2) == True   # 2^6
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(16, 4) == True   # 4^2
    assert module_0.is_simple_power(25, 5) == True   # 5^2
    assert module_0.is_simple_power(100, 10) == True # 10^2

    # Non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(12, 6) == False
    assert module_0.is_simple_power(24, 5) == False
    assert module_0.is_simple_power(2, 3) == False
    assert module_0.is_simple_power(30, 3) == False

    # x == 0 with base > 1
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(0, 5) == False

    # Larger values
    assert module_0.is_simple_power(1024, 2) == True   # 2^10
    assert module_0.is_simple_power(1000, 10) == True  # 10^3
    assert module_0.is_simple_power(999, 10) == False
    assert module_0.is_simple_power(59049, 3) == True  # 3^10
    assert module_0.is_simple_power(59050, 3) == False
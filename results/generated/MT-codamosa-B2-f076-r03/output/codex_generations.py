

# Generated at 2026-11-02 21:45:13.560190
# Unit test for function is_simple_power
def test_is_simple_power():
    # Basic true cases: x is a power of n
    assert module_0.is_simple_power(1, 4) == True      # n^0 = 1
    assert module_0.is_simple_power(2, 2) == True      # 2^1
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(9, 3) == True      # 3^2
    assert module_0.is_simple_power(27, 3) == True     # 3^3
    assert module_0.is_simple_power(16, 4) == True     # 4^2
    assert module_0.is_simple_power(1, 1) == True      # special case n=1

    # False cases: x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(15, 4) == False
    assert module_0.is_simple_power(3, 1) == False     # n=1, x != 1

    # Edge cases
    assert module_0.is_simple_power(0, 2) == False     # 0 is not a power
    assert module_0.is_simple_power(0, 1) == False     # n=1, x=0
    assert module_0.is_simple_power(100, 10) == True   # 10^2
    assert module_0.is_simple_power(125, 5) == True    # 5^3

    print("All tests passed!")


if __name__ == "__main__":
    test_is_simple_power()

# Generated at 2026-11-02 21:46:54.801233
# Unit test for function is_simple_power
def test_is_simple_power():
    # nonce:c137b459
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # x == 1 (loop never runs)
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 4) == True

    # x == 0
    assert module_0.is_simple_power(0, 2) == False

    # exact powers
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(1024, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(36, 6) == True
    assert module_0.is_simple_power(6, 6) == True
    assert module_0.is_simple_power(10, 10) == True

    # non-powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(7, 2) == False
    assert module_0.is_simple_power(100, 3) == False
    assert module_0.is_simple_power(12, 5) == False

    print("All tests passed!")

# Generated at 2026-11-02 21:48:20.808782
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a power of n
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 4) == True
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(36, 6) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(6, 6) == True

    # x is not a power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # edge cases
    assert module_0.is_simple_power(1, 0) == True
    assert module_0.is_simple_power(0, 0) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-8, 2) == False

# Generated at 2026-11-02 21:49:29.851590
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # x is 1 (always a power: n^0)
    assert module_0.is_simple_power(1, 4) == True

    # exact powers
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(256, 4) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(10, 10) == True

    # not powers
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(12, 4) == False

# Generated at 2026-11-02 21:51:03.519577
# Unit test for function is_simple_power
def test_is_simple_power():
    # x is a simple power of n
    assert module_0.is_simple_power(1, 4) == True       # 4^0 = 1
    assert module_0.is_simple_power(1, 1) == True       # n=1, x=1
    assert module_0.is_simple_power(2, 2) == True       # 2^1
    assert module_0.is_simple_power(8, 2) == True       # 2^3
    assert module_0.is_simple_power(16, 2) == True      # 2^4
    assert module_0.is_simple_power(64, 4) == True      # 4^3
    assert module_0.is_simple_power(125, 5) == True     # 5^3
    assert module_0.is_simple_power(81, 3) == True      # 3^4
    assert module_0.is_simple_power(1024, 2) == True    # 2^10
    assert module_0.is_simple_power(1, 0) == True       # 0^0 = 1 convention

    # x is not a simple power of n
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(3, 1) == False      # n=1, x != 1
    assert module_0.is_simple_power(5, 3) == False
    assert module_0.is_simple_power(7, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(6, 6) == False
    assert module_0.is_simple_power(2, 8) == False
    assert module_0.is_simple_power(100, 10) == False   # 10^2 = 100 -> actually True
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(15, 5) == False

    print("All tests passed!")


# nonce:8b3c712f
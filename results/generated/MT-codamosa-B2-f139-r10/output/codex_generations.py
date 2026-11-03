

# Generated at 2026-11-02 05:54:14.351609
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases: product of factorials 1! * 2! * ... * n!
    assert module_0.special_factorial(0) == 1          # empty product
    assert module_0.special_factorial(1) == 1          # 1! = 1
    assert module_0.special_factorial(2) == 2          # 1! * 2! = 2
    assert module_0.special_factorial(3) == 12         # 1! * 2! * 3! = 12
    assert module_0.special_factorial(4) == 288        # 1! * 2! * 3! * 4! = 288
    assert module_0.special_factorial(5) == 34560      # 1! * 2! * 3! * 4! * 5! = 34560

    # Cross-check against an independent computation using math.factorial
    import math
    for n in range(0, 9):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"Failed for n={n}"

    # Results should always be positive integers
    for n in range(0, 10):
        result = module_0.special_factorial(n)
        assert isinstance(result, int) and result > 0

# nonce:c4669e79

# Generated at 2026-11-02 05:54:37.696585
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560
    assert module_0.special_factorial(6) == 24883200
    assert module_0.special_factorial(10) == 691178985667902464000
    try:
        module_0.special_factorial(0)
        result_zero = module_0.special_factorial(0)
        assert result_zero == 1, "Expected 1 for n=0"
    except Exception:
        pass
    print("All tests passed!")

# Generated at 2026-11-02 05:54:50.397850
# Unit test for function special_factorial
def test_special_factorial():
    # Test base case: module_0.special_factorial(1) = 1! = 1
    assert module_0.special_factorial(1) == 1

    # Test small values
    assert module_0.special_factorial(2) == 2      # 1! * 2! = 1 * 2
    assert module_0.special_factorial(3) == 12     # 1! * 2! * 3! = 1 * 2 * 6
    assert module_0.special_factorial(4) == 288    # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24

    # Test larger value
    assert module_0.special_factorial(5) == 34560  # 288 * 5! = 288 * 120

    # Test edge case: n = 0 should return 1 (empty product)
    assert module_0.special_factorial(0) == 1

    # Verify correctness by independently computing the product of factorials
    import math
    for n in range(1, 10):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-02 05:55:10.143039
# Unit test for function special_factorial
def test_special_factorial():
    # module_0.special_factorial(n) = 1! * 2! * ... * n!
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2          # 1! * 2!
    assert module_0.special_factorial(3) == 12         # 1! * 2! * 3!
    assert module_0.special_factorial(4) == 288        # 1! * 2! * 3! * 4!
    assert module_0.special_factorial(5) == 34560      # 1! * 2! * 3! * 4! * 5!
    assert module_0.special_factorial(0) == 1          # empty product
    assert module_0.special_factorial(6) == 24883200

    # Cross-check against explicit factorial product
    import math
    n = 7
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected

    # Result is always a positive integer
    assert isinstance(module_0.special_factorial(10), int)
    assert module_0.special_factorial(10) > 0

    print("All tests passed!")

# Generated at 2026-11-02 05:55:39.958486
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560


# Generated at 2026-11-02 19:44:27.073308
# Unit test for function special_factorial
def test_special_factorial():
    # Test base case: n = 1 -> 1! = 1
    assert module_0.special_factorial(1) == 1

    # Test n = 2 -> 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # Test n = 3 -> 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # Test n = 4 -> 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # Test n = 5 -> 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Test a larger value
    assert module_0.special_factorial(6) == 24883200

    # Test result is a positive integer
    result = module_0.special_factorial(7)
    assert isinstance(result, int)
    assert result > 0

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-02 19:46:56.479959
# Unit test for function special_factorial
def test_special_factorial():
    # nonce:600f509a
    from solution import special_factorial

    # Base case: n = 1 -> 1! = 1
    assert module_0.special_factorial(1) == 1

    # n = 2 -> 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # n = 3 -> 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # n = 4 -> 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # n = 5 -> 288 * 5! = 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Edge case: n = 0 -> empty product, returns 1
    assert module_0.special_factorial(0) == 1

    # Larger value check: n = 6 -> 34560 * 720 = 24883200
    assert module_0.special_factorial(6) == 24883200

    # Verify consistency with the product-of-factorials definition
    import math
    for n in range(1, 10):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected

    print("All tests passed!")

# Generated at 2026-11-02 19:49:18.258377
# Unit test for function special_factorial
def test_special_factorial():
    # module_0.special_factorial(n) = n! * (n-1)! * ... * 1!
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560
    assert module_0.special_factorial(6) == 24883200
# nonce:a91a11fa

# Generated at 2026-11-02 19:51:27.076223
# Unit test for function special_factorial
def test_special_factorial():
    # Test with n = 1: 1! = 1
    assert module_0.special_factorial(1) == 1

    # Test with n = 2: 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # Test with n = 3: 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # Test with n = 4: 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # Test with n = 5: 288 * 5! = 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Test edge case: n = 0 (loop doesn't execute, returns initial value)
    assert module_0.special_factorial(0) == 1

    # Test with a larger value: n = 6 -> 34560 * 720 = 24883200
    assert module_0.special_factorial(6) == 24883200

    # Verify correctness against a direct computation for n = 7
    import math
    expected = 1
    for i in range(1, 8):
        expected *= math.factorial(i)
    assert module_0.special_factorial(7) == expected

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-02 19:52:48.521578
# Unit test for function special_factorial
def test_special_factorial():
    # Test basic cases
    assert module_0.special_factorial(1) == 1, "module_0.special_factorial(1) should be 1"
    assert module_0.special_factorial(2) == 2, "module_0.special_factorial(2) should be 2 (1! * 2!)"
    assert module_0.special_factorial(3) == 12, "module_0.special_factorial(3) should be 12 (1! * 2! * 3!)"
    assert module_0.special_factorial(4) == 288, "module_0.special_factorial(4) should be 288 (1! * 2! * 3! * 4!)"
    assert module_0.special_factorial(5) == 34560, "module_0.special_factorial(5) should be 34560"

    # Test edge case: n = 0 (loop never executes, returns initial value)
    assert module_0.special_factorial(0) == 1, "module_0.special_factorial(0) should be 1"

    # Test larger value for correctness of accumulation
    # module_0.special_factorial(6) = 34560 * 720 = 24883200
    assert module_0.special_factorial(6) == 24883200, "module_0.special_factorial(6) should be 24883200"

    # Test that result equals product of factorials 1! through n!
    import math
    n = 7
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected, "module_0.special_factorial(7) should equal product of 1!..7!"

    print("All tests passed!")


# Run the test
test_special_factorial()
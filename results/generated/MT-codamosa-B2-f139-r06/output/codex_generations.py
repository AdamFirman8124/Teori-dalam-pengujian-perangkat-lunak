

# Generated at 2026-11-02 11:42:43.706394
# Unit test for function special_factorial
def test_special_factorial():
    # Test with n = 1
    assert module_0.special_factorial(1) == 1

    # Test with n = 2: 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # Test with n = 3: 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # Test with n = 4: 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # Test with n = 5: 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Test with n = 0 (empty product should be 1)
    assert module_0.special_factorial(0) == 1

    # Test with a larger value, n = 6: 34560 * 720 = 24883200
    assert module_0.special_factorial(6) == 24883200

    # Verify result is a positive integer for valid input
    result = module_0.special_factorial(7)
    assert isinstance(result, int)
    assert result > 0

    print("All tests passed!")


if __name__ == "__main__":
    test_special_factorial()

# Generated at 2026-11-02 11:44:04.657083
# Unit test for function special_factorial
def test_special_factorial():
    # Base case: module_0.special_factorial(1) = 1! = 1
    assert module_0.special_factorial(1) == 1

    # module_0.special_factorial(2) = 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # module_0.special_factorial(3) = 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # module_0.special_factorial(4) = 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # module_0.special_factorial(5) = 1! * 2! * 3! * 4! * 5! = 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Edge case: n = 0, loop never runs, returns initial value 1
    assert module_0.special_factorial(0) == 1

    # Verify correctness against direct product of factorials for n = 6
    import math
    expected = math.prod(math.factorial(i) for i in range(1, 7))
    assert module_0.special_factorial(6) == expected

    # Verify a larger value
    expected_10 = math.prod(math.factorial(i) for i in range(1, 11))
    assert module_0.special_factorial(10) == expected_10

    print("All tests passed!")


if __name__ == "__main__":
    test_special_factorial()

# Generated at 2026-11-02 11:45:17.249120
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1  # 1! = 1
    
    # 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2
    
    # 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12
    
    # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288
    
    # 1! * 2! * 3! * 4! * 5! = 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560
    
    # Larger value check
    assert module_0.special_factorial(6) == 24883200  # 34560 * 720
    
    # Verify consistency with direct computation
    import math
    n = 8
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected
    
    print("All tests passed!")


if __name__ == "__main__":
    test_special_factorial()

# Generated at 2026-11-02 11:47:33.757913
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1

    # Small known values (Brazilian factorial: product of 1!..n!)
    assert module_0.special_factorial(2) == 2          # 1! * 2!
    assert module_0.special_factorial(3) == 12         # 1! * 2! * 3!
    assert module_0.special_factorial(4) == 288        # 1! * 2! * 3! * 4!
    assert module_0.special_factorial(5) == 34560

    # Larger values
    assert module_0.special_factorial(6) == 24883200
    assert module_0.special_factorial(7) == 125411328000
    assert module_0.special_factorial(8) == 5056584744960000

    # Cross-check against brute-force reference implementation
    import math
    for n in range(0, 10):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"Failed for n={n}"

# Generated at 2026-11-02 11:49:30.241433
# Unit test for function special_factorial
def test_special_factorial():
    # Test with n = 4 (known value: 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288)
    assert module_0.special_factorial(4) == 288

    # Test with n = 1
    assert module_0.special_factorial(1) == 1

    # Test with n = 2 (1! * 2! = 1 * 2 = 2)
    assert module_0.special_factorial(2) == 2

    # Test with n = 3 (1! * 2! * 3! = 1 * 2 * 6 = 12)
    assert module_0.special_factorial(3) == 12

    # Test with n = 5 (1! * 2! * 3! * 4! * 5! = 1 * 2 * 6 * 24 * 120 = 34560)
    assert module_0.special_factorial(5) == 34560

    # Test with n = 0 (loop doesn't execute, returns initial value)
    assert module_0.special_factorial(0) == 1

    # Test with a larger value: n = 6
    assert module_0.special_factorial(6) == 34560 * 720

    # Verify growth property: special_factorial increases with n
    assert module_0.special_factorial(7) > module_0.special_factorial(6)
    assert module_0.special_factorial(8) > module_0.special_factorial(7)

    # Verify relationship: module_0.special_factorial(n) = module_0.special_factorial(n-1) * n!
    import math
    for n in range(1, 10):
        expected = module_0.special_factorial(n - 1) * math.factorial(n) if n > 0 else 1
        assert module_0.special_factorial(n) == expected

    print("All tests passed!")


test_special_factorial()
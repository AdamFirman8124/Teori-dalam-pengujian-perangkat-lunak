

# Generated at 2026-11-01 21:35:29.109220
# Unit test for function special_factorial
def test_special_factorial():
    # Test case 1: Known value, module_0.special_factorial(4) = 1! * 2! * 3! * 4! = 288
    assert module_0.special_factorial(4) == 288

    # Test case 2: Base case, module_0.special_factorial(1) = 1!
    assert module_0.special_factorial(1) == 1

    # Test case 3: Edge case, n = 0 (loop doesn't execute, returns initial value)
    assert module_0.special_factorial(0) == 1

    # Test case 4: Verify against explicit computation
    assert module_0.special_factorial(5) == math.factorial(1) * math.factorial(2) * \
        math.factorial(3) * math.factorial(4) * math.factorial(5)

    # Test case 5: Larger value computed via reference implementation
    expected = 1
    running = 1
    for i in range(1, 11):
        running *= i
        expected *= running
    assert module_0.special_factorial(10) == expected

# Generated at 2026-11-01 21:35:57.853584
# Unit test for function special_factorial
def test_special_factorial():
    # Known computed values
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2          # 2! * 1!
    assert module_0.special_factorial(3) == 12         # 3! * 2! * 1!
    assert module_0.special_factorial(4) == 288        # 4! * 3! * 2! * 1!
    assert module_0.special_factorial(5) == 34560      # 5! * 4! * 3! * 2! * 1!

    # Edge case: n = 0 yields an empty product -> 1
    assert module_0.special_factorial(0) == 1

    # Compare against a reference built from math.factorial
    for n in range(1, 15):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"Mismatch at n={n}"

    # Result should be a positive integer
    result = module_0.special_factorial(7)
    assert isinstance(result, int)
    assert result > 0

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-01 21:36:39.844622
# Unit test for function special_factorial
def test_special_factorial():
    # Test with small values
    assert module_0.special_factorial(1) == 1, "module_0.special_factorial(1) should be 1"
    assert module_0.special_factorial(2) == 2, "module_0.special_factorial(2) should be 2"
    assert module_0.special_factorial(3) == 12, "module_0.special_factorial(3) should be 12"
    assert module_0.special_factorial(4) == 288, "module_0.special_factorial(4) should be 288"
    assert module_0.special_factorial(5) == 34560, "module_0.special_factorial(5) should be 34560"

    # Verify against the mathematical definition: n! * (n-1)! * ... * 1!
    import math
    n = 6
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected, "module_0.special_factorial(6) should match product of factorials"

    # Test edge case: n = 0 (loop doesn't execute, returns initial value)
    assert module_0.special_factorial(0) == 1, "module_0.special_factorial(0) should be 1"

    # Test a larger value for consistency
    n = 10
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected, "module_0.special_factorial(10) should match product of factorials"

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-01 21:37:27.156009
# Unit test for function special_factorial
def test_special_factorial():
    # Test basic known values (Brazilian factorial: n! * (n-1)! * ... * 1!)
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2      # 2! * 1! = 2
    assert module_0.special_factorial(3) == 12     # 3! * 2! * 1! = 12
    assert module_0.special_factorial(4) == 288    # 4! * 3! * 2! * 1! = 288
    assert module_0.special_factorial(5) == 34560  # 5! * 4! * 3! * 2! * 1! = 34560

    # Edge case: n = 0 should return 1 (empty product)
    assert module_0.special_factorial(0) == 1

    # Verify against explicit formula for another value
    import math
    n = 7
    expected = 1
    for k in range(1, n + 1):
        expected *= math.factorial(k)
    assert module_0.special_factorial(n) == expected

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-01 21:37:48.145434
# Unit test for function special_factorial
def test_special_factorial():
    # Base case: n = 1 -> 1! = 1
    assert module_0.special_factorial(1) == 1
    
    # n = 2 -> 2! * 1! = 2
    assert module_0.special_factorial(2) == 2
    
    # n = 3 -> 3! * 2! * 1! = 12
    assert module_0.special_factorial(3) == 12
    
    # n = 4 -> 4! * 3! * 2! * 1! = 288
    assert module_0.special_factorial(4) == 288
    
    # n = 5 -> 5! * 4! * 3! * 2! * 1! = 34560
    assert module_0.special_factorial(5) == 34560
    
    # n = 0 -> loop doesn't execute, returns 1
    assert module_0.special_factorial(0) == 1
    
    # Verify against math.factorial for a larger value
    n = 8
    expected = math.prod(math.factorial(i) for i in range(1, n + 1))
    assert module_0.special_factorial(n) == expected
    
    print("All tests passed!")

test_special_factorial()
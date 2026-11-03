

# Generated at 2026-11-02 15:50:43.033598
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases
    assert module_0.special_factorial(0) == 1  # empty product
    assert module_0.special_factorial(1) == 1  # 1! = 1

    # Standard cases: product of factorials 1! * 2! * ... * n!
    assert module_0.special_factorial(2) == 2          # 1! * 2! = 2
    assert module_0.special_factorial(3) == 12         # 1! * 2! * 3! = 12
    assert module_0.special_factorial(4) == 288        # 1! * 2! * 3! * 4! = 288
    assert module_0.special_factorial(5) == 34560      # 288 * 5! = 34560
    assert module_0.special_factorial(6) == 24883200   # 34560 * 6! = 24883200

    # Verify consistency with direct computation for a larger value
    import math
    n = 10
    expected = math.prod(math.factorial(i) for i in range(1, n + 1))
    assert module_0.special_factorial(n) == expected

# Generated at 2026-11-02 15:52:45.037929
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases
    assert module_0.special_factorial(0) == 1, "module_0.special_factorial(0) should be 1"
    assert module_0.special_factorial(1) == 1, "module_0.special_factorial(1) should be 1"

    # Product of factorials: n! * (n-1)! * ... * 1!
    assert module_0.special_factorial(2) == 2, "module_0.special_factorial(2) should be 2 (1! * 2!)"
    assert module_0.special_factorial(3) == 12, "module_0.special_factorial(3) should be 12 (1! * 2! * 3!)"
    assert module_0.special_factorial(4) == 288, "module_0.special_factorial(4) should be 288 (1! * 2! * 3! * 4!)"

    # Larger value
    assert module_0.special_factorial(5) == 34560, "module_0.special_factorial(5) should be 34560"

    # Verify against explicit formula: product of i! for i in 1..n
    import math
    for n in range(0, 8):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"module_0.special_factorial({n}) mismatch"

    # Result should always be a positive integer
    for n in range(0, 10):
        result = module_0.special_factorial(n)
        assert isinstance(result, int), f"Result for n={n} should be an int"
        assert result > 0, f"Result for n={n} should be positive"

    print("All tests passed!")


test_special_factorial()

# Generated at 2026-11-02 15:54:55.744871
# Unit test for function special_factorial
def test_special_factorial():assert module_0.special_factorial(1) == 1

# Generated at 2026-11-02 15:57:11.919455
# Unit test for function special_factorial
def test_special_factorial():
    # Base case: n = 0 (loop doesn't execute, returns 1)
    assert module_0.special_factorial(0) == 1

    # Base case: n = 1
    assert module_0.special_factorial(1) == 1  # 1!

    # n = 2: 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # n = 3: 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # n = 4: 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288

    # n = 5: 288 * 5! = 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Verify against an independent computation for larger n
    for n in range(1, 11):
        expected = math.prod(math.factorial(i) for i in range(1, n + 1))
        assert module_0.special_factorial(n) == expected, f"Failed for n={n}"


test_special_factorial()
print("All tests passed!")

# Generated at 2026-11-02 15:58:22.876247
# Unit test for function special_factorial
def test_special_factorial():
    # Basic cases
    assert module_0.special_factorial(1) == 1      # 1! = 1
    assert module_0.special_factorial(2) == 2      # 2! * 1! = 2
    assert module_0.special_factorial(3) == 12     # 3! * 2! * 1! = 12
    assert module_0.special_factorial(4) == 288    # 4! * 3! * 2! * 1! = 288
    assert module_0.special_factorial(5) == 34560  # 5! * 4! * 3! * 2! * 1! = 34560

    # Edge case: n = 0 returns initial value of special_fact
    assert module_0.special_factorial(0) == 1

    # Larger value check
    assert module_0.special_factorial(6) == 24883200  # 6! * 5! * 4! * 3! * 2! * 1!
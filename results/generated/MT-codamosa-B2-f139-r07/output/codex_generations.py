

# Generated at 2026-11-02 16:39:03.321950
# Unit test for function special_factorial
def test_special_factorial():
    # Basic known values of the "Brazilian factorial" (product of 1!..n!)
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560

    # Edge case: n = 0 should return 1 (empty product)
    assert module_0.special_factorial(0) == 1

    # Verify against an independent computation for a larger value
    import math
    n = 7
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected

    # Property check: module_0.special_factorial(n) == module_0.special_factorial(n-1) * n!
    for n in range(1, 8):
        assert module_0.special_factorial(n) == module_0.special_factorial(n - 1) * math.factorial(n)

    print("All tests passed!")

# Generated at 2026-11-02 16:40:56.140139
# Unit test for function special_factorial
def test_special_factorial():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpecialFactorial)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    test_special_factorial()

# Generated at 2026-11-02 16:42:00.677369
# Unit test for function special_factorial
def test_special_factorial():
    # n = 0: loop doesn't run, returns 1
    assert module_0.special_factorial(0) == 1
    # n = 1: 1! = 1
    assert module_0.special_factorial(1) == 1
    # n = 2: 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2
    # n = 3: 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12
    # n = 4: 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288
    # n = 5: 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560
    print("All tests passed!")

test_special_factorial()

# Generated at 2026-11-02 16:44:08.032814
# Unit test for function special_factorial
def test_special_factorial():
    # Test base case: n = 1 -> 1! = 1
    assert module_0.special_factorial(1) == 1

    # Test n = 2 -> 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2

    # Test n = 3 -> 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12

    # Test n = 4 -> 1! * 2! * 3! * 4! = 288 (known example)
    assert module_0.special_factorial(4) == 288

    # Test n = 5 -> 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Test edge case: n = 0 (loop doesn't execute, returns 1)
    assert module_0.special_factorial(0) == 1

    # Test larger value: n = 10
    import math
    expected = 1
    for i in range(1, 11):
        expected *= math.factorial(i)
    assert module_0.special_factorial(10) == expected

    print("All tests passed!")

# Generated at 2026-11-02 16:46:40.800264
# Unit test for function special_factorial
def test_special_factorial():
    # Test with n = 4: 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    assert module_0.special_factorial(4) == 288

    # Test with n = 1: only 1! = 1
    assert module_0.special_factorial(1) == 1

    # Test with n = 0: product of empty sequence, stays at initial 1
    assert module_0.special_factorial(0) == 1

    # Test with n = 2: 2! * 1! = 2
    assert module_0.special_factorial(2) == 2

    # Test with n = 3: 3! * 2! * 1! = 6 * 2 * 1 = 12
    assert module_0.special_factorial(3) == 12

    # Test with n = 5: 5! * 4! * 3! * 2! * 1! = 120 * 24 * 6 * 2 * 1 = 34560
    assert module_0.special_factorial(5) == 34560

    # Verify multiplicative recurrence: f(n) = f(n-1) * n!
    import math
    n = 7
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert module_0.special_factorial(n) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_special_factorial()
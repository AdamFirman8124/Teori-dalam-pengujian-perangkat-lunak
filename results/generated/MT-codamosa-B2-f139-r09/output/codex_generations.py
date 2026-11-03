

# Generated at 2026-11-02 21:07:18.297917
# Unit test for function special_factorial
def test_special_factorial():
    # Test case 1: module_0.special_factorial(4) should be 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288, "Test case 1 failed"

    # Test case 2: module_0.special_factorial(1) should be 1! = 1
    assert module_0.special_factorial(1) == 1, "Test case 2 failed"

    # Test case 3: module_0.special_factorial(2) should be 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2, "Test case 3 failed"

    # Test case 4: module_0.special_factorial(3) should be 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12, "Test case 4 failed"

    # Test case 5: module_0.special_factorial(5) should be 1! * 2! * 3! * 4! * 5! = 1 * 2 * 6 * 24 * 120 = 34560
    assert module_0.special_factorial(5) == 34560, "Test case 5 failed"

    # Test case 6: module_0.special_factorial(0) — empty loop, should return 1
    assert module_0.special_factorial(0) == 1, "Test case 6 failed"

    print("All test cases passed!")

# Run the test
test_special_factorial()
# nonce:7280cdd9

# Generated at 2026-11-02 21:08:26.069294
# Unit test for function special_factorial
def test_special_factorial():
    # n = 1: 1! = 1
    assert module_0.special_factorial(1) == 1
    # n = 2: 2! * 1! = 2
    assert module_0.special_factorial(2) == 2
    # n = 3: 3! * 2! * 1! = 12
    assert module_0.special_factorial(3) == 12
    # n = 4: 4! * 3! * 2! * 1! = 288
    assert module_0.special_factorial(4) == 288
    # n = 5: 5! * 4! * 3! * 2! * 1! = 34560
    assert module_0.special_factorial(5) == 34560
    # n = 6: 720 * 120 * 24 * 6 * 2 * 1 = 24883200
    assert module_0.special_factorial(6) == 24883200
    # Larger value: product of factorials 1! through 8!
    assert module_0.special_factorial(8) == 50565841728
    print("All tests passed!")

# nonce:def1c80d

# Generated at 2026-11-02 21:08:50.415514
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

    # Test with n = 5: 1 * 2 * 6 * 24 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Test with n = 0: loop does not execute, returns 1
    assert module_0.special_factorial(0) == 1

    # Test with a larger value
    assert module_0.special_factorial(6) == 34560 * 720

    print("All tests passed!")


# Run the tests
test_special_factorial()

# Generated at 2026-11-02 21:09:14.377262
# Unit test for function special_factorial
def test_special_factorial():
    # nonce:cf4da281
    # Brazilian factorial: n! * (n-1)! * ... * 1!
    assert module_0.special_factorial(4) == 288       # 1! * 2! * 3! * 4! = 1*2*6*24
    assert module_0.special_factorial(5) == 34560     # 288 * 5! = 288 * 120
    assert module_0.special_factorial(3) == 12        # 1! * 2! * 3! = 1*2*6
    assert module_0.special_factorial(2) == 2         # 1! * 2! = 2
    assert module_0.special_factorial(1) == 1         # 1!
    assert module_0.special_factorial(0) == 1         # empty product edge case
    assert isinstance(module_0.special_factorial(6), int)

test_special_factorial()
print("All tests passed!")

# Generated at 2026-11-02 21:09:44.823698
# Unit test for function special_factorial
def test_special_factorial():
    # module_0.special_factorial(n) = 1! * 2! * ... * n! (Brazilian factorial)
    # Base cases
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1

    # Known values
    assert module_0.special_factorial(2) == 2          # 1! * 2!
    assert module_0.special_factorial(3) == 12         # 1! * 2! * 3!
    assert module_0.special_factorial(4) == 288        # 1! * 2! * 3! * 4!
    assert module_0.special_factorial(5) == 34560      # 1! * 2! * ... * 5!

    # Verify against independent computation for a range of inputs
    for n in range(0, 11):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"Failed for n={n}"


# Generated at 2026-10-25 14:16:03.711210
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1      # 1! = 1
    assert module_0.special_factorial(2) == 2      # 1! * 2! = 1 * 2
    assert module_0.special_factorial(3) == 12     # 2 * 3! = 2 * 6
    assert module_0.special_factorial(4) == 288    # 12 * 4! = 12 * 24
    assert module_0.special_factorial(5) == 34560  # 288 * 5! = 288 * 120

# Generated at 2026-10-25 14:16:10.572589
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12       # 1! Ã 2! Ã 3!
    assert module_0.special_factorial(4) == 288      # 1! Ã 2! Ã 3! Ã 4!
    assert module_0.special_factorial(5) == 34560

# Generated at 2026-10-25 14:16:16.818051
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560

# Generated at 2026-10-25 14:16:24.745065
# Unit test for function special_factorial
def test_special_factorial():
    # Base cases
    assert module_0.special_factorial(0) == 1, "module_0.special_factorial(0) should be 1 (empty product)"
    assert module_0.special_factorial(1) == 1, "module_0.special_factorial(1) should be 1 (= 1!)"

    # Known values: product of i! for i = 1..n
    # n=2: 1! * 2! = 1 * 2 = 2
    assert module_0.special_factorial(2) == 2
    # n=3: 1! * 2! * 3! = 1 * 2 * 6 = 12
    assert module_0.special_factorial(3) == 12
    # n=4: 1 * 2 * 6 * 24 = 288
    assert module_0.special_factorial(4) == 288
    # n=5: 288 * 120 = 34560
    assert module_0.special_factorial(5) == 34560

    # Cross-check against a direct (slow) computation
    import math
    for n in range(6, 11):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected, f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_special_factorial()

# Generated at 2026-10-25 14:16:41.188853
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2       # 1! * 2!
    assert module_0.special_factorial(3) == 12      # 1! * 2! * 3!
    assert module_0.special_factorial(4) == 288     # 1! * 2! * 3! * 4!
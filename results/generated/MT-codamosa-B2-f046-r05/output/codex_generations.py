

# Generated at 2026-11-02 14:10:19.679058
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed cases
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Larger value
    assert module_0.fib4(15) == 1906

    # Verify recurrence: each term is sum of previous four
    seq = [module_0.fib4(i) for i in range(4, 12)]
    for i in range(4, len(seq)):
        assert seq[i] == seq[i - 1] + seq[i - 2] + seq[i - 3] + seq[i - 4]

    print("All fib4 tests passed!")


test_fib4()

# Generated at 2026-11-02 14:11:50.289713
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed values: module_0.fib4(n) = module_0.fib4(n-1) + module_0.fib4(n-2) + module_0.fib4(n-3) + module_0.fib4(n-4)
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104
    assert module_0.fib4(11) == 200
    assert module_0.fib4(12) == 386

# Generated at 2026-11-02 14:13:40.607274
# Unit test for function fib4
def test_fib4():
    # Test base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Test computed cases
    assert module_0.fib4(4) == 2    # 0 + 2 + 0 + 0
    assert module_0.fib4(5) == 4    # 2 + 0 + 2 + 0
    assert module_0.fib4(6) == 8    # 4 + 2 + 0 + 2
    assert module_0.fib4(7) == 14   # 8 + 4 + 2 + 0
    assert module_0.fib4(8) == 28   # 14 + 8 + 4 + 2
    assert module_0.fib4(9) == 54   # 28 + 14 + 8 + 4
    assert module_0.fib4(10) == 104 # 54 + 28 + 14 + 8

    # Test a larger value
    assert module_0.fib4(15) == 2036

    print("All tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 14:15:26.713584
# Unit test for function fib4
def test_fib4():
    # Base cases: n < 4 returns from the initial results list
    assert module_0.fib4(0) == 0, "module_0.fib4(0) should be 0"
    assert module_0.fib4(1) == 0, "module_0.fib4(1) should be 0"
    assert module_0.fib4(2) == 2, "module_0.fib4(2) should be 2"
    assert module_0.fib4(3) == 0, "module_0.fib4(3) should be 0"

    # Computed cases using the 4-element sliding window recurrence
    assert module_0.fib4(4) == 2, "module_0.fib4(4) should be 2"
    assert module_0.fib4(5) == 4, "module_0.fib4(5) should be 4"
    assert module_0.fib4(6) == 8, "module_0.fib4(6) should be 8"
    assert module_0.fib4(7) == 14, "module_0.fib4(7) should be 14"
    assert module_0.fib4(8) == 28, "module_0.fib4(8) should be 28"
    assert module_0.fib4(9) == 54, "module_0.fib4(9) should be 54"
    assert module_0.fib4(10) == 104, "module_0.fib4(10) should be 104"

    # Larger input to exercise the loop multiple times
    assert module_0.fib4(15) == 1490, "module_0.fib4(15) should be 1490"

    print("All tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 14:16:55.494290
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed values of the Fib4 sequence
    assert module_0.fib4(4) == 2    # 0+0+2+0
    assert module_0.fib4(5) == 4    # 2+0+0+2
    assert module_0.fib4(6) == 6
    assert module_0.fib4(7) == 12
    assert module_0.fib4(8) == 24
    assert module_0.fib4(9) == 46
    assert module_0.fib4(10) == 88
    assert module_0.fib4(11) == 170
    assert module_0.fib4(12) == 328

    # Larger value to verify iterative accumulation
    assert module_0.fib4(15) == 2348
    assert module_0.fib4(20) == 104308

    # Consistency: recurrence relation holds
    n = 25
    assert module_0.fib4(n) == module_0.fib4(n - 1) + module_0.fib4(n - 2) + module_0.fib4(n - 3) + module_0.fib4(n - 4)
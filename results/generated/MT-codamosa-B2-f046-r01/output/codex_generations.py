

# Generated at 2026-11-02 00:41:04.069215
# Unit test for function fib4
def test_fib4():
    # Test base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Test computed values
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Test a larger value
    assert module_0.fib4(15) == 1080

    print("All tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 00:42:14.781346
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed values from the recurrence module_0.fib4(n) = module_0.fib4(n-1)+module_0.fib4(n-2)+module_0.fib4(n-3)+module_0.fib4(n-4)
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104
    assert module_0.fib4(11) == 200
    assert module_0.fib4(12) == 386
    assert module_0.fib4(15) == 2764

# Generated at 2026-11-02 00:43:45.964960
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Iterative cases
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Larger value to verify recurrence and sliding window logic
    assert module_0.fib4(15) == 1436

    print("All test_fib4 tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 00:45:14.744649
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # First few computed values
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Larger value
    assert module_0.fib4(20) == 73552

    # Verify recurrence: each term is sum of previous four terms
    for n in range(4, 15):
        assert module_0.fib4(n) == module_0.fib4(n - 1) + module_0.fib4(n - 2) + module_0.fib4(n - 3) + module_0.fib4(n - 4)

    print("All tests passed!")

# Generated at 2026-11-02 00:46:14.753617
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Iterative cases (n >= 4)
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104
    assert module_0.fib4(11) == 200
    assert module_0.fib4(12) == 386
    assert module_0.fib4(15) == 2764

    # Larger input to verify iterative correctness
    assert module_0.fib4(20) == 73552

    print("All fib4 tests passed!")


if __name__ == "__main__":
    test_fib4()


# Generated at 2026-11-02 13:06:28.669838
# Unit test for function fib
def test_fib():
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765
    print("All tests passed!")


test_fib()

# Generated at 2026-11-02 13:09:14.885011
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Standard Fibonacci sequence values
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55

    # Larger values
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Verify recurrence relation holds
    n = 12
    assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

# Generated at 2026-11-02 13:10:32.704320
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Small values
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5

    # Larger values
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Cross-check against an iterative reference implementation
    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    for n in range(25):
        assert module_0.fib(n) == fib_iter(n), f"module_0.fib({n}) mismatch"

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 13:11:38.205362
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0, "module_0.fib(0) should be 0"
    assert module_0.fib(1) == 1, "module_0.fib(1) should be 1"

    # Known Fibonacci values
    assert module_0.fib(2) == 1, "module_0.fib(2) should be 1"
    assert module_0.fib(3) == 2, "module_0.fib(3) should be 2"
    assert module_0.fib(4) == 3, "module_0.fib(4) should be 3"
    assert module_0.fib(5) == 5, "module_0.fib(5) should be 5"
    assert module_0.fib(6) == 8, "module_0.fib(6) should be 8"
    assert module_0.fib(7) == 13, "module_0.fib(7) should be 13"
    assert module_0.fib(10) == 55, "module_0.fib(10) should be 55"
    assert module_0.fib(15) == 610, "module_0.fib(15) should be 610"
    assert module_0.fib(20) == 6765, "module_0.fib(20) should be 6765"

    # Cross-check consistency: module_0.fib(n) == module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2), f"Recurrence failed at n={n}"

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 13:12:51.135610
# Unit test for function fib
def test_fib():
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    print("All tests passed!")
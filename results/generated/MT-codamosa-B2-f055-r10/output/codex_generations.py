

# Generated at 2026-11-02 16:01:29.390349
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
    assert module_0.fib(20) == 6765

# Generated at 2026-11-02 16:04:19.563790
# Unit test for function fib
def test_fib():
# nonce:86832a25
    # Base cases
    assert module_0.fib(0) == 0, "module_0.fib(0) should be 0"
    assert module_0.fib(1) == 1, "module_0.fib(1) should be 1"

    # Standard cases
    assert module_0.fib(2) == 1, "module_0.fib(2) should be 1"
    assert module_0.fib(3) == 2, "module_0.fib(3) should be 2"
    assert module_0.fib(4) == 3, "module_0.fib(4) should be 3"
    assert module_0.fib(5) == 5, "module_0.fib(5) should be 5"
    assert module_0.fib(6) == 8, "module_0.fib(6) should be 8"
    assert module_0.fib(7) == 13, "module_0.fib(7) should be 13"
    assert module_0.fib(10) == 55, "module_0.fib(10) should be 55"
    assert module_0.fib(15) == 610, "module_0.fib(15) should be 610"

    # Recursive property check: module_0.fib(n) == module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2), f"module_0.fib({n}) violates recurrence"

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 16:05:25.811743
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Standard Fibonacci values
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55

    # Larger value to verify recursion
    assert module_0.fib(15) == 610

    print("All tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 16:06:50.247676
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Known Fibonacci values
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55

    # Larger value
    assert module_0.fib(20) == 6765

    # Verify recurrence relation holds for a sample of values
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    # Type check: results should be integers
    assert isinstance(module_0.fib(7), int)

    print("All fib tests passed!")

# Generated at 2026-11-02 16:08:33.692142
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0, "module_0.fib(0) should be 0"
    assert module_0.fib(1) == 1, "module_0.fib(1) should be 1"

    # Recursive cases
    assert module_0.fib(2) == 1, "module_0.fib(2) should be 1"
    assert module_0.fib(3) == 2, "module_0.fib(3) should be 2"
    assert module_0.fib(4) == 3, "module_0.fib(4) should be 3"
    assert module_0.fib(5) == 5, "module_0.fib(5) should be 5"
    assert module_0.fib(6) == 8, "module_0.fib(6) should be 8"
    assert module_0.fib(7) == 13, "module_0.fib(7) should be 13"
    assert module_0.fib(10) == 55, "module_0.fib(10) should be 55"
    assert module_0.fib(15) == 610, "module_0.fib(15) should be 610"
    assert module_0.fib(20) == 6765, "module_0.fib(20) should be 6765"

    # Verify recurrence relation holds for a range of values
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2), (
            f"module_0.fib({n}) should equal module_0.fib({n-1}) + module_0.fib({n-2})"
        )

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()


# Generated at 2026-11-02 14:47:57.863509
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0, "module_0.fib(0) should be 0"
    assert module_0.fib(1) == 1, "module_0.fib(1) should be 1"

    # Standard Fibonacci values
    assert module_0.fib(2) == 1, "module_0.fib(2) should be 1"
    assert module_0.fib(3) == 2, "module_0.fib(3) should be 2"
    assert module_0.fib(4) == 3, "module_0.fib(4) should be 3"
    assert module_0.fib(5) == 5, "module_0.fib(5) should be 5"
    assert module_0.fib(6) == 8, "module_0.fib(6) should be 8"
    assert module_0.fib(7) == 13, "module_0.fib(7) should be 13"
    assert module_0.fib(10) == 55, "module_0.fib(10) should be 55"

    # Larger value
    assert module_0.fib(20) == 6765, "module_0.fib(20) should be 6765"

    # Recurrence relation property: module_0.fib(n) = module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2), (
            f"module_0.fib({n}) should equal module_0.fib({n-1}) + module_0.fib({n-2})"
        )

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 14:49:38.693775
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
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13

    # Larger values
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()

# Generated at 2026-11-02 14:51:34.098388
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Recursive cases
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Verify recurrence relation holds for a range of values
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    # Verify result types
    assert isinstance(module_0.fib(0), int)
    assert isinstance(module_0.fib(10), int)

# Generated at 2026-11-02 14:53:32.124919
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Known Fibonacci sequence values
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, value in enumerate(expected):
        assert module_0.fib(i) == value, f"module_0.fib({i}) should be {value}, got {module_0.fib(i)}"

    # Larger values
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

# Generated at 2026-11-02 14:54:52.352023
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

    # Verify sequence consistency: module_0.fib(n) == module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    print("All fib tests passed!")
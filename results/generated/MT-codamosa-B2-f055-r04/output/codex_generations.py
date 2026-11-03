

# Generated at 2026-11-02 15:50:12.129109
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

# Generated at 2026-11-02 15:52:02.003413
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
    print("All test cases passed!")

# Generated at 2026-11-02 15:54:38.516709
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1

    # Typical values
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Property check: F(n) = F(n-1) + F(n-2)
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    # Verify first several terms against known sequence
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, value in enumerate(expected):
        assert module_0.fib(i) == value, f"module_0.fib({i}) should be {value}, got {module_0.fib(i)}"

# Generated at 2026-11-02 15:56:57.941477
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

    # Larger value
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    print("All test_fib tests passed!")


test_fib()

# Generated at 2026-11-02 15:57:59.346879
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
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55

    # Larger values
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Verify recurrence relation holds for a range of values
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    # Return type check
    assert isinstance(module_0.fib(10), int)
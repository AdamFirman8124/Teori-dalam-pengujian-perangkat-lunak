

# Generated at 2026-11-03 04:46:45.221600
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
    assert module_0.fib(10) == 55

    # Larger values
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765
    assert module_0.fib(25) == 75025


def test_fib_base_cases():
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1


def test_fib_known_values():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, value in enumerate(expected):
        assert module_0.fib(i) == value


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (12, 144),
])
def test_fib_parametrized(n, expected):
    assert module_0.fib(n) == expected


def test_fib_recurrence_property():
    # module_0.fib(n) should equal module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)


def test_fib_return_type():
    result = module_0.fib(10)
    assert isinstance(result, int)

# Generated at 2026-11-03 04:50:19.994504
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

    # Consistency: recurrence relation holds
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)

    print("All tests passed!")

# Generated at 2026-11-03 04:52:15.054601
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
    assert module_0.fib(10) == 55
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765

    # Verify a few values against an iterative reference
    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    for n in range(0, 15):
        assert module_0.fib(n) == fib_iter(n), f"Mismatch at n={n}"

    print("All fib tests passed!")


if __name__ == "__main__":
    test_fib()
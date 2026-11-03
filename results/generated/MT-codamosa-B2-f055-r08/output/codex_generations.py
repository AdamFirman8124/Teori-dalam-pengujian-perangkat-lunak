

# Generated at 2026-11-02 12:07:29.279923
# Unit test for function fib
def test_fib():
    # Base cases
    assert module_0.fib(0) == 0, "module_0.fib(0) should be 0"
    assert module_0.fib(1) == 1, "module_0.fib(1) should be 1"

    # Simple known values
    assert module_0.fib(2) == 1, "module_0.fib(2) should be 1"
    assert module_0.fib(3) == 2, "module_0.fib(3) should be 2"
    assert module_0.fib(4) == 3, "module_0.fib(4) should be 3"
    assert module_0.fib(5) == 5, "module_0.fib(5) should be 5"

    # Larger known values
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

# Generated at 2026-11-02 12:08:31.095640
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

    # Check return type
    assert isinstance(module_0.fib(10), int)


def test_fib_base_cases():
    assert module_0.fib(0) == 0
    assert module_0.fib(1) == 1


def test_fib_sequence():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    actual = [module_0.fib(i) for i in range(11)]
    assert actual == expected


def test_fib_recursive_property():
    # module_0.fib(n) == module_0.fib(n-1) + module_0.fib(n-2) for n >= 2
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)


def test_fib_negative_raises():
    with pytest.raises(RecursionError):
        module_0.fib(-1)

# Generated at 2026-11-02 12:10:20.155971
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

    # Verify Fibonacci property: module_0.fib(n) == module_0.fib(n-1) + module_0.fib(n-2)
    for n in range(2, 15):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)


@pytest.mark.parametrize("n, expected", [
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
])
def test_fib_parametrized(n, expected):
    assert module_0.fib(n) == expected

# Generated at 2026-11-02 12:12:21.702338
# Unit test for function fib
def test_fib():import pytest


def test_fib_base_case_zero():
    assert module_0.fib(0) == 0


def test_fib_base_case_one():
    assert module_0.fib(1) == 1


def test_fib_small_values():
    assert module_0.fib(2) == 1
    assert module_0.fib(3) == 2
    assert module_0.fib(4) == 3
    assert module_0.fib(5) == 5


def test_fib_known_values():
    assert module_0.fib(6) == 8
    assert module_0.fib(7) == 13
    assert module_0.fib(8) == 21
    assert module_0.fib(9) == 34
    assert module_0.fib(10) == 55


def test_fib_larger_value():
    assert module_0.fib(15) == 610
    assert module_0.fib(20) == 6765


def test_fib_recurrence_property():
    for n in range(2, 12):
        assert module_0.fib(n) == module_0.fib(n - 1) + module_0.fib(n - 2)


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
])
def test_fib_parametrized(n, expected):
    assert module_0.fib(n) == expected


def test_fib_returns_int():
    result = module_0.fib(7)
    assert isinstance(result, int)


def test_fib_monotonically_nondecreasing():
    values = [module_0.fib(n) for n in range(11)]
    assert values == sorted(values)


def test_fib_matches_iterative_reference():
    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    for n in range(15):
        assert module_0.fib(n) == fib_iter(n)

# Generated at 2026-11-02 12:13:34.109072
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
    
    # Larger value
    assert module_0.fib(20) == 6765
    
    print("All tests passed!")
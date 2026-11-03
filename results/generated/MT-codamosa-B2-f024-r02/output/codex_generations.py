

# Generated at 2026-11-02 00:41:50.736041
# Unit test for function largest_divisor
def test_largest_divisor():
    # Canonical cases
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7

    # Additional standard cases
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(28) == 14
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(81) == 27
    assert module_0.largest_divisor(97) == 1        # prime -> 1 is the only proper divisor
    assert module_0.largest_divisor(7919) == 1      # large prime
    assert module_0.largest_divisor(1000000) == 500000

    # Property: result is always a proper divisor of n (1 <= d < n)
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert 1 <= d < n
        assert n % d == 0

    # Return type check
    assert isinstance(module_0.largest_divisor(10), int)

    # Edge cases: non-positive inputs yield an empty loop -> implicit None
    assert module_0.largest_divisor(0) is None
    assert module_0.largest_divisor(-5) is None

    # n == 1 reaches i == 0 in the loop and raises ZeroDivisionError
    try:
        module_0.largest_divisor(1)
        raised = False
    except ZeroDivisionError:
        raised = True
    assert raised, "module_0.largest_divisor(1) should raise ZeroDivisionError"

# Generated at 2026-11-02 00:42:53.328604
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(1) == 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(5) == 1
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(28) == 14

    # Prime numbers should return 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(11) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Perfect squares - largest proper divisor is sqrt(n)
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(25) == 5
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(100) == 50

    # Powers of two
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(16) == 8
    assert module_0.largest_divisor(32) == 16
    assert module_0.largest_divisor(64) == 32

    # Larger composite numbers
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(60) == 30
    assert module_0.largest_divisor(360) == 180
    assert module_0.largest_divisor(1024) == 512

    # Verify property: result divides n and is less than n
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert n % d == 0
        assert 1 <= d < n

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 00:44:26.102617
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic composite numbers
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(4) == 2

    # Prime numbers: largest divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Perfect squares
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(81) == 27

    # Powers of two
    assert module_0.largest_divisor(16) == 8
    assert module_0.largest_divisor(64) == 32

    # Larger values
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(360) == 180

    # Large prime
    assert module_0.largest_divisor(7919) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 00:45:53.887515
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7

    # Prime numbers: largest divisor below n is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Squares of primes
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(25) == 5

    # Property-based checks: result divides n, is < n, and is maximal
    for n in range(2, 300):
        d = module_0.largest_divisor(n)
        assert n % d == 0, f"{d} does not divide {n}"
        assert d < n, f"{d} is not less than {n}"
        assert all(n % k != 0 for k in range(d + 1, n)), \
            f"found a larger divisor of {n} than {d}"

# Generated at 2026-11-02 00:47:34.415693
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(101) == 1
    assert module_0.largest_divisor(2) == 1

# Generated at 2026-11-02 00:48:53.206548
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers: largest proper divisor
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(6) == 3

    # Smallest case with a valid result
    assert module_0.largest_divisor(2) == 1

    # Prime numbers: largest proper divisor is 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Large value
    assert module_0.largest_divisor(1000000) == 500000
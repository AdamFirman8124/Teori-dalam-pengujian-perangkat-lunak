

# Generated at 2026-11-02 19:05:32.630483
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic composite numbers
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50

    # Prime numbers -> largest divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(97) == 1

    # Powers of two
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(64) == 32

    # Perfect squares
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(25) == 5
    assert module_0.largest_divisor(49) == 7

    # Even numbers
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(14) == 7
    assert module_0.largest_divisor(28) == 14

    # Larger numbers
    assert module_0.largest_divisor(1000000) == 500000
    assert module_0.largest_divisor(999983) == 1  # prime

    # Verify result divides n and is the largest below n
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert n % d == 0
        assert d < n
        assert all(n % i != 0 for i in range(d + 1, n))

# Generated at 2026-11-02 19:06:48.079577
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(7) == 1       # prime number -> only divisor below n is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7      # perfect square of a prime
    assert module_0.largest_divisor(1) is None    # range is empty, loop never executes
    assert module_0.largest_divisor(1000000) == 500000

# Generated at 2026-11-02 19:09:00.485477
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50

    # Smallest valid input
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(3) == 1

    # Prime numbers: largest divisor less than n is 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(29) == 1

    # Powers of two
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(64) == 32

    # Even numbers
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(20) == 10

    # Odd composite numbers
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(21) == 7
    assert module_0.largest_divisor(49) == 7

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 19:10:54.801749
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5

    # Prime numbers -> largest proper divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    assert module_0.largest_divisor(29) == 1

    # Powers of two
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(8) == 4
    assert module_0.largest_divisor(16) == 8

    # Perfect squares of primes
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(25) == 5
    assert module_0.largest_divisor(49) == 7

    # Even / composite numbers
    assert module_0.largest_divisor(6) == 3
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(21) == 7
    assert module_0.largest_divisor(35) == 7
    assert module_0.largest_divisor(100) == 50

    # Large number
    assert module_0.largest_divisor(1_000_000) == 500_000

    # Verify result actually divides n and is less than n
    for n in range(2, 200):
        d = module_0.largest_divisor(n)
        assert n % d == 0
        assert d < n

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 19:13:56.536423
# Unit test for function largest_divisor
def test_largest_divisor():
    # Basic cases
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7

    # Smallest valid input
    assert module_0.largest_divisor(2) == 1

    # Even numbers: largest proper divisor is n // 2
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(48) == 24
    assert module_0.largest_divisor(1000) == 500

    # Prime numbers: only proper divisor is 1
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97, 101]:
        assert module_0.largest_divisor(p) == 1

    # Composite numbers
    assert module_0.largest_divisor(9) == 3
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(21) == 7
    assert module_0.largest_divisor(25) == 5
    assert module_0.largest_divisor(105) == 35

    # Property checks: result divides n, is a proper divisor, and is the largest one
    for n in range(2, 300):
        d = module_0.largest_divisor(n)
        assert n % d == 0, f"{d} does not divide {n}"
        assert 1 <= d < n, f"result {d} out of valid range for {n}"
        for k in range(d + 1, n):
            assert n % k != 0, f"found larger divisor {k} of {n} (expected {d})"

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()
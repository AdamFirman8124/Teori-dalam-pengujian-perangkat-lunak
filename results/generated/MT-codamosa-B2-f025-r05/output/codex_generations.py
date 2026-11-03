

# Generated at 2026-11-02 00:10:43.683731
# Unit test for function factorize
def test_factorize():
    # Trivial cases
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]

    # Prime powers
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(64) == [2, 2, 2, 2, 2, 2]
    assert module_0.factorize(1024) == [2] * 10

    # Composites with mixed/distinct primes
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]

    # Larger primes and composites
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(600851475143) == [71, 839, 1471, 6857]

    # Property-based checks: product reconstructs n, factors sorted, all >= 2
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        d = 2
        while d * d <= k:
            if k % d == 0:
                return False
            d += 1
        return True

    for n in range(1, 1000):
        factors = module_0.factorize(n)
        product = 1
        for f in factors:
            assert f >= 2
            assert is_prime(f), f"factors of {n} must be prime, got {f}"
            product *= f
        assert product == n, f"product of factors of {n} mismatched"
        assert factors == sorted(factors), f"factors of {n} not in non-decreasing order"

    print("All factorize tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 00:11:29.765240
# Unit test for function factorize
def test_factorize():assert module_0.factorize(8) == [2, 2, 2]

# Generated at 2026-11-02 00:12:33.764404
# Unit test for function factorize
def test_factorize():
    # Test prime factorization of small numbers
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]

    # Test a prime number
    assert module_0.factorize(13) == [13]

    # Test perfect square of a prime
    assert module_0.factorize(25) == [5, 5]

    # Test composite with multiple distinct primes
    assert module_0.factorize(70) == [2, 5, 7]

    # Test larger composite number
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]

    # Test edge case: 1 has no prime factors
    assert module_0.factorize(1) == []

    # Property-based checks: product of factors equals original number
    for n in [12, 97, 100, 1024, 9999]:
        product = 1
        for f in module_0.factorize(n):
            product *= f
        assert product == n

    # All returned factors should be prime (>= 2)
    for n in [2, 36, 101, 7919]:
        for f in module_0.factorize(n):
            assert f >= 2
            # verify f is prime: no divisor between 2 and f-1
            for d in range(2, f):
                assert f % d != 0

    print("All tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 00:13:35.719576
# Unit test for function factorize
def test_factorize():
    # Basic factorizations
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(30) == [2, 3, 5]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10

    # Prime numbers factor to themselves
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(999983) == [999983]

    # Edge cases
    assert module_0.factorize(1) == []    # 1 has no prime factors
    assert module_0.factorize(0) == []    # loop never runs for 0

    # Negative input raises ValueError (from math.sqrt)
    try:
        module_0.factorize(-4)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass

    # Product of returned factors must reconstruct the original number
    for n in [2, 3, 4, 6, 12, 97, 100, 360, 2310, 1024, 999983, 2 ** 20]:
        product = 1
        for f in module_0.factorize(n):
            product *= f
        assert product == n, f"product of factors of {n} != {n}"

    # Every returned factor must itself be prime
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for d in range(2, int(k ** 0.5) + 1):
            if k % d == 0:
                return False
        return True

    for n in [2, 12, 360, 2310, 999983]:
        assert all(is_prime(f) for f in module_0.factorize(n))

    print("All factorize tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 00:14:23.027862
# Unit test for function factorize
def test_factorize():
    import math

    # Test basic factorizations
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]

    # Test prime numbers (only factor is the number itself)
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(7919) == [7919]  # large prime

    # Test edge cases
    assert module_0.factorize(1) == []  # 1 has no prime factors

    # Test numbers with large prime factors
    assert module_0.factorize(2 * 3 * 997) == [2, 3, 997]
    assert module_0.factorize(104729) == [104729]  # 10000th prime

    # Test product of factors equals original number
    for num in [12, 15, 99, 1000, 6469693230]:
        assert math.prod(module_0.factorize(num)) == num

    # Test factors are returned in non-decreasing order
    for num in [12, 15, 99, 1000, 360, 2 * 2 * 2 * 7 * 7]:
        factors = module_0.factorize(num)
        assert factors == sorted(factors)

    # Test all returned factors are prime
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for d in range(2, int(math.sqrt(k)) + 1):
            if k % d == 0:
                return False
        return True

    for num in [8, 70, 360, 1000, 999983]:
        for f in module_0.factorize(num):
            assert is_prime(f), f"{f} is not prime for input {num}"

    print("All tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 00:15:24.881172
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(210) == [2, 3, 5, 7]
    assert module_0.factorize(101) == [101]

# Generated at 2026-11-02 00:16:29.080590
# Unit test for function factorize
def test_factorize():
    # Small primes
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(7) == [7]

    # Powers of a single prime
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(1024) == [2] * 10

    # Composites with several distinct primes
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(30) == [2, 3, 5]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]

    # Large prime: remaining n must be appended after the loop
    assert module_0.factorize(7919) == [7919]

    # Edge case: 1 has no prime factors
    assert module_0.factorize(1) == []

    # Property checks: factors multiply back to n, are sorted, and are prime
    import math
    for n in range(2, 300):
        factors = module_0.factorize(n)
        product = 1
        for f in factors:
            product *= f
        assert product == n, f"product of {factors} != {n}"
        assert factors == sorted(factors), f"factors of {n} not sorted: {factors}"
        for f in factors:
            assert f >= 2
            assert all(f % d != 0 for d in range(2, int(math.sqrt(f)) + 1)), \
                f"{f} is not prime (factor of {n})"
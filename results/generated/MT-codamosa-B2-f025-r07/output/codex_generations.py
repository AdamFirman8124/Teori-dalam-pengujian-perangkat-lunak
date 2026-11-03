

# Generated at 2026-11-02 15:36:33.712568
# Unit test for function factorize
def test_factorize():
    # Simple composite numbers with repeated factors
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]

    # Prime numbers return themselves
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(9973) == [9973]

    # 1 has no prime factors
    assert module_0.factorize(1) == []

    # Product of distinct small primes
    assert module_0.factorize(2 * 3 * 5 * 7 * 11) == [2, 3, 5, 7, 11]

    # Powers of two
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(2 ** 20) == [2] * 20

    # Larger composites
    assert module_0.factorize(2 * 2 * 13 * 13) == [2, 2, 13, 13]
    assert module_0.factorize(3 * 3 * 7 * 11 * 11) == [3, 3, 7, 11, 11]

    # Property-based checks: factors multiply back to n and are all prime
    for n in [4, 6, 9, 12, 30, 49, 128, 1023, 1024, 510510, 999983]:
        factors = module_0.factorize(n)
        product = 1
        for f in factors:
            product *= f
            assert all(f % d != 0 for d in range(2, int(f ** 0.5) + 1)), \
                f"{f} is not prime in factorization of {n}"
        assert product == n, f"Factors of {n} do not multiply back to n"

    print("All tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 15:37:29.606407
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(3 * 19) == [3, 19]
    assert module_0.factorize(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(1) == []
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(2 * 2 * 2 * 3 * 3 * 5 * 7) == [2, 2, 2, 3, 3, 5, 7]

# Generated at 2026-11-02 15:39:14.584946
# Unit test for function factorize
def test_factorize():
    # Edge cases
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]

    # Prime powers
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(1024) == [2] * 10

    # Composite numbers with distinct/mixed primes
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(30) == [2, 3, 5]
    assert module_0.factorize(91) == [7, 13]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]

    # Large primes
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(101) == [101]
    assert module_0.factorize(7919) == [7919]

    # Property checks: factors are prime, non-decreasing, and multiply to n
    for n in range(2, 500):
        factors = module_0.factorize(n)
        assert factors == sorted(factors)
        product = 1
        for f in factors:
            assert all(f % d != 0 for d in range(2, int(f ** 0.5) + 1)), \
                f"{f} is not prime (n={n})"
            product *= f
        assert product == n, f"product of factors of {n} != {n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_factorize()

# Generated at 2026-11-02 15:40:46.031135
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(2 * 3 * 5 * 7) == [2, 3, 5, 7]
    assert module_0.factorize(3 * 3 * 3) == [3, 3, 3]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(13 * 17) == [13, 17]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(999999) == [3, 3, 3, 7, 11, 13, 37]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(2147483647) == [2147483647]
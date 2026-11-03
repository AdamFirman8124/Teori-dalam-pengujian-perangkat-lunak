

# Generated at 2026-11-02 14:18:00.742701
# Unit test for function factorize
def test_factorize():
    # Single prime factors
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(97) == [97]

    # Powers of a prime
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(1024) == [2] * 10

    # Composite numbers with distinct/mixed primes
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(70) == [2, 5, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]

# Generated at 2026-11-02 14:20:58.284478
# Unit test for function factorize

# Generated at 2026-11-02 14:22:08.033737
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(1) == []
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(2 * 3 * 5 * 7) == [2, 3, 5, 7]

# Generated at 2026-11-02 14:23:58.737495
# Unit test for function factorize
def test_factorize():
    # nonce:fbfbacae
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(3 * 19) == [3, 19]
    assert module_0.factorize(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert module_0.factorize(1) == []
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(2 * 2 * 3 * 7) == [2, 2, 3, 7]
    assert module_0.factorize(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(999983) == [999983]  # large prime

    # Property check: product of factors equals n, and each factor is prime
    import math
    for n in range(2, 500):
        facts = module_0.factorize(n)
        prod = 1
        for f in facts:
            assert all(f % d != 0 for d in range(2, int(math.sqrt(f)) + 1)), f"{f} is not prime"
            prod *= f
        assert prod == n
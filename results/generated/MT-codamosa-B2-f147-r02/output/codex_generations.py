

# Generated at 2026-11-02 11:34:48.457973
# Unit test for function get_max_triples
def test_get_max_triples():
    import itertools

    # Edge cases: fewer than 3 elements means no triples possible
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7]: only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13]: only (1, 7, 13) -> 21 is divisible by 3
    assert module_0.get_max_triples(4) == 1

    # A = [1, 3, 7, 13, 21]: still only (1, 7, 13) works
    assert module_0.get_max_triples(5) == 1

    # A = [1, 3, 7, 13, 21, 31]: four triples of values ≡ 1 (mod 3)
    assert module_0.get_max_triples(6) == 4

    # Larger hand-verified counts (values ≡ 1 or 0 mod 3, pattern 1,0,1,1,0,...)
    assert module_0.get_max_triples(7) == 10   # C(5,3) ones + 0
    assert module_0.get_max_triples(8) == 11   # C(5,3) ones + C(3,3) zeros
    assert module_0.get_max_triples(9) == 21   # C(6,3) ones + C(3,3) zeros

    # Cross-check against an independent brute-force implementation
    def brute_force(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        return sum(1 for combo in itertools.combinations(A, 3)
                   if sum(combo) % 3 == 0)

    for n in range(0, 15):
        assert module_0.get_max_triples(n) == brute_force(n), f"Mismatch at n={n}"

    # Return value must be a non-negative integer
    result = module_0.get_max_triples(10)
    assert isinstance(result, int)
    assert result >= 0

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 11:37:09.878558
# Unit test for function get_max_triples
def test_get_max_triples():
    # Known values
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0   # (1, 3, 7) sums to 11, not divisible by 3
    assert module_0.get_max_triples(4) == 1   # (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1
    assert module_0.get_max_triples(6) == 4   # (1,7,13), (1,7,31), (1,13,31), (7,13,31)
    assert module_0.get_max_triples(10) == 36

    # Cross-check against an independent brute-force count
    from itertools import combinations
    for n in range(1, 13):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        expected = sum(1 for a, b, c in combinations(A, 3) if (a + b + c) % 3 == 0)
        assert module_0.get_max_triples(n) == expected

# Generated at 2026-11-02 11:40:53.757710
# Unit test for function get_max_triples
def test_get_max_triples():
    # A = [i*i - i + 1 for i in 1..n]
    # Counts triples (a,b,c) from A whose sum is divisible by 3

    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A = [1, 3, 7]; only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # n=5: A = [1, 3, 7, 13, 21]; still only (1, 7, 13)
    assert module_0.get_max_triples(5) == 1

    # n=6: A = [1, 3, 7, 13, 21, 31]; residue-1 values {1,7,13,31} give C(4,3)=4 triples
    assert module_0.get_max_triples(6) == 4

    # n=10: residues -> seven 1s, three 0s; C(7,3) + C(3,3) = 35 + 1 = 36
    assert module_0.get_max_triples(10) == 36

    # Larger case verified by brute-force cross-check
    n = 20
    A = [i * i - i + 1 for i in range(1, n + 1)]
    expected = sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
        if (A[i] + A[j] + A[k]) % 3 == 0
    )
    assert module_0.get_max_triples(n) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()
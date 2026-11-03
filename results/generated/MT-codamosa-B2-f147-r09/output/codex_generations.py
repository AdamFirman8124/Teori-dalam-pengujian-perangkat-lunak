

# Generated at 2026-11-02 00:08:48.711018
# Unit test for function get_max_triples
def test_get_max_triples():
    # A = [i*i - i + 1 for i in range(1, n+1)]
    # Triple count requires (A[i]+A[j]+A[k]) % 3 == 0

    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1,3,7]; only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13]; only (1,7,13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # Known example from the problem specification
    assert module_0.get_max_triples(5) == 1

    # n=6: A=[1,3,7,13,21,31]; valid triples:
    # (1,7,13)=21, (1,7,31)=39, (1,13,31)=45, (7,13,31)=51
    assert module_0.get_max_triples(6) == 4

    # n=7: 10 valid triples (none with i % 3 == 2 indices)
    assert module_0.get_max_triples(7) == 10

    # n=8: C(3,3) triples from {2,5,8} indices + C(5,3)=10 from the rest
    assert module_0.get_max_triples(8) == 11

    # Cross-check against a straightforward brute-force reimplementation
    def brute_force(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(1, 25):
        assert module_0.get_max_triples(n) == brute_force(n), f"Mismatch for n={n}"

# Generated at 2026-11-02 00:09:48.078754
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: not enough elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A = [1, 3, 7]; only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # Known example: n=5 -> A = [1, 3, 7, 13, 21]; only (1, 7, 13) works
    assert module_0.get_max_triples(5) == 1

    # n=6: A = [1, 3, 7, 13, 21, 31]
    # Values ≡1 mod 3: {1, 7, 13, 31} -> C(4,3) = 4 triples; ≡0 mod 3: {3, 21} insufficient
    assert module_0.get_max_triples(6) == 4

    # n=10: values ≡1 mod 3: {1,7,13,31,43,73,91} -> C(7,3)=35
    #        values ≡0 mod 3: {3,21,57} -> C(3,3)=1; total 36
    assert module_0.get_max_triples(10) == 36

    # Brute-force cross-check for a range of n values
    for n in range(1, 15):
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

# Generated at 2026-11-02 00:11:42.871344
# Unit test for function get_max_triples
def test_get_max_triples():assert module_0.get_max_triples(1) == 0

# Generated at 2026-11-02 00:12:45.949757
# Unit test for function get_max_triples
def test_get_max_triples():
    import itertools
    from math import comb

    # Known-value cases
    assert module_0.get_max_triples(1) == 0      # single element -> no triples possible
    assert module_0.get_max_triples(2) == 0      # two elements -> no triples possible
    assert module_0.get_max_triples(3) == 0      # 1 + 3 + 7 = 11, not divisible by 3
    assert module_0.get_max_triples(4) == 1      # only (1, 7, 13) works
    assert module_0.get_max_triples(5) == 1      # only (1, 7, 13) works
    assert module_0.get_max_triples(6) == 4      # combos of residues {0:2, 1:4} -> C(4,3)

    # Cross-check against an independent brute-force reference implementation
    def reference(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        return sum(1 for c in itertools.combinations(A, 3) if sum(c) % 3 == 0)

    for n in range(0, 20):
        assert module_0.get_max_triples(n) == reference(n), f"Mismatch at n={n}"

    # Sanity bounds: non-negative and cannot exceed total number of triples
    for n in range(0, 15):
        result = module_0.get_max_triples(n)
        assert 0 <= result <= comb(max(n, 0), 3), f"Out-of-bounds result at n={n}"

    # Larger input runs without error and stays within bounds
    big = module_0.get_max_triples(50)
    assert 0 <= big <= comb(50, 3)

    print("All tests passed.")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 00:13:45.837433
# Unit test for function get_max_triples
def test_get_max_triples():
    # A[i] = i*i - i + 1; count triples (i<j<k) where A[i]+A[j]+A[k] % 3 == 0
    # A values mod 3: i≡2 (mod 3) -> 0, otherwise -> 1
    # Valid triples: all three ≡ 1 mod 3, or all three ≡ 0 mod 3

    assert module_0.get_max_triples(1) == 0   # A=[1], no triples
    assert module_0.get_max_triples(2) == 0   # A=[1,3], no triples
    assert module_0.get_max_triples(3) == 0   # A=[1,3,7]: 1+3+7=11, not divisible by 3
    assert module_0.get_max_triples(4) == 1   # A=[1,3,7,13]: only (1,7,13) works
    assert module_0.get_max_triples(5) == 1   # A=[1,3,7,13,21]: only (1,7,13) works
    assert module_0.get_max_triples(6) == 4   # ones: {1,7,13,31} -> C(4,3)=4
    assert module_0.get_max_triples(7) == 10  # ones: 5 values -> C(5,3)=10
    assert module_0.get_max_triples(8) == 20  # ones: 6 values -> C(6,3)=20
    assert module_0.get_max_triples(9) == 35  # ones: 7 values -> C(7,3)=35
    assert module_0.get_max_triples(10) == 56 # ones: 8 values -> C(8,3)=56
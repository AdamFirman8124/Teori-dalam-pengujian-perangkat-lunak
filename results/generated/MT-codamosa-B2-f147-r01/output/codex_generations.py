

# Generated at 2026-11-03 04:10:44.487132
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13]; only (1,7,13) sums to 21 (divisible by 3)
    assert module_0.get_max_triples(4) == 1

    # n=5: A=[1,3,7,13,21]; only (1,7,13) sums to 21 (divisible by 3)
    assert module_0.get_max_triples(5) == 1

    # n=6: A=[1,3,7,13,21,31]; valid triples:
    # (1,7,13)=21, (1,7,31)=39, (1,13,31)=45, (7,13,31)=51
    assert module_0.get_max_triples(6) == 4

    # n=10: A=[1,3,7,13,21,31,43,57,73,91]
    # values ≡0 mod 3: {3,21,57} -> C(3,3)=1
    # values ≡1 mod 3: {1,7,13,31

# Generated at 2026-11-03 04:12:00.950530
# Unit test for function get_max_triples
def test_get_max_triples():
    # Too few elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A = [1, 3, 7]; only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A = [1, 3, 7, 13]; (1, 7, 13) sums to 21 -> divisible by 3
    assert module_0.get_max_triples(4) == 1

    # Known example: n=5 -> 1
    assert module_0.get_max_triples(5) == 1

    # n=6: A = [1, 3, 7, 13, 21, 31]
    # Values mod 3: [1, 0, 1, 1, 0, 1]; only (1,1,1) combos work -> C(4,3) = 4
    assert module_0.get_max_triples(6) == 4

    # Result must never exceed total number of triples C(n, 3)
    from math import comb
    for n in range(1, 12):
        assert 0 <= module_0.get_max_triples(n) <= comb(n, 3)

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-03 04:13:13.456372
# Unit test for function get_max_triples
def test_get_max_triples():
    # nonce:39547798
    # Edge cases: fewer than 3 elements -> no triples possible
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # Small known values (A = [i*i - i + 1 for i in 1..n])
    assert module_0.get_max_triples(3) == 0   # A=[1,3,7], sum=11, not divisible by 3
    assert module_0.get_max_triples(4) == 1   # only (1,7,13) sums to 21
    assert module_0.get_max_triples(5) == 1   # A=[1,3,7,13,21], only (1,7,13)

    # Values verified via residue-class counting:
    # n=6: residues [1,0,1,1,0,1] -> C(4,3)=4 triples of residue 1
    assert module_0.get_max_triples(6) == 4
    # n=10: residues -> seven 1s and three 0s -> C(7,3)+C(3,3)=35+1=36
    assert module_0.get_max_triples(10) == 36

    # Cross-check against an independent brute-force count
    def brute(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        m = len(A)
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(0, 15):
        assert module_0.get_max_triples(n) == brute(n), f"Mismatch for n={n}"

    # Result must always be a non-negative integer
    for n in range(0, 12):
        result = module_0.get_max_triples(n)
        assert isinstance(result, int) and result >= 0

# Generated at 2026-11-03 04:14:46.290848
# Unit test for function get_max_triples
def test_get_max_triples():
    from math import comb

    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # Small known cases (hand-verified)
    # n=3: A=[1,3,7], sum=11 -> not divisible by 3
    assert module_0.get_max_triples(3) == 0
    # n=4: A=[1,3,7,13], only (1,7,13) sums to 21
    assert module_0.get_max_triples(4) == 1
    # n=5: A=[1,3,7,13,21], only (1,7,13)
    assert module_0.get_max_triples(5) == 1
    # n=6: ones at i=1,3,4,6; C(4,3)=4 triples of 1-mod-3 values
    assert module_0.get_max_triples(6) == 4
    # n=7: C(5,3)=10
    assert module_0.get_max_triples(7) == 10
    # n=8: C(5,3) + C(3,3) = 10 + 1 = 11
    assert module_0.get_max_triples(8) == 11
    # n=9: C(6,3) + C(3,3) = 20 + 1 = 21
    assert module_0.get_max_triples(9) == 21
    # n=10: C(7,3) + C(3,3) = 35 + 1 = 36
    assert module_0.get_max_triples(10) == 36

    # Property check: i*i - i + 1 is 1 mod 3 when i % 3 in {0, 1}, 0 mod 3 when i % 3 == 2.
    # A valid triple needs residues (1,1,1) or (0,0,0), so:
    # expected = C(count_of_ones, 3) + C(count_of_zeros, 3)
    for n in range(0, 31):
        ones = sum(1 for i in range(1, n + 1) if i % 3 in (0, 1))
        zeros = sum(1 for i in range(1, n + 1) if i % 3 == 2)
        expected = comb(ones, 3) + comb(zeros, 3)
        assert module_0.get_max_triples(n) == expected, f"failed for n={n}"

    # Result type sanity check
    assert isinstance(module_0.get_max_triples(5), int)

    # Monotonicity: count is non-decreasing as n grows
    prev = 0
    for n in range(1, 25):
        cur = module_0.get_max_triples(n)
        assert cur >= prev
        prev = cur


if __name__ == "__main__":
    test_get_max_triples()
    print("All tests passed")

# Generated at 2026-11-03 04:17:44.124757
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: not enough elements to form a single triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # Small known values
    # n=3: A=[1,3,7], sum=11 -> not divisible by 3
    assert module_0.get_max_triples(3) == 0
    # n=4: A=[1,3,7,13], only (1,7,13) sums to 21
    assert module_0.get_max_triples(4) == 1
    # n=5: A=[1,3,7,13,21], only (1,7,13)
    assert module_0.get_max_triples(5) == 1
    # n=6: residues mod 3 = [1,0,1,1,0,1] -> 4 valid triples
    assert module_0.get_max_triples(6) == 4
    # n=7: 5 ones, 2 zeros -> C(5,3) = 10
    assert module_0.get_max_triples(7) == 10
    # n=8: 5 ones, 3 zeros -> C(5,3)+C(3,3) = 11
    assert module_0.get_max_triples(8) == 11
    # n=10: 7 ones, 3 zeros -> C(7,3)+C(3,3) = 36
    assert module_0.get_max_triples(10) == 36

    # Cross-check against an independent brute-force reference
    def brute_force(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        m = len(A)
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(0, 15):
        assert module_0.get_max_triples(n) == brute_force(n)

    # Result must be a non-negative integer
    result = module_0.get_max_triples(12)
    assert isinstance(result, int)
    assert result >= 0
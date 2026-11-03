

# Generated at 2026-11-02 15:12:34.669949
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7]; only triple (1+3+7)=11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # A = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1

    # A = [1, 3, 7, 13, 21, 31]; four valid triples
    assert module_0.get_max_triples(6) == 4

    # Known reference case: answer is 36
    assert module_0.get_max_triples(10) == 36

    # Cross-check against a brute-force recomputation for a range of n
    def brute_force(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(0, 15):
        assert module_0.get_max_triples(n) == brute_force(n), f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 15:16:13.508465
# Unit test for function get_max_triples
def test_get_max_triples():
# nonce:9fb1af41
    # Edge cases: not enough elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1, 3, 7], only triple sums to 11 -> not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # Verified small cases:
    # n=5: A=[1, 3, 7, 13, 21], only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1
    # n=6: residue-1 values {1,7,13,31} give C(4,3)=4 triples
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(7) == 10
    # n=8: C(5,3) residue-1 triples + (3,21,57) = 10 + 1
    assert module_0.get_max_triples(8) == 11

    # Cross-check against an independent residue-counting method:
    # a triple sums to a multiple of 3 iff its residues are
    # (0,0,0), (1,1,1), (2,2,2), or (0,1,2)
    from collections import Counter
    for n in range(0, 25):
        counts = Counter((i * i - i + 1) % 3 for i in range(1, n + 1))
        c0, c1, c2 = counts.get(0, 0), counts.get(1, 0), counts.get(2, 0)
        expected = (
            c0 * (c0 - 1) * (c0 - 2) // 6
            + c1 * (c1 - 1) * (c1 - 2) // 6
            + c2 * (c2 - 1) * (c2 - 2) // 6
            + c0 * c1 * c2
        )
        assert module_0.get_max_triples(n) == expected, f"mismatch for n={n}"

# Generated at 2026-11-02 15:18:37.140525
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1,3,7], only triple sums to 11 (not divisible by 3)
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13], only (1,7,13)=21 is divisible by 3
    assert module_0.get_max_triples(4) == 1

    # n=5: A=[1,3,7,13,21], only (1,7,13)=21 is divisible by 3
    assert module_0.get_max_triples(5) == 1

    # n=6: A=[1,3,7,13,21,31], valid triples:
    # (1,7,13)=21, (1,7,31)=39, (1,13,31)=45, (7,13,31)=51
    assert module_0.get_max_triples(6) == 4

    # Values passed as tuples are correct: verify structure via a manual count
    n = 5
    A = [i * i - i + 1 for i in range(1, n + 1)]
    expected = sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
        if (A[i] + A[j] + A[k]) % 3 == 0
    )
    assert module_0.get_max_triples(n) == expected


# Generated at 2026-11-03 00:41:44.364689
# Unit test for function get_max_triples
def test_get_max_triples():
    # n too small to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1,3,7], sum=11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13], only (1,7,13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # n=5: A=[1,3,7,13,21], only (1,7,13) works
    assert module_0.get_max_triples(5) == 1

    # n=6: A=[1,3,7,13,21,31], mods are [1,0,1,1,0,1]
    # (1,1,1) combos: C(4,3)=4; (0,0,0) impossible with only two 0s
    assert module_0.get_max_triples(6) == 4

    # n=7: adds 43 (mod 1) -> C(5,3)=10 triples of all-1 residues
    assert module_0.get_max_triples(7) == 10

    # Cross-check with brute force for a larger n
    def brute(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(1, 12):
        assert module_0.get_max_triples(n) == brute(n), f"Mismatch at n={n}"

    print("All tests passed!")


test_get_max_triples()

# Generated at 2026-11-03 00:43:32.708798
# Unit test for function get_max_triples
def test_get_max_triples():
    # n too small to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7] -> only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13, 21] -> only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1

    # A = [1, 3, 7, 13, 21, 31] -> (1,7,13), (1,7,31), (1,13,31), (7,13,31)
    assert module_0.get_max_triples(6) == 4

    # n = 10: residues mod 3 -> three 0s, seven 1s -> C(3,3) + C(7,3) = 1 + 35
    assert module_0.get_max_triples(10) == 36

    # Result must be an integer count
    assert isinstance(module_0.get_max_triples(5), int)

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-03 00:44:40.974819
# Unit test for function get_max_triples
def test_get_max_triples():
    # A = [i*i - i + 1 for i in 1..n]; values are ≡ 0 or 1 (mod 3)
    # A triple sums to 0 mod 3 only when all three values ≡ 1 (mod 3)

    # n too small to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1,3,7], sum=11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13], only (1,7,13)=21 works
    assert module_0.get_max_triples(4) == 1

    # n=5: A=[1,3,7,13,21], only (1,7,13) works
    assert module_0.get_max_triples(5) == 1

    # n=6: A=[1,3,7,13,21,31], four values ≡1 mod 3 -> C(4,3)=4 triples
    assert module_0.get_max_triples(6) == 4

    # n=7: A=[1,3,7,13,21,31,43], five values ≡1 mod 3 -> C(5,3)=10 triples
    assert module_0.get_max_triples(7) == 10

    # n=10: six values ≡1 mod 3 -> C(6,3)=20 triples
    assert module_0.get_max_triples(10) == 20

    print("All tests passed!")


test_get_max_triples()

# Generated at 2026-11-03 00:45:59.710564
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: no triples possible
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A = [1, 3, 7]; only triple (1,3,7) sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21 (divisible by 3)
    assert module_0.get_max_triples(4) == 1

    # n=5: A = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1

    # n=6: residues mod 3 are [1,0,1,1,0,1]; C(4,3)=4 triples of residue-1 values
    assert module_0.get_max_triples(6) == 4

    # n=10: residues: seven 1s, three 0s -> C(7,3) + C(3,3) = 35 + 1 = 36
    assert module_0.get_max_triples(10) == 36

    # Return type check
    assert isinstance(module_0.get_max_triples(5), int)

    # Consistency check: brute-force recount for n=8
    A = [i * i - i + 1 for i in range(1, 9)]
    expected = sum(
        1
        for i in range(8)
        for j in range(i + 1, 8)
        for k in range(j + 1, 8)
        if (A[i] + A[j] + A[k]) % 3 == 0
    )
    assert module_0.get_max_triples(8) == expected

# Generated at 2026-11-03 00:47:36.614699
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: fewer than 3 elements means no triples are possible
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # Small inputs verified by direct enumeration of A = [i*i - i + 1]
    # n=3: A=[1,3,7] -> 1+3+7=11, not divisible by 3
    assert module_0.get_max_triples(3) == 0
    # n=4: only (1,7,13) sums to 21
    assert module_0.get_max_triples(4) == 1
    # n=5: only (1,7,13) sums to 21
    assert module_0.get_max_triples(5) == 1
    # n=6: (1,7,13), (1,7,31), (1,13,31), (7,13,31) all sum to a multiple of 3
    assert module_0.get_max_triples(6) == 4

    # Larger inputs (consistent with residue-class counting)
    assert module_0.get_max_triples(7) == 10
    assert module_0.get_max_triples(8) == 11
    assert module_0.get_max_triples(10) == 36

    # Return type / sanity checks
    result = module_0.get_max_triples(5)
    assert isinstance(result, int)
    assert result >= 0

    # Monotonicity: a larger n can only add candidate triples, never remove them
    assert module_0.get_max_triples(6) >= module_0.get_max_triples(5)
    assert module_0.get_max_triples(9) >= module_0.get_max_triples(8)
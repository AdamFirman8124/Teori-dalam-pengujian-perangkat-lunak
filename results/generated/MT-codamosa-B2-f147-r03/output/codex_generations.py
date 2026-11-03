

# Generated at 2026-11-02 13:10:10.996017
# Unit test for function get_max_triples
def test_get_max_triples():
    # n too small to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7] -> only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13] -> (1, 7, 13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # A = [1, 3, 7, 13, 21] -> only (1, 7, 13)
    assert module_0.get_max_triples(5) == 1

    # A = [1, 3, 7, 13, 21, 31] -> C(4,3) = 4 triples from {1, 7, 13, 31}
    assert module_0.get_max_triples(6) == 4

    # Cross-check against a brute-force reference over a range of inputs
    from itertools import combinations
    for n in range(1, 15):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        expected = sum(1 for c in combinations(A, 3) if sum(c) % 3 == 0)
        assert module_0.get_max_triples(n) == expected, f"Failed for n={n}"

# Generated at 2026-11-02 13:11:24.447426
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0  # A=[1,3,7], sum=11, not divisible by 3

    # Small known cases
    # n=4: A=[1,3,7,13]; only (1,7,13)=21 is divisible by 3
    assert module_0.get_max_triples(4) == 1
    # n=5: A=[1,3,7,13,21]; still only (1,7,13)=21
    assert module_0.get_max_triples(5) == 1
    # n=6: A=[1,3,7,13,21,31]; (1,7,13),(1,7,31),(1,13,31),(7,13,31)
    assert module_0.get_max_triples(6) == 4
    # n=10: 3 zeros + C(7,3)=35 ones-residue triples => 36
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
        expected = brute_force(n)
        assert module_0.get_max_triples(n) == expected, (
            f"module_0.get_max_triples({n}) returned {module_0.get_max_triples(n)}, "
            f"expected {expected}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 13:12:49.485841
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: A=[1,3,7], only triple sums to 11 (not divisible by 3)
    assert module_0.get_max_triples(3) == 0

    # n=4: A=[1,3,7,13], only (1,7,13)=21 is divisible by 3
    assert module_0.get_max_triples(4) == 1

    # Known example: n=5 -> 1 valid triple
    assert module_0.get_max_triples(5) == 1

    # Larger values (verified by brute force)
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(7) == 10
    assert module_0.get_max_triples(8) == 11

    # Cross-check against an independent brute-force implementation
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

    for n in range(1, 15):
        assert module_0.get_max_triples(n) == brute_force(n), f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 13:14:24.393308
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: fewer than 3 elements -> no triples
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0

    # Small known cases
    # A for n=4: [1, 3, 7, 13] -> only (1, 7, 13) sums to 21 (divisible by 3)
    assert module_0.get_max_triples(4) == 1
    # A for n=5: [1, 3, 7, 13, 21] -> only (1, 7, 13)
    assert module_0.get_max_triples(5) == 1
    # A for n=6: [1, 3, 7, 13, 21, 31] -> 4 valid triples
    assert module_0.get_max_triples(6) == 4
    # A for n=7: 10 valid triples
    assert module_0.get_max_triples(7) == 10

    # Larger cases
    assert module_0.get_max_triples(8) == 11
    assert module_0.get_max_triples(9) == 21
    assert module_0.get_max_triples(10) == 36

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 13:16:26.593943
# Unit test for function get_max_triples
def test_get_max_triples():
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(5) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(10) == 36
    assert module_0.get_max_triples(0) == 0
    print("All tests passed!")

test_get_max_triples()


# Generated at 2026-11-02 16:07:35.357044
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: not enough elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7]; only triple sums to 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21, divisible by 3
    assert module_0.get_max_triples(4) == 1

    # A = [1, 3, 7, 13, 21]; only (1, 7, 13) works
    assert module_0.get_max_triples(5) == 1

    # Residues mod 3 follow pattern: count triples of all-1s or all-0s
    # n=6: residues [1,0,1,1,0,1] -> C(4,3) = 4
    assert module_0.get_max_triples(6) == 4

    # n=10: residues [1,0,1,1,0,1,1,0,1,1] -> C(7,3) + C(3,3) = 35 + 1 = 36
    assert module_0.get_max_triples(10) == 36

    # n=0: empty list, no triples
    assert module_0.get_max_triples(0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-11-02 16:09:03.323533
# Unit test for function get_max_triples
def test_get_max_triples():
    # A = [i*i - i + 1 for i in range(1, n+1)]
    # For n=5: A = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to 21 (divisible by 3)
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(5) == 1

    # For n=6: A = [1, 3, 7, 13, 21, 31]
    # Valid triples: (1,7,13), (1,7,31), (1,13,31), (7,13,31)
    assert module_0.get_max_triples(6) == 4

    # For n=10: residues mod 3 are [1,0,1,1,0,1,1,0,1,1]
    # Sum divisible by 3 requires all three from residue-0 group (C(3,3)=1)
    # or all three from residue-1 group (C(7,3)=35) -> 36
    assert module_0.get_max_triples(10) == 36

    # Edge case: n=0 yields empty list, no triples
    assert module_0.get_max_triples(0) == 0

    # Result should be a non-negative integer
    result = module_0.get_max_triples(7)
    assert isinstance(result, int) and result >= 0

# Generated at 2026-11-02 16:09:55.891521
# Unit test for function get_max_triples
def test_get_max_triples():
    # Too few elements to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # n=3: only triple (1, 3, 7) -> sum 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # n=4: triple (1, 7, 13) -> sum 21, divisible by 3
    assert module_0.get_max_triples(4) == 1

    # Known example
    assert module_0.get_max_triples(5) == 1

    # Concrete values (verified analytically, see below)
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(7) == 10
    assert module_0.get_max_triples(8) == 11
    assert module_0.get_max_triples(10) == 36
    assert module_0.get_max_triples(20) == 321

    # Return type check
    assert isinstance(module_0.get_max_triples(10), int)

    def _c3(m):
        return m * (m - 1) * (m - 2) // 6 if m >= 3 else 0

    # Independent brute-force reference implementation
    def brute(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        m = len(A)
        count = 0
        for x in range(m):
            for y in range(x + 1, m):
                for z in range(y + 1, m):
                    if (A[x] + A[y] + A[z]) % 3 == 0:
                        count += 1
        return count

    # Analytic reference: A[i] % 3 == 0 iff i % 3 == 2 (1-indexed), else 1.
    # A triple sums to 0 mod 3 iff all three residues are equal (0+0+0 or 1+1+1).
    def analytic(n):
        c0 = sum(1 for i in range(1, n + 1) if i % 3 == 2)
        c1 = n - c0
        return _c3(c0) + _c3(c1)

    for n in range(1, 40):
        assert module_0.get_max_triples(n) == brute(n) == analytic(n)

# Generated at 2026-11-02 16:10:21.993548
# Unit test for function get_max_triples
def test_get_max_triples():
    # n too small to form any triple
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    # A = [1, 3, 7] -> 1+3+7 = 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0
    # A = [1, 3, 7, 13] -> only (1,7,13) sums to 21, divisible by 3
    assert module_0.get_max_triples(4) == 1
    # A = [1, 3, 7, 13, 21] -> still only (1,7,13) qualifies
    assert module_0.get_max_triples(5) == 1
    # Larger n: brute-force check against reference behavior
    def reference(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count
    for n in range(1, 12):
        assert module_0.get_max_triples(n) == reference(n), f"mismatch at n={n}"

# Generated at 2026-11-02 16:10:40.896380
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: too few elements to form any triple
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0

    # A = [1, 3, 7] -> sum 11, not divisible by 3
    assert module_0.get_max_triples(3) == 0

    # A = [1, 3, 7, 13] -> only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(4) == 1

    # A = [1, 3, 7, 13, 21] -> only (1, 7, 13) sums to 21
    assert module_0.get_max_triples(5) == 1

    # Cross-check against a brute-force reference for a range of n
    def reference(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(6, 15):
        assert module_0.get_max_triples(n) == reference(n), f"Mismatch for n={n}"

# nonce:f4830844
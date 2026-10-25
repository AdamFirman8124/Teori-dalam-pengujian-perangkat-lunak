

# Generated at 2026-10-24 19:47:28.549879
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:30.964444
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:33.379671
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:35.800990
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:38.216484
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:40.632058
# Unit test for function get_max_triples

# Generated at 2026-10-24 19:47:43.246024
# Unit test for function get_max_triples
def test_get_max_triples():
    # Brute-force reference for cross-checking
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

    # Known fixed values
    assert module_0.get_max_triples(1) == 0   # fewer than 3 elements
    assert module_0.get_max_triples(2) == 0   # fewer than 3 elements
    assert module_0.get_max_triples(3) == 0   # A=[1,3,7], sum=11, not divisible by 3
    assert module_0.get_max_triples(4) == 1   # (1,7,13) -> 21
    assert module_0.get_max_triples(5) == 1   # only (1,7,13) works
    assert module_0.get_max_triples(10) == 36

    # Cross-check against brute force for a range of sizes
    for n in range(1, 31):
        assert module_0.get_max_triples(n) == brute(n), f"mismatch at n={n}"

    print("All tests passed.")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-10-24 19:47:44.922409
# Unit test for function get_max_triples
def test_get_max_triples():
    # Known example: A(5) = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to a multiple of 3
    assert module_0.get_max_triples(1) == 0          # fewer than 3 elements
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0          # 1+3+7 = 11, not divisible by 3
    assert module_0.get_max_triples(5) == 1          # (1, 7, 13) -> 21
    assert module_0.get_max_triples(10) == 32

    # Cross-check against brute force on a larger input
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

    print("All tests passed.")


test_get_max_triples()

# Generated at 2026-10-24 19:47:46.244793
# Unit test for function get_max_triples
def test_get_max_triples():
    # Known example: A(5) = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to a multiple of 3
    assert module_0.get_max_triples(1) == 0          # fewer than 3 elements
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0          # 1+3+7 = 11, not divisible by 3
    assert module_0.get_max_triples(5) == 1          # (1, 7, 13) -> 21
    assert module_0.get_max_triples(10) == 32

    # Cross-check against brute force on a larger input
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

    print("All tests passed.")


test_get_max_triples()
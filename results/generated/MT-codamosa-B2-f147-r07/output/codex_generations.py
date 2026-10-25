

# Generated at 2026-10-24 07:45:24.306439
# Unit test for function get_max_triples
def test_get_max_triples():import pytest

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (5, 1),
        (6, 4),
        (7, 10),
        (8, 11),
        (9, 21),
        (10, 36),
    ],
)
def test_get_max_triples(n, expected):
    assert module_0.get_max_triples(n) == expected

# Generated at 2026-10-24 07:45:25.627270
# Unit test for function get_max_triples
def test_get_max_triples():assert module_0.get_max_triples(0) == 0

# Generated at 2026-10-24 07:47:24.933225
# Unit test for function get_max_triples
def test_get_max_triples():
    # Known small cases (hand-verified)
    assert module_0.get_max_triples(1) == 0   # A=[1], no triples
    assert module_0.get_max_triples(2) == 0   # A=[1,3], no triples
    assert module_0.get_max_triples(3) == 0   # A=[1,3,7], 1+3+7=11, not divisible by 3
    assert module_0.get_max_triples(5) == 1   # only (1,7,13): 21 % 3 == 0
    assert module_0.get_max_triples(10) == 36

    # Cross-check against an independent O(n^3) reference for many n
    def reference(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        m = len(A)
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(1, 26):
        assert module_0.get_max_triples(n) == reference(n), f"mismatch at n={n}"

    # Structural checks on returned triples for n=5
    A = [i * i - i + 1 for i in range(1, 6)]  # [1, 3, 7, 13, 21]
    assert (A[0], A[2], A[3]) == (1, 7, 13)   # the one valid triple

    print("All tests passed.")


if __name__ == "__main__":
    test_get_max_triples()

# Generated at 2026-10-24 07:47:49.408040
# Unit test for function get_max_triples
def test_get_max_triples():
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(5) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(8) == 11

# Generated at 2026-10-24 07:47:51.824298
# Unit test for function get_max_triples

# Generated at 2026-10-24 07:47:54.241022
# Unit test for function get_max_triples

# Generated at 2026-10-24 07:47:56.669191
# Unit test for function get_max_triples

# Generated at 2026-10-24 07:47:59.281438
# Unit test for function get_max_triples
def test_get_max_triples():
    # Known small cases (hand-verified)
    assert module_0.get_max_triples(1) == 0   # A=[1], no triples
    assert module_0.get_max_triples(2) == 0   # A=[1,3], no triples
    assert module_0.get_max_triples(3) == 0   # A=[1,3,7], 1+3+7=11, not divisible by 3
    assert module_0.get_max_triples(5) == 1   # only (1,7,13): 21 % 3 == 0
    assert module_0.get_max_triples(10) == 36

    # Cross-check against an independent O(n^3) reference for many n
    def reference(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        m = len(A)
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(1, 26):
        assert module_0.get_max_triples(n) == reference(n), f"mismatch at n={n}"

    # Structural checks on returned triples for n=5
    A = [i * i - i + 1 for i in range(1, 6)]  # [1, 3, 7, 13, 21]
    assert (A[0], A[2], A[3]) == (1, 7, 13)   # the one valid triple

    print("All tests passed.")


if __name__ == "__main__":
    test_get_max_triples()
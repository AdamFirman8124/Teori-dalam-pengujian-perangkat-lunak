

# Generated at 2026-10-24 20:56:13.801084
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:16.217916
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:18.634013
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:21.051012
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:23.469438
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:25.889339
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:28.305204
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:30.720724
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:33.139692
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:35.557530
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:37.973680
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:40.389652
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:42.808386
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:45.224262
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:47.640713
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:50.056695
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:52.473076
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:54.887977
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:57.304500
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:56:59.719698
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:57:02.134650
# Unit test for function get_max_triples

# Generated at 2026-10-24 20:57:04.677152
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

# Generated at 2026-10-24 20:57:05.999373
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

# Generated at 2026-10-24 20:57:07.323847
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

# Generated at 2026-10-24 20:57:08.650616
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

# Generated at 2026-10-24 20:57:10.364445
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

# Generated at 2026-10-24 20:57:11.714485
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

# Generated at 2026-10-24 20:57:13.047418
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

# Generated at 2026-10-24 20:57:14.369898
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
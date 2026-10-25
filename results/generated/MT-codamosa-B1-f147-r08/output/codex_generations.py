

# Generated at 2026-10-24 19:39:22.771528
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

# Generated at 2026-10-24 19:39:24.138985
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

# Generated at 2026-10-24 19:39:25.461784
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

# Generated at 2026-10-24 19:39:26.782988
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

# Generated at 2026-10-24 19:39:28.099914
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
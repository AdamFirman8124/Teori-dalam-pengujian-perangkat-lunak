

# Generated at 2026-10-25 02:49:15.288226
# Unit test for function get_max_triples

# Generated at 2026-10-25 02:49:17.701682
# Unit test for function get_max_triples

# Generated at 2026-10-25 02:49:20.119114
# Unit test for function get_max_triples

# Generated at 2026-10-25 02:49:30.838309
# Unit test for function get_max_triples
def test_get_max_triples():assert module_0.get_max_triples(0) == 0

# Generated at 2026-10-25 02:49:40.583884
# Unit test for function get_max_triples
def test_get_max_triples():
    expected_results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 1,
        5: 1,
        6: 4,
        7: 10,
        8: 11,
        9: 21,
    }

    for n, expected in expected_results.items():
        assert module_0.get_max_triples(n) == expected

# Generated at 2026-10-25 02:49:51.064044
# Unit test for function get_max_triples
def test_get_max_triples():
    def expected(n):
        # A[i] is divisible by 3 exactly when its 1-based index is 2 mod 3.
        divisible = (n + 1) // 3
        remainder_one = n - divisible

        return (
            comb(divisible, 3) if divisible >= 3 else 0
        ) + (
            comb(remainder_one, 3) if remainder_one >= 3 else 0
        )

    for n in range(0, 25):
        assert module_0.get_max_triples(n) == expected(n)

    # Explicit boundary cases
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(10) == 36

# Generated at 2026-10-25 02:49:59.714908
# Unit test for function get_max_triples
def test_get_max_triples():
    test_cases = [
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
    ]

    for n, expected in test_cases:
        assert module_0.get_max_triples(n) == expected
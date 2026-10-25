

# Generated at 2026-10-24 12:32:36.482255
# Unit test for function get_max_triples
def test_get_max_triples():
    test_cases = {
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
        10: 36,
    }

    for n, expected in test_cases.items():
        assert module_0.get_max_triples(n) == expected, (
            f"module_0.get_max_triples({n}) returned "
            f"{module_0.get_max_triples(n)}, expected {expected}"
        )

# Generated at 2026-10-24 12:32:46.720381
# Unit test for function get_max_triples
def test_get_max_triples():
    # Basic cases
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(5) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(8) == 11

    # A[i] is divisible by 3 when its 1-based index is 2 mod 3;
    # otherwise, A[i] is 1 mod 3. Valid triples contain either
    # three divisible elements or three non-divisible elements.
    for n in range(50):
        divisible = (n + 1) // 3
        non_divisible = n - divisible
        expected = comb(divisible, 3) + comb(non_divisible, 3)

        assert module_0.get_max_triples(n) == expected

# Generated at 2026-10-24 12:32:55.937129
# Unit test for function get_max_triples
def test_get_max_triples():
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(5) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(7) == 10
    assert module_0.get_max_triples(8) == 11
    assert module_0.get_max_triples(10) == 36

# Generated at 2026-10-24 12:33:04.190752
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
        (10, 36),
    ]

    for n, expected in test_cases:
        assert module_0.get_max_triples(n) == expected

# Generated at 2026-10-24 12:33:13.650179
# Unit test for function get_max_triples
def test_get_max_triples():
    assert module_0.get_max_triples(0) == 0
    assert module_0.get_max_triples(1) == 0
    assert module_0.get_max_triples(2) == 0
    assert module_0.get_max_triples(3) == 0
    assert module_0.get_max_triples(4) == 1
    assert module_0.get_max_triples(6) == 4
    assert module_0.get_max_triples(8) == 11
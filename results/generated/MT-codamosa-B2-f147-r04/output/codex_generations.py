

# Generated at 2026-10-24 06:29:58.634830
# Unit test for function get_max_triples
def test_get_max_triples():
    # Edge cases: no triple possible
    assert module_0.get_max_triples(1) == 0   # A = [1]
    assert module_0.get_max_triples(2) == 0   # A = [1, 3]
    assert module_0.get_max_triples(3) == 0   # 1+3+7 = 11, not divisible by 3

    # Known values (hand-checked)
    assert module_0.get_max_triples(4) == 1   # only (1, 7, 13): 21 % 3 == 0
    assert module_0.get_max_triples(5) == 1   # A = [1, 3, 7, 13, 21], only (1, 7, 13)
    assert module_0.get_max_triples(6) == 4   # (1,7,13), (1,7,31), (1,13,31), (7,13,31)

    # Cross-check against an independent count
    # (values â¡ 0 mod 3 when i â¡ 2 mod 3, else â¡ 1; valid triples are
    #  all-from-class-1 or all-from-class-0)
    from math import comb
    for n in range(1, 12):
        c0 = sum(1 for i in range(1, n + 1) if i % 3 == 2)
        c1 = n - c0
        expected = comb(c1, 3) + comb(c0, 3)
        assert module_0.get_max_triples(n) == expected, f"failed for n={n}"

    print("All tests passed.")


test_get_max_triples()

# Generated at 2026-10-24 06:30:01.048908
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:03.465063
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:05.880006
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:08.292498
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:10.854661
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:13.270296
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:15.686971
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:18.122868
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:20.517430
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:22.932933
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:25.346867
# Unit test for function get_max_triples

# Generated at 2026-10-24 06:30:35.172222
# Unit test for function get_max_triples
def test_get_max_triples():assert module_0.get_max_triples(0) == 0


# Generated at 2026-10-24 13:54:28.323594
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(10, 7) == 2

    # Compare against Python's built-in modular exponentiation
    for n in range(20):
        for p in range(1, 10):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-24 13:54:35.292202
# Unit test for function modp
def test_modp():
    test_cases = [
        (0, 5),
        (1, 5),
        (3, 5),
        (10, 7),
        (20, 13),
    ]

    for n, p in test_cases:
        assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-24 13:54:41.427571
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 7) == 1
    assert module_0.modp(1, 7) == 2
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(10, 7) == pow(2, 10, 7)
    assert module_0.modp(100, 13) == pow(2, 100, 13)

# Generated at 2026-10-24 13:54:46.651516
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3       # 2**3 % 5
    assert module_0.modp(10, 7) == 2      # 2**10 % 7
    assert module_0.modp(100, 13) == pow(2, 100, 13)

# Generated at 2026-10-24 13:54:51.821832
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(10, 7) == 2

    # Compare against Python's modular exponentiation.
    for n in range(20):
        for p in range(2, 20):
            assert module_0.modp(n, p) == pow(2, n, p)
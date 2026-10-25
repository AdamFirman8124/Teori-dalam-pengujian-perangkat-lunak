

# Generated at 2026-10-24 07:04:42.903042
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(10, 7) == 2

    # Compare against Python's built-in modular exponentiation.
    for n in range(20):
        for p in (2, 3, 5, 7, 11):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-24 07:04:47.269827
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3   # 2**3 % 5
    assert module_0.modp(10, 7) == 2  # 2**10 % 7

    # Compare against Python's built-in modular exponentiation.
    for n in range(20):
        for p in range(2, 20):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-24 07:04:56.181716
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 7) == 1
    assert module_0.modp(1, 7) == 2
    assert module_0.modp(3, 5) == 3       # 2**3 % 5
    assert module_0.modp(10, 7) == 2      # 2**10 % 7
    assert module_0.modp(100, 13) == pow(2, 100, 13)

# Generated at 2026-10-24 07:05:00.735379
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3       # 2**3 % 5
    assert module_0.modp(10, 7) == 2      # 2**10 % 7
    assert module_0.modp(20, 13) == pow(2, 20, 13)

# Generated at 2026-10-24 07:05:07.382784
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1       # 2^0 mod 5
    assert module_0.modp(1, 5) == 2       # 2^1 mod 5
    assert module_0.modp(3, 5) == 3       # 8 mod 5
    assert module_0.modp(10, 7) == 2      # 1024 mod 7
    assert module_0.modp(100, 13) == pow(2, 100, 13)
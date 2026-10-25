

# Generated at 2026-10-25 01:29:30.747031
# Unit test for function modp

# Generated at 2026-10-25 01:29:33.162905
# Unit test for function modp

# Generated at 2026-10-25 01:29:35.580957
# Unit test for function modp

# Generated at 2026-10-25 01:29:37.992262
# Unit test for function modp

# Generated at 2026-10-25 01:29:40.407042
# Unit test for function modp

# Generated at 2026-10-25 01:29:42.821776
# Unit test for function modp

# Generated at 2026-10-25 01:29:44.288497
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3      # 2**3 = 8, 8 % 5 = 3
    assert module_0.modp(10, 100) == 24  # 2**10 = 1024, 1024 % 100 = 24
    assert module_0.modp(5, 1) == 0

    for n in range(30):
        for p in (7, 97, 1000):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-25 01:29:45.621639
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3      # 2**3 = 8, 8 % 5 = 3
    assert module_0.modp(10, 100) == 24  # 2**10 = 1024, 1024 % 100 = 24
    assert module_0.modp(5, 1) == 0

    for n in range(30):
        for p in (7, 97, 1000):
            assert module_0.modp(n, p) == pow(2, n, p)

# Generated at 2026-10-25 01:29:46.951524
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3      # 2**3 = 8, 8 % 5 = 3
    assert module_0.modp(10, 100) == 24  # 2**10 = 1024, 1024 % 100 = 24
    assert module_0.modp(5, 1) == 0

    for n in range(30):
        for p in (7, 97, 1000):
            assert module_0.modp(n, p) == pow(2, n, p)
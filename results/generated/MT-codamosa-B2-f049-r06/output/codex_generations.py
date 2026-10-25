

# Generated at 2026-10-25 01:11:27.074100
# Unit test for function modp

# Generated at 2026-10-25 01:11:29.490754
# Unit test for function modp

# Generated at 2026-10-25 01:11:31.911445
# Unit test for function modp

# Generated at 2026-10-25 01:11:34.323782
# Unit test for function modp

# Generated at 2026-10-25 01:11:36.738904
# Unit test for function modp

# Generated at 2026-10-25 01:11:39.153146
# Unit test for function modp

# Generated at 2026-10-25 01:11:52.506004
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

# Generated at 2026-10-25 01:11:53.939269
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

# Generated at 2026-10-25 01:11:55.270458
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
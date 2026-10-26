

# Generated at 2026-10-25 07:16:35.732894
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

# Generated at 2026-10-25 07:16:38.562188
# Unit test for function modp

# Generated at 2026-10-25 07:16:40.976665
# Unit test for function modp

# Generated at 2026-10-25 07:16:43.390991
# Unit test for function modp

# Generated at 2026-10-25 07:16:45.806531
# Unit test for function modp

# Generated at 2026-10-25 07:16:48.221910
# Unit test for function modp

# Generated at 2026-10-25 07:16:50.636009
# Unit test for function modp

# Generated at 2026-10-25 07:16:53.050238
# Unit test for function modp

# Generated at 2026-10-25 07:17:00.584354
# Unit test for function modp
def test_modp():assert module_0.modp(0, 7) == 1

# Generated at 2026-10-25 07:17:17.479979
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
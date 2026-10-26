

# Generated at 2026-10-25 07:12:09.412616
# Unit test for function modp

# Generated at 2026-10-25 07:12:11.827663
# Unit test for function modp

# Generated at 2026-10-25 07:12:14.401044
# Unit test for function modp

# Generated at 2026-10-25 07:12:16.816899
# Unit test for function modp

# Generated at 2026-10-25 07:12:19.230777
# Unit test for function modp

# Generated at 2026-10-25 07:12:21.646389
# Unit test for function modp

# Generated at 2026-10-25 07:12:24.062353
# Unit test for function modp

# Generated at 2026-10-25 07:12:26.477320
# Unit test for function modp

# Generated at 2026-10-25 07:12:28.896881
# Unit test for function modp

# Generated at 2026-10-25 07:12:46.415126
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

# Generated at 2026-10-25 07:13:02.911919
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
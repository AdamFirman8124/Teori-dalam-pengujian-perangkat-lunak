

# Generated at 2026-10-24 14:53:58.384204
# Unit test for function modp

# Generated at 2026-10-24 14:54:00.794960
# Unit test for function modp

# Generated at 2026-10-24 14:54:03.207695
# Unit test for function modp

# Generated at 2026-10-24 14:54:05.619816
# Unit test for function modp

# Generated at 2026-10-24 14:54:08.032745
# Unit test for function modp

# Generated at 2026-10-24 14:54:10.446730
# Unit test for function modp

# Generated at 2026-10-24 14:54:12.857979
# Unit test for function modp

# Generated at 2026-10-24 14:54:16.458391
# Unit test for function modp
def test_modp():
    assert module_0.modp(0, 101) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3
    assert module_0.modp(10, 7) == 3
    assert module_0.modp(100, 101) == 2 ** 100 % 101

# Generated at 2026-10-24 14:54:24.936105
# Unit test for function modp
def test_modp():
    # basic cases
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3          # 8 % 5
    assert module_0.modp(10, 1000) == 24     # 1024 % 1000

    # large n / large modulus
    assert module_0.modp(1000, 10**9 + 7) == pow(2, 1000, 10**9 + 7)

    # result always reduced
    assert module_0.modp(50, 1) == 0

    # exhaustive cross-check against Python's built-in
    for n in range(0, 60):
        for p in range(2, 40):
            assert module_0.modp(n, p) == pow(2, n, p), (n, p)


def test_modp_known_divergences():
    # n=0, p=1: 2**0 % 1 == 0, but the loop never runs so it returns 1
    assert module_0.modp(0, 1) == 1
    assert pow(2, 0, 1) == 0        # documents the mismatch

    # p=0: n=0 returns 1, n>0 raises ZeroDivisionError
    assert module_0.modp(0, 0) == 1
    try:
        module_0.modp(1, 0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("expected ZeroDivisionError for p=0, n>0")

# Generated at 2026-10-24 14:54:26.264954
# Unit test for function modp
def test_modp():
    # basic cases
    assert module_0.modp(0, 5) == 1
    assert module_0.modp(1, 5) == 2
    assert module_0.modp(3, 5) == 3          # 8 % 5
    assert module_0.modp(10, 1000) == 24     # 1024 % 1000

    # large n / large modulus
    assert module_0.modp(1000, 10**9 + 7) == pow(2, 1000, 10**9 + 7)

    # result always reduced
    assert module_0.modp(50, 1) == 0

    # exhaustive cross-check against Python's built-in
    for n in range(0, 60):
        for p in range(2, 40):
            assert module_0.modp(n, p) == pow(2, n, p), (n, p)


def test_modp_known_divergences():
    # n=0, p=1: 2**0 % 1 == 0, but the loop never runs so it returns 1
    assert module_0.modp(0, 1) == 1
    assert pow(2, 0, 1) == 0        # documents the mismatch

    # p=0: n=0 returns 1, n>0 raises ZeroDivisionError
    assert module_0.modp(0, 0) == 1
    try:
        module_0.modp(1, 0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("expected ZeroDivisionError for p=0, n>0")
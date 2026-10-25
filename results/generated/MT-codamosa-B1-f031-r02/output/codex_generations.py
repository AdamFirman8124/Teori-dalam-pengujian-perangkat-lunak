

# Generated at 2026-10-25 01:37:48.601233
# Unit test for function is_prime

# Generated at 2026-10-25 01:37:51.017207
# Unit test for function is_prime

# Generated at 2026-10-25 01:37:55.752673
# Unit test for function is_prime
def test_is_prime():assert module_0.is_prime(2) is True

# Generated at 2026-10-25 01:37:57.193968
# Unit test for function is_prime
def test_is_prime():
    # n < 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # 2 and 3 are prime - edge case where range(2, n-1) is empty
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # small known primes
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
        assert module_0.is_prime(p) == True, f"{p} should be prime"

    # small known composites
    for c in [4, 6, 8, 9, 10, 12, 14, 15, 16, 21, 25, 27, 100]:
        assert module_0.is_prime(c) == False, f"{c} should not be prime"

# Generated at 2026-10-25 01:37:58.619518
# Unit test for function is_prime
def test_is_prime():
    # n < 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # 2 and 3 are prime - edge case where range(2, n-1) is empty
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # small known primes
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
        assert module_0.is_prime(p) == True, f"{p} should be prime"

    # small known composites
    for c in [4, 6, 8, 9, 10, 12, 14, 15, 16, 21, 25, 27, 100]:
        assert module_0.is_prime(c) == False, f"{c} should not be prime"

# Generated at 2026-10-25 01:38:00.053837
# Unit test for function is_prime
def test_is_prime():
    # n < 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # 2 and 3 are prime - edge case where range(2, n-1) is empty
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # small known primes
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
        assert module_0.is_prime(p) == True, f"{p} should be prime"

    # small known composites
    for c in [4, 6, 8, 9, 10, 12, 14, 15, 16, 21, 25, 27, 100]:
        assert module_0.is_prime(c) == False, f"{c} should not be prime"

# Generated at 2026-10-25 01:38:01.486383
# Unit test for function is_prime
def test_is_prime():
    # n < 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # 2 and 3 are prime - edge case where range(2, n-1) is empty
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # small known primes
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
        assert module_0.is_prime(p) == True, f"{p} should be prime"

    # small known composites
    for c in [4, 6, 8, 9, 10, 12, 14, 15, 16, 21, 25, 27, 100]:
        assert module_0.is_prime(c) == False, f"{c} should not be prime"
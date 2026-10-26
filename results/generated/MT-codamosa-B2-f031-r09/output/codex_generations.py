

# Generated at 2026-10-25 10:19:02.909134
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

# Generated at 2026-10-25 10:19:04.417926
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

# Generated at 2026-10-25 10:19:05.897618
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

# Generated at 2026-10-25 10:19:07.331501
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

# Generated at 2026-10-25 10:19:23.819707
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
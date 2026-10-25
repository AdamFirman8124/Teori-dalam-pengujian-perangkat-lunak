

# Generated at 2026-10-25 03:07:14.713801
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:17.120112
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:19.536331
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:21.950449
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:24.363931
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:26.778818
# Unit test for function is_prime

# Generated at 2026-10-25 03:07:32.909151
# Unit test for function is_prime
def test_is_prime():assert module_0.is_prime(-1) is False

# Generated at 2026-10-25 03:07:34.336581
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

# Generated at 2026-10-25 03:07:35.772014
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
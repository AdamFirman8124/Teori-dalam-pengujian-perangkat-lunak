

# Generated at 2026-10-25 09:01:20.122767
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

# Generated at 2026-10-25 09:01:29.475187
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    composites = [-7, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in composites:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

    print("all is_prime tests passed")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-10-25 09:01:31.893256
# Unit test for function is_prime

# Generated at 2026-10-25 09:01:34.395715
# Unit test for function is_prime

# Generated at 2026-10-25 09:01:36.810917
# Unit test for function is_prime

# Generated at 2026-10-25 09:01:39.230675
# Unit test for function is_prime

# Generated at 2026-10-25 09:01:52.072281
# Unit test for function is_prime
def test_is_prime():assert module_0.is_prime(-5) is False

# Generated at 2026-10-25 09:01:53.607473
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    composites = [-7, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in composites:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

    print("all is_prime tests passed")


if __name__ == "__main__":
    test_is_prime()


# Generated at 2026-10-24 13:35:18.980358
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:20.412831
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:21.741040
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:23.066710
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:24.406565
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:25.767710
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:27.100140
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:44.169400
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:35:46.587710
# Unit test for function is_prime

# Generated at 2026-10-24 13:35:49.292892
# Unit test for function is_prime

# Generated at 2026-10-24 13:35:51.792230
# Unit test for function is_prime

# Generated at 2026-10-24 13:35:54.330885
# Unit test for function is_prime

# Generated at 2026-10-24 13:35:56.748762
# Unit test for function is_prime

# Generated at 2026-10-24 13:35:59.296836
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:01.710721
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:04.128003
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:06.544549
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:08.961146
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:11.377323
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:13.792160
# Unit test for function is_prime

# Generated at 2026-10-24 13:36:32.617313
# Unit test for function is_prime
def test_is_prime():
    # edge cases
    assert module_0.is_prime(-7) is False
    assert module_0.is_prime(0) is False
    assert module_0.is_prime(1) is False
    assert module_0.is_prime(2) is True
    assert module_0.is_prime(3) is True

    # composites
    assert module_0.is_prime(4) is False
    assert module_0.is_prime(6) is False
    assert module_0.is_prime(9) is False
    assert module_0.is_prime(15) is False
    assert module_0.is_prime(100) is False
    assert module_0.is_prime(7917) is False  # 3 * 2639

    # primes
    assert module_0.is_prime(5) is True
    assert module_0.is_prime(17) is True
    assert module_0.is_prime(97) is True
    assert module_0.is_prime(7919) is True

    # perfect squares of primes (divisor equals sqrt)
    assert module_0.is_prime(49) is False
    assert module_0.is_prime(121) is False

# Generated at 2026-10-24 13:36:49.030798
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"

# Generated at 2026-10-24 13:36:50.356519
# Unit test for function is_prime
def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    for n in primes:
        assert module_0.is_prime(n) is True, f"{n} should be prime"

    non_primes = [-7, -1, 0, 1, 4, 6, 9, 15, 25, 100, 7917]
    for n in non_primes:
        assert module_0.is_prime(n) is False, f"{n} should not be prime"
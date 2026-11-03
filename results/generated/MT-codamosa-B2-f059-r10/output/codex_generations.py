

# Generated at 2026-11-02 17:23:12.281834
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite number
    assert module_0.largest_prime_factor(15) == 5, "15 = 3 * 5, largest prime factor is 5"
    assert module_0.largest_prime_factor(27) == 3, "27 = 3^3, largest prime factor is 3"
    assert module_0.largest_prime_factor(100) == 5, "100 = 2^2 * 5^2, largest prime factor is 5"

    # Classic example (Project Euler #3)
    assert module_0.largest_prime_factor(13195) == 29, "13195 = 5 * 7 * 13 * 29"

    # Prime numbers are their own largest prime factor
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Product of two primes
    assert module_0.largest_prime_factor(17 * 19) == 19
    assert module_0.largest_prime_factor(7 * 11) == 11

    # Powers of two
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(64) == 2

    # Larger number
    assert module_0.largest_prime_factor(600851475143) == 6857

    # Edge case: n = 1 has no prime factors, function returns default 1
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 17:26:04.750960
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
# nonce:963b9457
    # Classic cases
    assert module_0.largest_prime_factor(15) == 5        # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3        # 27 = 3^3
    assert module_0.largest_prime_factor(13195) == 29    # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(2048) == 2      # 2048 = 2^11

    # Prime inputs return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of a single prime
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(64) == 2
    assert module_0.largest_prime_factor(49) == 7

    # Mixed factors
    assert module_0.largest_prime_factor(100) == 5       # 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7        # 84 = 2^2 * 3 * 7
    assert module_0.largest_prime_factor(360) == 5       # 360 = 2^3 * 3^2 * 5
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(10) == 5

    # Edge case: 1 has no prime factors; function returns its initial value
    assert module_0.largest_prime_factor(1) == 1

    print("test_largest_prime_factor: all assertions passed")


if __name__ == "__main__":
    test_largest_prime_factor()
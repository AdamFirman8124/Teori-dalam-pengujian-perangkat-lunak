

# Generated at 2026-11-02 17:23:34.757306
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5, "15 = 3 * 5, largest prime factor is 5"
    assert module_0.largest_prime_factor(27) == 3, "27 = 3^3, largest prime factor is 3"
    assert module_0.largest_prime_factor(13195) == 29, "13195 = 5 * 7 * 13 * 29, largest is 29"
    assert module_0.largest_prime_factor(2048) == 2, "2048 = 2^11, largest prime factor is 2"

    # Prime inputs (number itself is the largest prime factor)
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(2) == 2

    # Composite with repeated prime factors
    assert module_0.largest_prime_factor(100) == 5, "100 = 2^2 * 5^2"
    assert module_0.largest_prime_factor(49) == 7, "49 = 7^2"
    assert module_0.largest_prime_factor(60) == 5, "60 = 2^2 * 3 * 5"

    # Edge case: 1 has no prime factors, function returns initial value
    assert module_0.largest_prime_factor(1) == 1

    # Larger value
    assert module_0.largest_prime_factor(600851475143) == 6857

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 17:26:53.536418
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Standard cases
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(2048) == 2    # 2048 = 2^11
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(63) == 7      # 63 = 3^2 * 7
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2

    # Prime input: largest prime factor is itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Edge case: n = 1 has no prime factors, function returns initial value
    assert module_0.largest_prime_factor(1) == 1

    # Larger composite number
    assert module_0.largest_prime_factor(600851475143) == 6857
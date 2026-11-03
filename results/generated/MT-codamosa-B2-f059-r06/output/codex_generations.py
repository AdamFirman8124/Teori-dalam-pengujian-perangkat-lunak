

# Generated at 2026-11-02 07:26:10.792553
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5, "15 = 3 * 5, largest prime factor is 5"
    assert module_0.largest_prime_factor(27) == 3, "27 = 3^3, largest prime factor is 3"
    assert module_0.largest_prime_factor(10) == 5, "10 = 2 * 5, largest prime factor is 5"
    assert module_0.largest_prime_factor(100) == 5, "100 = 2^2 * 5^2, largest prime factor is 5"

    # Classic example
    assert module_0.largest_prime_factor(13195) == 29, "13195 = 5 * 7 * 13 * 29"

    # Prime number itself
    assert module_0.largest_prime_factor(7) == 7, "7 is prime, largest prime factor is itself"
    assert module_0.largest_prime_factor(13) == 13, "13 is prime, largest prime factor is itself"
    assert module_0.largest_prime_factor(2) == 2, "2 is prime, smallest prime"

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1, "1 has no prime factors, returns default 1"
    assert module_0.largest_prime_factor(4) == 2, "4 = 2^2, largest prime factor is 2"
    assert module_0.largest_prime_factor(6) == 3, "6 = 2 * 3, largest prime factor is 3"

    # Larger composite
    assert module_0.largest_prime_factor(600851475143) == 6857, "Project Euler #3 example"

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-02 07:27:03.852629
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Test with a composite number with multiple prime factors
    assert module_0.largest_prime_factor(15) == 5       # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3       # 27 = 3^3
    assert module_0.largest_prime_factor(13195) == 29   # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(2048) == 2     # 2048 = 2^11
    assert module_0.largest_prime_factor(100) == 5      # 100 = 2^2 * 5^2

    # Test with a prime number (largest prime factor is itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Test with product of two primes
    assert module_0.largest_prime_factor(7 * 11) == 11
    assert module_0.largest_prime_factor(23 * 29) == 29

    # Test with large-ish number
    assert module_0.largest_prime_factor(600851475143) == 6857  # Project Euler example

    # Test with number whose largest prime factor is small
    assert module_0.largest_prime_factor(12) == 3       # 12 = 2^2 * 3
    assert module_0.largest_prime_factor(16) == 2       # 16 = 2^4
    assert module_0.largest_prime_factor(45) == 5       # 45 = 3^2 * 5

    print("All tests passed!")


# Run the tests
test_largest_prime_factor()

# Generated at 2026-11-02 07:27:52.673266
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(10) == 5

    # Prime number itself
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13

    # Powers of a prime
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(81) == 3
    assert module_0.largest_prime_factor(32) == 2

    # Larger composite numbers
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(1000) == 5
    assert module_0.largest_prime_factor(97) == 97
    assert module_0.largest_prime_factor(600851475143) == 6857

    # Edge case: n = 1 (no prime factors, returns initial value)
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 07:28:51.265901
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite cases
    assert module_0.largest_prime_factor(15) == 5       # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3       # 27 = 3^3
    assert module_0.largest_prime_factor(63) == 7       # 63 = 3^2 * 7
    assert module_0.largest_prime_factor(330) == 11     # 330 = 2 * 3 * 5 * 11

    # Reference cases
    assert module_0.largest_prime_factor(13195) == 29   # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(2048) == 2     # 2048 = 2^11

    # Small values
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(5) == 5
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3

    # Prime input returns itself
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(7919) == 7919

    # Powers of a single prime
    assert module_0.largest_prime_factor(121) == 11
    assert module_0.largest_prime_factor(1024) == 2

    # Larger composite
    assert module_0.largest_prime_factor(100) == 5      # 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(9973) == 9973  # prime

    # Edge case: n = 1 has no prime factors; initial value returned
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-11-02 07:29:18.365708
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(12) == 3      # 12 = 2^2 * 3
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2

    # Power of two
    assert module_0.largest_prime_factor(2048) == 2    # 2048 = 2^11

    # Prime number input (largest factor is itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Larger composite
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(63) == 7      # 63 = 3^2 * 7

    # Edge case: n = 1 has no prime factors, returns initial value
    assert module_0.largest_prime_factor(1) == 1
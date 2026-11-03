

# Generated at 2026-11-03 00:33:37.727678
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(2048) == 2

    # Prime inputs: largest prime factor is the number itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(13) == 13

    # Composite with repeated factors
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(45) == 5
    assert module_0.largest_prime_factor(72) == 3

    # Product of two primes
    assert module_0.largest_prime_factor(3 * 11) == 11
    assert module_0.largest_prime_factor(17 * 19) == 19

    # Edge case: n = 1 has no prime factors, loop doesn't run, returns 1
    assert module_0.largest_prime_factor(1) == 1

    # Larger but tractable value
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13) == 13

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-03 00:34:28.823582
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 3, 3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29
    assert module_0.largest_prime_factor(10) == 5      # factors: 2, 5
    assert module_0.largest_prime_factor(7) == 7       # prime number itself

    # Prime input
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(2) == 2       # smallest prime

    # Composite with repeated prime factors
    assert module_0.largest_prime_factor(64) == 2      # 2^6
    assert module_0.largest_prime_factor(45) == 5      # 3^2 * 5

    # Larger numbers
    assert module_0.largest_prime_factor(600851475143) == 6857
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1       # no prime factors
    assert module_0.largest_prime_factor(4) == 2       # 2^2

    # Product of two primes
    assert module_0.largest_prime_factor(21) == 7      # 3 * 7
    assert module_0.largest_prime_factor(77) == 11     # 7 * 11

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 00:35:58.883126
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(2048) == 2    # 2048 = 2^11
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(21) == 7      # 21 = 3 * 7

    # Prime inputs (largest prime factor is the number itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(97) == 97

    # Edge case: 1 has no prime factors, function returns initial value 1
    assert module_0.largest_prime_factor(1) == 1

    # Larger number
    assert module_0.largest_prime_factor(600851475143) == 6857  # Project Euler #3

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 00:37:24.593787
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 3, 3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29
    assert module_0.largest_prime_factor(2048) == 2    # power of 2

    # Prime number input itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Composite numbers
    assert module_0.largest_prime_factor(100) == 5     # factors: 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7      # factors: 2^2 * 3 * 7
    assert module_0.largest_prime_factor(360) == 5     # factors: 2^3 * 3^2 * 5
    assert module_0.largest_prime_factor(49) == 7      # 7^2

    # Edge case: n = 1 has no prime factors, returns default largest = 1
    assert module_0.largest_prime_factor(1) == 1

    # Large-ish number
    assert module_0.largest_prime_factor(600851475143) == 6857  # Project Euler #3

    print("All tests passed!")


test_largest_prime_factor()
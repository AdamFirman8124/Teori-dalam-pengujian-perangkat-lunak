

# Generated at 2026-11-02 10:49:40.428092
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(2048) == 2
    assert module_0.largest_prime_factor(13) == 13  # n itself is prime
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(2) == 2    # smallest prime
    assert module_0.largest_prime_factor(1) == 1    # no prime factors
    assert module_0.largest_prime_factor(1024) == 2 # power of 2
    assert module_0.largest_prime_factor(3 * 5 * 7 * 11) == 11
    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-02 10:49:56.105784
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # only prime factor is 3
    assert module_0.largest_prime_factor(12) == 3      # factors: 2, 3

    # Classic large example
    assert module_0.largest_prime_factor(13195) == 29  # 5 * 7 * 13 * 29

    # Power of a single prime
    assert module_0.largest_prime_factor(2048) == 2    # 2^11
    assert module_0.largest_prime_factor(243) == 3     # 3^5

    # Prime numbers themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Numbers with repeated prime factors
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2
    assert module_0.largest_prime_factor(60) == 5      # 2^2 * 3 * 5

    # Larger number
    assert module_0.largest_prime_factor(600851475143) == 6857

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 10:51:04.252751
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7      # 84 = 2^2 * 3 * 7

    # Prime inputs (largest prime factor is the number itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # Prime powers
    assert module_0.largest_prime_factor(4) == 2       # 4 = 2^2
    assert module_0.largest_prime_factor(49) == 7      # 49 = 7^2
    assert module_0.largest_prime_factor(8) == 2       # 8 = 2^3

    # Product of several primes
    assert module_0.largest_prime_factor(30030) == 13  # 2 * 3 * 5 * 7 * 11 * 13
    assert module_0.largest_prime_factor(210) == 7     # 2 * 3 * 5 * 7

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1       # no factors, default value
    assert module_0.largest_prime_factor(0) == 1       # loop never runs
    assert module_0.largest_prime_factor(-10) == 1     # negative input

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 10:51:18.588645
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(13) == 13

    # Prime number input (largest prime factor is itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(101) == 101

    # Powers of small primes
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(16) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(25) == 5
    assert module_0.largest_prime_factor(125) == 5

    # Products of multiple primes
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7) == 7
    assert module_0.largest_prime_factor(3 * 3 * 11) == 11
    assert module_0.largest_prime_factor(2 * 2 * 2 * 13) == 13

    # Larger composite numbers
    assert module_0.largest_prime_factor(600851475143) == 6857
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(1024) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 10:52:21.007383
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 3, 3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29

    # Small numbers
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(4) == 2       # factors: 2, 2

    # n itself is prime
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of primes
    assert module_0.largest_prime_factor(64) == 2      # 2^6
    assert module_0.largest_prime_factor(81) == 3      # 3^4

    # Composite with multiple distinct prime factors
    assert module_0.largest_prime_factor(100) == 5     # factors: 2, 5
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7 * 11) == 11
    assert module_0.largest_prime_factor(7 * 13 * 19) == 19

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1       # no prime factors, default
    assert module_0.largest_prime_factor(0) == 1       # loop never runs

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()
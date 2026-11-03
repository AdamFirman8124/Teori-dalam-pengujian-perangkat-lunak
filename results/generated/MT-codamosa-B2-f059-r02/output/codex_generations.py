

# Generated at 2026-11-02 18:13:01.284590
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # nonce:9482afb7
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 3^3
    assert module_0.largest_prime_factor(21) == 7      # 3 * 7
    assert module_0.largest_prime_factor(13195) == 29  # 5 * 7 * 13 * 29

    # Small / edge cases
    assert module_0.largest_prime_factor(1) == 1
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(4) == 2

    # Prime inputs return themselves
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(17) == 17
    assert module_0.largest_prime_factor(97) == 97

    # Numbers with repeated prime factors
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7      # 2^2 * 3 * 7
    assert module_0.largest_prime_factor(49) == 7      # 7^2
    assert module_0.largest_prime_factor(2310) == 11   # 2 * 3 * 5 * 7 * 11

# Generated at 2026-11-02 18:13:42.305175
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(12) == 3      # factors: 2, 2, 3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29

    # Prime input: largest prime factor is the number itself
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13

    # Powers of primes
    assert module_0.largest_prime_factor(4) == 2       # 2^2
    assert module_0.largest_prime_factor(8) == 2       # 2^3
    assert module_0.largest_prime_factor(9) == 3       # 3^2
    assert module_0.largest_prime_factor(16) == 2
    assert module_0.largest_prime_factor(1024) == 2

    # Composite with distinct primes
    assert module_0.largest_prime_factor(21) == 7      # 3 * 7
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2
    assert module_0.largest_prime_factor(66) == 11     # 2 * 3 * 11
    assert module_0.largest_prime_factor(84) == 7      # 2^2 * 3 * 7

    # Larger numbers
    assert module_0.largest_prime_factor(600851475143) == 6857
    assert module_0.largest_prime_factor(97) == 97
    assert module_0.largest_prime_factor(97 * 2) == 97

    # Edge case: n = 1 has no prime factors, loop never runs, returns 1
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-02 18:14:34.517516
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(63) == 7
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(330) == 11
    assert module_0.largest_prime_factor(13195) == 29

    # Powers of a single prime
    assert module_0.largest_prime_factor(2048) == 2
    assert module_0.largest_prime_factor(81) == 3
    assert module_0.largest_prime_factor(125) == 5

    # Prime inputs return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Product of distinct primes
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7 * 11) == 11

    # Larger composite
    assert module_0.largest_prime_factor(999) == 37

    # Edge case: n = 1 (loop never runs, returns initial value)
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-02 18:14:51.777360
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite number
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5

    # Classic example
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29

    # Prime number is its own largest prime factor
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3

    # Power of a single prime
    assert module_0.largest_prime_factor(16) == 2      # 2^4
    assert module_0.largest_prime_factor(27) == 3      # 3^3
    assert module_0.largest_prime_factor(125) == 5     # 5^3

    # Larger composite numbers
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7      # 2^2 * 3 * 7
    assert module_0.largest_prime_factor(9973) == 9973 # prime

    # Product of two primes
    assert module_0.largest_prime_factor(6) == 3       # 2 * 3
    assert module_0.largest_prime_factor(35) == 7      # 5 * 7

    # Large known case
    assert module_0.largest_prime_factor(600851475143) == 6857

    print("All tests passed!")


# Run tests
test_largest_prime_factor()

# Generated at 2026-11-02 18:15:47.904677
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # nonce:9b799eb1
    # Composite numbers with multiple prime factors
    assert module_0.largest_prime_factor(15) == 5      # 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 3**3
    assert module_0.largest_prime_factor(12) == 3      # 2**2 * 3
    assert module_0.largest_prime_factor(84) == 7      # 2**2 * 3 * 7
    assert module_0.largest_prime_factor(100) == 5     # 2**2 * 5**2
    assert module_0.largest_prime_factor(13195) == 29  # 5 * 7 * 13 * 29

    # Prime inputs return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Prime powers reduce to the base prime
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(16) == 2
    assert module_0.largest_prime_factor(2048) == 2
    assert module_0.largest_prime_factor(81) == 3
    assert module_0.largest_prime_factor(49) == 7

    # Edge case: no prime factors
    assert module_0.largest_prime_factor(1) == 1
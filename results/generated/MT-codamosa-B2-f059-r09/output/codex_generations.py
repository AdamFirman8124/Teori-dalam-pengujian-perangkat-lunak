

# Generated at 2026-11-02 11:01:14.534407
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    
    # Prime numbers are their own largest prime factor
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97
    
    # Powers of 2
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(1024) == 2
    
    # Composite numbers
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(60) == 5      # 60 = 2^2 * 3 * 5
    assert module_0.largest_prime_factor(84) == 7      # 84 = 2^2 * 3 * 7
    assert module_0.largest_prime_factor(102) == 17    # 102 = 2 * 3 * 17
    
    # Large number
    assert module_0.largest_prime_factor(600851475143) == 6857
    
    # Product of two primes
    assert module_0.largest_prime_factor(21) == 7      # 21 = 3 * 7
    assert module_0.largest_prime_factor(35) == 7      # 35 = 5 * 7
    
    print("All tests passed!")

# Generated at 2026-11-02 11:03:48.999287
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # 3^3
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2
    assert module_0.largest_prime_factor(84) == 7      # 2^2 * 3 * 7

    # Classic example: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # Prime inputs (number itself is its largest prime factor)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of two
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(1024) == 2

    # Large number
    assert module_0.largest_prime_factor(600851475143) == 6857

    # Edge case: n = 1 has no prime factors; loop never runs, returns 1
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()
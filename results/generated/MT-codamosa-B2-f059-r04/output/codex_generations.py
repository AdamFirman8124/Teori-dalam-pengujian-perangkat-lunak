

# Generated at 2026-11-03 06:18:42.404046
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases with composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # only prime factor is 3
    assert module_0.largest_prime_factor(12) == 3      # factors: 2, 3
    assert module_0.largest_prime_factor(100) == 5     # prime factors: 2, 5

    # Larger number with multiple prime factors
    assert module_0.largest_prime_factor(13195) == 29  # prime factors: 5, 7, 13, 29

    # Prime numbers (largest prime factor is itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1       # no prime factors, default value
    assert module_0.largest_prime_factor(4) == 2       # power of a prime

    # Product of two large primes
    assert module_0.largest_prime_factor(101 * 103) == 103

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-03 06:19:40.264372
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(2048) == 2

    # Classic example
    assert module_0.largest_prime_factor(13195) == 29

    # Prime inputs (number itself is the largest prime factor)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(97) == 97
    assert module_0.largest_prime_factor(6857) == 6857

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1
    assert module_0.largest_prime_factor(-10) == 1

# Generated at 2026-11-03 06:20:43.750401
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(63) == 7
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(100) == 5
    assert module_0.largest_prime_factor(97) == 97
    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:21:43.387593
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Classic example: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29
    # 15 = 3 * 5
    assert module_0.largest_prime_factor(15) == 5
    # 27 = 3^3
    assert module_0.largest_prime_factor(27) == 3
    # Prime number: largest prime factor is itself
    assert module_0.largest_prime_factor(17) == 17
    # Smallest prime
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    # Power of 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(64) == 2
    # Composite with multiple distinct primes: 100 = 2^2 * 5^2
    assert module_0.largest_prime_factor(100) == 5
    # 84 = 2^2 * 3 * 7
    assert module_0.largest_prime_factor(84) == 7
    # 21 = 3 * 7
    assert module_0.largest_prime_factor(21) == 7
    # 45 = 3^2 * 5
    assert module_0.largest_prime_factor(45) == 5
    # Large prime factor: 2 * 9973
    assert module_0.largest_prime_factor(19946) == 9973
    # Edge case: n = 1 has no prime factors, loop doesn't execute, returns initial value
    assert module_0.largest_prime_factor(1) == 1
    # 1024 = 2^10
    assert module_0.largest_prime_factor(1024) == 2
    # 97 is prime
    assert module_0.largest_prime_factor(97) == 97
    # 600 = 2^3 * 3 * 5^2
    assert module_0.largest_prime_factor(600) == 5
    # 12345 = 3 * 5 * 823
    assert module_0.largest_prime_factor(12345) == 823
    # 49 = 7^2
    assert module_0.largest_prime_factor(49) == 7
    print("All tests passed!")

# Generated at 2026-11-03 06:22:31.901550
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5, "Expected 5 for input 15 (factors: 3, 5)"
    assert module_0.largest_prime_factor(27) == 3, "Expected 3 for input 27 (3^3)"
    assert module_0.largest_prime_factor(13195) == 29, "Expected 29 for input 13195 (5*7*13*29)"

    # Prime number input: largest prime factor is itself
    assert module_0.largest_prime_factor(2) == 2, "Expected 2 for input 2"
    assert module_0.largest_prime_factor(13) == 13, "Expected 13 for input 13 (prime)"

    # Powers of small primes
    assert module_0.largest_prime_factor(4) == 2, "Expected 2 for input 4 (2^2)"
    assert module_0.largest_prime_factor(8) == 2, "Expected 2 for input 8 (2^3)"
    assert module_0.largest_prime_factor(9) == 3, "Expected 3 for input 9 (3^2)"
    assert module_0.largest_prime_factor(100) == 5, "Expected 5 for input 100 (2^2 * 5^2)"

    # Larger composite with distinct prime factors
    assert module_0.largest_prime_factor(91) == 13, "Expected 13 for input 91 (7*13)"
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7 * 11) == 11, "Expected 11 for input 2310"

    # Edge case: n = 1 has no prime factors, function returns initial value 1
    assert module_0.largest_prime_factor(1) == 1, "Expected 1 for input 1 (no prime factors)"

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:23:57.392678
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # nonce:4717d1d6

    # Basic composites
    assert module_0.largest_prime_factor(15) == 5      # 3 * 5
    assert module_0.largest_prime_factor(27) == 3      # 3^3
    assert module_0.largest_prime_factor(12) == 3      # 2^2 * 3
    assert module_0.largest_prime_factor(100) == 5     # 2^2 * 5^2

    # The number itself is prime -> largest prime factor is itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of 2 -> largest prime factor is 2
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(1024) == 2

    # Products of distinct primes
    assert module_0.largest_prime_factor(3 * 5 * 7) == 7
    assert module_0.largest_prime_factor(2 * 3 * 11) == 11
    assert module_0.largest_prime_factor(5 * 13 * 17) == 17

    # Classic example: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # Squares of primes
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(121) == 11

    # Edge case: 1 has no prime factors; loop never runs, initial value returned
    assert module_0.largest_prime_factor(1) == 1

    # Moderately large value (brute-force implementation stays fast)
    assert module_0.largest_prime_factor(2 * 3 * 7919) == 7919

    print("All largest_prime_factor tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:24:25.347155
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5        # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3        # factors: 3, 9 -> prime: 3
    assert module_0.largest_prime_factor(21) == 7        # factors: 3, 7
    assert module_0.largest_prime_factor(12) == 3        # factors: 2, 3, 4, 6 -> primes: 2, 3
    
    # Classic example
    assert module_0.largest_prime_factor(13195) == 29    # primes: 5, 7, 13, 29
    
    # Prime input (n itself is prime)
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(7) == 7
    
    # Powers of a prime
    assert module_0.largest_prime_factor(4) == 2         # 2^2
    assert module_0.largest_prime_factor(8) == 2         # 2^3
    assert module_0.largest_prime_factor(2048) == 2      # 2^11
    assert module_0.largest_prime_factor(81) == 3        # 3^4
    
    # Smallest valid input
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    
    # Edge case: no prime factors, returns initial value
    assert module_0.largest_prime_factor(1) == 1
    
    # Mixed factors with a larger prime
    assert module_0.largest_prime_factor(100) == 5       # primes: 2, 5
    assert module_0.largest_prime_factor(66) == 11       # primes: 2, 3, 11
    assert module_0.largest_prime_factor(105) == 7       # primes: 3, 5, 7
    assert module_0.largest_prime_factor(2 * 3 * 5 * 13) == 13
    
    # Squares and products of primes
    assert module_0.largest_prime_factor(49) == 7        # 7^2
    assert module_0.largest_prime_factor(121) == 11      # 11^2
    
    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:24:38.761275
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Composite numbers with multiple prime factors
    assert module_0.largest_prime_factor(15) == 5      # 15 = 3 * 5
    assert module_0.largest_prime_factor(21) == 7      # 21 = 3 * 7
    assert module_0.largest_prime_factor(13195) == 29  # 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(84) == 7      # 84 = 2^2 * 3 * 7

    # Prime powers
    assert module_0.largest_prime_factor(27) == 3      # 27 = 3^3
    assert module_0.largest_prime_factor(64) == 2      # 64 = 2^6
    assert module_0.largest_prime_factor(100) == 5     # 100 = 2^2 * 5^2

    # Prime inputs (number is its own largest prime factor)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(7) == 7
    assert module_0.largest_prime_factor(13) == 13

    # Mixed even/odd composites
    assert module_0.largest_prime_factor(10) == 5      # 10 = 2 * 5
    assert module_0.largest_prime_factor(6) == 3       # 6 = 2 * 3

    # Edge case: n = 1 has no prime factors, loop never runs, returns initial value
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-03 06:24:56.925776
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Small composite numbers
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(27) == 3
    assert module_0.largest_prime_factor(45) == 5
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # Prime inputs return the number itself
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Classic example: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # Edge case: no prime factors found, returns initial value
    assert module_0.largest_prime_factor(1) == 1

    print("All tests passed!")


test_largest_prime_factor()

# Generated at 2026-11-03 06:25:39.178347
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5, "15 = 3 * 5, largest prime factor is 5"
    assert module_0.largest_prime_factor(27) == 3, "27 = 3^3, only prime factor is 3"

    # Classic larger cases
    assert module_0.largest_prime_factor(13195) == 29, "13195 = 5 * 7 * 13 * 29"
    assert module_0.largest_prime_factor(2048) == 2, "2048 = 2^11, only prime factor is 2"

    # Prime number itself
    assert module_0.largest_prime_factor(13) == 13, "13 is prime, largest factor is itself"
    assert module_0.largest_prime_factor(2) == 2, "2 is the smallest prime"

    # Various composites
    assert module_0.largest_prime_factor(100) == 5, "100 = 2^2 * 5^2"
    assert module_0.largest_prime_factor(84) == 7, "84 = 2^2 * 3 * 7"
    assert module_0.largest_prime_factor(12) == 3, "12 = 2^2 * 3"
    assert module_0.largest_prime_factor(4) == 2, "4 = 2^2"

    # Edge case: 1 has no prime factors, initial value returned
    assert module_0.largest_prime_factor(1) == 1, "1 has no prime factors"

    # Large prime factor
    assert module_0.largest_prime_factor(2 * 3 * 997) == 997, "largest prime factor of 5982 is 997"

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:25:49.533938
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 3, 3
    assert module_0.largest_prime_factor(12) == 3      # factors: 2, 2, 3
    assert module_0.largest_prime_factor(100) == 5     # factors: 2, 2, 5, 5

    # Prime numbers are their own largest prime factor
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Larger number with multiple prime factors
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29
    assert module_0.largest_prime_factor(600851475143) == 6857

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1       # no prime factors, default remains 1
    assert module_0.largest_prime_factor(4) == 2       # factors: 2, 2

    # Number with repeated large prime factor
    assert module_0.largest_prime_factor(49) == 7      # factors: 7, 7
    assert module_0.largest_prime_factor(68) == 17     # factors: 2, 2, 17

# Generated at 2026-11-03 06:26:00.986918
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 9
    assert module_0.largest_prime_factor(63) == 7      # factors: 3, 7, 9, 21
    assert module_0.largest_prime_factor(100) == 5     # factors: 2, 4, 5, 10, ...

    # Classic example
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29

    # Prime input: largest prime factor is itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of a prime
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(81) == 3
    assert module_0.largest_prime_factor(1024) == 2

    # Large number
    assert module_0.largest_prime_factor(600851475143) == 6857

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:26:08.872795
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # 3^3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29
    assert module_0.largest_prime_factor(100) == 5     # factors: 2, 5
    assert module_0.largest_prime_factor(21) == 7      # factors: 3, 7

    # Prime inputs (largest prime factor is the number itself)
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97

    # Powers of two
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(1024) == 2

    # Product of two primes
    assert module_0.largest_prime_factor(2 * 3) == 3
    assert module_0.largest_prime_factor(11 * 7) == 11

    # Edge case: n = 1 has no prime factors, function returns initial value
    assert module_0.largest_prime_factor(1) == 1

    # Larger number: 600851475143 (Project Euler) is too slow for trial division,
    # so use a moderately large input
    assert module_0.largest_prime_factor(7919 * 104729) == 104729  # product of two primes

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:26:30.077069
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic composite numbers
    assert module_0.largest_prime_factor(15) == 5          # 3 * 5
    assert module_0.largest_prime_factor(27) == 3          # 3^3
    assert module_0.largest_prime_factor(12) == 3          # 2^2 * 3
    assert module_0.largest_prime_factor(100) == 5         # 2^2 * 5^2
    assert module_0.largest_prime_factor(13195) == 29      # 5 * 7 * 13 * 29

    # Prime inputs: largest prime factor is the number itself
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(97) == 97
    assert module_0.largest_prime_factor(7919) == 7919

    # Powers of two
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(1024) == 2

    # Mixed factors where the largest is not the last divisor found
    assert module_0.largest_prime_factor(10) == 5          # 2 * 5
    assert module_0.largest_prime_factor(21) == 7          # 3 * 7
    assert module_0.largest_prime_factor(45) == 5          # 3^2 * 5
    assert module_0.largest_prime_factor(330) == 11        # 2 * 3 * 5 * 11
    assert module_0.largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13) == 13

    # Edge cases
    assert module_0.largest_prime_factor(1) == 1           # no prime factors
    assert module_0.largest_prime_factor(0) == 1           # degenerate input

    # Larger values
    assert module_0.largest_prime_factor(510) == 17        # 2 * 3 * 5 * 17
    assert module_0.largest_prime_factor(9973) == 9973     # large prime

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()

# Generated at 2026-11-03 06:26:43.076028
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # Basic cases
    assert module_0.largest_prime_factor(15) == 5      # factors: 3, 5
    assert module_0.largest_prime_factor(27) == 3      # factors: 3, 3, 3
    assert module_0.largest_prime_factor(13195) == 29  # factors: 5, 7, 13, 29

    # Prime number itself
    assert module_0.largest_prime_factor(13) == 13
    assert module_0.largest_prime_factor(2) == 2

    # Powers of a prime
    assert module_0.largest_prime_factor(8) == 2       # 2^3
    assert module_0.largest_prime_factor(81) == 3      # 3^4

    # Composite with multiple prime factors
    assert module_0.largest_prime_factor(100) == 5     # factors: 2^2 * 5^2
    assert module_0.largest_prime_factor(60) == 5      # factors: 2^2 * 3 * 5
    assert module_0.largest_prime_factor(84) == 7      # factors: 2^2 * 3 * 7

    # Edge case: 1 has no prime factors, function returns default 1
    assert module_0.largest_prime_factor(1) == 1

    # Large prime
    assert module_0.largest_prime_factor(97) == 97

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_prime_factor()
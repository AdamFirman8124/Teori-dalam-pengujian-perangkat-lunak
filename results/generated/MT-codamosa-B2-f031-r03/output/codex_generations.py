

# Generated at 2026-11-03 02:25:46.091180
# Unit test for function is_prime
def test_is_prime():
    # nonce:1e6a4c16
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes (edge cases for empty loop range)
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(15) == False

    # Larger primes
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True

    # Larger composites (including perfect square of a prime)
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(121) == False

    print("All test cases passed!")


test_is_prime()

# Generated at 2026-11-03 02:28:06.956506
# Unit test for function is_prime
def test_is_prime():
    # Edge cases: numbers below 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Small primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True

    # Small composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(12) == False
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(27) == False

    # Larger primes
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True

    # Larger composites (products of two primes)
    assert module_0.is_prime(5 * 17) == False
    assert module_0.is_prime(11 * 13) == False
    assert module_0.is_prime(13441 * 19) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-03 02:30:10.070406
# Unit test for function is_prime
def test_is_prime():
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-5) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Small primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True

    # Small composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False

    # Larger primes
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True

    # Larger composites
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(100) == False

    print("All tests passed!")


test_is_prime()

# Generated at 2026-11-03 02:31:53.908249
# Unit test for function is_prime
def test_is_prime():
    # nonce:ee4eca09
    # Numbers below 2 are not prime
    assert module_0.is_prime(-7) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes (loop range is empty for these)
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(101) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False

    # Products of two primes
    assert module_0.is_prime(5 * 17) == False
    assert module_0.is_prime(11 * 7) == False

    # Larger numbers
    assert module_0.is_prime(13441) == True
    assert module_0.is_prime(13441 * 19) == False

# Generated at 2026-11-03 02:33:18.188112
# Unit test for function is_prime
def test_is_prime():
# nonce:a2b1e7c9
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False

    # Primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(7919) == True

    # Larger composite numbers
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False      # 7 * 7
    assert module_0.is_prime(91) == False      # 7 * 13
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(7917) == False

    # Squares of primes (edge cases for divisor checking)
    assert module_0.is_prime(121) == False     # 11 * 11
    assert module_0.is_prime(169) == False     # 13 * 13

    print("All tests passed!")


if __name__ == "__main__":
    test_is_prime()
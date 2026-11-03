

# Generated at 2026-11-03 00:51:18.899086
# Unit test for function is_prime
def test_is_prime():
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-7) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True

    # Small composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False

    # Larger primes
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True

    # Larger composite numbers
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(121) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-03 00:52:39.398137
# Unit test for function is_prime
def test_is_prime():
# nonce:f7b3a6fd
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13441) == True
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(1) == False
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(20) == False
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(79) == True
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(31) == True

# Generated at 2026-11-03 00:53:57.282253
# Unit test for function is_prime
def test_is_prime():
    # Edge cases: numbers below 2 are not prime
    assert module_0.is_prime(-5) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(12) == False

    # Primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(31) == True
    assert module_0.is_prime(97) == True

    # Larger composites (including perfect squares of primes)
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False
    assert module_0.is_prime(100) == False

    # Larger prime
    assert module_0.is_prime(7919) == True

    print("All tests passed!")


# nonce:532666c3
test_is_prime()

# Generated at 2026-11-03 00:55:53.930280
# Unit test for function is_prime
def test_is_prime():
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-10) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest prime numbers
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(100) == False

    # Larger prime numbers
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True

    print("All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-03 00:56:49.263307
# Unit test for function is_prime
def test_is_prime():
    # nonce:8857e43b
    # Non-primes and edge cases below 2
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(-7) == False

    # Small primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(17) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False

    # Larger primes
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(13441) == True

    # Products of primes (composites)
    assert module_0.is_prime(5 * 17) == False
    assert module_0.is_prime(11 * 17) == False
    assert module_0.is_prime(13441 * 19) == False
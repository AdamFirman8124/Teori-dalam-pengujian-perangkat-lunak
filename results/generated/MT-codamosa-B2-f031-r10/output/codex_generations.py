

# Generated at 2026-11-02 08:53:54.315098
# Unit test for function is_prime
def test_is_prime():
    # Edge cases: values below 2 are not prime
    assert module_0.is_prime(-7) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True

    # Small composites
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
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(5 * 17) == False
    assert module_0.is_prime(11 * 13) == False

# Generated at 2026-11-02 08:54:34.276953
# Unit test for function is_prime
def test_is_prime():
    # Non-prime numbers less than 2
    assert module_0.is_prime(-10) == False
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

    # Small non-primes
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(15) == False

    # Larger primes
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True
    assert module_0.is_prime(13441) == True

    # Larger non-primes
    assert module_0.is_prime(85) == False
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(13442) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-02 08:57:34.092085
# Unit test for function is_prime
def test_is_prime():# Numbers less than 2 are not prime
    assert module_0.is_prime(-5) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Small primes
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
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True
    assert module_0.is_prime(13441) == True

    # Larger composite numbers
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(13442) == False
    assert module_0.is_prime(5 * 17) == False
    assert module_0.is_prime(11 * 7) == False

# Generated at 2026-11-02 08:58:48.496291
# Unit test for function is_prime
def test_is_prime():
    # Numbers less than 2 are not prime
    assert module_0.is_prime(-5) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Smallest primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False

    # Larger primes
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True

    # Larger composites
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(121) == False  # 11 * 11
    assert module_0.is_prime(7917) == False

    # Edge cases: perfect squares and even numbers
    assert module_0.is_prime(49) == False  # 7 * 7
    assert module_0.is_prime(2 * 2) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-02 09:00:50.129265
# Unit test for function is_prime
def test_is_prime():
    # nonce:f4f4d85b
    # Edge cases: n < 2
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
    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(12) == False
    assert module_0.is_prime(15) == False
    # Larger values
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(101) == True
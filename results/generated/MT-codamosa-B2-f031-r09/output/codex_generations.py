

# Generated at 2026-11-02 21:04:09.253933
# Unit test for function is_prime
def test_is_prime():
    # nonce:4ae8fcfb
    # Numbers below 2 are not prime
    assert module_0.is_prime(-7) == False
    assert module_0.is_prime(-1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(1) == False

    # Boundary primes (loop body never executes for these)
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True

    # Small primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True

    # Larger primes
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True

    # Composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(12) == False
    assert module_0.is_prime(15) == False

    # Perfect squares of primes (edge cases for the divisor loop)
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False

    # Large composite
    assert module_0.is_prime(100) == False


if __name__ == "__main__":
    test_is_prime()
    print("All tests passed!")

# Generated at 2026-11-02 21:04:46.812265
# Unit test for function is_prime
def test_is_prime():assert module_0.is_prime(-7) == False

# Generated at 2026-11-02 21:05:46.913420
# Unit test for function is_prime
def test_is_prime():
    # Numbers less than 2 are not prime
    assert module_0.is_prime(1) == False
    assert module_0.is_prime(0) == False
    assert module_0.is_prime(-7) == False

    # Small primes
    assert module_0.is_prime(2) == True
    assert module_0.is_prime(3) == True
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True

    # Small composites
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(25) == False

    # Larger primes
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(61) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True
    assert module_0.is_prime(13441) == True

    # Larger composites
    assert module_0.is_prime(5 * 13) == False
    assert module_0.is_prime(13441 * 19) == False
    assert module_0.is_prime(100) == False


test_is_prime()

# Generated at 2026-11-02 21:06:25.454062
# Unit test for function is_prime
def test_is_prime():
    # Non-positive and numbers less than 2 are not prime
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

    # Small composite numbers
    assert module_0.is_prime(4) == False
    assert module_0.is_prime(6) == False
    assert module_0.is_prime(8) == False
    assert module_0.is_prime(9) == False
    assert module_0.is_prime(10) == False
    assert module_0.is_prime(12) == False
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False

    # Perfect squares (composite)
    assert module_0.is_prime(25) == False   # 5 * 5
    assert module_0.is_prime(49) == False   # 7 * 7
    assert module_0.is_prime(121) == False  # 11 * 11

    # Larger primes
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True
    assert module_0.is_prime(101) == True
    assert module_0.is_prime(7919) == True

    # Larger composites
    assert module_0.is_prime(100) == False
    assert module_0.is_prime(7917) == False

    print("All is_prime tests passed!")


if __name__ == "__main__":
    test_is_prime()

# Generated at 2026-11-02 21:07:34.409057
# Unit test for function is_prime
def test_is_prime():
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

    # Larger primes
    assert module_0.is_prime(5) == True
    assert module_0.is_prime(7) == True
    assert module_0.is_prime(11) == True
    assert module_0.is_prime(13) == True
    assert module_0.is_prime(17) == True
    assert module_0.is_prime(19) == True
    assert module_0.is_prime(23) == True
    assert module_0.is_prime(29) == True
    assert module_0.is_prime(97) == True

    # Larger composite numbers
    assert module_0.is_prime(15) == False
    assert module_0.is_prime(21) == False
    assert module_0.is_prime(25) == False
    assert module_0.is_prime(49) == False
    assert module_0.is_prime(100) == False
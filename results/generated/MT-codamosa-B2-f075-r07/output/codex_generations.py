

# Generated at 2026-11-02 09:15:50.563057
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # nonce:ec3447ae
    # True cases: numbers that are products of exactly three primes
    assert module_0.is_multiply_prime(30) == True      # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True       # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True      # 2 * 2 * 3
    assert module_0.is_multiply_prime(105) == True     # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True     # 5 * 5 * 5
    assert module_0.is_multiply_prime(18818) == True   # 2 * 97 * 97
    assert module_0.is_multiply_prime(912673) == True  # 97 * 97 * 97

    # False cases
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False      # prime itself
    assert module_0.is_multiply_prime(5) == False      # prime itself
    assert module_0.is_multiply_prime(6) == False      # 2 * 3, only two primes
    assert module_0.is_multiply_prime(10) == False     # 2 * 5, only two primes
    assert module_0.is_multiply_prime(49) == False     # 7 * 7, only two primes
    assert module_0.is_multiply_prime(64) == False     # 2^6, six prime factors
    assert module_0.is_multiply_prime(100) == False    # 2 * 2 * 5 * 5, four prime factors
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False

# Generated at 2026-11-02 09:17:57.745221
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Products of exactly three primes (primes may repeat)
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(66) == True    # 2 * 3 * 11
    assert module_0.is_multiply_prime(98) == True    # 2 * 7 * 7
    assert module_0.is_multiply_prime(99) == True    # 3 * 3 * 11

    # Not a product of exactly three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False    # prime itself
    assert module_0.is_multiply_prime(4) == False    # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(5) == False    # prime
    assert module_0.is_multiply_prime(6) == False    # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(7) == False    # prime
    assert module_0.is_multiply_prime(9) == False    # 3 * 3 (only two primes)
    assert module_0.is_multiply_prime(16) == False   # 2^4 (four primes)
    assert module_0.is_multiply_prime(60) == False   # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(64) == False   # 2^6 (six primes)
    assert module_0.is_multiply_prime(100) == False  # 2^2 * 5^2 (four primes)

    # Edge cases: numbers too small or with non-prime factors
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False  # negative input

    # Largest product of three primes within loop bounds (all < 101)
    assert module_0.is_multiply_prime(97 * 89 * 83) == True
    # Product exceeding achievable range
    assert module_0.is_multiply_prime(101 * 101 * 101) == False

    print("All tests passed!")


test_is_multiply_prime()

# Generated at 2026-11-02 09:19:01.637493
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that are products of exactly three primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(18) == True   # 2 * 3 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(60) == True   # 2 * 2 * 15? No -> 2*2*3*5 (4 factors)
    # Correction: 60 has four prime factors, should be False
    assert module_0.is_multiply_prime(60) == False

    # Numbers that are not products of three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False   # single prime
    assert module_0.is_multiply_prime(3) == False   # single prime
    assert module_0.is_multiply_prime(4) == False   # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(6) == False   # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(9) == False   # 3 * 3 (only two primes)
    assert module_0.is_multiply_prime(11) == False  # prime
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(16) == False  # 2^4 (four prime factors)
    assert module_0.is_multiply_prime(24) == False  # 2^3 * 3 (four prime factors)

    print("test_is_multiply_prime passed!")

# Generated at 2026-11-02 09:22:02.703391
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
# nonce:7f9908e9
    # Numbers that are products of exactly three primes
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(66) == True    # 2 * 3 * 11

    # Numbers that are not products of exactly three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(2) == False    # prime
    assert module_0.is_multiply_prime(5) == False    # prime
    assert module_0.is_multiply_prime(15) == False   # product of two primes (3 * 5)
    assert module_0.is_multiply_prime(60) == False   # product of four primes (2*2*3*5)
    assert module_0.is_multiply_prime(64) == False   # 2^6, not expressible as 3 primes
    assert module_0.is_multiply_prime(100) == False  # 2^2 * 5^2
    assert module_0.is_multiply_prime(-30) == False  # negative input

    print("All tests passed!")

# Generated at 2026-11-02 09:24:52.670982
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # True cases: product of exactly three primes
    assert module_0.is_multiply_prime(8) == True      # 2*2*2
    assert module_0.is_multiply_prime(12) == True     # 2*2*3
    assert module_0.is_multiply_prime(30) == True     # 2*3*5
    assert module_0.is_multiply_prime(105) == True    # 3*5*7
    assert module_0.is_multiply_prime(125) == True    # 5*5*5
    assert module_0.is_multiply_prime(2 * 3 * 97) == True

    # False cases: fewer or more than three prime factors
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(5) == False     # single prime
    assert module_0.is_multiply_prime(6) == False     # 2*3, only two primes
    assert module_0.is_multiply_prime(24) == False    # 2*2*2*3, four primes
    assert module_0.is_multiply_prime(64) == False    # 4^3, not three primes
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_multiply_prime()


# Generated at 2026-11-02 16:52:20.578974
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # not a product of three primes
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(10) == False          # 2 * 5 (only two primes)
    assert module_0.is_multiply_prime(3 * 6 * 7) == False   # 6 is not prime
    assert module_0.is_multiply_prime(8 * 9 * 10) == False
    assert module_0.is_multiply_prime(11 * 9 * 9) == False  # 9 is not prime
    assert module_0.is_multiply_prime(64) == False          # 2^6, cannot be split into 3 primes

    # valid products of three primes
    assert module_0.is_multiply_prime(8) == True            # 2 * 2 * 2
    assert module_0.is_multiply_prime(27) == True           # 3 * 3 * 3
    assert module_0.is_multiply_prime(30) == True           # 2 * 3 * 5
    assert module_0.is_multiply_prime(125) == True          # 5 * 5 * 5
    assert module_0.is_multiply_prime(3 * 5 * 7) == True    # 105
    assert module_0.is_multiply_prime(11 * 13 * 7) == True  # 1001
    assert module_0.is_multiply_prime(2 * 2 * 97) == True   # 388, primes at range boundary
    assert module_0.is_multiply_prime(2 * 3 * 97) == True   # 582

# Generated at 2026-11-02 16:54:09.361097
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
# nonce:114d0d65
    # True cases: product of exactly three primes
    assert module_0.is_multiply_prime(8) == True       # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True      # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True      # 3 * 3 * 3
    assert module_0.is_multiply_prime(30) == True      # 2 * 3 * 5
    assert module_0.is_multiply_prime(98) == True      # 2 * 7 * 7
    assert module_0.is_multiply_prime(99) == True      # 3 * 3 * 11
    assert module_0.is_multiply_prime(105) == True     # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True     # 5 * 5 * 5
    assert module_0.is_multiply_prime(18818) == True   # 2 * 97 * 97

    # False cases: primes themselves
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(7) == False
    assert module_0.is_multiply_prime(97) == False

    # False cases: products of only two primes
    assert module_0.is_multiply_prime(4) == False      # 2 * 2
    assert module_0.is_multiply_prime(6) == False      # 2 * 3
    assert module_0.is_multiply_prime(49) == False     # 7 * 7

    # False cases: products of four or more primes
    assert module_0.is_multiply_prime(16) == False     # 2^4
    assert module_0.is_multiply_prime(60) == False     # 2 * 2 * 3 * 5
    assert module_0.is_multiply_prime(64) == False     # 2^6
    assert module_0.is_multiply_prime(100) == False    # 2 * 2 * 5 * 5
    assert module_0.is_multiply_prime(210) == False    # 2 * 3 * 5 * 7
    assert module_0.is_multiply_prime(930) == False    # 2 * 3 * 5 * 31

    # False cases: edge values
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(5) == False

# Generated at 2026-11-02 16:56:15.151376
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that are products of exactly 3 primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True  # 5 * 5 * 5
    assert module_0.is_multiply_prime(66) == True   # 2 * 3 * 11
    assert module_0.is_multiply_prime(70) == True   # 2 * 5 * 7
    assert module_0.is_multiply_prime(98) == True   # 2 * 7 * 7

    # Numbers that are not products of exactly 3 primes
    assert module_0.is_multiply_prime(2) == False   # prime itself
    assert module_0.is_multiply_prime(6) == False   # 2 * 3 (only 2 primes)
    assert module_0.is_multiply_prime(1) == False   # not a product of primes
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(7) == False   # prime
    assert module_0.is_multiply_prime(100) == False # 2 * 2 * 5 * 5 (4 primes)
    assert module_0.is_multiply_prime(36) == False  # 2 * 2 * 3 * 3 (4 primes)
    assert module_0.is_multiply_prime(64) == False  # 2^6 (6 primes)
    assert module_0.is_multiply_prime(15) == False  # 3 * 5 (only 2 primes)
    assert module_0.is_multiply_prime(210) == False # 2 * 3 * 5 * 7 (4 primes)

    print("All tests passed!")

# Generated at 2026-11-02 16:58:10.132863
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # True cases: product of exactly three primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True  # 5 * 5 * 5

    # False cases
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(4) == False   # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(6) == False   # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(7) == False   # prime itself
    assert module_0.is_multiply_prime(64) == False  # 2^6 (six primes)
    assert module_0.is_multiply_prime(100) == False # 2^2 * 5^2 (four primes)
    assert module_0.is_multiply_prime(210) == False # 2 * 3 * 5 * 7 (four primes)

    print("All tests passed!")
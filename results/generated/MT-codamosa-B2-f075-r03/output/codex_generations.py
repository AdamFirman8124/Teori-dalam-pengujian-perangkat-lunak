

# Generated at 2026-11-03 03:14:43.559183
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # nonce:ddd4729b
    # Products of exactly three primes -> True
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(18) == True    # 2 * 3 * 3
    assert module_0.is_multiply_prime(20) == True    # 2 * 2 * 5
    assert module_0.is_multiply_prime(28) == True    # 2 * 2 * 7
    assert module_0.is_multiply_prime(70) == True    # 2 * 5 * 7

    # Not a product of exactly three primes -> False
    assert module_0.is_multiply_prime(1) == False    # not a product of primes
    assert module_0.is_multiply_prime(2) == False    # single prime
    assert module_0.is_multiply_prime(5) == False    # single prime
    assert module_0.is_multiply_prime(6) == False    # 2 * 3 (two primes)
    assert module_0.is_multiply_prime(4) == False    # 2 * 2 (two primes)
    assert module_0.is_multiply_prime(9) == False    # 3 * 3 (two primes)
    assert module_0.is_multiply_prime(60) == False   # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(100) == False  # 2 * 2 * 5 * 5 (four primes)
    assert module_0.is_multiply_prime(210) == False  # 2 * 3 * 5 * 7 (four primes)
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(7) == False    # single prime

    # Large valid case within search bounds
    assert module_0.is_multiply_prime(97 * 89 * 83) == True

# Generated at 2026-11-03 03:15:58.309018
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # nonce:77e62b64
    # True cases: products of exactly 3 primes (not necessarily distinct)
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(18) == True    # 2 * 3 * 3
    assert module_0.is_multiply_prime(70) == True    # 2 * 5 * 7

    # False cases: fewer than 3 prime factors
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(3) == False
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(4) == False    # 2 * 2 (only 2 primes)
    assert module_0.is_multiply_prime(6) == False    # 2 * 3
    assert module_0.is_multiply_prime(9) == False    # 3 * 3
    assert module_0.is_multiply_prime(1) == False

    # False cases: more than 3 prime factors
    assert module_0.is_multiply_prime(16) == False   # 2^4
    assert module_0.is_multiply_prime(64) == False   # 2^6
    assert module_0.is_multiply_prime(210) == False  # 2 * 3 * 5 * 7
    assert module_0.is_multiply_prime(100) == False  # 2^2 * 5^2

    # False cases: non-prime factors / special values
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(36) == False   # 6 * 6 * 1, 2^2 * 3^2

    print("All tests passed!")

# Generated at 2026-11-03 03:18:16.552870
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Product of three distinct primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(70) == True   # 2 * 5 * 7
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7

    # Product with repeated primes
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True  # 5 * 5 * 5

    # Single primes are not a product of three primes
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(97) == False

    # Product of only two primes
    assert module_0.is_multiply_prime(4) == False   # 2 * 2
    assert module_0.is_multiply_prime(6) == False   # 2 * 3
    assert module_0.is_multiply_prime(15) == False  # 3 * 5

    # Product of four primes
    assert module_0.is_multiply_prime(16) == False  # 2 * 2 * 2 * 2
    assert module_0.is_multiply_prime(24) == False  # 2 * 2 * 2 * 3

    # Trivial / edge cases
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(-30) == False

    # Boundary: largest product of three primes within loop range
    assert module_0.is_multiply_prime(97 * 97 * 97) == True  # 912673

    # Prime factor outside the search range (101 > 100 is never checked)
    assert module_0.is_multiply_prime(2 * 101 * 101) == False

test_is_multiply_prime()
print("All tests passed!")

# Generated at 2026-11-03 03:20:18.410854
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that are products of exactly three primes
    assert module_0.is_multiply_prime(8) == True    # 2*2*2
    assert module_0.is_multiply_prime(12) == True   # 2*2*3
    assert module_0.is_multiply_prime(18) == True   # 2*3*3
    assert module_0.is_multiply_prime(27) == True   # 3*3*3
    assert module_0.is_multiply_prime(30) == True   # 2*3*5
    assert module_0.is_multiply_prime(105) == True  # 3*5*7

    # Prime numbers are not products of three primes
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(11) == False
    assert module_0.is_multiply_prime(97) == False

    # Products of two primes are not products of three primes
    assert module_0.is_multiply_prime(4) == False   # 2*2
    assert module_0.is_multiply_prime(6) == False   # 2*3
    assert module_0.is_multiply_prime(15) == False  # 3*5

    # Products of four primes are not products of exactly three primes
    assert module_0.is_multiply_prime(16) == False  # 2*2*2*2
    assert module_0.is_multiply_prime(81) == False  # 3*3*3*3

    # Edge cases
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-8) == False

    print("All tests passed!")


test_is_multiply_prime()

# Generated at 2026-11-03 03:21:53.128453
# Unit test for function is_multiply_prime
def test_is_multiply_prime():assert module_0.is_multiply_prime(8) == True      # 2*2*2
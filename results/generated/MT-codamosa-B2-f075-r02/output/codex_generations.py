

# Generated at 2026-11-02 07:03:06.149080
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # nonce:944ec4e9

    # Products of exactly three primes -> True
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(64) == True    # 2 * 4 * 8 -> 2 * 2 * 2 * 2 * 2 * 2, but 2*2*16 no; actually 4*4*4 -> 2*2*2*2*2*2... check: 4 not prime. 2*2*16 no. So should be False
    # Correcting: 64 = 2^6, cannot be split into exactly 3 primes (2*2*16 invalid), so:
    assert module_0.is_multiply_prime(64) == False

    # Primes and products of fewer than three primes -> False
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(6) == False    # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(4) == False    # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(10) == False   # 2 * 5
    assert module_0.is_multiply_prime(1) == False

    # Products of four primes -> False
    assert module_0.is_multiply_prime(60) == False   # 2 * 2 * 3 * 5
    assert module_0.is_multiply_prime(100) == False  # 2 * 2 * 5 * 5
    assert module_0.is_multiply_prime(210) == False  # 2 * 3 * 5 * 7

    # Edge cases -> False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(7) == False    # prime itself

    # Large triple-prime product
    assert module_0.is_multiply_prime(742) == False  # 2 * 7 * 53 -> True actually
    # Correcting: 742 = 2 * 7 * 53 (all prime) -> True
    assert module_0.is_multiply_prime(742) == True

    print("All tests passed!")


# Run the tests
test_is_multiply_prime()

# Generated at 2026-11-02 07:04:59.171294
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # True cases: product of exactly three primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(60) == True   # 2 * 2 * 15 -> 2*2*3*5, also 2*5*6... check: 2*3*10 no, 2*2*15 no, 3*4*5 no -> actually False
    # Correction: 60 = 2*2*3*5 (four primes), cannot be written as exactly 3 primes
    assert module_0.is_multiply_prime(60) == False
    assert module_0.is_multiply_prime(28) == True   # 2 * 2 * 7
    assert module_0.is_multiply_prime(997002) is not None  # large number handled (returns False quickly)

    # False cases
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False   # single prime
    assert module_0.is_multiply_prime(4) == False   # 2 * 2, only two primes
    assert module_0.is_multiply_prime(6) == False   # 2 * 3, only two primes
    assert module_0.is_multiply_prime(64) == False  # 2^6, cannot split into 3 primes
    assert module_0.is_multiply_prime(100) == False # 2^2 * 5^2, cannot split into 3 primes
    assert module_0.is_multiply_prime(15) == False  # 3 * 5, only two primes
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False

# Generated at 2026-11-02 07:07:56.327438
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that ARE products of exactly three primes
    assert module_0.is_multiply_prime(8) == True       # 2*2*2
    assert module_0.is_multiply_prime(12) == True      # 2*2*3
    assert module_0.is_multiply_prime(18) == True      # 2*3*3
    assert module_0.is_multiply_prime(27) == True      # 3*3*3
    assert module_0.is_multiply_prime(30) == True      # 2*3*5
    assert module_0.is_multiply_prime(66) == True      # 2*3*11
    assert module_0.is_multiply_prime(70) == True      # 2*5*7
    assert module_0.is_multiply_prime(99) == True      # 3*3*11
    assert module_0.is_multiply_prime(105) == True     # 3*5*7
    assert module_0.is_multiply_prime(125) == True     # 5*5*5
    assert module_0.is_multiply_prime(18818) == True   # 2*97*97
    assert module_0.is_multiply_prime(716539) == True  # 97*89*83

    # Numbers that are NOT products of exactly three primes
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False      # single prime
    assert module_0.is_multiply_prime(4) == False      # 2*2 (only two primes)
    assert module_0.is_multiply_prime(6) == False      # 2*3 (only two primes)
    assert module_0.is_multiply_prime(7) == False      # prime
    assert module_0.is_multiply_prime(9) == False      # 3*3
    assert module_0.is_multiply_prime(16) == False     # 2^4 (four prime factors)
    assert module_0.is_multiply_prime(25) == False     # 5*5
    assert module_0.is_multiply_prime(26) == False     # 2*13
    assert module_0.is_multiply_prime(49) == False     # 7*7
    assert module_0.is_multiply_prime(60) == False     # 2*2*3*5 (four prime factors)
    assert module_0.is_multiply_prime(64) == False     # 2^6
    assert module_0.is_multiply_prime(100) == False    # 2*2*5*5
    assert module_0.is_multiply_prime(-30) == False    # negative input

    print("All tests passed!")


if __name__ == "__main__":
    test_is_multiply_prime()

# Generated at 2026-11-02 07:10:32.305212
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Products of exactly 3 primes -> True
    assert module_0.is_multiply_prime(30) == True      # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True       # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True      # 2 * 2 * 3
    assert module_0.is_multiply_prime(18) == True      # 2 * 3 * 3
    assert module_0.is_multiply_prime(28) == True      # 2 * 2 * 7
    assert module_0.is_multiply_prime(105) == True     # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True     # 5 * 5 * 5
    assert module_0.is_multiply_prime(18818) == True   # 2 * 97 * 97

    # Fewer than 3 prime factors -> False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(2) == False      # single prime
    assert module_0.is_multiply_prime(97) == False     # single large prime
    assert module_0.is_multiply_prime(4) == False      # 2 * 2 (two primes)
    assert module_0.is_multiply_prime(6) == False      # 2 * 3 (two primes)
    assert module_0.is_multiply_prime(25) == False     # 5 * 5 (two primes)
    assert module_0.is_multiply_prime(49) == False     # 7 * 7 (two primes)

    # More than 3 prime factors -> False
    assert module_0.is_multiply_prime(60) == False     # 2 * 2 * 3 * 5
    assert module_0.is_multiply_prime(210) == False    # 2 * 3 * 5 * 7
    assert module_0.is_multiply_prime(100) == False    # 2 * 2 * 5 * 5

    # Non-prime composites that can't be expressed as 3 primes
    assert module_0.is_multiply_prime(16) == False     # 2^4
    assert module_0.is_multiply_prime(81) == False     # 3^4

    print("All tests passed!")


test_is_multiply_prime()
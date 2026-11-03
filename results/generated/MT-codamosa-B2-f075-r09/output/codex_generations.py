

# Generated at 2026-11-02 10:34:43.327449
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that ARE products of exactly three primes
    assert module_0.is_multiply_prime(8) == True     # 2*2*2
    assert module_0.is_multiply_prime(12) == True    # 2*2*3
    assert module_0.is_multiply_prime(18) == True    # 2*3*3
    assert module_0.is_multiply_prime(20) == True    # 2*2*5
    assert module_0.is_multiply_prime(27) == True    # 3*3*3
    assert module_0.is_multiply_prime(28) == True    # 2*2*7
    assert module_0.is_multiply_prime(30) == True    # 2*3*5
    assert module_0.is_multiply_prime(42) == True    # 2*3*7
    assert module_0.is_multiply_prime(45) == True    # 3*3*5
    assert module_0.is_multiply_prime(70) == True    # 2*5*7
    assert module_0.is_multiply_prime(105) == True   # 3*5*7
    assert module_0.is_multiply_prime(125) == True   # 5*5*5
    assert module_0.is_multiply_prime(343) == True   # 7*7*7
    assert module_0.is_multiply_prime(582) == True   # 2*3*97 (largest primes in range)

    # Numbers that are NOT products of exactly three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(2) == False    # single prime
    assert module_0.is_multiply_prime(5) == False    # single prime
    assert module_0.is_multiply_prime(97) == False   # single prime
    assert module_0.is_multiply_prime(4) == False    # 2*2 (two primes)
    assert module_0.is_multiply_prime(6) == False    # 2*3 (two primes)
    assert module_0.is_multiply_prime(9) == False    # 3*3 (two primes)
    assert module_0.is_multiply_prime(25) == False   # 5*5 (two primes)
    assert module_0.is_multiply_prime(49) == False   # 7*7 (two primes)
    assert module_0.is_multiply_prime(16) == False   # 2*2*2*2 (four primes)
    assert module_0.is_multiply_prime(60) == False   # 2*2*3*5 (four primes)
    assert module_0.is_multiply_prime(210) == False  # 2*3*5*7 (four primes)
    assert module_0.is_multiply_prime(15) == False   # 3*5 (two primes)

    print("All tests passed!")


if __name__ == "__main__":
    test_is_multiply_prime()

# Generated at 2026-11-02 10:36:16.829457
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Test with product of three distinct primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(70) == True   # 2 * 5 * 7
    assert module_0.is_multiply_prime(42) == True   # 2 * 3 * 7

    # Test with repeated primes
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True  # 5 * 5 * 5
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(18) == True   # 2 * 3 * 3
    assert module_0.is_multiply_prime(20) == True   # 2 * 2 * 5

    # Test with numbers that are not products of exactly three primes
    assert module_0.is_multiply_prime(1) == False   # 1 is not a product of primes
    assert module_0.is_multiply_prime(2) == False   # single prime
    assert module_0.is_multiply_prime(4) == False   # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(6) == False   # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(60) == False  # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(100) == False # 2 * 2 * 5 * 5 (four primes)
    assert module_0.is_multiply_prime(0) == False   # zero
    assert module_0.is_multiply_prime(-8) == False  # negative number

    # Test edge cases
    assert module_0.is_multiply_prime(97 * 97 * 97) == True  # large prime cubed
    assert module_0.is_multiply_prime(2 * 97 * 97) == True   # large primes product

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_multiply_prime()

# Generated at 2026-11-02 10:37:53.178146
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
# nonce:dcd3c3f2
    # Should return True: products of exactly three primes
    assert module_0.is_multiply_prime(8) == True      # 2*2*2
    assert module_0.is_multiply_prime(12) == True     # 2*2*3
    assert module_0.is_multiply_prime(27) == True     # 3*3*3
    assert module_0.is_multiply_prime(30) == True     # 2*3*5
    assert module_0.is_multiply_prime(66) == True     # 2*3*11
    assert module_0.is_multiply_prime(99) == True     # 3*3*11
    assert module_0.is_multiply_prime(105) == True    # 3*5*7
    assert module_0.is_multiply_prime(125) == True    # 5*5*5
    assert module_0.is_multiply_prime(343) == True    # 7*7*7

    # Should return False: not a product of exactly three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False
    assert module_0.is_multiply_prime(2) == False     # prime
    assert module_0.is_multiply_prime(4) == False     # 2*2 (only two primes)
    assert module_0.is_multiply_prime(6) == False     # 2*3
    assert module_0.is_multiply_prime(9) == False     # 3*3
    assert module_0.is_multiply_prime(15) == False    # 3*5
    assert module_0.is_multiply_prime(64) == False    # 2^6
    assert module_0.is_multiply_prime(100) == False   # 2^2 * 5^2
    assert module_0.is_multiply_prime(210) == False   # 2*3*5*7 (four primes)

    # Cross-check against brute force over a range
    primes = [n for n in range(2, 101) if all(n % j for j in range(2, n))]
    products = {i * j * k for i in primes for j in primes for k in primes}
    for a in range(0, 201):
        assert module_0.is_multiply_prime(a) == (a in products), f"Mismatch at a={a}"

    print("test_is_multiply_prime passed")


test_is_multiply_prime()

# Generated at 2026-11-02 10:40:16.974004
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
# nonce:fd5d720c
    # True cases: product of exactly three primes (repetition allowed)
    assert module_0.is_multiply_prime(8) == True      # 2*2*2
    assert module_0.is_multiply_prime(12) == True     # 2*2*3
    assert module_0.is_multiply_prime(18) == True     # 2*3*3
    assert module_0.is_multiply_prime(27) == True     # 3*3*3
    assert module_0.is_multiply_prime(30) == True     # 2*3*5
    assert module_0.is_multiply_prime(42) == True     # 2*3*7
    assert module_0.is_multiply_prime(66) == True     # 2*3*11
    assert module_0.is_multiply_prime(70) == True     # 2*5*7
    assert module_0.is_multiply_prime(98) == True     # 2*7*7
    assert module_0.is_multiply_prime(99) == True     # 3*3*11
    assert module_0.is_multiply_prime(105) == True    # 3*5*7
    assert module_0.is_multiply_prime(125) == True    # 5*5*5

    # False cases: primes, semiprimes, products of 4+ primes, edge values
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False
    assert module_0.is_multiply_prime(3) == False
    assert module_0.is_multiply_prime(5) == False
    assert module_0.is_multiply_prime(7) == False
    assert module_0.is_multiply_prime(4) == False     # 2*2 (only two primes)
    assert module_0.is_multiply_prime(6) == False     # 2*3
    assert module_0.is_multiply_prime(9) == False     # 3*3
    assert module_0.is_multiply_prime(25) == False    # 5*5
    assert module_0.is_multiply_prime(49) == False    # 7*7
    assert module_0.is_multiply_prime(121) == False   # 11*11
    assert module_0.is_multiply_prime(64) == False    # 2*2*2*2 (four primes)
    assert module_0.is_multiply_prime(100) == False   # 2*2*5*5
    assert module_0.is_multiply_prime(210) == False   # 2*3*5*7
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(-30) == False

    # Cross-check: module_0.is_multiply_prime(a) should be True iff a has exactly
    # 3 prime factors (with multiplicity), verified independently.
    for a in range(1, 200):
        n = a
        num_factors = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                num_factors += 1
                n //= d
            d += 1
        if n > 1:
            num_factors += 1
        assert module_0.is_multiply_prime(a) == (num_factors == 3), f"Failed for a={a}"

    print("All tests passed!")


test_is_multiply_prime()

# Generated at 2026-11-02 10:42:53.917531
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
# nonce:159460a1
    # Numbers that ARE products of exactly three primes (repetition allowed)
    assert module_0.is_multiply_prime(8) == True      # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True     # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True     # 3 * 3 * 3
    assert module_0.is_multiply_prime(30) == True     # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True    # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True    # 5 * 5 * 5
    assert module_0.is_multiply_prime(582) == True    # 2 * 3 * 97

    # Numbers that are NOT products of exactly three primes
    assert module_0.is_multiply_prime(1) == False     # not a product of primes
    assert module_0.is_multiply_prime(2) == False     # single prime
    assert module_0.is_multiply_prime(3) == False     # single prime
    assert module_0.is_multiply_prime(4) == False     # 2 * 2 (two primes)
    assert module_0.is_multiply_prime(6) == False     # 2 * 3 (two primes)
    assert module_0.is_multiply_prime(10) == False    # 2 * 5 (two primes)
    assert module_0.is_multiply_prime(49) == False    # 7 * 7 (two primes)
    assert module_0.is_multiply_prime(60) == False    # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(210) == False   # 2 * 3 * 5 * 7 (four primes)
    assert module_0.is_multiply_prime(100) == False   # 2 * 2 * 5 * 5 (four primes)

    # Result should be a proper boolean
    assert isinstance(module_0.is_multiply_prime(30), bool)
    assert isinstance(module_0.is_multiply_prime(1), bool)

    print("All tests passed!")


if __name__ == "__main__":
    test_is_multiply_prime()
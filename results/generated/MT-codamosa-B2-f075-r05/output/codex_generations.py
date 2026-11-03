

# Generated at 2026-11-02 13:21:56.274540
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Product of three distinct primes
    assert module_0.is_multiply_prime(30) == True   # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True  # 3 * 5 * 7
    assert module_0.is_multiply_prime(70) == True   # 2 * 5 * 7
    assert module_0.is_multiply_prime(231) == True  # 3 * 7 * 11

    # Product of three primes with repetition
    assert module_0.is_multiply_prime(8) == True    # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True   # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True   # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True  # 5 * 5 * 5
    assert module_0.is_multiply_prime(28) == True   # 2 * 2 * 7

    # Not a product of exactly three primes
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(2) == False   # prime itself
    assert module_0.is_multiply_prime(4) == False   # 2 * 2 (only two primes)
    assert module_0.is_multiply_prime(6) == False   # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(64) == False  # 2^6 (six primes)
    assert module_0.is_multiply_prime(97) == False  # prime
    assert module_0.is_multiply_prime(100) == False # 2^2 * 5^2
    assert module_0.is_multiply_prime(-30) == False # negative input
    assert module_0.is_multiply_prime(5) == False   # prime

    # Larger valid case within search range
    assert module_0.is_multiply_prime(2 * 89 * 97) == True
    assert module_0.is_multiply_prime(97 * 97 * 97) == True

    print("All tests passed!")

test_is_multiply_prime()

# Generated at 2026-11-02 13:23:57.004336
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Products of exactly three primes -> True
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5
    assert module_0.is_multiply_prime(99) == True    # 3 * 3 * 11
    assert module_0.is_multiply_prime(28) == True    # 2 * 2 * 7

    # Primes, semiprimes, and other composites -> False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(2) == False    # prime
    assert module_0.is_multiply_prime(97) == False   # prime
    assert module_0.is_multiply_prime(6) == False    # 2 * 3 (only two primes)
    assert module_0.is_multiply_prime(4) == False    # 2 * 2
    assert module_0.is_multiply_prime(49) == False   # 7 * 7
    assert module_0.is_multiply_prime(15) == False   # 3 * 5
    assert module_0.is_multiply_prime(16) == False   # 2^4 (four primes)
    assert module_0.is_multiply_prime(60) == False   # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(100) == False  # 2^2 * 5^2
    assert module_0.is_multiply_prime(210) == False  # 2 * 3 * 5 * 7 (four primes)

    print("All tests passed!")


test_is_multiply_prime()

# Generated at 2026-11-02 13:27:30.156428
# Unit test for function is_multiply_prime
def test_is_multiply_prime():
    # Numbers that ARE the product of exactly three primes
    assert module_0.is_multiply_prime(30) == True    # 2 * 3 * 5
    assert module_0.is_multiply_prime(8) == True     # 2 * 2 * 2
    assert module_0.is_multiply_prime(12) == True    # 2 * 2 * 3
    assert module_0.is_multiply_prime(18) == True    # 2 * 3 * 3
    assert module_0.is_multiply_prime(20) == True    # 2 * 2 * 5
    assert module_0.is_multiply_prime(27) == True    # 3 * 3 * 3
    assert module_0.is_multiply_prime(28) == True    # 2 * 2 * 7
    assert module_0.is_multiply_prime(42) == True    # 2 * 3 * 7
    assert module_0.is_multiply_prime(45) == True    # 3 * 3 * 5
    assert module_0.is_multiply_prime(105) == True   # 3 * 5 * 7
    assert module_0.is_multiply_prime(125) == True   # 5 * 5 * 5

    # Numbers that are NOT the product of exactly three primes
    assert module_0.is_multiply_prime(0) == False
    assert module_0.is_multiply_prime(1) == False
    assert module_0.is_multiply_prime(2) == False    # prime itself
    assert module_0.is_multiply_prime(5) == False    # prime itself
    assert module_0.is_multiply_prime(6) == False    # product of only two primes
    assert module_0.is_multiply_prime(10) == False   # product of only two primes
    assert module_0.is_multiply_prime(16) == False   # 2 * 2 * 2 * 2 (four primes)
    assert module_0.is_multiply_prime(60) == False   # 2 * 2 * 3 * 5 (four primes)
    assert module_0.is_multiply_prime(64) == False   # 2^6 (six primes)
    assert module_0.is_multiply_prime(100) == False  # 2 * 2 * 5 * 5 (four primes)
    assert module_0.is_multiply_prime(-30) == False  # negative input

    # Exhaustive comparison against an independent brute-force reference
    def brute_force(a):
        for i in range(2, 101):
            if not all(i % j for j in range(2, i)): continue
            for j in range(2, 101):
                if not all(j % k for k in range(2, j)): continue
                for k in range(2, 101):
                    if not all(k % m for m in range(2, k)): continue
                    if i * j * k == a:
                        return True
        return False

    for a in range(-5, 130):
        assert module_0.is_multiply_prime(a) == brute_force(a), f"mismatch for a={a}"
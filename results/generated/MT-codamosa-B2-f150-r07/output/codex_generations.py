

# Generated at 2026-11-02 22:43:13.003307
# Unit test for function x_or_y
def test_x_or_y():
    # Primes return x
    assert module_0.x_or_y(7, 3, 5) == 3
    assert module_0.x_or_y(2, 10, 20) == 10      # smallest prime
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(13, 'prime', 'not') == 'prime'
    assert module_0.x_or_y(29, True, False) is True
    assert module_0.x_or_y(97, 1, 0) == 1

    # Non-primes return y
    assert module_0.x_or_y(1, 3, 5) == 5         # 1 is not prime
    assert module_0.x_or_y(4, 3, 5) == 5
    assert module_0.x_or_y(6, 3, 5) == 5
    assert module_0.x_or_y(9, 3, 5) == 5         # perfect square of a prime
    assert module_0.x_or_y(15, 'prime', 'not') == 'not'
    assert module_0.x_or_y(100, 1, 0) == 0

    # Larger values
    assert module_0.x_or_y(7919, 'yes', 'no') == 'yes'    # 1000th prime
    assert module_0.x_or_y(7917, 'yes', 'no') == 'no'

    print("All tests passed!")

# Generated at 2026-11-02 22:45:53.570609
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 10, 20) == 20
    
    # Small primes return x
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    
    # Small composites return y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(8, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(10, 10, 20) == 20
    
    # Larger primes return x
    assert module_0.x_or_y(13, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(29, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(97, 'prime', 'not prime') == 'prime'
    
    # Larger composites return y
    assert module_0.x_or_y(15, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(21, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(100, 'prime', 'not prime') == 'not prime'
    
    # Works with different value types
    assert module_0.x_or_y(11, [1, 2], [3, 4]) == [1, 2]
    assert module_0.x_or_y(12, [1, 2], [3, 4]) == [3, 4]
    assert module_0.x_or_y(17, None, 'composite') is None
    
    # Boundary behavior: 0 and negatives skip the loop and return x
    assert module_0.x_or_y(0, 10, 20) == 10
    assert module_0.x_or_y(-5, 10, 20) == 10
    
    print("All tests passed!")

if __name__ == "__main__":
    test_x_or_y()

# Generated at 2026-11-02 22:47:47.453729
# Unit test for function x_or_y
def test_x_or_y():
    # n = 1 is not prime -> returns y
    assert module_0.x_or_y(1, 10, 20) == 20
    # n = 2 is prime -> returns x
    assert module_0.x_or_y(2, 10, 20) == 10
    # n = 3 is prime -> returns x
    assert module_0.x_or_y(3, "prime", "not prime") == "prime"
    # n = 4 is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not prime") == "not prime"
    # n = 5 is prime -> returns x
    assert module_0.x_or_y(5, "prime", "not prime") == "prime"
    # n = 9 is composite -> returns y
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"
    # n = 12 is composite -> returns y
    assert module_0.x_or_y(12, "prime", "not prime") == "not prime"
    # n = 13 is prime -> returns x
    assert module_0.x_or_y(13, "prime", "not prime") == "prime"
    # n = 97 is prime -> returns x
    assert module_0.x_or_y(97, "prime", "not prime") == "prime"
    # n = 100 is composite -> returns y
    assert module_0.x_or_y(100, "prime", "not prime") == "not prime"
    print("All test cases passed!")

test_x_or_y()

# Generated at 2026-11-02 22:49:03.009096
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 'prime', 'not prime') == 'not prime'

    # Prime numbers return x
    assert module_0.x_or_y(2, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(3, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(5, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(7, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(13, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(97, 'prime', 'not prime') == 'prime'

    # Composite numbers return y
    assert module_0.x_or_y(4, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(6, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(9, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(15, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(100, 'prime', 'not prime') == 'not prime'

    # Works with arbitrary return values
    assert module_0.x_or_y(11, 100, 200) == 100
    assert module_0.x_or_y(12, 100, 200) == 200

    print("All tests passed!")

# Generated at 2026-11-02 22:50:50.085375
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, 5, 10) == 10    # n == 1 returns y
    assert module_0.x_or_y(2, 5, 10) == 5     # 2 is prime
    assert module_0.x_or_y(3, 5, 10) == 5     # 3 is prime
    assert module_0.x_or_y(4, 5, 10) == 10    # 4 is composite
    assert module_0.x_or_y(7, 5, 10) == 5     # 7 is prime
    assert module_0.x_or_y(9, 5, 10) == 10    # 9 is composite
    assert module_0.x_or_y(13, 3, 7) == 3     # 13 is prime
    assert module_0.x_or_y(15, 3, 7) == 7     # 15 is composite
    assert module_0.x_or_y(29, 100, 200) == 100   # 29 is prime
    assert module_0.x_or_y(30, 100, 200) == 200   # 30 is composite
    assert module_0.x_or_y(97, 'prime', 'not prime') == 'prime'      # 97 is prime
    assert module_0.x_or_y(100, 'prime', 'not prime') == 'not prime' # 100 is composite
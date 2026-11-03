

# Generated at 2026-11-02 13:48:45.144802
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> returns y
    assert module_0.x_or_y(1, 'prime', 'not prime') == 'not prime'

    # Small primes -> return x
    assert module_0.x_or_y(2, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(3, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(5, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(7, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(13, 'prime', 'not prime') == 'prime'
    assert module_0.x_or_y(97, 'prime', 'not prime') == 'prime'

    # Composite numbers -> return y
    assert module_0.x_or_y(4, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(6, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(9, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(15, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(25, 'prime', 'not prime') == 'not prime'
    assert module_0.x_or_y(100, 'prime', 'not prime') == 'not prime'

    # Works with arbitrary return values
    assert module_0.x_or_y(11, 10, 20) == 10
    assert module_0.x_or_y(12, 10, 20) == 20
    assert module_0.x_or_y(29, True, False) is True
    assert module_0.x_or_y(30, True, False) is False

    print("All tests passed!")


if __name__ == "__main__":
    test_x_or_y()

# Generated at 2026-11-02 13:50:21.163942
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime, returns y
    assert module_0.x_or_y(1, 10, 20) == 20

    # n == 2 is prime (loop doesn't execute), returns x
    assert module_0.x_or_y(2, 10, 20) == 10

    # n == 3 is prime, returns x
    assert module_0.x_or_y(3, 'prime', 'not') == 'prime'

    # n == 4 is composite, returns y
    assert module_0.x_or_y(4, 'prime', 'not') == 'not'

    # n == 5 is prime, returns x
    assert module_0.x_or_y(5, 100, 200) == 100

    # n == 6 is composite, returns y
    assert module_0.x_or_y(6, 100, 200) == 200

    # n == 7 is prime, returns x
    assert module_0.x_or_y(7, 'yes', 'no') == 'yes'

    # n == 9 is composite (3*3), returns y
    assert module_0.x_or_y(9, 'yes', 'no') == 'no'

    # larger prime, returns x
    assert module_0.x_or_y(13, 'prime', 'composite') == 'prime'

    # larger composite, returns y
    assert module_0.x_or_y(15, 'prime', 'composite') == 'composite'

    # n == 25 is composite (5*5), returns y
    assert module_0.x_or_y(25, 1, 0) == 0

    # n == 29 is prime, returns x
    assert module_0.x_or_y(29, 1, 0) == 1

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-02 13:53:03.800107
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime, should return y
    assert module_0.x_or_y(1, 5, 10) == 10

    # n == 2 is prime, should return x
    assert module_0.x_or_y(2, 5, 10) == 5

    # n == 3 is prime, should return x
    assert module_0.x_or_y(3, 5, 10) == 5

    # n == 4 is composite, should return y
    assert module_0.x_or_y(4, 5, 10) == 10

    # n == 5 is prime, should return x
    assert module_0.x_or_y(5, 5, 10) == 5

    # n == 7 is prime, should return x
    assert module_0.x_or_y(7, 7, 21) == 7

    # n == 9 is composite (3*3), should return y
    assert module_0.x_or_y(9, 7, 21) == 21

    # n == 12 is composite, should return y
    assert module_0.x_or_y(12, 7, 21) == 21

    # n == 13 is prime, should return x
    assert module_0.x_or_y(13, 100, 200) == 100

    # n == 15 is composite (3*5), should return y
    assert module_0.x_or_y(15, 100, 200) == 200

    # n == 17 is prime, should return x
    assert module_0.x_or_y(17, 100, 200) == 100

    # n == 25 is composite (5*5), should return y
    assert module_0.x_or_y(25, 100, 200) == 200

    # n == 29 is prime, should return x
    assert module_0.x_or_y(29, 100, 200) == 100

    # n == 30 is composite, should return y
    assert module_0.x_or_y(30, 100, 200) == 200

# Generated at 2026-11-02 13:55:12.484888
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y (1 is not prime)
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"

    # n == 2 returns x (2 is prime, loop body never executes)
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"

    # n == 3 returns x (prime)
    assert module_0.x_or_y(3, "prime", "not prime") == "prime"

    # n == 4 returns y (divisible by 2)
    assert module_0.x_or_y(4, "prime", "not prime") == "not prime"

    # n == 5 returns x (prime)
    assert module_0.x_or_y(5, "prime", "not prime") == "prime"

    # n == 9 returns y (divisible by 3)
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"

    # n == 13 returns x (prime)
    assert module_0.x_or_y(13, "prime", "not prime") == "prime"

    # n == 25 returns y (divisible by 5)
    assert module_0.x_or_y(25, "prime", "not prime") == "not prime"

    # n == 97 returns x (large prime)
    assert module_0.x_or_y(97, "prime", "not prime") == "prime"

    # n == 100 returns y (composite)
    assert module_0.x_or_y(100, "prime", "not prime") == "not prime"

    # Works with numeric values for x and y
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(8, 10, 20) == 20

    # Edge cases: n == 0 and negative n bypass the loop and return x
    assert module_0.x_or_y(0, "prime", "not prime") == "prime"
    assert module_0.x_or_y(-7, "prime", "not prime") == "prime"

    print("All tests passed!")


if __name__ == "__main__":
    test_x_or_y()

# Generated at 2026-11-02 13:57:51.488905
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 'x', 'y') == 'y'

    # n == 2 is prime, returns x (loop range is empty, for-else branch runs)
    assert module_0.x_or_y(2, 'x', 'y') == 'x'

    # Small primes return x
    assert module_0.x_or_y(3, 1, 0) == 1
    assert module_0.x_or_y(5, 1, 0) == 1
    assert module_0.x_or_y(7, 1, 0) == 1

    # Small composites return y
    assert module_0.x_or_y(4, 1, 0) == 0
    assert module_0.x_or_y(6, 1, 0) == 0
    assert module_0.x_or_y(9, 1, 0) == 0

    # Larger prime
    assert module_0.x_or_y(13, 'prime', 'composite') == 'prime'
    assert module_0.x_or_y(97, 'prime', 'composite') == 'prime'

    # Larger composite
    assert module_0.x_or_y(15, 'prime', 'composite') == 'composite'
    assert module_0.x_or_y(100, 'prime', 'composite') == 'composite'

    # Edge cases: n = 0 and negative n (loop body never runs, returns x)
    assert module_0.x_or_y(0, 'x', 'y') == 'x'
    assert module_0.x_or_y(-7, 'x', 'y') == 'x'

    print("All tests passed!")


if __name__ == "__main__":
    test_x_or_y()
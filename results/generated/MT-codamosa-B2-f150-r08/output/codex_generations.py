

# Generated at 2026-11-02 08:26:47.350244
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 10, 20) == 20
    # Small primes return x
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    # Composite numbers return y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(12, 10, 20) == 20
    assert module_0.x_or_y(15, 10, 20) == 20
    # Larger prime and composite
    assert module_0.x_or_y(97, 'prime', 'composite') == 'prime'
    assert module_0.x_or_y(100, 'prime', 'composite') == 'composite'
    # Edge cases: 0 and negative numbers (loop doesn't execute, returns x)
    assert module_0.x_or_y(0, 10, 20) == 10
    assert module_0.x_or_y(-7, 10, 20) == 10
    # Works with mixed types
    assert module_0.x_or_y(11, "yes", "no") == "yes"
    assert module_0.x_or_y(8, "yes", "no") == "no"

test_x_or_y()
print("All tests passed!")

# Generated at 2026-11-02 08:27:45.640660
# Unit test for function x_or_y
def test_x_or_y():
    # Prime numbers should return x
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"
    assert module_0.x_or_y(3, "prime", "not prime") == "prime"
    assert module_0.x_or_y(5, "prime", "not prime") == "prime"
    assert module_0.x_or_y(7, "prime", "not prime") == "prime"
    assert module_0.x_or_y(13, "prime", "not prime") == "prime"
    assert module_0.x_or_y(97, "prime", "not prime") == "prime"

    # Non-prime numbers should return y
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(4, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(6, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(15, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(100, "prime", "not prime") == "not prime"

    # Works with other value types
    assert module_0.x_or_y(11, 10, 20) == 10
    assert module_0.x_or_y(12, 10, 20) == 20
    assert module_0.x_or_y(1, True, False) is False

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-02 08:29:38.979482
# Unit test for function x_or_y
def test_x_or_y():
    # Prime numbers should return x
    assert module_0.x_or_y(7, 5, 3) == 5
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    assert module_0.x_or_y(29, 'prime', 'composite') == 'prime'

    # Non-prime numbers should return y
    assert module_0.x_or_y(1, 5, 3) == 3
    assert module_0.x_or_y(4, 5, 3) == 3
    assert module_0.x_or_y(6, 5, 3) == 3
    assert module_0.x_or_y(9, 5, 3) == 3
    assert module_0.x_or_y(15, 'prime', 'composite') == 'composite'
    assert module_0.x_or_y(100, 1, 0) == 0

    print("All tests passed!")

test_x_or_y()

# Generated at 2026-11-02 08:31:57.642810
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y (1 is not prime)
    assert module_0.x_or_y(1, 10, 20) == 20

    # n == 2 (prime) returns x
    assert module_0.x_or_y(2, 10, 20) == 10

    # n == 3 (prime) returns x
    assert module_0.x_or_y(3, 5, 9) == 5

    # n == 4 (composite) returns y
    assert module_0.x_or_y(4, 5, 9) == 9

    # n == 7 (prime) returns x
    assert module_0.x_or_y(7, 100, 200) == 100

    # n == 9 (composite, divisible by 3) returns y
    assert module_0.x_or_y(9, 100, 200) == 200

    # n == 13 (prime) returns x
    assert module_0.x_or_y(13, "prime", "not prime") == "prime"

    # n == 15 (composite) returns y
    assert module_0.x_or_y(15, "prime", "not prime") == "not prime"

    # n == 29 (larger prime) returns x
    assert module_0.x_or_y(29, 1, 0) == 1

    # n == 30 (larger composite) returns y
    assert module_0.x_or_y(30, 1, 0) == 0

    # n == 97 (prime) returns x
    assert module_0.x_or_y(97, True, False) is True

    # n == 100 (composite) returns y
    assert module_0.x_or_y(100, True, False) is False

# Generated at 2026-11-02 08:33:01.934009
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 2, 3) == 3
    # n == 2 is prime (loop doesn't execute)
    assert module_0.x_or_y(2, 5, 6) == 5
    # n == 3 is prime
    assert module_0.x_or_y(3, 7, 8) == 7
    # n == 4 is composite
    assert module_0.x_or_y(4, 9, 10) == 10
    # n == 7 is prime
    assert module_0.x_or_y(7, 11, 12) == 11
    # n == 9 is composite
    assert module_0.x_or_y(9, 13, 14) == 14
    # n == 13 is prime
    assert module_0.x_or_y(13, 100, 200) == 100
    # n == 15 is composite
    assert module_0.x_or_y(15, 100, 200) == 200
    print("All tests passed!")

if __name__ == "__main__":
    test_x_or_y()
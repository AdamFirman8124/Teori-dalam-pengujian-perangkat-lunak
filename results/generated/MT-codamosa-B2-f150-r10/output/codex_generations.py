

# Generated at 2026-11-01 20:41:23.605652
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 'prime', 'not_prime') == 'not_prime'

    # Prime numbers return x
    assert module_0.x_or_y(2, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(3, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(5, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(7, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(13, 'prime', 'not_prime') == 'prime'

    # Composite numbers return y
    assert module_0.x_or_y(4, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(6, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(9, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(15, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(25, 'prime', 'not_prime') == 'not_prime'

    # Works with other value types (numbers)
    assert module_0.x_or_y(11, 100, 200) == 100
    assert module_0.x_or_y(12, 100, 200) == 200

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-01 20:41:26.908702
# Unit test for function x_or_y
def test_x_or_y():
    # Prime numbers should return x
    assert module_0.x_or_y(7, 34, 12) == 34
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 5, 6) == 5
    assert module_0.x_or_y(13, 100, 200) == 100

    # Composite numbers should return y
    assert module_0.x_or_y(15, 8, 5) == 5
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(9, 1, 2) == 2
    assert module_0.x_or_y(100, 7, 9) == 9

    # n == 1 should return y
    assert module_0.x_or_y(1, 3, 4) == 4
    assert module_0.x_or_y(1, 10, 99) == 99

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-01 20:41:31.888375
# Unit test for function x_or_y
def test_x_or_y():
    # n = 1 is neither prime nor composite -> returns y
    assert module_0.x_or_y(1, 'prime', 'not_prime') == 'not_prime'

    # n = 2 is prime -> returns x
    assert module_0.x_or_y(2, 'prime', 'not_prime') == 'prime'

    # n = 3 is prime -> returns x
    assert module_0.x_or_y(3, 'prime', 'not_prime') == 'prime'

    # n = 4 is composite -> returns y
    assert module_0.x_or_y(4, 'prime', 'not_prime') == 'not_prime'

    # n = 5 is prime -> returns x
    assert module_0.x_or_y(5, 'prime', 'not_prime') == 'prime'

    # n = 7 is prime -> returns x
    assert module_0.x_or_y(7, 'prime', 'not_prime') == 'prime'

    # n = 9 is composite (3*3) -> returns y
    assert module_0.x_or_y(9, 'prime', 'not_prime') == 'not_prime'

    # n = 12 is composite -> returns y
    assert module_0.x_or_y(12, 'prime', 'not_prime') == 'not_prime'

    # n = 13 is prime -> returns x
    assert module_0.x_or_y(13, 'prime', 'not_prime') == 'prime'

    # n = 29 is prime -> returns x
    assert module_0.x_or_y(29, 'prime', 'not_prime') == 'prime'

    # Larger composite -> returns y
    assert module_0.x_or_y(100, True, False) is False

    # Larger prime -> returns x
    assert module_0.x_or_y(97, True, False) is True

    # Works with arbitrary values
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(17, 10, 20) == 10

    print("All tests passed!")

if __name__ == "__main__":
    test_x_or_y()

# Generated at 2026-11-01 20:41:39.986133
# Unit test for function x_or_y
def test_x_or_y():
    # n = 1 is not prime -> returns y
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"

    # n = 2 is prime (range(2, 2) is empty, else branch) -> returns x
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"

    # n = 3 is prime
    assert module_0.x_or_y(3, "prime", "not prime") == "prime"

    # n = 4 is composite (divisible by 2)
    assert module_0.x_or_y(4, "prime", "not prime") == "not prime"

    # n = 5 is prime
    assert module_0.x_or_y(5, "prime", "not prime") == "prime"

    # n = 6 is composite
    assert module_0.x_or_y(6, "prime", "not prime") == "not prime"

    # n = 7 is prime
    assert module_0.x_or_y(7, "prime", "not prime") == "prime"

    # n = 9 is composite (divisible by 3)
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"

    # n = 10 is composite
    assert module_0.x_or_y(10, "prime", "not prime") == "not prime"

    # n = 11 is prime
    assert module_0.x_or_y(11, "prime", "not prime") == "prime"

    # n = 13 is prime
    assert module_0.x_or_y(13, "prime", "not prime") == "prime"

    # n = 25 is composite (divisible by 5)
    assert module_0.x_or_y(25, "prime", "not prime") == "not prime"

    # n = 29 is prime
    assert module_0.x_or_y(29, "prime", "not prime") == "prime"

    # n = 97 is prime (larger prime)
    assert module_0.x_or_y(97, "yes", "no") == "yes"

    # n = 100 is composite
    assert module_0.x_or_y(100, "yes", "no") == "no"

    # Works with numeric x and y values
    assert module_0.x_or_y(7, 100, 200) == 100
    assert module_0.x_or_y(8, 100, 200) == 200

    # Works with other types (lists)
    assert module_0.x_or_y(5, [1, 2], [3, 4]) == [1, 2]
    assert module_0.x_or_y(6, [1, 2], [3, 4]) == [3, 4]

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-01 20:41:46.529902
# Unit test for function x_or_y
def test_x_or_y():
    # Prime numbers return x
    assert module_0.x_or_y(2, 'x', 'y') == 'x'
    assert module_0.x_or_y(3, 'x', 'y') == 'x'
    assert module_0.x_or_y(5, 'x', 'y') == 'x'
    assert module_0.x_or_y(7, 'x', 'y') == 'x'
    assert module_0.x_or_y(13, 'x', 'y') == 'x'
    assert module_0.x_or_y(97, 'x', 'y') == 'x'

    # n == 1 returns y (1 is not prime)
    assert module_0.x_or_y(1, 'x', 'y') == 'y'

    # Composite numbers return y
    assert module_0.x_or_y(4, 'x', 'y') == 'y'
    assert module_0.x_or_y(6, 'x', 'y') == 'y'
    assert module_0.x_or_y(9, 'x', 'y') == 'y'
    assert module_0.x_or_y(15, 'x', 'y') == 'y'
    assert module_0.x_or_y(100, 'x', 'y') == 'y'

    # Works with arbitrary value types
    assert module_0.x_or_y(11, 100, 200) == 100
    assert module_0.x_or_y(12, 100, 200) == 200

    print("All tests passed!")


test_x_or_y()
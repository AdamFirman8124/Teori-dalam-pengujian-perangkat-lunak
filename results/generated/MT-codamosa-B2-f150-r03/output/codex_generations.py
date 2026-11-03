

# Generated at 2026-11-02 19:55:55.026675
# Unit test for function x_or_y
def test_x_or_y():
    # n = 1 is not prime -> returns y
    assert module_0.x_or_y(1, 10, 20) == 20

    # Prime numbers -> returns x
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    assert module_0.x_or_y(97, 10, 20) == 10

    # Composite numbers -> returns y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(100, 10, 20) == 20

    # Works with non-numeric return values
    assert module_0.x_or_y(11, "prime", "not prime") == "prime"
    assert module_0.x_or_y(12, "prime", "not prime") == "not prime"

    print("All tests passed!")


test_x_or_y()
# nonce:cde1582f

# Generated at 2026-11-02 19:57:31.679209
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> returns y
    assert module_0.x_or_y(1, 3, 5) == 5

    # n == 2 is prime -> returns x (loop range is empty, else branch)
    assert module_0.x_or_y(2, 3, 5) == 3

    # n == 3 is prime -> returns x
    assert module_0.x_or_y(3, 7, 9) == 7

    # n == 4 is composite -> returns y
    assert module_0.x_or_y(4, 7, 9) == 9

    # n == 5 is prime -> returns x
    assert module_0.x_or_y(5, 100, 200) == 100

    # n == 6 is composite -> returns y
    assert module_0.x_or_y(6, 100, 200) == 200

    # n == 7 is prime -> returns x
    assert module_0.x_or_y(7, "prime", "composite") == "prime"

    # n == 8 is composite -> returns y
    assert module_0.x_or_y(8, "prime", "composite") == "composite"

    # n == 9 is composite (3*3) -> returns y
    assert module_0.x_or_y(9, "prime", "composite") == "composite"

    # n == 11 is prime -> returns x
    assert module_0.x_or_y(11, True, False) is True

    # n == 12 is composite -> returns y
    assert module_0.x_or_y(12, True, False) is False

    # larger prime -> returns x
    assert module_0.x_or_y(13, 1, 0) == 1

    # larger composite -> returns y
    assert module_0.x_or_y(15, 1, 0) == 0

    # works with mixed types
    assert module_0.x_or_y(17, [1], [2]) == [1]
    assert module_0.x_or_y(18, [1], [2]) == [2]

    print("All tests passed!")

# Generated at 2026-11-02 19:58:48.530975
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> returns y
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"

    # n == 2 is prime -> returns x
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"

    # n == 3 is prime -> returns x
    assert module_0.x_or_y(3, "prime", "not prime") == "prime"

    # n == 4 is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not prime") == "not prime"

    # n == 5 is prime -> returns x
    assert module_0.x_or_y(5, "prime", "not prime") == "prime"

    # n == 7 is prime -> returns x
    assert module_0.x_or_y(7, 100, 200) == 100

    # n == 9 is composite -> returns y
    assert module_0.x_or_y(9, 100, 200) == 200

    # n == 10 is composite -> returns y
    assert module_0.x_or_y(10, 100, 200) == 200

    # n == 13 is prime -> returns x
    assert module_0.x_or_y(13, 100, 200) == 100

    # Large prime -> returns x
    assert module_0.x_or_y(997, "yes", "no") == "yes"

    # Large composite -> returns y
    assert module_0.x_or_y(1000, "yes", "no") == "no"

    print("All tests passed!")


test_x_or_y()

# Generated at 2026-11-02 20:00:52.232162
# Unit test for function x_or_y
def test_x_or_y():import unittest


class TestXOrY(unittest.TestCase):
    def test_n_is_one_returns_y(self):
        self.assertEqual(module_0.x_or_y(1, "prime", "not_prime"), "not_prime")

    def test_n_is_two_is_prime(self):
        self.assertEqual(module_0.x_or_y(2, "prime", "not_prime"), "prime")

    def test_n_is_three_is_prime(self):
        self.assertEqual(module_0.x_or_y(3, "prime", "not_prime"), "prime")

    def test_n_is_four_is_not_prime(self):
        self.assertEqual(module_0.x_or_y(4, "prime", "not_prime"), "not_prime")

    def test_n_is_five_is_prime(self):
        self.assertEqual(module_0.x_or_y(5, "prime", "not_prime"), "prime")

    def test_n_is_nine_is_not_prime(self):
        self.assertEqual(module_0.x_or_y(9, "prime", "not_prime"), "not_prime")

    def test_large_prime(self):
        self.assertEqual(module_0.x_or_y(97, "prime", "not_prime"), "prime")

    def test_large_composite(self):
        self.assertEqual(module_0.x_or_y(100, "prime", "not_prime"), "not_prime")

    def test_numeric_outputs(self):
        self.assertEqual(module_0.x_or_y(7, 10, 20), 10)
        self.assertEqual(module_0.x_or_y(8, 10, 20), 20)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 20:03:44.797131
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime, should return y
    assert module_0.x_or_y(1, 10, 20) == 20

    # Prime numbers should return x
    assert module_0.x_or_y(2, 10, 20) == 10   # smallest prime
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    assert module_0.x_or_y(97, 10, 20) == 10
    assert module_0.x_or_y(7919, 'prime', 'composite') == 'prime'  # large prime

    # Composite numbers should return y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(100, 10, 20) == 20
    assert module_0.x_or_y(7917, 'prime', 'composite') == 'composite'  # 3 * 7 * 13 * 29

    # Works with arbitrary return values
    assert module_0.x_or_y(11, 'yes', 'no') == 'yes'
    assert module_0.x_or_y(12, 'yes', 'no') == 'no'

    # Edge-case behavior of the implementation:
    # n = 0 and negatives skip the loop and fall through to the else branch
    assert module_0.x_or_y(0, 10, 20) == 10
    assert module_0.x_or_y(-7, 10, 20) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test_x_or_y()
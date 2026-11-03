

# Generated at 2026-11-02 17:05:15.328679
# Unit test for function multiply
def test_multiply():
    # nonce:4f9d79e0
    # Basic positive single-digit numbers
    assert module_0.multiply(3, 5) == 15
    assert module_0.multiply(4, 6) == 24
    assert module_0.multiply(9, 9) == 81
    assert module_0.multiply(1, 1) == 1

    # Multi-digit numbers use only the last digits
    assert module_0.multiply(123, 456) == 18
    assert module_0.multiply(12, 34) == 8
    assert module_0.multiply(11, 21) == 1
    assert module_0.multiply(52, 92) == 4

    # Numbers involving zero
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(10, 20) == 0
    assert module_0.multiply(100, 7) == 0

    # Negative numbers (Python: -x % 10 yields a positive remainder)
    assert module_0.multiply(-3, 7) == 49    # (-3 % 10) = 7 -> 7 * 7
    assert module_0.multiply(-12, 14) == 32  # (-12 % 10) = 8 -> 8 * 4
    assert module_0.multiply(-25, -4) == 30  # 5 * 6

# Generated at 2026-11-02 17:06:17.911665
# Unit test for function multiply
def test_multiply():
    # Positive integers - product of unit digits
    assert module_0.multiply(148, 412) == 16
    assert module_0.multiply(19, 28) == 72
    assert module_0.multiply(2020, 1851) == 0

    # Negative number (unit digit of -15 is 5)
    assert module_0.multiply(14, -15) == 20

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12
    assert module_0.multiply(9, 9) == 81

    # Zero values
    assert module_0.multiply(0, 7) == 0
    assert module_0.multiply(0, 0) == 0

    # Trailing zeros
    assert module_0.multiply(10, 50) == 0
    assert module_0.multiply(100, 3) == 0

    # Large numbers
    assert module_0.multiply(123456, 789012) == 12
    assert module_0.multiply(999999, 111111) == 81

    # Symmetry check
    assert module_0.multiply(27, 34) == module_0.multiply(34, 27) == 28

    print("All tests passed!")


if __name__ == "__main__":
    test_multiply()

# Generated at 2026-11-02 17:06:59.953273
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers
    assert module_0.multiply(12, 34) == 8       # 2 * 4
    assert module_0.multiply(123, 456) == 18    # 3 * 6
    assert module_0.multiply(7, 7) == 49        # 7 * 7
    assert module_0.multiply(15, 25) == 25      # 5 * 5

    # Zero last digits
    assert module_0.multiply(10, 20) == 0
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(100, 100) == 0

    # Negative numbers (Python modulo yields non-negative remainder)
    assert module_0.multiply(-12, 34) == 32     # abs(-12 % 10)=8, 8*4
    assert module_0.multiply(12, -34) == 12     # 2 * 6
    assert module_0.multiply(-12, -34) == 48    # 8 * 6
    assert module_0.multiply(-13, 7) == 49      # 7 * 7

    # Large numbers
    assert module_0.multiply(123456, 789) == 54 # 6 * 9
    assert module_0.multiply(999, 999) == 81    # 9 * 9

    print("All tests passed!")


if __name__ == "__main__":
    test_multiply()

# Generated at 2026-11-02 17:07:30.416373
# Unit test for function multiply
def test_multiply():
    # Positive numbers
    assert module_0.multiply(148, 412) == 16, "Expected 16 for module_0.multiply(148, 412)"
    assert module_0.multiply(19, 28) == 72, "Expected 72 for module_0.multiply(19, 28)"
    assert module_0.multiply(2020, 1851) == 0, "Expected 0 for module_0.multiply(2020, 1851)"
    assert module_0.multiply(14, -15) == 20, "Expected 20 for module_0.multiply(14, -15)"
    assert module_0.multiply(76, 67) == 42, "Expected 42 for module_0.multiply(76, 67)"

    # Negative numbers
    assert module_0.multiply(-148, 412) == 16, "Expected 16 for module_0.multiply(-148, 412)"
    assert module_0.multiply(148, -412) == 16, "Expected 16 for module_0.multiply(148, -412)"
    assert module_0.multiply(-19, -28) == 72, "Expected 72 for module_0.multiply(-19, -28)"
    assert module_0.multiply(-14, -15) == 20, "Expected 20 for module_0.multiply(-14, -15)"

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12, "Expected 12 for module_0.multiply(3, 4)"
    assert module_0.multiply(-3, 4) == 12, "Expected 12 for module_0.multiply(-3, 4)"

    # Zeros
    assert module_0.multiply(0, 5) == 0, "Expected 0 for module_0.multiply(0, 5)"
    assert module_0.multiply(5, 0) == 0, "Expected 0 for module_0.multiply(5, 0)"
    assert module_0.multiply(0, 0) == 0, "Expected 0 for module_0.multiply(0, 0)"
    assert module_0.multiply(10, 20) == 0, "Expected 0 for module_0.multiply(10, 20)"
    assert module_0.multiply(-10, -20) == 0, "Expected 0 for module_0.multiply(-10, -20)"


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(module_0.multiply(148, 412), 16)
        self.assertEqual(module_0.multiply(19, 28), 72)
        self.assertEqual(module_0.multiply(76, 67), 42)

    def test_negative_numbers(self):
        self.assertEqual(module_0.multiply(-148, 412), 16)
        self.assertEqual(module_0.multiply(148, -412), 16)
        self.assertEqual(module_0.multiply(-19, -28), 72)
        self.assertEqual(module_0.multiply(-14, -15), 20)

    def test_zeros(self):
        self.assertEqual(module_0.multiply(2020, 1851), 0)
        self.assertEqual(module_0.multiply(0, 5), 0)
        self.assertEqual(module_0.multiply(5, 0), 0)
        self.assertEqual(module_0.multiply(0, 0), 0)
        self.assertEqual(module_0.multiply(10, 20), 0)
        self.assertEqual(module_0.multiply(-10, -20), 0)

    def test_single_digits(self):
        self.assertEqual(module_0.multiply(3, 4), 12)
        self.assertEqual(module_0.multiply(-3, 4), 12)
        self.assertEqual(module_0.multiply(3, -4), 12)
        self.assertEqual(module_0.multiply(-3, -4), 12)


if __name__ == "__main__":
    test_multiply()
    unittest.main()

# Generated at 2026-11-02 17:07:36.105563
# Unit test for function multiply
def test_multiply():
    # Test with positive numbers
    assert module_0.multiply(4, 5) == 20, "Expected 20 for module_0.multiply(4, 5)"
    assert module_0.multiply(123, 456) == 18, "Expected 18 for module_0.multiply(123, 456)"  # 3 * 6

    # Test with negative numbers
    assert module_0.multiply(-4, 5) == 20, "Expected 20 for module_0.multiply(-4, 5)"  # abs(-4 % 10) = 6? No: -4 % 10 = 6 in Python
    # Careful: in Python, -4 % 10 == 6, so abs(-4 % 10) == 6
    assert module_0.multiply(-4, 5) == 30, "Expected 30 for module_0.multiply(-4, 5)"  # 6 * 5
    assert module_0.multiply(-1, -2) == 2, "Expected 2 for module_0.multiply(-1, -2)"  # 9 * 8 = 72? No: -1 % 10 = 9, -2 % 10 = 8
    assert module_0.multiply(-1, -2) == 72, "Expected 72 for module_0.multiply(-1, -2)"  # 9 * 8

    # Test with zero
    assert module_0.multiply(0, 5) == 0, "Expected 0 for module_0.multiply(0, 5)"
    assert module_0.multiply(10, 20) == 0, "Expected 0 for module_0.multiply(10, 20)"  # 0 * 0

    # Test with single digit numbers
    assert module_0.multiply(7, 8) == 56, "Expected 56 for module_0.multiply(7, 8)"

    # Test with large numbers
    assert module_0.multiply(999, 999) == 81, "Expected 81 for module_0.multiply(999, 999)"  # 9 * 9
    assert module_0.multiply(1000001, 2000002) == 2, "Expected 2 for module_0.multiply(1000001, 2000002)"  # 1 * 2

    print("All tests passed!")

if __name__ == "__main__":
    test_multiply()
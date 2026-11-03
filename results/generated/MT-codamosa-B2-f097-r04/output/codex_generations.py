

# Generated at 2026-11-02 08:22:03.188673
# Unit test for function multiply
def test_multiply():import unittest


class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(module_0.multiply(123, 456), 3 * 6)

    def test_single_digit_numbers(self):
        self.assertEqual(module_0.multiply(4, 7), 28)

    def test_negative_numbers(self):
        self.assertEqual(module_0.multiply(-123, -456), 18)

    def test_mixed_sign_numbers(self):
        self.assertEqual(module_0.multiply(-123, 456), 18)
        self.assertEqual(module_0.multiply(123, -456), 18)

    def test_zero(self):
        self.assertEqual(module_0.multiply(0, 5), 0)
        self.assertEqual(module_0.multiply(10, 0), 0)

    def test_number_ending_in_zero(self):
        self.assertEqual(module_0.multiply(120, 35), 0)

    def test_negative_last_digit(self):
        self.assertEqual(module_0.multiply(-17, -29), 63)

    def test_result_of_last_digits(self):
        self.assertEqual(module_0.multiply(9, 9), 81)

    def test_large_numbers(self):
        self.assertEqual(module_0.multiply(123456789, 987654321), 9 * 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 08:22:22.232650
# Unit test for function multiply
def test_multiply():
    # Basic positive integers: product of last digits
    assert module_0.multiply(12, 13) == 6      # 2 * 3
    assert module_0.multiply(148, 412) == 16   # 8 * 2
    assert module_0.multiply(19, 21) == 9      # 9 * 1
    assert module_0.multiply(3, 4) == 12       # 3 * 4
    assert module_0.multiply(9, 9) == 81       # 9 * 9

    # Cases involving zero
    assert module_0.multiply(0, 5) == 0        # 0 * 5
    assert module_0.multiply(100, 25) == 0     # 0 * 5
    assert module_0.multiply(0, 0) == 0

    # Negative numbers: Python's % yields non-negative results,
    # e.g. -12 % 10 == 8 and -13 % 10 == 7
    assert module_0.multiply(-12, 13) == 24    # abs(-12 % 10)=8, 3
    assert module_0.multiply(12, -13) == 21    # 2, abs(-13 % 10)=7
    assert module_0.multiply(-12, -13) == 56   # 8 * 7

# Generated at 2026-11-02 08:22:34.729008
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers
    assert module_0.multiply(123, 456) == 3 * 6  # last digits 3 and 6
    assert module_0.multiply(12, 22) == 2 * 2    # last digits 2 and 2
    assert module_0.multiply(10, 20) == 0        # last digits 0 and 0

    # Negative numbers use absolute value of last digit
    assert module_0.multiply(-123, -456) == 3 * 6
    assert module_0.multiply(-123, 456) == 3 * 6
    assert module_0.multiply(123, -456) == 3 * 6

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12
    assert module_0.multiply(0, 5) == 0

    # Large numbers, only last digit matters
    assert module_0.multiply(987654321, 123456789) == 1 * 9

    # Same number
    assert module_0.multiply(7, 7) == 49

    print("All tests passed!")

# Generated at 2026-11-02 08:23:07.494732
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers: product of unit digits
    assert module_0.multiply(148, 412) == 16          # 8 * 2
    assert module_0.multiply(19, 28) == 72            # 9 * 8
    assert module_0.multiply(7, 3) == 21              # 7 * 3
    assert module_0.multiply(1, 1) == 1               # 1 * 1
    assert module_0.multiply(9, 9) == 81              # 9 * 9

    # Numbers with unit digit 0
    assert module_0.multiply(2020, 1851) == 0         # 0 * 1
    assert module_0.multiply(10, 20) == 0             # 0 * 0
    assert module_0.multiply(100, 200) == 0           # 0 * 0

    # Zeros as inputs
    assert module_0.multiply(0, 0) == 0
    assert module_0.multiply(0, 123) == 0
    assert module_0.multiply(456, 0) == 0

    # Negative numbers (Python: -n % 10 yields positive remainder)
    assert module_0.multiply(14, -15) == 20           # 4 * 5
    assert module_0.multiply(-3, 7) == 49             # -3 % 10 == 7 -> 7 * 7
    assert module_0.multiply(-8, -8) == 4             # -8 % 10 == 2 -> 2 * 2

    # Large numbers
    assert module_0.multiply(123456789, 987654321) == 9        # 9 * 1
    assert module_0.multiply(10**18 + 5, 10**18 + 6) == 30     # 5 * 6

    print("All tests passed!")

# Generated at 2026-11-02 08:23:17.733284
# Unit test for function multiply
def test_multiply():
    # nonce:83037958
    # Basic positive numbers
    assert module_0.multiply(4, 5) == 20
    assert module_0.multiply(12, 34) == 8          # last digits 2 * 4
    assert module_0.multiply(123, 456) == 18       # last digits 3 * 6

    # Zero cases
    assert module_0.multiply(0, 9) == 0
    assert module_0.multiply(10, 20) == 0          # last digits are 0
    assert module_0.multiply(0, 0) == 0

    # Negative numbers (Python: -x % 10 gives 10 - digit)
    assert module_0.multiply(-3, 7) == 49          # (-3 % 10) == 7
    assert module_0.multiply(-14, 5) == 30         # (-14 % 10) == 6
    assert module_0.multiply(5, -5) == 25          # (-5 % 10) == 5
    assert module_0.multiply(-1, -1) == 81         # (-1 % 10) == 9

    # Single digit results
    assert module_0.multiply(1, 1) == 1
    assert module_0.multiply(9, 9) == 81
    assert module_0.multiply(11, 11) == 1

    # Floats supported by % operator
    assert module_0.multiply(2.5, 4.0) == 10.0

    print("All tests passed!")


# Generated at 2026-11-03 02:21:45.032869
# Unit test for function multiply
def test_multiply():import unittest


class TestMultiply(unittest.TestCase):
    def test_positive_single_digits(self):
        self.assertEqual(module_0.multiply(3, 4), 12)

    def test_positive_multi_digit(self):
        self.assertEqual(module_0.multiply(123, 456), 18)  # 3 * 6

    def test_negative_numbers(self):
        self.assertEqual(module_0.multiply(-3, 4), 12)  # abs handles negatives
        self.assertEqual(module_0.multiply(3, -4), 12)
        self.assertEqual(module_0.multiply(-3, -4), 12)

    def test_negative_multi_digit(self):
        self.assertEqual(module_0.multiply(-123, -456), 18)  # abs(3) * abs(6)

    def test_with_zero(self):
        self.assertEqual(module_0.multiply(0, 5), 0)
        self.assertEqual(module_0.multiply(5, 0), 0)
        self.assertEqual(module_0.multiply(0, 0), 0)

    def test_last_digit_zero(self):
        self.assertEqual(module_0.multiply(10, 7), 0)  # 0 * 7
        self.assertEqual(module_0.multiply(250, 3), 0)  # 0 * 3

    def test_result_wraps_beyond_nine(self):
        self.assertEqual(module_0.multiply(9, 9), 81)
        self.assertEqual(module_0.multiply(19, 29), 81)  # 9 * 9

    def test_same_number(self):
        self.assertEqual(module_0.multiply(7, 7), 49)

    def test_large_numbers(self):
        self.assertEqual(module_0.multiply(123456789, 987654321), 9)  # 9 * 1


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 02:24:54.590952
# Unit test for function multiply
def test_multiply():
    # Basic positive integers
    assert module_0.multiply(148, 412) == 16      # 8 * 2
    assert module_0.multiply(19, 28) == 72        # 9 * 8
    assert module_0.multiply(76, 67) == 42        # 6 * 7
    assert module_0.multiply(237, 967) == 49      # 7 * 7
    assert module_0.multiply(3, 4) == 12          # single digits

    # Zero cases
    assert module_0.multiply(2020, 1851) == 0     # 0 * 1
    assert module_0.multiply(0, 222) == 0         # 0 * 2
    assert module_0.multiply(0, 0) == 0

    # Negative numbers (abs of unit digit)
    assert module_0.multiply(14, -15) == 20       # 4 * 5
    assert module_0.multiply(-23, 45) == 35       # abs(-23 % 10)=7, 7 * 5
    assert module_0.multiply(-7, -8) == 6         # abs(-7 % 10)=3, abs(-8 % 10)=2

# Generated at 2026-11-03 02:26:34.607905
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers
    assert module_0.multiply(148, 412) == 16, "Expected 8*2=16"
    assert module_0.multiply(19, 28) == 72, "Expected 9*8=72"
    assert module_0.multiply(2020, 1851) == 0, "Expected 0*1=0"

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12, "Expected 3*4=12"
    assert module_0.multiply(9, 9) == 81, "Expected 9*9=81"

    # Negative numbers - last digit should be absolute value
    assert module_0.multiply(-148, 412) == 16, "Expected abs(-8)*2=16"
    assert module_0.multiply(148, -412) == 16, "Expected 8*abs(-2)=16"
    assert module_0.multiply(-19, -28) == 72, "Expected abs(-9)*abs(-8)=72"

    # Zero cases
    assert module_0.multiply(0, 5) == 0, "Expected 0*5=0"
    assert module_0.multiply(10, 20) == 0, "Expected 0*0=0"

    # Numbers ending in 1
    assert module_0.multiply(11, 21) == 1, "Expected 1*1=1"

    print("All test cases passed!")


if __name__ == "__main__":
    test_multiply()

# Generated at 2026-11-03 02:28:33.920378
# Unit test for function multiply
def test_multiply():import unittest


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(module_0.multiply(12, 3), 6)      # 2 * 3
        self.assertEqual(module_0.multiply(148, 412), 16)  # 8 * 2
        self.assertEqual(module_0.multiply(5, 7), 35)      # 5 * 7

    def test_negative_numbers(self):
        self.assertEqual(module_0.multiply(-12, 3), 6)     # 2 * 3
        self.assertEqual(module_0.multiply(12, -3), 6)     # 2 * 3
        self.assertEqual(module_0.multiply(-12, -3), 6)    # 2 * 3

    def test_zero(self):
        self.assertEqual(module_0.multiply(0, 5), 0)
        self.assertEqual(module_0.multiply(10, 0), 0)
        self.assertEqual(module_0.multiply(0, 0), 0)

    def test_numbers_ending_in_zero(self):
        self.assertEqual(module_0.multiply(20, 30), 0)
        self.assertEqual(module_0.multiply(100, 55), 0)    # 0 * 5

    def test_single_digits(self):
        self.assertEqual(module_0.multiply(9, 9), 81)
        self.assertEqual(module_0.multiply(1, 1), 1)

    def test_large_numbers(self):
        self.assertEqual(module_0.multiply(123456789, 987654321), 9)  # 9 * 1
        self.assertEqual(module_0.multiply(999999999, 888888888), 72)  # 9 * 8


if __name__ == "__main__":
    unittest.main()
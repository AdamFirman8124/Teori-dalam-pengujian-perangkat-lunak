

# Generated at 2026-11-03 02:13:20.398130
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():import unittest


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(module_0.greatest_common_divisor(48, 18), 6)
        self.assertEqual(module_0.greatest_common_divisor(18, 48), 6)
        self.assertEqual(module_0.greatest_common_divisor(12, 8), 4)
        self.assertEqual(module_0.greatest_common_divisor(100, 25), 25)

    def test_coprime_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(17, 13), 1)
        self.assertEqual(module_0.greatest_common_divisor(35, 64), 1)

    def test_same_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(7, 7), 7)
        self.assertEqual(module_0.greatest_common_divisor(100, 100), 100)

    def test_one_divides_other(self):
        self.assertEqual(module_0.greatest_common_divisor(5, 20), 5)
        self.assertEqual(module_0.greatest_common_divisor(20, 5), 5)

    def test_with_zero(self):
        self.assertEqual(module_0.greatest_common_divisor(0, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 0), 5)
        self.assertEqual(module_0.greatest_common_divisor(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(-48, 18), -6)
        self.assertEqual(module_0.greatest_common_divisor(48, -18), -6)
        self.assertEqual(module_0.greatest_common_divisor(-48, -18), -6)

    def test_one_number_is_one(self):
        self.assertEqual(module_0.greatest_common_divisor(1, 999), 1)
        self.assertEqual(module_0.greatest_common_divisor(999, 1), 1)

    def test_large_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(1071, 462), 21)
        self.assertEqual(module_0.greatest_common_divisor(2**20, 2**15), 2**15)
        self.assertEqual(module_0.greatest_common_divisor(123456, 789012), 12)

    def test_result_divides_both_inputs(self):
        a, b = 462, 1071
        g = module_0.greatest_common_divisor(a, b)
        self.assertEqual(a % g, 0)
        self.assertEqual(b % g, 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 02:14:45.389757
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive numbers
    assert module_0.greatest_common_divisor(12, 18) == 6
    assert module_0.greatest_common_divisor(18, 12) == 6
    assert module_0.greatest_common_divisor(48, 36) == 12
    assert module_0.greatest_common_divisor(7, 5) == 1  # coprime numbers

    # One operand is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Equal numbers
    assert module_0.greatest_common_divisor(10, 10) == 10
    assert module_0.greatest_common_divisor(1, 1) == 1

    # One divides the other
    assert module_0.greatest_common_divisor(4, 12) == 4
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Negative numbers
    assert module_0.greatest_common_divisor(-12, 18) == -6
    assert module_0.greatest_common_divisor(12, -18) == 6
    assert module_0.greatest_common_divisor(-12, -18) == 6

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**10) == 1024

    print("All tests passed!")

# Generated at 2026-11-03 02:16:05.813251
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 7) == 1
    assert module_0.greatest_common_divisor(10, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1

    # One is a multiple of the other
    assert module_0.greatest_common_divisor(12, 36) == 12
    assert module_0.greatest_common_divisor(36, 12) == 12

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Negative numbers (result is positive gcd)
    assert module_0.greatest_common_divisor(-10, -15) == 5
    assert module_0.greatest_common_divisor(-10, 15) == 5

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15

    print("All tests passed!")

# Generated at 2026-11-03 02:17:19.502752
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():import unittest


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(module_0.greatest_common_divisor(48, 18), 6)

    def test_basic_case_reversed(self):
        self.assertEqual(module_0.greatest_common_divisor(18, 48), 6)

    def test_coprime_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(17, 13), 1)

    def test_one_divides_other(self):
        self.assertEqual(module_0.greatest_common_divisor(10, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 10), 5)

    def test_equal_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(7, 7), 7)

    def test_with_zero(self):
        self.assertEqual(module_0.greatest_common_divisor(0, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 0), 5)

    def test_both_zero(self):
        self.assertEqual(module_0.greatest_common_divisor(0, 0), 0)

    def test_one_is_one(self):
        self.assertEqual(module_0.greatest_common_divisor(1, 999), 1)
        self.assertEqual(module_0.greatest_common_divisor(999, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(-48, 18), 6)
        self.assertEqual(module_0.greatest_common_divisor(48, -18), 6)
        self.assertEqual(module_0.greatest_common_divisor(-48, -18), 6)

    def test_large_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(1071, 462), 21)
        self.assertEqual(module_0.greatest_common_divisor(123456789, 987654321), 9)

    def test_consecutive_integers(self):
        self.assertEqual(module_0.greatest_common_divisor(100, 101), 1)

    def test_result_divides_both_inputs(self):
        a, b = 255, 175
        g = module_0.greatest_common_divisor(a, b)
        self.assertEqual(a % g, 0)
        self.assertEqual(b % g, 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 02:18:40.004253
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6

    # One number is a multiple of the other
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(7, 3) == 1

    # Zero cases
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Equal numbers
    assert module_0.greatest_common_divisor(12, 12) == 12

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(270, 192) == 6

    # Powers of two
    assert module_0.greatest_common_divisor(64, 96) == 32

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()
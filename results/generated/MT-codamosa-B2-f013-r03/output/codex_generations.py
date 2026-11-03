

# Generated at 2026-11-01 21:07:13.333952
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(270, 192) == 6
    assert module_0.greatest_common_divisor(1071, 462) == 21

    # Coprime numbers
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # One divides the other
    assert module_0.greatest_common_divisor(100, 25) == 25
    assert module_0.greatest_common_divisor(25, 100) == 25
    assert module_0.greatest_common_divisor(7, 21) == 7

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1
    assert module_0.greatest_common_divisor(12, 12) == 12

    # Zero cases
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative inputs (check magnitude of result)
    assert abs(module_0.greatest_common_divisor(-4, 6)) == 2
    assert abs(module_0.greatest_common_divisor(4, -6)) == 2
    assert abs(module_0.greatest_common_divisor(-4, -6)) == 2

    # Large numbers
    assert module_0.greatest_common_divisor(2**60, 2**40) == 2**40
    assert module_0.greatest_common_divisor(123456789, 987654321) == 9

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-01 21:07:51.527090
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():import unittest


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(module_0.greatest_common_divisor(12, 8), 4)
        self.assertEqual(module_0.greatest_common_divisor(48, 18), 6)
        self.assertEqual(module_0.greatest_common_divisor(100, 75), 25)

    def test_one_divides_other(self):
        self.assertEqual(module_0.greatest_common_divisor(10, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 10), 5)
        self.assertEqual(module_0.greatest_common_divisor(21, 7), 7)

    def test_coprime_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(8, 9), 1)
        self.assertEqual(module_0.greatest_common_divisor(17, 13), 1)
        self.assertEqual(module_0.greatest_common_divisor(35, 64), 1)

    def test_same_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(7, 7), 7)
        self.assertEqual(module_0.greatest_common_divisor(100, 100), 100)

    def test_with_zero(self):
        self.assertEqual(module_0.greatest_common_divisor(0, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 0), 5)
        self.assertEqual(module_0.greatest_common_divisor(0, 0), 0)

    def test_with_one(self):
        self.assertEqual(module_0.greatest_common_divisor(1, 5), 1)
        self.assertEqual(module_0.greatest_common_divisor(5, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(-12, 8), 4)
        self.assertEqual(module_0.greatest_common_divisor(12, -8), 4)
        self.assertEqual(module_0.greatest_common_divisor(-12, -8), 4)

    def test_large_numbers(self):
        self.assertEqual(module_0.greatest_common_divisor(1071, 462), 21)
        self.assertEqual(module_0.greatest_common_divisor(2**20, 2**15), 2**15)

    def test_result_divides_both(self):
        a, b = 462, 1071
        g = module_0.greatest_common_divisor(a, b)
        self.assertEqual(a % g, 0)
        self.assertEqual(b % g, 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 21:08:47.393830
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(25, 15) == 5

    # One argument divides the other
    assert module_0.greatest_common_divisor(10, 5) == 5
    assert module_0.greatest_common_divisor(5, 10) == 5

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(9, 28) == 1
    assert module_0.greatest_common_divisor(7, 7) == 7

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative numbers (use abs: sign follows Python's modulo semantics)
    assert module_0.greatest_common_divisor(-4, 6) == 2
    assert abs(module_0.greatest_common_divisor(6, -4)) == 2
    assert abs(module_0.greatest_common_divisor(-12, -18)) == 6

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**15) == 2**15

    print("All tests passed!")


test_greatest_common_divisor()

# Generated at 2026-11-01 21:09:25.116825
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6  # order shouldn't matter
    assert module_0.greatest_common_divisor(100, 25) == 25
    assert module_0.greatest_common_divisor(25, 100) == 25

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(8, 9) == 1

    # Identical numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(42, 42) == 42

    # One argument is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # One divides the other
    assert module_0.greatest_common_divisor(12, 4) == 4
    assert module_0.greatest_common_divisor(4, 12) == 4

    # Negative numbers (gcd conventionally non-negative)
    assert module_0.greatest_common_divisor(-48, 18) == 6
    assert module_0.greatest_common_divisor(48, -18) == 6
    assert module_0.greatest_common_divisor(-48, -18) == 6

    # Large numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20, 2**10) == 2**10

    # Prime numbers
    assert module_0.greatest_common_divisor(97, 89) == 1
    assert module_0.greatest_common_divisor(97, 97) == 97

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-01 21:09:54.432741
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Test basic cases
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6

    # Test coprime numbers
    assert module_0.greatest_common_divisor(7, 13) == 1
    assert module_0.greatest_common_divisor(17, 5) == 1

    # Test when one divides the other
    assert module_0.greatest_common_divisor(5, 10) == 5
    assert module_0.greatest_common_divisor(10, 5) == 5

    # Test with zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Test with equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(100, 100) == 100

    # Test with negative numbers
    assert module_0.greatest_common_divisor(-12, 8) == 4
    assert module_0.greatest_common_divisor(12, -8) == 4
    assert module_0.greatest_common_divisor(-12, -8) == 4

    # Test with larger numbers
    assert module_0.greatest_common_divisor(270, 192) == 6
    assert module_0.greatest_common_divisor(1000000, 500000) == 500000

    print("All tests passed!")


test_greatest_common_divisor()
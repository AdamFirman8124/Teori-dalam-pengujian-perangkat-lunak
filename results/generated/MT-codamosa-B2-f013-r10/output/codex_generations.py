

# Generated at 2026-11-02 21:30:32.867592
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(100, 75) == 25

    # One argument is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Both zero
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(2, 3) == 1

    # Negative numbers
    assert module_0.greatest_common_divisor(-4, 6) == 2
    assert module_0.greatest_common_divisor(-8, -12) == 4
    assert module_0.greatest_common_divisor(10, -5) == 5

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(123456, 789012) == 12

    # Power-of-two related
    assert module_0.greatest_common_divisor(64, 128) == 64
    assert module_0.greatest_common_divisor(96, 128) == 32

    print("All tests passed!")


class TestGreatestCommonDivisor(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.greatest_common_divisor(3, 5), 1)
        self.assertEqual(module_0.greatest_common_divisor(25, 15), 5)
        self.assertEqual(module_0.greatest_common_divisor(48, 18), 6)

    def test_zero(self):
        self.assertEqual(module_0.greatest_common_divisor(0, 5), 5)
        self.assertEqual(module_0.greatest_common_divisor(5, 0), 5)
        self.assertEqual(module_0.greatest_common_divisor(0, 0), 0)

    def test_negative(self):
        self.assertEqual(module_0.greatest_common_divisor(-4, 6), 2)
        self.assertEqual(module_0.greatest_common_divisor(-8, -12), 4)

    def test_large(self):
        self.assertEqual(module_0.greatest_common_divisor(1071, 462), 21)
        self.assertEqual(module_0.greatest_common_divisor(123456, 789012), 12)


if __name__ == "__main__":
    test_greatest_common_divisor()
    unittest.main()

# Generated at 2026-11-02 21:32:52.337099
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic cases
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(7, 7) == 7

    # One argument is zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5

    # Coprime numbers
    assert module_0.greatest_common_divisor(17, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Negative first argument
    assert module_0.greatest_common_divisor(-4, 6) == 2

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(100000, 25000) == 25000

    # Both zero
    assert module_0.greatest_common_divisor(0, 0) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()

# Generated at 2026-11-02 21:34:50.728437
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic coprime numbers
    assert module_0.greatest_common_divisor(3, 5) == 1
    assert module_0.greatest_common_divisor(5, 3) == 1

    # Common divisor cases
    assert module_0.greatest_common_divisor(25, 15) == 5
    assert module_0.greatest_common_divisor(15, 25) == 5
    assert module_0.greatest_common_divisor(12, 8) == 4
    assert module_0.greatest_common_divisor(8, 12) == 4

    # One divides the other
    assert module_0.greatest_common_divisor(6, 18) == 6
    assert module_0.greatest_common_divisor(18, 6) == 6

    # Equal numbers
    assert module_0.greatest_common_divisor(7, 7) == 7
    assert module_0.greatest_common_divisor(100, 100) == 100

    # With zero
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative numbers (Euclidean algorithm returns sign of initial a)
    assert module_0.greatest_common_divisor(-25, 15) == -5
    assert module_0.greatest_common_divisor(25, -15) == 5
    assert module_0.greatest_common_divisor(-25, -15) == -5

    # Larger numbers
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(462, 1071) == 21
    assert module_0.greatest_common_divisor(2**10, 2**5) == 32

    # Prime numbers
    assert module_0.greatest_common_divisor(13, 17) == 1
    assert module_0.greatest_common_divisor(97, 89) == 1

    print("All tests passed!")


test_greatest_common_divisor()

# Generated at 2026-11-02 21:38:21.005061
# Unit test for function greatest_common_divisor
def test_greatest_common_divisor():
    # Basic positive cases
    assert module_0.greatest_common_divisor(48, 18) == 6
    assert module_0.greatest_common_divisor(18, 48) == 6
    assert module_0.greatest_common_divisor(270, 192) == 6
    assert module_0.greatest_common_divisor(12, 8) == 4

    # One number divides the other
    assert module_0.greatest_common_divisor(25, 100) == 25
    assert module_0.greatest_common_divisor(100, 25) == 25

    # Coprime numbers
    assert module_0.greatest_common_divisor(7, 13) == 1
    assert module_0.greatest_common_divisor(35, 64) == 1

    # Equal numbers
    assert module_0.greatest_common_divisor(10, 10) == 10
    assert module_0.greatest_common_divisor(1, 1) == 1

    # Zero handling
    assert module_0.greatest_common_divisor(0, 5) == 5
    assert module_0.greatest_common_divisor(5, 0) == 5
    assert module_0.greatest_common_divisor(0, 0) == 0

    # Negative inputs (Python modulo semantics; sign may follow divisor)
    assert module_0.greatest_common_divisor(-4, 6) == 2
    assert abs(module_0.greatest_common_divisor(4, -6)) == 2
    assert abs(module_0.greatest_common_divisor(-4, -6)) == 2

    # Classic and large-number cases
    assert module_0.greatest_common_divisor(1071, 462) == 21
    assert module_0.greatest_common_divisor(2**20 * 3, 2**18 * 5) == 2**18

    print("All tests passed!")


if __name__ == "__main__":
    test_greatest_common_divisor()


# Generated at 2026-11-03 01:36:29.053135
# Unit test for function circular_shift
def test_circular_shift():
    # Basic circular shift: last `shift` digits move to the front
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(123, 1) == "312"
    assert module_0.circular_shift(123, 2) == "231"
    assert module_0.circular_shift(100, 2) == "001"

    # Shift equal to length returns the original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(123, 3) == "123"

    # Shift greater than length returns the reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(97, 8) == "79"
    assert module_0.circular_shift(11, 101) == "11"
    assert module_0.circular_shift(12345, 6) == "54321"

    # Zero shift returns the original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit cases
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Result is always a string
    assert isinstance(module_0.circular_shift(12, 1), str)

# Generated at 2026-11-03 01:37:45.957449
# Unit test for function circular_shift
def test_circular_shift():
    # shift within length: rotate right by shift digits
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(1234, 3) == "2341"

    # shift equal to length: string unchanged
    assert module_0.circular_shift(123, 3) == "123"

    # shift of zero: string unchanged
    assert module_0.circular_shift(123, 0) == "123"

    # shift greater than length: reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 5) == "321"
    assert module_0.circular_shift(12345, 6) == "54321"

    # single digit cases
    assert module_0.circular_shift(7, 1) == "7"
    assert module_0.circular_shift(7, 10) == "7"

    # zero as input
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(0, 5) == "0"

    # result is always a string
    assert isinstance(module_0.circular_shift(123, 1), str)

# Generated at 2026-11-03 01:38:47.498167
# Unit test for function circular_shift
def test_circular_shift():import unittest


class TestCircularShift(unittest.TestCase):

    def test_basic_shift(self):
        self.assertEqual(module_0.circular_shift(12, 1), "21")

    def test_shift_by_one(self):
        self.assertEqual(module_0.circular_shift(1234, 1), "4123")

    def test_shift_by_two(self):
        self.assertEqual(module_0.circular_shift(123, 2), "231")

    def test_shift_equals_length(self):
        self.assertEqual(module_0.circular_shift(123, 3), "123")

    def test_shift_zero(self):
        self.assertEqual(module_0.circular_shift(123, 0), "123")

    def test_shift_greater_than_length(self):
        self.assertEqual(module_0.circular_shift(123, 4), "321")

    def test_shift_much_greater_than_length(self):
        self.assertEqual(module_0.circular_shift(12345, 10), "54321")

    def test_single_digit(self):
        self.assertEqual(module_0.circular_shift(5, 1), "5")

    def test_zero(self):
        self.assertEqual(module_0.circular_shift(0, 1), "0")

    def test_result_is_string(self):
        self.assertIsInstance(module_0.circular_shift(123, 1), str)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 01:40:23.976077
# Unit test for function circular_shift
def test_circular_shift():
# nonce:35038a20
    # Basic circular shifts
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to length returns original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than length returns reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(1234, 5) == "4321"
    assert module_0.circular_shift(100, 10) == "001"

    # Shift of zero returns original string
    assert module_0.circular_shift(1234, 0) == "1234"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 2) == "5"

    # Zero
    assert module_0.circular_shift(0, 1) == "0"
    assert module_0.circular_shift(0, 10) == "0"

    # Negative numbers (sign is part of the string)
    assert module_0.circular_shift(-12, 1) == "2-1"
    assert module_0.circular_shift(-12, 5) == "21-"

    print("All tests passed!")


test_circular_shift()

# Generated at 2026-11-03 01:42:35.959453
# Unit test for function circular_shift
def test_circular_shift():
    # nonce:45f35f27
    # Basic circular shift (right shift by given amount)
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(1234, 1) == "4123"
    assert module_0.circular_shift(1234, 2) == "3412"
    assert module_0.circular_shift(1234, 3) == "2341"

    # Shift equal to string length returns the original string
    assert module_0.circular_shift(12, 2) == "12"
    assert module_0.circular_shift(1234, 4) == "1234"

    # Shift greater than string length returns the reversed string
    assert module_0.circular_shift(12, 3) == "21"
    assert module_0.circular_shift(123, 5) == "321"
    assert module_0.circular_shift(123, 100) == "321"

    # Shift of zero returns the original string
    assert module_0.circular_shift(123, 0) == "123"

    # Single digit numbers
    assert module_0.circular_shift(5, 1) == "5"
    assert module_0.circular_shift(5, 10) == "5"

    # Numbers containing zeros
    assert module_0.circular_shift(1000000, 3) == "0001000"
    assert module_0.circular_shift(1050, 2) == "5010"

    # Result is always a string
    assert isinstance(module_0.circular_shift(1234, 2), str)
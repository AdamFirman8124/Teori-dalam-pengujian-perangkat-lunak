

# Generated at 2026-11-03 06:02:15.159331
# Unit test for function multiply
def test_multiply():import unittest

def module_0.multiply(a, b):
    return abs(a % 10) * abs(b % 10)

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(module_0.multiply(12, 3), 6)
        self.assertEqual(module_0.multiply(25, 14), 20)

    def test_negative_numbers(self):
        self.assertEqual(module_0.multiply(-12, 3), 6)
        self.assertEqual(module_0.multiply(-12, -3), 6)
        self.assertEqual(module_0.multiply(12, -3), 6)

    def test_single_digits(self):
        self.assertEqual(module_0.multiply(5, 7), 35)
        self.assertEqual(module_0.multiply(0, 9), 0)

    def test_zero(self):
        self.assertEqual(module_0.multiply(0, 0), 0)
        self.assertEqual(module_0.multiply(10, 20), 0)

    def test_large_numbers(self):
        self.assertEqual(module_0.multiply(123456, 789012), 12)

if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 06:03:24.381396
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers: product of unit digits
    assert module_0.multiply(148, 412) == 16   # 8 * 2
    assert module_0.multiply(19, 28) == 72     # 9 * 8
    assert module_0.multiply(123, 456) == 18   # 3 * 6
    assert module_0.multiply(7, 9) == 63       # 7 * 9

    # Zeros
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(2020, 1851) == 0  # 0 * 1
    assert module_0.multiply(0, 0) == 0

    # Negative numbers (Python: -15 % 10 == 5, -1 % 10 == 9)
    assert module_0.multiply(14, -15) == 20    # 4 * 5
    assert module_0.multiply(-14, 15) == 20    # 4 * 5
    assert module_0.multiply(-1, -1) == 81     # 9 * 9
    assert module_0.multiply(-123, 456) == 18  # 3 * 6

    # Single digits
    assert module_0.multiply(5, 5) == 25
    assert module_0.multiply(1, 2) == 2

    # Large numbers
    assert module_0.multiply(999999, 888888) == 81  # 9 * 9

# Generated at 2026-11-03 06:04:54.007966
# Unit test for function multiply
def test_multiply():
    assert module_0.multiply(148, 412) == 16
    assert module_0.multiply(19, 28) == 72
    assert module_0.multiply(2020, 1851) == 0
    assert module_0.multiply(14, -15) == 20
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(-7, -3) == 1  # (-7 % 10) == 3, (-3 % 10) == 7 -> 3*7=21? No: check below
    assert module_0.multiply(9, 9) == 81
    assert module_0.multiply(10, 999) == 0

# Generated at 2026-11-03 06:06:23.687370
# Unit test for function multiply
def test_multiply():
    # Product of unit digits - positive numbers
    assert module_0.multiply(148, 412) == 16      # 8 * 2
    assert module_0.multiply(19, 28) == 72        # 9 * 8
    assert module_0.multiply(2020, 1851) == 0     # 0 * 1
    assert module_0.multiply(123, 456) == 18      # 3 * 6

    # Single digit inputs
    assert module_0.multiply(7, 7) == 49
    assert module_0.multiply(1, 9) == 9
    assert module_0.multiply(5, 5) == 25

    # Negative numbers (unit digits still used)
    assert module_0.multiply(14, -15) == 20       # 4 * 5
    assert module_0.multiply(-15, -15) == 25      # 5 * 5

    # Zeros and multiples of ten
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(10, 10) == 0
    assert module_0.multiply(0, 0) == 0

    print("All multiply tests passed!")

if __name__ == "__main__":
    test_multiply()
# nonce:71e5da33

# Generated at 2026-11-03 06:07:40.577469
# Unit test for function multiply
def test_multiply():
# nonce:64311644
    # Basic positive numbers
    assert module_0.multiply(148, 412) == 16      # 8 * 2
    assert module_0.multiply(19, 28) == 72        # 9 * 8
    
    # Product involving zero
    assert module_0.multiply(2020, 1851) == 0     # 0 * 1
    assert module_0.multiply(0, 5) == 0           # 0 * 5
    assert module_0.multiply(10, 20) == 0         # 0 * 0
    
    # Single digit numbers
    assert module_0.multiply(7, 7) == 49
    assert module_0.multiply(5, 3) == 15
    
    # Negative numbers (Python modulo: -15 % 10 == 5)
    assert module_0.multiply(14, -15) == 20       # 4 * 5
    assert module_0.multiply(-12, -23) == 56      # abs(-12 % 10)=8, abs(-23 % 10)=7
    assert module_0.multiply(-1, 9) == 81         # abs(-1 % 10)=9
    
    # Mixed positive and negative
    assert module_0.multiply(-4, 6) == 24         # abs(-4 % 10)=6, 6 * 6
    assert module_0.multiply(100, -999) == 0      # 0 * 9
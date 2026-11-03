

# Generated at 2026-11-03 00:33:45.611832
# Unit test for function iscube
def test_iscube():
    # Perfect positive cubes
    assert module_0.iscube(1) is True
    assert module_0.iscube(8) is True
    assert module_0.iscube(27) is True
    assert module_0.iscube(64) is True
    assert module_0.iscube(125) is True
    assert module_0.iscube(1000) is True

    # Perfect negative cubes (abs is applied, so these should be True)
    assert module_0.iscube(-1) is True
    assert module_0.iscube(-8) is True
    assert module_0.iscube(-27) is True
    assert module_0.iscube(-64) is True

    # Zero is a cube (0**3 == 0)
    assert module_0.iscube(0) is True

    # Non-cube positive integers
    assert module_0.iscube(2) is False
    assert module_0.iscube(3) is False
    assert module_0.iscube(4) is False
    assert module_0.iscube(9) is False
    assert module_0.iscube(10) is False
    assert module_0.iscube(26) is False
    assert module_0.iscube(28) is False

    # Non-cube negative integers
    assert module_0.iscube(-2) is False
    assert module_0.iscube(-3) is False
    assert module_0.iscube(-9) is False

    # Larger perfect cubes
    assert module_0.iscube(1000000) is True      # 100**3
    assert module_0.iscube(-1000000) is True     # -100**3
    assert module_0.iscube(27000) is True        # 30**3

    # Larger non-cubes
    assert module_0.iscube(1000001) is False
    assert module_0.iscube(999999) is False

    # Numbers close to cubes (floating-point boundary cases)
    assert module_0.iscube(2 ** 3 - 1) is False   # 7
    assert module_0.iscube(2 ** 3 + 1) is False   # 9
    assert module_0.iscube(10 ** 3 - 1) is False  # 999
    assert module_0.iscube(10 ** 3 + 1) is False  # 1001

# Generated at 2026-11-03 00:34:31.717082
# Unit test for function iscube
def test_iscube():import unittest


class TestIscube(unittest.TestCase):

    def test_positive_cubes(self):
        self.assertTrue(module_0.iscube(1))
        self.assertTrue(module_0.iscube(8))
        self.assertTrue(module_0.iscube(27))
        self.assertTrue(module_0.iscube(64))
        self.assertTrue(module_0.iscube(125))
        self.assertTrue(module_0.iscube(1000))

    def test_negative_cubes(self):
        self.assertTrue(module_0.iscube(-1))
        self.assertTrue(module_0.iscube(-8))
        self.assertTrue(module_0.iscube(-27))
        self.assertTrue(module_0.iscube(-64))
        self.assertTrue(module_0.iscube(-125))

    def test_zero(self):
        self.assertTrue(module_0.iscube(0))

    def test_non_cubes(self):
        self.assertFalse(module_0.iscube(2))
        self.assertFalse(module_0.iscube(3))
        self.assertFalse(module_0.iscube(9))
        self.assertFalse(module_0.iscube(10))
        self.assertFalse(module_0.iscube(26))
        self.assertFalse(module_0.iscube(28))
        self.assertFalse(module_0.iscube(-2))
        self.assertFalse(module_0.iscube(-9))

    def test_large_cube(self):
        self.assertTrue(module_0.iscube(1000000))      # 100^3
        self.assertTrue(module_0.iscube(27000))        # 30^3
        self.assertFalse(module_0.iscube(1000001))

    def test_near_miss_values(self):
        # Values just off from perfect cubes
        self.assertFalse(module_0.iscube(7))
        self.assertFalse(module_0.iscube(9))
        self.assertFalse(module_0.iscube(63))
        self.assertFalse(module_0.iscube(65))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 00:35:13.879029
# Unit test for function iscube
def test_iscube():
    # Perfect cubes (positive)
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True
    assert module_0.iscube(1728) == True      # 12^3
    assert module_0.iscube(27000) == True     # 30^3

    # Perfect cubes (negative) - abs() handles these
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-1000) == True

    # Zero is a cube (0^3)
    assert module_0.iscube(0) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-10) == False
    assert module_0.iscube(26) == False

    # Larger numbers
    assert module_0.iscube(1000000) == True       # 100^3
    assert module_0.iscube(999999) == False
    assert module_0.iscube(1277742720) == True    # 1044^3

    print("All tests passed!")

# Generated at 2026-11-03 00:36:02.730842
# Unit test for function iscube
def test_iscube():
    # Perfect positive cubes
    assert module_0.iscube(0) == True
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True
    assert module_0.iscube(1000000) == True

    # Perfect negative cubes (abs is applied, so these should be True)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-125) == True
    assert module_0.iscube(-1000) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False

    # Larger values
    assert module_0.iscube(10 ** 9) == True          # (10^3)^3
    assert module_0.iscube(999999999) == False
    assert module_0.iscube(12 ** 3) == True          # 1728
    assert module_0.iscube(1729) == False            # famous taxicab number, not a cube

    # Boundary around small cubes
    assert module_0.iscube(7) == False
    assert module_0.iscube(9) == False

    # Very large cube
    assert module_0.iscube(1000 ** 3) == True        # 10^9
    assert module_0.iscube(-(1000 ** 3)) == True

# Generated at 2026-11-03 00:37:19.089309
# Unit test for function iscube
def test_iscube():
    # Test positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Test zero (0 is a perfect cube: 0^3 = 0)
    assert module_0.iscube(0) == True

    # Test negative perfect cubes (abs is taken, so -8 is a cube)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Test non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(5) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(-10) == False

    # Test large perfect cubes
    assert module_0.iscube(1000000) == True      # 100^3
    assert module_0.iscube(1000000000000) == True  # 10^12 = 10^4 cubed
    assert module_0.iscube(-1000000) == True

    # Test large non-cubes
    assert module_0.iscube(1000001) == False
    assert module_0.iscube(999999) == False

    # Test boundary between cubes
    assert module_0.iscube(63) == False
    assert module_0.iscube(65) == False
    assert module_0.iscube(124) == False
    assert module_0.iscube(126) == False
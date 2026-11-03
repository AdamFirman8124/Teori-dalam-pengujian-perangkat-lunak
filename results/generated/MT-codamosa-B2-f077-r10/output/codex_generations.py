

# Generated at 2026-11-02 09:22:14.712193
# Unit test for function iscube
def test_iscube():import unittest


class TestIscube(unittest.TestCase):
    def test_iscube(self):
        # Positive perfect cubes
        self.assertTrue(module_0.iscube(1))
        self.assertTrue(module_0.iscube(8))
        self.assertTrue(module_0.iscube(27))
        self.assertTrue(module_0.iscube(64))
        self.assertTrue(module_0.iscube(125))
        self.assertTrue(module_0.iscube(1000))

        # Zero is a cube
        self.assertTrue(module_0.iscube(0))

        # Negative perfect cubes (abs handled)
        self.assertTrue(module_0.iscube(-1))
        self.assertTrue(module_0.iscube(-8))
        self.assertTrue(module_0.iscube(-27))
        self.assertTrue(module_0.iscube(-64))

        # Non-cubes
        self.assertFalse(module_0.iscube(2))
        self.assertFalse(module_0.iscube(9))
        self.assertFalse(module_0.iscube(10))
        self.assertFalse(module_0.iscube(26))
        self.assertFalse(module_0.iscube(28))
        self.assertFalse(module_0.iscube(100))

        # Large values
        self.assertTrue(module_0.iscube(1000000))
        self.assertTrue(module_0.iscube(-1000000))
        self.assertFalse(module_0.iscube(999999))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 09:24:41.820454
# Unit test for function iscube
def test_iscube():
    # Test positive perfect cubes
    assert module_0.iscube(1) == True, "1 is a cube (1^3)"
    assert module_0.iscube(8) == True, "8 is a cube (2^3)"
    assert module_0.iscube(27) == True, "27 is a cube (3^3)"
    assert module_0.iscube(64) == True, "64 is a cube (4^3)"
    assert module_0.iscube(125) == True, "125 is a cube (5^3)"
    assert module_0.iscube(216) == True, "216 is a cube (6^3)"
    assert module_0.iscube(1000) == True, "1000 is a cube (10^3)"

    # Test zero
    assert module_0.iscube(0) == True, "0 is a cube (0^3)"

    # Test negative perfect cubes (abs is taken, so they should be cubes)
    assert module_0.iscube(-1) == True, "-1 is a cube"
    assert module_0.iscube(-8) == True, "-8 is a cube"
    assert module_0.iscube(-27) == True, "-27 is a cube"
    assert module_0.iscube(-64) == True, "-64 is a cube"

    # Test non-cubes
    assert module_0.iscube(2) == False, "2 is not a cube"
    assert module_0.iscube(3) == False, "3 is not a cube"
    assert module_0.iscube(4) == False, "4 is not a cube"
    assert module_0.iscube(9) == False, "9 is not a cube"
    assert module_0.iscube(10) == False, "10 is not a cube"
    assert module_0.iscube(26) == False, "26 is not a cube"
    assert module_0.iscube(28) == False, "28 is not a cube"
    assert module_0.iscube(-5) == False, "-5 is not a cube"
    assert module_0.iscube(-10) == False, "-10 is not a cube"

    # Test larger numbers
    assert module_0.iscube(1728) == True, "1728 is a cube (12^3)"
    assert module_0.iscube(27000) == True, "27000 is a cube (30^3)"
    assert module_0.iscube(1000000) == True, "1000000 is a cube (100^3)"
    assert module_0.iscube(1000001) == False, "1000001 is not a cube"
    assert module_0.iscube(999999) == False, "999999 is not a cube"

    # Test numbers near cube boundaries (floating point robustness)
    assert module_0.iscube(63) == False, "63 is not a cube"
    assert module_0.iscube(65) == False, "65 is not a cube"
    assert module_0.iscube(124) == False, "124 is not a cube"
    assert module_0.iscube(126) == False, "126 is not a cube"

    print("All tests passed!")


if __name__ == "__main__":
    test_iscube()

# Generated at 2026-11-02 09:26:58.114459
# Unit test for function iscube
def test_iscube():
    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(512) == True
    assert module_0.iscube(1000) == True
    assert module_0.iscube(1728) == True
    assert module_0.iscube(1000000) == True

    # Negative perfect cubes (function uses abs)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-125) == True
    assert module_0.iscube(-1000) == True

    # Positive non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(5) == False
    assert module_0.iscube(6) == False
    assert module_0.iscube(7) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(999) == False

    # Negative non-cubes
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-7) == False
    assert module_0.iscube(-26) == False
    assert module_0.iscube(-100) == False

# Generated at 2026-11-02 09:28:50.896038
# Unit test for function iscube
def test_iscube():
    # Test positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True

    # Test negative perfect cubes
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Test zero
    assert module_0.iscube(0) == True

    # Test non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False

    # Test large numbers
    assert module_0.iscube(1000000) == True      # 100^3
    assert module_0.iscube(1000001) == False
    assert module_0.iscube(-1000000) == True

    # Test numbers close to cubes (rounding edge cases)
    assert module_0.iscube(63) == False
    assert module_0.iscube(65) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_iscube()
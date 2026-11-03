

# Generated at 2026-11-03 04:39:59.137141
# Unit test for function iscube
def test_iscube():
    # Positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Negative perfect cubes (abs handles sign)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(180) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-100) == False

    # Large cube values
    assert module_0.iscube(1000000) == True      # 100^3
    assert module_0.iscube(999999) == False
    assert module_0.iscube(-1000000) == True

    print("All iscube tests passed!")


test_iscube()

# Generated at 2026-11-03 04:40:21.838649
# Unit test for function iscube
def test_iscube():
    # Perfect cubes
    assert module_0.iscube(0) == True
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000000) == True

    # Negative perfect cubes (abs is applied)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-125) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(180) == False
    assert module_0.iscube(126) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(999999) == False

    # Large cube
    assert module_0.iscube(27000) == True   # 30 ** 3
    assert module_0.iscube(27001) == False

# Generated at 2026-11-03 04:41:33.430402
# Unit test for function iscube
def test_iscube():
    # Perfect positive cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Negative perfect cubes (abs value makes them valid)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(100) == False

    # Negative non-cubes
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False
    assert module_0.iscube(-100) == False

    # Larger values
    assert module_0.iscube(512) == True       # 8^3
    assert module_0.iscube(729) == True       # 9^3
    assert module_0.iscube(1000000) == True   # 100^3
    assert module_0.iscube(-1000000) == True  # (-100)^3
    assert module_0.iscube(999999) == False   # not a cube

    print("All tests passed!")

# Generated at 2026-11-03 04:44:31.488841
# Unit test for function iscube
def test_iscube():
    # Zero is a perfect cube (0^3 = 0)
    assert module_0.iscube(0) == True

    # Positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(216) == True
    assert module_0.iscube(1000) == True

    # Negative perfect cubes (abs makes them valid)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-1000) == True

    # Positive non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(999) == False

    # Negative non-cubes
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False
    assert module_0.iscube(-28) == False

    # Large numbers
    assert module_0.iscube(1000000) == True       # 100^3
    assert module_0.iscube(1000001) == False
    assert module_0.iscube(1000003) == False
    assert module_0.iscube(10**18) == True        # (10^6)^3
    assert module_0.iscube(-(10**15)) == True     # -(10^5)^3

# Generated at 2026-11-03 04:48:38.069357
# Unit test for function iscube
def test_iscube():import unittest


class TestIsCube(unittest.TestCase):

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
        self.assertFalse(module_0.iscube(100))

    def test_negative_non_cubes(self):
        self.assertFalse(module_0.iscube(-2))
        self.assertFalse(module_0.iscube(-9))
        self.assertFalse(module_0.iscube(-26))

    def test_large_cube(self):
        self.assertTrue(module_0.iscube(1000000))  # 100^3
        self.assertTrue(module_0.iscube(27000))    # 30^3

    def test_large_non_cube(self):
        self.assertFalse(module_0.iscube(1000001))
        self.assertFalse(module_0.iscube(999999))

    def test_large_negative_cube(self):
        self.assertTrue(module_0.iscube(-1000000))


if __name__ == "__main__":
    unittest.main()
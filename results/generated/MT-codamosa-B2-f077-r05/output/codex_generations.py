

# Generated at 2026-11-02 22:56:20.883490
# Unit test for function iscube
def test_iscube():
    # Perfect cubes - positive
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Perfect cubes - negative
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-125) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Not perfect cubes - positive
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(63) == False
    assert module_0.iscube(65) == False

    # Not perfect cubes - negative
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False
    assert module_0.iscube(-28) == False

    # Large perfect cube
    assert module_0.iscube(10 ** 9) == True  # 1000^3
    assert module_0.iscube(1000000) == True  # 100^3

    # Large non-cube
    assert module_0.iscube(10 ** 9 + 1) == False

    # Float cube values
    assert module_0.iscube(2.0 ** 3) == True
    assert module_0.iscube(3.5 ** 3) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_iscube()

# Generated at 2026-11-02 22:59:44.552985
# Unit test for function iscube
def test_iscube():import unittest


def module_0.iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


class TestIscube(unittest.TestCase):

    def test_zero_is_cube(self):
        self.assertTrue(module_0.iscube(0))

    def test_one_is_cube(self):
        self.assertTrue(module_0.iscube(1))

    def test_positive_cube(self):
        self.assertTrue(module_0.iscube(8))
        self.assertTrue(module_0.iscube(27))
        self.assertTrue(module_0.iscube(64))
        self.assertTrue(module_0.iscube(125))
        self.assertTrue(module_0.iscube(1000))

    def test_negative_cube(self):
        self.assertTrue(module_0.iscube(-1))
        self.assertTrue(module_0.iscube(-8))
        self.assertTrue(module_0.iscube(-27))
        self.assertTrue(module_0.iscube(-64))
        self.assertTrue(module_0.iscube(-1000))

    def test_positive_non_cube(self):
        self.assertFalse(module_0.iscube(2))
        self.assertFalse(module_0.iscube(3))
        self.assertFalse(module_0.iscube(9))
        self.assertFalse(module_0.iscube(26))
        self.assertFalse(module_0.iscube(28))

    def test_negative_non_cube(self):
        self.assertFalse(module_0.iscube(-2))
        self.assertFalse(module_0.iscube(-9))
        self.assertFalse(module_0.iscube(-26))
        self.assertFalse(module_0.iscube(-28))

    def test_large_cube(self):
        self.assertTrue(module_0.iscube(1000000))      # 100^3
        self.assertTrue(module_0.iscube(10 ** 18))     # (10^6)^3
        self.assertTrue(module_0.iscube(-(10 ** 18)))

    def test_large_non_cube(self):
        self.assertFalse(module_0.iscube(10 ** 18 + 1))
        self.assertFalse(module_0.iscube(1000001))

    def test_cube_of_cube_root_near_integer(self):
        # Values whose cube root is near an integer but not cubes
        self.assertFalse(module_0.iscube(7))
        self.assertFalse(module_0.iscube(63))
        self.assertFalse(module_0.iscube(65))

    def test_returns_bool(self):
        self.assertIsInstance(module_0.iscube(8), bool)
        self.assertIsInstance(module_0.iscube(7), bool)


if __name__ == "__main__":
    unittest.main()
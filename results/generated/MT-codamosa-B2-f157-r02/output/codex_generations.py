

# Generated at 2026-11-02 22:03:34.645398
# Unit test for function right_angle_triangle
def test_right_angle_triangle():import unittest


class TestRightAngleTriangle(unittest.TestCase):
    def test_classic_3_4_5(self):
        self.assertTrue(module_0.right_angle_triangle(3, 4, 5))

    def test_permutation_5_3_4(self):
        self.assertTrue(module_0.right_angle_triangle(5, 3, 4))

    def test_permutation_4_5_3(self):
        self.assertTrue(module_0.right_angle_triangle(4, 5, 3))

    def test_hypotenuse_first(self):
        self.assertTrue(module_0.right_angle_triangle(5, 12, 13))
        self.assertTrue(module_0.right_angle_triangle(13, 5, 12))

    def test_not_right_triangle(self):
        self.assertFalse(module_0.right_angle_triangle(1, 2, 3))

    def test_equilateral(self):
        self.assertFalse(module_0.right_angle_triangle(2, 2, 2))

    def test_obtuse_triangle(self):
        self.assertFalse(module_0.right_angle_triangle(2, 3, 4))

    def test_acute_triangle(self):
        self.assertFalse(module_0.right_angle_triangle(4, 4, 4))

    def test_another_right_triangle(self):
        self.assertTrue(module_0.right_angle_triangle(8, 6, 10))

    def test_small_numbers(self):
        self.assertFalse(module_0.right_angle_triangle(1, 1, 1))

    def test_degenerate_sides(self):
        self.assertFalse(module_0.right_angle_triangle(1, 1, 2))

    def test_large_right_triangle(self):
        self.assertTrue(module_0.right_angle_triangle(7, 24, 25))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 22:09:25.468227
# Unit test for function right_angle_triangle
def test_right_angle_triangle():# Classic right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Same triangle with sides in different orders
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    # Other right-angled triangles
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    # Non right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 3) == False
    assert module_0.right_angle_triangle(7, 8, 9) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False
    # Nearly right-angled but not
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(20, 21, 29) == True
    assert module_0.right_angle_triangle(20, 21, 30) == False
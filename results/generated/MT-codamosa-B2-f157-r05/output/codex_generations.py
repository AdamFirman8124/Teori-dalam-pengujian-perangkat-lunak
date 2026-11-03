

# Generated at 2026-11-02 05:54:03.948371
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(0, 0, 0) == True  # degenerate: 0 == 0
    assert module_0.right_angle_triangle(7, 24, 25) == True

# Generated at 2026-11-02 05:54:25.396838
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(10, 10, 10) == False

# Generated at 2026-11-02 05:54:48.754433
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Right angle at different positions (permutations)
    assert module_0.right_angle_triangle(4, 3, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(3, 5, 4) == True
    # Another right triangle: 5-12-13
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(13, 12, 5) == True
    # Not a triangle (1, 2, 3)
    assert module_0.right_angle_triangle(1, 2, 3) == False
    # Non-right triangles
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(7, 10, 5) == False
    # Degenerate / invalid sides
    assert module_0.right_angle_triangle(0, 0, 0) == False
    assert module_0.right_angle_triangle(1, 1, 3) == False
    assert module_0.right_angle_triangle(-3, 4, 5) == False
    # Isosceles right triangle (legs 1, 1, hypotenuse sqrt(2) approximated)
    assert module_0.right_angle_triangle(1, 1, 1.4142135623730951) == True
    # Near-miss values should be False
    assert module_0.right_angle_triangle(3, 4, 6) == False

    print("All tests passed!")

# Generated at 2026-11-02 05:55:04.831858
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(9, 40, 41) == True
    assert module_0.right_angle_triangle(1, 1, 1.414) == False
    assert module_0.right_angle_triangle(0, 0, 0) == True

# Generated at 2026-11-02 05:55:38.654922
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic Pythagorean triples
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True

    # Permutations of sides (right angle can be at any position)
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(13, 5, 12) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False  # equilateral

    # Isosceles non-right triangles
    assert module_0.right_angle_triangle(5, 5, 8) == False
    assert module_0.right_angle_triangle(6, 6, 6) == False

    # Degenerate / invalid sides
    assert module_0.right_angle_triangle(0, 0, 0) == False
    assert module_0.right_angle_triangle(1, 1, 2) == False  # degenerate (collinear)
    assert module_0.right_angle_triangle(1, 1, 3) == False

    # Near-miss cases (close but not right)
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(6, 8, 11) == False

    # Large numbers
    assert module_0.right_angle_triangle(300, 400, 500) == True
    assert module_0.right_angle_triangle(1000, 1000, 1000) == False

    print("All tests passed!")


test_right_angle_triangle()
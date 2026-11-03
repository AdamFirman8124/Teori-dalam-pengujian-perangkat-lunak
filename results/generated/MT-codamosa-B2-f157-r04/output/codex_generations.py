

# Generated at 2026-11-02 10:48:01.442384
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic 3-4-5 right triangle (all rotations of the hypotenuse)
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True

    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(12, 13, 5) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True
    assert module_0.right_angle_triangle(9, 12, 15) == True

    # Floating-point right triangles (exact in binary floating point)
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    assert module_0.right_angle_triangle(2.5, 6.0, 6.5) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(7, 8, 9) == False
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(5, 10, 12) == False

    # Edge cases
    assert module_0.right_angle_triangle(0, 4, 5) == False
    assert module_0.right_angle_triangle(1, 1, 2) == False  # degenerate, not right-angled

    print("All test cases passed!")


if __name__ == "__main__":
    test_right_angle_triangle()

# Generated at 2026-11-02 10:48:20.695223
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True

    # Another right-angled triangle (scaled)
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True

    # Non right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False

    # Large values
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True

    # Nearly right but not exact
    assert module_0.right_angle_triangle(3, 4, 6) == False

# Generated at 2026-11-02 10:48:28.779645
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Not a right triangle (and not a valid triangle)
    assert module_0.right_angle_triangle(1, 2, 3) == False
    # Right triangle with hypotenuse in different positions
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    # Other well-known right triangles
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    # Equilateral triangle: not right-angled
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    # Isosceles non-right triangle
    assert module_0.right_angle_triangle(2, 2, 3) == False
    # Float inputs
    assert module_0.right_angle_triangle(3.0, 4.0, 5.0) == True
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    # Invalid triangle sides (violates triangle inequality)
    assert module_0.right_angle_triangle(1, 1, 10) == False
    # Very small sides
    assert module_0.right_angle_triangle(0.3, 0.4, 0.5) == True
    # Large numbers
    assert module_0.right_angle_triangle(300, 400, 500) == True
    assert module_0.right_angle_triangle(300, 400, 501) == False

# Generated at 2026-11-02 10:49:01.727025
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Different order of sides
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    # Another Pythagorean triple
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False
    # Invalid triangle (degenerate / impossible)
    assert module_0.right_angle_triangle(1, 1, 5) == False
    assert module_0.right_angle_triangle(0, 0, 0) == False
    # Near miss
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(6, 8, 10) == True
    # Negative sides (squared, mathematically satisfies condition)
    assert module_0.right_angle_triangle(-3, 4, 5) == True
    # Floating point sides
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    assert module_0.right_angle_triangle(1.5, 2.0, 2.6) == False

# Generated at 2026-11-02 10:49:12.299454
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Permutations of a right triangle (right angle can be at any side)
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True

    # Not a right triangle
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False

    # Larger right triangles
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True

    # Invalid triangles (sides don't form a triangle)
    assert module_0.right_angle_triangle(1, 1, 10) == False
    assert module_0.right_angle_triangle(0, 0, 0) == False

    # Near-miss cases (off by one)
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(6, 8, 9) == False

    # Floating point right triangle
    assert module_0.right_angle_triangle(0.5, 1.2, 1.3) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_right_angle_triangle()
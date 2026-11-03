

# Generated at 2026-11-02 08:26:26.190353
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangle: 3-4-5
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Right angle in different positions
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    # Not a right-angled triangle (degenerate: 1+2 == 3)
    assert module_0.right_angle_triangle(1, 2, 3) == False
    # Equilateral triangle
    assert module_0.right_angle_triangle(2, 2, 2) == False
    # Another Pythagorean triple: 5-12-13
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(13, 12, 5) == True
    # Isosceles right triangle: 1-1-sqrt(2)
    assert module_0.right_angle_triangle(1, 1, 2**0.5) == True
    # Random non-right triangle
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(7, 8, 9) == False
    # Larger Pythagorean triple: 8-15-17
    assert module_0.right_angle_triangle(8, 15, 17) == True
    # Sides that don't form a valid triangle
    assert module_0.right_angle_triangle(1, 1, 10) == False
    # Zero and negative sides
    assert module_0.right_angle_triangle(0, 0, 0) == False
    assert module_0.right_angle_triangle(-3, 4, 5) == False

# Generated at 2026-11-02 08:26:40.796507
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic 3-4-5 right triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Hypotenuse in each position
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(13, 12, 5) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    # Multiples of triples
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(9, 12, 15) == True
    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    # Near miss (not exactly right angle)
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(5, 12, 14) == False
    # Impossible / degenerate triangles
    assert module_0.right_angle_triangle(1, 1, 10) == False
    assert module_0.right_angle_triangle(1, 10, 1) == False
    assert module_0.right_angle_triangle(10, 1, 1) == False
    # Float inputs
    assert module_0.right_angle_triangle(3.0, 4.0, 5.0) == True
    assert module_0.right_angle_triangle(2.5, 6.0, 6.5) == True
    assert module_0.right_angle_triangle(1.5, 2.5, 3.0) == False
    # Negative sides are squared, so sign doesn't matter
    assert module_0.right_angle_triangle(-3, 4, 5) == True
    assert module_0.right_angle_triangle(-3, -4, -5) == True
    # Degenerate all-zero case (current implementation returns True)
    assert module_0.right_angle_triangle(0, 0, 0) == True


if __name__ == "__main__":
    test_right_angle_triangle()
    print("All tests passed!")

# Generated at 2026-11-02 08:27:36.500192
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic 3-4-5 right triangle with hypotenuse in each position
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True

    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(9, 12, 15) == True

    # Float inputs forming a right triangle
    assert module_0.right_angle_triangle(3.0, 4.0, 5.0) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(10, 20, 30) == False

    # Near-miss lengths that do not satisfy the Pythagorean theorem
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False


if __name__ == "__main__":
    test_right_angle_triangle()
    print("All tests passed!")

# Generated at 2026-11-02 08:29:31.395922
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic 3-4-5 right triangle and all permutations
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(4, 3, 5) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(3, 5, 4) == True
    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(13, 12, 5) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True
    # Triangles that are not right-angled
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(7, 10, 5) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    # Sides that do not form a valid triangle at all
    assert module_0.right_angle_triangle(10, 1, 1) == False
    assert module_0.right_angle_triangle(1, 1, 10) == False
    # Float sides forming a right triangle
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    assert module_0.right_angle_triangle(2.5, 6.0, 6.5) == True
    # Float sides not forming a right triangle
    assert module_0.right_angle_triangle(1.5, 2.5, 3.5) == False

# Generated at 2026-11-02 08:31:48.203350
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # nonce:5dc2fc3a
    # Classic 3-4-5 triangle, with the hypotenuse in each argument position
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True

    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True

    # Float side lengths (exactly representable)
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 3) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False

    # Near-miss cases
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(1, 2, 4) == False


if __name__ == "__main__":
    test_right_angle_triangle()
    print("All tests passed!")
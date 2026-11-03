

# Generated at 2026-11-02 07:52:23.159574
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangles (all side orderings)
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(4, 3, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True

    # Multiples of Pythagorean triples
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(10, 6, 8) == True
    assert module_0.right_angle_triangle(300, 400, 500) == True

    # Float sides that are exactly representable
    assert module_0.right_angle_triangle(3.0, 4.0, 5.0) == True
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(5, 5, 5) == False
    assert module_0.right_angle_triangle(2, 2, 3) == False

# nonce:ba4b4ddf

if __name__ == "__main__":
    test_right_angle_triangle()
    print("All tests passed!")

# Generated at 2026-11-02 07:53:11.691094
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) == True
    # Not a right-angled triangle
    assert module_0.right_angle_triangle(1, 2, 3) == False

    # Right angle with hypotenuse in each position
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True
    assert module_0.right_angle_triangle(4, 3, 5) == True
    assert module_0.right_angle_triangle(3, 5, 4) == True

    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(13, 12, 5) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(9, 40, 41) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 1, 1) == False   # equilateral
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(2, 2, 3) == False   # isosceles
    assert module_0.right_angle_triangle(2, 3, 4) == False   # scalene
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(3, 4, 6) == False   # close but not right

    # Float inputs
    assert module_0.right_angle_triangle(3.0, 4.0, 5.0) == True
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    assert module_0.right_angle_triangle(1.0, 1.0, 1.5) == False

    # Edge cases
    assert module_0.right_angle_triangle(0, 0, 0) == False
    assert module_0.right_angle_triangle(-3, 4, 5) == True   # squares are positive

# Generated at 2026-11-02 07:54:46.423909
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Right-angled triangles (True) — hypotenuse tested in each position
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(3, 5, 4) == True
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(9, 12, 15) == True
    # Non right-angled triangles (False)
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(1, 1, 2) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False

test_right_angle_triangle()
print("All test cases passed!")

# Generated at 2026-11-02 07:56:12.699853
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic 3-4-5 right triangle (all orderings)
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True

    # Not a right-angled triangle
    assert module_0.right_angle_triangle(1, 2, 3) == False

    # Other Pythagorean triples
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(9, 40, 41) == True

    # Hypotenuse in different positions
    assert module_0.right_angle_triangle(13, 5, 12) == True
    assert module_0.right_angle_triangle(41, 9, 40) == True

    # Equilateral / non-right triangles
    assert module_0.right_angle_triangle(1, 1, 1) == False
    assert module_0.right_angle_triangle(2, 2, 3) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False

    # Degenerate cases (sides do not form a valid triangle)
    assert module_0.right_angle_triangle(1, 1, 2) == False
    assert module_0.right_angle_triangle(1, 2, 1) == False

    # Float sides (exact in binary floating point)
    assert module_0.right_angle_triangle(2.5, 6.0, 6.5) == True
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True
    assert module_0.right_angle_triangle(1.0, 1.0, 1.0) == False

    # Larger values
    assert module_0.right_angle_triangle(30, 40, 50) == True
    assert module_0.right_angle_triangle(100, 100, 100) == False

# Generated at 2026-11-02 07:57:58.512989
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True
    assert module_0.right_angle_triangle(7, 24, 25) == True
    assert module_0.right_angle_triangle(20, 21, 29) == True

    # Hypotenuse in every position (permutations)
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(5, 4, 3) == True
    assert module_0.right_angle_triangle(10, 8, 6) == True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(3, 4, 6) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False

    # Equilateral triangles are not right-angled
    assert module_0.right_angle_triangle(2, 2, 2) == False
    assert module_0.right_angle_triangle(10, 10, 10) == False

    # Near-miss values
    assert module_0.right_angle_triangle(3, 4, 5.1) == False
    assert module_0.right_angle_triangle(6, 8, 11) == False

    # Floating-point sides forming an exact right triangle
    assert module_0.right_angle_triangle(1.5, 2.0, 2.5) == True

    # Degenerate inputs (documents current behavior)
    assert module_0.right_angle_triangle(0, 0, 0) == True
    assert module_0.right_angle_triangle(1, 0, 1) == True

# nonce:e588cefc


# Generated at 2026-11-02 22:12:01.618240
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle (3, 4, 5) -> area = 6.0
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Equilateral triangle (3, 3, 3) -> area ≈ 3.90
    assert module_0.triangle_area(3, 3, 3) == 3.9

    # Isosceles triangle (5, 5, 6) -> area = 12.0
    assert module_0.triangle_area(5, 5, 6) == 12.0

    # Scalene triangle (7, 8, 9) -> area ≈ 26.83
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Larger valid triangle (10, 12, 14) -> area ≈ 58.79
    assert module_0.triangle_area(10, 12, 14) == 58.79

    # Invalid triangle: violates triangle inequality
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: sum of two sides equals third side
    assert module_0.triangle_area(1, 2, 3) == -1

    # Zero-length side is invalid
    assert module_0.triangle_area(0, 1, 1) == -1

    # Invalid triangle with different ordering of inequality violation
    assert module_0.triangle_area(10, 1, 2) == -1
    assert module_0.triangle_area(1, 10, 2) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 22:14:08.920471
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5 -> area 6.0
    assert module_0.triangle_area(3, 4, 5) == 6.0, "Expected 6.0 for sides (3, 4, 5)"

    # Valid triangle with non-integer result
    assert module_0.triangle_area(4, 8, 5) == 8.18, "Expected 8.18 for sides (4, 8, 5)"

    # Equilateral triangle: area = sqrt(3)
    assert module_0.triangle_area(2, 2, 2) == 1.73, "Expected 1.73 for sides (2, 2, 2)"

    # Another valid triangle: s = 7.5 -> area ~6.5
    assert module_0.triangle_area(7, 5, 3) == 6.5, "Expected 6.5 for sides (7, 5, 3)"

    # Float inputs: s = 3.0 -> area = 1.5
    assert module_0.triangle_area(1.5, 2.0, 2.5) == 1.5, "Expected 1.5 for sides (1.5, 2.0, 2.5)"

    # Larger equilateral triangle
    assert module_0.triangle_area(10, 10, 10) == 43.3, "Expected 43.3 for sides (10, 10, 10)"

    # Invalid: violates triangle inequality (1 + 2 <= 3, degenerate)
    assert module_0.triangle_area(1, 2, 3) == -1, "Expected -1 for degenerate sides (1, 2, 3)"

    # Invalid: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1, "Expected -1 for sides (1, 2, 10)"

    # Invalid: zero-length sides
    assert module_0.triangle_area(0, 0, 0) == -1, "Expected -1 for zero sides"

    # Invalid: negative side length
    assert module_0.triangle_area(-3, 4, 5) == -1, "Expected -1 for negative side"

    # Invalid: all sides negative
    assert module_0.triangle_area(-1, -1, -1) == -1, "Expected -1 for all negative sides"

    # Permutation invariance for a valid triangle
    assert module_0.triangle_area(5, 3, 4) == module_0.triangle_area(3, 4, 5) == 6.0, \
        "Expected same area regardless of side order"

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 22:16:35.550799
# Unit test for function triangle_area
def test_triangle_area():
    # --- Valid triangles ---
    # Right triangle 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.00
    # Equilateral triangles
    assert module_0.triangle_area(3, 3, 3) == 3.90
    assert module_0.triangle_area(10, 10, 10) == 43.30
    # Isosceles triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98
    # Scalene triangles
    assert module_0.triangle_area(4, 8, 5) == 8.18
    assert module_0.triangle_area(7, 8, 9) == 26.83
    assert module_0.triangle_area(2, 3, 4) == 2.90
    # Floating point side lengths
    assert module_0.triangle_area(1.5, 2.5, 2.0) == 1.50
    # Result is rounded to 2 decimal places
    assert module_0.triangle_area(3, 4, 5) == round(6.0, 2)

    # --- Invalid triangles -> return -1 ---
    assert module_0.triangle_area(1, 2, 10) == -1      # a + b <= c
    assert module_0.triangle_area(1, 2, 3) == -1       # degenerate (a + b == c)
    assert module_0.triangle_area(2, 2, 5) == -1
    assert module_0.triangle_area(5, 1, 2) == -1       # b + c <= a
    assert module_0.triangle_area(1, 5, 2) == -1       # a + c <= b
    assert module_0.triangle_area(0, 0, 0) == -1       # zero-length sides
    assert module_0.triangle_area(1, 1, 0) == -1
    assert module_0.triangle_area(-1, 2, 2) == -1      # negative side length


if __name__ == "__main__":
    test_triangle_area()
    print("All tests passed!")

# Generated at 2026-11-02 22:18:36.447090
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0, "Right triangle 3-4-5 should have area 6.0"
    assert module_0.triangle_area(6, 8, 10) == 24.0, "Right triangle 6-8-10 should have area 24.0"
    assert module_0.triangle_area(1, 1, 1) == 0.43, "Equilateral triangle side 1 should have area 0.43"
    assert module_0.triangle_area(5, 5, 5) == 10.83, "Equilateral triangle side 5 should have area 10.83"
    assert module_0.triangle_area(7, 8, 9) == 26.83, "Scalene triangle 7-8-9 should have area 26.83"
    assert module_0.triangle_area(2, 2, 3) == 1.98, "Isosceles triangle 2-2-3 should have area 1.98"

    # Invalid triangles (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1, "1+2 <= 10, invalid triangle"
    assert module_0.triangle_area(10, 1, 1) == -1, "1+1 <= 10, invalid triangle"
    assert module_0.triangle_area(1, 10, 1) == -1, "1+1 <= 10, invalid triangle"

    # Degenerate triangle (collinear points)
    assert module_0.triangle_area(1, 1, 2) == -1, "1+1 == 2, degenerate triangle"

    # Zero and negative side lengths
    assert module_0.triangle_area(0, 0, 0) == -1, "Zero-length sides are invalid"
    assert module_0.triangle_area(-3, 4, 5) == -1, "Negative side is invalid"

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 22:19:42.945732
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0
    # Valid triangle with different order of sides
    assert module_0.triangle_area(5, 3, 4) == 6.0
    # Equilateral triangle: area = sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == 1.73
    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0
    # Scalene triangle
    assert module_0.triangle_area(4, 8, 5) == 8.18
    # Triangle with float sides
    assert module_0.triangle_area(1.5, 2.5, 2.0) == 1.5
    # Invalid triangle: sum of two sides less than the third
    assert module_0.triangle_area(1, 2, 10) == -1
    # Invalid triangle: degenerate (collinear) case, sum equals third side
    assert module_0.triangle_area(1, 1, 2) == -1
    assert module_0.triangle_area(10, 1, 2) == -1
    assert module_0.triangle_area(2, 10, 1) == -1
    # Invalid triangle: zero-length side
    assert module_0.triangle_area(0, 4, 5) == -1
    assert module_0.triangle_area(3, 0, 5) == -1
    assert module_0.triangle_area(3, 4, 0) == -1
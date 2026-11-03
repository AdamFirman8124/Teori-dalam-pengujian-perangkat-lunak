

# Generated at 2026-11-02 10:14:48.898243
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles (Heron's formula)
    assert module_0.triangle_area(3, 4, 5) == 6.0, "3-4-5 right triangle should have area 6.0"
    assert module_0.triangle_area(2, 2, 2) == 1.73, "Equilateral triangle with side 2 should have area 1.73"
    assert module_0.triangle_area(4, 8, 5) == 8.18, "Scalene triangle 4-8-5 should have area 8.18"
    assert module_0.triangle_area(10, 10, 10) == 43.30, "Equilateral triangle with side 10 should have area 43.30"
    assert module_0.triangle_area(1.5, 2.5, 2) == 1.5, "Triangle with float sides should have area 1.5"

    # Invalid triangles (triangle inequality fails) -> -1
    assert module_0.triangle_area(1, 2, 10) == -1, "1+2 <= 10, should return -1"
    assert module_0.triangle_area(1, 2, 3) == -1, "Degenerate triangle 1+2 == 3, should return -1"
    assert module_0.triangle_area(10, 1, 2) == -1, "1+2 <= 10, should return -1"
    assert module_0.triangle_area(2, 10, 2) == -1, "2+2 <= 10, should return -1"

    # Zero or negative side lengths -> -1
    assert module_0.triangle_area(0, 1, 1) == -1, "Zero-length side, should return -1"
    assert module_0.triangle_area(-3, 4, 5) == -1, "Negative side length, should return -1"
    assert module_0.triangle_area(0, 0, 0) == -1, "All sides zero, should return -1"

    print("All tests passed!")


test_triangle_area()

# Generated at 2026-11-02 10:15:35.308524
# Unit test for function triangle_area
def test_triangle_area():
    # Invalid triangles (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 1, 2) == -1
    assert module_0.triangle_area(2, 10, 1) == -1
    # Degenerate triangle (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 5, 10) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # Valid triangles (Heron's formula, rounded to 2 decimals)
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(1, 1, 1) == 0.43
    assert module_0.triangle_area(2, 2, 3) == 1.98
    assert module_0.triangle_area(4, 8, 5) == 8.18
    assert module_0.triangle_area(5, 12, 13) == 30.0

    # Floating point sides
    assert module_0.triangle_area(1.5, 2.5, 2.0) == 1.5
    assert module_0.triangle_area(2.5, 2.5, 2.5) == 2.71

    # Result should be positive for valid triangles
    assert module_0.triangle_area(7, 8, 9) > 0

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 10:16:16.479145
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Equilateral triangle
    assert module_0.triangle_area(1, 1, 1) == 0.43

    # Isosceles triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98

    # Scalene triangle
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Invalid triangle (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1

    # Zero-length side
    assert module_0.triangle_area(0, 4, 5) == -1

    # Negative side length
    assert module_0.triangle_area(-3, 4, 5) == -1

    # Larger valid triangle
    assert module_0.triangle_area(10, 15, 20) == 72.62

    # Reordered valid sides should give same result
    assert module_0.triangle_area(5, 3, 4) == 6.0
    assert module_0.triangle_area(4, 5, 3) == 6.0

    print("All tests passed!")


test_triangle_area()

# Generated at 2026-11-02 10:18:12.894189
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle (3-4-5) with different argument orderings
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(4, 5, 3) == 6.0
    assert module_0.triangle_area(5, 3, 4) == 6.0

    # Equilateral triangles
    assert module_0.triangle_area(1, 1, 1) == 0.43    # sqrt(3)/4 ≈ 0.4330
    assert module_0.triangle_area(2, 2, 2) == 1.73    # sqrt(3) ≈ 1.7321

    # Isosceles triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98    # sqrt(3.9375) ≈ 1.9843

    # Scalene triangle
    assert module_0.triangle_area(4, 6, 8) == 11.62   # sqrt(135) ≈ 11.6189

    # Larger right triangle (5-12-13)
    assert module_0.triangle_area(5, 12, 13) == 30.0

    # Floating-point sides
    assert module_0.triangle_area(1.5, 2.0, 2.0) == 1.39  # sqrt(1.93359375) ≈ 1.3905

    # Invalid triangles -> -1
    assert module_0.triangle_area(1, 2, 3) == -1      # degenerate: a + b == c
    assert module_0.triangle_area(3, 1, 2) == -1      # degenerate: b + c == a
    assert module_0.triangle_area(2, 3, 1) == -1      # degenerate: a + c == b
    assert module_0.triangle_area(1, 1, 3) == -1      # a + b < c
    assert module_0.triangle_area(10, 2, 3) == -1     # a > b + c
    assert module_0.triangle_area(1, 10, 3) == -1     # b > a + c

    # Zero-length sides -> -1
    assert module_0.triangle_area(0, 1, 1) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # Negative sides -> -1
    assert module_0.triangle_area(-1, 2, 2) == -1
    assert module_0.triangle_area(-3, -4, -5) == -1


if __name__ == "__main__":
    test_triangle_area()
    print("All tests passed!")

# Generated at 2026-11-02 10:19:34.499919
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles (Heron's formula, rounded to 2 decimals)
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(2, 2, 2) == 1.73       # equilateral, sqrt(3)
    assert module_0.triangle_area(4, 8, 5) == 8.18
    assert module_0.triangle_area(7, 10, 5) == 16.25
    assert module_0.triangle_area(1, 1, 1) == 0.43
    assert module_0.triangle_area(10, 10, 10) == 43.30

    # Invalid triangles (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 5, 3) == -1
    assert module_0.triangle_area(0, 0, 0) == -1
    assert module_0.triangle_area(-1, 2, 2) == -1

    # Degenerate triangles (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 5, 10) == -1

    # Non-integer side lengths
    assert module_0.triangle_area(2.5, 2.5, 3.5) == 3.09

    print("All tests passed!")

test_triangle_area()
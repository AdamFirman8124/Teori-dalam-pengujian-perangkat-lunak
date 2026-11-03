

# Generated at 2026-11-02 23:02:42.052854
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Equilateral triangle: side 1
    assert module_0.triangle_area(1, 1, 1) == 0.43

    # Isosceles triangle: 5-5-8
    assert module_0.triangle_area(5, 5, 8) == 12.0

    # Scalene triangle with rounding: 2-2-3
    assert module_0.triangle_area(2, 2, 3) == 1.98

    # Larger scalene triangle: 7-8-9
    assert module_0.triangle_area(7, 8, 9) == math.sqrt(12 * 5 * 4 * 3)  # ~26.83

    # Invalid triangle (one side too long): returns -1
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle (a + b == c): returns -1
    assert module_0.triangle_area(1, 2, 3) == -1

    # Degenerate triangle (a + c == b): returns -1
    assert module_0.triangle_area(5, 1, 4) == -1

    # Degenerate triangle (b + c == a): returns -1
    assert module_0.triangle_area(4, 5, 1) == -1

    # Zero-length side: returns -1
    assert module_0.triangle_area(0, 4, 5) == -1

    # Negative side lengths: returns -1
    assert module_0.triangle_area(-3, 4, 5) == -1

    # All sides negative: returns -1
    assert module_0.triangle_area(-1, -1, -1) == -1

    # Float inputs: valid triangle
    assert module_0.triangle_area(2.5, 2.5, 3.0) == 3.0

    # Float inputs: invalid triangle
    assert module_0.triangle_area(1.5, 1.5, 5.0) == -1

    # Very small valid triangle
    assert module_0.triangle_area(0.1, 0.1, 0.1) == 0.0  # rounds to 0.0

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 23:04:32.815714
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0          # classic right triangle
    assert module_0.triangle_area(5, 12, 13) == 30.0       # another right triangle
    assert module_0.triangle_area(4, 8, 5) == 8.18         # scalene triangle
    assert module_0.triangle_area(3, 3, 3) == 3.9          # equilateral triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98         # isosceles triangle
    assert module_0.triangle_area(2.5, 2.5, 2.5) == 2.71   # float sides

    # Invalid / degenerate triangles should return -1
    assert module_0.triangle_area(1, 2, 3) == -1           # degenerate (a + b == c)
    assert module_0.triangle_area(1, 1, 10) == -1          # c too large
    assert module_0.triangle_area(10, 1, 1) == -1          # a too large
    assert module_0.triangle_area(1, 10, 1) == -1          # b too large

# Generated at 2026-11-02 23:09:28.646284
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0
    # Valid equilateral triangles
    assert module_0.triangle_area(1, 1, 1) == 0.43
    assert module_0.triangle_area(2, 2, 2) == 1.73
    assert module_0.triangle_area(5, 5, 5) == 10.83
    # Valid scalene triangle
    assert module_0.triangle_area(4, 8, 5) == 8.18
    assert module_0.triangle_area(7, 10, 5) == 16.25
    # Invalid triangles (triangle inequality violated) return -1
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 1, 1) == -1
    assert module_0.triangle_area(1, 10, 1) == -1
    # Degenerate triangle (sum equals third side) returns -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 3, 2) == -1
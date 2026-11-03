

# Generated at 2026-11-02 11:59:20.188023
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Valid triangle with float sides
    assert module_0.triangle_area(3.0, 4.0, 5.0) == 6.0

    # Invalid triangle: sum of two sides less than third
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: sum of two sides equals third
    assert module_0.triangle_area(1, 2, 3) == -1

    # Equilateral triangle: side 2 -> sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == 1.73

    # Isosceles triangle: (5, 5, 8) -> area 12.0
    assert module_0.triangle_area(5, 5, 8) == 12.0

    # Scalene triangle: (4, 13, 15) -> area 24.0
    assert module_0.triangle_area(4, 13, 15) == 24.0

    # Zero-length sides are invalid
    assert module_0.triangle_area(0, 0, 0) == -1
    assert module_0.triangle_area(0, 4, 5) == -1

    # Negative sides are invalid (fail triangle inequality)
    assert module_0.triangle_area(-3, 4, 5) == -1

    # Rounding check: (7, 8, 9) -> s=12, area=sqrt(12*5*4*3)=sqrt(720)≈26.83
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Large valid triangle
    assert module_0.triangle_area(100, 100, 100) == 4330.13

    # Result should be a float for valid triangles
    assert isinstance(module_0.triangle_area(3, 4, 5), float)

    # Result should be int-like -1 for invalid triangles
    assert module_0.triangle_area(10, 1, 1) == -1

    print("All tests passed!")

if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 12:01:05.863014
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles - check Heron's formula results
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(1, 2, 10) == -1          # invalid: sum of two sides <= third
    assert module_0.triangle_area(4, 8, 5) == 8.18
    assert module_0.triangle_area(2, 2, 3) == 1.98

    # Degenerate (zero-area) triangle should return -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 5, 10) == -1
    assert module_0.triangle_area(1, 1, 2) == -1

    # Invalid cases with one side too long
    assert module_0.triangle_area(10, 2, 3) == -1
    assert module_0.triangle_area(2, 10, 3) == -1
    assert module_0.triangle_area(2, 3, 10) == -1

    # Equilateral triangle: side 2 -> area = sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == 1.73

    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0

    # Float inputs
    assert module_0.triangle_area(1.5, 2.5, 2.0) == 1.5

    # Zero or negative sides -> invalid
    assert module_0.triangle_area(0, 4, 5) == -1
    assert module_0.triangle_area(-3, 4, 5) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 12:04:09.685595
# Unit test for function triangle_area

# Generated at 2026-11-02 12:05:04.490944
# Unit test for function triangle_area
def test_triangle_area():assert module_0.triangle_area(3, 4, 5) == 6.0

# Generated at 2026-11-02 12:06:02.019791
# Unit test for function triangle_area

# Generated at 2026-11-02 12:06:28.631260
# Unit test for function triangle_area
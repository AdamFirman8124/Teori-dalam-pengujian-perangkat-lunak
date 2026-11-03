

# Generated at 2026-11-02 00:31:53.663235
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5 has area exactly 6
    assert module_0.triangle_area(3, 4, 5) == 6.00
    
    # Equilateral triangle with side 2: area = sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == 1.73
    
    # Isosceles triangle 5-5-6: s=8, area = sqrt(8*3*3*2) = 12
    assert module_0.triangle_area(5, 5, 6) == 12.00
    
    # Scalene triangle 4-8-5: s=8.5, area ≈ 8.18
    assert module_0.triangle_area(4, 8, 5) == 8.18
    
    # Triangle requiring rounding: 1-1-1, area = sqrt(3)/4 ≈ 0.43
    assert module_0.triangle_area(1, 1, 1) == 0.43
    
    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1
    
    # Degenerate triangle: sides sum exactly (collinear points)
    assert module_0.triangle_area(1, 2, 3) == -1
    
    # Degenerate triangle: another permutation
    assert module_0.triangle_area(3, 1, 2) == -1
    
    # Zero-length side is invalid
    assert module_0.triangle_area(0, 4, 5) == -1
    
    # Larger scalene triangle: 7-10-5, s=11, area = sqrt(11*4*1*6) = sqrt(264) ≈ 16.25
    assert module_0.triangle_area(7, 10, 5) == 16.25
    
    print("All tests passed!")

# Generated at 2026-11-02 00:32:20.796791
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangle: classic 3-4-5 right triangle
    assert module_0.triangle_area(3, 4, 5) == 6.00

    # Valid triangle: another Pythagorean triple
    assert module_0.triangle_area(5, 12, 13) == 30.00

    # Equilateral triangle with side 1
    assert module_0.triangle_area(1, 1, 1) == round(math.sqrt(3) / 4, 2)

    # Scalene triangle
    assert module_0.triangle_area(2, 3, 4) == 2.90

    # Isosceles triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98

    # Larger triangle
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Degenerate triangle (sum equals third side) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(10, 20, 30) == -1

    # Impossible triangle (one side too long) -> invalid
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(1, 1, 100) == -1

    # Negative side lengths -> invalid
    assert module_0.triangle_area(-3, 4, 5) == -1
    assert module_0.triangle_area(-1, -1, -1) == -1

    # Zero side length -> invalid
    assert module_0.triangle_area(0, 4, 5) == -1

# Generated at 2026-11-02 00:32:48.238873
# Unit test for function triangle_area
def test_triangle_area():
    # Valid scalene triangle (right triangle 3-4-5)
    assert module_0.triangle_area(3, 4, 5) == 6.00

    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1

    # Equilateral triangle
    assert module_0.triangle_area(3, 3, 3) == 3.9

    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.00

    # Degenerate triangle (points are collinear)
    assert module_0.triangle_area(1, 2, 3) == -1

    # Another invalid triangle
    assert module_0.triangle_area(1, 10, 2) == -1

    # Float-sided valid triangle
    assert module_0.triangle_area(2.0, 3.0, 4.0) == 2.9

    # Larger triangle
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Minimum valid triangle just above degeneracy
    assert module_0.triangle_area(1, 1, 1.999) == 0.04

    # Symmetry of inputs
    assert module_0.triangle_area(4, 3, 5) == module_0.triangle_area(5, 4, 3)

    print("All tests passed!")

# Generated at 2026-11-02 00:33:17.419862
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5 has area exactly 6.0
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Equilateral triangle with side 2: Heron's formula gives ~1.73
    assert module_0.triangle_area(2, 2, 2) == round(math.sqrt(3), 2)

    # Isosceles triangle 5-5-6 has area exactly 12.0
    assert module_0.triangle_area(5, 5, 6) == 12.0

    # Scalene triangle 7-10-5
    expected = round(math.sqrt(11 * 4 * 1 * 6), 2)  # s=11 -> sqrt(264) ~ 16.25
    assert module_0.triangle_area(7, 10, 5) == expected == 16.25

    # Larger triangle 10-15-20
    expected = round(math.sqrt(22.5 * 12.5 * 7.5 * 2.5), 2)  # ~72.62
    assert module_0.triangle_area(10, 15, 20) == expected == 72.62

    # Tiny equilateral triangle 1-1-1
    assert module_0.triangle_area(1, 1, 1) == 0.43

    # Triangle inequality violated: cannot form a triangle
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: points are collinear (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1

    # Zero-length side is invalid
    assert module_0.triangle_area(0, 4, 4) == -1

    # Negative side lengths are invalid
    assert module_0.triangle_area(-1, 2, 2) == -1

    # All sides zero
    assert module_0.triangle_area(0, 0, 0) == -1

    # Result must be rounded to at most 2 decimal places
    result = module_0.triangle_area(10, 15, 20)
    assert round(result, 2) == result


def test_triangle_area_returns_float_for_valid_input():
    assert isinstance(module_0.triangle_area(3, 4, 5), float)


def test_triangle_area_invalid_returns_minus_one():
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(100, 1, 1) == -1
    assert module_0.triangle_area(1, 100, 1) == -1

# Generated at 2026-11-02 00:33:52.549064
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles - verify Heron's formula results
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(6, 8, 10) == 24.0
    assert module_0.triangle_area(5, 5, 8) == 12.0
    assert module_0.triangle_area(1, 1, 1) == 0.43
    assert module_0.triangle_area(2, 3, 4) == 2.9
    assert module_0.triangle_area(7, 8, 9) == 26.83
    assert module_0.triangle_area(10, 10, 10) == 43.3

    # Invalid triangles - should return -1
    assert module_0.triangle_area(1, 2, 3) == -1      # degenerate (a + b == c)
    assert module_0.triangle_area(2, 2, 4) == -1      # degenerate (b + c == a)
    assert module_0.triangle_area(1, 1, 10) == -1     # impossible side lengths
    assert module_0.triangle_area(0, 1, 1) == -1      # zero-length side
    assert module_0.triangle_area(-1, 2, 2) == -1     # negative side length
    assert module_0.triangle_area(1, 10, 1) == -1     # two sides sum equals third

    # Floating point sides
    assert module_0.triangle_area(2.5, 2.5, 3.0) == 3.0
    assert module_0.triangle_area(0.5, 0.5, 0.5) == 0.11
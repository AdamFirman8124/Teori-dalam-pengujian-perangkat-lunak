

# Generated at 2026-11-02 13:03:47.801925
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle
    assert module_0.triangle_area(3, 4, 5) == 6.0
    # Equilateral triangle
    assert module_0.triangle_area(2, 2, 2) == 1.73
    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0
    # Scalene triangle with decimal result
    assert module_0.triangle_area(4, 8, 5) == 8.18
    # Degenerate triangle (sum of two sides equals third)
    assert module_0.triangle_area(1, 2, 3) == -1
    # Invalid triangle (sum of two sides less than third)
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 2, 3) == -1
    # Zero-length side
    assert module_0.triangle_area(0, 4, 5) == -1
    # Floating point sides
    assert module_0.triangle_area(3.5, 4.5, 5.5) == 7.85
    # Permutations of a valid triangle
    assert module_0.triangle_area(4, 5, 3) == module_0.triangle_area(5, 3, 4) == 6.0
    # Large triangle
    assert module_0.triangle_area(100, 100, 100) == 4330.13
    print("All tests passed!")

test_triangle_area()

# Generated at 2026-11-02 13:06:04.293815
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangle: classic 3-4-5 right triangle
    assert module_0.triangle_area(3, 4, 5) == 6.00
    
    # Valid triangle: equilateral
    assert module_0.triangle_area(2, 2, 2) == 1.73
    
    # Valid triangle: scalene
    assert module_0.triangle_area(4, 8, 5) == 8.18
    
    # Valid triangle with float inputs
    assert module_0.triangle_area(3.0, 4.0, 5.0) == 6.00
    
    # Invalid triangle: sum of two sides less than third
    assert module_0.triangle_area(1, 2, 10) == -1
    
    # Invalid triangle: degenerate (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(10, 20, 30) == -1
    
    # Invalid triangle: zero-length side
    assert module_0.triangle_area(0, 0, 0) == -1
    
    # Invalid triangle: negative side length
    assert module_0.triangle_area(-1, 2, 3) == -1
    
    # Valid isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.00

# Generated at 2026-11-02 13:09:05.000824
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(4, 3, 5) == 6.0
    assert module_0.triangle_area(5, 4, 3) == 6.0

    # Equilateral triangle
    assert module_0.triangle_area(2, 2, 2) == 1.73
    assert module_0.triangle_area(5, 5, 5) == 10.83

    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0

    # Scalene triangle
    assert module_0.triangle_area(4, 5, 6) == 9.92

    # Invalid triangles (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 1, 2) == -1
    assert module_0.triangle_area(1, 10, 2) == -1

    # Degenerate triangle (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 1, 2) == -1

    # Zero side length
    assert module_0.triangle_area(0, 4, 5) == -1

    print("All tests passed!")

test_triangle_area()

# Generated at 2026-11-02 13:10:29.817980
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5 has area 6.0
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Another valid right triangle: 5-12-13 has area 30.0
    assert module_0.triangle_area(5, 12, 13) == 30.0

    # Equilateral triangle with side 2: area = sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == round(math.sqrt(3), 2)

    # Equilateral triangle with side 1: area = sqrt(3)/4 ≈ 0.43
    assert module_0.triangle_area(1, 1, 1) == 0.43

    # Isosceles triangle: sides 5, 5, 6 -> s = 8, area = sqrt(8*3*3*2) = 12.0
    assert module_0.triangle_area(5, 5, 6) == 12.0

    # Isosceles triangle: sides 5, 5, 8 -> s = 9, area = sqrt(9*4*4*1) = 12.0
    assert module_0.triangle_area(5, 5, 8) == 12.0

    # Scalene triangle: sides 4, 5, 6 -> s = 7.5, area ≈ 9.92
    assert module_0.triangle_area(4, 5, 6) == 9.92

    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 2, 1) == -1
    assert module_0.triangle_area(2, 10, 1) == -1

    # Degenerate (zero-area) triangle: points are collinear
    assert module_0.triangle_area(1, 1, 2) == -1
    assert module_0.triangle_area(2, 1, 1) == -1
    assert module_0.triangle_area(1, 2, 1) == -1

    # Zero-length sides are invalid
    assert module_0.triangle_area(0, 0, 0) == -1
    assert module_0.triangle_area(0, 3, 4) == -1
    assert module_0.triangle_area(3, 0, 4) == -1
    assert module_0.triangle_area(3, 4, 0) == -1

    # Result should be rounded to 2 decimal places
    result = module_0.triangle_area(7, 8, 9)
    assert result == round(math.sqrt(12 * 5 * 4 * 3), 2)
    assert result == round(result, 2)

    # Floating point side lengths
    assert module_0.triangle_area(2.0, 2.0, 2.0) == round(math.sqrt(3), 2)

    # Symmetry: order of arguments should not matter
    assert module_0.triangle_area(3, 4, 5) == module_0.triangle_area(4, 5, 3)
    assert module_0.triangle_area(3, 4, 5) == module_0.triangle_area(5, 3, 4)
    assert module_0.triangle_area(1, 2, 10) == module_0.triangle_area(10, 1, 2)

# Generated at 2026-11-02 13:11:30.573652
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0

    # Valid right triangle: 5-12-13
    assert module_0.triangle_area(5, 12, 13) == 30.0

    # Equilateral triangle
    assert module_0.triangle_area(2, 2, 2) == 1.73

    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 8) == 12.0

    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: sum equals third side
    assert module_0.triangle_area(1, 2, 3) == -1

    # Degenerate triangle with zero-length side
    assert module_0.triangle_area(0, 4, 4) == -1

    # Scalene triangle with fractional sides
    assert module_0.triangle_area(4.5, 6.5, 8.0) == 14.51
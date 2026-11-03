

# Generated at 2026-11-03 00:07:57.616509
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangle: 3-4-5 right triangle
    assert module_0.triangle_area(3, 4, 5) == 6.00

    # Equilateral triangle with side 2: sqrt(3) ≈ 1.73
    assert module_0.triangle_area(2, 2, 2) == 1.73

    # Isosceles triangle: area exactly 12
    assert module_0.triangle_area(5, 5, 6) == 12.00

    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: sides sum equals third side
    assert module_0.triangle_area(1, 2, 3) == -1

    # Invalid triangle: another permutation
    assert module_0.triangle_area(10, 1, 1) == -1

    # Invalid triangle: zero-length sides
    assert module_0.triangle_area(0, 0, 0) == -1

    # Valid triangle with float inputs
    assert module_0.triangle_area(3.0, 4.0, 5.0) == 6.00

    # Scalene triangle: sides 7, 8, 9 -> s=12, sqrt(12*5*4*3)=sqrt(720)≈26.83
    assert module_0.triangle_area(7, 8, 9) == 26.83

    # Large valid triangle: sides 10, 10, 10 -> sqrt(15*5*5*5)≈64.95
    assert module_0.triangle_area(10, 10, 10) == 64.95

    # Invalid: negative side length treated via inequality check
    assert module_0.triangle_area(-1, 2, 3) == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-03 00:10:04.694973
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle
    assert module_0.triangle_area(3, 4, 5) == 6.0
    # Valid triangle with reordered sides
    assert module_0.triangle_area(5, 3, 4) == 6.0
    # Equilateral triangle
    assert module_0.triangle_area(3, 3, 3) == 3.9
    assert module_0.triangle_area(2, 2, 2) == 1.73
    # Isosceles triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0
    # Another valid scalene triangle
    assert module_0.triangle_area(10, 6, 8) == 24.0
    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1
    # Degenerate triangle: sum equals third side
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 1, 1) == -1
    # Zero-length side
    assert module_0.triangle_area(0, 4, 4) == -1

# Generated at 2026-11-03 00:12:29.185750
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0          # right triangle
    assert module_0.triangle_area(4, 8, 5) == 8.79         # scalene triangle
    assert module_0.triangle_area(2, 2, 2) == 1.73         # equilateral triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0         # isosceles triangle
    assert module_0.triangle_area(7, 8, 9) == 26.83        # scalene triangle
    assert module_0.triangle_area(1, 1, 1) == 0.43         # tiny equilateral

    # Invalid triangles (triangle inequality violated)
    assert module_0.triangle_area(1, 2, 10) == -1
    assert module_0.triangle_area(10, 2, 1) == -1
    assert module_0.triangle_area(2, 10, 1) == -1

    # Degenerate triangles (sum equals third side)
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(5, 5, 10) == -1

    # Zero / negative side lengths
    assert module_0.triangle_area(0, 4, 4) == -1
    assert module_0.triangle_area(-3, 4, 5) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # Floating point side lengths
    assert module_0.triangle_area(2.5, 2.5, 3.0) == 3.0
    assert module_0.triangle_area(1.5, 2.5, 3.5) == 1.85

    print("All tests passed!")

# Generated at 2026-11-03 00:14:56.130452
# Unit test for function triangle_area
def test_triangle_area():
    # Valid right triangle: 3-4-5
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 3, 4) == 6.0  # order of sides shouldn't matter

    # Equilateral triangle
    assert module_0.triangle_area(1, 1, 1) == 0.43
    assert module_0.triangle_area(2, 2, 2) == 1.73

    # Isosceles triangle
    assert module_0.triangle_area(2, 2, 3) == 1.98

    # Larger equilateral triangle
    assert module_0.triangle_area(10, 10, 10) == 43.3

    # Invalid triangle: one side too long
    assert module_0.triangle_area(1, 2, 10) == -1

    # Degenerate triangle: sum equals third side
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 1, 2) == -1

    # Invalid triangle with zero side
    assert module_0.triangle_area(0, 1, 1) == -1

    # Scalene triangle
    assert module_0.triangle_area(4, 5, 6) == 9.92

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()
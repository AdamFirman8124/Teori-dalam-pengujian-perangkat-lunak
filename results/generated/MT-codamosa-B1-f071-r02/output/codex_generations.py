

# Generated at 2026-10-25 08:56:22.998957
# Unit test for function triangle_area

# Generated at 2026-10-25 08:56:25.419917
# Unit test for function triangle_area

# Generated at 2026-10-25 08:56:27.840902
# Unit test for function triangle_area

# Generated at 2026-10-25 08:56:30.258137
# Unit test for function triangle_area

# Generated at 2026-10-25 08:56:40.889407
# Unit test for function triangle_area
def test_triangle_area():assert module_0.triangle_area(3, 4, 5) == 6.0

# Generated at 2026-10-25 08:56:53.992390
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0  # right triangle
    assert module_0.triangle_area(5, 5, 6) == 12.0  # isosceles
    assert module_0.triangle_area(2, 2, 2) == 1.73  # equilateral: sqrt(3) = 1.73
    assert module_0.triangle_area(2.5, 3.5, 4.0) == 4.33  # floats

    # Invalid / degenerate triangles -> -1
    assert module_0.triangle_area(1, 2, 3) == -1  # a + b <= c
    assert module_0.triangle_area(2, 2, 4) == -1  # degenerate
    assert module_0.triangle_area(1, 10, 12) == -1
    assert module_0.triangle_area(0, 5, 5) == -1  # zero side
    assert module_0.triangle_area(-1, 2, 2) == -1  # negative side

# Generated at 2026-10-25 08:57:00.743541
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(2, 2, 2) == 1.73          # sqrt(3), rounded
    assert module_0.triangle_area(5, 5, 6) == 12.0
    assert module_0.triangle_area(6, 8, 10) == 24.0

    # Invalid triangles
    assert module_0.triangle_area(1, 2, 3) == -1            # degenerate
    assert module_0.triangle_area(1, 1, 3) == -1
    assert module_0.triangle_area(10, 2, 2) == -1

    # Zero / non-positive sides are invalid by the triangle inequality
    assert module_0.triangle_area(0, 1, 1) == -1

# Generated at 2026-10-25 08:57:02.278732
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(2, 2, 2) == 1.73          # sqrt(3), rounded
    assert module_0.triangle_area(5, 5, 6) == 12.0
    assert module_0.triangle_area(6, 8, 10) == 24.0

    # Invalid triangles
    assert module_0.triangle_area(1, 2, 3) == -1            # degenerate
    assert module_0.triangle_area(1, 1, 3) == -1
    assert module_0.triangle_area(10, 2, 2) == -1

    # Zero / non-positive sides are invalid by the triangle inequality
    assert module_0.triangle_area(0, 1, 1) == -1


# Generated at 2026-10-25 10:47:03.216288
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

# Generated at 2026-10-25 10:47:04.700141
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

# Generated at 2026-10-25 10:47:06.176930
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

# Generated at 2026-10-25 10:47:07.607070
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

# Generated at 2026-10-25 10:47:09.167736
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
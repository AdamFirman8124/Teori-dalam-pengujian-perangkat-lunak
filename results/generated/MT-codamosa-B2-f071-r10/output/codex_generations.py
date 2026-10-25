

# Generated at 2026-10-24 07:44:05.355236
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 5, 5) == round((25 * 3 ** 0.5 / 4), 2)  # equilateral â 10.83
    assert module_0.triangle_area(1, 1, 1.41421356) == 0.7  # near-right isosceles

    # Degenerate triangles (zero area) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1   # points are collinear
    assert module_0.triangle_area(0, 0, 0) == -1   # zero sides
    assert module_0.triangle_area(0, 4, 5) == -1   # zero side

    # Impossible triangles
    assert module_0.triangle_area(1, 1, 10) == -1  # one side too long
    assert module_0.triangle_area(-3, 4, 5) == -1  # negative length

    print("All tests passed.")

test_triangle_area()

# Generated at 2026-10-24 07:44:06.684374
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 5, 5) == round((25 * 3 ** 0.5 / 4), 2)  # equilateral â 10.83
    assert module_0.triangle_area(1, 1, 1.41421356) == 0.7  # near-right isosceles

    # Degenerate triangles (zero area) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1   # points are collinear
    assert module_0.triangle_area(0, 0, 0) == -1   # zero sides
    assert module_0.triangle_area(0, 4, 5) == -1   # zero side

    # Impossible triangles
    assert module_0.triangle_area(1, 1, 10) == -1  # one side too long
    assert module_0.triangle_area(-3, 4, 5) == -1  # negative length

    print("All tests passed.")

test_triangle_area()

# Generated at 2026-10-24 07:44:07.990554
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 5, 5) == round((25 * 3 ** 0.5 / 4), 2)  # equilateral â 10.83
    assert module_0.triangle_area(1, 1, 1.41421356) == 0.7  # near-right isosceles

    # Degenerate triangles (zero area) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1   # points are collinear
    assert module_0.triangle_area(0, 0, 0) == -1   # zero sides
    assert module_0.triangle_area(0, 4, 5) == -1   # zero side

    # Impossible triangles
    assert module_0.triangle_area(1, 1, 10) == -1  # one side too long
    assert module_0.triangle_area(-3, 4, 5) == -1  # negative length

    print("All tests passed.")

test_triangle_area()

# Generated at 2026-10-24 07:44:09.314504
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 5, 5) == round((25 * 3 ** 0.5 / 4), 2)  # equilateral â 10.83
    assert module_0.triangle_area(1, 1, 1.41421356) == 0.7  # near-right isosceles

    # Degenerate triangles (zero area) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1   # points are collinear
    assert module_0.triangle_area(0, 0, 0) == -1   # zero sides
    assert module_0.triangle_area(0, 4, 5) == -1   # zero side

    # Impossible triangles
    assert module_0.triangle_area(1, 1, 10) == -1  # one side too long
    assert module_0.triangle_area(-3, 4, 5) == -1  # negative length

    print("All tests passed.")

test_triangle_area()

# Generated at 2026-10-24 07:44:10.633926
# Unit test for function triangle_area
def test_triangle_area():
    # Valid triangles
    assert module_0.triangle_area(3, 4, 5) == 6.0
    assert module_0.triangle_area(5, 5, 5) == round((25 * 3 ** 0.5 / 4), 2)  # equilateral â 10.83
    assert module_0.triangle_area(1, 1, 1.41421356) == 0.7  # near-right isosceles

    # Degenerate triangles (zero area) -> invalid
    assert module_0.triangle_area(1, 2, 3) == -1   # points are collinear
    assert module_0.triangle_area(0, 0, 0) == -1   # zero sides
    assert module_0.triangle_area(0, 4, 5) == -1   # zero side

    # Impossible triangles
    assert module_0.triangle_area(1, 1, 10) == -1  # one side too long
    assert module_0.triangle_area(-3, 4, 5) == -1  # negative length

    print("All tests passed.")

test_triangle_area()


# Generated at 2026-10-24 22:54:39.511398
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right triangles
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(6, 7, 8) is False

# Generated at 2026-10-24 22:54:51.926776
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 3, 4) is True
    assert module_0.right_angle_triangle(8, 15, 17) is True

    # Valid non-right-angled triangles
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(3, 4, 6) is False
    assert module_0.right_angle_triangle(1, 2, 2) is False

    # Values that do not form a right-angled triangle
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:55:05.008725
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 3, 4) is True
    assert module_0.right_angle_triangle(4, 5, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right triangle
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(6, 7, 8) is False

# Generated at 2026-10-24 22:55:18.320499
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # A valid right triangle, in different side orders
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(3, 4, 4) is False

# Generated at 2026-10-24 22:55:29.891785
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # The order of the sides should not matter
    assert module_0.right_angle_triangle(5, 3, 4) is True
    assert module_0.right_angle_triangle(4, 5, 3) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False
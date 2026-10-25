

# Generated at 2026-10-24 22:32:59.185858
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:33:01.603992
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:33:04.021456
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:33:17.152669
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:33:29.952484
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True
    assert module_0.right_angle_triangle(8, 15, 17) is True

    # The order of the sides should not matter
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 3) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

# Generated at 2026-10-24 22:33:45.619577
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(1, 1, 1) is False
    assert module_0.right_angle_triangle(2, 2, 3) is False

    # Invalid side lengths
    assert module_0.right_angle_triangle(0, 3, 3) is False
    assert module_0.right_angle_triangle(-3, 4, 5) is False

# Generated at 2026-10-24 22:34:00.159528
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # A standard right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # The order of the sides should not matter
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 3) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False
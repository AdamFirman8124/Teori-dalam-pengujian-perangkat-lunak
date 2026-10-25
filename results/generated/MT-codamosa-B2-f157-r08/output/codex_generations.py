

# Generated at 2026-10-25 02:13:27.180649
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Classic right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # The hypotenuse can be in any argument position
    assert module_0.right_angle_triangle(5, 3, 4) is True
    assert module_0.right_angle_triangle(4, 5, 3) is True

    # Not a right-angled triangle
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(4, 4, 5) is False

# Generated at 2026-10-25 02:13:29.605245
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:32.022981
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:34.444838
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:36.860390
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:39.278363
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:41.688420
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:44.104300
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:46.517234
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 02:13:51.063571
# Unit test for function right_angle_triangle
def test_right_angle_triangle():assert module_0.right_angle_triangle(3, 4, 5) is True

# Generated at 2026-10-25 02:14:06.734528
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Valid triangles that are not right-angled
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(4, 5, 6) is False

    # Invalid or degenerate triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(0, 3, 3) is False
    assert module_0.right_angle_triangle(-3, 4, 5) is False
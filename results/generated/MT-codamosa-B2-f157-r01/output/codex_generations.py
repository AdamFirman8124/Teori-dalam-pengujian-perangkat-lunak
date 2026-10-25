

# Generated at 2026-10-24 22:38:50.671926
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True  # Different order

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

# Generated at 2026-10-24 22:39:01.439123
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Standard Pythagorean triple
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # Order of the sides should not matter
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Not a right-angled triangle
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False

    # Another valid right-angled triangle
    assert module_0.right_angle_triangle(5, 12, 13) is True

# Generated at 2026-10-24 22:39:13.814063
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

# Generated at 2026-10-24 22:39:25.695068
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right triangles
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(4, 4, 4) is False
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:39:40.333621
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # A standard right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # The order of the sides should not matter
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Other right-angled triangles
    assert module_0.right_angle_triangle(5, 12, 13) is True
    assert module_0.right_angle_triangle(8, 15, 17) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

    # The example given
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:39:54.055007
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(1, 1, 1) is False

    assert module_0.right_angle_triangle(0, 3, 3) is False
    assert module_0.right_angle_triangle(-3, 4, 5) is False

# Generated at 2026-10-24 22:40:07.060258
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:40:09.601815
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:40:12.134028
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:40:14.664593
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:40:28.666098
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True
    assert module_0.right_angle_triangle(8, 15, 17) is True
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(4, 5, 6) is False

# Generated at 2026-10-24 22:40:39.213256
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True
    assert module_0.right_angle_triangle(4, 5, 3) is True

    # Valid triangles that are not right-angled
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False

    # Degenerate triangle
    assert module_0.right_angle_triangle(1, 2, 3) is False

# Generated at 2026-10-24 22:40:53.857391
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Valid right-angled triangles
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 12, 13) is True

    # Non-right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 3, 4) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

# Generated at 2026-10-24 22:41:07.782575
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # A valid right-angled triangle
    assert module_0.right_angle_triangle(3, 4, 5) is True

    # The order of the sides should not matter
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    # Non-right triangles
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 3) is False
    assert module_0.right_angle_triangle(5, 5, 5) is False

# Generated at 2026-10-24 22:41:10.201671
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:41:12.622535
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:41:15.251685
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:41:17.667927
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 22:41:22.632908
# Unit test for function right_angle_triangle
def test_right_angle_triangle():assert module_0.right_angle_triangle(3, 4, 5) is True

# Generated at 2026-10-24 22:41:36.968403
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(4, 3, 5) is True
    assert module_0.right_angle_triangle(5, 4, 3) is True

    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(2, 2, 2) is False
    assert module_0.right_angle_triangle(3, 3, 4) is False

    # Invalid side lengths
    assert module_0.right_angle_triangle(0, 3, 4) is False
    assert module_0.right_angle_triangle(-3, 4, 5) is False
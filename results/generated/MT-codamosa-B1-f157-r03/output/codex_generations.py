

# Generated at 2026-10-24 19:23:23.027095
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:25.443442
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:27.862776
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:30.279438
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:32.856565
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:35.272020
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:37.689717
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:40.106581
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:42.522064
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:44.939358
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:47.356872
# Unit test for function right_angle_triangle

# Generated at 2026-10-24 19:23:52.545379
# Unit test for function right_angle_triangle
def test_right_angle_triangle():assert module_0.right_angle_triangle(3, 4, 5) is True

# Generated at 2026-10-24 19:24:09.762222
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    # Right-angled triangles - all permutations
    assert module_0.right_angle_triangle(3, 4, 5) == True
    assert module_0.right_angle_triangle(5, 3, 4) == True
    assert module_0.right_angle_triangle(4, 5, 3) == True
    assert module_0.right_angle_triangle(6, 8, 10) == True
    assert module_0.right_angle_triangle(5, 12, 13) == True
    assert module_0.right_angle_triangle(8, 15, 17) == True

    # Not right-angled triangles
    assert module_0.right_angle_triangle(1, 2, 3) == False
    assert module_0.right_angle_triangle(2, 3, 4) == False
    assert module_0.right_angle_triangle(4, 5, 6) == False
    assert module_0.right_angle_triangle(3, 3, 3) == False
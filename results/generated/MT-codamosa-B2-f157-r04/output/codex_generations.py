

# Generated at 2026-10-25 11:47:47.655024
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:47:50.861455
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:47:53.488716
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:47:55.902354
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:47:58.349780
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:00.731025
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:03.330972
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:05.745427
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:08.158355
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:10.574061
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:12.987768
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:15.401535
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:17.818010
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:20.231797
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:22.651269
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:25.064181
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:27.479103
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:29.894265
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:32.308805
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:34.722440
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:37.136290
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:48:44.971494
# Unit test for function right_angle_triangle
def test_right_angle_triangle():
    assert module_0.right_angle_triangle(3, 4, 5) is True
    assert module_0.right_angle_triangle(5, 3, 4) is True
    assert module_0.right_angle_triangle(4, 5, 3) is True
    assert module_0.right_angle_triangle(6, 8, 10) is True
    assert module_0.right_angle_triangle(1, 2, 3) is False
    assert module_0.right_angle_triangle(3, 4, 6) is False
    assert module_0.right_angle_triangle(2, 2, 2) is False
    print("All tests passed")


if __name__ == "__main__":
    test_right_angle_triangle()

# Generated at 2026-10-25 11:48:49.714657
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

# Generated at 2026-10-25 11:48:51.250288
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

# Generated at 2026-10-25 11:48:52.785555
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

# Generated at 2026-10-25 11:48:54.218225
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

# Generated at 2026-10-25 11:48:56.190016
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

# Generated at 2026-10-25 11:48:57.701356
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

# Generated at 2026-10-25 11:49:01.404481
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:49:03.818503
# Unit test for function right_angle_triangle

# Generated at 2026-10-25 11:49:06.232970
# Unit test for function right_angle_triangle
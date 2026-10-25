

# Generated at 2026-10-24 14:25:19.095841
# Unit test for function sum_squares

# Generated at 2026-10-24 14:25:21.510924
# Unit test for function sum_squares

# Generated at 2026-10-24 14:25:23.925719
# Unit test for function sum_squares

# Generated at 2026-10-24 14:25:26.342878
# Unit test for function sum_squares

# Generated at 2026-10-24 14:25:28.756359
# Unit test for function sum_squares

# Generated at 2026-10-24 14:25:35.812919
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:25:44.810195
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.0, -1.2]) == 9
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:25:46.141241
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14      # exact ints: 1+4+9
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29      # ceil -> 2,3,4 -> 4+9+16
    assert module_0.sum_squares([-1.5, -2.5]) == 5          # ceil -> -1,-2 -> 1+4
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([]) == 0                    # empty list
    assert module_0.sum_squares([0.1]) == 1                 # ceil(0.1) == 1

# Generated at 2026-10-24 14:25:52.594268
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.8, -2.1]) == 5      # (-1)Â² + (-2)Â²
    assert module_0.sum_squares([0, 2.01, -3.9]) == 18  # 0Â² + 3Â² + (-3)Â²
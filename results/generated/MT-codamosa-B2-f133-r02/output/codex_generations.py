

# Generated at 2026-10-24 21:33:23.918677
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.5, 2.1]) == 10      # (-1)Â² + 3Â²
    assert module_0.sum_squares([0, 4.0]) == 16

# Generated at 2026-10-24 21:33:28.833670
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.5, -2.1]) == 5      # (-1)Â² + (-2)Â²
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 21:33:33.954616
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.5, 3.1]) == 29
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 21:33:38.768145
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.5, -2.1]) == 5      # (-1)Â² + (-2)Â²
    assert module_0.sum_squares([0, 2.7, -3.2]) == 25   # 0Â² + 3Â² + (-3)Â²

# Generated at 2026-10-24 21:33:43.887155
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.8]) == 13
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([1.2, -2.8, 0]) == 8
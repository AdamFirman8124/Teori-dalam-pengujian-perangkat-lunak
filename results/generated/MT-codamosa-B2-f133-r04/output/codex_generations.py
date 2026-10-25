

# Generated at 2026-10-24 20:31:02.829414
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.5, 3.1]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.2, -2.8]) == 5      # (-1)Â² + (-2)Â²
    assert module_0.sum_squares([0, 4.0]) == 16

# Generated at 2026-10-24 20:31:08.850665
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.5, 3.1]) == 29
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 20:31:15.005714
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.1, 2.2, 3.3]) == 29
    assert module_0.sum_squares([-1.2, -2.8, 0]) == 5
    assert module_0.sum_squares([4.0]) == 16

# Generated at 2026-10-24 20:31:20.725006
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.3]) == 13
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([0, 1.2, -1.2, 2]) == 9

# Generated at 2026-10-24 20:31:27.396268
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([]) == 0
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.5, 3.7]) == 29
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([0, 0.1, -0.1]) == 1
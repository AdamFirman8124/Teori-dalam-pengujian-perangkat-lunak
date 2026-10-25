

# Generated at 2026-10-24 14:09:45.585831
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.7, 3.0]) == 29  # 4 + 9 + 16
    assert module_0.sum_squares([-1.2, 2.1]) == 5        # 1 + 4
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:09:46.976775
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14      # exact ints: 1+4+9
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29      # ceil -> 2,3,4 -> 4+9+16
    assert module_0.sum_squares([-1.5, -2.5]) == 5          # ceil -> -1,-2 -> 1+4
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([]) == 0                    # empty list
    assert module_0.sum_squares([0.1]) == 1                 # ceil(0.1) == 1

# Generated at 2026-10-24 14:09:56.069307
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.1, 2.9, -1.2]) == 14
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:10:05.490346
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.8, 3.0]) == 22
    assert module_0.sum_squares([-1.2, -2.8]) == 5
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 14:10:14.167116
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.8, -1.1]) == 14
    assert module_0.sum_squares([]) == 0
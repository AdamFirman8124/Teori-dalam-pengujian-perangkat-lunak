

# Generated at 2026-10-24 12:18:55.933987
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.1, 3.9]) == 29  # 2Â² + 3Â² + 4Â²
    assert module_0.sum_squares([-1.2, 0, 2.5]) == 10   # (-1)Â² + 0Â² + 3Â²
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 12:19:04.111748
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.1, 2.0, -1.2]) == 9
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 12:19:14.584105
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1.2, 2.9, -1.2]) == 14
    assert module_0.sum_squares([]) == 0

# Generated at 2026-10-24 12:19:27.279793
# Unit test for function sum_squares
def test_sum_squares():
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14      # exact ints: 1+4+9
    assert module_0.sum_squares([1.2, 2.3, 3.4]) == 29      # ceil -> 2,3,4 -> 4+9+16
    assert module_0.sum_squares([-1.5, -2.5]) == 5          # ceil -> -1,-2 -> 1+4
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([]) == 0                    # empty list
    assert module_0.sum_squares([0.1]) == 1                 # ceil(0.1) == 1

# Generated at 2026-10-24 12:19:29.703491
# Unit test for function sum_squares

# Generated at 2026-10-24 12:19:32.125017
# Unit test for function sum_squares

# Generated at 2026-10-24 12:19:34.744979
# Unit test for function sum_squares
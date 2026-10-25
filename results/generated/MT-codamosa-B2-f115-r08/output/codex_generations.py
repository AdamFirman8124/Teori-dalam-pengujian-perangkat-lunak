

# Generated at 2026-10-25 04:19:45.197657
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:47.803234
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:50.217372
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:52.632073
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:55.047542
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:57.463006
# Unit test for function max_fill

# Generated at 2026-10-25 04:19:59.877954
# Unit test for function max_fill

# Generated at 2026-10-25 04:20:02.293274
# Unit test for function max_fill

# Generated at 2026-10-25 04:20:07.280908
# Unit test for function max_fill
def test_max_fill():grid = [[1, 2], [3, 4]]

# Generated at 2026-10-25 04:20:13.882718
# Unit test for function max_fill
def test_max_fill():
    assert module_0.max_fill([[2, 4, 3], [5, 0, 0], [2, 1, 0]], 3) == 6
    assert module_0.max_fill([[3, 3], [6]], 3) == 4       # Exact multiples
    assert module_0.max_fill([[1], [1], [1]], 2) == 3     # Partial capacity per row
    assert module_0.max_fill([[0, 0], [0]], 5) == 0       # Empty loads
    assert module_0.max_fill([], 5) == 0                  # Empty grid

# Generated at 2026-10-25 04:20:20.517974
# Unit test for function max_fill
def test_max_fill():
    assert module_0.max_fill([[2, 4, 2], [4, 4, 5], [6]], 3) == 10
    assert module_0.max_fill([[3, 3], [6]], 3) == 4
    assert module_0.max_fill([[1], [1], [1]], 2) == 3
    assert module_0.max_fill([], 5) == 0
    assert module_0.max_fill([[]], 5) == 0
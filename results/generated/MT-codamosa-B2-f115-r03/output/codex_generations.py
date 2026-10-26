

# Generated at 2026-10-25 12:00:22.874440
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:25.287195
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:27.702023
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:30.117541
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:32.532302
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:34.951846
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:37.364935
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:39.779892
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:42.193051
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:44.609867
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:47.022463
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:49.436842
# Unit test for function max_fill

# Generated at 2026-10-25 12:00:50.922029
# Unit test for function max_fill
def test_max_fill():
    # one dip per well when capacity=1
    assert module_0.max_fill([[0, 0, 1], [0, 1, 0], [0, 1, 0]], 1) == 3
    # capacity 2, each row has 1 unit -> 1 dip each
    assert module_0.max_fill([[0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]], 2) == 3
    # mixed row sums: 2,0,1,1 with capacity 2 -> 1+0+1+1
    assert module_0.max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 2) == 3
    # empty grid
    assert module_0.max_fill([], 1) == 0
    # all-zero well
    assert module_0.max_fill([[0, 0, 0]], 5) == 0
    # needs two dips
    assert module_0.max_fill([[1, 1, 1]], 2) == 2
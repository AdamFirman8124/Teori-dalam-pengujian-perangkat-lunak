

# Generated at 2026-10-24 12:07:00.230163
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:02.648415
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:05.071065
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:07.489090
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:09.910620
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:21.876281
# Unit test for function max_fill
def test_max_fill():
    # Each row needs ceil(total_in_row / capacity) trips
    assert module_0.max_fill([[0, 0, 0], [0, 0, 0]], 1) == 0
    assert module_0.max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 4) == 2
    assert module_0.max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 3) == 4
    assert module_0.max_fill([[1, 1, 1], [0, 0, 0], [1, 1]], 2) == 3
    assert module_0.max_fill([[0]], 5) == 0
    assert module_0.max_fill([[1]], 1) == 1
    assert module_0.max_fill([[1, 0, 1, 0, 1]], 2) == 2

# Generated at 2026-10-24 12:07:38.374994
# Unit test for function max_fill
def test_max_fill():
    assert module_0.max_fill([[0,0,1,0],[0,1,0,0],[1,1,1,1]], 1) == 6
    assert module_0.max_fill([[0,0,1,0],[0,1,0,0],[1,1,1,1]], 2) == 4
    assert module_0.max_fill([[0,0,1,0],[0,1,0,0],[1,1,1,1]], 3) == 4
    assert module_0.max_fill([[0,0,1,0],[0,1,0,0],[1,1,1,1]], 4) == 3
    assert module_0.max_fill([[0,0,0],[0,0,0]], 1) == 0
    assert module_0.max_fill([], 5) == 0
    assert module_0.max_fill([[]], 1) == 0
    assert module_0.max_fill([[1,1,1],[1,1,1]], 2) == 4
    assert module_0.max_fill([[1]], 1) == 1
    assert module_0.max_fill([[1,0,1]], 5) == 1

# Generated at 2026-10-24 12:07:40.878115
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:43.298236
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:45.714846
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:48.132091
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:50.547522
# Unit test for function max_fill

# Generated at 2026-10-24 12:07:52.969282
# Unit test for function max_fill
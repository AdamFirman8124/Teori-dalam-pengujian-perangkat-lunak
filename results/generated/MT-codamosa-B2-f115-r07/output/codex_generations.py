

# Generated at 2026-10-25 07:53:23.354235
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

# Generated at 2026-10-25 07:53:24.697347
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

# Generated at 2026-10-25 07:53:26.118921
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

# Generated at 2026-10-25 07:53:27.551887
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

# Generated at 2026-10-25 07:53:28.985457
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
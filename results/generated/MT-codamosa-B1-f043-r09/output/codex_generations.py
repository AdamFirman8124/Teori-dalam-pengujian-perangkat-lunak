

# Generated at 2026-10-25 12:19:18.694659
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    assert module_0.pairs_sum_to_zero([1, -1]) is True
    assert module_0.pairs_sum_to_zero([3, 4, -2]) is False
    assert module_0.pairs_sum_to_zero([0, 0]) is True
    assert module_0.pairs_sum_to_zero([1, 2, 3]) is False
    assert module_0.pairs_sum_to_zero([]) is False

# Generated at 2026-10-25 12:19:49.618366
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    assert module_0.pairs_sum_to_zero([1, -1]) is True
    assert module_0.pairs_sum_to_zero([3, 4, -2]) is False
    assert module_0.pairs_sum_to_zero([0, 0]) is True
    assert module_0.pairs_sum_to_zero([-5, 2, 5]) is True
    assert module_0.pairs_sum_to_zero([]) is False
    assert module_0.pairs_sum_to_zero([7]) is False

# Generated at 2026-10-25 12:20:19.928912
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # empty and single-element -> no pair possible
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([0]) == False

    # basic pairs
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([-1, 1]) == True
    assert module_0.pairs_sum_to_zero([1.5, -1.5]) == True
    assert module_0.pairs_sum_to_zero([1, 2, 3]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4]) == False

    # pair not at start
    assert module_0.pairs_sum_to_zero([1, 2, 3, -2]) == True
    assert module_0.pairs_sum_to_zero([5, 1, 2, -5]) == True

    # zero handling: needs two distinct zeros
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0, 1]) == False
    assert module_0.pairs_sum_to_zero([0, 1, 2]) == False
    assert module_0.pairs_sum_to_zero([0, 0, 1]) == True

    # same value without opposite does not count
    assert module_0.pairs_sum_to_zero([2, 2]) == False
    assert module_0.pairs_sum_to_zero([-3, -3, 3, 3]) == True

    # must be exactly two elements summing to zero
    assert module_0.pairs_sum_to_zero([2, 3, -5]) == False
    assert module_0.pairs_sum_to_zero([1, 2, -3]) == False

# Generated at 2026-10-25 12:20:51.052629
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    assert module_0.pairs_sum_to_zero([1, -1]) is True
    assert module_0.pairs_sum_to_zero([3, 5, -2]) is False
    assert module_0.pairs_sum_to_zero([0, 0]) is True
    assert module_0.pairs_sum_to_zero([1, 2, 3, -3]) is True
    assert module_0.pairs_sum_to_zero([]) is False
    assert module_0.pairs_sum_to_zero([0]) is False
    assert module_0.pairs_sum_to_zero([-4, -2, 1, 3]) is False

# Generated at 2026-10-25 12:21:17.786526
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    assert module_0.pairs_sum_to_zero([1, -1]) is True
    assert module_0.pairs_sum_to_zero([1, 2, 3]) is False
    assert module_0.pairs_sum_to_zero([-5, 0, 5]) is True
    assert module_0.pairs_sum_to_zero([0, 0]) is True
    assert module_0.pairs_sum_to_zero([1]) is False
    assert module_0.pairs_sum_to_zero([]) is False
    assert module_0.pairs_sum_to_zero([-2, 4, 6, 8]) is False
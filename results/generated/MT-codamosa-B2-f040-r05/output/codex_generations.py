

# Generated at 2026-11-03 02:21:49.331534
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Basic positive case: triple summing to zero exists
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([1, 2]) == False
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([0, 0, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True
    assert module_0.triples_sum_to_zero([-5, 2, 3]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True
    assert module_0.triples_sum_to_zero([10, 20, 30, 40, 50]) == False
    assert module_0.triples_sum_to_zero([1, -1, 2, -2, 3]) == True
    assert module_0.triples_sum_to_zero([100, -50, -50]) == True
    assert module_0.triples_sum_to_zero([5, -5, 1, 0, -1]) == True

# Generated at 2026-11-03 02:25:05.024671
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Triples that sum to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([0, 0, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True
    assert module_0.triples_sum_to_zero([5, -5, 10, -10, 3]) == False
    assert module_0.triples_sum_to_zero([5, -5, 10, -10, 3, 0]) == True
    assert module_0.triples_sum_to_zero([1, 1, 1]) == False
    assert module_0.triples_sum_to_zero([-3, 1, 2]) == True
    assert module_0.triples_sum_to_zero([100, -50, -50]) == True

# Generated at 2026-11-03 02:27:14.085178
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():# No triple sums to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == False

    # Triple sums to zero
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, -1, 0]) == True
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([5, -5, 10, -10]) == True
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True

    # Duplicate values at distinct indices still count
    assert module_0.triples_sum_to_zero([1, 1, -2]) == True
    assert module_0.triples_sum_to_zero([2, 2, -4, 3]) == True

    # Too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # All same sign
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([-1, -2, -3]) == False

    # Large mixed list without a zero-sum triple
    assert module_0.triples_sum_to_zero([10, 20, 30, 40, 50]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_triples_sum_to_zero()

# Generated at 2026-11-03 02:29:00.451274
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # Triple exists
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True   # 1 + (-2) + 1 = 0
    assert module_0.triples_sum_to_zero([1, 2, -3, 4]) == True   # 1 + 2 + (-3) = 0
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True       # 0 + 0 + 0 = 0
    assert module_0.triples_sum_to_zero([1, -1, 0]) == True      # 1 + (-1) + 0 = 0
    assert module_0.triples_sum_to_zero([-1, -2, 3]) == True     # -1 + (-2) + 3 = 0
    assert module_0.triples_sum_to_zero([3, -1, -2]) == True     # unsorted input
    assert module_0.triples_sum_to_zero([2, 2, -4]) == True      # duplicate values, distinct indices

    # No triple sums to zero
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([1, 1, 1]) == False
    assert module_0.triples_sum_to_zero([5, 5, 5]) == False
    assert module_0.triples_sum_to_zero([0, 0, 1]) == False

    # Fewer than three elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([1]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # Larger lists
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True   # 2 + (-5) + 3 = 0
    assert module_0.triples_sum_to_zero([10, 20, 30, 40, 50]) == False
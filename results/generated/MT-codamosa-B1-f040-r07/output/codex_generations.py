

# Generated at 2026-10-25 12:28:36.982742
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases from spec
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # edge cases: too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0]) == False
    assert module_0.triples_sum_to_zero([0, 0]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # exactly three elements
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True

    # pair sums to zero is not enough
    assert module_0.triples_sum_to_zero([1, -1, 5]) == False

    # triple later in list
    assert module_0.triples_sum_to_zero([5, 1, 2, -3, 7]) == True
    assert module_0.triples_sum_to_zero([-5, -1, -2, 8, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3, 5]) == True

# Generated at 2026-10-25 12:28:38.860804
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases from spec
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # edge cases: too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0]) == False
    assert module_0.triples_sum_to_zero([0, 0]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # exactly three elements
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True

    # pair sums to zero is not enough
    assert module_0.triples_sum_to_zero([1, -1, 5]) == False

    # triple later in list
    assert module_0.triples_sum_to_zero([5, 1, 2, -3, 7]) == True
    assert module_0.triples_sum_to_zero([-5, -1, -2, 8, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3, 5]) == True

# Generated at 2026-10-25 12:28:42.318917
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases from spec
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # edge cases: too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0]) == False
    assert module_0.triples_sum_to_zero([0, 0]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # exactly three elements
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True

    # pair sums to zero is not enough
    assert module_0.triples_sum_to_zero([1, -1, 5]) == False

    # triple later in list
    assert module_0.triples_sum_to_zero([5, 1, 2, -3, 7]) == True
    assert module_0.triples_sum_to_zero([-5, -1, -2, 8, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3, 5]) == True

# Generated at 2026-10-25 12:29:29.207472
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases from spec
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # edge cases: too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0]) == False
    assert module_0.triples_sum_to_zero([0, 0]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # exactly three elements
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True

    # pair sums to zero is not enough
    assert module_0.triples_sum_to_zero([1, -1, 5]) == False

    # triple later in list
    assert module_0.triples_sum_to_zero([5, 1, 2, -3, 7]) == True
    assert module_0.triples_sum_to_zero([-5, -1, -2, 8, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3, 5]) == True

# Generated at 2026-10-25 12:29:32.173541
# Unit test for function triples_sum_to_zero
def test_triples_sum_to_zero():
    # basic cases from spec
    assert module_0.triples_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.triples_sum_to_zero([1, 3, -2, 1]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert module_0.triples_sum_to_zero([1]) == False

    # edge cases: too few elements
    assert module_0.triples_sum_to_zero([]) == False
    assert module_0.triples_sum_to_zero([0]) == False
    assert module_0.triples_sum_to_zero([0, 0]) == False
    assert module_0.triples_sum_to_zero([1, -1]) == False

    # exactly three elements
    assert module_0.triples_sum_to_zero([1, 2, -3]) == True
    assert module_0.triples_sum_to_zero([1, 2, 3]) == False
    assert module_0.triples_sum_to_zero([0, 0, 0]) == True
    assert module_0.triples_sum_to_zero([-1, 0, 1]) == True

    # pair sums to zero is not enough
    assert module_0.triples_sum_to_zero([1, -1, 5]) == False

    # triple later in list
    assert module_0.triples_sum_to_zero([5, 1, 2, -3, 7]) == True
    assert module_0.triples_sum_to_zero([-5, -1, -2, 8, 1]) == False
    assert module_0.triples_sum_to_zero([-1, -2, 3, 5]) == True


# Generated at 2026-10-25 06:29:49.096480
# Unit test for function prod_signs
def test_prod_signs():
    # empty input
    assert module_0.prod_signs([]) is None

    # all positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([1]) == 1

    # even number of negatives -> positive product
    assert module_0.prod_signs([-1, -2]) == 3
    assert module_0.prod_signs([-1, -2, 5, 5]) == 13

    # odd number of negatives -> negative product
    assert module_0.prod_signs([-1, 2]) == -3
    assert module_0.prod_signs([-1]) == -1

    # any zero -> zero result
    assert module_0.prod_signs([0, 5, -3]) == 0
    assert module_0.prod_signs([0]) == 0

# Generated at 2026-10-25 06:30:05.595258
# Unit test for function prod_signs
def test_prod_signs():
    # empty input
    assert module_0.prod_signs([]) is None

    # all positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([1]) == 1

    # even number of negatives -> positive product
    assert module_0.prod_signs([-1, -2]) == 3
    assert module_0.prod_signs([-1, -2, 5, 5]) == 13

    # odd number of negatives -> negative product
    assert module_0.prod_signs([-1, 2]) == -3
    assert module_0.prod_signs([-1]) == -1

    # any zero -> zero result
    assert module_0.prod_signs([0, 5, -3]) == 0
    assert module_0.prod_signs([0]) == 0

# Generated at 2026-10-25 06:30:21.881286
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([0, 1, -2]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

# Generated at 2026-10-25 06:30:49.520287
# Unit test for function prod_signs
def test_prod_signs():
    # empty list -> None
    assert module_0.prod_signs([]) is None

    # single values
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([0]) == 0

    # all positive -> positive sum
    assert module_0.prod_signs([1, 2, 3]) == 6

    # odd negatives -> negative sum
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # even negatives -> positive sum
    assert module_0.prod_signs([-1, -2]) == 3
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10

    # contains zero -> 0
    assert module_0.prod_signs([0, 1, 2]) == 0
    assert module_0.prod_signs([2, 0, -3]) == 0
    assert module_0.prod_signs([0, 0]) == 0

# Generated at 2026-10-25 06:30:51.937650
# Unit test for function prod_signs

# Generated at 2026-10-25 06:30:54.353745
# Unit test for function prod_signs

# Generated at 2026-10-25 06:30:56.771732
# Unit test for function prod_signs
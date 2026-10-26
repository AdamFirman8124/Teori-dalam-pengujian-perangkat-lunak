

# Generated at 2026-10-25 09:41:50.395647
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

# Generated at 2026-10-25 09:41:51.779831
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

# Generated at 2026-10-25 09:41:59.817299
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

# Generated at 2026-10-25 09:42:03.398557
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

# Generated at 2026-10-25 09:42:04.831985
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
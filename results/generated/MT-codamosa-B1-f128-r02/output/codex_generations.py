

# Generated at 2026-10-24 13:26:59.865443
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array -> None
    assert module_0.prod_signs([]) is None

    # All positive: sign = +1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Even number of negatives: sign = +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Odd number of negatives: sign = -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Contains zero -> result is 0
    assert module_0.prod_signs([-1, 0, 3]) == 0

    # Single negative
    assert module_0.prod_signs([-5]) == -5

    # Single positive
    assert module_0.prod_signs([4]) == 4


if __name__ == "__main__":
    test_prod_signs()
    print("All tests passed")

# Generated at 2026-10-24 13:27:16.467618
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([0, 1, 2]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

# Generated at 2026-10-24 13:27:32.954914
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array -> None
    assert module_0.prod_signs([]) is None

    # All positive: sign = +1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Even number of negatives: sign = +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Odd number of negatives: sign = -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Contains zero -> result is 0
    assert module_0.prod_signs([-1, 0, 3]) == 0

    # Single negative
    assert module_0.prod_signs([-5]) == -5

    # Single positive
    assert module_0.prod_signs([4]) == 4


if __name__ == "__main__":
    test_prod_signs()
    print("All tests passed")

# Generated at 2026-10-24 13:27:49.034522
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([0, 1, -2]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([5]) == 5

# Generated at 2026-10-24 13:27:50.433821
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array -> None
    assert module_0.prod_signs([]) is None

    # All positive: sign = +1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Even number of negatives: sign = +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Odd number of negatives: sign = -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Contains zero -> result is 0
    assert module_0.prod_signs([-1, 0, 3]) == 0

    # Single negative
    assert module_0.prod_signs([-5]) == -5

    # Single positive
    assert module_0.prod_signs([4]) == 4


if __name__ == "__main__":
    test_prod_signs()
    print("All tests passed")
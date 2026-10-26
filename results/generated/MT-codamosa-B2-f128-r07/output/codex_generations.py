

# Generated at 2026-10-25 11:46:39.767451
# Unit test for function prod_signs
def test_prod_signs():
    # Empty
    assert module_0.prod_signs([]) is None

    # All positive / single element
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Odd negatives -> negative, even negatives -> positive
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Contains zero -> 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -5]) == 0

    # Floats
    assert module_0.prod_signs([-1.5, 2.0]) == -3.5
    assert module_0.prod_signs([-1.5, -2.5]) == 4.0

# Generated at 2026-10-25 11:46:57.891740
# Unit test for function prod_signs
def test_prod_signs():
    # Empty
    assert module_0.prod_signs([]) is None

    # All positive / single element
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Odd negatives -> negative, even negatives -> positive
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Contains zero -> 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -5]) == 0

    # Floats
    assert module_0.prod_signs([-1.5, 2.0]) == -3.5
    assert module_0.prod_signs([-1.5, -2.5]) == 4.0

# Generated at 2026-10-25 11:47:00.308026
# Unit test for function prod_signs

# Generated at 2026-10-25 11:47:02.723078
# Unit test for function prod_signs

# Generated at 2026-10-25 11:47:05.136166
# Unit test for function prod_signs

# Generated at 2026-10-25 11:47:12.968638
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array -> None
    assert module_0.prod_signs([]) is None

    # All positive numbers: sign is +1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Even count of negatives: sign is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Odd count of negatives: sign is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Zero present: result is 0
    assert module_0.prod_signs([0, 1, -2]) == 0
    assert module_0.prod_signs([0]) == 0

    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Mixed with duplicates
    assert module_0.prod_signs([-1, -1, -1]) == -3
    assert module_0.prod_signs([-2, -2]) == 4

    # Larger mixed case
    assert module_0.prod_signs([1, -2, 3, -4, 5]) == -15

    print("All prod_signs tests passed!")


test_prod_signs()

# Generated at 2026-10-25 11:47:29.478982
# Unit test for function prod_signs
def test_prod_signs():
    # Empty
    assert module_0.prod_signs([]) is None

    # All positive / single element
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Odd negatives -> negative, even negatives -> positive
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Contains zero -> 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -5]) == 0

    # Floats
    assert module_0.prod_signs([-1.5, 2.0]) == -3.5
    assert module_0.prod_signs([-1.5, -2.5]) == 4.0


# Generated at 2026-11-02 00:27:47.784223
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2]) == 0
    assert module_0.prod_signs([-1, 0, 1]) == 0

    # All positive numbers: sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([1, 2]) == 3

    # Even number of negatives: sign product is 1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -1, -1, -1]) == 4
    assert module_0.prod_signs([1, 2, 2, 2, 4, -6, -8]) == -22  # wait: 3 negatives -> -1

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([1, 2, -3, -1, -2, -6]) == -15
    assert module_0.prod_signs([-1, 1, 1, 1]) == -4
    assert module_0.prod_signs([-1, -1, -1, 1]) == -4

    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Verify correction for the earlier case (3 negatives => negative result)
    assert module_0.prod_signs([1, 2, 2, 2, 4, -6, -8]) == -22

# Generated at 2026-11-02 00:27:52.108344
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2, 3]) == 0
    assert module_0.prod_signs([0, 0, 0]) == 0

    # All positive numbers: sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives: sign product is 1
    assert module_0.prod_signs([-1, -2, -3]) == 6
    assert module_0.prod_signs([-4, -9]) == 13
    assert module_0.prod_signs([1, -2, 2, -3]) == 8

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, 3]) == -6

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-02 00:28:02.063067
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None
    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 1]) == 0
    # All positive numbers: sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    # Even number of negatives: sign product is 1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10

# Generated at 2026-11-02 00:28:51.190643
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None

    # Test array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 2]) == 0

    # Test all positive numbers: product of signs is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Test odd number of negatives: product of signs is -1
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5

    # Test even number of negatives: product of signs is 1
    assert module_0.prod_signs([-1, 2, -3]) == 6
    assert module_0.prod_signs([-2, -4]) == 6

    # Test mixed values including zero and duplicates
    assert module_0.prod_signs([1, 1, 1, 1]) == 4
    assert module_0.prod_signs([0, 0, 0]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 00:29:16.218733
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None

    # Test array with all positive numbers (sign product = +1)
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Test array with one negative number (sign product = -1)
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Test array with two negatives (sign product = +1)
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Test array with three negatives (sign product = -1)
    assert module_0.prod_signs([-1, -2, -3]) == -18

    # Test array containing zero -> result is 0
    assert module_0.prod_signs([0, 1, -2, 3]) == 0

    # Test single positive element
    assert module_0.prod_signs([5]) == 5

    # Test single negative element
    assert module_0.prod_signs([-5]) == -5

    # Test mixed array with duplicates and zero
    assert module_0.prod_signs([-2, -2, 0, 4]) == 0

    print("All tests passed!")


test_prod_signs()
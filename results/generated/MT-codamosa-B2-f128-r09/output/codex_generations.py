

# Generated at 2026-11-02 10:15:23.737721
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-1, 1, 1, 1]) == -4
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-1, 0, 1]) == 0
    assert module_0.prod_signs([-2, -3, 4]) == -9
    assert module_0.prod_signs([1, 1, 1, 1]) == 4

test_prod_signs()
print("All tests passed!")

# Generated at 2026-11-02 10:16:05.422779
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0 (sign product is 0)
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 5]) == 0
    assert module_0.prod_signs([1, 2, 0, -3]) == 0

    # All positive numbers: sign product is +1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives: sign product is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    assert module_0.prod_signs([1, -2, 3, -4, 5]) == 15  # 2 negatives

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, 2, -3, 4, -5]) == -15  # 3 negatives

    print("All prod_signs tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 10:17:42.497151
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing 0 returns 0
    assert module_0.prod_signs([0, 1, 2]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 3]) == 0

    # All positive numbers: sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([7]) == 7

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Even number of negatives: sign product is 1
    assert module_0.prod_signs([1, -2, 2, -3]) == 8
    assert module_0.prod_signs([-1, -2]) == 3

# Generated at 2026-11-02 10:19:11.271551
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, 3]) == 0
    assert module_0.prod_signs([-2, 0, 5]) == 0

    # All positive numbers: product sign is +1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives: product sign is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

    # Odd number of negatives: product sign is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, -3, 4]) == -10

    # Mixed signs with repeated values
    assert module_0.prod_signs([-1, 1, -1, 1]) == 4
    assert module_0.prod_signs([2, 2, 2]) == 6

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-02 10:20:00.377930
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array should return None
    assert module_0.prod_signs([]) is None

    # Array containing zero should return 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, 3, -2]) == 0

    # No negative numbers: product of signs is +1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives: product of signs is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6  # even negatives
    assert module_0.prod_signs([-1, -2, -3]) == -6  # odd negatives
    assert module_0.prod_signs([-5]) == -5

    # Even number of negatives: product of signs is +1
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-2, -3]) == 5

    # Mixed with zero among negatives
    assert module_0.prod_signs([-1, 0, -3]) == 0

    # Larger example
    assert module_0.prod_signs([-1, 1, 1, 1]) == -4
    assert module_0.prod_signs([2, 4, 1, -1, -1]) == 9

    # Duplicates
    assert module_0.prod_signs([-1, -1, -1, -1]) == 4

    # Large values
    assert module_0.prod_signs([1000000, -1000000]) == 2000000
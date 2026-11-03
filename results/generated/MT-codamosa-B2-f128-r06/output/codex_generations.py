

# Generated at 2026-11-02 13:11:17.540344
# Unit test for function prod_signs
def test_prod_signs():
    # nonce:2e93921a
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # All positive numbers: sign product is +1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # One negative number: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Two negative numbers: sign product is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Three negative numbers: sign product is -1
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2]) == 0
    assert module_0.prod_signs([0, 4, 3]) == 0
    assert module_0.prod_signs([0]) == 0

    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Canonical example: 1 + 2 + 2 + 4 = 9, one negative -> -9
    assert module_0.prod_signs([1, 2, 2, -4]) == -9

    # Mixed signs, even number of negatives
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10

    # Float values
    assert module_0.prod_signs([-2.5, 3]) == -5.5

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 13:12:34.881100
# Unit test for function prod_signs
def test_prod_signs():
# nonce:880bd51f
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2]) == 0
    assert module_0.prod_signs([-1, 0, -2, 3]) == 0

    # All positive numbers: sum of magnitudes
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives: negative result
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -1, -1]) == -3

    # Even number of negatives: positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -1, 1]) == 3
    assert module_0.prod_signs([-2, -3, -4, -5]) == 14

    # Larger mixed example
    assert module_0.prod_signs([1, -4, 6, 8, -10]) == -29

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-02 13:14:19.398314
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None
    
    # Test array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2, 3]) == 0
    assert module_0.prod_signs([-1, 0, 5]) == 0
    
    # Test all positive numbers: sign is positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    
    # Test odd number of negatives: result is negative
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3]) == 6  # even negatives -> positive
    assert module_0.prod_signs([-1, -2, -3]) == -6  # odd negatives -> negative
    
    # Test single negative element
    assert module_0.prod_signs([-5]) == -5
    
    # Test mixed with duplicate values
    assert module_0.prod_signs([-2, -2, 4]) == 8
    assert module_0.prod_signs([-2, -2, -4]) == -8
    
    # Test larger numbers
    assert module_0.prod_signs([10, -20, 30]) == -60
    assert module_0.prod_signs([-10, -20, -30, 40]) == 100
    
    print("All tests passed!")

test_prod_signs()

# Generated at 2026-11-02 13:16:20.404573
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-1]) == -1
    assert module_0.prod_signs([1]) == 1
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([-1, 1, 0]) == 0
    assert module_0.prod_signs([-2, 2, 4, 8]) == -16
    assert module_0.prod_signs([1, 1, 1, 1, 1, 1, 1]) == 7
    assert module_0.prod_signs([-1, -1, -1, -1, -1, -1, -1]) == -7
    assert module_0.prod_signs([1, 1, 1, 1, 1, 1, 1, -1]) == -8
    assert module_0.prod_signs([0, 1, 1, 1, 1, 1, 1, -1]) == 0
    assert module_0.prod_signs([0, 1, 1, 1, 1, 1, -1, -1]) == 0

if __name__ == "__main__":
    test_prod_signs()
    print("All tests passed!")

# Generated at 2026-11-02 13:19:44.915970
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([1, 0, 3, -5]) == 0
    assert module_0.prod_signs([0]) == 0

    # All positive numbers: sum of absolute values
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Even number of negatives: positive sum
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Odd number of negatives: negative sum
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    # Mixed with duplicates and larger values
    assert module_0.prod_signs([-2, -2, -2, 4]) == -10
    assert module_0.prod_signs([10, -10]) == 20

    print("All prod_signs tests passed!")


if __name__ == "__main__":
    test_prod_signs()
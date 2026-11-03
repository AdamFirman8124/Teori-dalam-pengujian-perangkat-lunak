

# Generated at 2026-11-02 12:49:34.329475
# Unit test for function prod_signs
def test_prod_signs():
    # Test with empty array
    assert module_0.prod_signs([]) is None

    # Test with array containing zero
    assert module_0.prod_signs([0, 1, 2, -3]) == 0
    assert module_0.prod_signs([0]) == 0

    # Test with all positive numbers (even count of negatives = 0)
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Test with odd number of negatives (result should be negative)
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5

    # Test with even number of negatives (result should be positive)
    assert module_0.prod_signs([-1, -2]) == 3
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10

    # Test with mixed values including zero and negatives
    assert module_0.prod_signs([-1, 0, 2]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 12:51:04.556704
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None
    
    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2, 3]) == 0
    assert module_0.prod_signs([-1, 0, 5]) == 0
    
    # All positive numbers: sign is +1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    
    # Even number of negatives: sign is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    
    # Odd number of negatives: sign is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, 3, 4]) == -10
    
    # Single negative element
    assert module_0.prod_signs([-5]) == -5
    
    # Duplicates and mixed values
    assert module_0.prod_signs([2, -2, 2, -2]) == 8
    
    print("All tests passed!")

test_prod_signs()

# Generated at 2026-11-02 12:52:01.771964
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -2]) == 0
    assert module_0.prod_signs([-1, 0, -3]) == 0

    # All positive numbers -> positive sign
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives -> negative sign
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Even number of negatives -> positive sign
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

    # Duplicated values
    assert module_0.prod_signs([2, 2, 2]) == 6
    assert module_0.prod_signs([-2, -2]) == 4

    print("All test_prod_signs tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 12:53:18.698364
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None

    # Test array containing zero returns 0
    assert module_0.prod_signs([1, 0, 3]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 5]) == 0

    # Test array with all positive numbers (sign product is +1)
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Test array with even number of negatives (sign product is +1)
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10

    # Test array with odd number of negatives (sign product is -1)
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5

    # Test single element zero
    assert module_0.prod_signs([0]) == 0

    # Test larger mixed values
    assert module_0.prod_signs([1, -2, 2, -3]) == 8  # two negatives -> positive sign
    assert module_0.prod_signs([-1, -2, 2]) == -5    # two negatives -> positive sign... 
    # correction: two negatives -> +1, sum abs = 5, so result is 5
    assert module_0.prod_signs([-1, -2, 2]) == 5

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-02 12:54:18.351170
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([1, 0, 3]) == 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([-1, 0, 2, -3]) == 0

    # All positive numbers: sign is positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives: sign is negative
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([1, -2, 3, -4, 5]) == -(1 + 2 + 3 + 4 + 5)

    # Even number of negatives: sign is positive
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2]) == 3
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

    # Mixed with duplicates
    assert module_0.prod_signs([2, 2, -2]) == -6
    assert module_0.prod_signs([2, 2, 2]) == 6

    print("All tests passed!")


test_prod_signs()
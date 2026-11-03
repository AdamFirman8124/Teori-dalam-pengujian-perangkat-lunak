

# Generated at 2026-11-02 12:56:10.273428
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2, 3]) == 0
    assert module_0.prod_signs([-1, 0, 2]) == 0
    assert module_0.prod_signs([-1, -2, 0]) == 0

    # All positive numbers: sign product is +1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Even number of negatives: sign product is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

    # Odd number of negatives: sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, -2, 3, 4, -5]) == -15

    # Single element cases
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([7]) == 7
    assert module_0.prod_signs([-7]) == -7

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-02 12:57:31.330542
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None
    
    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1, 2, -4]) == 0
    assert module_0.prod_signs([0]) == 0
    
    # Single negative number -> negative result
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    
    # All positive numbers -> positive result
    assert module_0.prod_signs([1, 2, 3]) == 6
    
    # Odd count of negatives -> negative result
    assert module_0.prod_signs([-1, -2, -3]) == -6
    
    # Even count of negatives -> positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    
    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5
    
    # Negative-only array with even count
    assert module_0.prod_signs([-2, -3]) == 5
    
    # Mixed with zero and negatives -> 0
    assert module_0.prod_signs([-1, -2, 0]) == 0
    
    # Larger mixed case
    assert module_0.prod_signs([1, -2, 3, -4, 5]) == -15

# Generated at 2026-11-02 12:58:33.195003
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero -> sign product is 0
    assert module_0.prod_signs([1, 0, 2, 3]) == 0
    assert module_0.prod_signs([-1, 0, -2]) == 0
    assert module_0.prod_signs([0]) == 0

    # All positive numbers -> sum of absolute values
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives -> negative result
    assert module_0.prod_signs([1, -2, 3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, 2, -3, 4, -5]) == -(1 + 2 + 3 + 4 + 5)

    # Even number of negatives -> positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10
    assert module_0.prod_signs([-2, -4]) == 6

    # Mixed with duplicates and zero
    assert module_0.prod_signs([-1, 0, -1]) == 0

    # Large values
    assert module_0.prod_signs([100, -200, 300]) == -600

    print("All prod_signs tests passed!")


test_prod_signs()

# Generated at 2026-11-02 12:59:55.941954
# Unit test for function prod_signs
def test_prod_signs():
    # Test with empty array
    assert module_0.prod_signs([]) is None
    
    # Test with array containing zero
    assert module_0.prod_signs([0, 1, 2, -3]) == 0
    assert module_0.prod_signs([0]) == 0
    
    # Test with all positive numbers
    assert module_0.prod_signs([1, 2, 3]) == 6
    
    # Test with odd number of negative numbers
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    
    # Test with even number of negative numbers
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10
    
    # Test with single element
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5
    
    # Test with large numbers
    assert module_0.prod_signs([100, -200, 300]) == 600
    
    print("All tests passed!")

test_prod_signs()

# Generated at 2026-11-02 13:01:52.952237
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([1, 2, 0, -4]) == 0

    # No negatives: sign product is positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([1, 2, 2, 4]) == 9

    # Odd number of negatives: sign product is negative
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6

    # Even number of negatives: sign product is positive
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10

    # Single element cases
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()
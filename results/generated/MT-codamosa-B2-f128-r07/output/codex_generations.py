

# Generated at 2026-11-01 20:07:55.814617
# Unit test for function prod_signs
def test_prod_signs():
    # Test with an empty list - should return None
    assert module_0.prod_signs([]) == None

    # Test with all positive numbers - sign product is 1
    assert module_0.prod_signs([1, 2, 3]) == 6

    # Test with negative numbers - two negatives means sign product is +1
    assert module_0.prod_signs([-1, -2, 3]) == 6

    # Test with odd number of negatives - sign product is -1
    assert module_0.prod_signs([-1, 2, 3]) == -6

    # Test with zero in the list - result should be 0
    assert module_0.prod_signs([0, -1, 2]) == 0

    # Test with single positive element
    assert module_0.prod_signs([5]) == 5

    # Test with single negative element
    assert module_0.prod_signs([-5]) == -5

    # Test with larger mixed values
    assert module_0.prod_signs([-10, -20, 30, -40]) == 100

    print("All tests passed!")


if __name__ == "__main__":
    test_prod_signs()

# Generated at 2026-11-01 20:08:25.612285
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None

    # Array containing 0 returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, -3, 2]) == 0

    # All positive numbers: sign is positive
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5

    # Odd number of negatives: negative result
    assert module_0.prod_signs([-1, 2, 3]) == -6
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([1, 2, 2, -4]) == -9

    # Even number of negatives: positive result
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2]) == 3

    # Single negative element
    assert module_0.prod_signs([-7]) == -7

    # Large values
    assert module_0.prod_signs([100, -200, 300]) == -600

    print("All tests passed!")


test_prod_signs()

# Generated at 2026-11-01 20:08:48.447878
# Unit test for function prod_signs
def test_prod_signs():
    # Empty array returns None
    assert module_0.prod_signs([]) is None
    # Array containing zero returns 0
    assert module_0.prod_signs([0, 1]) == 0
    assert module_0.prod_signs([0, -2, 3]) == 0
    # All positive numbers: product of signs is 1
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    # Odd number of negatives: product of signs is -1
    assert module_0.prod_signs([1, 2, 2, -4]) == -9
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    # Even number of negatives: product of signs is 1
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, -2, -3, -4]) == 10

# Generated at 2026-11-01 20:09:13.752370
# Unit test for function prod_signs
def test_prod_signs():
    # Test with an empty array
    assert module_0.prod_signs([]) == None
    
    # Test with all positive numbers
    assert module_0.prod_signs([1, 2, 3]) == 6
    
    # Test with all negative numbers
    assert module_0.prod_signs([-1, -2, -3]) == -6
    
    # Test with mixed positive and negative numbers
    assert module_0.prod_signs([-1, 2, -3]) == 6
    
    # Test with a zero in the array
    assert module_0.prod_signs([-1, 0, 3]) == 0
    
    # Test with single positive element
    assert module_0.prod_signs([5]) == 5
    
    # Test with single negative element
    assert module_0.prod_signs([-5]) == -5
    
    # Test with only zero
    assert module_0.prod_signs([0]) == 0
    
    print("All tests passed!")

test_prod_signs()

# Generated at 2026-11-01 20:09:31.777833
# Unit test for function prod_signs
def test_prod_signs():
    # Test empty array returns None
    assert module_0.prod_signs([]) is None
    
    # Test array containing zero returns 0
    assert module_0.prod_signs([0]) == 0
    assert module_0.prod_signs([1, 0, 2, 3]) == 0
    
    # Test all positive numbers
    assert module_0.prod_signs([1, 2, 3]) == 6
    assert module_0.prod_signs([5]) == 5
    
    # Test even number of negative elements (positive product)
    assert module_0.prod_signs([-1, -2, 3]) == 6
    assert module_0.prod_signs([-1, 2, -3, 4]) == 10
    
    # Test odd number of negative elements (negative product)
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([-5]) == -5
    assert module_0.prod_signs([-1, 2, 3]) == -6
    
    # Test single negative element
    assert module_0.prod_signs([-7]) == -7
    
    # Test mixed with zero and negatives (zero dominates)
    assert module_0.prod_signs([-1, 0, -2]) == 0
    
    print("All prod_signs tests passed!")

test_prod_signs()
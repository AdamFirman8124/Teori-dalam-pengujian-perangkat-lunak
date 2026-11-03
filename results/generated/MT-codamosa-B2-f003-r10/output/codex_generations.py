

# Generated at 2026-11-02 18:40:16.613650
# Unit test for function below_zero
def test_below_zero():
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([1, 2, -4, 5]) == True
    assert module_0.below_zero([1, -1, 2, -2]) == False
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([]) == False
    assert module_0.below_zero([0, 0, 0]) == False
    assert module_0.below_zero([5, -10]) == True
    assert module_0.below_zero([10, -5, 3, -8]) == True

# Generated at 2026-11-02 18:42:16.137868
# Unit test for function below_zero
def test_below_zero():
    # Test case where balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) is True
    
    # Test case where balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) is False
    
    # Test case with empty list
    assert module_0.below_zero([]) is False
    
    # Test case where first operation makes balance negative
    assert module_0.below_zero([-1]) is True
    
    # Test case where balance goes to exactly zero (not below)
    assert module_0.below_zero([1, -1]) is False
    
    # Test case where balance goes negative then positive
    assert module_0.below_zero([1, -2, 5]) is True
    
    # Test case with all positive numbers
    assert module_0.below_zero([1, 2, 3, 4, 5]) is False
    
    # Test case with all negative numbers
    assert module_0.below_zero([-1, -2, -3]) is True
    
    # Test case where balance goes below zero only after multiple operations
    assert module_0.below_zero([10, -5, -6]) is True
    
    # Test case where balance drops to zero then goes negative
    assert module_0.below_zero([5, -5, -1]) is True
    
    # Test case with zero operations
    assert module_0.below_zero([0, 0, 0]) is False
    
    # Test case with large numbers
    assert module_0.below_zero([1000000, -2000000]) is True

# Generated at 2026-11-02 18:44:05.061850
# Unit test for function below_zero
def test_below_zero():
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True
    # Empty list, no operations
    assert module_0.below_zero([]) == False
    # Balance hits exactly zero, never below
    assert module_0.below_zero([1, -1]) == False
    # Starts negative immediately
    assert module_0.below_zero([-1]) == True
    # Goes below then recovers, should still return True
    assert module_0.below_zero([5, -10, 10]) == True
    # Single positive operation
    assert module_0.below_zero([10]) == False
    # Ends at zero after dipping negative
    assert module_0.below_zero([3, -5, 2]) == True
    # All positive operations
    assert module_0.below_zero([1, 1, 1, 1]) == False
    # Large numbers
    assert module_0.below_zero([1000000, -2000000]) == True

# Generated at 2026-11-02 18:45:07.701140
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero at some point
    assert module_0.below_zero([1, 2, -4, 5]) is True

    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) is False

    # Empty operations list
    assert module_0.below_zero([]) is False

    # Single negative operation drops balance below zero
    assert module_0.below_zero([-1]) is True

    # Single positive operation
    assert module_0.below_zero([5]) is False

    # Balance drops below zero then recovers — still True
    assert module_0.below_zero([10, -15, 20]) is True

    # Balance reaches exactly zero (not below) — False
    assert module_0.below_zero([5, -5]) is False

    # Balance goes negative immediately then stays positive
    assert module_0.below_zero([-2, 5, 3]) is True

    # Multiple dips below zero
    assert module_0.below_zero([3, -5, 10, -12]) is True

    # Large values
    assert module_0.below_zero([1000000, -1000001]) is True
    assert module_0.below_zero([1000000, -1000000]) is False

    # All zeros — never below zero
    assert module_0.below_zero([0, 0, 0]) is False

    # Negative result only at the very end
    assert module_0.below_zero([1, 1, 1, -5]) is True


test_below_zero()
print("All tests passed!")

# Generated at 2026-11-02 18:46:38.426535
# Unit test for function below_zero
def test_below_zero():
    # Test case 1: balance goes below zero
    assert module_0.below_zero([1, 2, -3]) == True

    # Test case 2: balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test case 3: empty list
    assert module_0.below_zero([]) == False

    # Test case 4: single negative operation
    assert module_0.below_zero([-1]) == True

    # Test case 5: single positive operation
    assert module_0.below_zero([5]) == False

    # Test case 6: balance reaches exactly zero (not below)
    assert module_0.below_zero([5, -5]) == False

    # Test case 7: balance goes below zero after several operations
    assert module_0.below_zero([10, -5, -6]) == True

    # Test case 8: dips below zero then recovers (still returns True)
    assert module_0.below_zero([3, -5, 10]) == True

    # Test case 9: all zeros
    assert module_0.below_zero([0, 0, 0]) == False

    # Test case 10: large numbers
    assert module_0.below_zero([1000000, -1000001]) == True

    # Test case 11: negative result from the start
    assert module_0.below_zero([-100, 50]) == True

    # Test case 12: alternating operations that stay non-negative
    assert module_0.below_zero([1, -1, 1, -1, 1]) == False
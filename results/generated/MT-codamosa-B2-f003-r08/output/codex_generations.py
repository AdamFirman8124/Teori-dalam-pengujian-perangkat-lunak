

# Generated at 2026-11-02 08:46:58.445073
# Unit test for function below_zero
def test_below_zero():
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True
    # Empty list, no operations
    assert module_0.below_zero([]) == False
    # Single negative operation
    assert module_0.below_zero([-1]) == True
    # Balance drops to exactly zero (not below)
    assert module_0.below_zero([1, -1]) == False
    # Balance drops below zero after several operations
    assert module_0.below_zero([10, 5, -8, -10]) == True
    # Balance goes below and comes back but should still return True
    assert module_0.below_zero([5, -10, 20]) == True
    # All positive operations
    assert module_0.below_zero([100, 200, 300]) == False
    # Zero operations only
    assert module_0.below_zero([0, 0, 0]) == False

# Generated at 2026-11-02 08:47:07.316653
# Unit test for function below_zero
def test_below_zero():
    # Test with operations that drop balance below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Test with operations that never go below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test with empty list
    assert module_0.below_zero([]) == False

    # Test with a single negative operation
    assert module_0.below_zero([-1]) == True

    # Test with balance hitting exactly zero (not below)
    assert module_0.below_zero([1, -1]) == False

    # Test where balance goes negative then recovers
    assert module_0.below_zero([5, -10, 20]) == True

    # Test with all positive operations
    assert module_0.below_zero([10, 20, 30]) == False

    # Test with zero operations included
    assert module_0.below_zero([0, 0, -1]) == True

    # Test with large numbers
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -999999]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 08:47:12.924867
# Unit test for function below_zero
def test_below_zero():
    # Empty list: no operations, balance never drops below zero
    assert module_0.below_zero([]) is False

    # All positive operations: balance stays positive
    assert module_0.below_zero([1, 2, 3]) is False

    # Balance drops below zero mid-sequence
    assert module_0.below_zero([1, 2, -4, 5]) is True

    # Balance reaches exactly zero but never below
    assert module_0.below_zero([1, 2, -3]) is False

    # Single negative operation
    assert module_0.below_zero([-1]) is True

    # Single zero operation
    assert module_0.below_zero([0]) is False

    # Balance returns to exactly zero, never negative
    assert module_0.below_zero([1, -1]) is False

    # Large positive then larger negative
    assert module_0.below_zero([100, -101]) is True

    # Negative at the very end
    assert module_0.below_zero([5, 5, -20]) is True

    # Multiple dips below zero
    assert module_0.below_zero([-2, 3, -4]) is True

    # Long sequence staying non-negative
    assert module_0.below_zero([1, 1, 1, 1, -2, -2]) is False

    # Early dip then recovery still returns True
    assert module_0.below_zero([10, -15, 100]) is True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 08:47:18.722024
# Unit test for function below_zero
def test_below_zero():
    # Test case 1: Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Test case 2: Balance goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Test case 3: Empty list - no operations, never below zero
    assert module_0.below_zero([]) == False

    # Test case 4: Single positive operation
    assert module_0.below_zero([5]) == False

    # Test case 5: Single negative operation
    assert module_0.below_zero([-1]) == True

    # Test case 6: Balance goes to exactly zero but not below
    assert module_0.below_zero([1, -1]) == False

    # Test case 7: Balance goes below zero but recovers
    assert module_0.below_zero([5, -10, 20]) == True

    # Test case 8: Starts with deposit then withdrawal to zero
    assert module_0.below_zero([10, -10]) == False

    # Test case 9: First operation goes below zero
    assert module_0.below_zero([-5, 10]) == True

    # Test case 10: Large numbers
    assert module_0.below_zero([1000000, -2000000]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 08:47:27.532231
# Unit test for function below_zero
def test_below_zero():
    # Empty list: balance never changes, stays at 0
    assert module_0.below_zero([]) is False

    # Balance goes negative on first operation
    assert module_0.below_zero([-1]) is True

    # Balance stays positive throughout
    assert module_0.below_zero([1, 2, 3]) is False

    # Balance goes negative partway through
    assert module_0.below_zero([1, 2, -4, 5]) is True

    # Balance drops to exactly zero but never below
    assert module_0.below_zero([1, 2, -3]) is False

    # Balance dips below zero then recovers — still True
    assert module_0.below_zero([5, -6, 10]) is True

    # Balance ends negative
    assert module_0.below_zero([1, -2]) is True

    # Balance touches zero multiple times without going below
    assert module_0.below_zero([1, -1, 1, -1]) is False

    # Large values
    assert module_0.below_zero([1000000, -2000000]) is True
    assert module_0.below_zero([1000000, -1000000, 1]) is False
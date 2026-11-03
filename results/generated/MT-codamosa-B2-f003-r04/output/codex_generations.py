

# Generated at 2026-11-02 11:23:38.616248
# Unit test for function below_zero
def test_below_zero():
    # Empty list: balance never changes, stays at zero (not below)
    assert module_0.below_zero([]) == False

    # Only positive operations: balance never drops below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance drops below zero at the end of the sequence
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance drops below zero in the middle, then recovers
    assert module_0.below_zero([10, -15, 20]) == True

    # Balance reaches exactly zero but never goes below it
    assert module_0.below_zero([1, 2, -3]) == False

    # Single negative operation immediately drops below zero
    assert module_0.below_zero([-1]) == True

    # Single positive operation never drops below zero
    assert module_0.below_zero([5]) == False

    # Larger values crossing zero late in the sequence
    assert module_0.below_zero([100, 50, -200]) == True

    print("All below_zero tests passed!")

# Generated at 2026-11-02 11:26:32.429045
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -3]) == True
    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False
    # Empty list, no operations
    assert module_0.below_zero([]) == False
    # Single negative operation
    assert module_0.below_zero([-1]) == True
    # Balance drops to exactly zero, not below
    assert module_0.below_zero([1, -1]) == False
    # Balance goes below zero then recovers, should still be True
    assert module_0.below_zero([1, -2, 5, 10]) == True
    # Large positive numbers never below zero
    assert module_0.below_zero([100, -50, -50]) == False
    # First operation drops below zero immediately
    assert module_0.below_zero([-5, 10]) == True
    # Balance stays at zero boundary
    assert module_0.below_zero([5, -5, 5, -5]) == False

# Generated at 2026-11-02 11:29:21.950626
# Unit test for function below_zero
def test_below_zero():
    # Operations that dip below zero
    assert module_0.below_zero([1, 2, -3]) is True
    assert module_0.below_zero([1, 2, -4, 5]) is True
    assert module_0.below_zero([-1]) is True
    assert module_0.below_zero([5, -10]) is True

    # Operations that never go below zero
    assert module_0.below_zero([]) is False
    assert module_0.below_zero([1, 2, 3]) is False
    assert module_0.below_zero([1, -1, 1, -1]) is False
    assert module_0.below_zero([0, 0, 0]) is False
    assert module_0.below_zero([10, -5, -5]) is False  # reaches exactly zero

    # Recovery after going below zero still returns True
    assert module_0.below_zero([2, -3, 10]) is True

    # Single positive / zero values
    assert module_0.below_zero([100]) is False
    assert module_0.below_zero([0]) is False

    # Large values
    assert module_0.below_zero([1000000, -2000000]) is True
    assert module_0.below_zero([1000000, -1000000]) is False

    # Order matters: same values, different results
    assert module_0.below_zero([-3, 1, 2]) is True
    assert module_0.below_zero([1, 2, -3]) is True
    assert module_0.below_zero([1, 2, 3, -6]) is False
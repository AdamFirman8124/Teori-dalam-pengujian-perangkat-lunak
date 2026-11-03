

# Generated at 2026-11-02 16:56:09.365356
# Unit test for function below_zero
def test_below_zero():
    # Empty operations list - balance never changes
    assert module_0.below_zero([]) == False

    # Only positive operations - never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Simple case: goes below zero
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance touches exactly zero but never goes below
    assert module_0.below_zero([1, -1]) == False
    assert module_0.below_zero([5, -5]) == False

    # Single negative operation drops below zero immediately
    assert module_0.below_zero([-1]) == True

    # Goes below zero early, then recovers - still True
    assert module_0.below_zero([1, -2, 10, 20]) == True

    # Goes below zero only at the very end
    assert module_0.below_zero([10, 10, -25]) == True

    # Large values
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -1000000]) == False

    # Mixed sequence staying non-negative throughout
    assert module_0.below_zero([2, 3, -4, 1]) == False

# Generated at 2026-11-02 16:57:31.826433
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero at the end
    assert module_0.below_zero([1, 2, 3]) == False

    # Balance goes below zero in the middle
    assert module_0.below_zero([1, 2, -4, 5]) == True

    # Balance goes below zero with first operation
    assert module_0.below_zero([-1]) == True

    # Balance exactly reaches zero but never below
    assert module_0.below_zero([1, 2, -3]) == False

    # Empty list - no operations, never below zero
    assert module_0.below_zero([]) == False

    # Balance drops below zero then recovers
    assert module_0.below_zero([5, -10, 20]) == True

    # Multiple dips below zero
    assert module_0.below_zero([1, -2, 5, -10]) == True

    # All positive operations
    assert module_0.below_zero([10, 20, 30]) == False

    # All negative operations
    assert module_0.below_zero([-1, -2, -3]) == True

    # Single zero operation
    assert module_0.below_zero([0]) == False

    # Balance touches zero exactly then goes positive
    assert module_0.below_zero([5, -5, 3]) == False

    # Large values
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -999999]) == False

    print("All test cases passed!")


# Run tests
if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 16:59:03.680719
# Unit test for function below_zero
def test_below_zero():
    # Balance drops below zero at the end
    assert module_0.below_zero([1, 2, -3]) is True

    # Balance never drops below zero
    assert module_0.below_zero([1, 2, 3]) is False

    # Empty operations list
    assert module_0.below_zero([]) is False

    # Balance reaches exactly zero, never below
    assert module_0.below_zero([1, -1]) is False

    # First operation is negative
    assert module_0.below_zero([-1]) is True

    # Drops below zero mid-sequence then recovers
    assert module_0.below_zero([5, -10, 20]) is False and module_0.below_zero([5, -6, 20]) is True

    # All zeros
    assert module_0.below_zero([0, 0, 0]) is False

    # Single positive operation
    assert module_0.below_zero([10]) is False

    # Multiple dips below zero
    assert module_0.below_zero([-1, 5, -10]) is True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-02 17:00:14.014273
# Unit test for function below_zero
def test_below_zero():
    # Balance goes below zero
    assert module_0.below_zero([1, 2, -3]) == True

    # Balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Empty list of operations
    assert module_0.below_zero([]) == False

    # Immediately goes negative
    assert module_0.below_zero([-1]) == True

    # Balance touches zero but never goes below
    assert module_0.below_zero([5, -5, 3]) == False

    # Goes below zero then recovers
    assert module_0.below_zero([5, -10, 10]) == True

    # All zeros
    assert module_0.below_zero([0, 0, 0]) == False

    # Large values
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -1000000, 1]) == False

# Generated at 2026-11-02 17:01:23.212590
# Unit test for function below_zero
def test_below_zero():
    # Empty list: no operations, balance never drops below zero
    assert module_0.below_zero([]) is False

    # All positive operations: balance stays non-negative
    assert module_0.below_zero([1, 2, 3]) is False

    # Balance drops below zero at some point
    assert module_0.below_zero([1, 2, -4, 5]) is True

    # Balance reaches exactly zero but never goes below
    assert module_0.below_zero([1, -1, 2, -2]) is False

    # First operation immediately drops below zero
    assert module_0.below_zero([-1]) is True

    # Balance goes negative then recovers, but still returns True
    assert module_0.below_zero([5, -10, 20]) is True

    # Balance ends at zero exactly, never negative
    assert module_0.below_zero([3, -3]) is False

    # Large values
    assert module_0.below_zero([1000000, -2000000]) is True
    assert module_0.below_zero([1000000, -999999]) is False

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()